---
tags:
  - TYPE__/Concept/Argument
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentFoundations
foundational: 3
prereqs: 2
density: 2
value: 4
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# protein vs DNA alignment

When you can choose, **aligning protein sequences is often more informative than aligning the underlying DNA**. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=1|L3 p.1]] Four reasons:

1. **Bigger alphabet → more signal.** Proteins use **20** amino-acid letters vs only **4** nucleotides. With more distinct symbols, a chance match is far less likely, so real similarity stands out instead of drowning in [[dot plot|background noise]].
2. **Conservation is visible.** Many amino acids share **biophysical properties**, so a substitution can be "[[identity conservation similarity|conservative]]" (similar properties preserved). This biochemical similarity is invisible at the DNA level but meaningful in proteins.
3. **The genetic code is degenerate.** Codons are **redundant**: a change in the **third codon position** often does *not* change the encoded amino acid (a **synonymous / silent mutation**). Such DNA changes add noise to a DNA alignment but leave the protein unchanged. [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=2|codon table, L3 p.2]]
4. **Longer "look-back" in time.** Because proteins change more slowly (synonymous DNA changes are filtered out), protein similarity remains detectable across far greater evolutionary distances — a longer evolutionary "look-back".

> [!Hint] Practical move
> If you only have DNA, you can **translate it to protein first**, align the proteins, and project the result back — exploiting all four advantages above.

# TLDR
When you can choose, aligning **protein** beats aligning DNA: 20 letters vs 4 give more signal, conservation is visible, silent (synonymous) codon changes add DNA-only noise, and proteins offer a longer evolutionary look-back.

# Recitation Anchors
- 20 amino-acid letters vs 4 nucleotides → chance matches rarer, more signal
- **Conservation visible** in proteins (conservative substitutions) — invisible in DNA
- Degenerate code → **silent** 3rd-position mutations add DNA noise
- Proteins change slower → longer evolutionary **look-back**
- Tip: translate DNA → protein, align, project back

> [!Cool] Cool fact
> The genetic code's redundancy is dramatic: **61** sense codons encode just **20** amino acids, so leucine, serine and arginine each have **six** different codons — meaning many DNA mutations are completely silent at the protein level. [source](https://www.ncbi.nlm.nih.gov/books/NBK22356/)

# Read aloud
KP.0.Concept: The core claim.
When you have a choice, it's often better to align protein sequences than the DNA that codes for them. Here are four reasons why.

KP.1.Concept: A bigger alphabet means more signal.
Proteins are written with twenty different amino-acid letters, while DNA uses only four. With more symbols, two unrelated sequences are far less likely to match just by chance, so genuine similarity stands out clearly instead of being buried in background noise.

KP.2.Concept: Conservation shows up in proteins.
Many amino acids share physical and chemical properties, so when one is swapped for a similar one, the protein's character is largely preserved. We call that a conservative substitution. This kind of similarity is simply invisible if you look at the raw DNA.

KP.3.Concept: The genetic code is redundant.
The genetic code is degenerate, meaning several codons can spell the same amino acid. In particular, a change in the third letter of a codon very often leaves the amino acid unchanged. These silent, or synonymous, mutations clutter a DNA alignment with noise but don't touch the protein at all.

KP.4.Connection: A longer look-back and a practical tip.
Because those silent changes are filtered out, protein sequences change more slowly, so we can still detect their relationships across much greater spans of evolutionary time — a longer look-back. And if all you have is DNA, the practical move is to translate it into protein first, align the proteins, then map the result back.

KP.5.CoolFact: Sixty-one codons, twenty amino acids.
And here's the cool part — there are sixty-one meaningful codons but only twenty amino acids, so some amino acids, like leucine, serine, and arginine, each have six different codons. That's why so many DNA mutations are completely silent.

# Question and Answer
Q. Why does a 20-letter alphabet beat a 4-letter one for alignment?
A. More distinct symbols make chance matches rarer, so real similarity stands out above the background noise.

Q. What is a synonymous (silent) mutation?
A. A DNA change — typically in the third codon position — that does not alter the encoded amino acid, because the genetic code is degenerate.

Q. What does "degenerate" mean for the genetic code?
A. Multiple codons map to the same amino acid (61 sense codons → 20 amino acids), so some changes are redundant.

Q. What is meant by proteins offering a longer "look-back"?
A. Proteins evolve more slowly (silent DNA changes are filtered out), so homology stays detectable across greater evolutionary distances.

Q. If you only have DNA but want the protein advantages, what do you do?
A. Translate the DNA to protein, align the proteins, then project the alignment back to the DNA.

Q. Give one reason conservation is invisible at the DNA level.
A. Biophysical similarity between amino acids has no counterpart among the four equally-different nucleotides, so a conservative protein change looks like an ordinary mismatch in DNA.
