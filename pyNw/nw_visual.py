"""
Needleman-Wunsch visual simulator
==================================

A small Tkinter GUI that walks through the Needleman-Wunsch global alignment
algorithm one phase at a time:

    Step 1 - type the two sequences (and optional scores) into the inputs
    Step 2 - click "Init"      -> build the matrix + fill row 0 / column 0
    Step 3 - click "Fill"      -> compute every interior cell (recurrence)
    Step 4 - click "Traceback" -> walk back from the corner -> the alignment

During / after the Fill step, click any cell to highlight which neighbour
produced its optimal score (the predecessor used by the recurrence).

Convention (matches the wiki): sequence 1 runs along the TOP (columns),
sequence 2 runs down the SIDE (rows).
    - diagonal move  = pair the two residues (no gap)
    - vertical  move = gap in the TOP sequence
    - horizontal move = gap in the SIDE sequence

Run with:  python nw_visual.py
Requires only the Python standard library (tkinter).
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

C = {
    "grid":     "#c7ccd1",
    "init":     "#fdf3d0",   # row 0 / col 0 baseline cells
    "interior": "#ffffff",
    "selected": "#ffca28",   # the cell you clicked
    "pred":     "#aed581",   # the neighbour(s) that produced its score
    "pathcell": "#64b5f6",   # cells on the optimal traceback path
    "seqhdr":   "#eaeef3",
    "text":     "#1b1b1b",
    "arrow":    "#37474f",
    "patharrow":"#1565c0",
}


class NWApp:
    def __init__(self, root):
        self.root = root
        root.title("Needleman-Wunsch - visual stepper")

        self.stage = "input"          # input -> init -> fill -> traceback
        self.selected = None          # (i, j) cell the user clicked
        self.pred_cells = []          # [(i, j, direction), ...]
        self.path = set()             # cells on the optimal path
        self.path_list = []           # ordered path cells

        self._build_controls()
        self._build_canvas()
        self._build_footer()
        self._update_buttons()
        self._set_status("Step 1 - enter two sequences, then click 'Init'.")

    # ------------------------------------------------------------------ UI
    def _build_controls(self):
        bar = ttk.Frame(self.root, padding=8)
        bar.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(bar, text="Seq 1 (top):").grid(row=0, column=0, sticky="e")
        self.e_seq1 = ttk.Entry(bar, width=24, font=("Consolas", 11))
        self.e_seq1.insert(0, "GATTACA")
        self.e_seq1.grid(row=0, column=1, padx=(2, 12))

        ttk.Label(bar, text="Seq 2 (side):").grid(row=0, column=2, sticky="e")
        self.e_seq2 = ttk.Entry(bar, width=24, font=("Consolas", 11))
        self.e_seq2.insert(0, "GCATGCU")
        self.e_seq2.grid(row=0, column=3, padx=(2, 12))

        # scoring
        sc = ttk.Frame(bar)
        sc.grid(row=0, column=4, padx=(4, 12))
        self.e_match = self._score_entry(sc, "match", "1", 0)
        self.e_mis = self._score_entry(sc, "mismatch", "-1", 2)
        self.e_gap = self._score_entry(sc, "gap", "-2", 4)

        # step buttons
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

    def _build_canvas(self):
        wrap = ttk.Frame(self.root)
        wrap.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(wrap, background="white", highlightthickness=0)
        hbar = ttk.Scrollbar(wrap, orient=tk.HORIZONTAL, command=self.canvas.xview)
        vbar = ttk.Scrollbar(wrap, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        vbar.grid(row=0, column=1, sticky="ns")
        hbar.grid(row=1, column=0, sticky="ew")
        wrap.rowconfigure(0, weight=1)
        wrap.columnconfigure(0, weight=1)

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

    def _update_buttons(self):
        st = self.stage
        self.b_init.configure(state=(tk.NORMAL if st == "input" else tk.DISABLED))
        self.b_fill.configure(state=(tk.NORMAL if st == "init" else tk.DISABLED))
        self.b_tb.configure(state=(tk.NORMAL if st == "fill" else tk.DISABLED))
        ent = tk.NORMAL if st == "input" else tk.DISABLED
        for e in (self.e_seq1, self.e_seq2, self.e_match, self.e_mis, self.e_gap):
            e.configure(state=ent)

    def _read_int(self, entry, name):
        try:
            return int(entry.get().strip())
        except ValueError:
            raise ValueError(f"Score '{name}' must be an integer.")

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
            self.gap = self._read_int(self.e_gap, "gap")
        except ValueError as ex:
            messagebox.showerror("Bad score", str(ex))
            return

        self.seq1, self.seq2 = s1, s2
        self.n, self.m = len(s1), len(s2)

        # H = score matrix, P = predecessor directions per cell
        self.H = [[None] * (self.n + 1) for _ in range(self.m + 1)]
        self.P = [[[] for _ in range(self.n + 1)] for _ in range(self.m + 1)]

        self.H[0][0] = 0
        for j in range(1, self.n + 1):
            self.H[0][j] = self.H[0][j - 1] + self.gap
            self.P[0][j] = ["left"]
        for i in range(1, self.m + 1):
            self.H[i][0] = self.H[i - 1][0] + self.gap
            self.P[i][0] = ["up"]

        self.stage = "init"
        self.selected = None
        self.pred_cells = []
        self.path = set()
        self.path_list = []
        self._set_align("")
        self._update_buttons()
        self.draw()
        self._set_status("Step 2 done - matrix built; row 0 and column 0 hold the "
                         "cumulative gap baseline. Now click 'Fill'.")

    # ----------------------------------------------------------- step 3: fill
    def on_fill(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                a, b = self.seq2[i - 1], self.seq1[j - 1]
                diag = self.H[i - 1][j - 1] + (self.match if a == b else self.mismatch)
                up = self.H[i - 1][j] + self.gap        # gap in top sequence
                left = self.H[i][j - 1] + self.gap      # gap in side sequence
                best = max(diag, up, left)
                self.H[i][j] = best
                dirs = []
                if diag == best:
                    dirs.append("diag")
                if up == best:
                    dirs.append("up")
                if left == best:
                    dirs.append("left")
                self.P[i][j] = dirs

        self.stage = "fill"
        self._update_buttons()
        self.draw()
        self._set_status("Step 3 done - every cell = base score + best predecessor. "
                         "Click any cell to see where its score came from, "
                         "then click 'Traceback'.")

    # ------------------------------------------------------- step 4: traceback
    def on_traceback(self):
        i, j = self.m, self.n
        order = [(i, j)]
        top, bot = [], []
        # priority diag > up > left, respecting boundaries
        while i > 0 or j > 0:
            dirs = self.P[i][j]
            if i > 0 and j > 0 and "diag" in dirs:
                top.append(self.seq1[j - 1]); bot.append(self.seq2[i - 1]); i -= 1; j -= 1
            elif i > 0 and "up" in dirs:
                top.append("-"); bot.append(self.seq2[i - 1]); i -= 1
            elif j > 0 and "left" in dirs:
                top.append(self.seq1[j - 1]); bot.append("-"); j -= 1
            elif i > 0:                       # boundary fallback
                top.append("-"); bot.append(self.seq2[i - 1]); i -= 1
            else:
                top.append(self.seq1[j - 1]); bot.append("-"); j -= 1
            order.append((i, j))

        top.reverse(); bot.reverse()
        self.path = set(order)
        self.path_list = list(reversed(order))

        a_top = "".join(top)
        a_bot = "".join(bot)
        mid = "".join("|" if t == b and t != "-" else " " for t, b in zip(top, bot))
        ident = sum(1 for t, b in zip(top, bot) if t == b and t != "-")
        L = len(top)
        pct = (100.0 * ident / L) if L else 0.0

        self.stage = "traceback"
        self.selected = None
        self.pred_cells = []
        self._update_buttons()
        self.draw()
        self._set_status(f"Step 4 done - optimal score = {self.H[self.m][self.n]}; "
                         f"identity {ident}/{L} = {pct:.0f}% (alignment length includes gaps).")
        self._set_align(f"{a_top}\n{mid}\n{a_bot}")

    # ------------------------------------------------------------- step reset
    def on_reset(self):
        self.stage = "input"
        self.selected = None
        self.pred_cells = []
        self.path = set()
        self.path_list = []
        self.canvas.delete("all")
        self._set_align("")
        self._update_buttons()
        self._set_status("Step 1 - enter two sequences, then click 'Init'.")

    # -------------------------------------------------------------- geometry
    def _ox(self):
        return MARGIN + CELL          # leave one cell on the left for seq2 letters

    def _oy(self):
        return MARGIN + CELL          # leave one cell on top for seq1 letters

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

        pred_lookup = {(pi, pj): d for (pi, pj, d) in self.pred_cells}

        # sequence-letter headers
        for j in range(1, self.n + 1):
            cx, _ = self._center(0, j)
            self.canvas.create_text(cx, self._oy() - CELL / 2,
                                    text=self.seq1[j - 1], font=SEQFONT, fill="#0d47a1")
        for i in range(1, self.m + 1):
            _, cy = self._center(i, 0)
            self.canvas.create_text(self._ox() - CELL / 2, cy,
                                    text=self.seq2[i - 1], font=SEQFONT, fill="#0d47a1")

        # cells
        for i in range(self.m + 1):
            for j in range(self.n + 1):
                x0, y0, x1, y1 = self._bbox(i, j)
                fill = C["init"] if (i == 0 or j == 0) else C["interior"]
                if (i, j) in self.path:
                    fill = C["pathcell"]
                if (i, j) in pred_lookup:
                    fill = C["pred"]
                if self.selected == (i, j):
                    fill = C["selected"]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill,
                                             outline=C["grid"])
                val = self.H[i][j]
                if val is not None:
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                                            text=str(val), font=VALFONT, fill=C["text"])

        # traceback path arrows (parent -> child)
        for k in range(len(self.path_list) - 1):
            self._arrow(self.path_list[k], self.path_list[k + 1],
                        C["patharrow"], 3)

        # predecessor arrows for the selected cell (cell -> predecessor)
        if self.selected and self.pred_cells:
            for (pi, pj, _d) in self.pred_cells:
                self._arrow(self.selected, (pi, pj), C["arrow"], 2)

        # scroll region
        w = self._ox() + (self.n + 1) * CELL + MARGIN
        h = self._oy() + (self.m + 1) * CELL + MARGIN
        self.canvas.configure(scrollregion=(0, 0, w, h))

    def _arrow(self, c_from, c_to, color, width):
        x0, y0 = self._center(*c_from)
        x1, y1 = self._center(*c_to)
        # shrink endpoints so the arrow sits inside the cells
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
        if i == 0 and j == 0:
            self.selected = (0, 0)
            self.pred_cells = []
            self.draw()
            self._set_status("Cell (0,0) is the origin - it has no predecessor.")
            return

        self.selected = (i, j)
        self.pred_cells = []
        for d in self.P[i][j]:
            if d == "diag":
                self.pred_cells.append((i - 1, j - 1, d))
            elif d == "up":
                self.pred_cells.append((i - 1, j, d))
            elif d == "left":
                self.pred_cells.append((i, j - 1, d))
        self.draw()
        self._describe_cell(i, j)

    def _describe_cell(self, i, j):
        parts = []
        for d in self.P[i][j]:
            if d == "diag":
                a, b = self.seq2[i - 1], self.seq1[j - 1]
                kind = "match" if a == b else "mismatch"
                sc = self.match if a == b else self.mismatch
                parts.append(f"DIAGONAL ({i-1},{j-1}) [{b}/{a} {kind} {sc:+d}]")
            elif d == "up":
                parts.append(f"VERTICAL ({i-1},{j}) [gap in top seq {self.gap:+d}]")
            elif d == "left":
                parts.append(f"HORIZONTAL ({i},{j-1}) [gap in side seq {self.gap:+d}]")
        tie = "  (tie - multiple optimal paths)" if len(parts) > 1 else ""
        self._set_status(f"Cell ({i},{j}) = {self.H[i][j]}  <-  " + " or ".join(parts) + tie)


def main():
    root = tk.Tk()
    try:
        ttk.Style().theme_use("clam")
    except tk.TclError:
        pass
    NWApp(root)
    root.geometry("980x680")
    root.mainloop()


if __name__ == "__main__":
    main()
