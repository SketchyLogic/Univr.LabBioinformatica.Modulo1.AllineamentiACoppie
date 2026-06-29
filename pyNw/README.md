# pyNw — Needleman–Wunsch visual stepper

A tiny Tkinter GUI that walks through the [Needleman–Wunsch](../wiki/glossary/Needleman-Wunsch%20algorithm.md)
global alignment algorithm one phase at a time, so you can *see* the matrix
fill and the traceback happen.

## Run

```bash
python nw_visual.py
```

No installation needed — it uses only the Python standard library (`tkinter`,
which ships with CPython on Windows/macOS and is in the `python3-tk` package on
Linux). Python 3.8+.

## Scoring — general recurrence with affine gaps

This build uses the **general** recurrence, where a gap may span any length in
one step, with an **affine** gap penalty:

```
S(i,j) = max [ S(i-1,j-1) + s(a_i,b_j),     # diagonal: pair, no gap
               max_{k>=1} S(i-k, j) + W(k),  # gap of length k in TOP seq
               max_{l>=1} S(i, j-l) + W(l) ] # gap of length l in SIDE seq
W(L) = gap_open + (L-1) * gap_extend
```

Four score inputs (defaults `match +1 / mismatch -1 / gap_open -2 /
gap_extend -1`). With `gap_extend` close to 0, one long gap is cheap (affine);
set `gap_extend == gap_open` to recover a plain linear penalty.

## The stepper

1. **Enter sequences** — *Seq 1* (top / columns), *Seq 2* (side / rows), plus
   the four scores.
2. **Init** — builds the matrix; row 0 / column 0 hold a single affine gap of
   growing length, `W(L)`.
3. **Fill** — computes every interior cell with the recurrence above. After
   this, cells become **clickable** and the right-hand panel shows the rule.
4. **Traceback** — walks back from the corner, highlights the optimal path
   (blue, including the cells a long gap spans), and prints the alignment +
   % identity at the bottom.

**Reset** returns to step 1 and re-enables the inputs.

## Inspecting a cell (during/after Fill)

Click any cell to expand the recurrence for it. The grid colours **every
candidate** of the formula, not just three neighbours:

- **purple** — the diagonal candidate `S(i-1,j-1)`
- **blue** — the vertical candidates `S(i-k, j)` (the whole column above: gaps
  of length 1, 2, 3, …)
- **orange** — the horizontal candidates `S(i, j-l)` (the whole row to the left)
- **green** — the winning predecessor(s), with an arrow (ties = several)
- **yellow** — the clicked cell

The right panel lists each candidate with its score arithmetic, marks the
winner(s) with `*`, and renders the **optimal sub-alignment(s)** that the cell
represents (the best alignment of the two prefixes ending there) — optimal
substructure made visible. See `render_sub_alignments` in the source.

## Convention

Matches the wiki: Seq 1 on top, Seq 2 on the side; the score is the standard
linear-gap global alignment. See
[Needleman-Wunsch recurrence](../wiki/glossary/Needleman-Wunsch%20recurrence.md)
and [traceback](../wiki/glossary/traceback.md).



# TODO
Understand the code - Rebuild it from scratch with spec-kit, web-based.
Add comments
Handle scoring matrix
Handle sliding window
Generate scenarios