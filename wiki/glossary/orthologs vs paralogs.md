---
tags:
  - TYPE__/Concept/Argument
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

# orthologs vs paralogs

Both [[orthologs]] and [[paralogs]] are kinds of [[homology]] — sequences descended from a common ancestor. They differ **only in the event** that separated the copies. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=4|L3 p.4]]

| | **Orthologs** | **Paralogs** |
|---|---|---|
| **Separating event** | **Speciation** | **Gene duplication** |
| **Where the copies sit** | Different **species** | Same **species** (genome) |
| **Function** | May or may not be similar (often retained) | Often diverge / new related functions |
| **Globin example** | α-globin in human vs mouse vs chicken | α-globin vs β-globin vs myoglobin (all human) |

Both are often drawn on **one tree**: start from an "early globin gene"; a **gene duplication** splits it into the α-chain and β-chain lineages (the two halves are **paralogs**); subsequent **speciations** then propagate each chain into frog, chicken, mouse, etc. (corresponding chains across species are **orthologs**). [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=4|combined homology tree, L3 p.4]]

> [!Hint] Read the tree by the node type
> At any branch point, ask *what split here?* A **speciation** node → the descendants are orthologs. A **duplication** node → the descendants are paralogs.

# TLDR
Both orthologs and paralogs are homologs; they differ **only in the splitting event** — speciation (orthologs, different species) vs gene duplication (paralogs, same genome). Orthologs are the more reliable basis for transferring functional annotation.

# Recitation Anchors
- Both are homologs; differ **only by the separating event**
- Orthologs: **speciation**, different species
- Paralogs: **duplication**, same genome
- Read the tree by node: speciation → orthologs, duplication → paralogs
- Orthologs more reliable for transferring function

> [!Cool] Cool fact
> The distinction has real clinical weight: when transferring gene-function annotations between species, **orthologs** are far more reliable predictors of function than paralogs — getting ortholog vs paralog wrong is a notorious source of mis-annotation in genome databases. [source](https://doi.org/10.1371/journal.pcbi.1002386)

# Read aloud
KP.0.Concept: What they share.
Orthologs and paralogs are both kinds of homology — both are sequences that descend from a common ancestor. The only thing that separates them is the event that split the copies apart.

KP.1.Definition: The two events.
Orthologs are split by speciation, so the copies end up in different species. Paralogs are split by gene duplication, so the copies sit together in the same genome. That single difference — speciation versus duplication — is the whole distinction.

KP.2.Concept: Function.
Their fates differ too. Orthologs often, though not always, keep the same function across species. Paralogs, since one copy can cover the original job, are freer to drift and take on new but related functions.

KP.3.Connection: Reading the globin tree.
Both show up on one tree. Start with an early globin gene. A duplication splits it into the alpha-chain and beta-chain lineages — those two halves are paralogs of each other. Then speciation carries each chain into frog, chicken, mouse, and human — and the matching chains across those species are orthologs. So you read the tree by the node: a speciation node gives orthologs, a duplication node gives paralogs.

KP.4.CoolFact: Why the distinction matters clinically.
And here's the cool part — this isn't just terminology. When scientists guess a gene's function by comparing it to another species, orthologs are far more trustworthy than paralogs. Confusing the two is a well-known cause of wrong annotations in genome databases.

# Question and Answer
Q. What single thing distinguishes orthologs from paralogs?
A. The separating event: speciation (orthologs) vs gene duplication (paralogs).

Q. Where do the copies reside in each case?
A. Orthologs: different species. Paralogs: the same species/genome.

Q. In a phylogenetic tree, how do you tell which is which?
A. By the node type: a speciation node yields orthologs; a duplication node yields paralogs.

Q. Give a globin example of each.
A. Orthologs: human vs mouse α-globin. Paralogs: human α-globin vs β-globin vs myoglobin.

Q. Which type is more reliable for transferring functional annotation, and why?
A. Orthologs — they more reliably retain the ancestral function across species.

Q. Are both orthologs and paralogs homologous?
A. Yes — both descend from a common ancestor; only the splitting event differs.
