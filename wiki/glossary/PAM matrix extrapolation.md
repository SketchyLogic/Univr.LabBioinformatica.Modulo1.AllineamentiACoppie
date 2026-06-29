---
tags:
  - TYPE__/Concept/Procedure
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/SubstitutionMatrices
  - EXAM_PREP
foundational: 4
prereqs: 3
density: 4
value: 5
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# PAM matrix extrapolation

How do you get **PAM250** when your data only gave you **PAM1**? You **multiply the matrix by itself**. The key idea: raising the [[PAM1 mutation probability matrix]] to the power *n* simulates **n steps of evolution**. [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=9|L4 p.9]]

$$\text{PAM}_n = (\text{PAM}_1)^n$$

This works because mutation is modelled as a **Markov process**: each evolutionary step applies the same per-step probabilities, so *n* steps = the matrix multiplied *n* times.

**The three landmark cases:**

| Matrix | = | Meaning |
|---|---|---|
| **PAM0** | identity matrix | **0 steps** — nothing has changed (100% on the diagonal) |
| **PAM250** | $(\text{PAM}_1)^{250}$ | ~**20% conserved**; A→A ≈ 13%; **W, C still ≈ 50%** unchanged |
| **PAM2000** | $(\text{PAM}_1)^{2000}$ | every column → **background frequencies** = pure **chance** |

![[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=9|PAM0 (identity) and PAM2000 (chance) — the two extremes of extrapolation]]

The progression **PAM0 → PAM250 → PAM2000** runs from "no change" through "twilight" to "indistinguishable from random". The extrapolated probability matrix is then turned into a [[log-odds score|log-odds]] score matrix for use in alignment.

> [!Hint] Why PAM2000 = chance
> As $n\to\infty$ a Markov chain **forgets its starting state** and settles into a fixed **stationary distribution** — here the [[amino acid frequencies|background frequencies]]. So in PAM2000 every column is the *same* (the frequencies): knowing the original residue tells you nothing. That is exactly "by chance".

# TLDR
PAM matrices for large distances are made by **matrix multiplication**: $\text{PAM}_n=(\text{PAM}_1)^n$, modelling *n* steps of a **Markov** evolutionary process. **PAM0** = identity (no change); **PAM250** ≈ 20% conserved; **PAM2000** → background frequencies (pure chance, the Markov chain's stationary state). The result is then log-odds-transformed into a score matrix.

# Recitation Anchors
- $\text{PAM}_n = (\text{PAM}_1)^n$ — *n* multiplications = *n* evolutionary steps
- Works because mutation is a **Markov process**
- **PAM0** = identity (0 steps, nothing changed)
- **PAM250** ≈ 20% conserved (A→A 13%; W, C ≈ 50%)
- **PAM2000** → background frequencies = **chance** (stationary distribution)
- Then [[log-odds score|log-odds]] transform → score matrix

> [!Cool] Cool fact
> PAM extrapolation is a textbook **Markov chain converging to its stationary distribution**: push the power high enough and the matrix *completely forgets* the original amino acid — every column becomes the same background frequencies. PAM2000 is literally the chain's equilibrium, the mathematical face of "all evolutionary signal has decayed to noise." [source](https://en.wikipedia.org/wiki/Point_accepted_mutation)

# Read aloud
KP.0.Concept: The core trick.
Here's a puzzle: your data only gave you PAM-one, the matrix for one percent divergence. How do you get PAM-two-fifty? The answer is to multiply the matrix by itself. Raising the PAM-one matrix to the power n simulates n steps of evolution.

KP.1.Concept: Why multiplication works.
This works because mutation is modelled as a Markov process. Each step of evolution applies the same per-step probabilities, so n steps of evolution is just the matrix multiplied by itself n times.

KP.2.Numbers: The three landmarks.
Three cases are worth memorising. PAM-zero is the identity matrix — zero steps, nothing has changed, a hundred percent on the diagonal. PAM-two-fifty, the matrix raised to the two-hundred-fiftieth power, leaves only about twenty percent conserved; alanine stays alanine just thirteen percent of the time, though tryptophan and cysteine still hold at around fifty percent. And PAM-two-thousand pushes things so far that every column converges to the background frequencies — pure chance.

KP.3.Concept: Why PAM2000 is chance.
The reason PAM-two-thousand equals chance is a property of Markov chains: as you take more and more steps, the chain forgets its starting state and settles into a fixed stationary distribution — here, the background amino-acid frequencies. So in PAM-two-thousand every column is identical, and knowing the original residue tells you nothing at all. That's the definition of by chance. The extrapolated matrix is then turned into log-odds scores for actual alignment.

KP.4.CoolFact: Forgetting the start.
And here's the cool part — PAM extrapolation is a textbook example of a Markov chain converging to equilibrium. Push the power high enough and the matrix completely forgets the original amino acid: every column becomes the same set of background frequencies. PAM-two-thousand is literally the chain's equilibrium — the mathematical face of all evolutionary signal decaying into noise.

# Question and Answer
Q. How are higher PAM matrices obtained from PAM1?
A. By matrix multiplication: $\text{PAM}_n=(\text{PAM}_1)^n$, modelling *n* steps of evolution.

Q. Why does raising PAM1 to a power model evolutionary time?
A. Mutation is a Markov process with fixed per-step probabilities, so *n* steps = the matrix multiplied *n* times.

Q. What is PAM0?
A. The identity matrix — zero evolutionary steps, nothing changed (100% diagonal).

Q. What does PAM250 imply about conservation?
A. About 20% of residues are conserved (A→A ≈ 13%, though W and C stay ~50%).

Q. What does PAM2000 converge to, and why?
A. The background amino-acid frequencies (pure chance) — the Markov chain's stationary distribution, having forgotten the original residue.

Q. What is done to the extrapolated probability matrix before alignment?
A. It is converted into a log-odds score matrix.
