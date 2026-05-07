---
audit:
  scope: episode
  target: s01e01 (state-updates facet, Phase 2 writer-fork output)
  timestamp: 2026-05-06
  rubric: design/shoot-v2/rubric-state-updates.md (V2 locked)
  phase1-baseline: 6/90 = 6.7% V2 accept rate
---

# Phase 2 State-Updates Audit — s01e01

## 1. Headline

**Total fires across all forks: 14 authored / 13 canonical** (1 withdrawn by Taylor fork before final list).
**Final entry list: 13 entries** (Studio 10 + Taylor 3 + Edric 1 = 14 authored; Taylor F1 withdrawn = 13 final).
**V2 accept rate (this audit): see §9.**

---

## 2. Canonical Merged Entry List

All forks combined. Monotonic IDs. Grouped by `@<beat>`, ascending.

| ID | Beat | Entry |
|----|------|-------|
| 1  | @9   | `prop:district-ledger.physical-condition: rolled -> unrolled` |
| 2  | @30  | `prop:district-ledger.taylor-entry: absent -> name-inscribed-pending-dictation` |
| 3  | @38  | `prop:letter.holder: taylor -> mid-air-between-them` |
| 4  | @40  | `prop:letter.holder: mid-air-between-them -> officer` |
| 5  | @41  | `prop:letter.seal-condition: intact -> broken` |
| 6  | @45  | `prop:letter.holder: officer -> taylor` |
| 7  | @48  | `actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible` |
| 8  | @48  | `prop:district-ledger.taylor-entry: name-inscribed-pending-dictation -> dictated-provisional` |
| 9  | @57  | `studio.doors_and_shutters.cottage-door: closed -> open` |
| 10 | @57  | `actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)` |
| 11 | @64  | `prop:district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin` |
| 12 | @64  | `actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks` |
| 13 | @68  | `prop:district-ledger.physical-condition: unrolled -> folded-or-stored` |
| 14 | @77  | `actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private` |

**Note on Taylor F1 withdrawal:** Taylor fork authored a 4th entry (`@45 actor:taylor-hebert-westeros.inventory: -letter-extended -> +letter-held`) and then self-withdrew it on cross-facet co-citation grounds (narrator-interest silent at @45; @43 fire is one beat off the flip-beat). The withdrawal is reviewed in §6 (Refusal verdicts). The canonical list above has 13 entries; if F1 is reinstated by reviewer, add ID 6b `@45 actor:taylor-hebert-westeros.inventory: -letter-extended -> +letter-held` between IDs 6 and 7, renumbering downstream.

---

## 3. Per-Entry Verdict Table

Key: CORRECT = passes all three V2 axes, no anti-pattern. INCORRECT-{class} = named failure.

| ID | Beat | Target.Field | V (verdict) | Notes |
|----|------|-------------|-------------|-------|
| 1  | @9   | prop:district-ledger.physical-condition | **CORRECT** | Verb "unrolls" = explicit physical-condition transition. Persists through @68. First-touch old=rolled. Approach-zone (tens=1) permitted: real prop-state mutation, not registration. Field-extension flagged. |
| 2  | @30  | prop:district-ledger.taylor-entry | **FLAG** | Reality: "the stylus moves on taylor's name" is ambiguous — at @30 the clerk is following the officer's dictation-in-progress (@20–@22 officer works the line, @22 stylus follows dictation). Stylus moving on a name during an active dictation pass is stylus-motion that may be recording other names, not necessarily a first-touch write of Taylor's entry. Taylor's name-inscription is more clearly established at @47–@48 (the officer speaks the entry, then dictates specifically). The claim that @30 is "first-touch of Taylor's name" is not secured by the proto-line text: "the stylus moves on taylor's name" can be read as the stylus passing over, not necessarily the inscription of Taylor's new entry. OLD is `absent` but the proto-line does not prove the name was absent before @30 and inscribed at @30. RISK: if @30 is not the first-touch beat, then `<old>=absent` is wrong (drift-old, anti-pattern #5), and the entire @30→@48→@64 chain is seeded incorrectly. |
| 3  | @38  | prop:letter.holder | **CORRECT** | Calibration anchor explicitly defends. Holder transitions from Taylor to mid-air. Persists through @39 until @40. Studio licensed. |
| 4  | @40  | prop:letter.holder | **CORRECT** | Chain: mid-air → officer. Officer unfolds presupposes receipt. Persistence through @42. Draft B (physical-condition transient) correctly rejected. |
| 5  | @41  | prop:letter.seal-condition | **CORRECT** | "seal breaks" = irreversible physical transition. ACCEPT signature explicitly named in rubric. First-touch old=intact. Holder context (officer) consistent with @40 chain. |
| 6  | @45  | prop:letter.holder | **CORRECT** | Calibration anchor explicitly defends. Flip-beat correctly identified vs. @43 (offer) and @44 (trajectory). Chain: officer → taylor. Persists through @49, @74. |
| 7  | @48  | actor:taylor-hebert-westeros.administrative-status | **CORRECT** | Calibration anchor authorizes. Field-extension licit. Narrator-interest @48 fires → POV co-citation satisfied. Tensometer @48=2 not @39-class. |
| 8  | @48  | prop:district-ledger.taylor-entry | **FLAG** | Conditional on ID-2 verdict. If ID-2 (@30 fire) is culled, then old here should be `absent` or `pending` (per calibration anchor's own phrasing), not `name-inscribed-pending-dictation`. Studio acknowledges this dependency in "Entry 7 note." If ID-2 stands as a FLAG rather than a CORRECT, the chain is valid but the @30 anchor is uncertain. Old-value becomes load-bearing: if @30 is culled, old must revert to `pending` per calibration anchor. The @30 fault propagates forward to a drift-old risk here. Not independently incorrect if @30 stands; but conditional. |
| 9  | @57  | studio.doors_and_shutters.cottage-door | **INCORRECT-REALITY** | Studio fires door-open (`closed -> open`) reasoning that Edric must pass through it. However, the proto-line reads "edric steps back through the door" — this implies the door was already open or openable, but it does NOT establish the door was `closed` immediately prior. More critically, the Edric-fork uses `sept interior (past threshold)` as the destination, and the state.md records "sept interior (door swung shut behind him)." The rubric calibration anchor for @57 explicitly conditions the door-close entry on proto-line evidence; the studio refusal to fire door-close is correct. But the door-open entry fires on an assumed prior state (closed) without explicit proto-line establishment of the door being closed when Edric crosses. The cottage-door state prior to @57 is not established by any prior proto-line entry or by a prior state-update in this file. The studio defends `<old>=closed` by citing the s01e06 state.md — but that is a future-session state file, not the s01e01 baseline. Using s01e06 state.md as the s01e01 `<old>` baseline is drift-old (anti-pattern #5) unless the s01e01 episode-open state establishes cottage-door:closed. This is an authority/frugality failure: `<old>` is not canonically established for s01e01. |
| 10 | @57  | actor:edric-cray.sublocation | **CORRECT** | Edric-fork licensed. `sublocation` is on-schema (verified: state.md has sublocation field). Old=`yard (near sept door)` traceable from @8 establishing context. Persistence confirmed: state.md records sept interior, yard out of sightline; no later proto-line returns him to yard. Tensometer @57=2 social-reversal; narrator-interest @57 fires, but non-POV actor-state requires no co-citation. |
| 11 | @64  | prop:district-ledger.taylor-entry | **CORRECT** | Calibration anchor explicitly authorizes. Chain from @48: dictated-provisional → marked-parallel-margin. Irreversible. Tensometer @64=3, STATE-UPDATE NOTE "co-citation strongly expected" honored. |
| 12 | @64  | actor:taylor-hebert-westeros.knowledge.record-state | **CORRECT** | Calibration anchor explicitly authorizes. Narrator-interest @64 fires → POV co-citation satisfied. Tensometer @64=3 strongly expects. Persistence absolute. Field-extension licit. |
| 13 | @68  | prop:district-ledger.physical-condition | **CORRECT** | "the clerk folds the board" is a physical transition closing the @9 open. Chain: unrolled → folded-or-stored. Persistence holds. Tens=1 release zone; real field-change permitted in 1-zone (per same defense as ID-1). |
| 14 | @77  | actor:taylor-hebert-westeros.mask-state | **FLAG** | Reality: mask-state is rubric-named as a licit extension, and narrator-interest @77 fires with explicit mask-thin content. Cross-facet co-citation satisfied. However, the `<old>` value `maintained-cooperative-child` is derived from persona-card reading, not from a prior state-update in this episode or a prior project-setup state-file field. The field-extension note says mask-state is new; if it is new there is no canonical `<old>` on file — the fork asserts the old value from persona-card inference. This is not a fatal drift-old if the persona card unambiguously establishes maintained-cooperative-child as the baseline; it is a soft flag for the showrunner to confirm at write-back time that the field-extension is properly baselined before the entry is applied. Additionally, `mask-thinned-private` as `<new>` is a single-beat state that may shift again in s01e02 (mask could be re-engaged when Taylor interacts with others inside the sept); persistence into s01e02 is plausible but not guaranteed. The Reality axis passes on the beat; the persistence caveat is episode-boundary. Flag, not fault. |

---

## 4. Cross-Author Dependency Check

Pairs/groups of entries sharing a beat, audited for consistency and distinct (target, field) pairs.

### @48 — ID-7 (Taylor) + ID-8 (Studio)

| Check | Result |
|-------|--------|
| Same beat? | Yes |
| Same (target, field)? | No — Taylor: `actor:taylor-hebert-westeros.administrative-status`; Studio: `prop:district-ledger.taylor-entry` |
| Contradiction? | No — they describe the same dictation event from two different target classes (actor-state + prop-state). Consistent: the dictation creates both the actor's classification and the ledger record. |
| Authorship licensed? | Taylor fork for actor:taylor; studio for prop. Both correct. |
| Verdict | PASS — no conflict, distinct (target, field), consistent narrative |

### @57 — ID-9 (Studio cottage-door) + ID-10 (Edric sublocation)

| Check | Result |
|-------|--------|
| Same beat? | Yes |
| Same (target, field)? | No — Studio: `studio.doors_and_shutters.cottage-door`; Edric: `actor:edric-cray.sublocation` |
| Contradiction? | Partial. Studio fires door-open; Edric-fork correctly notes "The door-state itself is studio's authority, not authored here." Consistent in scope. However, studio fires `closed -> open` while state.md records "door swung shut behind him" — this suggests the door did close eventually, which studio explicitly withheld. The two entries are not in direct contradiction on the same (target, field) pair, but the studio entry leaves the door in `open` state with no close entry, while Edric's state.md records the door shut. The unresolved door-state is a dependency gap, not a contradiction between the two entries. |
| Authorship licensed? | Studio for door; Edric-fork for sublocation. Both correct. |
| Verdict | FLAG — door left in `open` state after @57 with no close entry; state.md records closed. This is the studio's known withheld refusal (no proto-line evidence for close). The gap means canonical door-state will be `open` at write-back unless a close entry is added in Phase 4. See §6 for refusal verdict on door-close. |

### @64 — ID-11 (Studio ledger) + ID-12 (Taylor knowledge)

| Check | Result |
|-------|--------|
| Same beat? | Yes |
| Same (target, field)? | No — Studio: `prop:district-ledger.taylor-entry`; Taylor: `actor:taylor-hebert-westeros.knowledge.record-state` |
| Contradiction? | No — two sides of the same registration event. Consistent: ledger is physically marked; Taylor's knowledge of the record-state changes. |
| Authorship licensed? | Studio for prop; Taylor fork for actor:taylor. Both correct. |
| Verdict | PASS |

---

## 5. Refusal Verdicts

| ID | Fork | Beat | Defended NONE | Verdict |
|----|------|------|---------------|---------|
| T1 | Taylor | @39 | "feet-set is @39 held-against-turn; tensometer STATE-UPDATE NOTE explicitly forbids canonical state-update; resolves at @40" | **NONE-CORRECT** — Tensometer @39 STATE-UPDATE NOTE is the authority: "any co-citation here must be actor-posture only; pure registration class — canonical state does not change at @39." The refusal is correct and explicitly supported by the calibration anchor. |
| T4 | Taylor | @50 | "turning is momentary directional shift per rubric REJECT signature; reverts at @54; tens=1, narrator-interest silent" | **NONE-CORRECT** — Rubric names @50 explicitly as a REJECT signature for posture-as-state (#8). Strip-test passes for refusal. |
| T5 | Taylor | @52 | "cross-POV trap; actor:mira is Mira-fork authority; count-of-allies is not a tracked field per rubric REJECT signature" | **NONE-CORRECT** — Rubric explicitly names the ally-count perception as not a tracked field. Cross-POV authoring (anti-pattern #2) would fire if Taylor fork wrote actor:mira.engagement-state. Refusal correct. |
| S6 | Studio | @43 | "pre-emption of @45 flip-beat; anti-pattern #7; calibration anchor explicitly names @43 as not the fire beat" | **NONE-CORRECT** — Calibration anchor is explicit. @43 is the offer; @45 is the flip-beat. Correct. |
| S5-close | Studio | @57 | "no proto-line evidence door closes at @57; rubric calibration anchor conditions close entry on proto-line evidence" | **NONE-CORRECT (with caveat)** — The refusal to fire door-close at @57 is correct per rubric (conditional confirmed by anchor). However, the canonical state.md records "door swung shut behind him" — the close-event is real but unanchored to a specific proto-line beat. This leaves a write-back gap: the door will be in `open` state at episode end unless a Phase 4 repair fires the close. The refusal is rubric-correct but creates a downstream continuity obligation. Flag for Phase 4. |
| F1 | Taylor | @45 | "inventory entry withdrawn: narrator-interest silent at @45; @43 fire is one beat off; POV co-citation requirement unmet" | **NONE-CORRECT** — The co-citation requirement is real: every `actor:taylor.*` entry requires narrator-interest co-citation on the exact `@<beat>`. Narrator-interest fires at @43 (letter returns), not @45 (palm closes). The Taylor fork correctly identifies the mismatch and withdraws. The withdrawal is proper floor-defense. Note: this means Taylor's inventory does not update at @45 in the canonical file; the prop-side entry (studio @45) captures the mutation, and Taylor's inventory can be inferred but is not directly written back. This is the design tradeoff the fork accepted. |
| F3 | Taylor | @23 | "exposure-state is registration-only; rubric REJECT signature names @23 explicitly; narrator-interest is the register" | **NONE-CORRECT** — Rubric REJECT signature explicitly names @23: gaze-targeting is narrator-interest territory, not state-updates. Correct. |

---

## 6. SKIP-MISSED Check

Walk the proto-lines for beats where the rubric warrants a state-update that no fork fired.

Conservative standard: only mark SKIP-MISSED when a field demonstrably changes and persists.

| Beat | Proto-line | Assessment |
|------|-----------|------------|
| @11 | officer comes through the gate | Studio correctly refused (actor-state not studio authority; gate status not established). Officer-fork is not active in this batch. SKIP-MISSED if an officer-fork were running — but officer-fork was not dispatched. **Not in-scope for this batch.** |
| @14 | taylor crosses the twelve feet of packed dirt | Taylor's position changes. No Taylor-fork actor-position entry exists. Taylor's state.md presumably tracks position, but no position-update entry fires. However: no narrator-interest co-citation exists at @14 (narrator-interest silent), so a `actor:taylor-hebert-westeros.position` entry would have no POV co-citation. Additionally, the rubric's approach-zone (tens=1 through @22) is permitted-silent on actor-state — these are establishing-state beats. **NOT SKIP-MISSED — approach-zone; no narrator-interest co-citation available.** |
| @15 | taylor enters the line | Same as @14 reasoning. **NOT SKIP-MISSED.** |
| @41 | the seal breaks | Covered by ID-5. |
| @42 | the officer folds the letter back | Prop:letter.physical-condition might warrant a folded-back entry. However: the officer re-folds the letter after unfolding at @40; the physical-condition during @40–@42 is `unfolded` (transitional); at @42 it returns to `folded`. Studio chose to track `holder` chain rather than `physical-condition` across the unfold/refold cycle, correctly treating the unfold→refold as a transient (fails persistence-test: the unfolding does not persist). **NOT SKIP-MISSED — correctly identified as transient; studio rationale in S3a addresses this.** |
| @46 | officer turns toward the clerk | Actor position/orientation shift. No co-citation. Tens=1. **NOT SKIP-MISSED.** |
| @57 | edric steps back through the door (door close) | The door-close is unanchored. Studio's S5-close refusal is rubric-correct. Edric's state.md records "door swung shut behind him" — this canonical state exists but has no proto-line that establishes the closing moment. The close happens at or after @57 but is not established in proto-lines. This is a **SKIP-MISSED candidate** for Phase 4 only: the door-close needs a write-back entry somewhere. It cannot fire at @57 without proto-line evidence; it may need a @57-post or a cleanup entry. **FLAG for Phase 4 — not a current-batch SKIP-MISSED since no proto-line supports the fire.** |
| @65 | officer's shoulder turns toward the gate | Not a persistent position change in-episode; approach to departure. Tens=1. **NOT SKIP-MISSED.** |
| @70–@76 | taylor turns, steps, finds latch, lifts latch | Taylor's position chain changes across @70–@77. No Taylor-fork position entries fire. Narrator-interest is silent from @70–@76 (fires only at @73 frame-shadow and @77 through-door). A `actor:taylor-hebert-westeros.position` or `sublocation` entry at @77 (she crosses the threshold) is potentially warranted: this is a persistent location change (she enters the sept interior). However, narrator-interest @77 fires and the Taylor fork addresses @77 as a mask-state event, not a position event. A position entry at @77 would require narrator-interest co-citation on @77 — narrator-interest @77 fires, so the co-citation would be satisfied. **Soft SKIP-MISSED: `actor:taylor-hebert-westeros.sublocation` (or position) at @77 — she crosses the sept threshold. The change is persistent; narrator-interest co-citation is available. Not caught by any fork.** |

### Named SKIP-MISSED

| SMID | Beat | Description | Severity |
|------|------|-------------|----------|
| SM-1 | @77 | `actor:taylor-hebert-westeros.sublocation` (or position): yard -> sept-interior. Taylor crosses the sept threshold at @77, matching Edric's schema field. Narrator-interest @77 fires → POV co-citation satisfied. Persistent: Taylor stays in sept interior through episode end. | **fault** (missed irreversible location-change on POV actor; narrator-interest co-citation available but not consumed) |
| SM-2 | @57 | `studio.doors_and_shutters.cottage-door: open -> closed` — physically implied by Edric's state.md ("door swung shut behind him") but unanchored to a proto-line beat. Phase 4 obligation. | **flag** (no proto-line anchor; Phase 4 must resolve) |

---

## 7. Cross-Facet Contract Verification

### Tensometer cross-facet

| Requirement | Beat | Status |
|-------------|------|--------|
| @39 must NOT receive canonical state-update | @39 | PASS — no entry fires at @39 |
| @64 strongly expects state-update co-citation | @64 | PASS — ID-11 (ledger) + ID-12 (knowledge) both fire |
| @38 co-citation permitted | @38 | PASS — ID-3 fires on prop:letter.holder (permitted class) |
| @48 not @39-class, no prohibition | @48 | PASS — IDs 7 and 8 fire correctly |

### Narrator-interest cross-facet (POV co-citation requirement)

Every `actor:taylor-hebert-westeros.*` entry must have a narrator-interest entry on the exact `@<beat>`.

| Entry ID | Beat | actor:taylor field | NI fire at beat? | Status |
|----------|------|--------------------|-----------------|--------|
| 7 | @48 | administrative-status | YES — NI @48 fires | PASS |
| 12 | @64 | knowledge.record-state | YES — NI @64 fires | PASS |
| 14 | @77 | mask-state | YES — NI @77 fires | PASS |
| SM-1 | @77 | sublocation (missed) | YES — NI @77 fires | Co-citation WOULD be satisfied if entry were present; supports SKIP-MISSED classification |

### Non-POV actor-state (co-citation NOT required)

| Entry ID | Beat | actor | NI required? | Status |
|----------|------|-------|-------------|--------|
| 10 | @57 | edric-cray | NO | PASS |

### Studio/prop (co-citation NOT required)

All studio.* and prop:* entries: co-citation not required. All pass by rule.

---

## 8. File-Level Verdict

### SHAPE-OK / SHAPE-FAIL assessment

| Axis | Target | Result |
|------|--------|--------|
| Density | 8–18% band (~6–14 entries / 77) | 13 entries / 77 = **16.9%** — within band. PASS |
| Approach-zone sparsity | @1–@22 nearly silent | Entries at @9 only (prop physical-condition). 1 entry in 22 beats = 4.5%. PASS |
| Confrontation-zone density | @23–@48 + @57 + @64 cluster | 10 entries in confrontation cluster vs 1 in approach (22 beats): ratio ~10× exceeds 2× requirement. PASS |
| Target diversity | studio.*, prop:*, actor:POV, actor:non-POV | 4 target classes represented. PASS |
| POV actor co-citation | every actor:taylor.* pairs with NI | 3 entries, 3 co-citations verified. PASS |
| Cross-facet @64 | strongly expected | Honored (ID-11 + ID-12). PASS |
| Cross-facet @39 | forbidden | Honored (no entry). PASS |

**File-level verdict: SHAPE-OK**

Named caveats:
1. **ID-2 (@30) FLAG** — `<old>=absent` for ledger.taylor-entry is asserted without secure proto-line grounding. If culled, ID-8 (@48) old-value must revert to `pending`. Chain dependency must be resolved at Phase 4.
2. **ID-9 (@57 door-open) INCORRECT-REALITY** — `<old>=closed` derived from s01e06 state.md, not from s01e01 episode-open baseline. Drift-old risk; Phase 4 must establish s01e01 cottage-door baseline or cull this entry.
3. **SM-1 (@77 taylor sublocation) SKIP-MISSED** — POV actor fails to record position-change on threshold-crossing; NI co-citation is available. Phase 4 addition required.
4. **SM-2 (@57 door-close) FLAG** — door left `open` at write-back; state.md shows `closed`. Phase 4 must anchor and fire the close.
5. **ID-14 (@77 mask-state) FLAG** — `<old>` is persona-card-inferred, not a prior state-update. Showrunner must baseline the field-extension before write-back.

---

## 9. Lift Report

| Stage | Entries | Beats | Rate |
|-------|---------|-------|------|
| Phase 1 V2 baseline | 6 | 90 | 6.7% |
| Phase 2 final canonical list | 13 | 77 | **16.9%** |
| V2 accept (this audit) | 10 CORRECT + 3 FLAG | 13 | 76.9% per-entry pass rate |
| SKIP-MISSED adds (Phase 4 obligation) | +1 fire (SM-1) | — | — |
| Phase 2 V2 lift | +10.2pp | — | 6.7% → 16.9% |

**V2 baseline 6.7% → Phase 2 V2 16.9%. Lift: +10.2 percentage points.**

Per-entry breakdown:
- **CORRECT:** IDs 1, 3, 4, 5, 6, 7, 10, 11, 12, 13 = **10 entries**
- **FLAG:** IDs 2, 8 (conditional on ID-2), 14 = **3 entries**
- **INCORRECT-REALITY:** ID-9 = **1 entry**
- **SKIP-MISSED:** SM-1 (@77 taylor sublocation) = 1 obligated add

---

## Findings

```yaml
findings:
  - id: fault-001
    type: fault
    what: ID-9, @57, studio.doors_and_shutters.cottage-door, <old>=closed derived from s01e06 state.md
    why: Using a future-session state file as the s01e01 baseline is drift-old (anti-pattern #5). If the s01e01 episode-open cottage-door state is not explicitly established as closed, the entry's old-value is ungrounded and will corrupt canonical write-back.
    criteria: Entry must supply <old> from a verified s01e01 baseline source (episode-open state, not s01e06 state.md). If no s01e01 baseline establishes cottage-door:closed, the entry must be culled or the baseline must be authored before the entry ships.

  - id: fault-002
    type: fault
    what: SM-1, @77, actor:taylor-hebert-westeros.sublocation (or position) — no entry authored
    why: Taylor crosses the sept threshold at @77, a persistent location-change on the POV actor. Narrator-interest @77 fires, satisfying the co-citation requirement. The omission means Taylor's canonical position is not updated at write-back, corrupting her spatial state for s01e02 onward.
    criteria: Phase 4 must add an entry for actor:taylor-hebert-westeros.sublocation (or equivalent position field) at @77, transitioning from yard to sept-interior (or equivalent). Entry must cite narrator-interest @77 as co-citation.

  - id: flag-001
    type: flag
    what: ID-2, @30, prop:district-ledger.taylor-entry, <old>=absent assertion
    why: "The stylus moves on taylor's name" at @30 is ambiguous — the clerk has been following dictation since @22; the name-inscription may precede @30 or @30 may be a continuation pass, not a first-touch. If @30 is not the first-touch, <old>=absent is incorrect and seeds drift-old into the @48 chain.
    criteria: No fix required at Phase 2. Phase 4 reviewer must determine whether @30 is the first-touch beat for taylor-entry or whether the inscription began earlier. If ID-2 is culled, ID-8's <old> must revert to `pending` (calibration anchor phrasing) or `absent`.

  - id: flag-002
    type: flag
    what: SM-2, @57 door-close — studio correctly withheld but state.md records cottage-door closed
    why: The door will be written back as open after @57 unless a close entry is authored. State.md records "door swung shut behind him" — the close is real but has no proto-line anchor in s01e01.
    criteria: Phase 4 must either (a) identify a proto-line beat that establishes the door-close (check whether the narrative context of @57 implies the close within the same beat), or (b) author a non-proto-line baseline correction entry with explicit justification. The write-back must not leave cottage-door in open state at episode close.

  - id: flag-003
    type: flag
    what: ID-14, @77, actor:taylor-hebert-westeros.mask-state, <old>=maintained-cooperative-child inferred from persona card without prior state-update on the field
    why: mask-state is a new field-extension with no project-setup baseline state-file entry. Showrunner cannot apply the write-back without a confirmed baseline. If the persona card is treated as the baseline source, this must be made explicit in the field-extension note.
    criteria: Before write-back, showrunner must confirm the mask-state field baseline from the persona card and record it in the actor's state.md as an episode-open value. No fixer action required; showrunner verification at write-back gate.

  - id: flag-004
    type: flag
    what: Taylor F1 withdrawal — actor:taylor-hebert-westeros.inventory not updated at @45
    why: The letter moves into Taylor's inventory at @45 per the prop-side entry, but no actor-side inventory entry fires. Taylor's inventory state at write-back will not reflect letter-held unless inferred from prop:letter.holder. Downstream episodes or stitcher querying actor:taylor-hebert-westeros.inventory directly will not find the letter.
    criteria: Advisory only. If the actor state schema explicitly tracks inventory separately from prop-holder chain, Phase 4 should revisit F1. If inventory is considered derivable from prop-side holder chain, this gap is acceptable and may be resolved by showrunner convention. No immediate fixer action.
```
