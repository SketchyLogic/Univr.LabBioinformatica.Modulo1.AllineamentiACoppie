---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Dynamic Programming Alignment (Arc 3)

**Summary**: The Needleman–Wunsch algorithm and the dynamic-programming idea behind it — how to find the *provably optimal* alignment of two sequences, indels included, without enumerating the astronomically many possibilities.
**Sources**: [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf|Teoria L3, slides 29–40]]

---

## Why a new method
[[dot plot|Dot plots]] don't treat indels as alignment operations, and brute-forcing all alignments is impossible (their number explodes with length). The answer is [[dynamic programming]]: solve the big problem from optimal sub-solutions, exploiting **optimal substructure** — an optimal alignment is built from optimal sub-alignments.

## The algorithm
The [[Needleman-Wunsch algorithm]] (1970) lays the two sequences on a matrix where an alignment is a **path**. It runs in three phases: **initialize**, **fill** (recompute each cell from its best predecessor), and **[[traceback]]** (walk back from the bottom-right to read the alignment). It moves forward only, maximises identical residues, minimises gaps, and weighs similarity through a [[scoring matrix]].

## The maths
The fill phase is governed by the [[Needleman-Wunsch recurrence]] — `S(i,j) = s(aᵢ,bⱼ) + max[diagonal, up, left]` — where the diagonal means *no gap* and the vertical/horizontal moves mean *a gap*. Taking the max is the single best decision per step; remembering which neighbour won enables traceback.

## Putting it to work
The worked example reaches 8/15 = 53% identity ([[exercise-needleman-wunsch-worked]]). In practice, run it as **EMBOSS `needle`** at EBI; the lecture's β/α-globin run gives 43.6% identity, 60.4% similarity.

## Related pages
- [[alignment-foundations]]
- [[dot-plots]]
- [[dynamic-programming-alignment-key-concepts]]
