---
tags:
  - TYPE__/Executable/Exercise
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
  - EXAM_PREP
foundational: 3
prereqs: 2
density: 2
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# exercise-sequence-identity-percent

**Tool**: pen & paper / EMBOSS `needle` output · **Source**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=7|L3 slide 28]] & [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=11|EMBOSS output, p.11]]

## Task
Given an alignment, compute **% identity** and explain how **% similarity** would be obtained. Then interpret a real EMBOSS `needle` report.

Alignment to score (a "`|`" marks an identical column, a gap is `-`):
```
S1:  A D C N - Y R Q C L C R P M
S2:  A Y C N K Y R - C K C R D P
     |   | |   | |   | | |
```

## Walkthrough
1. **Count the matches** — the columns marked `|`.
2. **Find the denominator.** Because the alignment **contains gaps**, use the **alignment length** (columns including gaps), per [[sequence identity and similarity percent]] — *not* the original sequence length.
3. **Compute** $\text{s.i.} = (\#\text{matches}/\text{alignment length})\times 100$.
4. **For similarity**, you would instead sum the [[scoring matrix]] score of S1-vs-S2 and divide by the S1-vs-S1 self score, ×100 — always ≥ identity.

## Expected answer
- Matches (`|`): A, C, N, Y, R, C, C, R = **8 matches**.
- Alignment length (columns incl. gaps) = **14**.
- **% identity = 8 / 14 ≈ 57%.**
- If you had wrongly used S1's length (13) you'd get 62% — the **gap caveat** matters.
- **Similarity** would be higher: conservative pairs (e.g. D↔Y? no; but K↔R *is* conservative, both basic) add to the numerator via the scoring matrix, so s.s. > s.i.

**Reading the real EMBOSS β/α-globin report** [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=11|p.11]]:
- `Identity: 65/149 (43.6%)`, `Similarity: 90/149 (60.4%)`, `Gaps: 9/149 (6.0%)`, `Score: 292.5`.
- Note **similarity (60.4%) > identity (43.6%)**, and the denominator **149** is the alignment length, consistent with the gap caveat.

## Concepts exercised
- [[sequence identity and similarity percent]]
- [[scoring matrix]]
- [[identity conservation similarity]]
- [[match mismatch gap]]

# TLDR
Count matches and divide by the **alignment length** (gaps included) → 8/14 ≈ **57% identity**; using the original length (13) wrongly gives 62%. Similarity uses the scoring-matrix score over the self score and is always higher (real EMBOSS globins: 43.6% identity vs 60.4% similarity).

# Recitation Anchors
- %identity = matches / alignment length × 100
- Denominator = **alignment length (incl. gaps)**, not original length
- Here: 8 / 14 ≈ **57%** (wrongly using 13 → 62%)
- %similarity = (S₁-vs-S₂ score / S₁-vs-S₁ self score) × 100 ≥ identity
- EMBOSS β/α-globin: identity 65/149 (43.6%), similarity 90/149 (60.4%)

> [!Cool] Cool fact
> EMBOSS `needle` (the very tool in the slide) implements Needleman–Wunsch and is still in everyday use; "needle" and its local-alignment sibling "water" are named after **Needle**man and Smith–**Water**man — a quiet pun baked into one of bioinformatics' most-run programs. [source](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/needle.html)

# Read aloud
KP.0.Procedure: The task.
This exercise asks you to take an alignment and work out its percent identity, then explain how percent similarity would be found, and finally read a real tool's report.

KP.1.Procedure: Counting and the denominator.
First, count the matching columns — the ones marked with a vertical bar. Then pick the denominator carefully. Because this alignment contains gaps, you divide by the alignment length, counting all the columns including the gaps, not by the original sequence length.

KP.2.Numbers: The calculation.
There are eight matches across fourteen columns, so the identity is eight over fourteen, about fifty-seven percent. If you'd carelessly divided by the original length of thirteen, you'd have gotten sixty-two percent — which shows exactly why the gap caveat matters.

KP.3.Concept: Similarity.
Similarity would be computed differently: you'd add up the scoring-matrix values for aligning the two sequences, divide by the score of aligning the first sequence against itself, and multiply by a hundred. Because conservative substitutions, like lysine paired with arginine, both basic, also score, similarity always comes out higher than identity.

KP.4.Numbers: The real report.
In the real beta-versus-alpha globin report, identity is sixty-five out of one hundred forty-nine, about forty-four percent, while similarity is ninety out of one hundred forty-nine, about sixty percent, with six percent gaps. Notice similarity beats identity, and the denominator, one hundred forty-nine, is the alignment length — exactly the gap caveat in action.

KP.5.CoolFact: A hidden pun.
And here's the cool part — the tool in the slide, called needle, runs Needleman–Wunsch, and its local-alignment sibling is called water, after Smith–Waterman. It's a quiet pun built into two of bioinformatics' most-used programs.

# Question and Answer
Q. What is the formula for percent identity?
A. (number of matches / alignment length) × 100.

Q. When the alignment has gaps, what must the denominator be?
A. The alignment length including gaps — not the original sequence length.

Q. For the given alignment, what is the % identity?
A. 8 matches / 14 columns ≈ 57%.

Q. Why is using the original sequence length (13) wrong here?
A. It ignores the gap columns and inflates the result to ~62%.

Q. How is percent similarity computed, and why is it ≥ identity?
A. (S1-vs-S2 similarity score / S1-vs-S1 self score) × 100; it also credits conservative substitutions, so it's ≥ identity.

Q. In the EMBOSS globin report, why is similarity (60.4%) greater than identity (43.6%)?
A. Many positions are conservative substitutions that count toward similarity but not identity.
