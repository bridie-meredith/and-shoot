# Margit Working Memory

## Mutation Log

### 2026-05-18 — Step 1c (Phase 2): Cast candidate menu authored for taylor-hebert-westeros-good-intentions

Candidate menu output: `active-project/staff/showrunner/cast-candidate-menu.md`

Inputs read: cast-brief.md, memory.md, boundary-scope.md, prompt-binding.md, cards/personas/INDEX.md, cards/personas/{taylor-hebert-westeros, taylor-hebert-flea-bottom-mirror, otto-hightower, aemond-targaryen, oc-lyra-targaryen-ward, oc-maester-edwyn, oc-block-fixture, oc-renderer-flea-bottom, oc-flea-bottom-boy, oc-broken-maester, oc-dock-runner, oc-tanner-mother}.card.md, projects/project_07/staff/showrunner/1c-candidate-menu.md (name-collision check), projects/project_05 and project_06 actor lists (name-collision check), cards/conditions/cond-nessa-scene-frequency.card.md (confirms Nessa disqualified).

**Phase 2 findings summary:**

| Slot | Status | Recommended slug(s) |
|---|---|---|
| TAYLOR-HEBERT | New variant required | `taylor-hebert-kl-122ac` (not-yet-authored) |
| OTTO-HIGHTOWER | Exists (scant) — quality upgrade recommended | `otto-hightower` (exists: cards/personas/otto-hightower.card.md) |
| AEMOND-TARGARYEN | Age mismatch at 122 AC — 122AC variant recommended | `aemond-targaryen-122ac` (not-yet-authored); base `aemond-targaryen` exists (scant) |
| ALICENT-HIGHTOWER | Not in library — conditional on protect-target selection | `alicent-hightower` (not-yet-authored; conditional) |
| COST-BEARER | OC required — 6 candidates proposed | Profiles A–F; screen-writer selects at Phase 3 |
| PROTECT-TARGET | OC required (A/B preferred) — 5 candidates proposed | Profiles 6-A1, 6-A2, 6-B1, 6-B2, 6-C1 |
| WITNESS-MIRROR | OC required — 4 candidates proposed | Profiles 7-A through 7-D |
| FLEA-BOTTOM-FIXTURE | OC required — 4 candidates proposed | Profiles 8-A through 8-D |
| MAESTER-CHRONICLER | OC required — 4 candidates proposed | Profiles 9-A through 9-D |

**Name-novelty confirmed:** All OC names in the menu (Pell, Wren, Bram, Alis, Jonn, Sabel, Sera, Torrhen, Orla, Hyla, Brynn, Halvard, Gylda, Osric, Brea, Coll, Pott, Helwy, Rivin, Corvan, Halvyn, Perwyn, Orlith) are confirmed novel against the disqualified-names register. No prior project or library OC name is reused.

**Pending at Phase 3:** Screen-writer selects from all slots. Margit will author new cards at Phase 4 for all selected OC candidates.

---

### 2026-05-17 — Step 1d: Constraint cards authored for taylor-hebert-kl-122ac

10 constraint cards authored (laws + lore + behaviors). Each card written to both library (`cards/conditions/<slug>.card.md`) and warehouse (`active-project/warehouse/<slug>.md`). Index updated at `cards/conditions/INDEX.md`.

| slug | subclass | library path | warehouse path |
|---|---|---|---|
| cond-khepri-residue-122ac | law | cards/conditions/cond-khepri-residue-122ac.card.md | active-project/warehouse/cond-khepri-residue-122ac.md |
| cond-earth-bet-noun-fence | law | cards/conditions/cond-earth-bet-noun-fence.card.md | active-project/warehouse/cond-earth-bet-noun-fence.md |
| cond-westerosi-magic-dormant-122ac | law | cards/conditions/cond-westerosi-magic-dormant-122ac.card.md | active-project/warehouse/cond-westerosi-magic-dormant-122ac.md |
| cond-dragon-proximity-122ac | law | cards/conditions/cond-dragon-proximity-122ac.card.md | active-project/warehouse/cond-dragon-proximity-122ac.md |
| cond-kl-court-state-122ac | lore | cards/conditions/cond-kl-court-state-122ac.card.md | active-project/warehouse/cond-kl-court-state-122ac.md |
| cond-kl-geography-122ac | lore | cards/conditions/cond-kl-geography-122ac.card.md | active-project/warehouse/cond-kl-geography-122ac.md |
| cond-kl-social-physics-122ac | lore | cards/conditions/cond-kl-social-physics-122ac.card.md | active-project/warehouse/cond-kl-social-physics-122ac.md |
| cond-taylor-pov-behavior | behavior | cards/conditions/cond-taylor-pov-behavior.card.md | active-project/warehouse/cond-taylor-pov-behavior.md |
| cond-westerosi-witness-vocabulary | behavior | cards/conditions/cond-westerosi-witness-vocabulary.card.md | active-project/warehouse/cond-westerosi-witness-vocabulary.md |
| cond-maester-chronicler-voice | behavior | cards/conditions/cond-maester-chronicler-voice.card.md | active-project/warehouse/cond-maester-chronicler-voice.md |

All 10 cards: quality full, scope library (library copy) / scope project (warehouse copy), world planetos, project taylor-hebert-kl-122ac. Index updated by_world, by_quality, and by_type.

**Reuse decisions:** The following existing library cards are pulled into this project without modification and do not require new authoring:
- `cond-fauna-control-rules` — base fauna-control rules; referenced by cond-khepri-residue-122ac
- `cond-no-parahuman-infrastructure` — Earth-Bet world-law; referenced by cond-earth-bet-noun-fence and cond-khepri-residue-122ac
- `cond-shard-behavioral-weight` — escalation bias; referenced by cond-taylor-pov-behavior
- `cond-westerosi-superstition-frame` — folk epistemology; referenced by cond-westerosi-witness-vocabulary and cond-westerosi-magic-dormant-122ac
- `cond-dance-faction-state-previserys` — ~125 AC faction state context for cond-kl-court-state-122ac reference
- `cond-kl-witch-label-formation` — KL witch-label mechanics; referenced by cond-westerosi-witness-vocabulary
- `cond-feudal-hierarchy-law`, `cond-smallfolk-political-physics`, `cond-westerosi-customary-authority` — referenced by cond-kl-social-physics-122ac
