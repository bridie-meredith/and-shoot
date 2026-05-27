# Tournament tuning framework

**Purpose.** Define the signals, feedback loops, and promotion paths that let `/and-stitch`'s multi-arm tournament + cherry-pick produce the best version every time — and detectably improve over time as evidence accumulates.

**Scope.** The renderer-voice tournament + cherry-pick path at `/and-stitch` Phase 1.5. Companion tournaments at impersonator (PROP-0005-A Tier-1 Phase 2) and audience (Phase 3) — deferred under the impersonator-experiment evidence — will follow this same framework when they land.

**Status.** v1 — 2026-05-27. Codifies the lessons from the b01-c01 ablation, the b01-c02 multi-arm tournament + three CONTINUE=no cold-reads + cherry-pick experiment. Expected to evolve as scorecards accumulate across c03+ chapters.

---

## Why the framework exists

The b01-c02 trail produced four converging observations that demand a tuning framework, not just a one-off rubric:

1. **Per-paragraph craft optimization is not predictive of continue-rate.** Three stitches of c02 (original / single-arm voice-primed / multi-arm tournament + cherry-pick) all returned cold-read CONTINUE=no. The tournament's 16-criterion rubric was selecting against prose-surface taste; cold-read was reading against reader-orientation and stake-legibility. The two layers were measuring different things and the prose-layer optimization could not move the reader-layer outcome.

2. **The rubric is blind to its own gaps.** The cherry-pick draft fired three pet peeves (protagonist-cost-not-legible walkout; symbolic-relationship strong; setting-dressing-as-meaning strong) that the tournament rubric did not check. Adding RW9 reader-orientation + PEEVE #9 cost-not-legible at the rubric closed the visible gap — but only the next 5+ chapters of scorecards will tell us whether the new criteria actually predict continue-rate.

3. **Cherry-pick reveals ceiling, not just gain.** Scene-A and Scene-C had no per-paragraph lift room (arm-1 swept the criteria); Scene-B had real lifts the cold-reader noticed. This is information about the SCENE not the rubric — and the framework needs to surface it so we know when multi-arm is buying us anything.

4. **Some failures are unreachable from stitch.** The cost-not-legible walkout and the symbolic-relationship-with-the-woman strong-fires live in **bones authoring**, not stitch composition. No paragraph swap at /and-stitch can ground a woman the bones authored as a function-signature. The framework's most important feedback loop is **stitch-scorecard → /and-write revise** when failures concentrate on bones-level criteria.

---

## Signals tracked

Three signal layers, persisting across runs:

### Layer 1 — Per-arm tournament verdict (existing; Phase 1.5 Step 1)

Persisted at `active-project/staff/reviews/tournament-<book>-<chapter>-scene-<L>-<timestamp>.md`. Contains:
- Per-criterion 16-row table (PET PEEVES × N + REWARDS × N — now 9 each)
- Counterweight verdict (inverts | amplifies | mixed)
- Blind ranking 1..N
- Per-criterion best/worst with anchor quotes

**Tuning signal:** which arm wins which scene, why, and which rubric dimensions discriminate.

### Layer 2 — Cherry-pick composition record (new; Phase 1.5 Step 2)

Persisted at `active-project/staff/reviews/cherry-pick-<book>-<chapter>-scene-<L>-<timestamp>.md`. Contains:
- Paragraph correspondence table (winner para → arm-K corresponding para per bone-range)
- Per-paragraph KEEP-WINNER | SUBSTITUTE decisions with evidence
- Substitution count, source distribution, tonal-seam-risk aggregate
- `ceiling-collapse: true|false` — true when 0 substitutions made

**Tuning signal:** where cherry-pick captures lift, where pure-winner is already optimal, which arms contribute which kinds of paragraphs.

### Layer 3 — Per-scene scorecard (new; Phase 1.5 Step 3)

Per `schemas/tournament-scorecard.schema.md`. Persisted at `active-project/staff/reviews/scorecard-<book>-<chapter>-scene-<L>-<timestamp>.md`, aggregated at `active-project/staff/showrunner/tournament-scorecards.md`. Contains:
- Per-PEEVE fire count + severity + anchor sentences
- Per-REWARD hit count + anchor sentences
- Scene-level numeric score
- Voice-consistency verdict (seamless | minor-seam | flag-seam)
- Tuning-signal flags (peeves-firing-on-every-arm, rewards-no-arm-hit, cherry-pick-source-concentration, ceiling-collapse-context)

**Tuning signal:** the accumulating evidence base. The ledger row also gets back-referenced to the Phase 9 verdict for that chapter (Phase 9.6 writes the Phase 9 fields into the ledger row).

### Layer 4 — Phase 9 cold-read verdict (existing)

The terminal gate. Already persisted at `active-project/staff/reviews/coldread-<book>-<chapter>-<timestamp>.md`. Contains EVENTS / JEOPARDY / CAUSALITY / PAYOFF / CONTINUE / ONE-LINE SUMMARY.

**Tuning signal:** the ground truth. The framework's whole point is to make Layers 1-3 predictive of Layer 4.

---

## Feedback loops

### Loop A — Scorecard → Rubric edit (within /and-stitch)

**Trigger:** 5+ scenes across 2+ chapters where the same peeve appears in `peeves-firing-on-every-arm` OR the same reward appears in `rewards-no-arm-hit`.

**Path:** admin process-critic detects the pattern from the aggregate ledger → drafts a `change_type: modify` (re-calibrate criterion) or `change_type: delete` (retire useless criterion) proposal against `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md` → principal triages → next chapter's tournament uses the revised rubric.

**Reversibility:** high. Rubric edits don't invalidate prior scorecards (they reference rubric-by-name); future runs use the new rubric; trend is visible in the ledger.

### Loop B — Cold-read FAIL → Rubric extension (within /and-stitch)

**Trigger:** Phase 9 cold-read FAIL on a chapter whose Layer 1-3 signals showed nothing wrong (the rubric was blind to the failure mode).

**Path:** admin process-critic auto-fires on the Phase 9 FAIL → reads the cold-read report + the Layer 1-3 outputs → drafts a `change_type: add` proposal for a new PEEVE or REWARD that would have caught the failure → principal triages → rubric extension lands.

**Example:** the 2026-05-27 cherry-pick experiment produced exactly this. Cold-read FAIL diagnostics ("the woman is never described as a person") were absent from the existing rubric → added PEEVE #3 special-case (function-token-only central figures) + REWARD #9 reader-orientation → next tournament dispatches the extended rubric.

**Reversibility:** high. Same as Loop A.

### Loop C — Cherry-pick concentration → Upstream gate (out of /and-stitch)

**Trigger:** 5+ scenes across 2+ chapters where `cherry-pick-source-concentration` consistently names the same rubric dimension (e.g. always RW2 Embodied, always PEEVE #5 compound-noun-saturation).

**Path:** admin process-critic identifies the concentration → if the criterion is about prose-surface taste (cadence, density), proposes promotion to a primary discriminator in the renderer-voice rubric; if the criterion is about bones-level facts (embodiment, body-staging, person-presence), proposes a `change_type: add` against `/and-write` Phase 1 (authoring guidance) or Phase 6 (AP-SCAN) — the same shape as PROP-0007's compound-noun escalation.

**Example:** PROP-0007 (compound-noun economy at `/and-write` Phase 1 + Phase 6) is the existing instance of this loop firing. The pattern was detected at /and-stitch (Phase 7 Q9 found bone-content compounds; bone-faithfulness fence blocked the cull); the fix lives upstream at /and-write.

**Reversibility:** medium. Adds upstream gates that affect future bones authoring; reversible by retiring the gate.

### Loop D — Cold-read FAIL + bones-level cause → /and-write revise --from-signals (terminal)

**Trigger:** Phase 9 cold-read FAIL where the diagnosis is bones-level (cost-not-legible, person-as-function-token, missing concrete-noun anchors for central figures) — failures the cherry-pick scorecard can detect but the cherry-pick composition cannot fix.

**Path:** Phase 9 verdict routes to `/and-write <chapter> revise --from-signals` (existing path) → /and-write Phase 1 reads the scorecard + the cold-read FAIL diagnosis as signals → bones authoring corrects the upstream cause → re-cascade through /and-facets + /and-stitch.

**Difference from current Phase 9 FAIL routing:** today's routing surfaces the diff between cold-read and intent; the scorecard adds a structured per-criterion attribution so /and-write knows which signal-class to address. Specifically: a FAIL where the scorecard fires RW9=0 + PEEVE #9 walkout = "the bones did not give a person to the reader." That's directly actionable at /and-write Phase 1 step 5 (SVO discipline + RW9 amendment).

**Reversibility:** high. Re-cascade produces a new draft; old draft preserved in git.

### Loop E — Ceiling-collapse > 50% → Exemplar selection (out of /and-stitch)

**Trigger:** `ceiling-collapse: true` on more than half the scenes across 3+ chapters.

**Path:** admin process-critic detects pattern → indicates the N arms are not differentiating enough at the rubric level (one arm always wins; cherry-pick has no room to operate) → either the exemplar candidate set is too homogeneous (Phase 0 step 4a needs more counterweight variety) or the rubric is not granular enough to discriminate (back to Loop A).

**Reversibility:** medium. Exemplar candidates can be added/swapped per chapter; rubric edits per Loop A.

---

## Promotion paths (criterion → gate)

Three-tier promotion based on where the gap is structurally addressable:

### Tier 1 — Audience-pattern → Rubric (Loop B)

A pattern the cold-reader (or post-op audience fork) flags consistently graduates into the renderer-voice rubric as a new PEEVE or REWARD. Cost: S. Reversibility: high. Triggers: 2+ chapters showing the pattern in cold-read or postop divergent forks.

### Tier 2 — Rubric-criterion → Authoring guidance (Loop C)

A rubric criterion that consistently fires across all arms (the tournament cannot fix it via prime selection) graduates into `/and-write` Phase 1 authoring guidance OR Phase 6 AP-SCAN. Cost: S (one bullet point + one classification table entry). Reversibility: medium. Triggers: peeves-firing-on-every-arm pattern across 5+ scenes.

### Tier 3 — Authoring gap → Substance contract (out of scope here)

A failure that survives both rubric and authoring guidance — i.e. the bones themselves cannot be authored to deliver the missing element because the substance contract doesn't allow it (dormancy-prefigure chapter deliberately deferring stakes) — escalates to substance-contract revision at `/and-substance chapter <slug> revise`. This is the c02 case under DEC-0024: the cold-read CONTINUE=no is design-intended-collision, not gate miscalibration; the proposal threshold for adding a dormancy-prefigure exemption to Phase 9 Step 2 requires a second chapter to discriminate "designed deferred stakes" from "actually under-delivering."

---

## Anti-patterns

### "Tournament-as-gospel"

The tournament rubric is a craft proxy. It is not the cold-reader. A variant that swept the 18-criterion rubric (9 peeves + 9 rewards) can still produce a chapter the cold-reader refuses to continue. The b01-c02 trail is the canonical evidence: every stitch passed the tournament (some swept it), all three failed the cold-read.

**Discipline:** the scorecard's `voice-consistency` field and tuning flags are the early-warning signals; Phase 9 cold-read is the truth.

### "Rubric inflation"

Each new PEEVE or REWARD added to the rubric increases the cost of every future tournament dispatch. The tuning framework adds criteria selectively, only under Loop B trigger conditions (2+ chapters of evidence), and removes them under Loop A trigger conditions (consistently 0-count rewards / always-firing peeves).

**Discipline:** before adding, ask: would this criterion have caught a real Phase 9 FAIL? If not, defer.

### "Bones-blaming"

Loop D routes scorecard signals back to /and-write. The temptation is to route every failure there because bones authoring is the deepest upstream lever. But many failures ARE within stitch reach (cadence, compound-noun density, paragraph-level economy). The scorecard's per-criterion attribution is the discriminator — RW9=0 + PEEVE #9 = bones; PEEVE #5 (compound-saturation) + PEEVE #6 (metronome) = stitch.

**Discipline:** route to /and-write only when the failure is structurally upstream of stitch (Loop D's specified trigger). Otherwise iterate within /and-stitch via Loop A/B.

### "Single-chapter calibration"

Rubric edits triggered by a single chapter's evidence are overfitting. The framework requires 2+ chapters or 5+ scenes for promotion triggers. The b01-c02 evidence was sufficient for adding PEEVE #9 and REWARD #9 BECAUSE the pattern recurred — cold-read FAIL on three distinct stitches of the same chapter with bones unchanged, plus convergent post-op Forks B+C on a separate pattern (compound-noun saturation, → PROP-0007).

**Discipline:** patience over reactivity. First-occurrence findings get recorded; not promoted.

---

## Open questions (for future tuning sessions)

1. **Should cherry-pick run on N=2 only?** The current spec runs cherry-pick on any N ≥ 2. At N=3+ the paragraph correspondence table grows quadratically; cost may not be worth it.

2. **Should the scorer be a different agent than the judge?** Currently both are `general-purpose`. Using a more specific persona for scoring (e.g. an audience-card fork) might produce more consistent severity calls — at the cost of importing the persona's biases.

3. **Should voice-consistency seam-flagging be a hard fence at composition or a soft signal at scoring?** Currently soft (composer flags; scorer reports; nothing auto-blocks). If `flag-seam` correlates with Phase 9 FAIL across 3+ chapters, tighten to composition-time hard fence.

4. **How does this framework interact with the audience-tournament (PROP-0005-A Phase 3) when it lands?** Currently the renderer-voice tournament is the only Tier-1 application. Audience tournaments would produce a third class of scorecard (per-persona-card) — the framework should generalize without rewrite.

5. **What's the minimum scorecard count for an admin process-critic auto-fire?** Currently the process-critic fires per Phase 9 verdict. Scorecard-driven auto-fires (e.g. "5 chapters with the same peeve always firing") would be a useful addition. Implement after 5+ chapters of accumulated ledger evidence — premature now.

---

## Provenance

- 2026-05-27 — v1 — initial framework. Authored after the b01-c02 cherry-pick experiment + cold-read FAIL (third stitch). Codifies the lessons from b01-c01 ablation (Loop A original instance: leave-out-exposition rank 1 → PROP-0001 + PROP-0002 dialogue-adjacent fence + per-chapter em-dash-fold cap), b01-c02 multi-arm tournament (Loop B original instance: voice-exemplar tournament codified via URI-STITCH-MULTI-ARM), b01-c02 cherry-pick experiment (Loops A + B + D fired: RW9 + PEEVE #9 added to rubric; cherry-pick promoted to default-on; tournament-tuning ledger schema authored).
