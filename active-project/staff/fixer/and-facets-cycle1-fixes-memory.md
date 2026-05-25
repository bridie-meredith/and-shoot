## SESSION-START — 2026-05-25T09:00:00Z — facets-cycle1-fixes-memory
dispatch: Phase 5b cycle-1 remediation for memory facet — all 3 reviewers dissented; dedupe callouts by [memory:id] and resolve with minimum change; ADD pre-validation per URI-FACETS-CYCLE-N-ADD
target: active-project/theater/facets/memory-b01-c01.md
audit-report: active-project/staff/auditor/facets-final-audit-r2.md (flags carried by reference); verdicts: cape-fic-reader + dark-fantasy-reader + worm-canon-pedant memory-r1-verdict.md
findings-queued: 2 entries (mem:1, mem:2) deduped from 3 verdict files

---
task: and-facets-cycle1-fixes-memory
facet: memory
episode: b01-c01
date: 2026-05-25
fixer-session: SESSION-START 2026-05-25T13:00:00Z
---

# /and-facets Phase 5b cycle-1 fixes — memory facet

## Dedup summary (3 verdicts → 2 unique callouts)

| Entry | cape-fic-reader | dark-fantasy-reader | worm-canon-pedant | Deduped action |
|-------|-----------------|---------------------|-------------------|----------------|
| mem:1 @3 | ACCEPT + SIGNAL (flag-013: cond-* slug) | ACCEPT + SIGNAL (flag-013) | ACCEPT + SIGNAL (flag-013) | NO-ACTION-DEFENDED |
| mem:2 @26 | REVISE (spineless fire) | REVISE (spineless fire) | REVISE (spineless fire) | ADD-LANDED-AFTER-UPSTREAM-EDIT |

---

## mem:1 @3 — NO-ACTION-DEFENDED

**Callout (all 3 reviewers):** flag-013 — target-reference slug `cond-override-architecture-residue-122ac` uses `cond-*` class form rather than the required `monument-*` convention (URI-032). All three reviewers flagged SIGNAL, not HARD. All three reviewers accepted the entry on all other axes.

**Fixer reasoning:**
- All three reviewers explicitly accepted the entry on monument-trigger, displacement-discipline, and licensing-discipline axes.
- Spine confirmed: narrator:7 @3 back=Y co=[mem:1].
- All reviewers rated this SIGNAL — not a hard block, not a revise verdict on the entry itself.
- Slug convention correction is margit territory (card rename or new card authoring under monument-class), not fixer territory. Fixer does not rename card slugs without margit authority.
- Minimum change to address criteria: none. SIGNAL carries forward as-is.

**Disposition:** NO-ACTION-DEFENDED

**Margit referral (flag-013):** `cond-override-architecture-residue-122ac` vs expected `monument-*` form. Margit to either (a) author `monument-override-architecture-prohibition` card sourced from the condition card, or (b) confirm `cond-*` form is canonical for this slug class and update URI-032 rubric.

---

## mem:2 @26 — ADD-LANDED-AFTER-UPSTREAM-EDIT

**Callout (all 3 reviewers):** spineless fire. mem:2 @26 co-cited [state:2, state:8] only. No narrator-interest at @26. No feel-flag at @26. V3 feel-as-spine carve-out fails condition (3): no feel-flag on same @proto-line-id. R2 judge's "graph spine" claim (state co-citation = licensing spine) is an authoring error — state-update co-citation confirms a story-world delta occurred; NI or feel co-citation confirms the interior registered the trigger. These are distinct requirements.

**Pre-validation (URI-FACETS-CYCLE-N-ADD):**
- @26 scene-map zone: scene-C, rhythm-shape: peak-and-release, peak-bone: @21. @26 is post-peak resolving tail — default-licit for memory-flag fire. PASS.
- Bone SVO: `oswyn-mudway-flea-bottom-elder lifts the chin` — categorization-completing body-tell; witch-label assembling.
- Monument-trigger: Westerosi-monument clamp on witch-label-formation. "The word has been waiting for a person" construction is the Planetos-specific recognition-clamp. Plausibly active per reviewer consensus. PASS.
- Displacement-discipline: description uses no proper nouns, no monument named; the cue-shape ("the way it lifts in the country's older stories when a word has been waiting for a person") produces the shape without naming the monument. PASS.
- Multi-justification (≥2 of 4 functional-register hits required): (a) moment of realization — Taylor catches the category closing around her; (b) social commentary — the institutional witch-categorization apparatus assembling through a body-tell; (c) painting characterization — Taylor's pattern-recognition registering the social-structure. ≥2 hits. PASS.
- Per-scene cap: only one memory-flag in scene-C. PASS.
- Sparsity: 2/27 = 7.4%. In-band (5–12%). PASS.
- Cross-facet contract: narrator-interest co-citation mandatory at @26. MISSING — this is the fault being repaired.

**Repair path (dispatch: "cross-facet anchor missing → land upstream edit first"):**

### Step 1 — ADD narrator:9 @26 to interest-narrator-b01-c01.md

New entry appended:
```
9 @26 the chin-lift filed her in a category she recognized the shape of without needing the country's name for it.
```

Register rationale: clinical-of-the-horrible base register. No feeling-word. Inventory-tell: the categorization is filed (registering, not reacting). "Without needing the country's name for it" — the interior catches the shape before the label arrives, consistent with Taylor's pattern-recognition profile and the monument's cue (the word was waiting; she recognizes the slot without needing the word). The NI entry is consistent with mem:2's description — they do not contradict on which channel fired. PASS.

### Step 2 — ADD [narrator:9] citation to proto-lines/b01-c01.md @26

Line @26 updated from:
```
26 oswyn-mudway-flea-bottom-elder lifts the chin [mem:2] [state:2] [state:8]
```
to:
```
26 oswyn-mudway-flea-bottom-elder lifts the chin [mem:2] [narrator:9] [state:2] [state:8]
```
(Note: state:8 subsequently deleted by state-updates cycle-1 remediation; proto-lines line reflects deletions applied by that session.)

### Step 3 — Update _cite-index.md

Changes applied (later superseded and consolidated by state-updates cycle-1 session):
- narrator section: 8 → 9 entries; narrator:9 @26 back=Y co=[mem:2, state:2, state:8] added
- mem:2 co-list: [state:2, state:8] → [narrator:9, state:2, state:8]
- state:2 co-list: [mem:2, state:8] → [mem:2, narrator:9, state:8]
- state:8 co-list: [mem:2, state:2] → [mem:2, narrator:9, state:2] (state:8 later deleted by state-updates session)

Current cite-index state (post state-updates session consolidation):
- narrator:9 @26 back=Y co=[mem:2, state:2]
- mem:2 @26 back=Y co=[narrator:9, state:2]
- spine for mem:2 is satisfied: narrator:9 @26

### memory-b01-c01.md

No change to entry text. Description and target-reference of mem:2 confirmed correct by all three reviewers. The spine gap was entirely upstream; the memory entry itself ships as written.

**Disposition:** ADD-LANDED-AFTER-UPSTREAM-EDIT

---

## Flag-013 (SIGNAL — both entries) — margit referral required

Both target-references use `cond-*` form rather than `monument-*`:
- mem:1: `cond-override-architecture-residue-122ac` → expected `monument-override-architecture-prohibition` or equivalent
- mem:2: `cond-kl-witch-label-formation-122ac` → expected `monument-witch-label-as-ancient-slot` or `monument-older-stories-word-waiting-for-person` or equivalent

All three reviewers rated SIGNAL, not HARD. dark-fantasy-reader and worm-canon-pedant escalated mem:2's slug as substantively affecting stitcher routing (condition card = process-rule; monument card = figurative-content anchor). The flag-013 findings are pre-existing; fixer carries them forward as SIGNAL, margit referral required.

Fixer does not revise cards directly. Both slugs are flagged for margit.

---

## File-level checks post-remediation

- Doubled-register gate: 1 Earth-Bet (mem:1) + 1 Westerosi (mem:2) — PASS
- Sparsity: 2/27 = 7.4% — in-band (5–12%) — PASS
- Pressure-signal inversion: both fires in flat-low or resolving tail; zero peak-bone fires — PASS
- Per-scene cap: scene-A = 1 fire (mem:1 @3); scene-B = 0; scene-C = 1 fire (mem:2 @26) — PASS
- Spine coverage: mem:1 → narrator:7 @3; mem:2 → narrator:9 @26 — PASS (post-repair)

---

## Files changed

| File | Change |
|------|--------|
| `active-project/theater/facets/interest-narrator-b01-c01.md` | +1 line: narrator:9 @26 |
| `active-project/theater/proto-lines/b01-c01.md` | @26: added [narrator:9] citation |
| `active-project/theater/facets/_cite-index.md` | narrator:9 added; mem:2 co-list updated; total count updated |
| `active-project/theater/facets/memory-b01-c01.md` | no change |

## SESSION-END — 2026-05-25T13:30:00Z — and-facets-cycle1-fixes-memory
findings-applied: 1 (mem:2 spine repaired via narrator:9 ADD upstream)
findings-skipped: 1 (mem:1 — NO-ACTION-DEFENDED; SIGNAL only, margit referral, not fixer scope)
exit: CLEAN
