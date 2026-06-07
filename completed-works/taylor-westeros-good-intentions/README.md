# Book One -- *(working title TBD)*

**Project:** `taylor-westeros-good-intentions`
**Status:** Complete. Reader-facing export.
**Exported:** 2026-06-07

---

## What this is

A one-book tragedy. Taylor Hebert -- after Gold Morning -- wakes in another body in King's Landing, 122 AC, the year before the year before the Dance of the Dragons. She comes to atone for Khepri by being useful without taking control. A courtier, Otto Hightower, identifies what she can do and offers her a function: read the city through her insects, route information, keep one protected person safe. The trades are accurate. The accuracy is the catastrophe. The road to hell is paved with good intentions, in the literal, instrumental sense -- every step is correct, and the sum is the war she was trying to prevent, with Flea Bottom among the first wards to burn.

First-person throughout, single POV. The narrator's voice is deliberately cold and analytical -- a moral "ledger" register that accounts for every cost except the one it refuses to price. That coldness is the book's signature, not a flaw to be warmed over.

20 chapters  -  ~21,900 words.

## Files

| File | Use |
|------|-----|
| `book-one.md` | **Primary deliverable.** Markdown tuned for Google Docs. To import: in Google Docs enable *Tools -> Preferences -> Enable Markdown*, then paste -- `# / ##` become headings, `*...*` become italics, `---` become section rules. (Or **File -> Open** the `.md` directly in recent Docs.) |
| `book-one.txt` | Plain-text fallback. Headings as plain caps, scene breaks as `* * *`, italics flattened. |
| `README.md` | This colophon. |

> **Encoding:** these files are plain 7-bit ASCII on purpose -- em-dashes are written as `--` rather than the Unicode em-dash, so the text reads correctly in any viewer regardless of encoding (no `"` mojibake). Google Docs keeps `--` as-is, or auto-converts it to a real em-dash if Markdown paste is enabled. To restore typographic em-dashes after import, Find & replace `--` with an em-dash.

## How it was finalized

Produced by the `design/finalize-export-protocol.md` book-close pass over the verdict-passed manuscript:

1. **Cold-read** -- four naive-reader forks swept the 20 chapters for drag, restatement, and over-repeated motifs (findings in the archived project at `staff/finalize/coldread-*.md`).
2. **Editor trim** -- four `editor`-agent passes applied a **MODERATE, voice-preserving** trim (DEC-0114): cut true redundancy and the drag the cold-readers independently flagged; thinned over-repeated images so the climax payoffs land clean; **never flattened the signature density**. Net reduction ~6.3% (~23,350 -> 21,870 words), heaviest in the mid-book repetition cluster (c11-c15), lightest at the earned-slow climax (c16-c20).
3. **Assemble & format** -- concatenated, box-dividers stripped, headings normalized, artifacts removed.

The export is a **derived reader-facing artifact.** The canonical per-chapter drafts and the full substance/bones pipeline state are preserved unchanged in the archived project (see Provenance). The export was intentionally *not* re-cascaded through the bones chain.

## Caveats of record

The book shipped `/and-review verdict b01` = PASS-WITH-NOTES. The back-third (c14-c20) carries an accepted "airless"/apparatus-register quality that the production logged as **design-inherent** -- the contract's own coldness, not a defect ("the accuracy is the catastrophe"). The export trim thinned redundancy but deliberately preserved that register. Two soft cohere-queue items (the Sera establish/confirm legs at c03/c20) were principal-deferred at completion.

## Provenance

- Source commit: `e7accff` (branch `claude/book-polish-docs-export-FWZtl`).
- Canonical drafts at export time: `projects/taylor-westeros-good-intentions/draft/b01-c01.md ... b01-c20.md` (after archival).
- Consolidated source manuscript: `.../draft/b01-manuscript.md`.
- No chapter or book title was authored in production (a standing project fence -- slugs only). "Book One" is a functional header; a title can be set in Google Docs.
