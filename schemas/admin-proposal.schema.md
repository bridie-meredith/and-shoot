# Admin process-change proposal schema

Process-change proposals authored by the `admin` agent in **process-critic mode**. Admin reads a non-PASS verdict report (or a postop convergence) plus the upstream gate that produced it, judges whether the *process itself* needs to change, and appends a proposal to the log.

**File location.** `staff/admin/process-proposals.md` (project-wide; not active-project-scoped — process changes outlive any single project). Append-only. Triage stamps add fields rather than delete entries.

**Lifecycle.**
1. Admin (in process-critic mode) appends an entry with `status: open`.
2. The principal triages: accepts → entry stamped `accepted` + `pr_ref` once implemented; rejects → entry stamped `rejected` + `rejection_note`; defers → entry stamped `deferred` + `defer_until`.
3. Rejected entries stay on disk so admin does not re-propose the same change. Admin scans the log before authoring a new proposal and aborts proposal authoring (returning `OK-PRIOR-REJECTION`) if a materially-same proposal is already `rejected`.

---

## Format

One entry per `## PROP-<NNNN>` heading, monotonic. YAML body inside the heading.

```yaml
id: PROP-<NNNN>                          # monotonic; allocate by reading tail of file
created_at: <ISO timestamp>
created_by: admin process-critic         # always; admin is sole author
trigger:
  reason: failure | postop                # which auto-fire path invoked admin
  source_report: <path>                   # the report that triggered the proposal
  source_verdict: <verdict-string>        # e.g. FAIL, REVISE, PASS-WITH-DEPTH-PASS-REQUIRED, postop-convergence
target:
  type: command | rubric | schema | agent-card
  path: <path>                            # file the proposed change would edit
  section: <heading-or-anchor> | null     # specific section if scoped
change_type: delete | modify | add | promote
  # delete  — gate or check should be removed (false-positive-heavy, redundant with another gate, costing more than it catches)
  # modify  — existing gate's criteria/threshold/disposition needs change
  # add     — new gate or check needed (slipped through with no owning gate)
  # promote — taste flag should become mechanical check (Rule 11 promotion path)
rationale: |
  <one paragraph; why goals + methodology say this process needs to change.
   Must cite the evidence, not just assert the conclusion.>
evidence_refs:
  - <report path + finding-id or line>
  - <prior occurrence path if recurrence-based>
  - <command-body or rubric path that owns the gate>
recurrence_count: <integer>               # how many times the same gap has been seen across staff/reviews/; 1 = first occurrence
proposed_diff: |
  <prose sketch of the change. NOT a literal patch — implementation is the principal's call.
   Naming the section + the operation + the load-bearing sentence is enough.>
cost_estimate: <S | M | L>                # rough implementation cost (S = ≤1 file, M = command + schema, L = multi-file + downstream cascade)
status: open | accepted | rejected | deferred | superseded
# Triage stamps (added by principal or principal's delegate; admin never edits these on own initiative):
triaged_at: <ISO timestamp> | null
triaged_by: <human | session-id> | null
disposition_note: <one line> | null       # required when rejecting or deferring; optional on accept
pr_ref: <PR number or branch> | null      # set when accepted + implemented
defer_until: <date or condition> | null   # set when deferred
supersedes: PROP-<NNNN> | null            # set when this proposal replaces an earlier one
```

---

## Field semantics

**`id`** — `PROP-<NNNN>` monotonic. Allocate by reading the file tail. Stable forever; never reused.

**`trigger.reason`** — `failure` (auto-fired on FAIL/REVISE/PASS-WITH-DEPTH-PASS-REQUIRED from `/and-review`, `/and-write` bone-gate, the `/and-facets` Phase 5 orchestrator-critic verdict — the Phase 5b audience-gate trigger is retired under DEC-0116, `/and-stitch` Phase 9) or `postop` (auto-fired after `/and-postop` convergence write). On-demand invocation (future `/and-review process`) uses `reason: on-demand`.

**`target.type`** —
- `command` — change a command body in `.claude/commands/`.
- `rubric` — change a facet rubric or auditor class-library entry.
- `schema` — change a schema in `schemas/`.
- `agent-card` — change an agent definition in `.claude/agents/` or a staff agent card.

**`change_type`** — one of four shapes:
- **`delete`** — the gate fires too often without catching anything, or another gate has subsumed it. Rationale must name what makes it net-negative.
- **`modify`** — threshold, disposition (HARD vs SIGNAL), or criteria of an existing check need adjustment.
- **`add`** — a failure slipped through with no owning gate; a new check is needed somewhere upstream.
- **`promote`** — a taste flag from audience or postop has repeated enough times that it should graduate to a mechanical check per Rule 11.

**`recurrence_count`** — admin's count of how many times the same gap has appeared. Promoted from STM if admin recognizes the pattern; otherwise admin greps `staff/reviews/` for the finding class. `recurrence_count >= 3` is the default threshold for `promote`; below that, prefer `add` or `modify` with explicit rationale for early action.

**`cost_estimate`** —
- **S** — single file edit (one rubric line, one command-body phase note).
- **M** — command + schema edit, or rubric + multiple command bodies.
- **L** — schema rewrite, multi-file cascade, new command, new gate phase.

**`status`** lifecycle:
- `open` → `accepted` → (PR lands; entry stays with `pr_ref`)
- `open` → `rejected` (entry stays; admin scans on next proposal to avoid re-proposal)
- `open` → `deferred` (admin may re-surface once `defer_until` passes; not before)
- `open` → `superseded` (a later proposal replaced this one; the later entry's `supersedes` field points back)

---

## Anti-patterns (admin must avoid)

- **Content-failure-as-process-failure.** A single chapter under-delivering on a substance axis is a content problem, not a process problem, unless the gate that should have caught it was structurally incapable of catching it. Discriminator: "could a stricter version of the existing gate have caught this?" If yes, propose `modify`. If no, propose `add`. If the gate did catch it but the author shipped anyway, that's a disposition problem — propose `modify` on the disposition rules, not the gate itself.
- **Proposing on first occurrence of a SIGNAL.** SIGNALs are designed to surface taste-flags before they harden. Promoting a one-off SIGNAL to a mechanical check is premature. Wait for recurrence unless the failure was catastrophic.
- **Re-proposal of rejected work.** Admin scans the log for `status: rejected` proposals with the same `target.path` + `change_type` + materially-same rationale. If found, return `OK-PRIOR-REJECTION` instead of authoring a duplicate.
- **Vague target.** `target.path` must be a specific file. "The audit pipeline" is not a target; `.claude/commands/and-write.md` Phase 6 is.

---

## Matching rules (admin scan before proposing)

Before appending a new proposal, admin reads `staff/admin/process-proposals.md` tail and checks:

1. Is there an `open` proposal with the same `target.path` + `change_type`? If yes, append a comment to the existing proposal (`recurrence_refs: + <new evidence>`) and increment `recurrence_count`. Do not author a duplicate `open` entry.
2. Is there a `rejected` proposal with materially-same target + rationale? If yes, return `OK-PRIOR-REJECTION` with a one-line note citing the prior rejection. Do not re-author.
3. Is there a `deferred` proposal whose `defer_until` has passed? Re-surface it (don't author a new one); status flips back to `open` with a `re_surfaced_at` stamp.

---

## File header

`staff/admin/process-proposals.md` opens with a fixed header block (admin does not edit the header):

```
# Admin process-change proposals

Append-only log. Schema: schemas/admin-proposal.schema.md.
Triage stamps owned by the principal. Admin does not edit `status`,
`triaged_at`, `triaged_by`, `disposition_note`, or `pr_ref` on own
initiative — only on a follow-up dispatch carrying the principal's ruling.

---
```
