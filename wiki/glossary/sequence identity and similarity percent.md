---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/DotPlots
  - EXAM_PREP
foundational: 4
prereqs: 2
density: 3
value: 5
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# sequence identity and similarity percent

Once two sequences are aligned, [[identity conservation similarity|identity and similarity]] are quantified as **percentages**. Let $S_1$ and $S_2$ be sequences of length $L_1$ and $L_2$; take $L_1$ as the reference. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=7|L3 p.7]]

**Sequence identity (s.i.):**
$$\text{s.i.} = \left(\frac{\#\text{matches}}{L_1}\right)\times 100$$
the count of identical aligned positions over the reference length.

**Sequence similarity (s.s.):**
$$\text{s.s.} = \left(\frac{S_1 \text{ vs } S_2 \text{ similarity score}}{S_1 \text{ vs } S_1 \text{ identity score}}\right)\times 100$$
- **Numerator:** score of aligning $S_1$ with $S_2$, using the [[scoring matrix]].
- **Denominator:** score of aligning $S_1$ with **itself** (the maximum possible "self" score) — a normalisation so the ratio is a percentage.

> [!Danger] The indel caveat
> If the alignment contains **indels (gaps)**, put the **alignment length** (gaps included) in the denominator, **not** the original sequence length. Forgetting this inflates the percentage.

> [!Example] From the NW worked example
> The completed [[Needleman-Wunsch algorithm]] matrix gives 8 matches over a length-15 alignment → $8/15 = 0.53 = $ **53% identity**. The real EMBOSS β/α-globin run reports **Identity 65/149 (43.6%)**, **Similarity 90/149 (60.4%)** — similarity > identity, as always.

# TLDR
**Percent identity** = matches / length × 100; **percent similarity** = (S₁-vs-S₂ score / S₁-vs-S₁ self score) × 100, always ≥ identity. The key trap: when the alignment has gaps, the denominator must be the **alignment length** (gaps included), not the original sequence length.

# Recitation Anchors
- $\text{s.i.} = (\#\text{matches}/L)\times 100$
- $\text{s.s.} = (\text{score } S_1\text{ vs }S_2 \,/\, \text{score } S_1\text{ vs }S_1)\times 100$
- With gaps: denominator = **alignment length**, not original length
- Similarity ≥ identity always
- Twilight zone ~30% identity; random 100-mers ~6% identity

> [!Cool] Cool fact
> Percent identity is treacherous without context: two random protein sequences of length 100 already share ~**6%** identity by chance, and the "safe homology" cutoff is famously ~**30%** identity — below it you're in the *twilight zone* and need similarity, not identity, to argue relatedness. [source](https://doi.org/10.1093/protein/12.2.85)

# Read aloud
KP.0.Concept: Turning likeness into a number.
Once two sequences are aligned, we put numbers on how alike they are, as percentages. Call the two sequences S-one and S-two, and pick S-one's length as the reference.

KP.1.Definition: Percent identity.
Sequence identity is the simplest: count the positions where the aligned letters are exactly the same, divide by the reference length, and multiply by a hundred. So if eight out of fifteen positions match, that's about fifty-three percent identity.

KP.2.Definition: Percent similarity.
Sequence similarity is a ratio. On top, you put the score of aligning S-one against S-two, using a scoring matrix that rewards conservative substitutions. On the bottom, you put the score of aligning S-one against itself — the highest score it could possibly get. Dividing the two and multiplying by a hundred normalises it into a percentage. Because it also credits similar-but-not-identical residues, similarity always comes out at least as high as identity.

KP.3.Procedure: The indel caveat.
There's one trap to remember. If the alignment contains gaps — insertions or deletions — you must divide by the length of the alignment including those gaps, not by the original sequence length. Skip that and your percentage comes out too high.

KP.4.Connection: A real example.
In the worked Needleman–Wunsch matrix, eight matches over a fifteen-long alignment give fifty-three percent identity. And in a real run aligning beta and alpha globin, the tool reports about forty-four percent identity but sixty percent similarity — similarity higher than identity, exactly as expected.

KP.5.CoolFact: Percentages can fool you.
And here's the cool part — percent identity is sneaky without context. Two completely random hundred-residue proteins already share around six percent identity just by chance. The well-known rule of thumb is that above about thirty percent identity you can safely call sequences homologous; below that you're in the twilight zone and must lean on similarity instead.

# Question and Answer
Q. Write the formula for sequence identity (%).
A. $\text{s.i.} = (\#\text{matches}/L_1)\times 100$ — identical aligned positions over the reference length.

Q. Write the formula for sequence similarity (%).
A. $\text{s.s.} = (\text{score}(S_1\text{ vs }S_2)/\text{score}(S_1\text{ vs }S_1))\times 100$.

Q. What do the numerator and denominator of s.s. represent?
A. Numerator: similarity score of $S_1$ vs $S_2$; denominator: $S_1$ aligned to itself (max possible score), for normalisation.

Q. When the alignment has gaps, what goes in the denominator?
A. The alignment length including the gaps, not the original sequence length.

Q. Why is similarity always ≥ identity?
A. Similarity credits both identical positions and conservative substitutions, while identity counts only exact matches.

Q. What is the rough "twilight zone" identity threshold, and why does it matter?
A. ~30% identity; below it, homology can't be reliably claimed from identity alone — you rely on similarity.
