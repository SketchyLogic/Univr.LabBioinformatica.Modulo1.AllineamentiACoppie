"""
Needleman-Wunsch visual simulator (general recurrence + affine gaps)
====================================================================

A Tkinter GUI that walks through global alignment one phase at a time:

    Step 1 - type the two sequences (+ scores) into the inputs
    Step 2 - click "Init"      -> build the matrix + fill row 0 / column 0
    Step 3 - click "Fill"      -> compute every interior cell (recurrence)
    Step 4 - click "Traceback" -> walk back from the corner -> the alignment

This version uses the GENERAL recurrence, where a gap may have ANY length in
one step (the original 1970 form), with an AFFINE gap penalty:

    S(i,j) = max [ S(i-1,j-1) + s(a_i,b_j) ,            # diagonal: pair, no gap
                   max_{k>=1} S(i-k, j) + W(k) ,         # gap of length k in TOP seq
                   max_{l>=1} S(i, j-l) + W(l) ]         # gap of length l in SIDE seq
    W(L) = gap_open + (L-1) * gap_extend                 # affine gap cost

So the candidates for cell (i,j) are NOT just three neighbours: they are the
diagonal cell, every cell straight up the column (gaps of length 1,2,3,...),
and every cell straight left along the row. Click a cell in the Fill step to
see all of them, which one(s) win, and the optimal sub-alignment that the cell
represents (optimal substructure made visible).

Convention (matches the wiki): Seq 1 along the TOP (columns), Seq 2 down the
SIDE (rows). diagonal = pair; vertical = gap in top seq; horizontal = gap in
side seq.

Run with:  python nw_visual.py   (standard library only)
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------------------------------------------------------
# Look & feel
# ----------------------------------------------------------------------------
CELL = 50
MARGIN = 24
SEQFONT = ("Consolas", 13, "bold")
VALFONT = ("Consolas", 12)
HINTFONT = ("Segoe UI", 9)
MONO = ("Consolas", 10)

C = {
    "grid":      "#c7ccd1",
    "init":      "#fdf3d0",   # row 0 / col 0 baseline cells
    "interior":  "#ffffff",
    "selected":  "#ffca28",   # the cell you clicked
    "pred":      "#66bb6a",   # winning predecessor(s)
    "cand_diag": "#e1bee7",   # diagonal candidate
    "cand_up":   "#bbdefb",   # vertical candidates (column above)
    "cand_left": "#ffe0b2",   # horizontal candidates (row to the left)
    "pathcell":  "#90caf9",   # cells on the optimal traceback path
    "text":      "#1b1b1b",
    "arrow":     "#37474f",
    "patharrow": "#1565c0",
}

NEG_INF = float("-inf")


class NWApp:
    def __init__(self, root):
        self.root = root
        root.title("Needleman-Wunsch - visual stepper (affine gaps)")

        self.stage = "input"          # input -> init -> fill -> traceback
        self.selected = None          # (i, j) clicked cell
        self.pred_cells = []          # winning predecessors [(i, j, dir), ...]
        self.cand_diag = None         # diagonal candidate cell
        self.cand_up = []             # vertical candidate cells
        self.cand_left = []           # horizontal candidate cells
        self.path = set()             # all cells the optimal path passes through
        self.path_jumps = []          # [(from, to), ...] for path arrows

        self._build_controls()
        self._build_body()
        self._build_footer()
        self._update_buttons()
        self._set_status("Step 1 - enter two sequences, then click 'Init'.")

    # ------------------------------------------------------------------ UI
    def _build_controls(self):
        bar = ttk.Frame(self.root, padding=8)
        bar.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(bar, text="Seq 1 (top):").grid(row=0, column=0, sticky="e")
        self.e_seq1 = ttk.Entry(bar, width=20, font=("Consolas", 11))
        self.e_seq1.insert(0, "GATTACA")
        self.e_seq1.grid(row=0, column=1, padx=(2, 10))

        ttk.Label(bar, text="Seq 2 (side):").grid(row=0, column=2, sticky="e")
        self.e_seq2 = ttk.Entry(bar, width=20, font=("Consolas", 11))
        self.e_seq2.insert(0, "GCATGCU")
        self.e_seq2.grid(row=0, column=3, padx=(2, 10))

        sc = ttk.Frame(bar)
        sc.grid(row=0, column=4, padx=(4, 10))
        self.e_match = self._score_entry(sc, "match", "1", 0)
        self.e_mis = self._score_entry(sc, "mismatch", "-1", 2)
        self.e_open = self._score_entry(sc, "gap_open", "-2", 4)
        self.e_ext = self._score_entry(sc, "gap_extend", "-1", 6)

        bb = ttk.Frame(bar)
        bb.grid(row=0, column=5)
        self.b_init = ttk.Button(bb, text="2 - Init", command=self.on_init)
        self.b_fill = ttk.Button(bb, text="3 - Fill", command=self.on_fill)
        self.b_tb = ttk.Button(bb, text="4 - Traceback", command=self.on_traceback)
        self.b_reset = ttk.Button(bb, text="Reset", command=self.on_reset)
        for b in (self.b_init, self.b_fill, self.b_tb, self.b_reset):
            b.pack(side=tk.LEFT, padx=2)

    def _score_entry(self, parent, label, default, col):
        ttk.Label(parent, text=label + ":").grid(row=0, column=col, sticky="e")
        e = ttk.Entry(parent, width=4)
        e.insert(0, default)
        e.grid(row=0, column=col + 1, padx=(2, 8))
        return e

    def _build_body(self):
        mid = ttk.Frame(self.root)
        mid.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # --- info panel (right) ---
        info_wrap = ttk.Frame(mid)
        info_wrap.pack(side=tk.RIGHT, fill=tk.Y)
        self.info = tk.Text(info_wrap, width=46, font=MONO, wrap="none",
                            background="#fcfcfc", relief=tk.FLAT, padx=8, pady=6,
                            state=tk.DISABLED)
        isb = ttk.Scrollbar(info_wrap, orient=tk.VERTICAL, command=self.info.yview)
        self.info.configure(yscrollcommand=isb.set)
        self.info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        isb.pack(side=tk.RIGHT, fill=tk.Y)
        self.info.tag_configure("h1", font=("Consolas", 11, "bold"), foreground="#0d47a1")
        self.info.tag_configure("win", font=("Consolas", 10, "bold"), foreground="#1b5e20")
        self.info.tag_configure("dim", foreground="#8a8a8a")
        self.info.tag_configure("sub", font=("Consolas", 11, "bold"), foreground="#4a148c")

        # --- canvas (left) ---
        canvas_wrap = ttk.Frame(mid)
        canvas_wrap.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(canvas_wrap, background="white", highlightthickness=0)
        hbar = ttk.Scrollbar(canvas_wrap, orient=tk.HORIZONTAL, command=self.canvas.xview)
        vbar = ttk.Scrollbar(canvas_wrap, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        vbar.grid(row=0, column=1, sticky="ns")
        hbar.grid(row=1, column=0, sticky="ew")
        canvas_wrap.rowconfigure(0, weight=1)
        canvas_wrap.columnconfigure(0, weight=1)
        self.canvas.bind("<Button-1>", self.on_click)

    def _build_footer(self):
        foot = ttk.Frame(self.root, padding=(8, 4))
        foot.pack(side=tk.BOTTOM, fill=tk.X)
        self.status = ttk.Label(foot, text="", font=HINTFONT, foreground="#37474f")
        self.status.pack(side=tk.TOP, anchor="w")
        self.align_box = tk.Text(foot, height=4, font=("Consolas", 12),
                                 background="#fbfbfb", relief=tk.FLAT, state=tk.DISABLED)
        self.align_box.pack(side=tk.TOP, fill=tk.X, pady=(4, 0))

    # -------------------------------------------------------------- helpers
    def _set_status(self, msg):
        self.status.configure(text=msg)

    def _set_align(self, msg):
        self.align_box.configure(state=tk.NORMAL)
        self.align_box.delete("1.0", tk.END)
        self.align_box.insert(tk.END, msg)
        self.align_box.configure(state=tk.DISABLED)

    def _ins(self, text, tag=None):
        if tag:
            self.info.insert(tk.END, text, tag)
        else:
            self.info.insert(tk.END, text)

    def _set_info(self, text):
        self.info.configure(state=tk.NORMAL)
        self.info.delete("1.0", tk.END)
        self.info.insert(tk.END, text)
        self.info.configure(state=tk.DISABLED)

    def _update_buttons(self):
        st = self.stage
        self.b_init.configure(state=(tk.NORMAL if st == "input" else tk.DISABLED))
        self.b_fill.configure(state=(tk.NORMAL if st == "init" else tk.DISABLED))
        self.b_tb.configure(state=(tk.NORMAL if st == "fill" else tk.DISABLED))
        ent = tk.NORMAL if st == "input" else tk.DISABLED
        for e in (self.e_seq1, self.e_seq2, self.e_match, self.e_mis,
                  self.e_open, self.e_ext):
            e.configure(state=ent)

    def _read_int(self, entry, name):
        try:
            return int(entry.get().strip())
        except ValueError:
            raise ValueError(f"Score '{name}' must be an integer.")

    def _W(self, length):
        """Affine penalty for a gap of the given length."""
        return self.gap_open + (length - 1) * self.gap_extend

    def _sub(self, i, j):
        """Substitution score for pairing seq2[i-1] with seq1[j-1]."""
        return self.match if self.seq2[i - 1] == self.seq1[j - 1] else self.mismatch

    # ----------------------------------------------------------- step 2: init
    def on_init(self):
        s1 = "".join(self.e_seq1.get().split()).upper()
        s2 = "".join(self.e_seq2.get().split()).upper()
        if not s1 or not s2:
            messagebox.showwarning("Missing input", "Please enter both sequences.")
            return
        if len(s1) > 40 or len(s2) > 40:
            messagebox.showwarning("Too long",
                                   "Keep each sequence <= 40 characters for a readable grid.")
            return
        try:
            self.match = self._read_int(self.e_match, "match")
            self.mismatch = self._read_int(self.e_mis, "mismatch")
            self.gap_open = self._read_int(self.e_open, "gap_open")
            self.gap_extend = self._read_int(self.e_ext, "gap_extend")
        except ValueError as ex:
            messagebox.showerror("Bad score", str(ex))
            return

        self.seq1, self.seq2 = s1, s2
        self.n, self.m = len(s1), len(s2)

        self.H = [[None] * (self.n + 1) for _ in range(self.m + 1)]
        self.P = [[[] for _ in range(self.n + 1)] for _ in range(self.m + 1)]

        # Affine baseline: row 0 / col 0 are ONE gap of growing length => W(len)
        self.H[0][0] = 0
        for j in range(1, self.n + 1):
            self.H[0][j] = self._W(j)
        for i in range(1, self.m + 1):
            self.H[i][0] = self._W(i)

        self._clear_selection()
        self.path = set()
        self.path_jumps = []
        self.stage = "init"
        self._set_align("")
        self._update_buttons()
        self.draw()
        self._set_info("Step 2 - Init done.\n\nRow 0 and column 0 hold one affine "
                       "gap of growing length:\n   W(L) = gap_open + (L-1)*gap_extend\n\n"
                       "Now click 'Fill'.")
        self._set_status("Step 2 done - affine gap baseline laid down. Click 'Fill'.")

    # ----------------------------------------------------------- step 3: fill
    def on_fill(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                best = NEG_INF
                winners = []

                def consider(direction, pi, pj, length, total):
                    nonlocal best, winners
                    if total > best:
                        best = total
                        winners = [(direction, pi, pj, length)]
                    elif total == best:
                        winners.append((direction, pi, pj, length))

                consider("diag", i - 1, j - 1, 1, self.H[i - 1][j - 1] + self._sub(i, j))
                for k in range(1, i + 1):                       # gap in TOP seq
                    consider("up", i - k, j, k, self.H[i - k][j] + self._W(k))
                for l in range(1, j + 1):                       # gap in SIDE seq
                    consider("left", i, j - l, l, self.H[i][j - l] + self._W(l))

                self.H[i][j] = best
                self.P[i][j] = winners

        self.stage = "fill"
        self._clear_selection()
        self._update_buttons()
        self.draw()
        self._show_legend()
        self._set_status("Step 3 done - click any cell to expand the recurrence "
                         "and see its optimal sub-alignment, then click 'Traceback'.")

    # ------------------------------------------------------- step 4: traceback
    def on_traceback(self):
        ci, cj = self.m, self.n
        visited = {(ci, cj)}
        jumps = []
        top, bot = [], []
        while ci > 0 or cj > 0:
            d, pi, pj, length = self._best_move(ci, cj)
            if d == "up":
                for r in range(pi, ci):
                    visited.add((r, cj))
            elif d == "left":
                for c in range(pj, cj):
                    visited.add((ci, c))
            jumps.append(((ci, cj), (pi, pj)))
            self._emit(ci, cj, (d, pi, pj, length), top, bot)
            ci, cj = pi, pj
            visited.add((ci, cj))

        top.reverse(); bot.reverse()
        self.path = visited
        self.path_jumps = jumps

        mid = "".join("|" if t == b and t != "-" else " " for t, b in zip(top, bot))
        ident = sum(1 for t, b in zip(top, bot) if t == b and t != "-")
        L = len(top)
        pct = (100.0 * ident / L) if L else 0.0

        self.stage = "traceback"
        self._clear_selection()
        self._update_buttons()
        self.draw()
        self._set_align(f"{''.join(top)}\n{mid}\n{''.join(bot)}")
        self._set_info(f"Step 4 - Traceback done.\n\nOptimal score = "
                       f"{self.H[self.m][self.n]}\nIdentity {ident}/{L} = {pct:.0f}%\n"
                       f"(length includes gaps)\n\nClick cells to keep exploring "
                       f"sub-alignments.")
        self._set_status(f"Step 4 done - optimal score = {self.H[self.m][self.n]}; "
                         f"identity {ident}/{L} = {pct:.0f}%.")

    # ------------------------------------------------------------- step reset
    def on_reset(self):
        self.stage = "input"
        self._clear_selection()
        self.path = set()
        self.path_jumps = []
        self.canvas.delete("all")
        self._set_align("")
        self._set_info("")
        self._update_buttons()
        self._set_status("Step 1 - enter two sequences, then click 'Init'.")

    def _clear_selection(self):
        self.selected = None
        self.pred_cells = []
        self.cand_diag = None
        self.cand_up = []
        self.cand_left = []

    # -------------------------------------------------- traceback / alignment
    def _best_move(self, i, j):
        """Pick one optimal incoming move (priority: diag > shortest up > shortest left)."""
        if i == 0 and j == 0:
            return None
        if i == 0:
            return ("left", 0, j - 1, 1)
        if j == 0:
            return ("up", i - 1, 0, 1)
        ws = self.P[i][j]
        diag = [w for w in ws if w[0] == "diag"]
        if diag:
            return diag[0]
        ups = sorted((w for w in ws if w[0] == "up"), key=lambda w: w[3])
        if ups:
            return ups[0]
        lefts = sorted((w for w in ws if w[0] == "left"), key=lambda w: w[3])
        return lefts[0]

    def _emit(self, ci, cj, mv, top, bot):
        """Append the alignment column(s) for one backward move."""
        d, _, _, length = mv
        if d == "diag":
            top.append(self.seq1[cj - 1]); bot.append(self.seq2[ci - 1])
        elif d == "up":                                  # gap of length k in top seq
            for t in range(length):
                top.append("-"); bot.append(self.seq2[ci - 1 - t])
        elif d == "left":                                # gap of length l in side seq
            for t in range(length):
                top.append(self.seq1[cj - 1 - t]); bot.append("-")

    def _trace_from(self, i, j, first_move=None):
        """Build the optimal sub-alignment of prefixes ending at (i, j)."""
        top, bot = [], []
        ci, cj = i, j
        if first_move is not None:
            _, pi, pj, _ = first_move
            self._emit(ci, cj, first_move, top, bot)
            ci, cj = pi, pj
        while ci > 0 or cj > 0:
            mv = self._best_move(ci, cj)
            _, pi, pj, _ = mv
            self._emit(ci, cj, mv, top, bot)
            ci, cj = pi, pj
        top.reverse(); bot.reverse()
        return "".join(top), "".join(bot)

    def render_sub_alignments(self, i, j):
        """
        Return the optimal sub-alignment(s) of the prefixes seq1[:j] / seq2[:i]
        represented by cell (i, j) -- one variant per distinct winning last move
        (so ties show several 'possibilities'). Each item is
        (label, top, mid, bot).
        """
        if i == 0 and j == 0:
            return [("(empty prefixes)", "", "", "")]

        if i == 0 or j == 0:
            firsts = [self._best_move(i, j)]
        else:
            firsts = list(self.P[i][j])

        # dedupe by (direction, length) and cap for readability
        seen, uniq = set(), []
        for mv in firsts:
            key = (mv[0], mv[3])
            if key not in seen:
                seen.add(key)
                uniq.append(mv)
        uniq = uniq[:3]

        out = []
        for mv in uniq:
            top, bot = self._trace_from(i, j, first_move=mv)
            mid = "".join("|" if t == b and t != "-" else " "
                          for t, b in zip(top, bot))
            out.append((self._move_label(mv), top, mid, bot))
        return out

    def _move_label(self, mv):
        d, pi, pj, length = mv
        if d == "diag":
            same = self.seq2[pi] == self.seq1[pj]
            return f"end: diagonal ({'match' if same else 'mismatch'})"
        if d == "up":
            return f"end: vertical gap, length {length} (gap in top seq)"
        return f"end: horizontal gap, length {length} (gap in side seq)"

    # -------------------------------------------------------------- geometry
    def _ox(self):
        return MARGIN + CELL

    def _oy(self):
        return MARGIN + CELL

    def _bbox(self, i, j):
        x0 = self._ox() + j * CELL
        y0 = self._oy() + i * CELL
        return x0, y0, x0 + CELL, y0 + CELL

    def _center(self, i, j):
        x0, y0, x1, y1 = self._bbox(i, j)
        return (x0 + x1) / 2, (y0 + y1) / 2

    # ---------------------------------------------------------------- drawing
    def draw(self):
        self.canvas.delete("all")
        if self.stage == "input":
            return

        pred_set = {(pi, pj) for (pi, pj, _d) in self.pred_cells}
        up_set = set(self.cand_up)
        left_set = set(self.cand_left)

        for j in range(1, self.n + 1):
            cx, _ = self._center(0, j)
            self.canvas.create_text(cx, self._oy() - CELL / 2,
                                    text=self.seq1[j - 1], font=SEQFONT, fill="#0d47a1")
        for i in range(1, self.m + 1):
            _, cy = self._center(i, 0)
            self.canvas.create_text(self._ox() - CELL / 2, cy,
                                    text=self.seq2[i - 1], font=SEQFONT, fill="#0d47a1")

        for i in range(self.m + 1):
            for j in range(self.n + 1):
                x0, y0, x1, y1 = self._bbox(i, j)
                fill = C["init"] if (i == 0 or j == 0) else C["interior"]
                if (i, j) in self.path:
                    fill = C["pathcell"]
                if self.cand_diag == (i, j):
                    fill = C["cand_diag"]
                if (i, j) in up_set:
                    fill = C["cand_up"]
                if (i, j) in left_set:
                    fill = C["cand_left"]
                if (i, j) in pred_set:
                    fill = C["pred"]
                if self.selected == (i, j):
                    fill = C["selected"]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=C["grid"])
                val = self.H[i][j]
                if val is not None:
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                                            text=str(val), font=VALFONT, fill=C["text"])

        for (a, b) in self.path_jumps:
            self._arrow(a, b, C["patharrow"], 3)
        if self.selected and self.pred_cells:
            for (pi, pj, _) in self.pred_cells:
                self._arrow(self.selected, (pi, pj), C["arrow"], 2)

        w = self._ox() + (self.n + 1) * CELL + MARGIN
        h = self._oy() + (self.m + 1) * CELL + MARGIN
        self.canvas.configure(scrollregion=(0, 0, w, h))

    def _arrow(self, c_from, c_to, color, width):
        x0, y0 = self._center(*c_from)
        x1, y1 = self._center(*c_to)
        dx, dy = x1 - x0, y1 - y0
        dist = (dx * dx + dy * dy) ** 0.5 or 1
        s = CELL * 0.32
        x0 += dx / dist * s; y0 += dy / dist * s
        x1 -= dx / dist * s; y1 -= dy / dist * s
        self.canvas.create_line(x0, y0, x1, y1, fill=color, width=width,
                                arrow=tk.LAST, arrowshape=(12, 14, 5))

    # ---------------------------------------------------------------- clicking
    def on_click(self, event):
        if self.stage not in ("fill", "traceback"):
            return
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        j = int((x - self._ox()) // CELL)
        i = int((y - self._oy()) // CELL)
        if not (0 <= i <= self.m and 0 <= j <= self.n):
            return

        self._clear_selection()
        self.selected = (i, j)

        if i == 0 and j == 0:
            self.draw()
            self._set_info("CELL (0, 0)\n\nThe origin - empty vs empty.\n"
                           "Score 0, no predecessor.")
            self._set_status("Cell (0,0): origin (no predecessor).")
            return

        if i == 0 or j == 0:
            d, pi, pj, _ = self._best_move(i, j)
            self.pred_cells = [(pi, pj, d)]
            self.draw()
            self._show_cell_info(i, j, baseline=True)
            self._set_status(f"Cell ({i},{j}): affine gap baseline = {self.H[i][j]}.")
            return

        self.pred_cells = [(pi, pj, d) for (d, pi, pj, _) in self.P[i][j]]
        self.cand_diag = (i - 1, j - 1)
        self.cand_up = [(i - k, j) for k in range(1, i + 1)]
        self.cand_left = [(i, j - l) for l in range(1, j + 1)]
        self.draw()
        self._show_cell_info(i, j, baseline=False)
        self._set_status(f"Cell ({i},{j}) = {self.H[i][j]}  "
                         f"({'tie' if len(self.P[i][j]) > 1 else 'unique'} optimum).")

    # ----------------------------------------------------- info-panel rendering
    def _show_legend(self):
        self.info.configure(state=tk.NORMAL)
        self.info.delete("1.0", tk.END)
        self._ins("RECURRENCE (general + affine gaps)\n", "h1")
        self._ins("S(i,j) = max of\n"
                  "  - diagonal:  S(i-1,j-1) + s(a,b)\n"
                  "  - vertical:  S(i-k, j) + W(k)\n"
                  "  - horizontal:S(i, j-l) + W(l)\n"
                  "  W(L)=open+(L-1)*extend\n\n")
        self._ins("Click any cell to expand every\n"
                  "candidate and see its optimal\n"
                  "sub-alignment.\n\n")
        self._ins("Colours:\n", "h1")
        self._ins("  yellow  = clicked cell\n")
        self._ins("  green   = winning predecessor(s)\n")
        self._ins("  purple  = diagonal candidate\n")
        self._ins("  blue    = vertical candidates\n")
        self._ins("  orange  = horizontal candidates\n")
        self.info.configure(state=tk.DISABLED)

    def _show_cell_info(self, i, j, baseline):
        self.info.configure(state=tk.NORMAL)
        self.info.delete("1.0", tk.END)

        self._ins(f"CELL (i={i}, j={j})    S = {self.H[i][j]}\n", "h1")

        if baseline:
            length = j if i == 0 else i
            side = "side seq (seq2)" if i == 0 else "top seq (seq1)"
            self._ins(f"\nBaseline cell: one affine gap of\nlength {length} in the "
                      f"{side}.\n")
            self._ins(f"W({length}) = open + ({length}-1)*extend"
                      f" = {self._W(length)}\n")
        else:
            a, b = self.seq2[i - 1], self.seq1[j - 1]
            s = self._sub(i, j)
            kind = "match" if a == b else "mismatch"
            self._ins(f"\na_i = seq2[{i}] = '{a}'\n")
            self._ins(f"b_j = seq1[{j}] = '{b}'\n")
            self._ins(f"s(a_i,b_j) = {kind} = {s:+d}\n")
            self._ins(f"W(L) = {self.gap_open} + (L-1)*{self.gap_extend}\n\n")

            best = self.H[i][j]
            self._ins("S(i,j) = max of:\n", "h1")
            # diagonal
            self._cand_line(self.H[i - 1][j - 1] + s == best, "diag",
                            i - 1, j - 1, self.H[i - 1][j - 1], "s", s,
                            self.H[i - 1][j - 1] + s)
            # vertical (column above): gaps of length k
            for k in range(1, i + 1):
                tot = self.H[i - k][j] + self._W(k)
                self._cand_line(tot == best, f"vert k={k}", i - k, j,
                                self.H[i - k][j], "W", self._W(k), tot)
            # horizontal (row to left): gaps of length l
            for l in range(1, j + 1):
                tot = self.H[i][j - l] + self._W(l)
                self._cand_line(tot == best, f"horz l={l}", i, j - l,
                                self.H[i][j - l], "W", self._W(l), tot)

        # sub-alignment(s)
        self._ins("\nOptimal sub-alignment(s) here:\n", "sub")
        self._ins("(prefixes seq1[:%d] / seq2[:%d])\n" % (j, i), "dim")
        subs = self.render_sub_alignments(i, j)
        for (label, top, mid, bot) in subs:
            self._ins(f"\n {label}\n", "dim")
            self._ins(f"   {top}\n")
            self._ins(f"   {mid}\n")
            self._ins(f"   {bot}\n")

        self.info.configure(state=tk.DISABLED)

    def _cand_line(self, winner, tag, si, sj, sval, clabel, cval, total):
        mark = "*" if winner else " "
        src = f"S({si},{sj})={sval:>3}"
        con = f"{clabel}={cval:>+3}"
        line = f" {mark} {tag:<8}{src:<13}{con:<7}=> {total:>3}\n"
        self._ins(line, "win" if winner else None)


def main():
    root = tk.Tk()
    try:
        ttk.Style().theme_use("clam")
    except tk.TclError:
        pass
    NWApp(root)
    root.geometry("1180x720")
    root.mainloop()


if __name__ == "__main__":
    main()
