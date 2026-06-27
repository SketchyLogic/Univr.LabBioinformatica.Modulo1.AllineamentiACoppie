---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Dot Plots (Arc 2)

**Summary**: The dot plot (dot matrix) — the simplest *visual* way to compare two sequences — and the refinements (sliding window, scoring matrix, thresholds, % metrics) that make it usable for real, noisy data.
**Sources**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf|Teoria L3, slides 19–28]]

---

## The basic plot
A [[dot plot]] stacks one sequence on the top axis and the other on the side, marking a dot at every identity. Similarity shows up as **diagonals**; the geometry of those diagonals — [[dot plot patterns|main diagonal, inversions, repeats, deletions]] — tells you what kind of event relates the sequences. A self-comparison exposes internal repeats.

## Taming the noise
For 4-letter nucleotide alphabets the real signal drowns in random matches. The fix is the [[sliding window]]: compare whole segments (radius *g*, length *L = 2g+1*) and mark the center only if the segment matches well above a threshold *s*. True matches lie on diagonals; noise is scattered.

## From identity to similarity
The strict identity-only rule is relaxed by a [[scoring matrix]] (*matrice di punteggio*): score every residue pair, average over the window, and let the matrix define what "similar" means. A finished dot plot depends on three choices: the window length *L*, the similarity measure *S(x,y)*, and the threshold *s*.

## Quantifying the result
Finally, [[sequence identity and similarity percent|% identity and % similarity]] put numbers on the comparison — with the crucial caveat that, when gaps are present, the denominator is the **alignment length**, not the original sequence length.

## Limitation → next arc
Dot plots **ignore indels** as alignment operations, which is exactly what [[dynamic-programming-alignment|dynamic programming]] (Needleman–Wunsch) fixes.

## Related pages
- [[alignment-foundations]]
- [[dynamic-programming-alignment]]
- [[dot-plots-key-concepts]]
