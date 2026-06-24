---
tags:
  - TYPE__/Concept/Argument
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentFoundations
foundational: 4
prereqs: 2
density: 3
value: 4
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# sequence structure function

The logical chain that makes [[pairwise alignment]] biologically meaningful: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=3|L3 p.3]]

$$\text{sequence} \;\longrightarrow\; \text{structure} \;\longrightarrow\; \text{function}$$

1. **Sequence → structure.** A protein's 3-D structure is *determined by* its amino-acid sequence. This is the principle behind **protein folding**: the sequence carries the information needed to fold.
2. **Structure → function.** The 3-D structure determines the protein's **molecular function** (what it binds, catalyses, etc.).

The payoff for evolution: if a protein sequence is **conserved** during evolution — present in different organisms, forming a protein **family** — it is reasonable to assume its members have **similar or at least correlated functions**. Conserved sequence ⇒ conserved structure ⇒ conserved function.

This is exactly why [[homology]] supports **function prediction**, in two steps:

1. **Identify the family** — the proteins evolved from a common progenitor (sequences "similar enough").
2. **Align** — use [[pairwise alignment]] to find the amino acids that play an analogous **structural or functional** role.

> [!Example] Globins
> The β-chain of hemoglobin and myoglobin "look alike": their sequences align, and their 3-D structures **superimpose** almost perfectly — visible homology predicting shared oxygen-binding function. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=3|β-globin / myoglobin superposition, L3 p.3]] Conversely, the zones bearing [[match mismatch gap|indels]] are exactly the structurally **dissimilar** regions.

# TLDR
The chain **sequence → structure → function**: a protein's sequence determines its 3-D structure, which determines its function. So conserved sequence implies conserved structure and function — which is exactly why homology enables function prediction.

# Recitation Anchors
- **sequence → structure → function**
- Sequence→structure = protein folding (sequence holds the info)
- Conserved sequence ⇒ conserved structure ⇒ conserved function
- Function prediction: identify family, then align
- Globins: sequences align & structures superimpose; indel zones = structurally dissimilar

> [!Cool] Cool fact
> Structure is conserved far more strongly than sequence: hemoglobin and myoglobin share only **~18%** sequence identity yet adopt essentially the same "globin fold" — a vivid demonstration that structure (and function) outlast the sequence that encodes them. [source](https://doi.org/10.1038/scientificamerican1178-118)

# Read aloud
KP.0.Concept: The central chain.
Here's the idea that makes sequence alignment biologically meaningful. There's a chain: sequence leads to structure, and structure leads to function.

KP.1.Concept: Sequence determines structure.
First link: a protein's three-dimensional shape is determined by its amino-acid sequence. The sequence itself carries all the information the protein needs to fold up into its proper shape. That's the principle behind protein folding.

KP.2.Concept: Structure determines function.
Second link: that three-dimensional shape determines what the protein actually does — what it binds, what reactions it speeds up, its molecular function. Change the shape and you change the job.

KP.3.Connection: Why conservation predicts function.
Now the payoff. If a protein's sequence stays conserved through evolution and shows up in many different organisms as a protein family, it's reasonable to assume those proteins do similar or related jobs. Conserved sequence means conserved structure, which means conserved function. That's why homology lets us predict function: first identify the family, then align the members to find the residues doing the same structural or functional work.

KP.4.Connection: The globin example.
Take the globins. The beta chain of hemoglobin and myoglobin look alike — their sequences align and their structures lay almost perfectly on top of each other, predicting the same oxygen-binding role. And tellingly, the spots where they carry insertions or deletions are exactly the regions where their structures stop matching.

KP.5.CoolFact: Structure outlasts sequence.
And here's the cool part — structure is conserved far more stubbornly than sequence. Hemoglobin and myoglobin agree in only about eighteen percent of their amino acids, yet they fold into essentially the same globin shape. Structure, and function, outlive the sequence that wrote them.

# Question and Answer
Q. State the sequence→structure→function chain.
A. A protein's amino-acid sequence determines its 3-D structure, and its structure determines its molecular function.

Q. Which biological process embodies the "sequence → structure" step?
A. Protein folding — the sequence holds the information to fold into the native structure.

Q. Why does conserved sequence imply conserved function?
A. Conserved sequence → conserved structure → conserved function, so family members likely share function.

Q. What two steps turn this chain into function prediction?
A. (1) Identify the protein family; (2) align members to locate residues with an analogous structural/functional role.

Q. In the globin example, what do indel regions correspond to structurally?
A. The structurally dissimilar regions — where sequences carry indels, the 3-D structures stop superimposing.

Q. What surprising fact about hemoglobin/myoglobin illustrates structure outlasting sequence?
A. They share only ~18% identity yet adopt essentially the same globin fold.
