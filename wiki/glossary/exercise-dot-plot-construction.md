---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
foundational: 3
prereqs: 2
density: 2
value: 4
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# exercise-dot-plot-construction

**Tool**: pen & paper (or DOTTER / Dotlet) · **Source**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=5|L3 slides 19–24]]

## Task
Build a [[dot plot]] by hand for the self-comparison of a short "sequence", then read off its [[dot plot patterns|patterns]]. Use the lecture's toy string and a variant with a reversed segment.

```
String A (top & side):  L A B I N F O B A L
```

## Walkthrough
1. **Grid.** Write the string along the top (columns) and down the left (rows).
2. **Dots.** Put a `×` in every cell where the column letter equals the row letter.
3. **Read the main diagonal.** Self-comparison always yields a full main diagonal (every letter matches itself).
4. **Find off-diagonal dots.** Repeated letters/segments produce extra dots off the main diagonal — these mark internal **repeats**.
5. **Variant — make a reversed copy** (e.g. compare `LABNFO` against `OFNBAL`) and observe the **anti-diagonal**: a reversed segment shows up perpendicular to the main diagonal (an **inversion**).
6. **Add a [[sliding window]]** (e.g. L = 3): only mark a center cell if the whole 3-letter window matches — watch isolated noise dots disappear while diagonals survive.

## Expected answer
- **Main diagonal**: present and complete (self-identity).
- **Off-diagonal dots**: appear wherever a letter repeats (e.g. the two `A`s, two `B`s, two `L`s) — short broken diagonals = internal repeats.
- **Reversed variant**: the matching segment appears as an **anti-diagonal** → diagnostic of an **inversion**.
- **With the sliding window**: scattered single dots vanish; only runs of ≥ L consecutive matches remain — the diagonals become legible, exactly the noise-reduction the lecture motivates for 4-letter alphabets.

## Concepts exercised
- [[dot plot]]
- [[dot plot patterns]]
- [[sliding window]]
- [[scoring matrix]]

# TLDR
Build a self dot plot (dot wherever the column letter equals the row letter): you get a complete **main diagonal** plus off-diagonal dots marking **internal repeats**. A reversed segment appears as an **anti-diagonal** (inversion), and a sliding window removes isolated noise dots.

# Recitation Anchors
- Dot where column letter = row letter
- Self-comparison → complete **main diagonal**
- Off-diagonal dots = **internal repeats**
- Reversed segment → **anti-diagonal** = inversion
- Sliding window (L=3) → kills isolated noise, keeps real diagonals
- Crucial for 4-letter nucleotide alphabets

> [!Cool] Cool fact
> A dot plot of a sequence against itself is the classic way to expose **tandem repeats** and **palindromes** — and in genomics, self-dot-plots of chromosomes reveal segmental duplications spanning thousands of bases, visible as bright off-diagonal stripes. [source](https://doi.org/10.1016/0378-1119(95)00714-8)

# Read aloud
KP.0.Procedure: The task.
This exercise has you build a dot plot by hand for a short string compared with itself, then read the patterns it makes. You'll also try a reversed copy and a sliding window.

KP.1.Procedure: Building the grid.
Write the string across the top and down the left side. Then put a mark in every cell where the column letter matches the row letter. Because you're comparing the string with itself, you always get a complete main diagonal — every letter matches itself.

KP.2.Concept: Reading repeats.
Now look off the main diagonal. Wherever a letter or a short segment repeats inside the string, you get extra dots away from the diagonal. Those short, broken diagonals are the signature of internal repeats.

KP.3.Concept: Inversions and the window.
Next, compare the string against a reversed copy of part of it. The matching segment now shows up running the other way, perpendicular to the main diagonal — that anti-diagonal is the telltale sign of an inversion. Finally, switch on a sliding window of, say, length three: only mark a centre cell when the whole window matches. Watch the scattered single noise dots vanish while the genuine diagonals survive. That's exactly the noise reduction the lecture says we need for four-letter DNA.

KP.4.CoolFact: Repeats and palindromes at a glance.
And here's the cool part — plotting a sequence against itself is the classic trick for revealing tandem repeats and palindromes. In genomics, self-dot-plots of whole chromosomes light up segmental duplications thousands of bases long, as bright stripes off the main diagonal.

# Question and Answer
Q. How do you place dots in a basic dot plot?
A. Mark each cell where the column letter equals the row letter.

Q. What always appears in a self-comparison dot plot, and why?
A. A complete main diagonal, because every letter matches itself.

Q. What do off-diagonal dots indicate in a self dot plot?
A. Internal repeats — repeated letters or segments within the sequence.

Q. How does an inversion appear?
A. As an anti-diagonal (perpendicular to the main diagonal), from a reversed segment.

Q. What does adding a sliding window (L=3) do to the plot?
A. Removes isolated noise dots, keeping only runs of ≥ L consecutive matches, so diagonals become legible.

Q. Why is this filtering especially important for nucleotide sequences?
A. With only 4 letters, random single matches are frequent; windowing suppresses that background noise.
