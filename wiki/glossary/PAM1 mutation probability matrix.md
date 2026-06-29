---
tags:
  - TYPE__/Concept/Model
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/SubstitutionMatrices
foundational: 3
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

# PAM1 mutation probability matrix

The **PAM1 mutation probability matrix** is Dayhoff's starting point: a 20×20 table whose entry $M_{ij}$ is the **probability that the (column) amino acid $j$ is replaced by the (row) amino acid $i$** over **one [[PAM (Point Accepted Mutation)|PAM]] of evolution** (1% divergence). [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=8|L4 p.8]]

**How it's built (counts → probabilities):**
1. Count **observed substitutions** between aligned, closely-related sequences (the count matrix, Dayhoff 1978).
2. Weight by each residue's [[relative mutability]] and normalise so the **overall change is exactly 1%** (hence "PAM**1**").
3. The result is a **probability** matrix.

**What it looks like:** the **diagonal ≈ 99%** — at 1% divergence almost every residue stays the same (e.g. A→A ≈ 98.6%); off-diagonal entries are tiny (fractions of a percent). Each **column sums to 1** (the original residue must become *something*). This single matrix is then **[[PAM matrix extrapolation|raised to powers]]** to reach every larger evolutionary distance, and converted via [[log-odds score|log-odds]] into the score matrix you actually align with.

> [!Caution] Probability matrix vs score matrix
> PAM1 here holds **probabilities** (≈99% on the diagonal). The familiar **PAM250 score matrix** (with values like +17, −5) is a *different* object — a [[log-odds score|log-odds]] transform of an *extrapolated* probability matrix. Don't conflate the two.

# TLDR
The **PAM1 mutation probability matrix** gives the probability each amino acid is replaced by another over **1% divergence** (one PAM). Built from observed substitution **counts** weighted by [[relative mutability]] and normalised to 1% change, its **diagonal is ≈99%** and each **column sums to 1**. It's the seed matrix that gets [[PAM matrix extrapolation|raised to powers]] for larger distances.

# Recitation Anchors
- $M_{ij}=P(j \to i)$ over **one PAM** (1% divergence)
- Built: observed **counts** → weight by mutability → normalise to **1% change**
- **Diagonal ≈ 99%** (A→A ≈ 98.6%); off-diagonal tiny
- **Columns sum to 1** (original aa becomes something)
- Seed for [[PAM matrix extrapolation]]; later log-odds-transformed into scores

> [!Cool] Cool fact
> Dayhoff's original PAM1 was estimated from just **1,572 observed amino-acid changes** across **71 families** of closely related proteins — a tiny dataset by modern standards, yet it underpinned protein sequence analysis for **decades** before bigger databases enabled BLOSUM. [source](https://en.wikipedia.org/wiki/Point_accepted_mutation)

# Read aloud
KP.0.Definition: What PAM1 is.
The PAM-one mutation probability matrix is Dayhoff's starting point. It's a twenty-by-twenty table where each entry is the probability that one amino acid gets replaced by another over a single PAM of evolution — that is, one percent divergence.

KP.1.Procedure: From counts to probabilities.
It's built in steps. First, count the substitutions actually observed between aligned, closely related sequences — that's the count matrix. Then weight those by each residue's mutability and normalise everything so the overall change is exactly one percent, which is why it's called PAM-one. The result is a probability matrix.

KP.2.Concept: What it looks like.
At one percent divergence almost nothing changes, so the diagonal is about ninety-nine percent — for example, alanine stays alanine about ninety-eight point six percent of the time. The off-diagonal entries are tiny, fractions of a percent. Each column sums to one, because the original residue has to become something. This single matrix is then raised to powers to reach every larger evolutionary distance, and converted by log-odds into the score matrix you actually align with.

KP.3.Connection: Probability versus score.
Don't confuse this with the famous PAM-two-fifty score matrix that has values like plus seventeen and minus five. That's a different object — a log-odds transform of an extrapolated probability matrix. PAM-one here holds plain probabilities.

KP.4.CoolFact: A tiny but mighty dataset.
And here's the cool part — Dayhoff's original PAM-one was estimated from just one thousand five hundred seventy-two observed amino-acid changes across seventy-one families of closely related proteins. That's a minuscule dataset by today's standards, yet it underpinned protein sequence analysis for decades, until bigger databases made BLOSUM possible.

# Question and Answer
Q. What does an entry of the PAM1 mutation probability matrix represent?
A. The probability that a (column) amino acid is replaced by a (row) amino acid over one PAM (1% divergence).

Q. How is PAM1 constructed from data?
A. Count observed substitutions, weight by relative mutability, and normalise so the total change is exactly 1%.

Q. What does the diagonal of PAM1 look like, and why?
A. About 99% (e.g. A→A ≈ 98.6%) — at 1% divergence almost every residue stays the same.

Q. Why does each column sum to 1?
A. The original residue must end up as some amino acid (probabilities over all outcomes total 1).

Q. How is PAM1 used to get other PAM matrices?
A. It is raised to integer powers (PAM1ⁿ) to model larger evolutionary distances.

Q. How does the PAM1 probability matrix differ from the PAM250 score matrix?
A. PAM1 holds probabilities (~99% diagonal); PAM250 score is a log-odds transform of an extrapolated matrix (values like +17, −5).
