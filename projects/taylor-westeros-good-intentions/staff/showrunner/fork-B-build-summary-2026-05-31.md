# Fork B build summary — 2026-05-31

Session: PROP-0030 + PROP-0031 build-and-run.
Worktree: `worktree-agent-a8eb9a5659185ddd2` (branched from `session/audit-and-stitch-2026-05-31`).
Fork A: running in parallel on a separate worktree; revising chapter drafts. No coordination this session.

---

## Deliverables shipped

| Artifact | Path | Status |
|---|---|---|
| `/and-review cohere` subcommand body | `.claude/commands/and-review.md` (extended; added cohere section under verdict subcommand) | Authored, ready to execute on PROP-0030 accept |
| `/and-cohere` command body | `.claude/commands/and-cohere.md` (new) | Authored, ready to execute on PROP-0031 accept |
| Cohere state schema | `schemas/cohere-state.schema.md` (new) | Authored, matches `parking-lot.schema.md` shape |
| Manual cohere run report | `active-project/staff/reviews/cohere-b01-c01-c07-2026-05-31.md` (new) | First manual run output — verdict FAIL-COHERE |
| This summary | `active-project/staff/showrunner/fork-B-build-summary-2026-05-31.md` | Handoff document |

Commit on worktree: `Fork B: author /and-cohere + /and-review cohere + cohere-state schema (PROP-0030/0031)`.

---

## Manual cohere run — verdict

**`/and-review cohere b01 c01-c07`**

**Verdict: FAIL-COHERE** (3 load-bearing FAILs)

Load-bearing FAILs:
- **naive-q4** — character-presence accumulation. **Wren Stitch-Maker arrives cold at her c06 hinge.** Named in c01 (one line); referenced obliquely in c02 / c04 inside the deliberate-exclusion frame; not referenced c05; then asked to carry a relational hinge in c06 ("the silence that had been between us for four months"). The reader has not been given enough to receive the c06 beat.
- **naive-q6** — apparatus-register cumulative load. Each chapter individually passed Phase 9 and Phase 5b. Across seven chapters the accounting-register accumulates past sustainable density without sufficient embodied counterweight. c07's Halvard break works *because* the register has drained the prose first — which works for c07, but signals the register needed earlier relief.
- **audience-substance (cape-fic-reader rotation)** — **SUBSTANCE-FLAT**. Driven by the same Wren cold walk-on hitting the persona's "new character earning trust without paying for it" hot-button on a load-bearing structural beat. Substance compounds on c01/c03/c07; flatlines on c02/c04/c06 apparatus middles.

Non-load-bearing CAUTIONs (advisory, would land as SOFT parking-lot items in live run):
- naive-q1 (voice consistent at cost of monotony)
- naive-q3 (calendar drift c05→c06; narrated but at start only)
- naive-q5 (sensory thin in chapter middles)
- naive-q7 (c02 + c05 read as machinery-chapters)
- naive-q8 (close lands; apparatus-fatigue lowers c08 appetite)
- dramatist-arc (asymmetric pacing — 2-2-2-1 across c01-c07)
- dramatist-scene-shape (interior-dominant skew)

PASS axes:
- naive-q2 (setup→payoff inventory — every promise pays, holds, or is explicitly deferred)
- dramatist promise/payoff inventory (ACCEPT)
- dramatist antagonist pressure (ACCEPT)

---

## Chapter-revise queue (4 items; HARD)

Listed in full YAML in the cohere report. Summary:

| Item | Chapter | Severity | Driver | Fix shape |
|---|---|---|---|---|
| pl-2026-05-31-001 | b01c02 | HARD | naive-q4 | Add bone-level recognition of c02 "ward-junction body" as Wren; the yield at the alley-mouth needs to carry "this is the c01 girl" as substance |
| pl-2026-05-31-002 | b01c04 | HARD | naive-q4 | Add c04 bone for mutual non-acknowledgment with Wren at second-ward range — relational beat, not declarative |
| pl-2026-05-31-003 | b01c06 | HARD | naive-q4 + audience-substance | c06 hinge bones need to carry the relational weight the prose currently claims by assertion ("four months silence") |
| pl-2026-05-31-004 | b01c05 (+ c02 + c04 secondary) | HARD | naive-q6 | Apparatus-register relief breaks — at least one embodied moment in each of c02 / c04 evening, c05 evening review the highest-leverage single fix |

Queue NOT appended to live `parking-lot.md` per Fork B scope — listed in full YAML in the cohere report for principal paste-in on triage approval.

---

## Open questions for principal triage

1. **Series-substance vs chapter-revise framing of Wren accumulation.** The c01 register choice ("nobody here knows my name") is what *causes* Wren's under-presentation. The Fork B revise queue treats this as a fixable bone-level accumulation problem. The deeper read is that the signature itself is in tension with conventional character-presence accumulation — the prose is being asked to carry a person the narrator refuses to write down. If the answer is "Wren has to be felt-but-unnamed," the fix is harder than bone additions. Principal: chapter-revise (Fork B queue) OR escalate to series-substance review?

2. **PROP-0030 + PROP-0031 acceptance dependency.** This Fork B build assumed PROP-0030 / PROP-0031 will be accepted. Schemas, command bodies, and the manual-run report all reference the not-yet-live `chapters[<slug>].cohere_review` / `chapters[<slug>].cohere_iterations` memory.md fields. Per Fork B scope, schema-level memory.md additions are deferred. If PROP-0030 is rejected, the cohere subcommand should be reverted from `.claude/commands/and-review.md`; if PROP-0031 is rejected, `.claude/commands/and-cohere.md` should be archived. Schema file `cohere-state.schema.md` should be archived if both reject.

3. **Cohere subcommand vs `/and-review` Common-Phase Phase 4.5 interaction.** Cohere subcommand has a Phase 4 that calls out the always-fires admin pattern; it's also covered by the `/and-review` Common Phase 4.5 auto-fire-on-non-PASS contract. There is no double-fire (Phase 4.5 only fires on non-PASS; cohere's Phase 4 persist + parking-lot append is what makes it non-PASS-eligible). But worth confirming the call-pattern on live execution.

4. **Convergence cap default of 3.** Per design plan, default `--max-iter 3`. Cost shape suggests realistic case is 1-2 iterations. Cap of 3 is conservative; principal may want to lower to 2 to bound spend more tightly on opt-in runs.

5. **Audience persona rotation tracking file.** `active-project/audience/<slug>/cohere-history.md` is implied by Phase 1 Fork C round-robin. Schema for that file is not authored (out of scope; minimal — one entry per `<book>-<range>-<timestamp>` invocation). Principal may want margit to bless the format before first live cohere run.

---

## Handoff to Fork A / follow-on session

Fork A (parallel session) is running chapter-revise work on its own worktree. Fork A's worktree carries the per-chapter revises that the principal will merge into main.

After Fork A returns and is merged:
1. Principal reviews this Fork B build (this summary + the three command/schema files + the manual cohere run report).
2. Principal triages PROP-0030 / PROP-0031.
3. On accept: live `/and-cohere b01 c01-c07` runs against Fork A's revised drafts. The convergence check (PASS-COHERE on the revised stretch) is the canonical first-live-validation of the new machinery.
4. On reject: revert the worktree commit per the open-question-2 unwind plan above.

Fork B claims no convergence — these are *proposed* fixes against the *current* (pre-Fork-A-revise) drafts. The live cohere re-run after merge will either ratify the proposed fixes (PASS-COHERE on revised) or surface a different revise queue (Fork A's revises may have already addressed some of these items; some may persist; some may surface new items).

---

## Cost spend (Fork B session)

- Read: design plan (large), `/and-review.md` (large), `parking-lot.schema.md`, `audit-report.schema.md`, `/and-postop.md`, combined draft c01-c07 (read in two passes covering all 470 lines).
- Write: 3 command/schema files (cohere subcommand inline-extension of and-review.md, and-cohere.md new, cohere-state.schema.md new), cohere report (~12k words), this summary.
- Dispatches: 0 (Fork B builds machinery; live agent-dispatched cohere is a follow-on session per Fork B scope constraint).
- Commits: 1 build commit; this summary will commit after write.

Total session: under the one-Agent-session budget. The command-body authoring was the bulk of spend; the manual cohere run was read + reason against the combined draft.
