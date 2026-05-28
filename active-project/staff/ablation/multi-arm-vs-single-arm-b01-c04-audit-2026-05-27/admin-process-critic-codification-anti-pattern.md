# Admin process-critic verdict — codification anti-pattern
## Dispatch: 2026-05-28 | DEC-0038 | PROCESS-CHANGE-PROPOSED PROP-0017

---

## Verdict

```
verdict: PROCESS-CHANGE-PROPOSED
proposal_id: PROP-0017
summary: Structural trigger-surface gap — process-critic fires on chain-command non-PASS verdicts
         but has no trigger covering URI default-change spec edits that cite experiment conclusions;
         add new trigger class to CLAUDE.md Rule 13.
dec-id: DEC-0038
```

---

## Rationale

### Is this one-occurrence-disposable or recurring-class-warranting-structural-fix?

Recurring class warranting structural fix — but not because of prior recurrences (this is the
first traced occurrence of this exact pattern). The exception to the standard two-occurrence
recurrence threshold applies here for the same reason it applied to PROP-0009/0010/0011: the
failure mode is deterministic-structural, not probabilistic.

The standard first-occurrence hold applies to probabilistic coincidences (two authoring decisions
that happen to align, per DEC-0032 Pattern A). It does NOT apply when the gap is:
- A structural property of the trigger surface (no trigger exists for this class of authoring activity)
- Predictably recurrent on every future experiment that surfaces a tuning-candidates list in the same session
- Already demonstrated as non-trivially costly to remediate

This is all three. The 12-minute gap between experiment-conclusion and contradictory-codification
is not an anomalous rush — it is normal in-session pacing. The same pattern will fire on the next
experiment that surfaces A-E candidates. Holding for recurrence means the pattern fires again
before the trigger is added.

### The structural gap

The process-critic trigger surface (CLAUDE.md Rule 13 tail-step hooks) covers chain-command
non-PASS verdicts: /and-write Phase 6.5, /and-facets Phase 5c, /and-stitch Phase 9.5, /and-postop
Phase 3.5, /and-review Common-Phase 4.5. These fire on *output quality failures* — the chapter
was not good enough.

A URI default-change spec edit is a *pipeline-authoring activity*, not a chapter-authoring output.
The chain-command trigger surface has no reach over it. When a session runs an experiment, concludes
with a tuning-candidates list, and 12 minutes later codifies option D as default-on, there is no
gate between those two events. The process-critic exists to read experiments critically and check
that codifications accurately represent conclusions — but it was never told to fire here.

The audit traced the specific failure shape:
- Experiment concluded: CONTINUE=no. Cost-legibility lives in bones SVO authoring, not stitch
  paragraph composition. Per-paragraph craft optimization is not predictive of continue-rate.
- Codification framed: "cherry-pick path captures paragraph-level lift the pure-winner cannot...
  making paragraph the strictly-better default."
- The codification cited per-paragraph craft improvements (which the experiment said were not
  predictive) as positive evidence, and wrote "strictly-better default" without addressing the
  experiment's actual CONTINUE=no finding.

This is not a content failure (the chapter was wrong). It is a pipeline-authoring failure (the spec
was not authored faithfully to its evidence base). The process-critic's content-vs-process
discrimination points at a new trigger class, not a modification of an existing gate.

### Why not wait for recurrence?

Three reasons:

1. **The gap is structural.** Every future experiment that surfaces a tuning-candidates list in
   the same session will have the same gap. The pattern is not "this session was careless" — it
   is "sessions in this state have structural confirmation-bias pressure and no independent
   reviewer." The fix is independent of how careful future sessions are.

2. **The remediation cost signal is clear.** The wasted spend (multi-arm b01-c04 production run,
   tournament, cherry-pick, comparative scoring, multi-judge verification audit, principal-surfacing
   effort) is the cost of one missed gate firing. At the project's current dispatch rate, one
   missed gate firing is a significant fraction of a chapter's total chain spend. A S-cost gate
   addition prevents that cost class permanently.

3. **The fix is precisely discriminable at one occurrence.** The trigger condition is enumerable:
   (a) URI default-change + (b) experiment citation as primary justification. Both conditions are
   checkable at commit time. The proposed dispatch payload (experiment_conclusion_verbatim +
   proposed_spec_text + gate_path) gives process-critic everything it needs to do the comparison.
   There is no ambiguity about whether the gate is correctly targeted — the incident names the
   exact shape.

### Proposed change

Target: CLAUDE.md Rule 13, process-critic mode trigger enumeration.
Change_type: add (new trigger class).
Cost: S (one clause addition to one rule; no command-body, rubric, or schema changes).

The new trigger fires when both hold:
  (a) The spec edit changes a flag default from off → on, or enables a new pipeline feature as default.
  (b) The spec edit directly cites a session-run experiment's conclusion as primary justification.

When both hold: dispatch process-critic before committing, passing the experiment's verbatim
conclusion + the proposed spec text + the gate_path. Process-critic checks whether the spec text
accurately represents the conclusion, including any negative-result language. Returns OK if
faithful; REVISE if misrepresented. No commit until OK or PROCESS-CHANGE-PROPOSED is returned.

Derivative defaults (a URI built on another URI, as happened with URI-STITCH-MULTI-ARM-DEFAULT-ON
depending on URI-STITCH-CHERRY-PICK-DEFAULT-ON) are not exempt — each must be dispatched on its
own evidence.

### What the process-critic does NOT propose

The audit finding, remediation, and multi-judge verification are all complete. The spec state is
correct (both URIs reverted; default-off restored; audit note appended). Admin does not propose
changes to the command body beyond what the remediation already applied. The b01-c04 canonical
draft is restored. The only open process gap is the trigger-surface gap addressed by PROP-0017.

---

## Filed artifacts

- `staff/admin/process-proposals.md` — PROP-0017 appended
- `staff/admin/decisions.md` — DEC-0038 appended
- `staff/admin/stm.md` — updated
