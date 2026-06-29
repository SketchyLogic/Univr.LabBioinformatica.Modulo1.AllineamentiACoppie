---
tags:
  - TYPE__/Concept/Argument
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
foundational: 4
prereqs: 3
density: 3
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# PAM vs BLOSUM

Both are [[substitution matrix|substitution matrices]] of [[log-odds score|log-odds]] scores, but they're built on **opposite philosophies** — and, crucially, their **numbering runs in opposite directions**. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=12|L4 p.12]]

| | **[[PAM (Point Accepted Mutation)\|PAM]]** | **[[BLOSUM matrix\|BLOSUM]]** |
|---|---|---|
| Basis | **evolutionary model** (assumes homology) | **empirical** (observed alignments, no assumption) |
| Built from | **global** alignments of **closely related** proteins | **local** blocks of **distantly related** proteins |
| Extrapolation | yes — [[PAM matrix extrapolation\|matrix powers]] from PAM1 | no — each counted directly |
| **Higher number** = | **MORE** divergent (PAM250 = distant) | **LESS** divergent (BLOSUM80 = close) |

> [!Danger] The classic exam trap — inverse numbering
> **High PAM = distant; high BLOSUM = close.** A *low* BLOSUM (e.g. 45) is for *distant* sequences; a *low* PAM (e.g. 1) is for *close* ones. Mnemonic: **"low number, low divergence"** is true for **PAM** but **false** for **BLOSUM**.

**Rough correspondences** (lecture): **BLOSUM80 ≈ PAM1** (mouse vs rat — conserved), **BLOSUM62 ≈ PAM120**, **BLOSUM45 ≈ PAM250** (mouse vs bacterium — divergent). BLOSUM80 / PAM1 suit *similar* proteins; BLOSUM45 / PAM250 suit *different* ones. In practice **BLOSUM62** is the everyday default because it performs well across the broad middle and especially for **remote** homologs.

# TLDR
**PAM** is an **evolutionary model** (extrapolated from close, global alignments); **BLOSUM** is **empirical** (counted from distant, local blocks). Their numbering is **inverse**: **high PAM = distant, high BLOSUM = close**. Correspondences: BLOSUM80≈PAM1, BLOSUM62≈PAM120, BLOSUM45≈PAM250. BLOSUM62 is the everyday default.

# Recitation Anchors
- PAM = **evolutionary/model**, extrapolated; BLOSUM = **empirical**, directly counted
- PAM from **global/close**; BLOSUM from **local/distant**
- **Inverse numbering**: high PAM = distant, high BLOSUM = close ⚠
- "low number low divergence" → true for PAM, false for BLOSUM
- BLOSUM80≈PAM1, BLOSUM62≈PAM120, BLOSUM45≈PAM250
- BLOSUM62 = default; best for **remote** homologs

> [!Cool] Cool fact
> The inverse numbering exists because the two scales measure **opposite things**: PAM counts *accumulated mutations* (more = more diverged), while BLOSUM's number is the *clustering identity %* of the sequences used (more = more similar). When BLOSUM62 was shown to beat PAM at detecting **distant** homologs, it **dethroned PAM** as the default for tools like BLAST. [source](https://doi.org/10.1073/pnas.89.22.10915)

# Read aloud
KP.0.Concept: Two philosophies.
PAM and BLOSUM are both substitution matrices made of log-odds scores, but they're built on opposite philosophies, and — this is the part that trips people up — their numbering runs in opposite directions.

KP.1.Concept: How each is built.
PAM is an evolutionary model: it assumes homology and extrapolates from closely related proteins aligned globally, raising PAM-one to powers. BLOSUM is empirical: it just counts substitutions in local blocks of distantly related proteins, with no evolutionary assumption at all.

KP.2.Concept: The inverse numbering trap.
Now the trap. For PAM, a higher number means more divergent — PAM-two-fifty is for distant sequences. For BLOSUM, a higher number means less divergent — BLOSUM-eighty is for close sequences. So a low BLOSUM, like forty-five, is actually for distant sequences, while a low PAM, like one, is for close ones. The mnemonic "low number means low divergence" is true for PAM but false for BLOSUM.

KP.3.Numbers: The correspondences.
Roughly, BLOSUM-eighty matches PAM-one — think mouse versus rat, highly conserved. BLOSUM-sixty-two matches PAM-one-twenty. And BLOSUM-forty-five matches PAM-two-fifty — think mouse versus bacterium, very divergent. In everyday practice BLOSUM-sixty-two is the default, because it works well across the broad middle and especially for remote homologs.

KP.4.CoolFact: Why opposite, and the dethroning.
And here's the cool part — the numbering is inverse because the two scales measure opposite things. PAM counts accumulated mutations, so more means more diverged. BLOSUM's number is the clustering identity percentage of the sequences it was built from, so more means more similar. When BLOSUM-sixty-two was shown to beat PAM at spotting distant homologs, it dethroned PAM as the default in tools like BLAST.

# Question and Answer
Q. What is the fundamental difference in how PAM and BLOSUM are built?
A. PAM is an evolutionary model extrapolated from closely-related global alignments; BLOSUM is empirical, counted from distantly-related local blocks.

Q. How does the numbering differ between PAM and BLOSUM?
A. Inversely: high PAM = more divergent; high BLOSUM = more similar.

Q. Which matrix would you use for very divergent sequences — high or low BLOSUM? PAM?
A. Low BLOSUM (e.g. 45) and high PAM (e.g. 250).

Q. Give the rough PAM↔BLOSUM correspondences.
A. BLOSUM80≈PAM1, BLOSUM62≈PAM120, BLOSUM45≈PAM250.

Q. Why does the numbering run in opposite directions?
A. PAM counts accumulated mutations (more = diverged); BLOSUM's number is the clustering identity % (more = similar).

Q. Which is the everyday default and why?
A. BLOSUM62 — it performs well broadly and is better for remote homologs, which is why it replaced PAM in BLAST.
