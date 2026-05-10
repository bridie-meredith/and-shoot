```yaml
audit:
  scope: season
  target: s01
  pass: 2-reaudit-r6 (round 6 — convergence-or-discretionary gate)
  timestamp: 2026-05-09
  verdict: PASS
  verdict_summary: >
    All five r5 faults (IDs 337, 562, 439, 246, 544) verified closed by direct inspection.
    Full body re-walk finds zero surviving violations in any known fault class and zero
    new fault classes. Nine standing advisories carried forward unchanged; none promoted.
    Hard-escalate trigger not met. Pass 2 converges. Pass 3 (shape, dramatist) may dispatch.
```

---

# Season s01 Pass-2 Constraint Re-Audit — Round 6

**File:** `active-project/theater/proto-lines/s01.aggregate.md`
**Prior audit:** `active-project/staff/auditor/season-s01-pass-2-constraint-reaudit-r5.md`
**Prior fix log:** `active-project/staff/fixer/season-s01-pass-2-fix-log-round5.md`
**Scope:** full re-walk; convergence-or-discretionary gate

---

## SECTION 0 — Round-5 Fixer Verification

All five r5 faults verified against the current file by direct line inspection:

| r5 fault | Agg. ID | Expected form | Current file | Status |
|---|---|---|---|---|
| r5-fault-001 | 337 | `a townsman retreats` | `a townsman retreats` | CLOSED |
| r5-fault-002 | 439 | `oc-craftsman-father approaches the table` | `oc-craftsman-father approaches the table` | CLOSED |
| r5-fault-003 | 562 | `mira-stonefield-jaehaerys retreats` | `mira-stonefield-jaehaerys retreats` | CLOSED |
| r5-fault-004 | 246 | `the light crosses the window` | `the light crosses the window` | CLOSED |
| r5-fault-005 | 544 | `the town reeve approaches the inquiry rider` | `the town reeve approaches the inquiry rider` | CLOSED |

**5/5 CLOSED.**

Register check on recasts:
- IDs 337 and 562 (`retreats`) — consistent with `retreats` precedent at IDs 385, 393, 431, 438, 471. Register match: PASS.
- ID 439 (`approaches the table`) — destination is the collection table; confirmed by scene context (IDs 434–450 are table-centered; ID 441 `the townsman approaches the table` is the immediately adjacent parallel form). Register match: PASS.
- ID 246 (`the light crosses the window`) — stripped both modifiers; no referent ambiguity in surrounding sept-interior context. Clean form: PASS.
- ID 544 (`the town reeve approaches the inquiry rider`) — destination verified against IDs 542–551; ID 545 `the inquiry rider speaks to the town reeve` confirms pairing. Transitive, destination-named: PASS.

No recast introduces a bare-intransitive residue fault.

---

## SECTION 1 — Full Body Sweep

### Structural checks

- Header comment block (lines 1–4): intact.
- POV markers: five markers present and correctly placed.
  - `# pov: taylor-hebert-jaehaerys` (opening)
  - `# pov: mira-stonefield-jaehaerys` (after ID 564)
  - `# pov: taylor-hebert-jaehaerys` (after ID 643)
  - `# pov: oc-craftsman-mother` (after ID 700)
  - `# pov: taylor-hebert-jaehaerys` (after ID 788)
- `split-from` markers at file end: structural annotations, not schema violations (established in prior rounds). PASS.
- ID gaps: all gaps confirmed as established deletion markers from prior rounds (389, 752, 901–903, 913). Legal per schema. PASS.
- ID 388 / 390 sequence (gap at 389): pre-existing, legal. PASS.

### FAULT-FORM-MODIFIER sweep

No surviving `steps back` or `steps forward` instances.
No surviving adjective modifiers on `light` or `window`.
No new adverb-on-motion-verb instances found.
No new adjective-on-generic-noun instances found beyond standing advisory set.

### FAULT-FORM-NO-VERB sweep

No surviving bare-intransitive `approaches` without destination.
All `crosses` instances carry named location objects.
All `retreats` instances treated as licensed intransitive per prior-round ruling (directional withdrawal, observable, no destination required). Consistent with established precedent (IDs 385, 393, 431, 438, 471). No change in classification.

### FAULT-FORM-COPULA sweep

No `is`, `was`, `were`, `be`, `been`, `being` instances in body. PASS.

### FAULT-FORM-CONJUNCTION sweep

No `and`, `but`, `while`, `as` joining clauses within a proto-line. PASS.

### FAULT-FORM-MULTI-SUBJECT sweep

No multi-subject lines. PASS.

### FAULT-FORM-NON-ACTION-VERB / FAULT-FORM-INTERIORITY sweep

All `holds` instances verified against narrow license: all objects are body parts of the subject (`holds the feet`, `holds the eyes`, `holds the chin`, `holds the breath`, `holds the head`, `holds the mouth`, `holds the face`, `holds the hands`, `holds the shoulder`, `holds the finger`). All licensed.
No stative position-naming, possession, or containment verbs found. PASS.

### FAULT-FORM-PERCEPTION sweep

No `sees`, `hears`, `notices`, `watches`, `notes`, `counted`, `measured`, `tracked` or similar perception verbs. PASS.

### FAULT-FORM-NEGATION sweep

No negation constructions. PASS.

---

## SECTION 2 — Fault Inventory (Round 6)

**Total faults found this round: 0**
**New fault classes: 0**
**Hard-escalate trigger met: NO**

---

## SECTION 3 — Standing Advisories (Carried Forward Unchanged)

All nine standing advisories from r5 are carried forward. No advisory is promoted to fault in this pass.

| Flag ID | Agg. ID | Line | Status |
|---|---|---|---|
| r3-flag-002 | 412 | `rymer-hedge shifts the eyes` | Retained advisory — borderline object (prior ruling: pass) |
| r3-flag-003 | 763 | `oc-craftsman-mother fills the two cups` | Retained advisory — plural object |
| r3-flag-004 | 344 | `a mounted man tethers the horses` | Retained advisory — plural object |
| r3-flag-005 | 793 | `taylor-hebert-jaehaerys faces the table surface` | Retained advisory — `surface` as object qualifier |
| r3-flag-008 | 302 | `oc-child-peer calls` | Retained advisory — bare vocalization |
| r4-flag-001 | 309 | `oc-child-peer scrapes a boot against the cobble` | Retained advisory — prepositional phrase on manner |
| r4-flag-004 | 472/473 | dual `the collector's man` beats | Retained advisory — editor continuity |
| r4-flag-005 | 268 | `oc-craftsman-mother approaches the two children` | Retained advisory — ordinal adjective on object |
| r5-advisory-001 | 911 | `oc-craftsman-mother calls` | Retained advisory — bare vocalization; consistent with ID 302 treatment |

No advisory is promoted in this round. None has changed character since r5.

---

## SECTION 4 — Convergence Assessment

**Convergence trajectory:** 84 (r3) → 11 (r4) → 5 (r5) → **0 (r6)**

**Verdict: PASS.**

Pass 2 (constraint audit) converges. The file is clean against all schema constraints established across rounds 1–5. All fault classes are closed. The nine standing advisories are editor-scope items that do not block progression.

**Pass 3 (shape, dramatist) may dispatch.**

---

## SECTION 5 — Findings (Schema Format)

No fault or escalate findings this round.

```yaml
audit:
  scope: season
  target: s01
  pass: 2-reaudit-r6
  timestamp: 2026-05-09
  findings:
    - id: pass-001
      type: pass
      what: all proto-lines 1–912 (plus split-from annotations 914–915)
      why: zero schema violations found; all five r5 faults confirmed closed; no new fault classes
```
