audit:
  scope: episode
  target: chapter-02
  timestamp: 2026-05-07
  findings:

    - id: fault-001
      type: fault
      what: chapter-02.md line 58 — "a girl appears the mill hamlet road edge"
      why: "appears" is an existential/observational verb, not a physical action verb. The FAULT-FORM-NON-ACTION-VERB class requires every numbered line to carry a physical action verb. The girl is introduced through the narrator's perception rather than through a physical action she performs. This breaks the chapter format's action-verb contract, which ch01 maintains throughout.
      criteria: line 58 must use a physical action verb that names what the girl does at the mill hamlet road edge — an arrival, movement, or physical behavior she performs — not a verb that names the narrator's perceptual event of her becoming visible.

    - id: fault-002
      type: fault
      what: chapter-02.md line 31 — "the headache starts"
      why: "starts" is a state-onset verb, not a physical action verb. No actor is performing an action; a physiological condition is initializing. FAULT-FORM-NON-ACTION-VERB applies. The physical cost of fauna control is correctly present in the chapter — the fault is in the verb form, not the content.
      criteria: line 31 must use a physical action verb that names a concrete physical event marking the headache onset — what Taylor's body does, not what the condition does.

    - id: fault-003
      type: fault
      what: chapter-02.md line 52 — "the nosebleed starts"
      why: Same class as fault-002. "starts" names state onset, not actor action. Identical FAULT-FORM-NON-ACTION-VERB violation.
      criteria: line 52 must use a physical action verb that names a concrete physical event marking the nosebleed onset — what Taylor's body does, not what the condition does.

    - id: fault-004
      type: fault
      what: chapter-02.md — actor naming throughout (e.g., lines 4, 5, 8, 17, 23, 29, 30, 39, 41, 51, 53, 54, 65, 66, 67, 68, 80, 81, 83, 84, 86, 96, 97, 100)
      why: ch02 uses "Taylor" (first-name only) for the protagonist. ch01 uses the full slug form "taylor-hebert-westeros" throughout. The chapter format requires consistent slug-form actor identifiers. "Taylor" is not a slug; it is a display name. The inconsistency creates a format fault and breaks slug-based lookup that downstream pipeline stages depend on.
      criteria: all references to the protagonist must use the slug "taylor-hebert-westeros" in place of "Taylor" — matching the naming discipline established in chapter-01 and required by the chapter format.

    - id: pass-001
      type: pass
      what: constraints — cond-fauna-control-rules
      why: Physical cost curve is present and escalating: headache (line 31), nosebleed (line 52), nose-bridge pinch and head tilt (lines 53–54). Fauna types used — raven, fly, rat, passive multi-species feed — are within the defined capability set (insects, rats, ravens, non-complex fauna). No violation of the cost-curves-are-mandatory rule.

    - id: pass-002
      type: pass
      what: constraints — cond-series-tone-constraints
      why: Chapter is action-line-only; no introspection, no dialogue, no internal register lines. Satisfies the fast/pulpy/action-register constraint throughout.

    - id: pass-003
      type: pass
      what: constraints — cond-riverlands-120ac-state
      why: Setting elements (Harrenhal, postern gate, garrison hall, mill hamlet road, farmsteads, grain shed, orchard) are consistent with the 120 AC Riverlands environment. No anachronism or setting violation found.

    - id: pass-004
      type: pass
      what: plan goal vs chapter header goal
      why: Exact match between chapter-02-plan.md goal field and chapter-02.md goal field.

    - id: pass-005
      type: pass
      what: chapter-02-plan change statement vs delivered chapter end-state
      why: Plan change: "End: Plumm's man has a written observation log naming three anomaly sites and a recurring figure; the pattern is on paper before Taylor knows it is being traced." Chapter delivers five transcribed entries (lines 88–93), Taylor releases fauna and exits the scene without awareness of the ledger (lines 96–101). Change is fully delivered.

    - id: pass-006
      type: pass
      what: narrator field — chapter-02.md line 1
      why: "narrator: taylor-hebert-westeros" matches chapter-02-plan.md narrator field exactly.

# summary
# Four faults. Three are FAULT-FORM-NON-ACTION-VERB class: line 58 ("appears"), line 31 ("starts"), line 52 ("starts"). One is a format fault: protagonist named as "Taylor" throughout instead of slug "taylor-hebert-westeros." No constraint violations found. Physical cost curve present and escalating. Plan change delivered in full.
