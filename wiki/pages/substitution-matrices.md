---
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Substitution Matrices (Arc 6)

**Summary**: Where do the per-residue scores in protein alignment *come from*? This arc derives them from **evolution**: how to quantify amino-acid similarity, the **PAM** family (Dayhoff's accepted mutations + matrix powers + log-odds), the **BLOSUM** family, how the two **compare**, and the **twilight zone** where sequence similarity runs out.
**Sources**: [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf|Teoria L4, slides 15–48]]

---

## Quantifying amino-acid similarity
A protein [[scoring matrix]] needs a notion of how interchangeable two residues are. Physico-chemical properties ([[amino acid similarity]]) give intuition but **no objective rule**, so we instead **count observed substitutions** — the empirical idea behind every [[substitution matrix]] (20×20, symmetric).

## The PAM family
[[PAM (Point Accepted Mutation)|PAM]] = *point accepted mutation*, a fixed amino-acid change. Dayhoff built the [[PAM1 mutation probability matrix]] from close homologs (using [[relative mutability]] and background [[amino acid frequencies]]), then reached every distance by [[PAM matrix extrapolation|raising it to powers]] — PAM0 (identity) → PAM250 (~20% conserved) → PAM2000 (chance).

## The log-odds score — the shared engine
Both families convert probabilities into scores with the **[[log-odds score]]** $s=10\log(q/p)$: observed-over-chance, logged (so scores **add**), ×10 (to keep a decimal). This is what makes a matrix's numbers — e.g. PAM250's $s(W,W)\approx17$ — meaningful.

## The BLOSUM family
[[BLOSUM matrix|BLOSUM]] = *BLOck SUbstitution Matrix*, built **empirically** from conserved **local blocks** of distant sequences; **BLOSUM62** is BLAST's default.

## PAM vs BLOSUM
[[PAM vs BLOSUM]] is the classic comparison — model vs empirical, and the **inverse numbering** trap (high PAM = distant, high BLOSUM = close).

## The twilight zone
Identity decays exponentially with distance; below ~20–25% you hit the [[twilight zone]], where homology can no longer be seen from sequence alone.

## Putting it to work
- [[exercise-blosum62-scoring]] — score an alignment with BLOSUM62 → 15.
- [[exercise-log-odds-score]] — compute $s(W,W)\approx17.4$.
→ Review: [[substitution-matrices-key-concepts]]

## Connections
- **Precision/personalized medicine** — substitution scores underlie variant-effect interpretation (is an amino-acid change conservative or damaging?).
- **Data mining** — PAM extrapolation is a **Markov process**; the twilight zone is where signal decays into noise.

## Related pages
- [[dot-plots]] (Arc 2 — the generic [[scoring matrix]] these refine)
- [[alignment-significance]] (Arc 5 — the matrix sets the constants $K$, $\lambda$)
- [[local-alignment]] (Arc 4 — where the matrix is actually applied)

## Read aloud
This arc answers a question the earlier lectures left open: where do the per-residue scores in protein alignment actually come from? The answer is evolution. First, we need a way to say how similar two amino acids are. Physical and chemical properties give intuition, but there's no objective rule for which property matters, so instead we count the substitutions that evolution actually tolerates. That empirical idea is the foundation of every substitution matrix, a twenty-by-twenty symmetric table. The first family is PAM, for point accepted mutation. Margaret Dayhoff built a matrix for one percent divergence from closely related proteins, then reached every larger distance by raising that matrix to powers — from PAM-zero, the identity, through PAM-two-fifty, to PAM-two-thousand, which is pure chance. Both families turn probabilities into scores using the log-odds formula: observed over chance, logged so scores add, times ten to keep a decimal. The second family is BLOSUM, built empirically from conserved local blocks of distant sequences, and BLOSUM-sixty-two is the BLAST default. The two families invite a classic comparison — model versus empirical — with a famous trap: the numbering runs in opposite directions. Finally, identity decays exponentially with distance, and below about twenty to twenty-five percent you reach the twilight zone, where you can no longer detect homology from sequence alone and must turn to structure.
