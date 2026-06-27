---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
foundational: 3
prereqs: 2
density: 2
value: 4
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-26
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# dot plot patterns

A [[dot plot]] turns sequence relationships into **geometry**: the *shape* of the diagonals tells you what kind of event relates the two sequences. With the top sequence held fixed, the characteristic patterns are: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=6|L3 p.6]]

- **Main diagonal** — a continuous diagonal (top-left → bottom-right) = the sequences are identical / highly similar along their length.
- **Inversion** — the main diagonal **breaks** and a segment reappears as an **anti-diagonal** (perpendicular slope): a portion of the sequence is reversed. The pattern of broken diagonals shows it clearly.
- **Repetition (repeat)** — the **same** off-diagonal segment appears **more than once** (parallel diagonals): a word/motif is repeated.
- **Deletion (indel)** — the diagonal continues but is **shifted** (jumps to a parallel track) at the point where characters were inserted/deleted: the diagonal is offset above or below the main one.

> [!Hint] Slope tells the story
> Parallel to the main diagonal = same orientation (match/repeat/shift). Perpendicular (anti-diagonal) = **reversed** orientation (inversion). A *break-then-offset* = an indel; a *break-then-flip* = an inversion.

For nucleotide sequences these clean patterns are obscured by random-match noise, which is why a [[sliding window]] and [[scoring matrix]] are layered on top to make the diagonals legible.

To *see* each of these patterns built up from scratch — one worked dot-plot figure per pattern, from a plain main diagonal to the noisy DNA case — work through [[dot plot patterns visualized]].

# TLDR
The *geometry* of a dot plot's diagonals diagnoses the event relating two sequences: a continuous **main diagonal** (similar), an **anti-diagonal** (inversion), **parallel repeated** diagonals (repetition), and a **shifted/offset** diagonal (indel).

# Recitation Anchors
- **Main diagonal** = identical/similar throughout
- **Anti-diagonal** (perpendicular) = inversion (reversed segment)
- **Repeated parallel** diagonals = repetition
- **Shifted/offset** diagonal = indel (deletion/insertion)
- Slope rule: parallel = same orientation, perpendicular = reversed

> [!Cool] Cool fact
> Genome-vs-genome dot plots make large-scale evolution visible to the naked eye: comparing two bacterial strains often shows a giant **X** — an "inversion bubble" — where a chromosomal segment flipped around the replication origin, a remarkably common rearrangement. [source](https://doi.org/10.1101/gr.2289704)

# Read aloud
KP.0.Concept: Patterns are geometry.
A dot plot turns the relationship between two sequences into geometry. The shape the diagonals make tells you what kind of evolutionary event connects the sequences. Keep the top sequence fixed, and watch the patterns.

KP.1.Definition: The main diagonal.
A single continuous diagonal running from top-left to bottom-right means the two sequences are identical, or highly similar, all the way along.

KP.2.Definition: Inversion.
If the main diagonal breaks and a piece of it reappears running the other way — perpendicular, like an anti-diagonal — that's an inversion. A chunk of the sequence has been reversed, and the broken pattern of diagonals shows it plainly.

KP.3.Definition: Repetition and deletion.
If the same off-diagonal segment shows up more than once, in parallel diagonals, you're looking at a repeat — a word or motif that occurs several times. And if the diagonal carries on but suddenly jumps to a parallel track, that offset marks a deletion or insertion at that point.

KP.4.Connection: Slope is the key.
Here's the rule of thumb. Parallel to the main diagonal means the same orientation — a match, a repeat, or a shifted indel. Perpendicular means reversed orientation — an inversion. For DNA, random noise smears these patterns, which is why we add a sliding window and a scoring matrix to make the diagonals readable.

KP.5.CoolFact: Inversions you can see.
And here's the cool part — when you dot-plot one whole genome against another, large-scale evolution becomes visible to the naked eye. Comparing two bacterial strains often produces a giant X shape, an inversion bubble, where a stretch of chromosome flipped around the origin of replication.

# Question and Answer
Q. What does a continuous main diagonal mean?
A. The two sequences are identical or highly similar along their whole length.

Q. How does an inversion appear on a dot plot?
A. The main diagonal breaks and a segment reappears as an anti-diagonal (perpendicular), signalling a reversed region.

Q. How does a repeat appear?
A. The same off-diagonal segment appears more than once, as parallel diagonals.

Q. How does an indel (deletion/insertion) appear?
A. The diagonal continues but is shifted onto a parallel track at the indel point.

Q. What does the slope of a feature tell you?
A. Parallel to the main diagonal = same orientation; perpendicular = reversed (inversion).

Q. Why are these patterns harder to see in nucleotide dot plots?
A. Random matches among only 4 letters add noise, masking the diagonals — fixed with a sliding window/scoring matrix.
