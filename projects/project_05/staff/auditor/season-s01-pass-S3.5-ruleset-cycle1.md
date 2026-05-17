# Audit Report — Season s01 Pass S3.5 — Ruleset Compliance (Mechanic-Strictness)
# schema: schemas/audit-report.schema.md
# generated: 2026-05-11
# auditor-fork: Sweep A / S3.5
# target: active-project/theater/proto-lines/s01.bones.md
# file-level verdict: RULESET-FAIL
# archive: cycle-1 (superseded by cycle-2)

---

## Scope

Walk of all numbered non-blank lines in `active-project/theater/proto-lines/s01.bones.md` (~480 active bones, IDs 1–508 with gaps). Evaluated against:
- Non-action-verb deny-list (full list per brief + schema)
- `holds` narrow license
- Mechanic re-check: copulas, negations, perception verbs, modifiers, conjunctions, abstractions-as-objects
- Drift-pattern report (verb ≥5 instances as borderline state-verb)
- Idiom-depletion check (URI-007, 2026-05-10): physical-stasis idioms ≥10 instances

Bias applied: when in doubt, flag.

---

## Checks run — clean passes

| Check | Result |
|---|---|
| Copulas (`is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being`) | CLEAN — zero instances |
| Negations (`didn't`, `does not`, `won't`, etc.) | CLEAN — zero instances |
| Perception verbs (`read`, `took`, `tracked`, `noted`, `counted`, `measured`, `watches`, `sees`, `hears`, `notices`) | CLEAN — zero instances |
| Prepositional-padding modifiers (appended to complete SVOs) | CLEAN — `pivots toward` uses all within licensed form; no unlicensed directional/instrumental/locative appendages found |
| Conjunctions (`and`, `but`, `while`, `as`) | CLEAN — zero instances |
| Multi-subject lines | CLEAN — zero instances |
| Dialogue form (`speaks to <listener>`) | CLEAN — all dialogue beats follow licensed form; no spoken content embedded |
| Deny-list: possession verbs | CLEAN |
| Deny-list: sustained-carrying verbs | CLEAN |
| Deny-list: containment verbs | CLEAN |
| Deny-list: `lies`, `stands` | CLEAN |
| Idiom-depletion (URI-007): `holds the feet` | 6 instances — below 10-instance threshold. No depletion flag. |
| Idiom-depletion (URI-007): `holds the eyes` | 5 instances — below 10-instance threshold. No depletion flag. |
| Idiom-depletion (URI-007): `holds the chin` | 1 instance — below threshold. |

---

## Findings

---

### fault-001

- **id:** fault-001
- **type:** fault
- **bone:** 166
- **line:** `oc-tanner-father holds the step`
- **what:** `holds` with object `the step`. "The step" is not a body part of the subject and is not a physical object resisting external pressure. It is a motion-unit abstraction meaning "pause mid-stride." Neither prong of the narrow `holds` license is satisfied: (1) body-part-as-object for stillness-against-pressure — `the step` is not a body part; (2) physical-object-resisting-pressure — `the step` is not a physical object. This is the idiom "holds his step" = pauses, which is a stative-pause construction.
- **why:** Unlicensed `holds` use passes a state-verb through the bone layer. The stitcher renders this as a physical act; the facet pass inherits a false premise. Downstream: the rendered moment encodes a non-event as an event, degrading physical-action fidelity.
- **fault-class:** FAULT-FORM-NON-ACTION-VERB
- **criteria:** Recast bone 166 as the discrete observable act. Options: `oc-tanner-father stills` (joins the established intransitive-stasis pattern); `oc-tanner-father stops`; or split into the action that the pause delays (already present in context). Do not use `holds` with a motion-unit object.
- **scope:** episode — single bone, single change.
- **route:** fixer

---

### flag-001

- **id:** flag-001
- **type:** flag
- **bone:** 318
- **line:** `oc-tanner-mother sits`
- **what:** Intransitive `sits` used as the sole verb. Schema rule: "`sits` describing position rather than the act of sitting/standing/lying" faults FAULT-FORM-NON-ACTION-VERB. The schema also notes that `taylor stands` as the discrete act of rising passes. The intransitive form `sits` is ambiguous between (a) the discrete act of taking a seat (arriving and sitting down — licensed) and (b) the stative descriptor (she is seated — faults). Context: oc-tanner-mother has just entered the room (bones 315–316); bone 318 follows her entering and facing the narrator. In that context `sits` most naturally encodes the discrete act of sitting down. However, the rule requires certainty and bias is toward flagging.
- **why:** If stative, this is a non-action verb that should be a loc-state facet. If discrete, it passes. Ambiguity at the bone layer propagates to the stitcher.
- **criteria:** N/A (flag — screen-writer to confirm intent). If discrete act, add no change. If stative, recast or move to loc-state facet.
- **scope:** episode — single bone.
- **route:** screen-writer for intent confirmation; fixer if stative confirmed.

---

### flag-002

- **id:** flag-002
- **type:** flag
- **bone:** 226, 274, 355, 449
- **line (representative):** `the headache wakes taylor-hebert-flea-bottom`
- **what:** `the headache` as grammatical subject performing a physical action on the POV character. Appears 4 times (bones 226, 274, 355, 449 — the three recurring headache-onset beats and a parallel). Per schema, subject must be "a named entity — actor slug, prop slug, or `the <noun>` for unnamed environment elements." `the headache` is a `the <noun>` form but it is a bodily/internal sensation, not an environment element. A sensation triggering waking is an internal event rendered as an external physical act. This is borderline FAULT-FORM-INTERIORITY: the interiority (pain-sensation) is promoted to subject-slot and given agency over a physical act.
- **why:** If classified as interiority-as-subject, the bone is contaminated and the stitcher generates an action-beat from internal experience data, bypassing the facet layer where interiority belongs. Pattern: 4 identical instances — the recurring headache-wake beat is a structural device; if it faults, all four instances fault together.
- **criteria:** N/A (flag — below threshold for fault per ambiguity). Recommend screen-writer review: is `the headache` functioning as an environment element (external physical force) or an internal sensation? If the latter, recast: e.g., `taylor-hebert-flea-bottom wakes` (bone-level) + headache onset moved to a feel-flag facet citing the bone. If the former, document the ruling for the fixer.
- **scope:** episode-scope (4 bones across season span); if reclassified as fault, all 4 instances route to fixer.
- **route:** screen-writer for ruling; escalate to fixer if fault classification confirmed.

---

### flag-003

- **id:** flag-003
- **type:** flag
- **bone:** 235
- **line:** `the lords-man's man moves the family possessions`
- **what:** Transitive `moves` with the direct object `the family possessions`. `moves` is not on the explicit deny-list. However, as a transitive verb applied to possessions (household goods), the semantic is displacement/clearing, which is observable physical action. The concern is whether `moves` is sufficiently concrete: it encodes no specific manner of action (carries, drags, stacks, throws) and could mask a stative displacement rather than a discrete act. The schema prefers verbs that encode the specific physical act over generic motion verbs.
- **why:** Generic `moves` reduces specificity available to the stitcher. Not a clear fault but weakens the bone's action signal. Downstream: the facet pass has less grip on what the physical event was.
- **criteria:** N/A (flag only). Screen-writer may consider recasting to a more specific transitive act (`clears`, `removes`, `carries`).
- **scope:** episode — single bone.
- **route:** screen-writer optional.

---

### flag-004

- **id:** flag-004
- **type:** flag
- **bone:** all active bones (season aggregate)
- **drift-pattern:** `holds` — 13 total instances across season bones. 12 licensed (body-part stillness: `holds the chin` ×1, `holds the eyes` ×5, `holds the feet` ×6) + 1 faulted (bone 166: `holds the step`). The licensed instances are all body-part stillness-against-pressure per narrow license. However, 12 licensed instances across ~480 active bones makes `holds` the dominant stasis-encoding verb in the file. The schema explicitly calls this class of verb "borderline state-verb" (svo-split-notes.md note #2). At 12 licensed instances + 1 fault, the pattern is above the 5-instance drift-pattern threshold and warrants season-scope systematic review.
- **what:** `holds` is the most-used stasis idiom by count. Its licensed uses are individually clean; collectively, the pattern reveals screen-writer reliance on the `holds <body-part>` construction as the primary physical-stasis encoding. Alternative physical stasis verbs (`stills`, `stops`, `freezes`, `braces`) are used less frequently.
- **why:** Idiom fatigue at stitching time. When 12 bones all encode stasis via the same verb-object pattern, the stitcher's rendered output will repeat the same prose shape. Not a schema fault; a quality signal.
- **criteria:** N/A (flag). Screen-writer to review: at minimum 25% of `holds <body-part>` instances should be recoded to alternative stasis verbs or given facet-level differentiation. No mandatory recast, but systematic awareness required.
- **scope:** season-scope pattern review.
- **route:** screen-writer.

---

### flag-005

- **id:** flag-005
- **type:** flag
- **bone:** 14, 170, 171, 496, 504
- **drift-pattern:** `stills` — 5 instances. Bones: 14 (`oc-tanner-father stills`), 170 (`oc-tanner-father stills`), 171 (`oc-tanner-mother stills`), 496 (`taylor-hebert-flea-bottom stills`), 504 (`taylor-hebert-flea-bottom stills`).
- **what:** `stills` is an intransitive verb encoding onset-of-stillness. It is not on the explicit deny-list. However, it sits at the boundary between discrete-act ("became still") and state-onset ("is now still"). At exactly 5 instances, it hits the drift-pattern threshold. As a borderline state-onset verb, its accumulation warrants review. Also note: if bone 166's `holds the step` is recast (as required by fault-001), `stills` is the natural replacement — which would increase its instance count to 6.
- **why:** Pattern coherence. Five instances of `stills` is not individually a problem; collectively, it signals a recurring stasis-encoding device that may be overused or may absorb the fault-001 replacement and grow further.
- **criteria:** N/A (flag). Screen-writer to monitor; if fault-001 recast uses `stills`, review whether the 6-instance total warrants distributing to other verbs.
- **scope:** season-scope.
- **route:** screen-writer awareness.

---

### flag-006

- **id:** flag-006
- **type:** flag
- **bone:** N/A (file-level structure)
- **what:** `s01.bones.md` is filed as the season aggregate working artifact. Per `schemas/proto-line.schema.md`, the aggregate format requires internal sections delimited by `# === episode: <slug> ===` lines, each immediately followed by `narrator:` and `goal:` headers. The file contains neither section delimiters nor any `narrator:`/`goal:` header. The file header is a comment block (`# Season Bones — s01`, schema ref, numbering notes). No episode-scope headers exist.
- **why:** The schema's aggregate format spec is not satisfied. Downstream: Pass 5 continuity (narrator-consistency) and the per-episode extended header generation at Phase 4 Step 3.2 depend on `narrator:` fields being resolvable per episode section. Their absence means either (a) the file is being treated as a flat season-level artifact outside the aggregate format (which would require a different schema convention) or (b) the headers were omitted in authoring.
- **criteria:** N/A (flag — structural). If this file is a Phase 2/3 working aggregate, add episode-section delimiters and per-section headers before Phase 4 split. If it is intentionally a flat season-bones format outside the aggregate spec, document the exception in the file header.
- **scope:** season-scope (file structure).
- **route:** showrunner or screen-writer to confirm format intent; fixer to add headers if aggregate format is confirmed.

---

## Verdict

**RULESET-FAIL**

One fault (fault-001: bone 166, FAULT-FORM-NON-ACTION-VERB, `holds the step`) triggers RULESET-FAIL. Five flags (flag-001 through flag-006) do not individually trigger fail but require screen-writer review before Phase 4 split.

### Fault routing summary

| id | type | bone(s) | route | action required |
|---|---|---|---|---|
| fault-001 | fault | 166 | fixer | Recast `oc-tanner-father holds the step` to licensed stasis verb |
| flag-001 | flag | 318 | screen-writer | Confirm `sits` is discrete act; recast if stative |
| flag-002 | flag | 226, 274, 355, 449 | screen-writer | Rule on `the headache` as subject; recast to `wakes` + feel-facet if interiority-as-subject |
| flag-003 | flag | 235 | screen-writer optional | Consider recasting `moves` to more specific transitive verb |
| flag-004 | flag | season-wide | screen-writer | Systematic review of `holds <body-part>` pattern density |
| flag-005 | flag | 14, 170, 171, 496, 504 | screen-writer | Monitor `stills` count post fault-001 recast |
| flag-006 | flag | file-level | showrunner/screen-writer | Confirm aggregate format; add section headers or document exception |
