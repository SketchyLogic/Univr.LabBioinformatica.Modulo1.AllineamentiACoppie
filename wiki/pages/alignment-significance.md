---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Alignment Significance (Arc 5)

**Summary**: You aligned two sequences and got a score — but **is it meaningful, or chance?** This arc answers that question two ways: by **shuffling** (the Z-score) for global alignments, and by the **Karlin–Altschul E-value** with its **Gumbel** distribution for local alignments.
**Sources**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf|Teoria L4, slides 9–14]]

---

## The question
Any two sequences align to *some* score, and that score is matrix-dependent and **not absolute**. [[statistical significance of an alignment]] frames the problem: a score only matters relative to a **null model** of chance — and statistical significance never replaces **biological** significance.

## Global: the Z-score
For [[global vs local alignment|global]] alignments there's no neat formula, so significance is **empirical**. The [[Z-score (alignment)|Z-score]] shuffles one sequence many times, builds a distribution of random scores, and measures how many standard deviations the real score sits above the mean: $Z=(S-\mu)/\sigma$. Its weakness — it assumes a **normal** distribution — sets up the local case.

## Local: the E-value and the Gumbel curve
For [[global vs local alignment|local]] alignments, Karlin and Altschul give a closed form. The [[E-value (Karlin-Altschul)|E-value]] $E=Kmn\,e^{-\lambda x}$ is the **expected number** of chance alignments scoring $\ge x$; converting it gives the [[Gumbel distribution and the p-value|p-value]] $p=1-e^{-E}$ — an **extreme-value (Gumbel)** law, not a bell curve, because a local score is a **maximum**. This is the number **BLAST** reports.

## A note on the source
The lecture's printed p-value drops a minus sign; the wiki uses the correct form and documents the discrepancy in [[Karlin-Altschul p-value erratum]].

## Putting it to work
Interpret E-values and convert them to p-values in [[exercise-evalue-interpretation]].
→ Review: [[alignment-significance-key-concepts]]

## Connections
- **Role of the bioinformatician** — reading E-values is a daily act of judgement; the practitioner supplies the biological significance the statistics can't.
- **Data mining** — significance thresholds are how a database search separates signal from the noise of millions of comparisons.

## Related pages
- [[local-alignment]] (Arc 4 — the local alignments being tested)
- [[substitution-matrices]] (Arc 6 — the matrix sets $K$ and $\lambda$)

## Read aloud
This arc tackles one question: when you align two sequences and get a score, is that score meaningful or could you get it by chance? It matters because any two sequences align to some score, and the score depends on your scoring matrix, so it isn't an absolute number. There are two ways to test it. For global alignments, there's no clean formula, so you do it empirically: you shuffle one sequence many times, align each shuffle, and see how many standard deviations your real score stands above the random average — that's the Z-score. Its weakness is that it assumes a bell curve. For local alignments, Karlin and Altschul give a beautiful formula. The E-value is the expected number of chance alignments scoring at least as high, and converting it gives a probability that follows the extreme-value, or Gumbel, distribution — not a bell curve, because a local alignment score is a maximum over many possibilities. That E-value is exactly the number BLAST prints beside every hit. One caution throughout: statistical significance only says "unlikely by chance"; you always still need biological evidence before claiming the sequences are related.
