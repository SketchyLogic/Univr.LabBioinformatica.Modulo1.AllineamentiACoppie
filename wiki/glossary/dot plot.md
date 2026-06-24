---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
foundational: 4
prereqs: 2
density: 3
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# dot plot

A **dot plot** (or **dot matrix**) is the simplest *visual* way to spot regions of local similarity between two sequences. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=5|L3 p.5]]

**Construction (basic version):**
1. Write sequence 1 along the **top** (columns) and sequence 2 down the **left** (rows).
2. For every cell *(x, y)*, put a **dot/× if the two residues are identical**; leave it blank otherwise.

Reading it: **diagonal runs of dots = stretches of similarity.** A single long main diagonal means the sequences are (nearly) identical. Where the diagonal breaks, shifts, or appears off-axis, structure is revealed — see [[dot plot patterns]].

A sequence compared **with itself** (*autoconfronto* / self-comparison) gives a perfect main diagonal plus off-diagonal dots wherever the sequence has **internal repeats** — useful for finding repeated motifs.

**Limitations** that motivate everything after it:
- For 4-letter **nucleotide** alphabets, the true signal is buried in random-match **noise** → needs filtering with a [[sliding window]].
- A raw dot plot scores only **identity**, not [[identity conservation similarity|similarity]] → needs a [[scoring matrix]] + threshold.
- It **ignores indels** as alignment operations → motivates [[Needleman-Wunsch algorithm|dynamic-programming alignment]].

A finished dot plot depends on **three choices**: the window length *L*, the similarity measure *S(x,y)*, and the threshold *s* for marking a cell.

# TLDR
A dot plot puts one sequence on each axis and marks a dot wherever two residues are identical; **diagonal runs of dots = regions of similarity**. Self-comparison exposes internal repeats. It scores only identity and ignores indels — limits that motivate sliding windows, scoring matrices, and dynamic-programming alignment.

# Recitation Anchors
- Seq1 on top, seq2 on side; dot where residues identical
- **Diagonal runs = similarity**; full main diagonal = near-identical
- Self-comparison → main diagonal + off-diagonal repeats
- Three choices: window length **L**, similarity measure **S**, threshold **s**
- Limits: noise (→ sliding window), identity-only (→ scoring matrix), ignores indels (→ DP)

> [!Cool] Cool fact
> Dot plots aren't just historical: modern tools like **DOTTER** and **Dotlet** colour each cell by score, and self-dot-plots remain the go-to method for spotting tandem repeats and palindromes in genomes at a glance. [source](https://doi.org/10.1016/0378-1119(95)00714-8)

# Read aloud
KP.0.Definition: What a dot plot is.
A dot plot, also called a dot matrix, is the simplest visual way to see where two sequences resemble each other.

KP.1.Procedure: How to build one.
You build it like a grid. Write the first sequence across the top, one letter per column, and the second sequence down the left side, one letter per row. Then, for every cell where the column letter and the row letter are the same, you place a dot. Leave the rest blank.

KP.2.Concept: How to read it.
The trick is to look for diagonals. A diagonal run of dots means a stretch where the two sequences match. One long diagonal straight down the middle means the sequences are nearly identical. When that diagonal breaks, shifts sideways, or shows up off the main axis, it's telling you something — repeats, inversions, deletions.

KP.3.Concept: Self-comparison.
If you plot a sequence against itself, you always get a perfect main diagonal, plus extra dots wherever the sequence repeats internally. That makes self-dot-plots a neat way to find repeated motifs.

KP.4.Connection: Why we need more.
But the basic dot plot has three weaknesses, and each one points to the next idea. With only four DNA letters, real matches drown in random noise, so we filter with a sliding window. It only catches identical letters, not similar ones, so we bring in a scoring matrix and a threshold. And it ignores insertions and deletions, which is what pushes us toward dynamic-programming alignment. In the end, a dot plot is defined by three choices: the window length, the similarity measure, and the threshold for marking a cell.

KP.5.CoolFact: Still used today.
And here's the cool part — dot plots aren't a museum piece. Modern programs like DOTTER and Dotlet colour each cell by its score, and plotting a sequence against itself is still the fastest way to spot tandem repeats and palindromes in a genome.

# Question and Answer
Q. How do you construct a basic dot plot?
A. Put one sequence on the top axis and the other on the side; mark each cell where the two residues are identical.

Q. What does a diagonal run of dots indicate?
A. A region of similarity between the two sequences; one long main diagonal means near-identity.

Q. What does a self-comparison dot plot reveal?
A. Internal repeats — a main diagonal plus off-diagonal dots wherever the sequence repeats itself.

Q. Name the three choices a dot plot depends on.
A. The window length L, the similarity measure S(x,y), and the marking threshold s.

Q. Why are nucleotide dot plots noisy, and what fixes it?
A. Only 4 letters → many random matches; a sliding window filters the noise. See [[sliding window]].

Q. Give two limitations of the basic dot plot beyond noise.
A. It scores only identity (fixed by a scoring matrix + threshold) and it ignores indels (fixed by dynamic-programming alignment).
