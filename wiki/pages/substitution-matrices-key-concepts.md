---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Key Concepts — Substitution Matrices

**Summary**: Exam-ready review sheet for [[substitution-matrices|Arc 6]]. Quantifying amino-acid similarity, the PAM and BLOSUM families, the log-odds engine, and the twilight zone.

---

## Definitions
- **[[substitution matrix]]** — 20×20, symmetric table of log-odds scores ∝ P(*i*→*j*).
- **[[amino acid similarity]]** — measured empirically (observed substitutions), not from chemistry.
- **[[PAM (Point Accepted Mutation)]]** — an accepted (fixed) amino-acid mutation; a unit of evolutionary distance.
- **[[relative mutability]]** / **[[amino acid frequencies]]** — how often a residue *changes* / *occurs*.
- **[[PAM1 mutation probability matrix]]** → **[[PAM matrix extrapolation]]** — seed matrix, raised to powers.
- **[[log-odds score]]** — $s=10\log(q/p)$, the score engine shared by PAM and BLOSUM.
- **[[BLOSUM matrix]]** — empirical, from BLOCKS; **[[PAM vs BLOSUM]]** — model vs empirical, inverse numbering.
- **[[twilight zone]]** — ~20–25% identity; homology undetectable from sequence below it.

## Key formulas
$$\text{PAM: } s_{ij}=10\log\frac{q_{ij}}{p_{ij}} \qquad \text{BLOSUM: } S_{ij}=\frac1\lambda\log\frac{p_{ij}}{q_iq_j}\ (\lambda=2) \qquad \text{PAM}_n=(\text{PAM}_1)^n$$

## Procedures
**Build PAM:** ≥85% families → align → infer ancestors → count → PAM1 (≈99% diagonal) → raise to powers → log-odds.
**Build BLOSUM:** BLOCKS local blocks → cluster at *n*% identity → count → log-odds (BLOSUM*n*).

## Questions & answers
Q. Why measure similarity empirically? → No objective a-priori rule for which chemical property matters.
Q. What is a PAM? → An accepted (fixed) amino-acid mutation; 1 PAM = 1 change/100 residues.
Q. How are high PAM matrices made? → $(\text{PAM}_1)^n$ — matrix powers (a Markov process).
Q. What does PAM2000 converge to? → Background frequencies (pure chance).
Q. Why log-odds? → Observed/chance, logged so scores **add**; ×10 keeps a decimal.
Q. PAM vs BLOSUM numbering? → **Inverse**: high PAM = distant, high BLOSUM = close.
Q. BLOSUM62 means? → Clustered at 62% identity; BLAST default.
Q. What is the twilight zone? → ~20–25% identity; homology no longer detectable from sequence.

## Key facts / numbers
- $s(W,W)\approx17$ on PAM250 (~50× chance); BLOSUM62 W·W = **+11** (highest).
- PAM1 ≈ 99% diagonal; PAM250 ≈ 20% conserved; PAM2000 = chance.
- Correspondences: BLOSUM80≈PAM1, BLOSUM62≈PAM120, BLOSUM45≈PAM250.
- Ubiquitin ≈ 0 PAMs/100 My (most conserved); Ig kappa ≈ 37 (fastest).
- Worked: [[exercise-blosum62-scoring]] (→15), [[exercise-log-odds-score]] (→17.4).
