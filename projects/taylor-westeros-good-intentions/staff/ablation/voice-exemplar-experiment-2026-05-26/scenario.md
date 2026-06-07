---
purpose: Voice-exemplar prime ablation for the /and-stitch renderer (PROP-0003-A wiring honor-check + variant test)
target: b01-c02 scene-A (bones @1-@14)
rhythm-shape: rising (peak @11; peak-shadow @10, @12; fusion-eligible @1-@2, @5-@8)
narrator: taylor-hebert-kl-122ac
methodology: 4 variants of the same scene rendered via renderer-minimal under different voice exemplar primes. Blind position labels assigned before reading outputs. Cold-read ranks via card voice criteria + register-fit. Position→filename revealed only after ranking is finalized.
date: 2026-05-26
---

# Test scenario

Render b01-c02 scene-A (bones @1-@14) under four voice-prime conditions. Use the same renderer (renderer-minimal), the same bones + facet set, the same scene window. The only variable is the voice exemplar passed inline to the dispatch prompt under the stitcher's surface-convention fence:

> The voice exemplar demonstrates prose register, sentence shape, and cadence. Do NOT import the exemplar's specific content (characters, place-names, events, surface conventions like italics formatting, scene-break symbols, or address forms) into the rendered prose. Only the cadence, sentence-shape, register, and noticing-patterns transfer.

## Variants

| Position | Variant | Exemplar source | Register |
|----------|---------|-----------------|----------|
| V0 | baseline | (none) | renderer's own register, card+facets only |
| V1 | robinson | `cards/persona-exemplars/voice-robinson-westeros-adjacent.md` | contemplative, long-sentence, recursive (Marilynne Robinson) |
| V2 | septon-halvard | `cards/persona-exemplars/septon-halvard-flea-bottom.md` | plain, pausal, short-sentence (religious-meditative; setting-adjacent) |
| V3 | criston-cole | `cards/persona-exemplars/criston-cole-122ac.md` | terse, procedural, economical (Kingsguard martial) |

## Why these three primes

- **Robinson** is the wired default (was missing on c02; just provisioned). The honor-check baseline.
- **Septon Halvard** is setting-adjacent (Flea Bottom register) and tests whether *being closer to the chapter's milieu* matters more than the Robinson contemplative register.
- **Criston Cole** is a contrast prime — terse and martial. Tests whether a register *very different from* the prior c02 prose moves the output more than a Robinson-adjacent register would.

## Scoring criteria

Adapted from c02's substance bone-gate + the existing renderer experiments:

1. **Substance-event recovery** — does the rendered scene make the bones' events legible to a first-time reader? (Peak @11 = Taylor extends her range; @12 = she draws the line; the suppression at @10 is the cost.)
2. **Bone-faithfulness** — every bone has a renderable trace; no invented body / dialogue / spatial / cognitive detail; no peek at omitted facets.
3. **Register-fit to the chapter** — Taylor's cold-utilitarian ledger-running interior; no theme-narration; no heroism-performance.
4. **Sentence-grammar transfer** — does the prime's cadence land *as cadence* in the prose, without importing exemplar surface content?
5. **Percussion discipline** — bones @1-@2 and @5-@8 are fusion-eligible; peak @11 stands alone; does the prose honor the rhythm?
6. **Surface-fence compliance** — no content leak from the exemplar (no septons appearing in scene-A, no Kingsguard rooms, no thyme-on-the-sill metaphor inserted).

## Output structure (per variant)

- Plain prose for scene-A, ~250-400 words (matched to scene-A bone density).
- No frontmatter, no scene markers, no annotation.
- File at `outputs/output-v{N}-{label}.md` (label hidden from cold reader during ranking).
