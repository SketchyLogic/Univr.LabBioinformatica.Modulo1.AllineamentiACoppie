---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/MolecularEvolution
  - MODULE__/AlignmentFoundations
  - EXAM_PREP
foundational: 4
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

# orthologs

**Orthologs** are **[[homology|homologous]] sequences in *different species* that descend, via *speciation*, from a common ancestral gene.** [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=4|L3 p.4]]

The defining event is **speciation**: one ancestral gene, present in an ancestral species, is inherited by the descendant species when that lineage splits. The "same" gene in mouse, frog, and chicken — e.g. the α-globin gene in each — are orthologs of one another.

Key nuance: their function **may or may not be similar**. Speciation does not force the gene to keep its old job, though orthologs *often* retain function (the "ortholog conjecture").

Contrast with [[paralogs]] (same species, born of gene **duplication**); the full comparison is in [[orthologs vs paralogs]]. Both are types of homology, distinguished only by the **event** that separated the copies.

> [!Hint] Mnemonic
> **Ortho**logs = **O**ther organisms (different species, via speciation). **Para**logs = in **Pa**rallel within one genome (gene duplication).

# TLDR
Orthologs are **homologous genes in *different species*** that descend, via a **speciation** event, from one common ancestral gene. Their function may or may not be conserved (often is).

# Recitation Anchors
- Orthologs = **different species**, via **speciation**
- One ancestral gene → each new species inherits a copy
- Function **may or may not** be conserved (often retained)
- Example: α-globin in mouse / frog / chicken
- Mnemonic: **Ortho = Other organisms**

> [!Cool] Cool fact
> Ortholog identification is the backbone of comparative genomics: the **OrthoDB** database tracks orthologous groups across **tens of thousands** of species, from bacteria to vertebrates, precisely because orthologs are the best guess for "the same gene" in another organism. [source](https://www.orthodb.org)

# Read aloud
KP.0.Definition: What orthologs are.
Orthologs are homologous sequences found in different species that descend, through speciation, from one common ancestral gene.

KP.1.Concept: The defining event is speciation.
The key is the event that separated them: speciation. Picture one gene sitting in an ancestral species. When that lineage splits into two new species, each inherits a copy. Those copies, now in different organisms, are orthologs. The alpha-globin gene in a mouse, a frog, and a chicken are all orthologs of each other.

KP.2.Concept: Function may or may not be conserved.
A subtle but important point: orthologs may or may not keep the same function. Speciation doesn't compel the gene to hold onto its old job, although in practice orthologs often do keep their function.

KP.3.Connection: How they differ from paralogs.
The mirror image of an ortholog is a paralog, which arises within a single species from gene duplication. Both are homologs; what distinguishes them is simply the event that created the split — speciation for orthologs, duplication for paralogs.

KP.4.CoolFact: The backbone of comparative genomics.
And here's the cool part — finding orthologs is the foundation of comparative genomics. Databases like OrthoDB catalogue orthologous groups across tens of thousands of species, from bacteria to vertebrates, because orthologs are our best bet for spotting the same gene in another organism.

# Question and Answer
Q. Define orthologs.
A. Homologous sequences in different species derived, via speciation, from a common ancestral gene.

Q. What event creates orthologs?
A. Speciation — the splitting of one lineage into separate species, each inheriting the ancestral gene.

Q. Do orthologs necessarily have the same function?
A. No — function may or may not be conserved, though orthologs often retain it.

Q. Give an example of orthologs.
A. The α-globin gene in mouse, frog, and chicken — the "same" gene across different species.

Q. How do orthologs differ from paralogs?
A. Orthologs separate by speciation (different species); paralogs separate by gene duplication (same species). See [[orthologs vs paralogs]].

Q. What mnemonic distinguishes the two?
A. Ortho = Other organisms (speciation); Para = in Parallel within one genome (duplication).
