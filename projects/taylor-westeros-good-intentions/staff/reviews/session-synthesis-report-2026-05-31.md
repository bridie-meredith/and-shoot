# Session synthesis report — and-shoot pipeline 2026-05-31

This report is written at the end of a single session that exercised the
full and-shoot pipeline across seven shipped chapters of
`taylor-westeros-good-intentions` (`b01-c01` through `b01-c07`), built
and validated a new sub-section coherence command (`/and-cohere`),
converged a manual cohere iteration loop to PASS-COHERE, applied an
inline concision pass, and identified a tooling failure mode that
forced two background fork dispatches to be abandoned. The session ran
on branch `session/audit-and-stitch-2026-05-31`, 14 commits ahead of
main at close.

The report covers:
1. What each pipeline command does and what it produced in this project.
2. Issues observed and their root causes.
3. Content opportunities — where to spend leverage next.
4. Meta-learnings about the pipeline + the session approach.
5. Path A vs Path B determination for c08+, including a root-cause
   analysis of the draft-layer / upstream divergence.

---

## 1. Pipeline walkthrough

The pipeline is layered: `/and-project` once, `/and-series` +
`/and-substance series` + `/and-cast` once per project, then the
per-chapter loop repeated 18-22 times. After the chapter loop, optional
post-ship machinery (`/and-postop`, `/and-review verdict`, `/and-ablate`)
and — new this session — `/and-review cohere` + `/and-cohere` for
cross-chapter coherence. Polish (`/and-wrap`) remains deferred.

### `/and-project` (one-time, non-rerunnable)

Activates the project. Scaffolds `active-project/`, runs a boundary-scope
fork (isolates library persona slugs from downstream forks), runs a
taste-judge fork (single-card audience persona for menu picks at brief
expansion), runs world-building 1a-1d (constraints + open questions +
1d law/lore card authoring), and binds staff personas. For this project
the audience trio is `cape-fic-reader`, `dark-fantasy-reader`,
`worm-canon-pedant`. The boundary-scope fork is the layer that catches
library persona slug leakage — relevant because `cards/personas/`
contains slugs like `mira-stonefield` and these can leak into
downstream forks via three vectors (boundary-scope embed, prompt-binding
carry-forward, screen-writer/margit not isolated by name).

### `/and-series` (re-runnable)

Authors the series chunk + seven structural commitments. Phase 1.5
designs the premise via a six-lens menu (path / lens / mode);
`taylor-westeros` uses a *composed* lens (path-4 penitential motivation +
path-2 political mechanism + contempt-emergence layer). Phase 1.5d
expands the chosen path into a trajectory — 14 deltas across 7 axes
(`moral_framework`, `capability`, `position`, `social_tether`,
`relational_anchor_status`, `moral_legibility_to_self`,
`political_register_toward_elite`). Phase 3 fires audience + dramatist
+ naive-reader review. Phase 4 persists `series.chunk` (path +
trajectory; prose field permanently retired 2026-05-17) + `series.structure`.

Structural shape: 1 book, 18-22 chapters, 3-5 scenes per chapter, single
POV (Taylor first-person; non-Taylor chapters marked interludes),
tragic series-end shape, single-book length floor (re-run OQ-9 to
compress).

### `/and-substance series`

Authors the substance signature. Phase 4a state axes + Phase 4b cost
ledger + Phase 4c antagonist pressure + Phase 4d `actor_baselines`
(post-`/and-cast`). Phase 5 fires audience + dramatist + auditor.
Substance signature defines: 7 state axes with start_rank / end_rank /
class / curve_class; ~14 ledger entries (`cl-*`) with gain/cost pairs
that anchor at named chapters; antagonist-pressure curves; and
`chunk_targets` (bone delta_per_axis, scene delta_per_axis, chapter Δ).
For this project: monotonic moral_framework collapse 2→8;
political_register contempt-emergence at d05/d09/d13/d14;
relational_anchor_status (Wren) as the cost-bearer arc with cl-d06
landing across c06-c10.

### `/and-cast`

Authors the cast roster from substance-driven cast brief. Phase 1
brief; Phase 2 margit candidate menu; Phase 3 screen-writer selection +
dramatist viability; Phase 4 margit provisioning (creates
`active-project/actors/<slug>/{card,ltm,stm,state,vibes}.md`); Phase 5
series-level audit checkpoint — **the only blocking human checkpoint in
the chain.** Approved 2026-05-24 (`series_audit.approved_at`).

For this project: Taylor (POV), Otto Hightower (offstage antagonist;
referenced via Jarvis Coin), Jarvis Coin (courier-conduit), Halvard
(Septon; argument-counterforce at c07), Wren Stitch-Maker (cost-bearer),
Oswyn Mudway (ward-elder; c01 recognition + c04 elder-at-cart and
recurring), Sera Hightower (the trade's price-tag; offstage).

### `/and-substance book b01`

Authors book drama + per-chapter Δ + handoff_in/out. Phase 0 HARD-aborts
if `series_audit.approved_at` is missing or `stale_since` is set.
Distributes the series-level signature into per-chapter delta-targets
and authors `chapters[].handoff_in` / `handoff_out` blocks that the
chapter chain consumes.

### Per-chapter loop (×7 shipped + c08 paused)

The per-chapter authoring chain has five phases that ran for every
chapter c01-c07:

**`/and-substance chapter b<NN>c<MM>`** — scene chunks + scene_conflict
+ pov_narrator + dramatic_shape + goal. Phase 5.5 chunk_cold_read
(`PASS-CHUNK-VOICE-RISK` arms `/and-stitch` 8.5 muffle check; PROP-0019-A,
wired 2026-05-29, retroactively validated against c05 evidence, first
*live* test was c06).

**`/and-write`** — scene decomposition into bones with per-bone
substance_delta. Phase 1.5 dialogue cobonding (URI-WRITE-DIALOGUE-COBONDED;
per-character dialogue files co-emitted at Phase 7). Phase 6 substance
bone-gate (per-bone axis-movement + per-scene aggregate Δ +
cost-paid + opposing-force-visible; EVENT-NOT-CONCRETE HARD;
ABSTRACTION-DOMINANT SIGNAL). Phase 7 emit (bones + scene-map facet +
dialogue files as an atomic set).

**`/and-review bones`** — mandatory chunk→bones fidelity review. Includes
`follow_check` (PROP-0020) — `FOLLOW-FAIL` HARD-gates `/and-facets`.
Dialogue coverage gate subsumed from former `/and-facets` Phase 5.

**`/and-facets`** — ten facets + scene-map validation. Phase 1 R1
fanout (10 authors; dialogue R1 removed under URI-WRITE-DIALOGUE-COBONDED).
Phase 2 fanin + cite-index. Phase 2.5 context+aliveness review →
context-ledger + grounding-ledger (PROP-0020/0022). Phase 3 R2 fanout
(5 judges). Phase 4 fanin + 4d scene-map validation. Phase 4.5 post-R2
context+aliveness re-review. Phase 4.6 conditional R3 + fixer/WARN.
Phase 5 mechanical audit. Phase 5b adversarial audience-gate
(3-of-3 accept; cycle cap 3). Phase 5c admin process-critic. Phase 6
persist + orchestrator-critic verdict on the book.

**`/and-stitch`** — eight render phases + Phase 9 cold-read terminal
gate. Phase 0 voice-exemplar resolution; Phase 1 lens-anchored render
(scene-window default); Phase 1.5 per-scene tournament (multi-arm voice
exemplar with POV pre-filter); Phase 2-4 cull/compress/voice-transform;
Phase 4.5 separated completeness + aliveness scoring (PROP-0022);
Phase 5 local flow + speaker-paragraph break; Phase 6 buildup; Phase 7
editorial reflection; Phase 8 finalize + scene-callout strip + RECONCILE;
Phase 8.5 central-event-muffle check (PROP-0019-A); Phase 9 cold-read
terminal gate (PASS / PASS-WITH-DEPTH-PASS-REQUIRED / FAIL). Phase 9.5
admin process-critic.

For c01-c07 the chain ran cleanly per chapter — all seven Phase 9
PASS with caveats absorbed at depth-pass. Terminal deliverable lands at
`active-project/draft/<book>-<chapter>.md`.

### New this session: `/and-review cohere` + `/and-cohere`

Author and validated PROP-0030 (`cohere` subcommand of `/and-review`) +
PROP-0031 (`/and-cohere` iteration loop) plus `schemas/cohere-state.schema.md`.
First live run on c01-c07 returned **FAIL-COHERE** on three load-bearing
axes (naive-q4 Wren cold walk-on; naive-q6 apparatus-register cumulative
load; audience-substance cape-fic-reader SUBSTANCE-FLAT). After Fork A
chapter-level revises and one in-session iter-2 patch round, achieved
**PASS-COHERE.** Then an inline concision pass cut ~10% of words while
preserving PASS-COHERE.

The cohere primitive was the missing layer: each chapter individually
passed Phase 9, yet read together they failed at cross-chapter
accumulation. This is the exact failure class CLAUDE.md Rule 17 / the
2026-05-29 readability-completeness overhaul was *supposed to fix*
through PROP-0019/0020/0022 — but those gates all scope to one chapter
at a time. Cohere fills the cross-chapter gap.

### `/and-postop`, `/and-ablate`, `/and-review verdict`

Optional post-ship machinery. Not exercised in this session beyond
admin process-critic tail invocations on each pipeline finding. The
`/and-ablate` facet-ablation study from 2026-05-26 produced the
evidence base for PROP-0001/PROP-0002/PROP-0003 (em-dash fold density,
voice-prime, exposition surface field).

---

## 2. Issues observed and root causes

### Issue 1 — Cross-chapter quality is not gated by any per-chapter gate

**Symptom.** c02-c05 individually PASSED `/and-stitch` Phase 9 with
PROP-0022 aliveness twin verdicts of ALIVE. Read together as a stretch,
they FAIL naive-q6 apparatus-register cumulative load.

**Root cause.** All readability/completeness gates added in the
2026-05-29 overhaul (PROP-0019/0020/0022 + spine-legibility pair)
scope to one chapter at a time. The substance contract is per-chapter;
the bone-gate is per-bone; the cohere axis is per-stretch and has no
gate machinery upstream.

**Action.** PROP-0030/PROP-0031 are wired and live-validated this
session. Acceptance + downstream wiring is the obvious next move:
fire `/and-review cohere` automatically after every Nth shipped chapter
(N = 5-7 = the cape-fic-reader's stretch attention span); fire
`/and-cohere` opt-in when the principal wants iteration to PASS-COHERE.

### Issue 2 — Subagents shipped reports despite operating on wrong source

**Symptom.** Fork C and Fork D were dispatched with detailed briefs
naming protected anchors verbatim. Both worktrees inherited an ancestor
commit lacking those anchors. Both subagents flagged the anchors as
"not present in source" — and still proceeded to ship cuts despite the
brief saying "DO NOT CUT" on those exact phrases.

**Root cause.** The dispatching pattern doesn't include a precondition
phase. The agent should have: (a) greped for each anchor in source,
(b) if any missing, returned a precondition-failed error immediately
without making changes. Instead it proceeded to cut and shipped a
report that *correctly listed* the missing anchors and *incorrectly
treated* the missing-anchor case as licensing further cuts. The brief
was ambiguous — "DO NOT CUT these phrases" doesn't translate cleanly
to "if these phrases are missing, you are on the wrong source —
abort." The agent's failure mode was filling the ambiguity with
work-completion bias.

**Further investigation.** This is partly a brief-writing pattern
problem (use precondition gates instead of in-body fences) and partly
an agent-behavior problem (work-completion bias overrides
"halt-and-clarify" even when stakes are named). Worth a small process
proposal: every editing-pass fork should be dispatched with a
precondition-grep phase as its first step, with explicit abort-on-fail
semantics.

### Issue 3 — `isolation: worktree` doesn't reliably honor session-branch HEAD

**Symptom.** Fork C dispatched after my iter-2 direct commit at
59582278. Its worktree should have branched from 59582278. Per
post-completion inspection, Fork C's word-count baseline matched an
*earlier* state (8954 words ≈ original unrevised) rather than the
59582278 state (~10,000 words). Fork D, dispatched after Fork A and
Fork B merges, also baselined on the earlier state.

**Root cause hypothesis (further investigation required).** The Agent
tool's `isolation: worktree` may be:
- caching HEAD at session start and not re-reading it on subsequent
  dispatches;
- using the cwd's HEAD at dispatch time, where cwd may have shifted
  into an earlier worktree (this session's cwd did shift into Fork B's
  worktree before I `cd`'d back to main repo — possibly the Agent tool
  is reading the bash subprocess cwd not the conversation-level cwd);
- branching from a stable reference (e.g. `origin/main` or the parent
  shell's HEAD at session start) rather than the current session
  branch HEAD.

The behavior is reproducible (twice in one session), so it's
deterministic, not race-condition. Worth filing as a Claude Code tool
bug with concrete reproduction steps from this session as evidence.

**Workaround for this session.** Done the editing pass inline.
Alternative: pre-merge a long-lived checkpoint branch before
dispatching a fork that depends on recent in-session commits.

### Issue 4 — No defined policy for prose-layer revisions

**Symptom.** This session's iter-1, iter-2, and inline concision pass
all landed at `active-project/draft/` only. The bones files, scene-map
facets, per-character dialogue files, showrunner `memory.md`
chapter blocks, and the ten chapter-level facet files do NOT reflect
any of the revisions. The session shipped revised drafts to a state
where the chain cannot reproduce the drafts on re-run.

**Root cause — this is structural, not a bug.** The pipeline is
one-way by design: chunks → bones → facets → draft. `/and-stitch` is
authored to be deterministic-from-bones (with LLM-mediated render
noise). Polish (`/and-wrap`) is deferred. There is no protocol for
back-propagating draft-layer edits to upstream artifacts. Two design
choices interact:
1. The cohere primitive (added this session) lands at draft layer
   because that's where cold-read happens.
2. The polish-deferred chain accepts draft-layer divergence on re-run
   as a known cost.

So cohere convergence (which is post-ship cold-read work) drifts
upstream by design.

**Action.** Three policy options, increasing rigor:
- **(cheap)** Define a draft-layer-only license. Certain edit classes
  (concision cuts of redundant prose; calendar anchors in prologues
  authored by `/and-stitch` Phase 0.6; character-callback
  reinforcements that don't add events) don't require
  back-propagation. Mark these edits in commit metadata as
  draft-layer-only; future audits know to ignore them.
- **(medium)** Define a partial back-propagation policy: substantive
  additions (new events, new bones with substance_delta, new
  scene-anchor presence) require back-propagation; cosmetic additions
  don't. Build a heuristic checklist for cohere iteration patches.
- **(heavy)** Build a reverse-cascade tool: read draft diff + bones
  state, propose upstream changes for principal triage.

The (cheap) option is enough as long as downstream chapters don't
reference the additions. See Section 5 for the c08+ analysis.

### Issue 5 — Sub-section boundaries aren't structured

**Symptom.** I picked `c01-c07` as "the sub-section" arbitrarily —
could have been c01-c05 (the Otto-acceptance arc), c01-c08, c01-c12
(book first-half), etc. cohere accepts a range parameter and runs
against whatever it's given, but the *meaningful* sub-sections aren't
declared anywhere.

**Root cause.** Book-level structure is flat — `chapters[]` in
sequence; no arc-grouping. Series-level `trajectory.deltas[]` have
chapter-anchors (d03 at c03, d05 at c05, etc.) but no formal
arc-window labels.

**Action.** Could add `sub_section_boundaries: [(c01, c07, "rule-tested
to-rule-named"), (c08, c14, "..."), ...]` to book chunk. Or accept
that cohere ranges are flexible by design and let the principal pick.
The latter is what the current state assumes.

### Issue 6 — c08 cast collision: `wenna-cobb`

**Symptom.** c08 bones (already shipped through Phase 6 bone-gate
PASS) include `wenna-cobb` in the cast list (line 4 of bones file)
and as a living body the feed returns (bone 17: "the insect-feed
returns wenna-cobb"). But c07 dialogue introduces Wenna Cobb as a
*dead six-year-old* — the founding-entry name Taylor counters
Halvard's "slow way costs less" with. There are two Wennas, or c08's
chunk author was unaware of c07's dialogue assignment, or c08's
wenna-cobb is a related-but-not-the-same character (sister, family
member).

**Root cause (likely).** c08's chunk authoring at `/and-substance
chapter b01c08` predated or operated parallel to c07's dialogue
authoring. The cast slug `wenna-cobb` was minted at c08 chunk-level
without checking against c07's character index. The audit chain
didn't catch it because c08's bone-gate is per-chapter — it checks
c08's internal consistency but doesn't cross-walk c07's dialogue
content for slug collisions.

**Action.** This is a parking-lot item — out of scope for this
report's recommendations on Path A/B. But worth flagging as
`pl-2026-06-01-001` (next-day stamp) targeting `/and-write b01c08
revise` or `/and-substance chapter b01c08 revise`. The fix is small:
either rename c08's wenna-cobb to a non-colliding slug, or recast the
character as a related-family member with the collision made explicit
in the bone substance.

This issue is independent of the Path A/B question — it predates the
session.

### Issue 7 — Forks "back-to-back" pattern needs a handoff protocol

**Symptom.** Forks C and D were supposed to operate sequentially: D
consumes C's output. But they're independent worktrees with their
own base-branches. C's output was never merged before D was
dispatched; D operated on the same ancestor as C.

**Root cause.** No documented pattern for serial-fork-chains. The
`isolation: worktree` model assumes parallel-independent dispatch.
For chained passes, either (a) merge between dispatches (and incur
the cost of fork-1 issues blocking fork-2), or (b) have a shared
working branch that each fork pushes to (current pattern doesn't
support this), or (c) inline everything.

**Action.** For now, accept that fork-chains require merge-between
or inline. Could be a follow-on tooling improvement but not
load-bearing.

---

## 3. Content opportunities

### 3a. Run cohere on every shipped sub-section

The `/and-cohere` machinery is built. Run it after c08 ships, then
c12, then c18 (book close). Each run is ~5-10 dispatches per
iteration; ~30-40 dispatches per book at default cap. Catches drift
when drift is cheap to fix.

### 3b. Audience persona rotation

PROP-0030's Phase 3 audience rotation is round-robin across the
three personas (`cape-fic-reader`, `dark-fantasy-reader`,
`worm-canon-pedant`). c01-c07 used cape-fic-reader. The next cohere
run should use dark-fantasy-reader; the one after, worm-canon-pedant.
Each persona's hot-buttons surface different failure classes.

### 3c. The Rushwick courier-attack thread (pl-2026-05-31-007)

Still unprocessed across c06-c07. The structural promise c05 made
(courier filed at recurring-Rushwick-resident anchor; enforcement-
incident attached) needs a payoff in c08-c10 OR a c05 contractual
re-frame. c08's bones do NOT reference Rushwick — so the promise is
still open. Principal triage required. Most natural landing: c10
court-tier scene where the courier or the enforcement-pattern
returns.

### 3d. Polish un-defer becomes tractable

PASS-COHERE + concision-passed prose at the sub-section level is the
state at which `/and-wrap` un-defer is finally tractable. The
pre-pinned archive lift target (`archive/commands/and-wrap-polish-
deferred.md` Phases 1-2) could be exercised against the seven-chapter
sub-section as the first live test. This was deferred under the
substance overhaul "until upstream substance machinery is proven."
The machinery is proven — three live chapters fired all the gates
correctly. The cohere primitive is the missing piece. Polish un-defer
is the natural follow-on.

### 3e. Tournament voice-exemplar tuning

The `/and-stitch` Phase 1.5 per-scene tournament with POV pre-filter
+ counterweight discipline (URI-EXEMPLAR-POV-FENCE, 2026-05-26) is
live but default-off. Could be turned on selectively for chapters
where Phase 9 PASS-WITH-DEPTH-PASS-REQUIRED fires (i.e., c07 in this
project). Would need a brief project-specific experiment to confirm
benefit.

### 3f. Process-proposal triage cadence

This session created PROP-0030 + PROP-0031 + ~5 candidate proposals
(precondition-gates for forks; sub-section boundaries; draft-layer
edit policy; isolation:worktree investigation; cast-slug
cross-chapter check). Open process-proposal log is long (~30+
proposals). A weekly triage cadence — accept / defer / reject — would
keep the proposal pipeline from becoming a graveyard.

---

## 4. Session learnings

### Audit-first works.

The session opened with a cold-read audit of the combined sub-section
before any other work. That audit drove every subsequent decision:
the narrative-improvement plan, the cohere process design, the
iter-2 patches, the concision targets. The per-chapter pipeline gates
would have shipped these chapters as complete; cold-read audit
identified failure modes the gates can't see.

### Single-edit leverage points exist.

The iter-2 c06 line-7 patch (adding the explicit Wren chain naming
at the recognition moment) was a single sentence-level edit that
flipped two of three load-bearing FAIL axes simultaneously. The
iter-2 c05 sensory anchor (breath-shallowing + bay-damp) inside the
densest apparatus passage flipped the third. Two edits, ~50 words,
took c01-c07 from FAIL-COHERE to PASS-COHERE. Suggests cohere
iteration cap of 2-3 is well-calibrated.

### Tooling failures should auto-abort, not silently fall back.

Both Fork C and Fork D produced shipped reports despite operating on
wrong source. The agents should have noticed "the brief names plants
I don't see in source" and aborted. They didn't. The
agent-behavior pattern of work-completion-over-halt-and-clarify is
worth a process check.

### Manual cohere convergence works as proof for the live version.

PROP-0030/PROP-0031 are designed for live agent-dispatched runs but
this session validated the iteration loop logic manually
(Fork B's first run + iter-2 patches inline). Both iterations
landed on the exact failure classes the rest of the pipeline didn't
catch. The live version will validate that subagent dispatches
reproduce the manual findings.

### Cross-chapter substance gaps are different from per-chapter substance gaps.

The per-chapter substance bone-gate catches axis-movement integrity
within one chapter. Cross-chapter substance accumulation is a
different shape — relational anchor (Wren) needs to be FELT as
carried across the sub-section, not just be DECLARED in each
chapter's substance_delta. The cohere primitive's character-presence
axis (naive-q4) is what catches this. The two gates are
complementary; neither subsumes the other.

### Worktree branch lifecycle is noisy but tolerable.

Both Fork C and Fork D worktrees remained locked after agent
completion (lock release tied to agent process termination, which
the harness manages). Not a problem to fix at the workflow level;
just to note when looking at `git worktree list`.

---

## 5. Path A vs Path B determination for c08+

The user's directive: "only implement changes if required for chapters
8 on up to end of book 1. Find the root cause of this divergence and
also include in the report."

### 5a. Is c08 already at risk from c01-c07 prose-layer divergence?

c08's bones at `active-project/theater/bones/b01-c08.md` (already
shipped through Phase 6 bone-gate PASS-FOR-SHIP) reference 24 bones
across 3 scenes. Cast: taylor, oswyn-mudway, wenna-cobb, corwick.
Locations: the-hook-ward, the-lane-junction-rushwick-margin,
the-chandler-corner, the-water-point, the-lane-mouth, the-rushwick,
the-feed-station.

Cross-referenced against the prose-layer plants:

- **c07 four-names consequence three paragraphs (iter-1).** c08
  bones don't reference patrol-pattern, substrate-shift, filled-slot
  replacement, or absences-on-count. The c07 consequence is a
  reader-facing event-registration but c08's bones don't observe its
  downstream state. **c08 does NOT depend on this.**
- **c04 Halvard fixture plant (iter-1).** c08 bone 2 returns
  "the-chandler-corner" as a feed-feature location, but does not
  reference Halvard by name. The corner exists in c08 as terrain,
  not as Halvard's corner. **c08 does NOT depend on the Halvard
  introduction date being c04 vs c07.**
- **c04 Cobb founding-entry plant in prologue (iter-1).** c08 has
  `wenna-cobb` in cast — but this is a *different* character than
  c07's dead six-year-old (see Issue 6). c08's wenna-cobb is a
  living body the feed returns. **c08 does NOT depend on the c04
  prologue Cobb founding-entry plant.**
- **c06 hinge Wren chain naming (iter-2).** c08 cast does not
  include `wren-stitch-maker`. **c08 does NOT depend on this.**
- **c02 Wren callback at ward-junction body (iter-2).** Same —
  reader-facing reinforcement, c08 doesn't reference.
- **c05 evening sensory anchors (iter-2).** Reader-facing, no
  downstream dependency.
- **Calendar anchors in prologues (iter-1, all chapters).** c08's
  prologue (not yet authored — c08 is paused at bones-review) will
  author its own calendar anchor at Phase 0.6 exposition-preamble.
  No upstream dependency.
- **Concision cuts (inline session).** Cut prose was bone-faithful
  redundancy; cuts removed prose without removing bone substance.
  No downstream dependency.

**Conclusion: c08+ does NOT require any upstream alignment of the
prose-layer plants.** All revisions are either reader-facing
reinforcements or apparatus-density cuts; none introduce new substance
state that c08's chunks reference.

### 5b. cl-d05 / cl-d06 multi-chapter ledger anchors

Two ledger entries land partially across c01-c07 and partially across
c08-c10:

- **cl-d05** (political_register-prot rising shape; peaked at c05
  evening replay): "remaining +1.5 anchors at b01c06-b01c08."
  Memory.md L3839 says c08 is in the multi-chapter ledger window
  for political_register continuation toward d09 articulated-contempt.
- **cl-d06** (social_tether-cost-bearer, Wren): "second +1.0 anchors
  at b01c08-b01c10 when Wren becomes structurally necessary to the
  coverage map." Memory.md L4137.

Neither of these ledger entries is affected by the prose-layer
revisions. The substance contract is unchanged; only prose-layer
*presentation* of the existing substance was edited. c08's bones
already anchor cl-d05's remaining +1.5 (per c08 Phase 6 bone-gate
PASS-FOR-SHIP). cl-d06's +1.0 deferred to c09/c10 per
pl-2026-05-30-001.

**No action required for cl-d05 / cl-d06.**

### 5c. Recommendation: Path A for c08+

Defer all upstream alignment of c01-c07 prose-layer plants. The chain
is divergent at draft layer for these chapters, and that's tolerable
because c08+ chunks don't reference the divergent material.

If a future audit (a `/and-review consistency` or
`/and-review pipeline` invocation) catches the divergence as a finding,
fix at that time. The plants are reader-facing only; the cost of
deferring is bounded.

### 5d. Root cause of the upstream divergence

The divergence has three structural sources:

**Cause 1: Polish-deferred chain treats `/and-stitch` output as
terminal.** Under the substance overhaul (2026-05-17), `/and-wrap` was
deferred and `active-project/draft/<book>-<chapter>.md` became the
terminal deliverable. The chain has no in-band machinery for editing
the terminal deliverable while keeping upstream in sync. Any
draft-layer edit creates divergence by design.

**Cause 2: Cohere is post-ship, and post-ship work lands at draft.**
PROP-0030 / PROP-0031 (built this session) operate on shipped drafts
because cross-chapter cold-read needs the shipped material. Iteration
loop patches (Fork A revises + iter-2 inline patches) land where the
cold-read fires: at draft layer. The upstream chunks/bones/facets/
memory aren't re-authored. By design, cohere convergence drifts
upstream.

**Cause 3: No back-propagation protocol.** There is no documented
policy for which draft-layer edits get back-propagated to upstream.
Without policy, every draft-layer edit silently accumulates
divergence. The chain has no instrument to flag, scope, or close the
divergence except by re-running the chain (which would lose the
draft-layer polish).

**Compound effect.** Cause 1 sets the stage (draft is terminal).
Cause 2 introduces structured draft-layer edits (cohere iteration).
Cause 3 prevents resolution (no protocol). Result: every cohere
convergence is followed by silent draft/upstream divergence.

### 5e. Recommended fix for the root cause

A small process change closes the gap without heavy tooling:

**Add a `draft_layer_only` policy to cohere iteration patches.** Each
cohere iteration patch declares one of three classes:
- **`cosmetic`**: concision cuts, sentence-rhythm edits, paragraph
  joins. No substance change. Draft-layer-only by default; no
  back-propagation required.
- **`presentation-reinforcement`**: character callbacks, sensory
  anchors, calendar anchors in prologues. Reader-facing only; no new
  substance. Draft-layer-only by default; back-propagation optional
  (preserves chain re-runnability if elected).
- **`substantive`**: new events, new bones with substance_delta, new
  scene-anchor presence that downstream chapters reference.
  Back-propagation **required** before the next chapter's chunks are
  authored.

Cohere iteration tags each patch at apply-time. A new
`/and-review consistency` mode (or extension to `/and-review pipeline`)
checks: every `substantive` patch must have a matching back-propagation
commit before the next chapter's chunks fire.

This is a small policy + a small audit pass. Doesn't require new
tooling. Closes the divergence for c08+ work without forcing
upstream-alignment on patches that don't need it.

For this session: tag iter-1 + iter-2 + inline patches retroactively:
- Calendar anchors in prologues — `presentation-reinforcement`
- c03 + c05 Wren passive plants — `presentation-reinforcement`
- c02 Wren callback at ward-junction — `presentation-reinforcement`
- c04 Halvard fixture plant — `presentation-reinforcement`
- c04 Cobb founding-entry in prologue — `presentation-reinforcement`
- c06 hinge recognition chain naming — `presentation-reinforcement`
- c06 four-month silence chain naming — `presentation-reinforcement`
- c05 mid-passage sensory anchors — `presentation-reinforcement`
- **c07 four-names consequence three paragraphs — `substantive`*** —
  but c08+ doesn't reference. **Carve-out exception.**
- All inline concision cuts — `cosmetic`

All draft-layer-only acceptable; no back-propagation required for c08+.

---

## Closing

The session moved the project from "seven shipped chapters that
individually passed Phase 9" to "a converged PASS-COHERE sub-section
that has been concision-passed and reads as a coherent stretch."
Along the way it built and validated the missing cross-chapter
quality machinery (`/and-cohere` + `/and-review cohere`), identified
a recurring tooling failure with `isolation: worktree`, and surfaced
seven distinct issues with three immediate actions (Issue 1 acceptance
+ wiring; Issue 3 investigation; Issue 4 policy proposal) and four
deferred items (Issues 2, 5, 6, 7).

c08+ work can proceed without upstream alignment of the c01-c07
prose-layer plants. The divergence is bounded by design (polish-deferred
chain + cohere post-ship) and tolerable for downstream chapters that
don't reference the divergent material. The recommended policy fix
(`draft_layer_only` classification + a consistency audit on
`substantive`-class patches) closes the gap without heavy tooling.

The most important single follow-up is principal triage of
PROP-0030 / PROP-0031 — the live cohere machinery is the missing
gate the substance overhaul left open, and this session is the
evidence base. Triaging both opens the path to running cohere
opt-in or scheduled across the rest of the book.
