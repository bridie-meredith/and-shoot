# Margit Working Memory

---

## Mutation Log

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

---

*Scrub note (2026-05-24): Mutation log entries for /and-cast Phase 2 candidate menu, /and-cast Phase 4 actor provisioning, b01c01 cycle-1/2/3 monument referrals, and end-of-cycle library sync have been removed from this working memory as part of the post-c01 project scrub back to fresh-/and-series state. The promoted cards themselves remain in the canonical library at `cards/`; the scrubbed log entries are preserved in git history.*

---

### 2026-05-24 — /and-cast Phase 2: Cast Candidate Menu authored

**Project:** taylor-hebert-westeros-road-to-hell
**Output:** `active-project/staff/showrunner/cast-candidate-menu.md`

**Library cards identified (5 roles, ready for Phase 4 copy):**

| slug | role |
|---|---|
| `taylor-hebert-kl-122ac` | protagonist |
| `otto-hightower` | antagonist |
| `aemond-targaryen-122ac` | world-embodiment:opposite-number |
| `wren-stitch-maker-flea-bottom-ward` | cost-bearer |
| `sera-hightower-kl-122ac` | protect-target |

**Library gaps among required roles (2 roles; margit-fork required at Phase 4):**

| missing slug | role |
|---|---|
| `alicent-hightower` | world-embodiment:green-faction-institution |
| `criston-cole` | world-embodiment:faction-violence-instrument |

**Original-character provisioning required (3 roles; name-novelty discipline applies to all):**

| role-slot | brief archetype guidance |
|---|---|
| supporting:Flea-Bottom-ward-network-anchor (ward-elder) | oc-old-hardass pattern; Flea Bottom-native |
| supporting:Otto-courier-adjacent (intermediary) | oc-local-expert pattern; 122 AC KL courier-tier |
| supporting:naive-idealist-foil | oc-young-idealist pattern; Faith or Black-adjacent; adult register |

**Optional / nice-to-have:**
- `rhaenyra-targaryen` (full card exists; 122 AC variant/addendum needed if elevated; decision deferred to Phase 3)
- `helaena-targaryen` (no card exists; margit-fork required if elevated; can be dropped under scene-count pressure)

**No mutations to library files in this phase.** Menu is read-only output. All provisioning deferred to Phase 4.

---

### 2026-05-24 — /and-cast Phase 4: Full Cast Provisioning

**Project:** taylor-hebert-westeros-road-to-hell
**Total actors provisioned:** 11
**Mode:** library-copies (5) + margit-forks (3) + original-characters (3)

#### A. Library Copies (5 actors)

All five cards copied from library to `active-project/actors/<slug>/card.md`. Memory stubs (ltm, stm, state) and vibes.md created per schemas/memory.schema.md.

| slug | library source | actor dir |
|---|---|---|
| `taylor-hebert-kl-122ac` | `cards/personas/taylor-hebert-kl-122ac.card.md` | `active-project/actors/taylor-hebert-kl-122ac/` |
| `otto-hightower` | `cards/personas/otto-hightower.card.md` | `active-project/actors/otto-hightower/` |
| `wren-stitch-maker-flea-bottom-ward` | `cards/personas/wren-stitch-maker-flea-bottom-ward.card.md` | `active-project/actors/wren-stitch-maker-flea-bottom-ward/` |
| `sera-hightower-kl-122ac` | `cards/personas/sera-hightower-kl-122ac.card.md` | `active-project/actors/sera-hightower-kl-122ac/` |
| `aemond-targaryen-122ac` | `cards/personas/aemond-targaryen-122ac.card.md` | `active-project/actors/aemond-targaryen-122ac/` |

#### B. Margit-Forks (3 actors)

New cards authored from F&B/HOTD canon. Dual-write: library path AND actor dir.

| slug | library path | actor dir | notes |
|---|---|---|---|
| `alicent-hightower-122ac` | `cards/personas/alicent-hightower-122ac.card.md` | `active-project/actors/alicent-hightower-122ac/` | Queen Consort 122 AC; dynastic-maternal; compound-eyes-only |
| `criston-cole-122ac` | `cards/personas/criston-cole-122ac.card.md` | `active-project/actors/criston-cole-122ac/` | Kingsguard commander; Green enforcement; observable-as-aftermath |
| `rhaenyra-targaryen-122ac` | `cards/personas/rhaenyra-targaryen-122ac.card.md` | `active-project/actors/rhaenyra-targaryen-122ac/` | variant-of: rhaenyra-targaryen; 122 AC config; Dragonstone-distance; active-agenda carry-forward |

#### C. Original Characters (3 actors)

Fresh originals authored. Dual-write: library path AND actor dir. Name-novelty checks all PASS.

| slug | library path | actor dir | name-novelty result | archetype |
|---|---|---|---|---|
| `oswyn-mudway-flea-bottom-elder` | `cards/personas/oswyn-mudway-flea-bottom-elder.card.md` | `active-project/actors/oswyn-mudway-flea-bottom-elder/` | PASS — "oswyn" and "mudway" not in library, projects/, or boundary-scope | oc-old-hardass Flea Bottom-native |
| `jarvis-coin-kl-courier` | `cards/personas/jarvis-coin-kl-courier.card.md` | `active-project/actors/jarvis-coin-kl-courier/` | PASS — "jarvis" and "coin" not in library, projects/, or boundary-scope | oc-local-expert Green-courier-tier adapted |
| `septon-halvard-flea-bottom` | `cards/personas/septon-halvard-flea-bottom.card.md` | `active-project/actors/septon-halvard-flea-bottom/` | PASS — "halvard" not in library, projects/, or boundary-scope; distinct from septon-rowan/septon-dying-protector/oc-ward-septon-dragon-gate; no recognizable HOTD/F&B canon name | naive-idealist-foil Flea Bottom Faith |

#### Index Updates

`cards/personas/INDEX.md` updated:
- by_world/planetos: added alicent-hightower-122ac, criston-cole-122ac, jarvis-coin-kl-courier, oswyn-mudway-flea-bottom-elder, rhaenyra-targaryen-122ac, septon-halvard-flea-bottom
- by_quality/full: added all 6 new cards
- by_trope/targaryen-era: added alicent-hightower-122ac, criston-cole-122ac, rhaenyra-targaryen-122ac
- new tropes added: kl-courier-tier, flea-bottom-ward-elder, faith-operator-flea-bottom, black-faction-claimant, road-to-hell-cast
- original_characters: added all 6 new entries with authoring notes

#### Showrunner Memory Updates

`active-project/staff/showrunner/memory.md` updated:
- `series.cast_roster` written (11 entries with slug, role, perspective)
- `series.cast_roster_notes.carry_forward` written (4 carry-forward items from Phase 3 dramatist viability)

#### Vibes Population

All 11 actor vibes.md populated with:
- Subset of `series.vibe_cloud.keys` (b01 vibe_cloud keys applicable to character)
- Personal/private associations per card Vibe Seeds
- Notable fences or carry-forward annotations for load-bearing characters (Wren d14, Aemond axis-movement, Alicent/Sera compound-eyes-only, Rhaenyra active-agenda-pressure-staging)
