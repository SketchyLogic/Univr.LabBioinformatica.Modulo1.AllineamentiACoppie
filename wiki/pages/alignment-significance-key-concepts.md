---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Key Concepts — Alignment Significance

**Summary**: Exam-ready review sheet for [[alignment-significance|Arc 5]]. Why a score needs a null model, the global Z-score, and the local E-value / Gumbel p-value.

---

## Definitions
- **[[statistical significance of an alignment]]** — is the score better than chance? (Score is *not* absolute.)
- **[[Z-score (alignment)]]** — global significance by shuffling: SDs above the random mean.
- **[[E-value (Karlin-Altschul)]]** — local: expected *number* of chance alignments scoring ≥ x.
- **[[Gumbel distribution and the p-value]]** — converts E to a probability; extreme-value law.

## Key formulas
$$Z = \frac{S-\mu}{\sigma} \qquad E(S\ge x) = K m n\, e^{-\lambda x} \qquad p(S\ge x) = 1 - e^{-E}$$
- $\mu,\sigma$ = mean/SD of **shuffled** scores · $m,n$ = lengths · $K$ = matrix constant · $\lambda$ = score scale.
- ⚠ Slide 14 mis-prints $p$ (drops the minus) — see [[Karlin-Altschul p-value erratum]].

## Procedures
**Z-score (global):** fix A → shuffle B *n*× → align each → mean/SD → $Z=(S-\mu)/\sigma$.
**E-value (local):** compute $E=Kmn\,e^{-\lambda x}$ → $p=1-e^{-E}$ → compare to threshold (e.g. 0.01).

## Questions & answers
Q. Why does a score need a null model? → Any two sequences align to *some* score; meaning is relative to chance.
Q. Global vs local significance tool? → Z-score (shuffling) vs E-value (Karlin–Altschul).
Q. What is the E-value — probability or count? → Expected *count* of chance hits ≥ x (can exceed 1).
Q. Why Gumbel, not Gaussian? → A local score is a **maximum** over many sub-alignments (fat tail).
Q. $Z=0$ means? → No better than random.
Q. Relation of $p$ and $E$ for small $E$? → $p \approx E$.
Q. Statistical significance enough? → No — need biological significance too.

## Key facts / numbers
- $E \propto mn$ (search space) $\times\, e^{-\lambda x}$ (score rarity).
- Best random local score grows like $\ln(mn)/\lambda$ (logarithmic).
- Common thresholds: $p<0.01$; BLAST default Expect = 10.
- Worked numbers: [[exercise-evalue-interpretation]].
