# Research / tuning backlog — reconciliation (2026-06-23)

**Purpose.** Reconcile the `process-proposals.md` `status:` fields and the
"first live test pending" gates against what actually shipped during the
(now-complete, archived) `taylor-westeros-good-intentions` book and the
no-ledger overhaul. Read-only reconnaissance; no proposal was re-triaged here —
this is a worksheet for principal triage.

**Headline.** The raw count is **~38 `status: open` + 7 `accepted`**. That
massively overstates the real backlog: the `status:` field is systematically
unmaintained. Mechanisms ship via DEC + command-body edits, but the owning
proposal's `status:` is rarely flipped. **At least 12 "open/accepted" items
have demonstrably shipped.** The genuinely-actionable *new* backlog is ~6 items.

---

## A. Shipped — status stale (recommend flip; evidence on disk)

| PROP | Subject | Evidence it shipped |
|------|---------|---------------------|
| 0005 | Persona-exemplar architecture | `schemas/persona-exemplar.schema.md` + `cards/persona-exemplars/` populated; CLAUDE.md Rule 16 (URI-PERSONA-EXEMPLAR, live) |
| 0005-A | Audience-exemplar Tier-1 / Tier-2 split | CLAUDE.md Rule 16 codifies Tier-1/2/3; library populated |
| 0017 | Cherry-pick default-on | present in `.claude/commands/and-stitch.md` |
| 0019 | Chunk-cold-read upstream gate + apparatus cull | wired in `and-substance.md` (Phase 5.5) + `and-stitch.md` (Phase 8.5); CLAUDE.md Rule 17 "all wired" |
| 0023 | Apparatus-register aliveness axis | wired at `/and-facets` Phase 2.5 (FOLLOWABLE×ALIVE); reshaped by DEC-0115 |
| 0031 | `/and-cohere` command | `.claude/commands/and-cohere.md` shipped |
| 0046–0051 | No-ledger overhaul (DEC-0115) | fences live in `and-write` / `and-stitch` / `and-review` / `and-facets` (ABSTRACTION-AS-SUBJECT, SCENE-ABSTRACT-DOMINANT, LEDGER-REGISTER, naive-follow/FOLLOW-FAIL, EMBODIMENT-BLOCKED); CLAUDE.md Rule 22. Currently `status: accepted` → should be `implemented`. |

**Note on the "first live test."** PROP-0019/0022/0023 were described as
"validated retroactively on c05; b01-c06 first live test." The book ran to
**c20** — the gates were exercised live. Verdict of the live run: they did
**not** catch the book's central readability defect (16 consecutive AIRLESS
"design-inherent" dispositions), which is why **DEC-0115** added the root-cause
no-ledger fix + the N=2 disposition circuit breaker. So these gates are not
"pending a test" — they were tested, found insufficient alone, and superseded
by the DEC-0115 layer.

---

## B. Partially superseded by DEC-0115 / Rule 22 (scope-reduced, not closed)

| PROP | Original target | Residual after DEC-0115 |
|------|-----------------|--------------------------|
| 0030 | Cross-chapter apparatus-register accumulation tracking | apparatus-register is now *prohibited as a prose mode*, not merely tracked — most of the concern is moot. Residual: cross-chapter *accumulation telemetry* unbuilt, but lower value now. |
| 0037 | `/and-substance` Phase 0 HARD-abort on N consecutive SHIPPED-WITH-CAVEATS (force `/and-cohere`) | Rule 22's **N=2 disposition circuit breaker** addresses the same failure mode at the disposition layer. PROP-0037's specific Phase-0 cohere-precondition counter is **still unbuilt** (confirmed: no `consecutive_shipped_with_caveats` check in `and-substance.md`). Genuine-open but scope-reduced — decide whether Rule 22 subsumes it. recurrence_count=8 (was the book's actual back-third failure mode). |

---

## C. Genuinely open + actionable (the real new backlog)

| PROP | Subject | Cost / readiness | Note |
|------|---------|------------------|------|
| **0052** | Cross-chapter **structural-sameness** detector | **Cheap (~1 dispatch, reads bones/scene-map, no re-render); well-specified `proposed_diff`** | Standout. Confirmed real gap: nothing detects N consecutive chapters running one scene-template. b01 mid-book ran Template-T in 8/10 chapters; the no-ledger rebuild fixed *register* but left *structure*, making sameness more legible. Structural analogue of Rule 22's circuit breaker. recurrence_count=2. |
| 0037 (residual) | Cohere-precondition Phase-0 gate | small command-body edit | see §B; build only if Rule 22 is judged insufficient |
| 0001 / 0002 | Per-chapter em-dash-fold density cap + terminal-anchor fence | small rubric edit | RUNBOOK explicitly lists as "in queue, not implemented." Genuinely open. |

---

## D. Genuinely open — first-occurrence authoring-discipline SIGNALs (low priority)

Single-chapter findings from the now-complete book, recorded but never promoted
to HARD (each wants a second-occurrence confirmation that won't come from this
archived book). Value is as *guidance for the next project*, not standing work:

`0006` `0007` `0009` `0010` `0011` `0012` `0013` `0014` `0015` `0016`
`0024` `0025` `0026` `0027` `0028` `0033` `0034` `0035` `0036`
`0038` `0039` `0040` `0041` `0042`

Several of the apparatus/abstraction-flavored ones (e.g. 0024 event-concreteness,
0030, 0035 central-event staging) are partly absorbed by the DEC-0115 no-ledger
fences. `0038–0041` had no captured `source_verdict` — worth a glance to confirm
they're real and not stubs.

---

## E. Evidence-blocked (cannot close by triage; need new runs)

- **PROP-0003 / 0003-A** — voice-prime field: needs fresh ablation evidence on a live project.
- **Tournament-tuning Q1–Q5** (`design/tournament-tuning.md`): cherry-pick N, scorer/judge separation, seam-gate tightness, audience-tournament interaction, scorecard auto-fires — all need ≥5 chapters of accumulated scorecards. No active project → frozen.
- **Tier-2 exemplars** (orchestrator-critic / dramatist / auditor / editor): explicitly blocked — priming regressed output (2026-05-26). Do not author without fresh experimental basis.

---

## F. OOS / follow-on (CLAUDE.md "Not in scope") — design decisions, unbuilt

Absolute-length floor · emotional-substance orthogonality · plot-arc-completion
dramatist check · world-detail consistency audit · `cards/dialects/` →
`cards/behaviors/` rename · **name-novelty enforcement** (the "Mira" leak; three
candidate fixes sketched) · `/and-wrap` polish revival (gated on substance
machinery being proven).

`design/substance/plan-holes-2026-05-17.md` **Hole E** still names an explicit
*principal decision*: which intent-gap items (4/6/10) carve into the plan vs.
OOS-track (5/7/8/11). **Hole C** (chapter-status enum in showrunner-memory
schema) also unbuilt.

---

## Recommended disposition

1. **Backlog hygiene (do first, cheap).** Flip the §A statuses to
   `implemented`/`superseded` with the evidence citations above. Turns a
   ~38-item "open" wall into ~6 genuinely-actionable items + a low-priority
   guidance tail. This is the single highest-leverage move — the current
   counts are actively misleading.
2. **Build, if anything, PROP-0052.** It is the only genuinely-new item that is
   cheap, well-specified, and addresses a *confirmed* (not first-occurrence)
   gap. Buildable now without an active project (command-body edit to
   `/and-review cohere` or `/and-stitch` Phase 10).
3. **Decide PROP-0037 residual** against Rule 22 (subsumed vs. still wanted).
4. **Everything else (D/E/F) is project-gated** — parks until the next book
   gives second-occurrence evidence or a live tuning run.
