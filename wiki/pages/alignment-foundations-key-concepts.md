---
CreatedAt: 2026-06-23
LastUpdateAt: 2026-06-23
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Key Concepts — Alignment Foundations

**Summary**: Exam-ready review sheet for [[alignment-foundations|Arc 1]]. Read top-to-bottom before the exam; follow the links for depth.

---

## Definitions
- **[[pairwise alignment]]** — aligning two sequences to maximise identity/conservation and assess similarity & possible homology.
- **[[identity conservation similarity|Identity]]** — fraction of aligned positions that are the *same* residue (quantitative, strictest).
- **[[identity conservation similarity|Conservation]]** — substitution preserving physico-chemical properties (proteins).
- **[[identity conservation similarity|Similarity]]** — identity + conservation; ≥ identity, always.
- **[[homology]]** — similarity *due to common ancestry*; **qualitative** (yes/no, no percentage).
- **[[orthologs]]** — homologs in different species, via **speciation**.
- **[[paralogs]]** — homologs in one species, via **gene duplication**.
- **[[match mismatch gap|Match / mismatch / gap]]** — identical / substitution / indel.
- **[[edit distance and parsimony|Edit distance]]** — minimum operations to transform one sequence into another.

## Questions & answers (lead with EXAM_PREP)
Q. Homology vs similarity — the key difference? → Homology is qualitative (shared ancestry, yes/no); similarity is quantitative (a measured degree). Similarity is the *evidence*, homology the *conclusion*. See [[homology vs similarity]].

Q. Why is "70% homologous" wrong? → Homology has no percentage; you can be 70% identical/similar.

Q. Orthologs vs paralogs — the one distinguishing factor? → The separating event: speciation (orthologs, different species) vs gene duplication (paralogs, same species). See [[orthologs vs paralogs]].

Q. Do orthologs always share function? → No — may or may not (often retained).

Q. State the sequence→structure→function chain. → Sequence determines 3-D structure; structure determines molecular function; so conserved sequence ⇒ likely conserved function. See [[sequence structure function]].

Q. Why prefer proteins over DNA for alignment? → 20 vs 4 letters (more signal), visible conservation, code degeneracy (silent mutations add DNA noise), longer evolutionary look-back. See [[protein vs DNA alignment]].

Q. Why are gaps penalised more than mismatches? → Indels are evolutionarily rarer than substitutions.

## Key facts / numbers
- Alphabets: **20** amino acids vs **4** nucleotides.
- Genetic code: **61** sense codons → **20** amino acids (degenerate; 3rd-position changes often silent).
- "Twilight zone": below ~**30%** identity, homology can't be claimed from identity alone.
- Globin family is the running example (orthologs across species; paralogs within human).

## Mnemonics
- **Ortho** = **O**ther organisms (speciation); **Para** = in **Pa**rallel within one genome (duplication).
- Similarity is measured; homology is inferred.
