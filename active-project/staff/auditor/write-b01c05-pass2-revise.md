audit:
  scope: bone
  target: b01c05-revise-fromsignals-5bones
  timestamp: 2026-05-28
  findings:

    - id: fault-001
      type: pass
      what: A1 — "the insect-feed returns the courier-entry" (slug b01c05s02n01a)
      why: >
        Subject form licensed: apparatus-as-subject in `the <noun>` form, consistent with
        @3 "the insect-feed fills the rushwick junction" and @13 "the side-alley returns the
        sound" (same apparatus-returns-object pattern). Verb "returns" is concrete mechanical
        action. Object "the courier-entry" is a concrete named record, not an abstraction.
        No copula, negation, conjunction, modifier, perception verb, or interiority.
        substance_delta: axis_moves: [] with cost_ledger_anchor: cl-d05. cl-d05 confirmed
        present in series.substance.cost_ledger (memory.md line 1362; gain:
        political_register-prot +3). Chatter bone form is valid.
      criteria: null

    - id: fault-002
      type: pass
      what: B1 — "the courier raises the spine" (slug b01c05s02n03a)
      why: >
        Subject "the courier" is unnamed character in `the <noun>` form; valid per schema.
        Verb "raises" is a concrete physical action (observable posture-act). Object "the
        spine" is a body part of the subject — a direct-object concrete noun, not an
        abstraction. "Raises the spine" reads as a visible postural recovery event, not as
        interiority or a thought-figure. Schema narrow license for body-part objects (parallel
        to "taylor holds the feet") is consistent. No copula, negation, conjunction, modifier,
        perception verb, or interiority.
        substance_delta: axes_held form with moral_framework and licensed-exception rationale.
        No axis_moves declared; no cost_ledger_anchor required under the axes_held hold form.
        No FAULT-BONE-DELTA-MALFORMED condition triggered.
      criteria: null

    - id: fault-003
      type: pass
      what: B2 — "the enforcement-report enters the jarvis-channel" (slug b01c05s02n06a)
      why: >
        Subject "the enforcement-report" is a named document (prop-class entity). Schema
        licenses prop slugs as subjects. "The enforcement-report" is prop-adjacent and
        consistent with named-document subjects in apparatus bones. Verb "enters" is a
        concrete motion verb. Object "the jarvis-channel" is a named routing channel —
        concrete noun. No prepositional tail. No copula, negation, conjunction, modifier,
        perception verb, or interiority.
        substance_delta: axes_held form with moral_framework rationale. Hold form valid; no
        FAULT-BONE-DELTA-MALFORMED.
      criteria: null

    - id: fault-004
      type: flag
      what: B3 — "taylor-hebert-kl-122ac adds the jarvis-form to the sera-arrangement-file" (slug b01c05s02n06b); specifically the prepositional tail "to the sera-arrangement-file"
      why: >
        Schema (bones.schema.md § harsh-SVO rules) explicitly bans prepositional phrases of
        destination: "Prepositional phrases of place / destination / source / direction /
        instrument / accompaniment are explicitly banned (FAULT-FORM-MODIFIER)." The phrase
        "to the sera-arrangement-file" is a prepositional phrase of destination.

        B3 is structurally identical to @18 in the existing bones file: "taylor-hebert-kl-122ac
        adds the courier to the body-map." @18 passed the prior Phase 2 audit per the
        dispatch brief. If @18's pass was correct, B3 passes on identical form and this flag
        requires no fix. If @18's pass was an oversight, both @18 and B3 carry the same
        latent FAULT-FORM-MODIFIER and both would require remediation.

        Auditor cannot re-litigate @18 at this phase (Phase 2 scope is the 5 new bones only;
        @18 is a pre-passed bone). Recording as a flag, not a fault, because the precedent is
        established in the live bones file and fixer would need to address @18 alongside B3
        for any fix to be consistent.

        substance_delta: axes_held form with moral_framework rationale. Hold form valid; no
        FAULT-BONE-DELTA-MALFORMED.
      criteria: null

    - id: fault-005
      type: pass
      what: C1 — "the rushwick-feed resists the flat-read" (slug b01c05s03n06a)
      why: >
        Subject "the rushwick-feed" is an established apparatus element in `the <noun>` form,
        with direct precedent in @23 "taylor-hebert-kl-122ac runs the rushwick-feed" naming
        the feed as a concrete system. Apparatus-as-subject licensed by @3 and @22 (same
        feed-apparatus class). Verb "resists" describes a discrete mechanical event (feed
        failing to complete the process); it is an observable outcome, not stative position,
        not possession, not interiority. Parallel form to @22 "the Hook-feed resolves" (feed
        completing a process) — "resists" is the mechanical inverse and of the same action
        class. Object "the flat-read" is a named procedure — concrete noun.
        No copula, negation, conjunction, modifier, perception verb, or interiority.
        substance_delta: axis_moves: [] with cost_ledger_anchor: cl-d05. cl-d05 confirmed
        present in series.substance.cost_ledger. Chatter bone form is valid. Orchestrator
        re-classification from "partial" to chatter+cl-d05 is reflected correctly; no
        magnitude field present that would trigger DEC-0040 floor violation.
      criteria: null

  summary: >
    ACCEPT WITH FLAG.

    4 of 5 bones: PASS — no faults.
    1 of 5 bones: FLAG (fault-004, B3) — prepositional-tail "to the sera-arrangement-file"
    is schema-banned (FAULT-FORM-MODIFIER class) but is structurally identical to @18, which
    passed the prior Phase 2 audit. Flag is informational; it does not block Phase 3 or
    subsequent phases. No fixer dispatch warranted unless @18 is also being remediated.

    No FAULT-BONE-DELTA-MALFORMED findings. No FAULT-COST-LEDGER-UNRESOLVED findings (cl-d05
    confirmed present). No FAULT-FORM-COPULA, FAULT-FORM-NEGATION, FAULT-FORM-CONJUNCTION,
    FAULT-FORM-PERCEPTION, FAULT-FORM-INTERIORITY, or FAULT-FORM-NON-ACTION-VERB findings.

    The 5 new bones are cleared to proceed to Phase 3 (shape) and Phase 6 (substance
    bone-gate).
