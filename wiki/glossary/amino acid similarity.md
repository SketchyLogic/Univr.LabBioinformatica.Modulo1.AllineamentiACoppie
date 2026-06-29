---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/SubstitutionMatrices
foundational: 3
prereqs: 1
density: 2
value: 3
CreatedAt: 2026-06-27
LastUpdateAt: 2026-06-27
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# amino acid similarity

To score a protein alignment we must say **how similar two amino acids are** — but *which* similarity? [[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|L4 p.4]]

**The chemist's view (insufficient).** Amino acids cluster by **physico-chemical properties** — hydrophobic, polar, charged (positive/negative), aromatic, aliphatic, tiny, small — overlapping groups usually drawn as a **Venn diagram**.

[[raw/Teoria_L4_ALGO_WS_MATRICI_DI_PUNTEGGIO.pdf#page=4|Amino-acid property Venn diagram — overlapping physico-chemical groups]]

But there is **no objective, a-priori criterion**: we cannot know in advance *which* property matters most for a given protein. Two residues "similar" by charge may be very different by size.

**The empirical fix (what actually works).** Instead of arguing about chemistry, **measure which substitutions evolution actually tolerates**. **Zuckerkandl & Pauling (1965)** counted substitution frequencies in **18 globins** (myoglobins + hemoglobins, human to lamprey): a swap seen *often* across homologs is, by definition, "conservative" — e.g. **Lys appears at 58% of Arg sites**. This *observed-substitution* idea is exactly what [[PAM (Point Accepted Mutation)|PAM]] and [[BLOSUM matrix|BLOSUM]] [[substitution matrix|matrices]] formalise.

# TLDR
We can't score amino-acid similarity from **physico-chemical properties** alone (the Venn groups) — there's no a-priori way to know which property matters. The working answer is **empirical**: count which substitutions evolution actually tolerates (Zuckerkandl & Pauling counted them in 18 globins), which is the basis of all [[substitution matrix|substitution matrices]].

# Recitation Anchors
- Need a measure of how **similar** two amino acids are
- Physico-chemical Venn groups: hydrophobic / polar / charged / aromatic / aliphatic / tiny / small
- **No objective a-priori criterion** (which property matters?)
- Fix: **measure observed substitutions** in homologs
- Zuckerkandl & Pauling (1965): **18 globins**; Lys at 58% of Arg sites
- → basis of PAM / BLOSUM

> [!Cool] Cool fact
> There is no single "right" similarity scale: the **AAindex** database catalogues **hundreds** of distinct numerical amino-acid property indices (hydrophobicity, volume, charge, flexibility…) collected from the literature — concrete proof that "amino-acid similarity" has no unique definition. [source](https://www.genome.jp/aaindex/)

# Read aloud
KP.0.Concept: The question.
To score a protein alignment, we need to say how similar any two amino acids are. But that immediately raises a question: similar in what sense?

KP.1.Concept: The chemist's view, and why it falls short.
The obvious approach is physico-chemical. Amino acids fall into overlapping groups — hydrophobic, polar, charged, aromatic, aliphatic, tiny, small — usually drawn as a Venn diagram. The trouble is there's no objective, advance way to know which property matters most for a given protein. Two residues that look similar by charge might be wildly different in size.

KP.2.Concept: The empirical fix.
So instead of arguing about chemistry, we measure what evolution actually tolerates. Zuckerkandl and Pauling, back in 1965, counted how often each substitution appeared across eighteen globins, from human to lamprey. If a swap shows up often among related proteins, then by definition it's conservative — for instance, lysine turns up at fifty-eight percent of arginine sites. That observed-substitution idea is exactly what the PAM and BLOSUM matrices later formalised.

KP.3.CoolFact: Hundreds of similarity scales.
And here's the cool part — there really is no single right answer. The AAindex database catalogues hundreds of different numerical scales for amino-acid properties — hydrophobicity, volume, charge, flexibility, and many more — gathered from the literature. That's concrete proof that amino-acid similarity simply has no unique definition.

# Question and Answer
Q. Why can't physico-chemical properties alone define amino-acid similarity?
A. There's no objective a-priori way to know which property matters most for a given protein; residues similar by one property differ by another.

Q. What physico-chemical groups are typically shown in the Venn diagram?
A. Hydrophobic, polar, charged (positive/negative), aromatic, aliphatic, tiny, small (overlapping).

Q. What is the empirical alternative to chemistry?
A. Measuring which substitutions evolution actually tolerates — counting observed substitutions in homologous proteins.

Q. What did Zuckerkandl & Pauling (1965) do?
A. Counted substitution frequencies across 18 globins (myoglobins/hemoglobins, human to lamprey) to define conservative substitutions.

Q. How does this connect to PAM and BLOSUM?
A. Both formalise the observed-substitution idea into substitution matrices.

Q. What does "Lys at 58% of Arg sites" illustrate?
A. A frequently-observed (hence conservative) substitution — empirical similarity, not chemical assumption.
