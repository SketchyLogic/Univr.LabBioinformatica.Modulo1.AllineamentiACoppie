---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/AlignmentFoundations
foundational: 5
prereqs: 2
density: 2
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# homology

**Homology** is **similarity attributed to descent from a common ancestor.** Two sequences (or genes, or proteins) are homologous if they share a common **phylogenetic origin** — they evolved from the same ancestral sequence. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=2|L3 p.2]]

The crucial property: **homology is a *qualitative* character — it is yes/no.** Two sequences either share a common ancestor or they do not; there is no "percent homology". This is the heart of [[homology vs similarity]].

Because [[sequence structure function|sequence determines structure, and structure determines function]], homology is biologically powerful: if a protein is **conserved** across different organisms (i.e. forms a protein **family**), it is reasonable to assume its members carry out **similar or correlated functions**. This licenses **function prediction**:

1. Identify the proteins of a **family** (evolved from a common progenitor → reasonably similar sequences).
2. Identify, via [[pairwise alignment]], the residues that play an analogous **structural or functional** role.

Homology comes in two flavours by the event that created it — [[orthologs]] (speciation) and [[paralogs]] (gene duplication).

> [!Caution] "Homologous", not "homologous to 80%"
> You may say two sequences *are* homologous, or share *X% identity/similarity* — but never that they are "80% homologous". Homology is the qualitative inference; identity and [[identity conservation similarity|similarity]] are the quantitative evidence for it.

# TLDR
Homology is **similarity attributed to descent from a common ancestor** — a *qualitative*, yes/no property (never a percentage), inferred from measured identity/similarity and used to predict function across a protein family.

# Recitation Anchors
- Homology = **shared common ancestor** (phylogenetic origin)
- **Qualitative, yes/no** — there is no "percent homology"
- sequence→structure→function ⇒ conserved family ⇒ shared function
- Function prediction: (1) identify family, (2) align to find analogous residues
- Two flavours: **orthologs** (speciation) vs **paralogs** (duplication)

> [!Cool] Cool fact
> Homology can be detected across staggering time spans: the histone protein **H4** is so conserved that cow and pea H4 differ by only **2 amino acids out of 102** — sequences that diverged well over a billion years ago are still unmistakably homologous. [source](https://www.ncbi.nlm.nih.gov/books/NBK26830/)

# Read aloud
KP.0.Definition: What homology is.
Homology means similarity that comes from sharing a common ancestor. Two sequences are homologous when they descend from the same ancestral sequence — when they have a shared evolutionary origin.

KP.1.Concept: Homology is yes or no.
The most important thing to grasp is that homology is qualitative. It's a yes-or-no property. Two sequences either share a common ancestor or they don't. There is no such thing as being eighty percent homologous.

KP.2.Connection: Why homology lets us predict function.
Homology is biologically powerful because sequence shapes structure, and structure dictates function. So if a protein stays conserved across many organisms — forming what we call a protein family — it's reasonable to assume its members do similar or related jobs. That's the basis of function prediction.

KP.3.Procedure: Predicting function in two steps.
The recipe has two steps. First, identify the members of a protein family, the ones that evolved from a common ancestor and so have fairly similar sequences. Second, use pairwise alignment to pinpoint the residues that play the same structural or functional role across them.

KP.4.Connection: Two kinds of homology.
Homology comes in two flavours depending on the event that created it: orthologs, born from a speciation event, and paralogs, born from a gene duplication.

KP.5.CoolFact: A billion years of conservation.
And here's the cool part — homology can survive enormous spans of time. The histone protein H4 is so tightly conserved that the versions in a cow and in a pea differ by only two amino acids out of a hundred and two, even though their lineages split more than a billion years ago.

# Question and Answer
Q. Define homology.
A. Similarity attributed to descent from a common ancestor; shared phylogenetic origin.

Q. Is homology qualitative or quantitative? Why does it matter?
A. Qualitative — it's yes/no. There is no "percent homology"; you only quote percent identity/similarity as evidence.

Q. How does homology enable function prediction?
A. Because sequence→structure→function, conserved (homologous) proteins likely share function; align family members to find functionally analogous residues.

Q. What are the two steps of homology-based function prediction?
A. (1) Identify the protein family (common progenitor, similar sequences); (2) align to find residues with an analogous structural/functional role.

Q. What two events produce the two types of homology?
A. Speciation (→ [[orthologs]]) and gene duplication (→ [[paralogs]]).

Q. Why is "these proteins are 80% homologous" wrong?
A. Homology is not a percentage; you can be 80% identical/similar, but homology itself is simply present or absent.
