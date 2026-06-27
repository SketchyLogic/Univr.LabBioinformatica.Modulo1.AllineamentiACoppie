---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/AlignmentFoundations
foundational: 4
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

# edit distance and parsimony

To compare two sequences, ask: **how can I transform one string into the other?** [[raw/Teoria_L3_ALLINEAMENTI_A_COPPIE_25-26.pdf#page=5|L3 p.5]] The simplest way to find out is to **align** them and count the operations needed.

- **Edit distance** — the **minimum number of operations** (substitutions + indels) required to turn one sequence into the other. Fewer operations ⇒ smaller distance ⇒ more related.
- The available operations are the [[match mismatch gap|mismatches and gaps]] — Nature's toolkit of mutations and indels.

> [!Example] "LA CASA NUOVA" → "LA CASSA VUOTA"
> One alignment needs a certain number of edits; a different alignment of the *same* strings needs **one operation more**. The better (shorter) alignment is the one with **fewer** operations.

**Maximum parsimony** is the principle that resolves which alignment is "right": **evolution chooses the shortest path.** Among all the ways to transform one sequence into another, the most plausible is the one requiring the **fewest** changes — because each independent mutation is an unlikely event, so the explanation with the least of them is the most probable. The optimal alignment *manifests* this shortest path.

This is the conceptual seed of scored alignment: rewarding matches and penalizing mismatches/gaps is just a way of **searching for the most parsimonious transformation** — formalized by the [[Needleman-Wunsch algorithm]].

# TLDR
**Edit distance** is the minimum number of operations (substitutions + indels) to turn one sequence into another — fewer ops means more related. **Maximum parsimony** resolves which alignment is "right": evolution follows the shortest path, so the fewest-changes explanation is the most probable.

# Recitation Anchors
- Edit distance = **min operations** to transform one sequence into the other
- Operations = mismatches (substitutions) + gaps (indels)
- Fewer ops → smaller distance → more related
- **Maximum parsimony**: evolution most-likely takes the shortest path
- Same idea as **Levenshtein distance** (spell-checkers, plagiarism)

> [!Cool] Cool fact
> "Edit distance" is not biology-specific — the same **Levenshtein distance** (1965) powers spell-checkers, DNA comparison, and plagiarism detection alike; aligning genes and autocorrecting your texts are, mathematically, the *same problem*. [source](https://en.wikipedia.org/wiki/Levenshtein_distance)

# Read aloud
KP.0.Concept: The guiding question.
To compare two sequences, we ask a simple question: how can I turn one string into the other? The easiest way to answer it is to line the two up and count how many changes that takes.

KP.1.Definition: Edit distance.
The edit distance is the minimum number of operations — substitutions plus insertions and deletions — needed to transform one sequence into the other. Fewer operations means a smaller distance, which means the sequences are more closely related. The operations themselves are just the mismatches and gaps, Nature's toolkit of mutations and indels.

KP.2.Concept: A worked feel for it.
Think of turning the phrase "la casa nuova" into "la cassa vuota". One way of aligning them needs a certain number of edits; another way of aligning the very same words needs one extra operation. The better alignment is simply the one that gets there with fewer edits.

KP.3.Concept: Maximum parsimony.
Which alignment is the right one? The principle of maximum parsimony decides: evolution takes the shortest path. Among all the ways to transform one sequence into another, the most believable is the one needing the fewest changes — because each mutation is individually unlikely, so the story with the fewest of them is the most probable. The optimal alignment is the visible form of that shortest path.

KP.4.Connection: The seed of scored alignment.
This is the seed of the whole scoring idea. Rewarding matches and penalising mismatches and gaps is just a way of hunting for the most parsimonious transformation — and that's exactly what the Needleman–Wunsch algorithm formalises.

KP.5.CoolFact: The same math as your spell-checker.
And here's the cool part — edit distance isn't a biology invention. The very same idea, called Levenshtein distance, runs your spell-checker and plagiarism detectors. Aligning two genes and autocorrecting your text messages are, mathematically, the exact same problem.

# Question and Answer
Q. Define edit distance.
A. The minimum number of operations (substitutions + indels) needed to transform one sequence into another; smaller = more related.

Q. What operations count toward edit distance?
A. Mismatches (substitutions) and gaps (indels) — the mismatches and gaps of the alignment.

Q. State the maximum parsimony principle.
A. Evolution chooses the shortest path: the most plausible transformation is the one needing the fewest changes.

Q. Why is the most parsimonious explanation the most probable?
A. Each independent mutation is unlikely, so an explanation invoking fewer of them is more probable.

Q. How does the "LA CASA NUOVA / LA CASSA VUOTA" example illustrate the idea?
A. Two alignments of the same strings differ by one operation; the shorter (fewer-edit) one is preferred.

Q. What general-purpose algorithm/metric is edit distance equivalent to?
A. Levenshtein distance, used in spell-checking, text comparison, and plagiarism detection.
