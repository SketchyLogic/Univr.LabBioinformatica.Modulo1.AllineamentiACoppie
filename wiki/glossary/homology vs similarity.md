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

# homology vs similarity

The single most common confusion in this topic — and a favourite exam trap. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=2|L3 p.2]]

| | **[[homology|Homology]]** | **[[identity conservation similarity|Similarity]]** |
|---|---|---|
| **What it asserts** | Two entities share a **common ancestor** (same phylogenetic origin) | Two entities are alike by some **comparative criterion** |
| **Character** | **Qualitative** — yes/no | **Quantitative** — a degree/percentage |
| **How stated** | "X and Y *are* homologous" | "X and Y are *40% similar*" |
| **Direction of inference** | The **conclusion** (an evolutionary claim) | The **evidence** that supports it |

The logic runs one way: we **measure** similarity (and [[identity conservation similarity|identity]]) and, if it is high enough, we **infer** homology. Similarity is an observation; homology is a hypothesis about history.

> [!Danger] The classic error
> "These proteins are 70% homologous." **Wrong.** They can be 70% *identical* or *similar*; homology itself is just present or absent. Homology is never a percentage.

Note the asymmetry: high similarity strongly suggests homology, but homologous sequences can drift so far apart that their similarity falls into the **twilight zone** (<~20% identity) — homologous yet barely similar. Conversely, short or compositionally biased sequences can be similar **by chance** without being homologous.

# TLDR
**Similarity** is the measured, *quantitative* evidence; **homology** is the inferred, *qualitative* (yes/no) conclusion of shared ancestry. You measure similarity and, if high enough, infer homology — but never quote a "% homology".

# Recitation Anchors
- Similarity = **quantitative evidence**; homology = **qualitative conclusion**
- Inference runs one way: measure similarity → infer homology
- Never "% homologous"
- Homologous yet low similarity = **twilight zone** (<~20% identity)
- Similar by chance ≠ homologous

> [!Cool] Cool fact
> The terms were sharpened by a 1987 plea from Reeck *et al.* titled *"Homology in proteins and nucleic acids: a terminology muddle"* — biologists were so routinely misusing "homology" to mean "similarity" that a formal correction was published. [source](https://doi.org/10.1016/0092-8674(87)90568-X)

# Read aloud
KP.0.Concept: The confusion to avoid.
This is the most common mix-up in the whole topic, and examiners love it: the difference between homology and similarity. They sound interchangeable, but they are not.

KP.1.Definition: What each one asserts.
Similarity says two sequences are alike by some measurable criterion — it's quantitative, a degree, a percentage. Homology says two sequences share a common ancestor — it's qualitative, a simple yes or no. You say two proteins are forty percent similar, but you say they either are or are not homologous.

KP.2.Concept: Evidence versus conclusion.
The relationship between them runs in one direction. Similarity is the evidence; homology is the conclusion. We measure how similar two sequences are, and if that similarity is high enough, we infer that they're homologous. Similarity is an observation; homology is a hypothesis about evolutionary history.

KP.3.Connection: The asymmetry.
But the link isn't perfect. Two truly homologous sequences can drift so far apart that they barely look similar — that's the twilight zone. And two unrelated short sequences can look similar purely by chance. So high similarity suggests homology, but doesn't guarantee it.

KP.4.CoolFact: A published plea for clarity.
And here's the cool part — back in 1987 a group of scientists were so fed up with people saying homology when they meant similarity that they published a paper literally titled a terminology muddle, just to set the record straight.

# Question and Answer
Q. State the key difference between homology and similarity.
A. Homology is qualitative (shared ancestry, yes/no); similarity is quantitative (degree of likeness, a percentage).

Q. Which is the evidence and which is the conclusion?
A. Similarity is the measured evidence; homology is the inferred conclusion.

Q. Why is "60% homologous" incorrect?
A. Homology has no percentage; only identity/similarity are quantified. Sequences are homologous or not.

Q. Can two sequences be homologous yet have low similarity? Explain.
A. Yes — homologs can diverge into the twilight zone (<~20% identity) and still share an ancestor.

Q. Can two sequences be similar but not homologous?
A. Yes — short or biased sequences can match by chance without any shared ancestry.

Q. In one sentence, how do you move from similarity to homology?
A. Measure similarity/identity; if high enough, infer that the sequences descend from a common ancestor.
