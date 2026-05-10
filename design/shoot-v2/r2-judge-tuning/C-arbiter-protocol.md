---
phase: C — arbiter protocol
project: R2 hybrid judge tuning
date: 2026-05-10
status: ACTIVE — applies during Phases D (audience attack), E (R2 self-review), F (validation re-run)
parent: design/shoot-v2/r2-judge-tuning/B-locked-rubric.md
---

# Phase C — Arbiter Protocol

## Role

The **arbiter** is the main-session orchestrator (the model holding the conversation context, not a subagent). The arbiter's job during R2 tuning is to ensure reviewers — both R2 layer authors and audience personas reviewing R2 output — produce **taste-justifications** rather than mechanical pattern-matching against rubrics.

This protocol exists because the four failure modes in `A-corpus.md` (F-R2-1 through F-R2-4) are not fundamentally rubric-content gaps. They are **discipline gaps**: reviewers who hold a rubric as a checklist will pattern-match to that checklist, miss what the entry actually does, and produce verdicts that look defensible on paper but fail audience adjudication later. The fix is the reviewer holding themselves to taste-argument; the arbiter is the second-line check that the holding is real.

## What "taste-justification" means here

A taste-justification:

1. **Names something specific to the entry under review** — a phrase, a register-shift, a moment, a construction. Not the rubric's anti-pattern label, not a category name.
2. **Articulates what the entry does or doesn't do** — what it's reaching for, what it's actually producing, where the gap is. In the reviewer's voice.
3. **Carries a remediation argument when the verdict is negative** — "I'd cut," "I'd revise toward X," "I'd keep but flag this concern." Not just "FAIL."
4. **Is testable by a reader who has the entry but not the rubric** — another reader could read the justification and the entry, and see the argument.

Mechanical pattern-matching:

1. **Cites rubric labels** — "AP6 violation," "Q2 FAIL," "tens=3 with no memory" — without naming what specifically in the entry produces the violation.
2. **Treats the rubric as a list to satisfy** — entries pass when they tick off the right boxes, not when they earn their place.
3. **Produces verdicts indistinguishable from a different entry with the same checkboxes** — a sign the verdict is reading checkboxes, not the entry.

## Arbiter intervention triggers

The arbiter intervenes when a reviewer (R2 layer author or audience persona) produces a verdict that:

### Trigger T1 — Rubric-label-heavy, entry-specific-light

Verdict justification consists primarily of rubric citations (AP labels, Q gates, named anti-patterns) without naming concrete content from the entry. **Intervention:** the arbiter responds to the reviewer with a clarifying request: *"What specifically in this entry produced that verdict? Quote the phrase or describe the construction in your own words."*

### Trigger T2 — Pattern-flag without remediation

Reviewer flags a pattern (cross-character same-strategy, formula-repetition) by counting instances against a threshold, without saying what should change. **Intervention:** *"You named the pattern. What would you do about it? Which instances would you cut, revise, or keep, and on what grounds?"*

### Trigger T3 — Verdict that could have been written without reading the entry

If the reviewer's justification could plausibly be produced by reading only the rubric and the entry's metadata (facet, anchor, ID), without reading the entry's content — the verdict is mechanical. **Intervention:** *"Tell me what the entry says, in your own words, before telling me whether it works."*

### Trigger T4 — Niche-driven add justification

R2-add justification works backward from "the graph reveals a niche" rather than forward from "the at-rest reading wants this entry." **Intervention:** *"Set aside the cite-index for a moment. Read the proto-line. Does it want this entry? Why?"*

### Trigger T5 — Adjacent-context dependency

Verdict on a lonely entry that, when articulated, only makes sense if the next or prior proto-line is present. **Intervention:** *"Cover the surrounding proto-lines. Does your verdict still hold? Restate it without referring to what comes next."*

### Trigger T6 — Defense by recitation

When R2 receives a Phase-D audience seam and produces a defense that recites the rubric license rather than answering the seam's actual concern. **Intervention:** *"The seam isn't asking whether the rubric licenses the entry. It's asking whether the entry earns its license. Answer the seam, not the rubric."*

## Arbiter discipline (limits on the arbiter)

The arbiter is **not** a content reviewer. The arbiter:

- Does not produce verdicts on entries.
- Does not adjudicate seams.
- Does not author or revise facet entries.
- Does not score reviewers.

The arbiter's only product is **process intervention**: when a verdict is mechanical, request a justification rewrite; when a justification is mechanical, request a re-read. The arbiter trusts the reviewer's taste once the discipline holds; the arbiter does not impose taste of its own.

The arbiter is also bounded:

- **Two intervention rounds per verdict, maximum.** If a reviewer cannot produce a non-mechanical justification after two interventions, the verdict is logged as **DISCIPLINE-FAIL** and surfaced for the next session's adjudication. The arbiter does not override; it surfaces.
- **No interventions on hard-fence violations.** If R2 refuses an entry on POV-perceptual-access or hard-fence vocabulary grounds, the refusal is mechanical by design and is not an intervention target.
- **No interventions on schema/citation work.** Cascade strips, add-writes, cite-index rebuilds — all mechanical. Not arbiter scope.

## Logging

Arbiter interventions are logged inline in the reviewer's decision log:

```
- <facet>:<id> @<proto-line>: KEEP
  Justification: <reviewer's first attempt — mechanical>
  [ARBITER T1: requested entry-specific articulation]
  Justification (revised): <reviewer's second attempt — taste-driven>

- <facet>:<id> @<proto-line>: DELETE
  Justification: <reviewer's attempt>
  [ARBITER T3: could-have-been-written-without-reading]
  Justification (revised): <reviewer's revision>
  [ARBITER T3 again]
  DISCIPLINE-FAIL — surfaced for adjudication
```

Per-session arbiter summary at the close:

```
## Arbiter Summary
- Total verdicts reviewed: <n>
- Interventions fired: <n> across <n> verdicts (<percentage>)
- Most-common trigger: <T1-T6>
- DISCIPLINE-FAIL count: <n>
- Pattern: <one paragraph in arbiter voice — what the reviewer is systematically slipping toward and what's earning clean justifications>
```

## When the arbiter is the main session vs a subagent

This protocol is written for the **main session** as arbiter — the model in the user-facing conversation, holding the showrunner-context. In dispatch-heavy phases (D, E, F), the arbiter still runs as main session: each subagent dispatch returns its decision log; the main session reads the log, fires intervention triggers as needed, and re-dispatches the subagent with the intervention request as additional brief content.

This means the arbiter's work happens in **between** subagent dispatches, not inside them. The subagent doesn't know it's being arbited — it receives a fresh prompt with the intervention question in the brief and responds. The decision log accumulates across dispatches.

Subagent budget implication: each intervention is +1 dispatch. With T1–T6 triggers calibrated to fire on ~20–30% of verdicts (estimate from memory + feeling tuning), expect total dispatch count to inflate by 20–30% over the un-arbited budget. This is real cost and is acknowledged in the runtime budget for Phase F validation.

## Success criteria

The arbiter protocol is working when:

- Reviewers' first-pass justifications increasingly avoid rubric-label-heavy framing without prompting (the discipline becomes self-sustaining).
- Audience adjudication at Phase F finds fewer "verdict was technically correct but the reasoning didn't hold" cases.
- Arbiter intervention rate decreases across the run — early sessions fire 30%+ interventions; late sessions fire <10%. If the rate is flat or rising, the protocol or the rubric is mis-tuned.
- The arbiter produces no false-intervention complaints from reviewers ("you're asking me to restate what I already said"). When reviewers feel the intervention is justified — not pedantic — the discipline is calibrated.

## Limits this protocol acknowledges

- **Taste is not auditable in the same way as mechanics are.** The arbiter cannot prove a justification is mechanical; it can only flag verdicts that read mechanical and ask for a re-do. False-positive interventions are possible.
- **Reviewers who pattern-match well can produce justifications that look taste-driven but aren't.** The arbiter is a second-line check, not infallible. Audience adjudication at Phase F is the third line.
- **The arbiter does not scale linearly.** A single human (or single model context) arbiting hundreds of verdicts loses calibration. For corpus larger than ~50 verdicts per session, the arbiter samples (every Nth verdict + all DISCIPLINE-FAILs) rather than running every verdict.
