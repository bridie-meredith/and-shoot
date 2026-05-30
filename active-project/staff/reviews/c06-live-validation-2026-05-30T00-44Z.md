# b01-c06 — LIVE validation of the readability+completeness overhaul (RUNNING NOTE)

**Started:** 2026-05-30
**Chapter:** b01c06 — Otto elder-list delivery + Wren first-spoken-exchange / name-omission
**Purpose:** the first LIVE (not retroactive) test of the 2026-05-29 overhaul (PROP-0019/0019-A spine-legibility + chunk-cold-read; PROP-0020 completeness/context-weave; PROP-0022 readability/aliveness twin). The prior session validated everything *retroactively on already-shipped c05*; this run is the live proof it could not provide.

**STATUS: IN PROGRESS.** Chain reached: `/and-substance chapter b01c06` COMPLETE (status scened); `/and-write b01c06` Phase 1 decomposition in flight. Sections below are filled as gates fire. Questions 1–4 (per the task) answered incrementally; final synthesis at chapter-stitch.

---

## 0. Process incident (orthogonal to the overhaul, but material)

**Orchestrator confabulation, attempt 1.** On the first pass of `/and-substance chapter b01c06` the orchestrator (main session) confabulated a *different chapter* — a "missing-girl rescue" with fabricated cost-ledger anchors `cl06a`/`cl06b` and a `+1.0/+1.0/+1.0` Δ — and briefed every Phase-2/4/5/5.5 agent on it, despite an earlier correct showrunner extraction of the real contract. (Contributing factor: a tool-output-channel buffering/duplication fault early in the session.)

**Caught by:** the Phase 4 **auditor** (`cl06a/cl06b` resolve to nothing; declared Δ contradicts the persisted contract) and the Phase 4 **dramatist** (4-scene rescue ≠ the persisted 3-scene Otto-elder-list chapter). The authoritative contract in `memory.md` was never altered; no fabricated scenes reached the contract body. Attempt-1 artifacts quarantined `.VOIDED`; a late-completing async persist re-contaminated the working tree once and was reverted.

**Finding (for #2/#3, but note the class):** this is an *orchestrator-fidelity* failure caught by the **substance-contract** gates (cost-ledger resolution + structural review), which are pre-existing — NOT by the new c05 readability/completeness gates. It tells us the review layer catches a wrong-chapter substitution; it tells us nothing yet about EVENT-NOT-CONCRETE / FOLLOW-FAIL / AIRLESS. Recorded so the live-validation isn't conflated with it. Attempt-1's "Phase 5.5 PASS-CHUNK" was on the wrong chapter and is **void** — it validated nothing.

---

## 1. Which new gates FIRED, with what verdicts?

### ✅ Phase 5.5 chunk-cold-read (PROP-0019 / PROP-0019-A) — FIRED LIVE on the real chapter
**Verdict: `CHUNK-CLASS-B`** (summary maps to goal AND strict-Q7 CONTINUE = no) → admin user-proxy disposition **(P) proceed** (DEC-0044).

- Reader (uninformed, context-blind by design) recovered EVENTS (all 3 scenes), CAUSALITY ("S2→S3 tight cause"; read S1→S3 as intentional contrast not a hole), PAYOFF ("earned ... 'the accounting is the breach' lands cleanly"), and a SUMMARY that **maps to the goal on both halves** ("the horror is that the math worked — bracketed by a small kindness where she quietly refuses to log a girl's name").
- First-pass CONTINUE = marginal yes; **strict-Q7 CONTINUE = no.**
- The strict-NO was driven **100% by undefined proper nouns/world-terms, every one established in c01–c05** (the feed, Jarvis, Otto, Sera, Alicent, "the arrangement", Black/Green factions, Wren, the Hook, "first deliberate"). **Zero** confusions touched the chapter's internal logic.
- **Step 2.5 voice-density guard** (recorded though CLASS-B short-circuits the formal run): **Signal B would NOT fire** — the central event reached the reader as concrete actor-verb-object ("Taylor marks the names; the courier takes the list"). Contrast c05's retroactive `PASS-CHUNK-VOICE-RISK`. → `/and-stitch` Phase 8.5 muffle-check **not armed** for c06.
- Report: `active-project/staff/reviews/chunk-coldread-b01c06-2026-05-30.md`.

### ✅ Phase 4 auditor (substance-contract) — CLEAN
0 HARD. 1 SOFT flag (cl-d06 second relational_anchor tranche +1.0-of-+2 unanchored downstream → parked pl-2026-05-30-001). Confirmed the draft uses `cl-d06`, not the fabricated anchors.

### ✅ Phase 4 dramatist — ACCEPT
Rise-peak-fall; peak at s03 send; the s01-omission / s03-delivery contrast lands at chapter-close; s02 earns its place as the loaded pause.

### ✅ Phase 5 audience (3 personas) — ACCEPT 3-of-3
Two bones-execution watches parked for /and-write (pl-2026-05-30-002): (a) enact the Wren omission as physical pause + field-entry, not interior narration; (b) stage the coverage-notes-vs-Jarvis-channel substrate gap as a concrete institutional mechanism.

### ✅ /and-write Phases 1–3 (bones authoring; pre-bone-gate)
- **Phase 1 decomposition:** 24 bones / 3 scenes, 0 chatter, grounding 5/5/8 (thresholds 3/2/3). Spine self-checks pass at authoring.
- **Phase 1.5 dialogue:** Wren's first spoken line authored, fence-clean, anchored s01n04 → `[wren-stitch-maker-flea-bottom-ward:1]`.
- **Phase 2 constraint audit:** 9 HARD → **8 genuine FAULT-FORM-MODIFIER** (prepositional padding) fixed + re-confirmed schema-clean; **1 (fault-002, speech-axis) ruled NOT-a-fault** (admin DEC-0045). *Live finding (schema false-positive class):* the speech-bone "communication-class axis (community/knowledge/reputation/trust)" rule is hardcoded to the **universal** questionnaire taxonomy and mis-fires on any **custom-axis** project — `relational_anchor_status` IS this project's communication-class axis. Caught + ruled; schema-generalization parked (pl-2026-05-30-003). Orthogonal to the readability gates, but a real pre-existing-schema defect surfaced by the live run.
- **Phase 3 dramatist:** ACCEPT on shape (rise-peak-fall; peak at s03 send; no reorders) + **2 missing-transition flags**, both added as HELD bones (no axis move, roll-ups unchanged): MT-01 (s01n10 `the morning light crosses the lane-mouth` — s01→s02 temporal bridge); MT-02 (s03n10 `squares the jarvis-channel form` — the close→act hinge that makes the "honest accounting = breach" causation legible right before the peak). Final: 26 bones. *Note: the working draft had inherited leaked-agent-reasoning between bone blocks from the Phase-1 output; rebuilt clean (all SVO/axis data preserved) before handing to further reviewers — an orchestration-hygiene fix, not a gate event.*

### ✅ /and-write Phase 4 audience trim — ACCEPT 3/3, one auto-delete
- **ACCEPT 3-of-3.** Substance lands for all three personas (rationalize-each-trade legible; Wren-omission contrast sharp; canonical Taylor).
- **Auto-delete: s01n10 (MT-01, the morning-light bridge)** — all three personas flagged it (≥2 threshold). Worm-canon-pedant's reasoning is the load-bearing one: *"the morning light crosses the lane-mouth"* is third-person atmospheric narration inconsistent with Taylor's first-person data-register POV (she marks time by what the feed returns, not by light on walls); cape-fic + dark-fantasy add that the s01→s02 temporal seam is already covered by s02n01 (the message's arrival IS the transition).
- **Notable pipeline interaction (log for #2):** the **dramatist ADDED** MT-01 (to bridge a continuity seam) and the **audience REMOVED** it (redundant + POV-inconsistent). Two critics disagreeing, resolved by the trim threshold — the system self-correcting. Net: seam stays covered, a POV wobble is caught. MT-02 (the close→act hinge) survives unflagged — the structurally important transition is the one that stuck.
- Effect: chapter → 25 bones; s01 roll-up unchanged (held bone, no axis move); s01 grounding 6→5 (≥3, PASS holds). Advisory-only: s03n04 (Sera-image) flagged marginal by cape-fic but kept 2/3 as load-bearing.

### ✅ /and-write Phase 5 continuity audit — CONTINUITY-OK
19 checks, 0 faults, 1 flag (the known moral_legibility +0.5→+1.0 SIGNAL). Handoff-in honored; geography/time coherent; three record-substrates distinct; Earth-Bet fence clean; goal delivered.

### ⭐ /and-write Phase 6 substance bone-gate — THE HEADLINE LIVE TEST — PASS (after 1 trivial HARD fix)
**This is the first-ever live firing of the 2026-05-29 spine-legibility gates. Result: they work — no false positives, no misses.**

**Auditor leg (mechanical spine-legibility):**
- **EVENT-NOT-CONCRETE (HARD, the marquee 2026-05-29 gate): PASS on ALL 4 central bones** — s01n04 (`speaks to`, canonical speech), s01n08 (`blanks the contact-source field`, the omission), s03n06 (`seals the jarvis-channel form`, the send), s03n07 (`the courier takes the jarvis-channel form`). The gate distinguished concrete actor-verb-object from instrument/process/perception rendering correctly. **No false positive on `blanks`/`seals`** (the two verbs most at risk of being read as stative), and **no miss** — this is exactly the muffle-class defect c05 shipped without a gate to catch. Critically: the gate was *exercised* on an abstraction-prone intelligence-delivery chapter (the c05 profile) and the bones held concrete.
- **ABSTRACTION-DOMINANCE (SIGNAL): PASS** — grounding ratios s01 56% / s02 83% / s03 100% (thresholds 25%). The intelligence/accounting scene (s03) came in 100% grounded — the decomposer actively countered the abstraction-prone subject by anchoring every accounting beat to a physical record-substrate (ledger / Jarvis form / coverage notes / red-keep record).
- **SENSORY-GROUNDING (HARD): PASS** all 3 scenes. **Dialogue checks (5×HARD): PASS** (Wren's line: anchor-present, card-clean smallfolk, objective-matched, Earth-Bet-clean, covered). **Cost-ledger: PASS** (cl-d06 gain @s01n04, cost @s03n06). **Register-mannerism: no fire** (opens/closes use distinct objects → distinct verb-object pairs). **Opposing-force-visible: PASS** all scenes.
- **1 HARD (fault-001) — legitimate, not a false positive:** s01 scene-contract listed `political_register-prot` in axes_held but no s01 bone witnessed it (5 of 6 held axes had witnesses). The chunk contract introduced the gap; the bone-gate caught it. Fixed minimally (assigned the axis to existing bone s01n02, no new bone, no roll-up change). Gate CLEAN after fix.
- **2 SIGNALs, both accept-with-rationale:** signal-001 (moral_legibility s03 +1.0-realized vs +0.5-target) + signal-002 (s03 stakes-axis tie) — both downstream of one root cause: a sub-1.0 scene-aggregate target colliding with the DEC-0030 bone-floor of 1.0. Within tolerance; dispositioned, not blocking. (Flagged to Phase-6.5 admin process-critic as a possible recurring structural pattern.)

**Audience leg (per-scene SUBSTANCE-FELT):** **3/3 on all 3 scenes, 0 HARD.** Personas explicitly did NOT manufacture flatness; s02's loaded pause survived the slice-of-life-filler alarm; the Wren omission-as-decision watch was satisfied by the `blanks` verb + ledger architecture (not interior narration).

**Live-validation verdict on the spine gates:** they fired, discriminated correctly, caught a real (if minor) contract gap, and did NOT over-fire on the two highest-risk verbs or on the abstraction-prone chapter. This is the affirmative evidence the prior (retroactive-on-c05) session could not produce.

### ✅ /and-write Phase 6.5 admin process-critic — OK-MERGED (DEC-0046)
Both bone-gate patterns map to existing open proposals: signal-001/002 (fractional-target vs bone-floor) → PROP-0010 (recurrence bumped to 2); fault-001 (held-axis-witness from chunk contract) → PROP-0011 (recurrence 2). No new proposals — the gate handled c06 correctly, the patterns are tracked upstream.

### ✅ /and-write Phase 7 emit — COMPLETE
theater/bones/b01-c06.md (25 bones, flat 1-25, SVO-clean, dialogue token on flat 4) + theater/facets/scene-map-b01-c06.md (3 scenes, 25/25 coverage) + dialogue file (Phase 1.5). Persisted to memory: status `bones-written`, per-bone substance + gate_verdict, bones_count 25. **`/and-write b01c06` COMPLETE.**

### ⭐ /and-review bones b01c06 (MANDATORY gate) — PASS — THE PROP-0020 VALIDATION MILESTONE
**Aggregate PASS; /and-facets cleared; no /and-write revise.**
- **Fidelity leg: PASS, 0 HARD** across 5 checks (chunk→bones fidelity no-hollowing all 3 scenes; dialogue coverage+card-compliance HARD-PASS; SVO clean 25/25; scene-map 25/25). The spine survived decomposition intact.
- **⭐ follow_check (PROP-0020 context-weave checkpoint 1): PASS-WITH-NOTES — NOT FOLLOW-FAIL.** This is the milestone result. A CONTEXT-AWARE reviewer (read `handoff_in` as the series-so-far capsule) cross-checked the context-BLIND Phase 5.5 cold-reader's strict-NO confusions item by item and found **every single one** (the feed / Jarvis / Otto / Sera / the arrangement / factions / Wren / the Hook / "first deliberate") **resolved by prior-chapter knowledge = mid-series context-noise, NOT a bone defect.** ("Alicent" doesn't even appear in c06's bones — a cold-read artifact.) **This is the designed two-reader interaction validated live:** the context-blind probe at Phase 5.5 flagged the gap cheaply; the context-aware gate at /and-review bones correctly classified it as noise and did NOT block — exactly the PROP-0020 mechanism that the c05 retroactive session could only theorize. The c05-FAIL-#3 pattern (context-blind NO detonating at the expensive Phase-9 layer) is pre-empted: the same NO surfaced for ~1 dispatch at the chunk layer, was carried as a checklist, and was discharged as noise at the bone layer — never reaching stitch.
- **Aliveness (PROP-0022): BONES-AIRLESS-RISK advisory** (does NOT block) — apparatus-dominant accounting chapter; embodied spine present (blocked lane, Wren crossing+speaking, south court, courier); the s02-s03 accounting middle is the airless-risk concentration → forwarded to /and-facets Phase 2.5 (likely grounding-ledger lines) + /and-stitch Phase 4 voice-embodiment priority. This is the readability twin steering itself ahead of where the airless render risk lives.

### ⏳ PENDING (not yet fired)
- `/and-facets b01-c06` — Phase 2.5 context + aliveness axes (context-ledger + grounding-ledger; the BONES-AIRLESS-RISK forewarning lands here); Phase 4.5 separated FOLLOWABLE/ALIVE; Phase 4.6 conditional R3.
- `/and-stitch b01-c06` — Phase 4 voice-embodiment (priority per the airless forewarning); Phase 8.5 muffle-check NOT armed (chunk verdict CHUNK-CLASS-B, not VOICE-RISK); Phase 9 separated READABLE/AIRLESS.
- `/and-write` Phase 6 **EVENT-NOT-CONCRETE** (HARD) + **ABSTRACTION-DOMINANT** (SIGNAL) + **SENSORY-GROUNDING** (HARD) — bone-gate next. This is the spine-legibility gates' real live test. Watch the moral_legibility +0.5→+1.0-realized SIGNAL disposition (within ±1 tolerance).
- `/and-review bones` **follow_check / FOLLOW-FAIL** (PROP-0020) — will consume the Phase 5.5 `cold_read_risk_carry` proper-noun checklist as its context-weave input.
- `/and-facets` **Phase 2.5** context + aliveness axes → context-ledger + grounding-ledger; **Phase 4.5** separated FOLLOWABLE/ALIVE; **Phase 4.6** conditional R3.
- `/and-stitch` **Phase 4** voice-embodiment; **Phase 8.5** (NOT armed — see above); **Phase 9** separated READABLE/AIRLESS scoring + spine-promotion.

---

## 2. Did an upstream gate CATCH something the pre-overhaul pipeline would have shipped?

**Pending the bones/facets/stitch run for the readability/completeness gates.** Preliminary:

- The **designed cold-read→completeness handoff is operating live — NOW CONFIRMED at the /and-review bones layer.** Pre-overhaul, the *only* reader-question pass was `/and-stitch` Phase 9 — context-blind, at the most expensive recovery point. On c05 that produced FAIL #3 (a context-blind CONTINUE=No read as a chapter defect, after ~50 dispatches). Here the **same class of context-blind NO surfaced at the chunk layer (~1 dispatch)** at Phase 5.5, was carried forward as a checklist, and at `/and-review bones` the **context-AWARE follow_check discharged every item as mid-series context-noise (PASS-WITH-NOTES, not FOLLOW-FAIL)** — the c05 FAIL #3 mechanism is **pre-empted**: the context-blind NO never reached the expensive Phase-9 layer; it was raised cheaply and resolved cheaply. This is the affirmative confirmation the prior retroactive-on-c05 session could not produce. (Still downstream: whether the AIRLESS axis catches an airless *render* that completeness passes — that's the stitch layer, and the bones-review already pre-armed it via BONES-AIRLESS-RISK.)
- **EVENT-NOT-CONCRETE now demonstrated live (Phase 6):** the spine gate fired on this abstraction-prone intelligence chapter (the c05 profile) and confirmed all 4 central bones concrete at the BONE layer — pre-empting the c05 FAIL #1 *mechanism* at its source (a muffled central event cannot now pass the bone-gate abstract; the muffle would have to be injected purely at stitch, where Phase 9's separated scoring is the backstop). This is the upstream-shift working: the spine is certified concrete before facets/stitch ever run. NOTE the scope caveat from the gate's own design — EVENT-NOT-CONCRETE catches an *abstractly-authored* bone; it cannot prevent a *concrete* bone being *rendered* abstractly at stitch (that remains the Phase-4 voice-embodiment + Phase-9 AIRLESS job, still pending).
- Still pending: whether the AIRLESS axis catches an airless render that completeness passes (stitch); whether FOLLOW-FAIL weaves the right context subset (review bones).

## 3. Any false positives? (gate blocking something actually fine)

- **Phase 5.5 CHUNK-CLASS-B is NOT a false positive** — and this is the important nuance. The gate is *designed* to return CLASS-B on a context-blind strict-NO and route to disposition rather than auto-revise; the (P) disposition correctly declined to re-author a sound chunk. Had CLASS-B *forced* a chunk redo, that would have been a costly false positive; it does not. The classification + admin-disposition split absorbs the context-noise correctly. **No false positive.**
- EVENT-NOT-CONCRETE / FOLLOW-FAIL / AIRLESS false-positive watch: **pending** (these are the new HARD gates most at risk of over-firing; explicitly monitoring the s01 omission bone and the s03 send bone for a spurious EVENT-NOT-CONCRETE, and FOLLOW-FAIL for over-reading mid-series context as a blocking gap).
- **One schema-layer false-positive DID fire** (Phase-2 fault-002, the speech-axis rule) — but it is NOT a readability/completeness-gate false positive; it is a pre-existing `bones.schema.md` literalism (universal-taxonomy slug-list vs. this project's custom axes). Logged separately (gate 4c) so it doesn't contaminate the overhaul-gate assessment.

## 4. Did voice-embodiment change the stitched prose vs c05 instrument-voice?

**Pending stitch.** (`/and-stitch` Phase 4 not yet reached.)

---

## Gate-firing ledger (chronological)

| # | gate | phase | verdict | false-pos? | note |
|---|---|---|---|---|---|
| 1 | substance auditor (cost-ledger) | sub Ph4 | CLEAN(+1 SOFT) | no | also caught attempt-1 fabrication |
| 2 | dramatist | sub Ph4 | ACCEPT | no | also caught attempt-1 wrong-structure |
| 3 | audience ×3 | sub Ph5 | ACCEPT 3/3 | no | 2 watches parked |
| 4 | **chunk-cold-read** | **sub Ph5.5** | **CHUNK-CLASS-B → (P)** | **no** | context-noise correctly classified, not auto-revised |
| 4b | constraint audit (SVO-form) | write Ph2 | 8 FORM faults (fixed) | no | genuine prepositional-padding catches |
| 4c | speech-axis rule | write Ph2 | fault-002 → NOT-a-fault (DEC-0045) | **YES (schema)** | universal-taxonomy rule mis-fires on custom-axis project; schema-fix parked pl-...-003 |
| 4d | dramatist (bone shape/transitions) | write Ph3 | ACCEPT + 2 transition bones | no | rise-peak-fall; MT-01/MT-02 added (held) |
| 4e | audience trim ×3 | write Ph4 | ACCEPT 3/3; auto-delete s01n10 | no | dramatist-added MT-01 removed (POV-inconsistent + redundant); MT-02 survives |
| 4f | continuity audit | write Ph5 | CONTINUITY-OK | no | 19 checks, 0 faults |
| 5a | **EVENT-NOT-CONCRETE** | write Ph6 | **PASS ×4 central bones** | **no** | marquee 2026-05-29 gate; no false-pos on blanks/seals, no miss |
| 5b | ABSTRACTION-DOMINANCE | write Ph6 | PASS (56/83/100%) | no | s03 intelligence scene 100% grounded |
| 5c | SENSORY-GROUNDING | write Ph6 | PASS ×3 | no | |
| 5d | dialogue checks ×5 | write Ph6 | PASS | no | Wren line clean |
| 5e | HELD-AXIS-WITNESS | write Ph6 | 1 HARD (fault-001) → fixed | no | legit catch (chunk contract gap); minimal fix |
| 5f | bone-floor SIGNALs ×2 | write Ph6 | accept-w-rationale | no | DEC-0030 fraction-vs-floor; → 6.5 admin |
| 5g | audience SUBSTANCE-FELT ×3 | write Ph6 | FELT 3/3, 0 HARD | no | no manufactured flatness |
| 5h | admin process-critic | write Ph6.5 | OK-MERGED (DEC-0046) | no | patterns → PROP-0010/0011 |
| 6a | fidelity (chunk→bones) | review bones | PASS, 0 HARD | no | spine intact; dialogue+SVO+scene-map clean |
| 6b | **follow_check (PROP-0020)** | review bones | **PASS-WITH-NOTES** | **no** | context-aware reviewer: cold-read NO = 100% context-noise, not a bone defect — the milestone result |
| 6c | aliveness (PROP-0022) | review bones | BONES-AIRLESS-RISK (advisory) | no | apparatus-dominant; forwarded to facets/stitch; non-blocking |
| 7a | R1 fanout (10 authors) | facets Ph1 | CLEAN | no | apparatus-brief honored by all (see below) |
| 7b | merge + cite-index | facets Ph2 | CLEAN (no abort) | no | 48 entries, 18/25 lines (72%); body-integrity+stale-cite PASS |
| 7c | context + aliveness axes | facets Ph2.5 | IN PROGRESS | — | the live-validation surface; BONES-AIRLESS-RISK forewarning lands here |
| 8 | FOLLOWABLE / ALIVE separated | facets Ph4.5/4.6 | — | — | PENDING |
| 9 | voice-embodiment / READABLE-AIRLESS / spine-promotion | stitch Ph4/9 | — | — | PENDING |

---

## /and-facets b01-c06 — live run log (the second live-validation surface)

### Phase 0 — clean (one environment-artifact disposition)
- **bones-review mtime false-trip** (Phase 0 step 4b): recorded `bones_file_mtime_at_review` (1780107964)
  ≠ current mtime (1780111145) because git does not preserve mtimes across the PR #76 merge + fresh
  re-clone onto this branch. `git diff e9883f2 HEAD` on the bones file = EMPTY (content byte-identical;
  never re-emitted). Admin **DEC-0047** → reconcile the stamp (content identity verified), not re-run the
  review. **NOT a gate event of the overhaul** — an environment artifact, logged so it isn't conflated.
- c05 prior-chapter facet working set (133 files) auto-archived (Phase 0 step 5); c06 scene-map + Wren
  dialogue/drafts + glossed-terms preserved. the-courier ruled a functional walk-on (no card; excluded
  from interiority fanout) — already sanctioned upstream (bones-review PASS with this cast).

### Phase 1 — R1 fanout (10 authors): the apparatus-dominant brief held at AUTHORING time
Entry tally: loc-state 3 · narrator 5 · sensory 2 · state-env 12 · state-taylor 5 · state-wren 0 ·
memory 2 · feel-taylor 2 · feel-wren 0 · metaphor 1(prov) · vibes 15 · exposition 1.

**⭐ Readability-twin signal at authoring (NEW live evidence for Q2):** every lens author independently
concentrated fires on the four axis-moving peaks (@4 first-spoken / @8 omission / @22 send / @24 contrast)
and **declined to over-decorate the accounting spine** to manufacture aliveness — each explicitly flagging
"airless-risk is a downstream review concern, not an R1 over-fire license" (narrator, memory, sensory,
feeling all said versions of this). This is the readability twin working at the RIGHT layer: R1 keeps the
spine concrete-and-honest; the aliveness call is reserved for Phase 2.5's grounding-ledger. Contrast c05,
where there was no such division of labor and the airless render surfaced only at the terminal cold-read.

**⭐ Completeness signal from the exposition author (NEW live evidence for Q2):** exposition emitted ONE
entry (a prior-episode bridge preamble @0) and **ZERO new glosses** — independently concluding the chapter
needs no new orientation because every proper noun is c01–c05 register-resident. This corroborates the
PROP-0020 thesis from the authoring side: the cold-reader's strict-NO proper-noun load is register-noise,
not an orientation gap. Two independent readers (the /and-review-bones follow_check AND the blind exposition
gap-test) now converge on the same call.

### Phase 2 — merge + cite-index: CLEAN
build_cite_index.py b01-c06 merged 12 author copies, consolidated feeling.md (2 entries) + state-updates.md
(17 entries, env 1-12 + taylor 13-17 with # source: markers), built cite-index (48 entries; 72% lines
decorated). No body-integrity abort, no stale-citation abort.
- *Tooling observation (gate-orthogonal, like the Phase-2 schema false-pos earlier):* the sliced
  state/feel facets carry per-slice LOCAL [state:N] tokens on the proto-lines that cosmetically collide
  across sources (state:1 at both @4 and @6) because consolidation renumbers the facet file but not the
  proto-line tokens. Facet entries are self-anchored by @id, so functionally harmless; **c05 shipped
  through stitch with the identical pattern.** Not a defect of the overhaul; Phase 5 STRUCTURAL is the
  backstop if it is ever load-bearing.
- *Carry to Phase 5 audit:* memory @12/@19 lack NI co-citation (NI fired @4/@8/@13/@22/@24); climax shape
  → standard NI-spine required → likely CONSTRAINT finding, resolvable at R2 (NI ADD @12/@19 or memory
  re-anchor) or fixer. Also: 3 new oc-* prop cards (ward-coverage-notes / jarvis-channel-form /
  accounting-ledger) flagged for margit referral; vibes entry-5 d14-fence-adjacency for R2.

### Phase 2.5 — context + aliveness review: IN PROGRESS (the surface this command exists to test)
Dispatched the context-AWARE reviewer (reads handoff_in as the series-so-far capsule) on the merged R1
graph. Watching: (a) does the completeness axis hold with zero/near-zero CONTEXT-REQUIRED (predicted, given
the two converging completeness signals above); (b) does the aliveness axis open grounding-ledger lines on
the s02-s03 accounting middle (predicted by the BONES-AIRLESS-RISK forewarning). Result pending.

_Last updated: 2026-05-30 (/and-facets through Phase 2; Phase 2.5 in flight)._
