---
packet: and-season-tuning
date: 2026-05-10
status: PLAN — to be executed in a separate session
trigger: user direction 2026-05-10f — "write and commit a packet to tune and-season with our antagonistic reviewers and auditors"
parent-pattern: design/shoot-v2/antagonistic-tuning-plan.md (memory facet adversarial pattern)
parent-pattern: .claude/commands/and-facets-audit.md (11-class audit pattern)
target: .claude/commands/and-season.md (season-scope orchestrator)
---

# /and-season Tuning Packet

A packet for tuning the season-scope orchestrator using the same two patterns we just validated on the memory facet:

1. **Antagonistic reviewers** — three audience persona forks attack each output unit through their distinct lenses (atmosphere / momentum / voice-precision). Defense or revise per `design/shoot-v2/facet-tuning-process.md` Phase 4. Final adjudication under same locked rubric per Phase 5.
2. **Upgraded auditor** — 11-class mechanical scan adapted to season-scope artifacts (the SVO aggregate, the per-episode split, the season memory). The same HARD vs SIGNAL split; the same audit + tuning bidirectional loop.

## Why now

We just validated the bidirectional audit + tuning loop on the memory facet:

- Audit-r1 caught 7 mechanical findings (5-class).
- Audit-r2 caught 5 soft flags post-remediation.
- Phase 3 audience seam-finding produced 8 strongest seams (5 STRONG / 3 MODERATE / 0 THIN). All 5 audit soft flags mapped to STRONG/MODERATE seams.
- Phase 4 defense produced 2 DEFEND / 6 REVISE / 0 WITHDRAW.
- Phase 5 adjudication: 8/8 ACCEPT (6 clean + 2 with caveat). Lift: 0% clean → 75% clean.
- Audit-r3 (upgraded 11-class) caught 13 findings, 1 HARD + 12 SIGNAL. New classes (FREQUENCY-BAND, CURVE-SHAPE, METADATA-INCONSISTENCY, AP-SCAN, TASTE-FLAG) caught what prior audits missed.

The pattern is shippable. /and-season is the next natural target because:

- It produces a multi-episode artifact (the SVO aggregate) that no per-episode audit currently validates.
- The nine-pass season review inside /and-season is the natural place to insert antagonistic reviewers.
- The SHAPE-FAIL finding from audit-r3 traces upstream — protolines didn't carry enough scene-level peaks. /and-season is one layer above protolines and is where dramatic-shape coverage decisions land.
- We have a season-scope artifact (`active-project/theater/proto-lines/s01.aggregate.md` per the proto-line schema) that can serve as tuning corpus.

## What /and-season currently does

Per `.claude/commands/and-season.md`:

- Authors one continuous SVO aggregate covering the whole season.
- Iterates the five-pass SVO pipeline + nine-pass season-scope review against that aggregate.
- Splits to per-episode files by interpretive cut (ideal size + dramatic shape; episode count must be a multiple of 3).

The nine-pass season-scope review is the existing review apparatus. We don't replace it — we **augment** it with antagonistic reviewers and the auditor pattern.

## What antagonistic tuning would add to /and-season

### Targets

- **Season escalation curve.** Does the season escalate honestly across episodes? The dark-fantasy-reader attacks atmosphere drift; the pulp-enthusiast attacks momentum dead zones; the worm-canon-pedant attacks voice-fidelity drift across multi-episode arcs.
- **Per-episode dramatic shape.** Each episode within the season needs a peak. The audit-r3 SHAPE-FAIL finding suggests s01e01 doesn't carry scene-peaks; this likely traces to /and-season's split decision putting transit material into episode boundaries.
- **Cross-episode continuity.** State carryover, character arcs, monument-callback trajectories. Audience attack: does the season feel like one story or eight short stories?
- **Episode boundary placement.** /and-season splits by interpretive cut. Audience attack: does each cut land at a natural breath, or does it interrupt momentum?

### Phase shape (mirroring memory tuning)

**Phase A — Corpus prep.**
- Load the season aggregate (`active-project/theater/proto-lines/s01.aggregate.md`) and the per-episode split (`s01e01.md` through `s01e06.md`).
- Lift season-level metadata: chunk statement, theme, escalation spine, cast roster, location set.
- Group by review axis: episode-boundary, dramatic-shape, cross-episode-continuity, character-arc.
- Lock the relevant rubrics: `/and-season` Phase 3 nine-pass review criteria + the SVO writer pipeline rubrics.

Output: `design/shoot-v2/and-season-tuning-corpus.md`.

**Phase B — Reviewer baseline.**
- The nine-pass review is the existing baseline. Document what each pass already catches.
- Identify gaps — categories of failure the nine-pass review doesn't surface.

Output: `design/shoot-v2/and-season-tuning-baseline.md`.

**Phase C — Adversarial seam dispatch.**
- Single audience dispatch (loads all 3 personas) running adversarial mode against:
  - The season aggregate as a whole.
  - Each episode boundary (split decision).
  - The escalation curve across episodes.
- Output: per-persona seams + aggregated strongest seam per audited unit.

Output: `design/shoot-v2/and-season-tuning-seams.md`.

**Phase D — Aggregate to single seam per unit.**
- Same as memory tuning Phase D. Strongest seam per audited unit.

Output: included in Phase C output (single dispatch combines C+D, per memory pattern).

**Phase E — Defense or revision.**
- The /and-season author (screen-writer or showrunner — TBD which agent owns the season-scope) defends or revises.
- DEFEND with rubric citation; REVISE the season aggregate or split decision; WITHDRAW (rare — entire episode-boundary or escalation arc unsalvageable).

Output: `design/shoot-v2/and-season-tuning-defense.md`.

**Phase F — Final adjudication.**
- Audience re-review under same locked rubric. Per-unit ACCEPT / REJECT.
- Cross-unit dependency check: episode boundaries adjacent to each other, escalation-arc consistency.
- Shippability assessment: is the season as a whole shippable, or does it need re-pass?

Output: `design/shoot-v2/and-season-tuning-final.md`.

**Phase G — Auditor pass (new — adapted from /and-facets-audit).**

Single auditor dispatch with the season-scope corpus. Adapted 11-class checks:

- **STRUCTURAL** — every episode file has the seven extended-header fields per `schemas/proto-line.schema.md`; `aggregate_range` fields are non-overlapping and contiguous; episode count is a multiple of 3 (per the /and-season constraint).
- **FREQUENCY-BAND** — per-rubric distributions across the season (not just per-episode). Tens distribution across all 6 episodes; sensory across; etc.
- **METADATA-INCONSISTENCY** — season memory.md vs episode-list consistency; aggregate file vs split file consistency.
- **CURVE-SHAPE — season-level.** Each episode is a "scene" at season scope; the season needs an act structure with rising action, climax episode (typically e05 or e06 of 6), denouement. Season-shape verdict.
- **CONTRADICTION** — cross-episode state contradictions (Taylor's location at end of e02 vs start of e03; etc.).
- **DEDUP** — episode boundary that repeats prior-episode content; redundant escalation beats across episodes.
- **SUPERFLUOUS** — episodes or scene-clusters that don't move the season forward.
- **CONSTRAINT** — series-law violations across the season; cast-presence consistency.
- **AP-SCAN** — the season-rubric anti-patterns (TBD — these emerge from Phase B baseline).
- **TASTE-FLAG** — audience-attack-anticipation candidates at season scope.
- **PILE-UP REVIEW** — episodes with unusually dense state-change accumulation; warranted vs over-loaded.

Output: `active-project/staff/auditor/season-final-audit.md`.

**Phase H — Rubric carry-back.**
- Same as memory tuning Phase G. Rubric edits queued for V2.1; not landed in this run.

## Estimated cost

- Phase A: 1 dispatch (corpus prep).
- Phase B: 1 dispatch (baseline documentation — could be main-session work).
- Phase C+D: 1 audience dispatch.
- Phase E: 1 author dispatch.
- Phase F: 1 audience dispatch.
- Phase G: 1 auditor dispatch.
- Phase H: rubric carry-back work (not a dispatch; queue entries).

Total: 6 dispatches plus orchestration. Larger than the per-facet runs because the corpus is bigger (whole season vs one facet's entries) but tractable.

## What this packet is and isn't

- **Is:** a plan to apply the validated antagonistic-tuning + 11-class-audit patterns to /and-season. Decisions deferred to the kickoff session.
- **Is not:** an executable command. /and-season-tune doesn't exist yet; building it is part of the kickoff session.
- **Is not:** a re-author of /and-season. The existing /and-season ships fine; this is a tuning project against its output.

## Open questions for the kickoff session

1. **Who is the /and-season author?** /and-season currently dispatches screen-writer for SVO authoring + dramatist for shape + auditor for constraint. Which of these owns "season-level decisions" for defense/revise? Likely showrunner, since season-scope is the showrunner's natural memory holder, but showrunner is read-only orchestrator. Worth resolving.
2. **Tuning corpus scope** — just s01 (the only completed season), or wait for s02 to land for cross-season validation?
3. **Build /and-season-tune as a new command**, or run ad-hoc the first time and command-ize after?
4. **Rubric source-of-truth** — /and-season's nine-pass review is documented in the command body itself, not in a separate rubric file. Should the rubric be extracted to `design/shoot-v2/rubric-and-season.md` first to give the audience and auditor a stable reference?

## Kickoff prompt for separate session

The user can paste this into a fresh Claude Code session to begin the work:

```
Read design/shoot-v2/and-season-tuning-packet.md in full. We are starting
the antagonistic-tuning + auditor pass on /and-season, modeled on the
memory facet run we just shipped (design/shoot-v2/memory-tuning-r2-*.md).

Begin with:

1. Read .claude/commands/and-season.md to refresh on what the season
   orchestrator currently does.
2. Read the validated patterns we're applying:
   - design/shoot-v2/antagonistic-tuning-plan.md (the memory plan that
     succeeded)
   - design/shoot-v2/memory-tuning-r2-{seams,defense,final}.md (the
     three artifacts from the memory run; reference for shape)
   - .claude/commands/and-facets-audit.md (the upgraded 11-class auditor)
3. Read the current corpus:
   - active-project/theater/proto-lines/s01.aggregate.md (season aggregate)
   - active-project/theater/proto-lines/s01e01.md through s01e06.md
     (per-episode split)
   - active-project/staff/showrunner/{series-plan,season-s01-plan}.md
4. Decide the four open questions in the packet (section "Open questions
   for the kickoff session"). Default-accept the recommended path if
   nothing is contested:
   - Author for defense/revise: showrunner with explicit override of its
     read-only-orchestrator role; OR screen-writer (the SVO author).
     Recommend showrunner for season-scope decisions; screen-writer
     handles SVO-level revisions surfaced as a sub-task.
   - Corpus: s01 only for first run.
   - Build: ad-hoc first run; command-ize as /and-season-tune after.
   - Rubric source: extract /and-season's nine-pass review to
     design/shoot-v2/rubric-and-season.md before Phase A.

Then execute Phases A through H per the packet. Commit after each phase
to a feature branch (mirror the per-phase commits from the memory run:
seams artifact -> defense artifact -> final artifact -> audit report).

Status flags should land in active-project/staff/showrunner/memory.md
under the season entry: tuning_complete, tuning_corpus_path,
tuning_audit_path, etc.

Flag for the upstream-tuning queue
(design/shoot-v2/upstream-tuning-queue.md) any issues that require
re-authoring at /and-protolines-v2 or earlier, rather than blocking the
tuning run on them.

Run all dispatches in background where the layer allows. Sequential where
shared-file write-race makes sequencing necessary.

Keep me in the loop with one summary per phase. Don't pause to confirm
between phases unless an open question surfaces that I need to decide.
```

---

## Risks

- **Season-scope corpus is large.** 6 episodes × ~150 protolines/episode = ~900 protolines. Audience seam-finding at this scale may produce too many seams; aggregation discipline matters.
- **Authoring agent ambiguity.** /and-season uses multiple agents for different sub-tasks; "the /and-season author" is not a single fork. Phase E may need to be split per sub-task (screen-writer for SVO revisions; dramatist for shape revisions; showrunner for season-memory updates).
- **Rubric extraction overhead.** If we extract the nine-pass review to a formal rubric file before the run, that's its own session of work. Recommend doing this as part of the kickoff session's Phase A.
- **CURVE-SHAPE feedback loop.** The audit-r3 SHAPE-FAIL on s01e01 is itself an /and-season output (via /and-protolines and Phase-4 split). This tuning run may reveal that the SHAPE-FAIL is a /and-season-rubric defect, not a per-episode protoline defect. If so, fixing the rubric here cascades down to the protoline pipeline.

---

## Success criteria

- The audience's strongest seam per audited unit is defended or revised under the locked rubric.
- The auditor's 11-class scan produces a SEASON-SHAPE verdict + per-episode metadata-consistency check.
- A measurable lift on a quantifiable metric (e.g., audience accept rate; per-episode peak coverage; season-shape verdict).
- The tuning run produces 1+ rubric carry-back candidates that, if landed, would resolve the s01e01 CURVE-SHAPE SHAPE-FAIL upstream.
- The artifacts are reusable — when s02 lands, the pattern can run again without re-design.
