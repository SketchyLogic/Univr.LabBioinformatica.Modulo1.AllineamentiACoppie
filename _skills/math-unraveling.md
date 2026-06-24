# Skill: Math Unraveling

**Invoke when** the user asks to "math-unravel", "unravel the math", "unpack this formula", or otherwise wants a formula/equation taken apart and explained on some material or topic.

**Goal**: turn an intimidating expression into something the learner *understands* — by naming every part, building intuition for the abstractions, and grounding it in concrete numbers.

## What you produce

A normal `wiki/glossary/` entry that follows the **Glossary entry format** in `CLAUDE.md` (frontmatter, required `TYPE__`/`PATH__`/`MODULE__` tags, the four numeric properties), **plus** the flag tag `MATH_UNRAVELING`. The filename is the formula's name as a learner would look it up (e.g. `sensitivity and specificity.md`, `Smith-Waterman scoring.md`).

- `TYPE__` is usually `Concept/Argument` (a derivation/explanation) or `Concept/Definition` (a defined quantity).
- Math is LaTeX: inline `$...$`, display `$$...$$` — never plain-text math.
- One formula per file. If an expression has several heavyweight sub-parts, give each its own unraveling and link them with `[[wiki-links]]` — respect the atomicity rule.

## Body structure of a generated entry

Use these sections in order; drop any that don't apply.

```markdown
# The formula
$$ <full expression in display LaTeX> $$
One sentence: what this formula computes / answers.

## Anatomy — part by part
| Symbol | Name | What it is | Role in the formula |
|--------|------|-----------|---------------------|
| ... | ... | ... | numerator pushes up / denominator normalizes / exponent controls ... |

## Intuition
Plain-language meaning of the abstractions. For each major part, say *what it does* to
the result and *why it's there*. Use limits to build feel:
- What happens as a term → 0, → ∞, or → its max?
- A one-line analogy if it genuinely clarifies (don't force it).
Use a `> [!Hint]` callout for the single most memorable takeaway.

## Worked example
Plug in concrete numbers, step by step, and interpret the result in words.
Add a second example only when it reveals something the first didn't
(e.g. an edge case, or a contrasting regime).

## Watch out  (optional)
Common misreadings, unit traps, or where the formula stops being valid.
Use `> [!Caution]`.
```

Close with `[[wiki-links]]` to the parent concept and to any sub-unravelings, and a `# TLDR` if the core idea compresses to a sentence.

## Quality bar

- **Every symbol is named.** No symbol appears in the Anatomy table without a row.
- **Intuition before manipulation.** The reader should know *why* each part exists before seeing it move in a worked example.
- **Numbers are real.** Worked examples use plausible values when possible

> [!Example] Typical trigger
> "Math-unravel the F1 score from the variant-calling notes." → create
> `wiki/glossary/F1 score.md` tagged `TYPE__/Concept/Definition`, the relevant
> `PATH__`/`MODULE__`, and `MATH_UNRAVELING`; follow the body structure above.
