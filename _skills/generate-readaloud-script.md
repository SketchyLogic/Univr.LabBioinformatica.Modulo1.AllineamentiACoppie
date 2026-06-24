# Skill: Generate Read Aloud Script

**Invoke when** the user asks to "generate a readaloud", "make the read aloud section", "add a read-aloud script", "do the podcast version", or otherwise wants the spoken-word/TTS narration produced for a page or glossary entry.

**Goal**: turn the file's written content into the *podcast version* — text optimized to be heard, not read. A narrator should be able to read it top to bottom and have the listener understand the concept without ever seeing the page.

## What you produce

A `## Read aloud` section appended to the end of an existing `wiki/pages/` page or `wiki/glossary/` entry. (See the **Read aloud** section in `CLAUDE.md`.)

- It does **not** count toward the 50–75 line body limit of glossary entries.
- It is **not** new frontmatter and adds no tags. You are editing an existing file, so on save set only `LastUpdateAt` to today; touch no human-only fields.
- One `## Read aloud` section per file; place it last, after `## Test yourself` / any optional sections.

## How to write it

Read the whole file first, then re-tell its content as flowing, spoken prose.

- **Speak, don't list.** Natural sentences and short paragraphs — no bullet lists, no tables, no headings inside the section.
- **Strange formulas don't read well.** Leave all LaTeX, symbols, and raw equations in the main article. In the Read aloud section, say the idea in words ("the score is the number of matches minus the number of gaps") or drop the notation entirely. Never paste `$...$`.
- **Drop the markup, keep the meaning.** No `[[wiki-links]]`, citations, figure markup, or frontmatter mechanics. If a linked concept matters, name it in plain words.
- **Optimize for the ear.** Expand abbreviations on first use, spell out what symbols mean, prefer short clauses, and use connective phrases a narrator would say ("Here's the key idea…", "Put simply…", "Now, why does this matter?").
- **Faithful, not padded.** Cover the same substance as the article; don't invent new claims or add content that isn't in the file. It can be slightly more conversational, but it is a re-narration, not an expansion.

## Structure of the section

```markdown
## Read aloud
<Opening sentence that frames what this entry is about.>

<One to a few short spoken paragraphs walking through the idea in the same
order as the article — definition, intuition, why it matters, a worked idea in
words if the article has one.>

<A closing line that restates the single most important takeaway.>
```

Length tracks the source: a short glossary entry gets a short paragraph; a dense page gets several. Aim for something that sounds right at normal speaking pace.

## Quality bar

- **Could be read aloud cold.** No symbol, link, or piece of markup that would trip a narrator survives.
- **Self-contained.** A listener who never sees the page still gets the concept.
- **Matches the file.** Same facts, same emphasis; no new claims, no omitted core idea.

> [!Example] Typical trigger
> "Generate the read aloud for the Smith-Waterman entry." → open
> `wiki/glossary/Smith-Waterman.md`, append a `## Read aloud` section that
> narrates the algorithm in plain spoken English with the scoring described in
> words rather than LaTeX, and bump `LastUpdateAt`.
