audit: facets-final-r1
episode: b01c01
date: 2026-05-19
mode: flag-only
status: FINDINGS-PRESENT
totals: 9 findings across 6 facets (2 HARD, 7 SIGNAL)

---

## STRUCTURAL findings (2)

- [metaphor:--] — frontmatter-missing-leading-delimiter — `metaphor.md` opens with `facet: metaphor` directly; no leading `---` delimiter. Schema permits optional header; format is irregular and could confuse parsers expecting an SVO body line first.
- [state:--] — multi-frontmatter — `state-updates.md` (consolidated) contains multiple `---`-delimited frontmatter blocks (one per source). Per schema and consolidator note "single top-of-file frontmatter per r3-signal-001"; the per-source restatement is an artifact of consolidation.

Both SIGNAL.

## FREQUENCY-BAND findings (3)

- exposition: actual 16.7% (4/24); band 1-5%; breach-high. R1+R2 both flagged as cold-start override (preamble + 3 first-mention entries land on chapter's named entities + Watch institution; no lens facet substitutes). SIGNAL.
- sensory: actual 12.5% (3/24); band 3-6% = 1-2 entries on 24 bones; breach-high by 1. Per-scene cap met scene-by-scene; each entry at distinct inflection (smell @1, sound @9, sound @15). SIGNAL.
- interest-narrator: actual 29.2% (7/24); band 15-25% = 4-6 entries on 24 bones; breach-high by 1. R2 ADD of narrator:7 @23 pushed past the band; R2 decision-log defends the add at chapter hinge beat. SIGNAL.

## METADATA-INCONSISTENCY findings (0)

_None._

## CURVE-SHAPE verdict

- Episode-level: SHAPE-OK for a hinge chapter under URI-SUBSTANCE-OVERHAUL (tensometer dropped; substance_delta is evaluation source).
- Per-scene: scene-A flat-low (capability 0, knowledge +0.2); scene-B flat-low (cap 0, kn +0.2); scene-C flat-low (cap 0, kn +0.1).
- Adjacency: uniform flat-low — consistent with declared `dramatic_shape: hinge` (chapter 1 of 18 in tragedy; no antagonist pressure; load-bearing baseline placement).
- Prohibition-test beat: structurally identifiable at @23-@24 (pattern-read auto-initiates + caught by rule); facet-dense (feel:1, mem:2, meta:1, narrator:6, narrator:7, vibes:17). SHAPE-OK.
- Flatlining: 24 bones total; flatline of 30+ impossible.

## CONTRADICTION findings (0)

_None._

## DEDUP findings (0)

_None._ The @1, @15, and @23 pile-ups each carry distinct facet-type payloads; no two entries render the same content. Dialogue utterances are all at anchors NI/feeling/memory do not render verbatim.

## SUPERFLUOUS findings (0)

Lonely entries (per cite-index) all survive rubric scrutiny:
- loc-state:3 @11 — Scene-B time/place-orient post-time-skip; load-bearing (this is why exposition's scene-orient at @11 was refused). PASS.
- vibes:6 @4 — on-anchor, back=Y, licensed-by proto:4+5 (Coll's needle-extension community-substrate cloud opening); persistent vibe established at first occurrence. PASS.
- vibes:9 @14 — on-anchor, back=Y, licensed-by proto:7+14+17 (ledger keyword for manual labor as permitted-surface). PASS.
- state:3 @5, narrator:5 @21, exposition:1 @0 — all lonely-by-design and rubric-justified.

## CONSTRAINT findings (2 HARD + multiple PASS)

- **HARD [vibes:21] @26 — vibes-citation-mismatch** — vibes:21 declares anchor @26 with `licensed-by: proto:21, proto:22, proto:25`; the proto-line @26 carries `[state:11] [vibes:18] [vibes:20]` but NO `[vibes:21]` token. Either (a) make vibes:21 off-anchor (drop @26 from entry shape) or (b) add `[vibes:21]` citation to proto-line @26 if the trust vibe was meant to fire on Wren's departure. Cite-index records `back=N` on this entry — graph integrity break.
- **HARD [vibes:17] @23 — earth-bet-hard-fence** — vibes keyword `khepri-residue` contains the proper-noun substring "khepri" (case-insensitive). Per cond-earth-bet-noun-fence + audit-class-8 rule "slug components matter — a margit-referral slug embedding `khepri-` or `gold-morning-` is a hard-fence violation even when no full English phrase is rendered." Remediation: rename keyword to a non-Earth-Bet form (candidates: `capability-residue`, `override-architecture-residue`, `pattern-read-residue`) and update licensed-by `world-build:khepri-residue-122ac` reference accordingly OR adopt a cross-reference convention that obscures the slug. Note: vibes entries are operator-bias only and never rendered as prose; the fence still applies to slugs per the audit rule.

PASS items (cross-checked):
- mem:2 @23 NI-spine — narrator:7 @23 satisfies (R2 ADD).
- exposition scene-open-orient fire-rule — @11 and @20 correctly refused (loc-state covers).
- exposition re-gloss — first episode, no prior glossed-terms register; all terms first-glossed here.
- dialogue behavior-card-compliance — all 3 utterances pass (no contractions for Taylor; no noble register for Coll/Wren; no Earth-Bet; no anachronistic idiom; no card-§-forbidden vocab).
- dialogue-coverage (URI-DIALOGUE-COVERAGE-GATE) — all 3 speech bones cited; all 3 speaker files non-empty.
- scene-map coverage (URI-SCENE-WINDOW) — 24/24 bones in exactly one scene; no gaps, overlaps, dangling anchors, duplicate labels; frontmatter consistent.
- scene-map per-scene caps — sensory ≤3/scene (2/1/0); feeling ≤1/char/scene (Taylor 1 in C, Wren 1 in C); metaphor ≤1 cross-character/scene (1 in C); exposition scene-open-orient ≤1/scene (0 in all).
- loc-state continuity-license — no continuity-carry entries; nothing to fire.
- first-mention-character coverage — Coll (@3) and Wren (@20) glossed; the-door-keeper @2 is a role reference not a named individual (no character-expectation; rubric does not require gloss).
- Earth-Bet scan across NI, memory target-references, metaphor text, feeling, sensory, loc-state, exposition gloss text, dialogue utterances, state field/value text — clean except vibes:17 keyword.

## AP-SCAN findings (1)

- [narrator:--] — within-author template-fatigue — "X is what Y" inverted-predicate construction appears at narrator:2 ("useful without controlling is what the threshold means today"), narrator:4 ("the cost of being legible is what she counts, not the patrol's count of her"), narrator:6 ("face, not node, is what she holds"). 3 of 7 entries. R2 author self-flagged in the decision-log as edge-of-fatigue. Construction is base-card-authentic for Taylor's cold-utilitarian register; not HARD AP violation, but visible syntactic template that should be tightened on subsequent chapter. SIGNAL.

Dialogue AP-scan (chassis-contamination, modern-hr-speak, deposition-cadence, nominalization) — all 3 utterances clean. PASS.

## TASTE-FLAG findings (1)

- [stitch-input:--] @6-7 / @16-17 — atmosphere-thin / stitcher-guidance-gap — 4 work-action bones (`threads the needle`, `handles the nets`, `holds the feet`, `the needle threads the mesh`) are completely bare of facet decoration. By design (prohibition-as-body-stillness is the Scene-B substance; R2 NI judge explicitly refused fires here). However, scene-map under URI-SUBSTANCE-OVERHAUL no longer carries `fusion-eligible-runs` (tensometer-derived field dropped); /and-stitch will not have explicit fusion-guidance for these bare runs. Stitcher should treat @6-@7 and @16-@17 as fusion-candidates by inference. SIGNAL (pipeline gap, not author fault).

## PILE-UP REVIEW (4)

- @1 (8 facets: loc-state:1, narrator:1, sensory:1, state:1, vibes:1+2+3+4) — verdict: WARRANTED — chapter-open bears highest orientation load; 8 entries from distinct facet types (4 vibes carrying distinct token-bundles: insects / king's-landing / corner-room-as-threshold / arrival-at-cost-threshold).
- @15 (8 facets: exposition:3, loc-state:5, mem:1, narrator:4, sensory:3, state:6, vibes:10+12) — verdict: WARRANTED — Scene-B peak; chapter's only external institutional pressure event; 8 distinct facet types.
- @3 (5 facets: coll-net-mender-flea-bottom:1, exposition:2, state:1+2, vibes:5) — verdict: WARRANTED — first social interaction + first-mention-character introduction + first dialogue beat.
- @23 (5 facets: feel:1, mem:2, meta:1, narrator:7, vibes:17) — verdict: WARRANTED — chapter's hinge beat (prohibition catches pattern-read); 5 dimensions (somatic / cognitive callback / figurative / NI cognition / persistent state cloud).

---

## Audit summary

- Total entries reviewed: ~73 (loc-state 6 + narrator 7 + sensory 3 + state-updates 20 + memory 2 + feeling 2 + metaphor 1 + vibes 23 + exposition 4 + dialogue 3 + scene-map 3)
- HARD classes: STRUCTURAL 0, CONTRADICTION 0, DEDUP 0, SUPERFLUOUS 0, **CONSTRAINT 2**
- SIGNAL classes: FREQUENCY-BAND 3, METADATA-INCONSISTENCY 0, STRUCTURAL 2, AP-SCAN 1, TASTE-FLAG 1, PILE-UP REVIEW 4 (all WARRANTED)
- CURVE-SHAPE: SHAPE-OK
- F-R2 protocol check: f-r2-counts {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0} from consolidated R2 decision-log — all zeros; no orchestrator-critic HARD/SIGNAL thresholds triggered from R2 layer.

## Routing

| Finding | Class | Severity | Author | Action |
|---|---|---|---|---|
| C-001 vibes:21 @26 back=N | CONSTRAINT | HARD | showrunner (vibes) | Resolve citation mismatch: either drop @26 from entry or add `[vibes:21]` to proto-line @26 |
| C-002 vibes:17 khepri-residue Earth-Bet | CONSTRAINT | HARD | showrunner (vibes) | Rename keyword to non-Earth-Bet form; update licensed-by world-build ref |
| FB-001 exposition 16.7% | FREQUENCY-BAND | SIGNAL | exposition-author | Advisory; cold-start override defended |
| FB-002 sensory 3/1-2 | FREQUENCY-BAND | SIGNAL | studio | Advisory; per-scene caps held |
| FB-003 NI 7/4-6 | FREQUENCY-BAND | SIGNAL | impersonator(NI) | Advisory; R2 ADD pushed past band |
| S-001 metaphor.md frontmatter | STRUCTURAL | SIGNAL | editor (metaphor) | Add leading `---` |
| S-002 state-updates multi-frontmatter | STRUCTURAL | SIGNAL | consolidation tool | Normalize to single frontmatter |
| AP-001 NI "X is what Y" ×3 | AP-SCAN | SIGNAL | impersonator(NI) | Tighten on next chapter |
| TF-001 bare work-bone gap | TASTE-FLAG | SIGNAL | pipeline (scene-map) | /and-stitch awareness; fusion-eligible-runs field not derived this run |

**Phase 5b gate:** HARD = 2 — Phase 5b CANNOT fire. Dispatch fixer to remediate C-001 and C-002; re-fire Phase 5 (or targeted re-check) until HARD = 0.
