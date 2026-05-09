# Audit Report — Season s01 Aggregate — Pass S3.5 Ruleset Compliance
# schema: schemas/audit-report.schema.md
# generated: 2026-05-09
# target: active-project/theater/proto-lines/s01.aggregate.md
# scope: mechanic-strictness re-check (season-wide pattern detection)

---

## File-level verdict: RULESET-FAIL

---

## Findings

---

### fault-001
- **type:** fault
- **what:** `holds the breath` — 5 occurrences. Proto-line IDs: 75, 172, 203, 261, 778. All authored as `taylor-hebert-jaehaerys holds the breath`.
- **why:** The `holds` narrow license requires "the object is a body part of the subject and the action is stillness-against-pressure." `breath` is a physiological process, not an anatomical body part. The licensed forms (`holds the feet`, `holds the eyes`, `holds the chin`, `holds the head`, `holds the face`, `holds the mouth`, `holds the shoulder`) are all named anatomical structures. `breath` is not. The svo-split-notes establish the license specifically against posture/position holds under pressure; breath-holding is voluntary respiratory arrest, not a posture-against-pressure. Five occurrences across the season constitute a drift pattern: the form recurs wherever taylor requires a beat of internal suspension before speech or action, and each time bypasses the pressure-posture logic the license was written to permit. Downstream consequence: the stitcher will render `holds the breath` as a physical bone and the facet author will have no clean proto-line to anchor a feel/narrator facet that actually carries the interiority. The beat is needed; the form is wrong.
- **criteria:** Recast each of the 5 occurrences as either (a) the observable physical act that accompanies breath-holding (e.g., `taylor-hebert-jaehaerys stills`, `taylor-hebert-jaehaerys tightens the jaw`, `taylor-hebert-jaehaerys presses the lips`) paired with the existing exhale beat (IDs 76, 505 etc.) where present; or (b) delete and route the interiority to a feel facet citing the surrounding proto-lines. If the physical stillness is load-bearing as a bone, option (a) is preferred.

---

### fault-002
- **type:** fault
- **what:** ID 916: `the fly settles at the mordant-beam joint`
- **why:** `the fly settles` is a complete intransitive SVO. `at the mordant-beam joint` is a prepositional phrase of place appended after a complete verb, which is explicitly banned (FAULT-FORM-MODIFIER). The schema states: "Never append a location, time, or instrument prepositional phrase to a complete SVO." Compare the surrounding licensed form: ID 27 `a fly touches the ink-pot rim` (transitive verb + direct object) and ID 904 `the sept fly orbits the baptismal basin rim` (transitive verb + direct object). The insert at ID 916 used the intransitive `settles` with a place-prep tail instead of a transitive motion verb.
- **criteria:** Recast to a transitive form that takes the location as direct object: `the fly settles the mordant-beam joint` is not English; preferred recast: `the fly lands the mordant-beam joint` (if `lands` takes the surface) or `the fly reaches the mordant-beam joint` (standard motion-verb direct-object form consistent with this aggregate's existing pattern). Alternatively: `the fly touches the mordant-beam joint` (consistent with ID 27's form). Delete the prepositional `at`.

---

### flag-001
- **type:** flag
- **what:** `traces` — 6 occurrences as physical reading-by-finger verb. IDs: 25 (`traces the column`), 188 (`traces the line`), 250 (`traces the column`), 683 (`traces the entry`), 843 (`traces the ledger entry`), 872 (`traces the literacy register`).
- **why:** `traces` is not on the explicit perception-verb deny-list (`read`, `took`, `tracked`, `noted`, `counted`, `measured`, `watches`, `sees`, `hears`, `notices`). However, all 6 uses apply `traces` to written text columns, document entries, or registers — making it functionally equivalent to `reads` in context (a character runs a finger along text to read it). `reads` is explicitly banned as a perception verb. Season-wide, this form appears 6 times and in each case the downstream meaning is "character reads by tracing a finger." The perception content belongs in narrator/feel facets; the proto-line should record only the physical contact event. At 6 occurrences across the season this is a pattern, not an isolated call. Partial drift: the physical contact (finger on surface) is real and observable; the perception implication is the contamination.
- **criteria (fixer guidance):** Not a mandatory recast under strict deny-list enforcement. Flag for fixer discretion: if the physical-contact reading is sufficient (finger contacts the surface, perception implied), retain. If the stitcher will render these as "X reads the column" in prose, recast to `presses the column` or `touches the entry` and route the reading-comprehension beat to narrator/feel facets. Systematic recast recommended given 6-instance pattern.

---

### flag-002
- **type:** flag
- **what:** ID 73: `oc-craftsman-father lowers his voice`
- **why:** `voice` is not a concrete physical object — it is a physiological property (volume/pitch of phonation). The schema bans abstraction-as-object: "A physical verb whose object is an abstract noun... is a thought-figure, not an event." `voice` is less abstract than `silence` or `tension` but is not an object that can be physically lowered (no mass, no location). The beat is observable (volume drops), but the form routes through a property-as-object construction. One occurrence; not a season-wide pattern.
- **criteria (fixer guidance):** Recast to a transitive form with a physical object, or use an intransitive: `oc-craftsman-father drops the voice` is no cleaner; preferred: `oc-craftsman-father murmurs` (intransitive, lets the dialogue file carry the content) or split into two beats — the physical act of leaning in / turning away, and then the dialogue beat. One occurrence; low priority.

---

### flag-003
- **type:** flag
- **what:** Possessive-qualified subjects at IDs 285 and 803. ID 285: `the wool-factor's cart rolls`. ID 803: `the maester's horse follows the ferryman's route marker`.
- **why:** The schema's subject rule specifies `the <noun>` as the form for unnamed environment elements. Both uses prepend a possessive qualifier (`the wool-factor's`, `the maester's`) that goes beyond the `the <noun>` template. Two occurrences; not a season-wide pattern. Secondary issue on ID 803: `follows the ferryman's route marker` — `follows` in this context means tracks/navigates-by, which carries a perception-navigation implication (the horse senses and responds to the marker). The verb does not appear on the explicit deny-list, but the navigation-tracking sense overlaps with banned `tracks`. Additionally, `the ferryman's route marker` as object is a possessive-qualified prop with an abstract directional function.
- **criteria (fixer guidance):** For ID 285: `the cart rolls` strips the possessive and is clean if the wool-factor's cart is established in context. For ID 803: `the maester's horse` → `the horse` (strip possessive, context-sufficient); recast verb: `the horse crosses the dock approach` or `the horse follows the column` (if the column is the physical entity being trailed). Strip the route-marker object entirely if it functions as prepositional padding.

---

### flag-004
- **type:** flag
- **what:** ID 841: `the maester draws the ledger query`
- **why:** `ledger query` is a compound noun where `query` is an abstract term (a question/request/enquiry) used to name a document. The schema bans abstraction-as-object. `query` in isolation names a piece of reasoning, not a physical artifact. If `ledger query` is an established prop name in the warehouse, this passes; if it is a descriptive compound coined here, `query` is the abstract component. One occurrence.
- **criteria (fixer guidance):** If a prop card exists for this document, retain. If not: recast object to the physical artifact class — `the maester draws the ledger folio` or `the maester draws the account folio` — per the established `folio` prop pattern used throughout this aggregate (IDs 347, 399, 404, etc.).

---

### flag-005
- **type:** flag
- **what:** ID 906: `the ferry folio crosses the water`
- **why:** The folio is a document (inanimate). Object-as-subject is licensed "when the actor is unknown / ambient / unspecified." At ID 898, the ferryman grips the folio; the causal actor is known. The proto-line renders an inanimate document as the agent of crossing a river — this is narrative shorthand, not a physical event with an observable actor. One occurrence; low priority.
- **criteria (fixer guidance):** Recast to name the known agent: `the ferryman crosses the water` (if the crossing itself is the load-bearing beat) or delete ID 906 entirely if the folio's movement is adequately established by IDs 894–898 and 909. If the image of the document's transit is the point (a shape beat), retain and flag for editor.

---

### flag-006
- **type:** flag
- **what:** ID 918: `taylor-hebert-jaehaerys cradles the head`
- **why:** `cradles` describes sustained gentle holding — it occupies the same functional space as a sustained-carry verb, adjacent to the `holds` deny-list class (which requires the narrow body-part/pressure-resistance license). `cradles the head` implies the head is being cradled (held in a cupped posture), which is sustained rather than a discrete physical act. Under strict analysis, `cradles` is closer to `carries` (sustained carrying posture) than to `holds the feet` (stillness-against-pressure). One occurrence.
- **criteria (fixer guidance):** If the beat is a discrete posture-change act (taking the head in both hands), recast to the act: `taylor-hebert-jaehaerys cups the head` or `taylor-hebert-jaehaerys takes the head in the hands` (split if needed). If it is sustained holding, route to a state-update facet citing the surrounding beats.

---

### flag-007
- **type:** flag
- **what:** Aggregate file-level header does not conform to schema. The schema for season aggregates specifies `# === episode: <slug> ===` section delimiters each immediately followed by `narrator:` and `goal:` headers. This file uses `# pov: <slug>` inline transitions with no `narrator:` or `goal:` fields at file or section level.
- **why:** Per `schemas/proto-line.schema.md`: "Every proto-line file begins with `narrator:` and `goal:` at minimum." The aggregate format further requires `narrator:` and `goal:` per section. Neither the file-level nor the section-level headers are present. This would fault `FAULT-HEADER-NARRATOR` and `FAULT-HEADER-GOAL` at Pass 2. Since Pass 2 ran 6 rounds and converged without raising this, the format may have been accepted as a working variant for the season-aggregate artifact. Noted for Phase 4 split: the per-episode files emitted by Phase 4 will need proper headers.
- **criteria (fixer guidance):** No action required before Phase 4 split if Pass 2 accepted this format. At Phase 4 split, each emitted per-episode file must carry the full extended header per schema.

---

## Drift-pattern report

| Verb / form | Occurrences | Classification | IDs |
|---|---|---|---|
| `holds the breath` | 5 | FAULT (unlicensed `holds` — object is not a body part) | 75, 172, 203, 261, 778 |
| `traces` (on written text) | 6 | FLAG (perception-adjacent; overlaps banned `read`) | 25, 188, 250, 683, 843, 872 |

No other verb reaches 5+ season-wide occurrences as a borderline state-verb. `holds the feet`, `holds the eyes`, `holds the chin`, `holds the face`, `holds the mouth`, `holds the shoulder`, `holds the hands` all appear frequently and are all licensed (anatomical body parts, stillness-against-pressure). Only `holds the breath` fails the license.

---

## Summary

- **Verdict:** RULESET-FAIL
- **Fault count:** 2 (fault-001: `holds the breath` ×5; fault-002: ID 916 FAULT-FORM-MODIFIER)
- **Flag count:** 7 (flag-001 through flag-007)
- **Drift patterns requiring systematic recast:** 1 mandatory (`holds the breath`, 5 instances — unlicensed `holds`); 1 recommended (`traces` on text, 6 instances — perception-adjacent)
- **Routing recommendation:** Route to fixer for fault-001 (5 targeted recasts) and fault-002 (1 line recast). Flag-001 (`traces`) is a fixer-discretion call — recommend systematic recast if the stitcher will render these as reading beats. Flags 002–007 are single-instance low-priority; batch with fault fixes if fixer is dispatched, or defer to Phase 4 editor. No escalation required; all findings are episode-scope or line-scope. No season-plan or series-plan change is implied.
