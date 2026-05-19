# Render-log — b01-c01

generated: 2026-05-19
slug: b01-c01
profile: (schema defaults; no episode/project profile authored)
persona: neutral
narrator: taylor-hebert-kl-122ac
voice: first-person past-tense, contractions on (schema default)
phase-7-mode: per-paragraph (schema default)
phase-1-mode: scene-window (schema default)
flags: (none)

---

## Phase 0 — Validate + Load

- bones file present: `active-project/theater/bones/b01-c01.md` (27 bones, flat IDs 1-29 with time-skip blanks at @10, @21)
- cite-index present: `active-project/theater/facets/_cite-index.md`
- scene-map present: `active-project/theater/facets/scene-map-b01-c01.md` (3 scenes, all rhythm-shape flat-low, no peaks, no protected patterns)
- exposition present: `active-project/theater/facets/exposition-b01-c01.md` (5 entries)
- dialogue files present: 3 files (coll, taylor, wren) — but anchor IDs are stale against the redo'd bones (see Phase 0.5 abort below)
- feedback file: absent
- showrunner memory read OK

State machine: stitched: false → in-progress (halted pre-Phase-1)

---

## Phase 0.5 — Pre-flight HARD ABORT

**Dialogue gate (URI-DIALOGUE-COVERAGE-GATE) triggered. Stitcher refuses to consume the graph.**

The bones file was redone at commit `b2e992b` (2026-05-19 /and-write redo) which renumbered every flat ID. The downstream dialogue facet was NOT re-authored against the new bones; the dialogue entries reference OLD bones IDs:

| dialogue entry | dialogue-file @anchor | current bones at that @ | actual speech bone in current bones |
|---|---|---|---|
| coll @3 | `@3 \| "Needle's idle. Sit, then."` | `taylor crosses the yard` (not a speech bone) | `@8 coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac` |
| wren @22 | `@22 \| "Mistress Coll teach you that knot?"` | `wren-stitch-maker-flea-bottom-ward enters the street` (not a speech bone) | `@23 wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` |
| taylor @25 | `@25 \| "I cannot say."` | `taylor speaks to wren` (MATCH) | `@25` |
| (missing) | — | — | `@26 wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` (no entry anywhere; this bone is new in redo) |

**Bare speech bones (current bones speech bones with no dialogue entry keyed at that ID):** @8, @23, @26 — 3 of 4 speech bones.

**Stale-anchored dialogue entries:** coll:1 @3 (should be @23), wren:1 @22 (should be @23).

Per Phase 0.5: "If proto-lines contains any `speaks to` bones AND bare speech bones > 0, ABORT before Phase 1 dispatch." Triggered.

### Broader staleness (informational; surfaced for user)

The bones-redo invalidated more than dialogue. The following facet entries also reference OLD bones IDs that have shifted in the new flat-ID assignment:

- `exposition:2 @3` (Coll first-mention inline-appositive) — Coll's first prose mention in current bones is @4 (`coll lifts the eyes`); @3 is now Taylor's bone. Should be @4 or @8.
- `exposition:3 @15` (the-Watch first-mention em-dash-fold) — the Watch column's bone in current bones is @18 (`the city-watch passes the hook`); @15 is now `the insects fill the block`. Should be @18.
- `exposition:4 @20` + `exposition:5 @20` (Wren + the-Hook first-mention inline-appositive) — Wren's first appearance in current bones is @22 (`wren enters the street`); @20 is now `coll folds the net`. Both should be @22.
- `cite-index` pile-up labels reference OLD SVO labels (e.g. `@23 taylor-hebert-kl-122ac faces wren-stitch-maker-flea-bottom-ward`, but new bones @23 is `wren speaks to taylor`). The per-facet @-keys in cite-index were carried forward without SVO refresh.
- `feeling-coll` R2 decision-shard documents intent at OLD anchors `@3`, `@4`, `@9` referring to OLD coll-bones positions.
- `feeling-wren` entry keyed `@21` is a time-skip blank in current bones — was wren-related in OLD bones.
- `memory` and other facets — TBD; spot-check shows mem:2 @23 was authored against the OLD "taylor faces wren" SVO at @23 but the current @23 SVO is "wren speaks to taylor" — content may still align in spirit but anchor semantics differ.

The audit-pipeline appears to have passed `/and-facets cycle-3` without catching these anchor-against-bones mismatches; the audience-gate reviewed dialogue/facet CONTENT in isolation, not against bones flat-IDs.

**Recommendation:** re-run `/and-facets b01-c01` to re-author the stale facet entries (or run a scoped anchor-remap fix). Then re-run `/and-stitch b01c01`.

**Opt-out path:** pass `--allow-bare-speech` to proceed with legacy silent-speech for @8/@23/@26 (Taylor's @25 utterance would still render normally), accepting that the chapter's three other speech bones will render as silent action only. The dialogue lines authored in the dialogue files would NOT be used (they're keyed at non-speech bones). The polish would be substantially degraded.

---

## Run halted

No Phase 1 dispatch attempted. No draft files written.

User choice (2026-05-19): re-run `/and-facets b01-c01` first to re-author stale dialogue + exposition anchors against the redo'd bones. `/and-stitch b01c01` to be re-invoked after /and-facets returns clean.

next: /and-facets b01-c01
resume: /and-stitch b01c01 (after /and-facets PASS)
