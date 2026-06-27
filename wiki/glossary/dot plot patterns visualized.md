---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
foundational: 3
prereqs: 2
density: 3
value: 4
CreatedAt: 2026-06-26
LastUpdateAt: 2026-06-26
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# dot plot patterns visualized

A hand-drawn gallery that *builds up* the [[dot plot patterns]] one step at a time, so you can see exactly **how each shape arises** from the rule "mark a cell when the two residues are identical" (see [[dot plot]]). Read top to bottom: every figure adds **one** new idea to the previous one.

**Convention for every figure:** sequence **X** runs along the **top** (columns, →), sequence **Y** runs down the **left** (rows, ↓). A cell shows `●` when `X[col] = Y[row]`, and `·` when they differ. To keep the *structure* visible (not noise), Examples 1–5 use **distinct letters**; Example 6 switches to the 4-letter DNA alphabet on purpose, to show where noise comes from.

---

## Example 1 — Identity → the main diagonal

The baseline. Compare a sequence with an identical copy: `MARS` vs `MARS`. Each letter matches only its own position, so dots fall on the **main diagonal** (top-left → bottom-right).

```
      M  A  R  S        X = M A R S
  M   ●  ·  ·  ·        Y = M A R S
  A   ·  ●  ·  ·
  R   ·  ·  ●  ·        → one continuous main diagonal
  S   ·  ·  ·  ●          = the sequences are identical / highly similar
```

**Why:** `M=M`, `A=A`, `R=R`, `S=S` sit at cells (1,1),(2,2),(3,3),(4,4) — the definition of the diagonal.

## Example 2 — One substitution → a break in the diagonal

Now mutate position 3, `R → K`: `MARS` vs `MA`**`K`**`S`. The diagonal loses exactly **one** dot where the letters disagree.

```
      M  A  R  S        X = M A R S
  M   ●  ·  ·  ·        Y = M A K S
  A   ·  ●  ·  ·                  ↑ substitution
  K   ·  ·  ·  ·        → diagonal continuous, with ONE hole at the mismatch
  S   ·  ·  ·  ●
```

**Why:** at row 3 the letter is now `K`, which matches no column, so cell (3,3) goes blank — a single missing dot is the signature of a **point mutation** ([[match mismatch gap|mismatch]]).

## Example 3 — Internal repeat → parallel diagonals

Compare a sequence **with itself** (*autoconfronto*) when it contains a repeated motif: `ABCABC` (the block `ABC` appears twice). You get the main diagonal **plus** two extra diagonals parallel to it.

```
      A  B  C  A  B  C       X = Y = A B C A B C
  A   ●  ·  ·  ●  ·  ·               (motif ABC repeated)
  B   ·  ●  ·  ·  ●  ·
  C   ·  ·  ●  ·  ·  ●        main diagonal  = self-identity
  A   ●  ·  ·  ●  ·  ·        upper diagonal = 2nd copy vs 1st
  B   ·  ●  ·  ·  ●  ·        lower diagonal = 1st copy vs 2nd
  C   ·  ·  ●  ·  ·  ●        offset = repeat length (3)
```

**Why:** the first `A` (col 1) also equals the second `A` (row 4), giving an off-diagonal dot at (4,1); the whole second `ABC` re-matches the first, producing a diagonal **shifted by the repeat length**. Self-comparison is always **symmetric**, so the extra diagonal appears both above and below the main one.

## Example 4 — Inversion → an anti-diagonal

Compare a sequence with a **reversed** copy: `ABCDE` vs `EDCBA`. The matching run now slopes the **other way** — a perpendicular **anti-diagonal** (top-right → bottom-left).

```
      A  B  C  D  E       X = A B C D E
  E   ·  ·  ·  ·  ●       Y = E D C B A  (X reversed)
  D   ·  ·  ·  ●  ·
  C   ·  ·  ●  ·  ·       → anti-diagonal = a reversed (inverted) segment
  B   ·  ●  ·  ·  ·
  A   ●  ·  ·  ·  ·
```

**Why:** the last letter of Y (`A`, row 5) matches the first letter of X (`A`, col 1), and so on inward — reversal flips the slope. **Slope is the whole story:** parallel to the main diagonal = same orientation; perpendicular = **inversion**.

## Example 5 — Indel (insertion/deletion) → a shifted diagonal

Insert one residue into Y: `MARST` (X) vs `MA`**`Z`**`RST` (Y, with `Z` inserted at position 3). The diagonal runs, then **jumps to a parallel track** at the indel.

```
      M  A  R  S  T       X = M A R S T
  M   ●  ·  ·  ·  ·       Y = M A Z R S T
  A   ·  ●  ·  ·  ·                ↑ insertion
  Z   ·  ·  ·  ·  ·       → diagonal shifts DOWN one row after the inserted Z
  R   ·  ·  ●  ·  ·         (the vertical step = the indel)
  S   ·  ·  ·  ●  ·
  T   ·  ·  ·  ·  ●
```

**Why:** before the insertion the match is on the main diagonal (1,1),(2,2); the extra `Z` pushes everything after it down one row, so the run resumes **offset** at (4,3),(5,4),(6,5). A *break-then-offset* (same slope) = an **indel**; contrast the *break-then-flip* of Example 4. This is exactly the limitation the raw dot plot can only *show* but not *score* — handling indels as operations is what [[Needleman-Wunsch algorithm|dynamic programming]] adds.

## Example 6 — Real noise, and the sliding-window fix

Switch to the 4-letter DNA alphabet, where letters *must* recur. `GATCAG` (X) vs `GATCTA` (Y) share a true `GATC` region (a 4-long diagonal run) **buried in scattered random matches**.

```
      G  A  T  C  A  G       X = G A T C A G
  G   ●  ·  ·  ·  ·  ●       Y = G A T C T A
  A   ·  ●  ·  ·  ●  ·       run (1,1)-(4,4) = real GATC similarity
  T   ·  ·  ●  ·  ·  ·       isolated dots  = chance matches (noise)
  C   ·  ·  ·  ●  ·  ·
  T   ·  ·  ●  ·  ·  ·
  A   ·  ●  ·  ·  ●  ·
```

Apply a [[sliding window]] (`L = 3`): keep a dot only if it sits inside a diagonal **run** of matches. The lone dots score `N = 1` and vanish; the genuine diagonal survives.

```
      G  A  T  C  A  G       after sliding window (L = 3):
  G   ●  ·  ·  ·  ·  ·       only the diagonal RUN remains;
  A   ·  ●  ·  ·  ·  ·       scattered single matches are filtered out
  T   ·  ·  ●  ·  ·  ·
  C   ·  ·  ·  ●  ·  ·       → this is why nucleotide dot plots
  T   ·  ·  ·  ·  ·  ·         need a window to be legible
  A   ·  ·  ·  ·  ·  ·
```

**Why:** with only 4 symbols, ~1 in 4 cells matches by chance, so real diagonals drown in dots. The window asks "does the whole *segment* match?" — true similarity (a run) passes, random isolated hits do not.

## How the patterns map to events

| Figure | Pattern | Geometry | Event |
|---|---|---|---|
| Ex. 1 | main diagonal | parallel, full | identical / similar |
| Ex. 2 | diagonal with a hole | parallel, 1 gap | substitution |
| Ex. 3 | extra parallel diagonals | parallel, offset | repeat |
| Ex. 4 | anti-diagonal | **perpendicular** | inversion |
| Ex. 5 | shifted diagonal | parallel, stepped | indel |
| Ex. 6 | run vs scattered dots | diagonal vs random | signal vs noise |

See [[dot plot patterns]] for the catalogue and [[exercise-dot-plot-construction]] to draw one yourself.

# TLDR
Six hand-drawn dot plots build the patterns one idea at a time: an **identical** copy gives the main diagonal; a **substitution** punches a hole in it; a **repeat** adds parallel diagonals; an **inversion** flips a run to a perpendicular anti-diagonal; an **indel** shifts the diagonal to a parallel track; and the **4-letter DNA** case shows random noise that a [[sliding window]] filters away.

# Recitation Anchors
- Rule for every cell: dot iff `X[col] = Y[row]`; X on top, Y on side
- Identity → full **main diagonal**
- Substitution → **one hole** in the diagonal
- Repeat → **parallel** off-diagonals, offset = repeat length (symmetric in self-comparison)
- Inversion → **perpendicular anti-diagonal** (slope flips)
- Indel → diagonal **shifted** to a parallel track (break-then-offset)
- Slope test: parallel = same orientation, perpendicular = reversed
- DNA noise → real run survives a sliding window; isolated dots vanish

> [!Cool] Cool fact
> The dot plot is as old as automated alignment itself: Gibbs & McIntyre introduced "**the diagram**" for comparing sequences in **1970** — the very same year Needleman & Wunsch published their algorithm — and its diagonals-and-anti-diagonals visual grammar has barely changed in over 50 years. [source](https://doi.org/10.1111/j.1432-1033.1970.tb00824.x)

# Read aloud
KP.0.Concept: One rule, many shapes.
Every dot plot comes from a single rule: put the first sequence along the top and the second down the side, then mark a cell whenever the two letters are the same. Everything that follows — diagonals, anti-diagonals, shifts — is just that one rule playing out on different sequences. We'll build the patterns up one at a time.

KP.1.Definition: The main diagonal.
Start with the simplest case: a sequence compared against an identical copy. Each letter matches only its own position, so the dots line up on the main diagonal, running from the top-left corner to the bottom-right. A full main diagonal means the two sequences are identical, or very nearly so.

KP.2.Concept: A substitution makes a hole.
Now change a single letter in the middle. That one position no longer matches, so its dot disappears, leaving a gap in the diagonal. A single missing dot is the fingerprint of a point mutation — a substitution.

KP.3.Concept: Repeats make parallel diagonals.
Next, compare a sequence with itself when it contains a repeated motif, like the block A-B-C appearing twice. You still get the main diagonal, but now two more diagonals appear parallel to it, because the second copy of the motif matches the first. The distance of those extra diagonals from the main one equals the length of the repeat. And because a sequence compared with itself is symmetric, the extra diagonal shows up both above and below the centre.

KP.4.Concept: Inversions flip the slope.
Then compare a sequence with a reversed copy. The matching run now slopes the other way — perpendicular to the main diagonal, an anti-diagonal. This is the key intuition: slope tells the story. Parallel to the main diagonal means the same orientation; perpendicular means a reversed, inverted segment.

KP.5.Concept: Indels shift the track.
Insert an extra residue into one sequence. The diagonal runs along normally, then suddenly jumps to a parallel track at the point of the insertion. That vertical step is the insertion or deletion. So a break-then-shift, keeping the same slope, means an indel, while a break-then-flip means an inversion. The raw dot plot can show an indel but can't score it — that's exactly what dynamic programming adds later.

KP.6.Connection: Noise and the sliding window.
Finally, switch to real DNA, with only four letters. Now matches happen by chance all over the grid, and the true diagonal is buried in scattered dots. The fix is a sliding window: keep a dot only if it sits inside a genuine diagonal run. The lone random dots score low and vanish, while the real diagonal survives. That's why nucleotide dot plots need a window to be readable at all.

KP.7.CoolFact: As old as alignment itself.
And here's the cool part — the dot plot isn't a modern gadget. Gibbs and McIntyre introduced this diagram method for comparing sequences back in 1970, the very same year the Needleman–Wunsch algorithm appeared. Its visual language of diagonals and anti-diagonals has barely changed in over fifty years.

# Question and Answer
Q. What single rule generates every dot in a dot plot?
A. Mark cell (col, row) whenever the top-sequence letter at that column equals the side-sequence letter at that row.

Q. What does a full, continuous main diagonal mean?
A. The two sequences are identical or highly similar along their whole length (Example 1).

Q. How does a single substitution appear, and why?
A. As one missing dot in the diagonal — that position's letters disagree, so its cell stays blank (Example 2).

Q. In a self-comparison, why do repeats produce diagonals both above and below the main one?
A. Self-comparison is symmetric: if copy 2 matches copy 1 off-diagonal, the mirror match also appears, so the extra diagonal shows on both sides. The offset equals the repeat length (Example 3).

Q. What distinguishes an inversion from an indel on a dot plot?
A. An inversion flips the run to a perpendicular anti-diagonal (slope reverses); an indel keeps the slope but shifts the diagonal to a parallel track (Examples 4–5).

Q. Why do nucleotide dot plots look noisy, and how does a sliding window clean them up?
A. With only 4 letters, ~25% of cells match by chance, scattering dots. A window keeps a dot only if it lies in a diagonal run, so isolated chance matches are filtered out while the true diagonal survives (Example 6).

Q. On a dot plot, what does "slope is the whole story" mean?
A. A feature parallel to the main diagonal has the same orientation (match/repeat/indel); a feature perpendicular to it is reversed (an inversion).
