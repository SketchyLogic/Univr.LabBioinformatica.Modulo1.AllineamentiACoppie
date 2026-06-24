# LLM Wiki

A personal, interlinked knowledge base maintained by Claude Code (after Andrej Karpathy's LLM Wiki pattern). Claude writes and maintains the wiki; the human curates sources, asks questions, and guides analysis.

**Glossary-first design**: the atomic unit is a glossary entry. Pages in `wiki/pages/` are mostly *navigation layers* — curated sequences of links to glossary entries with brief connective prose. When in doubt, write a glossary entry, not a page.

> [!Caution] This file is reused across subjects.
> All concrete examples below — subject, module names, `PATH__` tags, calibration examples — are **illustrative**. Replace or extend them to fit the material being ingested. The *structure and rules* are fixed; the *vocabulary* is per-subject.

## Folder structure

```
raw/               -- source documents (immutable -- NEVER modify)
raw/graphics/      -- curated figures; always check when ingesting
wiki/pages/        -- navigation pages (incl. one arc page + one "Key Concepts" review page per arc)
wiki/glossary/     -- atomic entries: one file per term/concept/exercise
wiki/sourcemaps/   -- one birdseye map per ingested raw file (raw->wiki crosswalk)
wiki/index.md      -- table of contents
wiki/study_path.md -- suggested study order
wiki/log.md        -- append-only operation log
templates/         -- e.g. exercise.md
```

## Ingest workflow

Ingestion is **two phases**: first *plan* (Step 1), then *generate* (Step 2). Never jump straight to generating — always produce and discuss a `PLAN.md` first.

### Step 1 — Plan (ingest the material, generate PLAN.md with the user)

When the user adds a source to `raw/` and asks you to ingest it:

1. Read the full source.
2. Write `PLAN{timestamp}.md` (the time stamp is to make it unique): an outline of everything you propose to generate. This is the **birdseye view** that lets the user parse the material fast and steer before any wiki files are written. Include:
   - A one-paragraph summary of the source and its key takeaways.
   - A **what's-where table** of the raw material — a linear walk through the source so the user sees its structure at a glance. One row per span, in source order, each a one-liner:

     | Raw span | Topic |
     |----------|-------|
     | pp. 1–4 | Intro to genome browsers (what they are, why they matter) |
     | pp. 5–9 | Coordinate systems and 0- vs 1-based indexing |

   - The summary page and concept pages you will create/update (with one-line descriptions).
   - Every glossary entry you propose, grouped sensibly, each with: proposed filename, a one-line gloss, and its draft `TYPE__` / `PATH__` / `MODULE__` tags and `foundational/prereqs/density/value` ratings.
   - Any exercises, figures from `raw/graphics/`, and new modules/tags you'd introduce.
   - The **arcs** the material splits into (one per `MODULE__`), and for each its arc page + Key Concepts review page.
   - Open questions or categorization calls you want the user to confirm.
3. Discuss `PLAN.md` with the user and revise it until they're satisfied. **Do not write any wiki files in this phase.**

### Step 2 — Generate (ingest the material and the PLAN to produce the wiki)

Once the user approves `PLAN.md`, execute it:

1. Create the summary page named after the source; create/update concept pages for each major idea.
2. For every new term, concept, or exercise, create an atomic glossary entry. Exercises use `templates/exercise.md` and go in a dedicated section of `index.md`.
3. Interlink everything with `[[wiki-links]]`.
4. For each arc the material touches, create/update its arc page **and** its `{arc}-key-concepts.md` review page (see Arcs and Key Concepts pages).
5. Write a **source map** in `wiki/sourcemaps/{source-name}.md` — a birdseye view of the raw file and where it lands in the wiki (see below).
6. Update `index.md` (new entries + one-line descriptions), `study_path.md`, and append to `log.md` (date, source, what changed).

A single source may touch 10–15 entries/pages. That is normal.

### Source maps (raw → wiki crosswalk)

For **every** raw file you ingest, generate one source map at `wiki/sourcemaps/{source-name}.md`. It is the birdseye view of that single source: what it covers and where each part of it ended up in the wiki. Keep the region indications **basic** — section titles, page numbers, slide ranges, or chapter numbers are enough; don't transcribe the source.

Use the standard page frontmatter, then include:

- A one-paragraph summary of the source.
- A **coverage table** mapping each span of the raw material to the wiki content it produced and the `PATH__` tag(s) that content carries:

| Raw span     | Topic                    | Wiki targets                  | `PATH__`                                 |
| ------------ | ------------------------ | ----------------------------- | ---------------------------------------- |
| pp. 1–4 / §1 | Intro to genome browsers | [[genome-browser]], [[track]] | `PATH__/Bioinformatics/GenomeBrowsers`   |
| slides 12–18 | Coordinate systems       | [[0-based-vs-1-based]]        | `PATH__/Bioinformatics/SequenceAnalysis` |

- A short **gaps / not-yet-ingested** note listing any parts of the source deliberately skipped or deferred, so the human can see what's missing.

The source map is navigation, not content — link out to glossary entries and pages rather than restating them.

## Arcs and Key Concepts pages

**Arc** = a coherent learning track through the material — a thematic thread a learner would study as one unit. An arc maps **one-to-one to a `MODULE__` tag**: every arc is a module, every module is an arc. **Subdivide the material into multiple arcs whenever it spans genuinely distinct themes** (e.g. *Variant Calling* vs *Precision Medicine*); keep it one arc when the material is a single thread. When in doubt about where to split, ask the user (see Step 1 — proposed modules/arcs are part of the plan).

Each arc gets **two** pages in `wiki/pages/`:

1. **The arc page** — the existing module navigation page (`wiki/pages/{arc}.md`): connective prose linking the arc's glossary entries in study order.
2. **The Key Concepts page** — `wiki/pages/{arc}-key-concepts.md`, titled `# Key Concepts — {Arc}`. A **review sheet** for the arc, meant to be read top-to-bottom before an exam.

### Key Concepts page format

A Key Concepts page is a **review layer, not new content** — it distills the arc's glossary entries and always links back to them with `[[wiki-links]]`. Use standard page frontmatter, then a body built from these blocks (include those that fit the arc):

- **Definitions** — a compact term → one-line definition list, each term linking to its `[[entry]]`.
- **Questions & answers** — self-test Q&A covering the arc's key points (lead with `EXAM_PREP`-flagged material).
- **Key facts / numbers** — the figures and results worth memorizing.
- **Procedures** — bare-bones step skeletons for any `Concept/Procedure` entries in the arc.

Keep answers tight; the page points to the glossary for depth. Order blocks so the most exam-relevant material comes first. The Key Concepts page is a nav/review page, so it is **exempt** from the glossary `[!Cool]` and `# Read aloud` requirements (though a `# Read aloud` review narration is welcome).

## Metadata

Every page and glossary entry opens with an Obsidian YAML frontmatter block. It tracks AI provenance and outstanding human work.

| Field                                            | Type                   | Set by         | Notes                                                                  |
| ------------------------------------------------ | ---------------------- | -------------- | ---------------------------------------------------------------------- |
| `CreatedAt`                                      | `YYYY-MM-DD`           | AI/human       | Set once; never changed                                                |
| `LastUpdateAt`                                   | `YYYY-MM-DD`           | AI/human       | Set to today on every meaningful change                                |
| `GeneratedBy`                                    | model ID or `null`     | AI             | Current model ID on create/substantial rewrite; `null` = human-written |
| `LastReviewAt`                                   | `YYYY-MM-DD` or `null` | **Human only** | AI must NEVER set this — not even when told "looks good"               |
| `ReviewerIds` / `OwnerIds`                       | list                   | **Human only** | Default `[admin]`; AI never modifies                                   |
| `IssueNotes`                                     | string or `null`       | **Human only** | A known problem to fix                                                 |
| `foundational` / `prereqs` / `density` / `value` | int 1–5                | AI             | **Glossary only** — see calibration below                              |

**AI rules**: on create set `CreatedAt`, `LastUpdateAt`, `GeneratedBy`; leave human-only fields at defaults. On update set only `LastUpdateAt`. `LastReviewAt: null` + a `GeneratedBy` model = unreviewed AI content (human review queue).

## Page format

```markdown
---
CreatedAt: YYYY-MM-DD
LastUpdateAt: YYYY-MM-DD
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---

# Page Title

**Summary**: one or two sentences.
**Sources**: raw source files, as Obsidian links where possible.

---

Main content: clear headings, short paragraphs, `[[wiki-links]]` throughout.
Embed figures inline right after the paragraph that references them.

## Related pages
- [[related-concept]]

## Other sources
External material covering the same topic (web pages, book chapters, videos, papers).

## Test yourself
Flashcards, Q&A, mnemonics.

## Read aloud
TTS-optimized narration of this file's content (see the Read aloud section below).
```

## Glossary entry format

One atomic note per file; filename = the exact term as it would appear in a textbook (spaces allowed, e.g. `gradient descent.md`). Frontmatter is the same as a page **plus** `tags` and the four numeric properties; do not add Summary/Sources headers. A glossary entry always start with the file title as header `#{fileTitle}`

```yaml
---
tags:
  - TYPE__/Concept/Definition
  - PATH__/Bioinformatics/SequenceAnalysis
  - MODULE__/GenomeBrowsers
foundational: 4
prereqs: 2
density: 3
value: 3
CreatedAt: YYYY-MM-DD
LastUpdateAt: YYYY-MM-DD
LastReviewAt: null
ReviewerIds: [admin]
OwnerIds: [admin]
IssueNotes: null
GeneratedBy: claude-opus-4-8
---
```

### Atomicity & length — the core rule

> [!Danger] Soft limit: **50-75 lines of body** (excluding frontmatter) per glossary entry.
> If a concept won't fit, **split it**: extract each sub-idea into its own file and link them with `[[wiki-links]]`. Generating many files is *good*; they must stay atomic and interlinked.

Decide by asking: *could someone look this up directly?* If yes, it deserves its own file — even when the parent is short. Good split candidates: a method's failure modes, why X is the gold standard for a task, a side-by-side comparison of two techniques. Prefer many tight, well-linked entries over one sprawling one.

### Tags

Every entry needs **exactly one** `TYPE__`, one `PATH__`, and one `MODULE__` tag (a second `MODULE__` only if it genuinely bridges two arcs; never three). Keep the vocabulary **narrow** — coin a new tag only when none fits, and when you do, add it to the relevant table below so this file stays canonical.

**`TYPE__`** — kind of entry:
`Concept/Definition` · `Concept/Theorem` · `Concept/Argument` · `Concept/Procedure` · `Concept/Model` · `ResearchIdea` · `Question` · `Executable/Code` · `Executable/Task` · `Executable/Exercise`

**`EXAM_PREP`** — add (in addition to the three required tags) when content is flagged as likely exam material.

**`MATH_UNRAVELING`** — add (in addition to the three required tags) when the entry unpacks a formula part-by-part with intuition and worked examples. Produced by the `_skills/math-unraveling.md` skill.

**`MODULE__`** *(example set — define modules only as sources are ingested; PascalCase nouns; each new module also gets a page in `wiki/pages/`)*:
`Introduction` · `GenePrediction` · `GenomeBrowsers` · `Sequencing` · `EffectAndVariants` · `StructuralPrediction` · `Docking` · `ProteinStructure` · `HomologyModeling` · `GenomeWideModeling` · `ForceFields` · `FoldRecognition` · `DeNovoModeling`

**`PATH__`** *(example set — where the entry lives in the knowledge map; extend per subject)*:
`Math/LinearAlgebra/*` · `Math/Calculus/*` · `Math/Probability/Distributions` · `Math/Probability/HMM` · `Math/Statistics/*` · `MachineLearning/Fundamentals/*` · `MachineLearning/SupervisedLearning/*` · `MachineLearning/DeepLearning/*` · `ComputerScience/Algorithms/DynamicProgramming` · `Bioinformatics/Genomics` · `Bioinformatics/GenePrediction` · `Bioinformatics/GenomeBrowsers` · `Bioinformatics/SequenceAnalysis` · `Bioinformatics/Sequencing/NGS` · `Bioinformatics/Validation` · `Bioinformatics/StructuralBioinformatics/ProteinStructure` · `Bioinformatics/StructuralBioinformatics/HomologyModeling` · `Bioinformatics/StructuralBioinformatics/GenomeWideModeling` · `Bioinformatics/StructuralBioinformatics/ForceFields` · `Bioinformatics/StructuralBioinformatics/FoldRecognition` · `Bioinformatics/StructuralBioinformatics/DeNovo`

### Numeric properties (1–5)

Set all four on every entry. Examples are illustrative.

- **`foundational`** — centrality to the field. 5 = bedrock everything builds on · 3 = important for a subfield · 1 = niche.
- **`prereqs`** — assumed prior knowledge. 1 = readable cold · 3 = needs a few related concepts · 5 = needs a full learning chain.
- **`density`** — how slowly it must be read. 1 = one light idea · 3 = some derivation / several ideas · 5 = proof-heavy, study slowly.
- **`value`** — centrality to *this source material*. 5 = will be on the exam · 1 = ancillary.

### Required sections

**Every glossary entry must include both `# TLDR` and `# Recitation Anchors`**, placed after the body (and after `# Argument` when present), before the optional sections below.

- **`# TLDR`** — the core idea in 1–2 sentences; enough for the reader to grasp "enough" without reading the full body.
- **`# Recitation Anchors`** — a **dotted (bulleted) list** of keywords or short sentences that help the reader recite the material from memory. Minimal recall hooks (keywords, skeleton steps, bare formulas, mnemonics) — **not** a summary or Q&A.

### Optional sections

Add only when they earn their place; place in this order after the required sections above.

| Section | Add when |
|---------|----------|
| `# Argument` | There's a non-obvious derivation/proof sketch — lay out steps, one idea each. (Place before TLDR.) |
| `# Stats and Numbers` | A concrete, *surprising* figure makes it tangible (genome sizes, gene counts, parameter counts, benchmark accuracy). Skip if the number is dry/obvious. |
| Footnotes (`[^1]`) | A term needs a gloss too tangential for inline prose. |

## Intresting facts

Every **glossary entry** (concept *and* exercise) carries a dedicated **`> [!Cool] Cool fact`** callout with **one or two** genuinely interesting, externally-sourced facts about the term. This is mandatory for glossary entries (nav pages in `wiki/pages/` are exempt).

- **What qualifies**: a surprising number or statistic, a record/extreme, an edge case or exception, a notable research finding or history or concept. Make it memorable, not a restated definition.
- **Sourced**: fact comes from an **external source** — cite it with an **inline markdown link inside the callout** (that link is the required citation; optionally also list it under `# Other sources`). Verify figures; don't invent precise numbers.
- **Preferred sources**:
	- Nature.com
	- Bioinformatics journal
	- Research papers and Wikipedia
- **Placement**: put the callout directly **before the `# Read aloud` section**. It does not count toward the 50–75 line body limit.
- **Integrate into Read aloud**: weave the cool fact into the spoken narration too (e.g. "and here's the cool part…"), so the podcast version delivers it as well.

```markdown
> [!Cool] Cool fact
> The fruit-fly gene *Dscam* can make **38,016** distinct isoforms from one gene — more than the number of genes in the whole fly genome. [source](https://example.org)
```

## Read aloud

Every page and glossary entry ends with a `# Read aloud` section: a version of the file's content rewritten and optimized for text-to-speech — the "podcast version" of the article. Produced by the `_skills/generate-readaloud-script.md` skill, which is canonical for the full format; the essentials:

- It does **not** count toward the 50–75 line body limit of glossary entries.
- **Structure it as a numbered list of Key Points (KP).** Each beat is one line `KP.<n>.<Type>: <recall-hook headline>` followed by a short spoken-word paragraph narrating that beat. The headline may be a keyword phrase or a short sentence — whichever is clearest and best triggers recall. The headlines double as a recall scaffold; the prose under them is still flowing, natural narration — not bullet lists or tables.
- **Number from `0`, in article order** — `Definition` first, then the key `Concept`s, then any `Connection`s, with the `CoolFact` beat last. One idea per KP; split a beat that covers two things.
- **`<Type>` classifies each beat.** Core set: `Definition` · `Concept` · `Connection` · `Procedure` · `Numbers` · `CoolFact`. Coin a new type only when a beat genuinely fits none — don't proliferate them.
- **Strange formulas don't read well** — leave LaTeX, symbol-heavy notation, and raw equations in the main article. In the Read aloud section, either describe the idea in words or omit the notation entirely.
- Skip `[[wiki-links]]`, citations, frontmatter mechanics, and figure markup; convey the *meaning*, not the markup.
- Aim for clarity when heard, not read: expand abbreviations, spell out what a symbol means, and keep sentences easy to follow aloud.
- Weave in the entry's **Cool fact** (see above) as the closing `KP.<n>.CoolFact` beat so the narrated version delivers it too.
- **Narrate the note's body only** — the Read aloud covers the entry's main content (and its Cool fact). It does **not** read out the `# Question and Answer` section; that self-test set sits after Read aloud and is excluded from the narration.

## Question and Answer

Every **glossary entry** (concept *and* exercise) ends with a `# Question and Answer` section, placed **after `# Read aloud`** — the last section in the file. It is a self-test set that lets the learner check the concepts just studied.

- **Count**: between **5 and 10** Q&A pairs. Cover the entry's key points; lead with `EXAM_PREP`-flagged material when present.
- **Format**: each pair is two lines — a question line `Q.` and an answer line `A.` — separated by a blank line from the next pair:

  ```markdown
  Q. Question text
  A. Answer text

  Q. Define xyz
  A. Definition ...
  ```

- **Question variety**: mix definitions, "why/how" reasoning, compare-and-contrast, and at least one that forces recall of a key number or formula when the entry has one.
- **It does not count** toward the 50–75 line body limit of glossary entries.
- **Formulas are allowed** — write them in LaTeX (`$...$` inline, `$$...$$` block). Unlike Read aloud, this section may use notation freely.
- **You may introduce simple extra notions** not already in the entry if they help test or round out understanding — keep them lightweight and consistent with the entry's.
- Keep answers tight and self-contained; this is a recall check, not a re-teach. Use `[[wiki-links]]` sparingly where a cross-reference genuinely helps.
- Nav pages in `wiki/pages/` are **exempt** (their Key Concepts page already carries Q&A); this requirement is glossary-only.

## Imagery

Enrich pages with figures from `raw/` whenever they aid understanding, placed inline right after the referencing paragraph and always captioned with a source reference.

- Standalone image: `![caption](../../raw/filename.png)`
- PDF figure: `[[raw/source.pdf#page=N|Caption – source]]`
- **`raw/graphics/`** holds curated, high-relevance figures — always check it when ingesting; embed every relevant one with a paragraph explaining what it shows and why it matters.
- Prefer figures showing a process, structure, or comparison; skip screenshots of plain text.

## Citations

- Every factual claim references its source: `[[item-in-raw#page=123|readable name]]` or an external link.
- If two sources disagree, note the contradiction explicitly. If a claim has no source, mark it as needing verification.

## Question answering

1. Read `index.md` to find relevant pages, read them, synthesize a cited answer.
2. If the answer isn't in the wiki, say so. If it's valuable, offer to file it back as a new entry/page so the wiki compounds.

## Lint / audit

When asked to lint, report findings as a numbered list with suggested fixes:

- Contradictions between pages; orphan pages (no inbound links); concepts mentioned but lacking their own entry; claims outdated by newer sources.
- Entries missing a valid `TYPE__`/`PATH__`/`MODULE__` tag, or carrying >1 `MODULE__` tag.
- Files missing `CreatedAt`/`LastUpdateAt`/`GeneratedBy`; entries over the 50-line body limit.
- Glossary entries missing the required `# TLDR` or `# Recitation Anchors` section.
- Files with `GeneratedBy` set and `LastReviewAt: null` (AI-generated, unreviewed).

## Callouts

Use Obsidian callouts to highlight content; one or two per page, not more. Syntax: `> [!Type] Title` then `> body`.

Types: `[!Info]` (background) · `[!Hint]` (tip/mnemonic) · `[!Question]` (self-test prompt) · `[!Example]` (worked example) · `[!Summary]` (recap) · `[!Quote]` (verbatim) · `[!Caution]` (common mistake) · `[!Danger]` (critical error) · `[!Cool]` (the mandatory glossary cool-fact callout — see [Cool facts](#cool-facts)).

The "one or two per page" limit does **not** count the mandatory `[!Cool]` callout.

## Global rules

- Never modify `raw/`. Always update `index.md` and `log.md` after changes.
- Page/entry filenames lowercase-hyphenated (entries may use the literal term with spaces).
- Write in clear, plain language. Math in LaTeX: `$...$` inline, `$$...$$` block.
- When uncertain how to categorize something, ask the user.
- Expand with your own knowledge or web research when it produces a richer, more accurate entry.

## About this knowledge base
These notes are specific for this knowledge base
### Connections

Cross-cutting themes beneath the modules. Weave in a brief explicit link (sentence, callout, or `# Connections` paragraph) wherever a topic *genuinely* touches one — never force it.

- **Role of the modern bioinformatician** — what practitioners actually do: interpreting data, bridging biology and computation, communicating results.
- **Bioinformatics in modern medicine** — clinical applications (diagnostic pipelines, hospital genomics, drug-target discovery).
- **Precision / personalized medicine** — patient-level decisions: variant interpretation, pharmacogenomics, personalized drug design.
- **Data mining** — extracting patterns from large biological datasets; name the analogous general technique.
### Subject
Effects and Variants, Variance Calling, Precision medicine.
Note: the material is a little thin, feel free to integrate what's necessary to enable a good study experience.

### Target audience
The learner is a 3rd university student that takes his math to be explained nice and slow.