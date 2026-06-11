# Library Improvement Loop — Ledger

One operation per run. Append only. Never delete entries.

---

## Entry 001 — 2026-06-11

**Scan scope:** `cards/` (256 card files), `and-experiment/warehouse/` (20 files), `active-project/warehouse/` (not present / empty).

**Findings:**

| Finding | Cards |
|---------|-------|
| Scant locations | `forest-clearing-dusk` (missing Hazards + AIH), `loc-red-keep-outer-ring` (quality mislabel — all 7 sections present), `oc-stitch-house-lane` (missing Fixed Props + AIH + title header) |
| Scant personas (on-stage) | `viserys-i-targaryen`, `aegon-ii-targaryen`, `peasant-woman-forest`, `oc-girl-from-hamlet`, `oc-plumms-man`, `oc-tributary-village-newcomer`, `victoria-dallon` |
| Scant props | `oc-fish-account-ledger`, `oc-procedural-form`, `oc-water-skin` |
| Archived/pre- cards (not active) | `*.pre-2026-*` variants — preserved for provenance, no action needed |
| Fuzzy-duplicate cluster | `loc-flea-bottom` / `loc-flea-bottom-base` / `loc-flea-bottom-mirror` — NOT duplicates; structurally differentiated (district-level / lodging sub-anchor / project variant). No merge warranted. |
| Thin behavior zone | `cards/dialects/` has 13 entries; `class: dialect` migration to `class: behavior` is deferred per CLAUDE.md. No action. |
| Archetype recurrence | No 3+ card archetype cluster identified without an existing paradigm card. |

**Operation chosen:** Quality-flag correction — `loc-red-keep-outer-ring`.

**Rationale:** All 7 required location sections are populated (Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks). Content is comparable in density to peer `quality: full` cards (`stormlands-coastal-cliffs`, `reach-smallfolk-village`). The `scant` label is a stale residual from authoring time. Promoting to `full` unlocks the card for scene use without a blocking scant-warning — critical since this is Taylor's s2/s3 endgame surveillance location (Red Keep outer ring, reachable at ~1.5km range ceiling). Highest impact-to-cost: one field change.

**Cards touched:** `cards/locations/loc-red-keep-outer-ring.card.md` — `quality: scant` → `quality: full`.

**Next candidate:** `forest-clearing-dusk` — genuine scant rescue (add Hazards + Ambient Interruption Hooks sections; 2 sections to write). Low project urgency but completes the card. OR `oc-stitch-house-lane` — missing Fixed Props + AIH + title header; project-variant card for `taylor-westeros-good-intentions`. OR `viserys-i-targaryen` — scant on-stage persona, blocking if cast; high urgency but high cost (many sections missing).
