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

## The stepper

1. **Enter sequences** — type *Seq 1* (drawn along the top / columns) and
   *Seq 2* (down the side / rows). Optionally adjust the **match / mismatch /
   gap** scores (defaults `+1 / -1 / -2`).
2. **Init** — builds the matrix and fills row 0 and column 0 with the
   cumulative gap baseline.
3. **Fill** — computes every interior cell as `base score + best predecessor`
   (the recurrence). After this, cells become **clickable**.
4. **Traceback** — walks back from the bottom-right corner along the stored
   best moves, highlights the optimal path (blue), and prints the resulting
   alignment + % identity at the bottom.

**Reset** returns to step 1 and re-enables the inputs.

## Inspecting a cell (during/after Fill)

Click any cell to highlight, in green, **which neighbour produced its optimal
score**, with an arrow from the cell to its predecessor:

- **diagonal** → the two residues were paired (match/mismatch, no gap)
- **vertical** → a gap in the **top** sequence
- **horizontal** → a gap in the **side** sequence

The status line spells out the move and its score contribution. If several
neighbours tie, all are highlighted (those are the co-optimal alignments).

## Convention

Matches the wiki: Seq 1 on top, Seq 2 on the side; the score is the standard
linear-gap global alignment. See
[Needleman-Wunsch recurrence](../wiki/glossary/Needleman-Wunsch%20recurrence.md)
and [traceback](../wiki/glossary/traceback.md).
