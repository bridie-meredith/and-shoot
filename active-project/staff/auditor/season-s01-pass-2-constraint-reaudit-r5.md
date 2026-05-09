```yaml
audit:
  scope: season
  target: s01
  pass: 2-reaudit-r5 (round 5 — convergence audit after round-4 pattern-sweep fixer)
  timestamp: 2026-05-09
  verdict: FAIL
  verdict_summary: >
    Round-4 fixer correctly closed all 11 named r4 faults (RESOLVED-PRE-EXISTING, confirmed by
    direct file inspection) and applied 2 pattern-sweep fixes (IDs 558 and 238). However, this
    round finds 6 surviving fault instances within known classes: 3 borderline promotions
    (IDs 337/439/562 — directional adverbs on steps), 1 borderline promotion (ID 246 —
    adjective modifiers on subject/object), 1 missed bare-intransitive motion fault (ID 544),
    and 1 advisory flag for ID 911. No new fault classes are present. The hard-escalate trigger
    is NOT met. Fault count: 5 faults (IDs 337, 439, 562, 246, 544) + 1 retained advisory (ID 911).
    All are missed instances or promoted advisories within known classes. Borderline calls made
    below. ID 558 recast verified consistent.
```

---

# Season s01 Pass-2 Constraint Re-Audit — Round 5

**File:** `active-project/theater/proto-lines/s01.aggregate.md`
**Prior audits:** rounds 1–4 (see paths in dispatch)
**Scope:** full re-walk per convergence-gate mandate; emphasis on borderline items dispatched for ruling, and independent sweep for any pattern the round-4 fixer pass might have missed
**Escalation pre-condition:** new fault classes → hard-escalate; reintroduced/missed instances within known classes → discretionary

---

## SECTION 0 — Round-4 Fixer Verification

All 11 named r4 faults verified against the current file by direct inspection:

| r4 fault | ID | Expected | Current file | Status |
|---|---|---|---|---|
| r4-fault-001 | 466 | `the horse rears` | `the horse rears` | CLOSED |
| r4-fault-002 | 206 | `septon-rowan offers the volume` | `septon-rowan offers the volume` | CLOSED |
| r4-fault-003 | 895 | `the ferryman takes the folio` | `the ferryman takes the folio` | CLOSED |
| r4-fault-004 | 898 | `the ferryman grips the folio` | `the ferryman grips the folio` | CLOSED |
| r4-fault-005 | 372 | `the fishwife approaches the table` | `the fishwife approaches the table` | CLOSED |
| r4-fault-006 | 849 | `the maester reaches the workshop center` | `the maester reaches the workshop center` | CLOSED |
| r4-fault-007 | 761 | `oc-craftsman-mother approaches the shelf` | `oc-craftsman-mother approaches the shelf` | CLOSED |
| r4-fault-008 | 547 | `the inquiry rider draws the letter` | `the inquiry rider draws the letter` | CLOSED |
| r4-fault-009 | 234 | `septon-rowan draws a volume` | `septon-rowan draws a volume` | CLOSED |
| r4-fault-010 | 314 | blank (time-skip) | blank | CLOSED |
| r4-fault-011 | 835 | `oc-craftsman-father draws the door` | `oc-craftsman-father draws the door` | CLOSED |

**11/11 CLOSED.**

Pattern-sweep fixes (r4-sweep-1 and r4-sweep-2) verified:
- ID 558: `mira-stonefield-jaehaerys exits the alley` — CONFIRMED
- ID 238: `taylor-hebert-jaehaerys marks the column` — CONFIRMED

---

## SECTION 1 — Borderline Items: Rulings

### IDs 337, 439, 562 — Directional adverbs `back`/`forward` on `steps`

**Lines:**
```
337 a townsman steps back
439 oc-craftsman-father steps forward
562 mira-stonefield-jaehaerys steps back
```

**Prior treatment:** r4-flag-002 (advisory, not promoted). The round-4 fixer explicitly declined to promote, citing compound-motion-form argument and absence of prior-round flagging.

**Ruling: FAULT — all three.**

The schema is explicit: *"No modifiers. No adjectives, no adverbs, no prepositional padding."* `back` and `forward` are directional adverbs appended to a motion verb. The schema does not carve out an exception for directional particles, compound-motion forms, or idiomatic step-constructions. The Pass 1 brief lists `direction` as an explicitly banned prepositional-phrase type; directional adverbs serve the same semantic function. The compound-motion-form argument (that `steps back` is an idiomatic unit) is not a schema defense — the schema bans adverbs, not only prepositional phrases. The prior advisory treatment was a deferral pending this ruling, not a pass.

**Classification:** FAULT-FORM-MODIFIER (adverb on motion verb). Known class — Cluster E (adverb modifier). Prior-round cluster established in rounds 1 and 3.
**Type:** Promoted advisory — not a new class.
**Criteria:** Strip the adverb in all three cases. Recast to avoid bare-intransitive residue. Suggested forms:
- ID 337: `a townsman retreats` (consistent with `the fishwife retreats` at ID 393, `the collector retreats` at ID 471)
- ID 439: `oc-craftsman-father approaches the table` (or the next named destination in scene)
- ID 562: `mira-stonefield-jaehaerys retreats` (consistent with established `retreats` precedent)

---

### ID 246 — `the morning light crosses the east window`

**Prior treatment:** r4-flag-003 (advisory, passed on compound-noun grounds). The round-4 fixer did not promote.

**Ruling: FAULT.**

`morning` on `light` and `east` on `window` are adjective modifiers on generic nouns. The compound-noun defense applies to established prop-slug names used consistently throughout the file (e.g., `mordant pot`, `market satchel`, `account ledger`, `census folio`, `literacy register`, `dye-stirrer` — all hyphenated or multi-word names that appear repeatedly as named artifacts with consistent slug-form). `morning light` and `east window` do not meet this bar: neither is a named prop slug, neither appears elsewhere in the file as a recurring named entity, and neither is established in the warehouse. `morning` is a time-of-day adjective; `east` is a directional adjective. Both are modifier types the schema explicitly bans. The prior advisory treatment correctly identified the risk but did not make the promotion call.

**Classification:** FAULT-FORM-MODIFIER (adjective on subject; adjective on object). Known class — Cluster E (adjective modifiers on nouns).
**Type:** Promoted advisory — not a new class.
**Fix criteria:** Strip both modifiers. Recast: `the light crosses the window`.
**Note:** There is no collision or ambiguity created by stripping both: `the light` and `the window` are the only referents in the beat, and the surrounding context (baptismal sept interior, daytime lesson session) provides adequate orientation.

---

### ID 558 — Recast consistency check (`mira-stonefield-jaehaerys exits the alley`)

**Context:**
```
553 mira-stonefield-jaehaerys enters the alley
554 [time-skip]
555 taylor-hebert-jaehaerys enters the market square
556 [time-skip]
557 taylor-hebert-jaehaerys crosses the square
558 mira-stonefield-jaehaerys exits the alley
```

**Verdict: CONSISTENT — PASS.**

ID 553 (`enters the alley`) and ID 558 (`exits the alley`) are parallel transitive SVO forms. The motion is directionally coherent: mira enters the alley at ID 553, and exits at ID 558 after a scene-shift gap. The r4 sweep-1 fix (`exits the alley` replacing `steps from the alley entrance`) removed both the banned source-prep phrase and the banned ordinal-adjective modifier that was on the prior form. The current form is clean. No collision with surrounding beats.

---

## SECTION 2 — Independent Sweep: New Finding

### r5-fault-005 — FAULT-FORM-NO-VERB (bare intransitive motion verb without destination)

**ID:** 544
**Line:** `the town reeve approaches`
**Class:** FAULT-FORM-NO-VERB — `approaches` is a motion verb that implies a destination; used here without any direct object or destination
**Schema basis:** *"Bare intransitive motion verbs without destination fault FAULT-FORM-NO-VERB. `taylor moves` is not observable; `taylor enters the yard` is. The intransitive-lands-cleanly exception (`taylor exhales`) does not extend to motion verbs that imply destination."* `Approaches` implies a destination by definition (it is a directional approach-toward-something verb). Without naming the destination, the beat is not concretely observable.
**Prior-round history:** Not in any prior finding set (rounds 1–4). The r4 audit Section 3 does not include ID 544 in its passing list. This is a missed instance.
**Prior-round class:** FAULT-FORM-NO-VERB. Prior instances: various `crosses to X` recast targets (Cluster B); the `moves` and `walks` class banned at project inception.
**Type:** Missed instance within known class.
**Context:**
```
542 the inquiry rider enters the market square
543 the inquiry rider dismounts
544 the town reeve approaches
545 the inquiry rider speaks to the town reeve
```
The destination is clearly the inquiry rider (ID 545 establishes they are in dialogue). The fix is transitive: `the town reeve approaches the inquiry rider`.
**Fix criteria:** Recast to transitive: `the town reeve approaches the inquiry rider`.

---

## SECTION 3 — Advisory Items (Retained and New)

### r5-advisory-001 — ID 911: `oc-craftsman-mother calls`

**Line:** `911 oc-craftsman-mother calls`
**Status:** Retained advisory. Same pattern as r3-flag-008 (`oc-child-peer calls` at ID 302), which has been carried as an advisory flag through all rounds without promotion. ID 911 presents the same bare-vocalization pattern. Prior audits flagged `oc-child-peer calls` but did not flag this ID. Consistent treatment requires flagging ID 911 as well.
**Classification:** FLAG (retained; consistent with ID 302 treatment). Not promoted to fault absent a ruling to promote ID 302.

### Previously retained advisories (status unchanged)

| Flag ID | ID | What | Status |
|---|---|---|---|
| r3-flag-002 | 412 | `rymer-hedge shifts the eyes` | Retained advisory |
| r3-flag-003 | 763 | `oc-craftsman-mother fills the two cups` | Retained advisory |
| r3-flag-004 | 344 | `a mounted man tethers the horses` | Retained advisory |
| r3-flag-005 | 793 | `taylor-hebert-jaehaerys faces the table surface` | Retained advisory |
| r3-flag-008 | 302 | `oc-child-peer calls` | Retained advisory |
| r4-flag-001 | 309 | `oc-child-peer scrapes a boot against the cobble` | Retained advisory |
| r4-flag-004 | 472/473 | dual `the collector's man` — editor continuity | Retained advisory |
| r4-flag-005 | 268 | `approaches the two children` | Retained advisory |

---

## SECTION 4 — Full Fault Inventory (Round 5)

| Fault ID | Agg. ID | Class | Prior-round cluster | Type |
|---|---|---|---|---|
| r5-fault-001 | 337 | FAULT-FORM-MODIFIER (adverb `back` on `steps`) | Cluster E (rounds 1, 3) | Promoted advisory (r4-flag-002) |
| r5-fault-002 | 439 | FAULT-FORM-MODIFIER (adverb `forward` on `steps`) | Cluster E (rounds 1, 3) | Promoted advisory (r4-flag-002) |
| r5-fault-003 | 562 | FAULT-FORM-MODIFIER (adverb `back` on `steps`) | Cluster E (rounds 1, 3) | Promoted advisory (r4-flag-002) |
| r5-fault-004 | 246 | FAULT-FORM-MODIFIER (adjective `morning` on subject; adjective `east` on object) | Cluster E (rounds 1, 3) | Promoted advisory (r4-flag-003) |
| r5-fault-005 | 544 | FAULT-FORM-NO-VERB (bare intransitive motion verb `approaches` without destination) | Cluster B / FAULT-FORM-NO-VERB (rounds 1–4) | Missed instance |

**Total fault findings this round: 5**
**New fault classes: 0**
**Promoted advisories: 4** (IDs 337, 439, 562, 246)
**Missed instances within known classes: 1** (ID 544)

---

## SECTION 5 — Structure, Header, POV, and Constraint Checks

All 5 POV markers verified present and correctly placed. Header (4-line comment block) intact. ID gap inventory unchanged from round 4 (all legal). Slug resolution consistent throughout. Constraint-coherence (suppression-policy stage, active-cost ceiling, smallfolk political physics) unchanged — no new violations. `split-from` markers at end of file are structural annotations, not schema violations. **All structural checks PASS.**

---

## SECTION 6 — Escalation Pre-Condition Assessment

Per `active-project/staff/showrunner/escalation-pass2-cap-decision.md`:

> If the over-cap fixer iteration also reveals new fault classes... stop, escalate, audit the auditor.

**New fault classes found this round: ZERO.**

All 5 findings fall within fault classes established in prior rounds:
- FAULT-FORM-MODIFIER / Cluster E (adjective/adverb modifiers) — established rounds 1 and 3
- FAULT-FORM-NO-VERB (bare intransitive motion verb) — established round 1

The 4 promoted advisories (IDs 337, 439, 562, 246) were explicitly on the table as deferred calls; this round makes the call. The 1 missed instance (ID 544) is a pattern-sweep miss within the known FAULT-FORM-NO-VERB class.

**The hard-escalate trigger is NOT met.**

---

## SECTION 7 — Routing Recommendation

**Verdict: FAIL.**

5 faults remain. All are within known classes. None require a new fault-class ruling. This is a compact, well-bounded set:

| Finding cluster | IDs | Recommended fix |
|---|---|---|
| Adverb `back`/`forward` on `steps` | 337, 439, 562 | Strip adverb; recast to avoid bare-intransitive residue |
| Adjective modifiers on `light`/`window` | 246 | Strip both: `the light crosses the window` |
| Bare intransitive `approaches` | 544 | Recast: `the town reeve approaches the inquiry rider` |

**Decision for user or dispatcher:** The 5 faults are all within the known cluster taxonomy, the fix operations are mechanical (3 recast-to-avoid-bare-intransitive, 1 strip, 1 transitive recast), and none require new class analysis. A targeted fixer pass against these 5 IDs is sufficient. The dispatcher should explicitly instruct the fixer to:
1. Fix all 5 named IDs only — no further pattern-sweep is warranted (the sweep has been run exhaustively across rounds 3 and 4).
2. Verify that recast of IDs 337, 439, 562 does not introduce a bare-intransitive residue fault.

If this sixth fixer pass closes all 5 without introducing new violations, Pass 2 converges and **Pass 3 (shape, dramatist) can dispatch.**

If the round-6 audit finds new instances not in this set, the user should reconsider the fixer dispatch discipline (naming-only vs. pattern-sweep) before authorizing further iterations.
