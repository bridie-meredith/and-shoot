# Card Build Manifest — and-experiment gap cards
# Session: 2026-06-05
# Authority: schemas/card.schema.md
# Margit-authored per instruction (principal directive, 2026-06-05)

---

## Cards created

| # | slug | class | subclass | quality | tier | scope | project copy | library copy |
|---|------|-------|----------|---------|------|-------|--------------|--------------|
| 1 | saerys-targaryen | persona | — | full | lead | both | `and-experiment/warehouse/saerys-targaryen.card.md` | `cards/personas/saerys-targaryen.card.md` |
| 2 | saerys-targaryen-behavior | behavior | per-character-behavior | full | — | both | `and-experiment/warehouse/saerys-targaryen-behavior.card.md` | `cards/dialects/saerys-targaryen-behavior.card.md` |
| 3 | saerys-targaryen (exemplar) | persona-exemplar | — | — | project-bound | `and-experiment/persona-exemplars/saerys-targaryen.md` | not promoted |
| 4 | viserys-i-targaryen (and-experiment variant) | persona | — | full | supporting | project | `and-experiment/warehouse/viserys-i-targaryen.card.md` | not separately stored (library card remains scant) |
| 5 | helaena-targaryen-122ac | persona | — | full | supporting | both | `and-experiment/warehouse/helaena-targaryen-122ac.card.md` | `cards/personas/helaena-targaryen-122ac.card.md` |
| 6 | daenys-velaryon | persona | — | full | supporting | both | `and-experiment/warehouse/daenys-velaryon.card.md` | `cards/personas/daenys-velaryon.card.md` |
| 7 | ser-harwin-the-patient | persona | — | full | supporting | both | `and-experiment/warehouse/ser-harwin-the-patient.card.md` | `cards/personas/ser-harwin-the-patient.card.md` |
| 8 | nymeria-summer-isles | persona | — | full | supporting | both | `and-experiment/warehouse/nymeria-summer-isles.card.md` | `cards/personas/nymeria-summer-isles.card.md` |
| 9 | saerys-septa | persona | — | full | minor | project-only | `and-experiment/warehouse/saerys-septa.card.md` | not stored (no reuse value outside and-experiment) |
| 10 | comedy-register | behavior | shared-behavior | full | — | both | `and-experiment/warehouse/comedy-register.card.md` | `cards/dialects/comedy-register.card.md` |
| 11 | loc-red-keep-interior | location | — | full | — | both | `and-experiment/warehouse/loc-red-keep-interior.card.md` | `cards/locations/loc-red-keep-interior.card.md` |

**Total: 11 items (10 card files + 1 persona-exemplar)**

---

## Reused without modification (per REUSE MAP)

Per `design/bones-first/run-01/constraints.md §4`:

| slug | class | reuse action | source |
|------|-------|--------------|--------|
| alicent-hightower-122ac | persona | reuse as-is | `cards/personas/alicent-hightower-122ac.card.md` |
| otto-hightower | persona | reuse as-is | `cards/personas/otto-hightower.card.md` |
| aemond-targaryen-122ac | persona | reuse as-is | `cards/personas/aemond-targaryen-122ac.card.md` |
| rhaenyra-targaryen-122ac | persona | reuse as-is | `cards/personas/rhaenyra-targaryen-122ac.card.md` |
| loc-dragonpit-interior | location | reuse as-is | `cards/locations/loc-dragonpit-interior.card.md` |
| loc-dragonpit-exterior | location | reuse as-is | `cards/locations/loc-dragonpit-exterior.card.md` |
| cond-kl-court-state-122ac | condition | reuse as-is | `cards/conditions/cond-kl-court-state-122ac.card.md` |
| cond-kl-geography-122ac | condition | reuse as-is | `cards/conditions/cond-kl-geography-122ac.card.md` |
| cond-dragon-bonding-claiming-rules | condition | reuse as-is | `cards/conditions/cond-dragon-bonding-claiming-rules.card.md` |
| westeros-noble-courtly | behavior | reuse as-is (inherited by new cards) | `cards/dialects/westeros-noble-courtly.card.md` |
| westeros-grrm-mannerisms | behavior | reuse as-is (referenced by new cards) | `cards/dialects/westeros-grrm-mannerisms.card.md` |

---

## Deferred / blocked items

| item | reason | flag |
|------|--------|------|
| Library upgrade of `viserys-i-targaryen.card.md` (scant→full) | Project variant is comedy-tolerant re-tone; library upgrade would bleed and-experiment-specific framing into cards serving other projects in other registers. Deferred pending principal triage. | FLAG: promote or keep project-scoped |
| Persona-exemplars for helaena-targaryen-122ac, daenys-velaryon, ser-harwin-the-patient, nymeria-summer-isles, saerys-septa | Not required until cast is locked at `/and-cast` Phase 5 equivalent. Five exemplars deferred. | FLAG: author before cast gate fires |
| Persona-exemplar for viserys-i-targaryen | On-stage supporting; exemplar eligible. Not authored this session (warm-cage-comedy beats well-covered by card body). | FLAG: author when cast active |
| `saerys-septa` library copy | No cross-project reuse value identified. Project-only. | FLAG: reassess on project promotion |
| Behavior card for helaena-targaryen-122ac | Her register is a shared-behavior variant (riddle-notation, associative-observational); sufficiently covered by `westeros-noble-courtly` + the persona card's Voice section for now. A per-character behavior card would add value before active shoot. | FLAG: author when shoot approaches |
| Behavior card for daenys-velaryon | Similar; covered by `westeros-noble-courtly` + persona card Voice. Per-character behavior card would sharpen the counter-thesis register. | FLAG: author when shoot approaches |

---

## Index updates completed

- `cards/personas/INDEX.md` — updated
- `cards/dialects/INDEX.md` — updated
- `cards/locations/INDEX.md` — updated
- `cards/persona-exemplars/INDEX.md` — updated
- `and-experiment/staff/margit/margit.memory.md` — updated

---

## Validation summary

All 11 items validated against `schemas/card.schema.md` before storage:
- Persona cards: frontmatter complete; all required body sections present; Hard Fences honored; Vibe Seeds populated for leads and full-quality supporting
- Behavior cards: frontmatter complete; Direct samples present (load-bearing sections); Cadence, Vocabulary, Syntax, Voice tells, Non-verbal tics, Memory monuments all present
- Location card: all seven required sections present
- Persona-exemplar: frontmatter per `schemas/persona-exemplar.schema.md`; length ~230 words (within range); fences declared; dispatch-status: active

No pre-existing cards were overwritten. All cards are net-new files. Preservation discipline honored.
