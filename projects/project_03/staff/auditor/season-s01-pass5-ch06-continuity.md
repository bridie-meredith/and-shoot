audit:
  scope: episode
  target: active-project/theater/proto-lines/chapter-06.md
  pass: 5 — Continuity (fresh-fork independent re-verify)
  timestamp: 2026-05-07
  file_level: FAIL
  total_ids_checked: 122 (file lines); active beat IDs: 108 (excluding blank timeskip IDs 14 and 54, and deleted-gap IDs 62 and 71)
  verdicts:
    pass: 5
    flag: 3
    fault: 2
  fault_count_by_class:
    FAULT-CONTINUITY-PROP: 1
    FAULT-CONTINUITY-REF: 1

---

## Audit dimensions checked

1. Reachability — can each beat be reached from the prior beat without an unexplained spatial or temporal gap?
2. State persistence — do props, positions, and conditions established in earlier lines hold through the file unless changed?
3. Reference resolution — does each named entity resolve to a known slug, card, or prior introduction?
4. POV consistency — does the narrator remain taylor-hebert-westeros throughout (non-interlude file)?
5. Time consistency — does scene time flow forward monotonically or via documented timeskips?
6. Cause-effect — does each beat causally connect to what preceded it?
7. ch05→ch06 boundary — does ch06 open from the state ch05 closed?
8. ch06→ch07 boundary — does ch07 open from the state ch06 closed?
9. Special focus A — do IDs 108-113 place Taylor within 600m of the courier road segment for all subsequent fauna deployments (IDs 56-105)?
10. Special focus B — is the parchment prop in Rowan's custody at chapter close (ID 114 anchor)?

---

## Findings

### PASS findings (no report entry required per scope calibration; noted in summary)

- **POV consistency:** narrator: taylor-hebert-westeros declared in header; all subject lines in the fauna-deployment sequence (IDs 55-105) are taylor-hebert-westeros, the couriers, the ravens, or the guard. No beat in the file requires access to interiority not available from Taylor's external position. POV is clean.
- **Time consistency:** timeskip ID 14 (between ID 13 and ID 15) is undated but structurally legal per schema (blank numbered line = timeskip). Timeskip ID 54 (between ID 53 and ID 108) is likewise legal. Both whitespace gaps correspond to spatial and temporal transitions that are legible from surrounding beats. Time flows forward.
- **Cause-effect:** the death sequence (IDs 1-13) leads causally to Taylor seeking Rowan (IDs 15-53). The sealing of the parchment (IDs 42-45/114) leads causally to Rowan's departure (IDs 46-53). Taylor's transit (IDs 108-113) leads causally to the vantage-point fauna deployment (IDs 55-105). The nosebleed at ID 82 follows the sustained fauna-control sequence (IDs 56-81) and is consistent with cond-fauna-control-rules (15-30 min sustained use → nosebleed onset). No missing cause-effect links.
- **ch05→ch06 boundary:** ch05 closes with septon-rowan on foot, having witnessed Plumm record both names; septon-rowan drops the eyes (ch05 ID 88) as chapter close. ch06 opens with septon-dying-protector's death (ID 1), which is a new narrative moment not temporally anchored to ch05's close. The interval is unspecified. No carry-forward prop or position from ch05 close is required to initiate ch06 IDs 1-13. The boundary is reachable.
- **ch06→ch07 boundary:** ch06 closes with `the ravens land` (ID 105), Taylor on the bank, ravens grounded. ch07 opens with `the recorder opens the claims ledger` (ID 1) and shortly `septon-rowan reaches the counter` (ID 5) / `septon-rowan produces the parchment` (ID 95). Rowan's transit from ch06 (where he departs the lane at ID 52 with the parchment tucked at ID 114) to ch07's recorder's office occurs in whitespace between chapters — no transit beats exist in either file covering this interval. The whitespace is consistent with chapter-boundary convention; no fault.
- **Prop-custody chain (parchment):** parchment is drawn at ID 31, completed IDs 34-41, lifted ID 42, dried ID 43, folded ID 44, sealed ID 45, tucked ID 114. Between ID 114 and the chapter close (IDs 46-105), Rowan departs (ID 52) and does not reappear. No line transfers the parchment from Rowan after ID 114. The parchment is in Rowan's custody at chapter close. ch07 IDs 95-96 (produces / sets the parchment) are consistent with this custody state. PROP CHAIN: VERIFIED.
- **Non-monotonic ID body order:** file header documents the exemption: "inserted later: 106 between 38/39, 107 between 41/42, 108-113 after 54 (transit + vantage; range fix), 114 after 45 (prop-custody)." IDs 106, 107, 114, and 108-113 appear out of numeric order in the file body but within their documented insertion zones. Treated as licensed per dispatch instructions. No fault.
- **Deleted-gap IDs:** IDs 62 and 71 are absent from the file body (no line appears for these IDs; they are not blank numbered lines — they simply do not appear). Per schema, absent IDs in a gap sequence are valid deleted-line markers. The surrounding sequence (61→63, 70→72) is readable without those beats. No fault.
- **Guard slug (ID 100):** `the guard speaks to the second courier` — per fixer log entry ch06 fault-032, `the gate guard` was renamed to `the guard` (bare-noun form; no oc-* card required for generic background role). The current file correctly shows `the guard`. Slug resolution: valid.

---

### FAULT-CONTINUITY-REF

- **id:** fault-C01
- **type:** fault
- **what:** ID 57 in the current file reads `a raven drops from the bank edge`. The fixer-log entry for ch06 fault-009 states the repair as: `taylor-hebert-westeros extends the network` → `a raven drops from the tower lip`. The current file shows `bank edge` where the fixer log records `tower lip` as the applied fix.
- **why:** The discrepancy is a reference-resolution inconsistency between the fixer log (an auditable record of what was changed) and the current file. Two interpretations: (a) the fixer applied `tower lip` and a subsequent pass changed it to `bank edge` without logging the change — creating an unlogged edit; or (b) the fixer log entry misstates the applied fix (the actual edit was `bank edge`, the log was written with the wrong target string). Either way, the fixer log and the current file disagree on the content of this line. If `tower lip` is authoritative, the current file has an undocumented content change. If `bank edge` is authoritative, the fixer log carries a false record of the repair. The `bank edge` form is spatially coherent with the iter1 transit (IDs 108-113 place Taylor descending a bank, crouching, facing the approach road; the ravens at bank edge in ID 56 is consistent with this position). The `tower lip` form would place the initiating raven at the bell tower — which contradicts Taylor's vantage position established by IDs 108-113 (she is at the bank, not the tower). The `bank edge` form is likely the correct final state; the fixer log entry appears to carry a stale reference string from a pre-transit-fix draft of the chapter.
- **criteria:** Fixer must confirm which form is authoritative and reconcile the discrepancy: either (a) update the fixer log to record the actual applied fix (`bank edge`, not `tower lip`) or (b) if `tower lip` was intended and was changed by an undocumented subsequent edit, restore `tower lip` and document the edit. Given the spatial logic (bank-edge vantage established by IDs 108-113, ravens already settled on the bank edge at ID 56), the `bank edge` form is the spatially coherent choice. The fixer log is the more likely source of error.

---

### FAULT-CONTINUITY-PROP

- **id:** fault-C02
- **type:** fault
- **what:** The parchment prop first appears as subject-matter at ID 31 (`septon-rowan draws the parchment`). Prior to ID 31, the parchment has no establishment beat in this chapter. The sealing-and-custody chain (IDs 42-45/114) and the ch07 reference (ID 95: `septon-rowan produces the parchment`) all use the definite article `the parchment`, which presupposes prior introduction. The prop's physical source is not established: the writing materials (stylus, parchment) are drawn from somewhere — Rowan's room, the writing case, a satchel — but no line names the parchment entering the scene before Rowan draws it. This is a prop-introduction gap. In ch07, the prop appears in the claims recorder's office as `the parchment` (definite, traceable to ch06). The chain is internally consistent once the prop appears at ID 31, but ID 31 uses `the parchment` as if it were already present in the scene when no prior ID established it. This is a FAULT-CONTINUITY-PROP: a prop is referenced with the definite article without a prior introduction beat in the chapter. The chapter-plan constraints (cond-westerosi-customary-authority) do not address prop-introduction; this is a state-tracking rule from the pipeline.
- **why:** Downstream facet authoring (state-updates) will need to cite the moment the parchment enters custody-of-the-scene. Without an introduction beat, state-update facet authors must infer the introduction from ID 31's verb (`draws the parchment` implies it was previously elsewhere), which is ambiguous. The prop chain from ch06 to ch07 is load-bearing (it is the document refused by the recorder in ch07); an ambiguous introduction creates a citations gap at the state-updates facet.
- **criteria:** A prop-introduction beat must be added establishing the parchment's presence before ID 31. Options: (a) a beat showing Rowan producing or placing a parchment from the writing case before `draws` (e.g., `septon-rowan draws the parchment` recasts as `septon-rowan takes the parchment` as the introduction beat followed by the heading/write sequence); or (b) the writing-case prop (mentioned in studio state for s01e06, which covers the same sept environs location) is carried into this chapter as the parchment's source, with an explicit taking-beat before ID 31. This is an episode-scope fix.

---

### FLAGS (non-blocking; no criteria required)

- **id:** flag-C01
- **type:** flag
- **what:** ID 82 reads `the nosebleed starts` — a state-onset verb without a named actor subject. Per the SVO schema the subject must be a named entity. The pass-2 auditor did not fault this line (it does not appear in the ch06-pass2-reverify.md fault list), and the fixer log does not record a repair on ID 82. In ch02 the parallel line `the nosebleed starts` was faulted (ch02-fault-003) and recast to `blood reaches the lip`. This precedent was not applied to ch06 ID 82, which remains in the state-onset form. This inconsistency is a flag, not a fault — the line was passed by prior audit — but it creates a surface inconsistency with the ch02 resolution and may draw a fault if a subsequent pass applies the ch02 precedent globally.
- **criteria:** no action required at this pass; advisory for fixer or editor to normalize to the `blood reaches the lip` pattern established in ch02 if global consistency is desired.

- **id:** flag-C02
- **type:** flag
- **what:** ID 63 reads `the first raven clears the road bend` and ID 64 reads `the second raven reaches the approach track`. These lines introduce `the first raven` and `the second raven` as discrete named subjects — but the ravens were deployed as `the first group` (IDs 59, 67, 77, 84, 87, 89) throughout the surrounding sequence. The switch from group-subject (`the first group`) to individual-subject (`the first raven`, `the second raven`) at IDs 63-64 and back to group-subject at ID 67 is a reference-continuity flag: it is not clear whether `the first raven` is a sub-member of `the first group` or a separate individual, and the relationship is not established before IDs 63-64. This is not a fault (the usage is physically legible — two lead ravens scouting ahead of the group) but the pronoun switch creates ambiguity in state-update and narrator-interest facet citation.
- **criteria:** no action required at this pass; advisory for editor pass or narrator-interest facet author to establish the individual/group relationship at citation time.

- **id:** flag-C03
- **type:** flag
- **what:** The 600m ceiling check (special focus A). IDs 108-113 establish Taylor's vantage on a bank overlooking a field, facing the approach road. The couriers emerge from the Harrenhal postern (IDs 65, 93). The studio state records Harrenhal as "half a league north" — approximately 2.4km. Taylor's vantage is in the field between the sept and Harrenhal. The fauna harassment operates on the "approach road" and "approach track" segments (IDs 60, 64, 91-92) — the section of road between Harrenhal and the open field, after the couriers have ridden away from the postern. The 600m ceiling applies to Taylor's maximum operational range, not the distance to Harrenhal itself. The proto-lines do not specify the distance from Taylor's bank vantage to the active harassment zone on the approach road. The pass-2 auditor's note ("No constraint card violations found") accepts the iter1 transit fix as resolving the range problem; no independent measurement appears in any file. This is structurally unverifiable from the proto-lines alone — the 600m claim rests on the insertion commentary (file header: "range fix") without an explicit spatial anchor in the line content. The fauna deployments are consistent with the stated range if the approach road section harassed is within 600m of Taylor's vantage; no line contradicts this, but no line confirms the distance either. This is a flag for the record: the range compliance rests on assertion (insertion comment) rather than proof (spatial beat naming distance or landmark). Downstream constraint-auditing at facet-authoring time should establish the citation chain for range compliance via location-state facet rather than leaving it as asserted-only.
- **criteria:** no action required at this pass; advisory that the 600m ceiling for fauna deployment on the approach road is currently asserted by insertion comment only; location-state facet authors should establish the spatial anchor explicitly when citing IDs 113-56 as the deployment origin.

---

## Summary

The chapter-06 proto-line file is structurally sound on the following axes: POV consistency, time consistency, cause-effect chain, ch05→ch06 boundary reachability, ch06→ch07 boundary reachability, non-monotonic ID handling (licensed), deleted-gap IDs (schema-valid), and the parchment prop-custody chain from ID 114 through ch07 IDs 95-96 (VERIFIED).

Two faults identified:

**fault-C01** (FAULT-CONTINUITY-REF): The fixer log records `a raven drops from the tower lip` as the ch06 fault-009 repair; the current file shows `a raven drops from the bank edge`. These forms are in conflict. The `bank edge` form is spatially coherent with IDs 108-113 (Taylor at the bank); the `tower lip` form is not. The fixer log likely carries a stale pre-transit-fix reference string. Fixer must reconcile the log against the file and document the authoritative form.

**fault-C02** (FAULT-CONTINUITY-PROP): The parchment prop (`the parchment`) is referenced at ID 31 with the definite article but has no prior introduction beat in the chapter establishing where it came from. The prop chain from ID 31 onward is internally consistent and the ch06→ch07 handoff is clean, but the missing introduction beat leaves a state-update facet citations gap at prop-entry. An introduction beat must be inserted before ID 31.

Three flags (non-blocking): flag-C01 records the ID 82 state-onset verb inconsistency with the ch02 `blood reaches the lip` precedent. flag-C02 records the individual/group raven subject switch at IDs 63-64. flag-C03 records that the 600m fauna range compliance for the approach road rests on insertion-comment assertion rather than explicit spatial anchoring in the line content, and recommends location-state facet authors establish the citation chain.

FILE-LEVEL: FAIL (2 faults; both are episode-scope; no escalation required).
