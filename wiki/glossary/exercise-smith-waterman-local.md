---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/ComputerScience/Algorithms/DynamicProgramming
  - MODULE__/LocalAlignment
  - EXAM_PREP
foundational: 2
prereqs: 3
density: 3
value: 4
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# exercise-smith-waterman-local

**Tool**: pen & paper (or EMBOSS `water` / `needle`) · **Source**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=2|L4 slide 8 (ESEMPIO 2)]]

## Task
Take the **same two peptides** used in the [[exercise-needleman-wunsch-worked|L3 NW exercise]] and align them **twice** with [[Smith-Waterman algorithm|Smith–Waterman]]: once **globally**, once **locally**. Then check whether the local alignment is a sub-piece of the global one.

```
S1: A D C N Y R Q C L C R P M
S2: A Y C Y N R C K C R D P
```

## Walkthrough
1. **Global SW.** Fill the matrix with [[affine gap penalty|gap penalties]] but **no** `0` option; trace back **corner → corner**.
2. **Local SW.** Re-fill with the **`0` option added** to the [[Needleman-Wunsch recurrence|recurrence]] (no negative cells). Find the **maximum-scoring cell** anywhere in the matrix and trace back from it **until you reach a `0`** — see [[Smith-Waterman algorithm]].
3. **Compare** the two alignments residue by residue.

## Expected answer
**WS-global** (end-to-end, one gap):
```
A D C N Y R Q C L C R P M
A Y C - Y N R C K C R D P
```
**WS-local** (best block only):
```
Y R Q C L C R
Y N R C K C R     → matches: Y · · C · C R  = 4/7 identical
```
- The local alignment isolates the conserved **`...RC.CR`** core (the C and R residues, plus Y) and **drops** the flanks `ADCN…` and `…RPM` / `…RDP`.
- **Key observation: AL ⊄ AG** — the local alignment is **not** a substring of the global one. Pairings differ (e.g. global pairs `Q–R` only after a different gap placement), because local traceback starts from the max cell, not the corner.

## Concepts exercised
- [[Smith-Waterman algorithm]]
- [[global vs local alignment]]
- [[affine gap penalty]]
- [[traceback]]
- [[Needleman-Wunsch recurrence]]

# TLDR
Aligning the same peptide pair globally vs locally with Smith–Waterman gives **different** results: global runs end-to-end (`ADCNYRQCLCRPM` / `AYC-YNRCKCRDP`), local extracts just the conserved core (`YRQCLCR` / `YNRCKCR`, 4/7 identical). The lesson: the local alignment is **not** a sub-piece of the global one (AL ⊄ AG).

# Recitation Anchors
- Same two peptides as the NW exercise, aligned global **and** local
- Global SW: corner→corner, full length, one gap
- Local SW: add `0`; start at **max cell**, stop at **`0`**
- Local result: `YRQCLCR` / `YNRCKCR` (the conserved C/R/Y core)
- **AL ⊄ AG** — local ≠ slice of global

> [!Cool] Cool fact
> The two EMBOSS tools you'd run this on are **named after the algorithms' authors**: `needle` for **Needle**man–Wunsch (global) and `water` for Smith–**Water**man (local) — a tiny in-joke baked into the most-used alignment suite in biology. [source](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/water.html)

# Read aloud
KP.0.Procedure: What the exercise asks.
This exercise takes the very same two peptides you aligned with Needleman–Wunsch back in lecture three, and aligns them twice with Smith–Waterman — once globally, once locally — so you can see how different the two results are.

KP.1.Procedure: Doing both alignments.
For the global version, you fill the matrix with gap penalties but no zero option, and trace back from corner to corner. For the local version, you add the zero option so no cell goes negative, then find the single highest-scoring cell anywhere in the grid and trace back from there until you hit a zero.

KP.2.Numbers: The two answers.
Globally, the alignment runs the full length with a single gap. Locally, it isolates just the best-matching block — the stretch Y-R-Q-C-L-C-R against Y-N-R-C-K-C-R, which is four matches out of seven, built around the conserved cysteines and arginines. The local alignment throws away both flanking ends.

KP.3.Connection: The key lesson.
And here's the lesson worth remembering: the local alignment is not simply a piece cut out of the global one. The pairings genuinely differ, because local traceback starts from the maximum cell rather than the corner. In the lecture's shorthand, A-L is not a subset of A-G.

KP.4.CoolFact: needle and water.
And here's the cool part — if you run this online, the two EMBOSS tools are named after the authors themselves: needle for Needleman–Wunsch, and water for Smith–Waterman. A little pun hidden inside the most widely used alignment software in biology.

# Question and Answer
Q. What is the point of aligning the same two peptides both globally and locally?
A. To show that the two modes give different alignments — the local one is not just a sub-region of the global one.

Q. What is the local Smith–Waterman result for this pair?
A. `YRQCLCR` aligned to `YNRCKCR` — the conserved core (4/7 identical), with both flanks dropped.

Q. How do you start and end the local traceback?
A. Start at the maximum-scoring cell anywhere in the matrix; stop at the first `0`.

Q. What does "AL ⊄ AG" mean here?
A. The local alignment (AL) is not a subset/substring of the global alignment (AG); their residue pairings differ.

Q. Which residues anchor the conserved local block, and why do they survive?
A. The cysteines and arginines (and a tyrosine) — they recur in both sequences, so the local path scores highest through them.

Q. What single change to the fill turns the global run into the local run?
A. Adding `0` as a fourth option in the recurrence's `max`, forbidding negative scores.
