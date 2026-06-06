# Persona-Exemplar Library Index

Margit-maintained index. One row per exemplar. Schema: `schemas/persona-exemplar.schema.md`. Authoring process: `staff/margit/exemplar-authoring-process.md`. Architectural rationale: PROP-0005 / DEC-0016 (narrowed by PROP-0005-A / DEC-0017).

---

## Audience persona exemplars

| slug | persona-ref | content-match | authored-by | dispatch-status |
|------|-------------|---------------|-------------|-----------------|
| cape-fic-reader | cape-fic-reader | high (generic capefic rooftop fight) | claude (2026-05-26) | active |
| dark-fantasy-reader | dark-fantasy-reader | high (generic grimdark battlefield aftermath) | claude (2026-05-26) | active |
| worm-canon-pedant | worm-canon-pedant | high (generic Worm-fic with Lisa + Travelers OC) | claude (2026-05-26) | active |

## Impersonator exemplars — active-project (taylor-westeros-good-intentions)

| slug | persona-ref | content-match | authored-by | dispatch-status |
|------|-------------|---------------|-------------|-----------------|
| taylor-hebert-kl-122ac | taylor-hebert-kl-122ac | high (Flea Bottom, water-carrier exchange, ledger-running interior) | claude (2026-05-26) | active |
| aemond-targaryen-122ac | aemond-targaryen-122ac | high (Dragonpit platform post-feeding) | claude (2026-05-26) | active |
| alicent-hightower-122ac | alicent-hightower-122ac | high (solar audience with steward) | claude (2026-05-26) | active |
| criston-cole-122ac | criston-cole-122ac | high (Kingsguard ready-room debrief) | claude (2026-05-26) | active |
| jarvis-coin-kl-courier | jarvis-coin-kl-courier | high (Iron Gate courier handoff) | claude (2026-05-26) | active |
| oswyn-mudway-flea-bottom-elder | oswyn-mudway-flea-bottom-elder | high (casting frame, fishmonger exchange) | claude (2026-05-26) | active |
| otto-hightower | otto-hightower | high (proposal to Velaryon-adjacent merchant) | claude (2026-05-26) | active |
| rhaenyra-targaryen-122ac | rhaenyra-targaryen-122ac | high (Dragonstone solar, dictation to Bar Emmon) | claude (2026-05-26) | active |
| septon-halvard-flea-bottom | septon-halvard-flea-bottom | high (sitting with dying tanner) | claude (2026-05-26) | active |
| sera-hightower-kl-122ac | sera-hightower-kl-122ac | high (corridor exchange with Lady Mertyns) | claude (2026-05-26) | active |
| wren-stitch-maker-flea-bottom-ward | wren-stitch-maker-flea-bottom-ward | high (vendor-swap report to journeywoman) | claude (2026-05-26) | active |

## Renderer voice exemplars

| slug | content-match | authored-by | dispatch-status | notes |
|------|---------------|-------------|-----------------|-------|
| voice-robinson-westeros-adjacent | high (Westeros port-city register, Robinson voice) | claude (2026-05-26) | active | Used at `/and-stitch` Phase 0 step 4a per PROP-0003-A. Project would copy/symlink to `active-project/voice-exemplar.md` for series-level prime. |

## Excluded (design artifacts, not dispatched)

| slug | persona-ref | excluded-by | reason summary |
|------|-------------|-------------|----------------|
| orchestrator-critic | orchestrator-critic | DEC-0017 | Tier-2 (template/structure-driven). Critic experiment 2026-05-26 found exemplar priming caused structural regression: schema checks dropped, F7-r2 lookup skipped, EFFICIENT verdict fabricated without runtime evidence (honesty-discipline violation). Retained as design artifact. |

---

## Impersonator exemplars — project-bound (and-experiment)

| slug | persona-ref | content-match | authored-by | dispatch-status |
|------|-------------|---------------|-------------|-----------------|
| viserys-i-targaryen | viserys-i-targaryen | high (small council anteroom, receiving steward's report on household expenditures) | claude (2026-06-06) | active |
| helaena-targaryen-122ac | helaena-targaryen-122ac | high (Red Keep gardens, cataloguing a specimen while a companion describes recent events) | claude (2026-06-06) | active |
| daenys-velaryon | daenys-velaryon | high (harbor district, discussing a plan; companion offers cosmological rationale) | claude (2026-06-06) | active |
| ser-harwin-the-patient | ser-harwin-the-patient | high (household corridor, end of a day that has produced a new list item) | claude (2026-06-06) | active |
| nymeria-summer-isles | nymeria-summer-isles | high (ship's deck, dawn, discussing previous port's events) | claude (2026-06-06) | active |
| saerys-septa | saerys-septa | high (household consultation room, septa delivering incident report to steward) | claude (2026-06-06) | active |

All six stored at `and-experiment/persona-exemplars/<slug>.md` (project-bound; not library-promoted; consistent with saerys-targaryen precedent).

---

## Coverage notes

- **Audience trio (3/3):** complete for the active-project audience selection. Library has 22 audience personas total; remaining 19 are uncovered. Author on demand when those personas activate in a project.
- **Active-project impersonators (11/11):** complete for taylor-westeros-good-intentions cast. Other active-project actors that get added in revisions will need exemplars authored at /and-cast Phase 4.
- **and-experiment impersonators (7/7 — saerys + six supporting cast):** complete. All seven stored project-bound at `and-experiment/persona-exemplars/`. Deferred flags from 2026-06-05 build session cleared.
- **Library personas without active-project use:** uncovered. Author on demand.
- **Voice exemplars:** one library entry (Robinson). Author additional library entries as voice registers become recurrent across projects; project-bound overrides live in `active-project/voice-exemplar.md`.
