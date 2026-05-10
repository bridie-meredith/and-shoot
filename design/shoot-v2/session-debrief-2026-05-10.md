---
debrief: session-end
date: 2026-05-10
session-branch: claude/plan-shoot-v2-testing-GBvjQ
session-scope: improving /and-facets — full tuning of 5 facets, audit upgrade 5-class → 11-class, architectural pivot to tighter-audiences, orchestrator-critic established
final-status: s01e01 facet graph SUCCESSFUL under orchestrator-critic standard (7/7 criteria); ready for next session
---

# Session Debrief — /and-facets improvement session

## What shipped

### Pipeline build (Steps A–G of Beta three-pass facet pipeline)

- **Step A** — `/and-facets-r1` (renamed from original `/and-facets`). Round 1 blind authoring; 9 facet authors in DAG order; bones-only protolines as input.
- **Step B** — cite-index builder (`active-project/staff/cite-index/build_cite_index.py`). Wired into `/and-facets` Phase 7 as default. Derives `_cite-index.md` from facets + protolines.
- **Step D** — `/and-facets-r2`. Round 2 hybrid judge; 4 midband authors; full nine-facet graph + cite-index in every dispatch payload (per the user's captured Round 2 directive).
- **Step E** — `/and-facets-r3`. Round 3 relaxation pass; tighter caps; default-skipped in production per Step I convergence signal (s01e01 ran zero-change).
- **Step G** — `/and-facets-audit`. Final cross-cutting audit. Originally 5-class; upgraded to 11-class mid-session (added STRUCTURAL, FREQUENCY-BAND, METADATA-INCONSISTENCY, CURVE-SHAPE, AP-SCAN, TASTE-FLAG; beefed CONSTRAINT with mechanical licensed-by resolvability + POV-perceptual access).
- **Master chain** — `/and-facets` re-built as the master orchestrator; chains R1 + R2 + audit by reading the sub-command bodies; R3 default-skipped; sub-commands remain individually callable for resume.

### Five facets fully tuned via Phases C–F

| Facet | Pattern | Pass rate | Clean ACCEPT | Notable |
|---|---|---|---|---|
| memory | legacy 3-persona | 100% | 75% | First antagonistic tuning; established the loop |
| feeling | legacy 3-persona | 92% | 75% | URI-008 cleared post-Phase-F (feel:10 AP6 regression) |
| narrator-interest | legacy 3-persona | 100% | 78% | +3 file-level adds to close mask-too-perfect channel-coverage gap |
| vibes | legacy 3-persona | 100% | 95% | Cleanest legacy run; AP8 mass cleanup; vibes:19 WITHDRAWN |
| sensory | **tighter audience** | 100% | 83% | First end-to-end tighter-pattern run; pilot validated the architectural pivot |

### Audit trajectory (5 passes)

```
audit-r1 (5-class):  7 findings (4 hard + 3 signal)
audit-r2 (5-class):  5 findings (post-memory-remediation; 0 hard)
audit-r3 (11-class): 13 findings (1 hard + 12 signal; expansion-driven)
audit-r4 (11-class): 12 findings (0 hard + 12 signal)
audit-r5 (11-class): 10 findings (0 hard + 10 signal)
```

Hard count went 4 → 0 → 1 → 0 → 0 across 5 passes. Signal-finding peak was the 11-class methodological expansion (audit-r3); subsequent passes show graph converging toward fewer findings.

### Architecture: tighter audiences + antagonistic generation pivot

User directive 2026-05-10g: "use antagonistic generation and feedback, based on tighter audiences rather than formulaic rulesets."

Captured at `design/shoot-v2/tighter-audiences-architecture.md`. Pilot ran on sensory: 3 facet-specialized critic cards (`staff/audience/sensory-{disambiguation-pedant,modality-coverage,old-state-reader}/card.md`) replacing the uniform 3-persona dispatch. Validated:
- 100% concrete-evidence rate (vs legacy rubric-citation grounding).
- Higher THIN-rate interpreted as a feature (refusal-to-fabricate vs legacy's force-fit).
- File-level lens (modality-coverage critic) produced unique signal per-entry critics couldn't.
- Meta-recursion landed: card-tuning notes added in production (action-verb self-charge clause; loc-state-gap clause) within the same session.

### Orchestrator-critic — success gate

User directive 2026-05-10h: "establish an orchestrator level critic card meant to judge performance by results and run time. it will be the standard to satisfy for and-facets to be considered a success."

Card at `staff/audience/and-facets-orchestrator-critic/card.md`. 7 acceptance criteria; verdict scale: SUCCESS / SHIPPABLE-WITH-CAVEATS / NOT-SUCCESSFUL. Wired into `/and-facets` Phase 4b as mandatory verdict.

First fire on s01e01: NOT-SUCCESSFUL (5/7) — sensory clean-ACCEPT 50% < 75% (sensory:4 anchor-vacuum); showrunner memory stale.

Re-fire post-housekeeping fixes: SUCCESS (7/7). Trajectory climbing = good iteration signal, exactly what the critic was designed to detect.

### Bidirectional audit + tuning loop empirically validated

Three independent convergences:
- audit-r4 caught feel:10 AP6 independently of feeling Phase F.
- audit-r5 caught narrator:27 channel-mislabel independently of NI Phase F.
- audit-r3 surfaced feeling AP-006 + taste-005 simultaneous with NI Phase F surfacing taste-002 + taste-003.

The mechanical auditor and adversarial audience converge on the same findings from independent paths.

---

## What's queued for next session

### High-priority (likely-next directions)

1. **Counter-training-of-critics** — adversarial pattern on critic cards themselves. Gap I acknowledged this session: card edits happen by inspection (after observing attack quality), not by adversarial pressure on the cards. Build options:
   - Meta-critic dispatch reads each critic card and attacks: scope too narrow / too broad; missed attack vector; mis-calibrated example seam.
   - OR blind generation of seams using critic cards on held-out facet entry, then audience adjudication of seam quality.
   - Output: critic-card revisions under adversarial pressure.

2. **Mechanic-rated facets remaining** — state-updates (22 entries), loc-state (8), tens (102). Apply tighter-audience pattern; author 3 specialist cards per facet. Tens may be too large to tune adversarially — the audit's CURVE-SHAPE + FREQUENCY-BAND already mechanically catch its issues.

3. **`/and-season` tuning packet kickoff** — packet ready at `design/shoot-v2/and-season-tuning-packet.md` with copy-pasteable prompt for a separate session. Eight phases; six dispatches estimated. Targets season escalation curve, episode boundary placement, cross-episode continuity.

### Medium-priority (URI queue items in `design/shoot-v2/upstream-tuning-queue.md`)

- **URI-002** — protoline scene-peak coverage gap (s01e01 CURVE-SHAPE SHAPE-FAIL). 6 of 8 scenes lack rung-3 peak. Requires dramatist re-pass with scene-exception authority OR screen-writer kickback for additional charged beats. Heaviest queued item; touches protolines + tens facet; would resolve FREQUENCY-BAND signal too.
- **URI-003** — margit referrals: oc-account-ledger prop card; field-extensions on actor cards (Taylor hair-state/public-role; mother apprentice-ratification; father household-economic-tracking + role-as-master + ledger-authority-state); 4 monument cards for memory free-text glosses (cape-reflex / parent-as-cost / child-performance-grooves / control-as-evidence).
- **URI-006** — auditor itself needs tuning (Step G design item). Large multi-session project; gates flag-only → delete-authoritative.

### Low-priority / paused

- **URI-001 (memory rubric V2.1)** + **URI-007 (feeling rubric V2.1 + R2-add blind re-test)** — paused per the tighter-audiences pivot. The rubric edits would deepen the formulaic ruleset, which is the wrong direction under the pivot. Edits remain documentation-valuable as captured audience-validated insights; deferring landing them.
- **URI-005** — AP-SCAN remediation routes to next per-facet tuning round. NI tuning addressed ap-002, ap-003, taste-002, taste-003. AP5 stillness-inflation (tens:29) + AP8 vibes:7 prose-token + AP14 free-text gloss remain — most resolved during or queued.
- **Re-tuning legacy facets under new pattern?** — Open question from architecture doc. Memory + feeling + NI + vibes shipped under legacy; sensory pilot validated tighter-audience pattern. Whether to re-tune the legacy four under tighter audiences is undecided. Recommendation: don't unless audit signals regression; tighter-audience pattern goes forward only by default.

### Architectural items (longer-horizon)

- **Antagonistic generation Step 4** — adversarial pressure at *draft time* (author + critic-persona co-loaded; critique → revise within single dispatch). Deferred until tighter-audiences pattern validated across more facets.
- **Stitching** — facet graph is now SHIPPABLE-WITH-CAVEATS-OR-CLEAN per orchestrator-critic. Eventual `/and-stitch` or equivalent chapter-rendering pipeline is the next major build. Out of scope for /and-facets-improvement session; it's a separate downstream phase.

---

## Comments and observations carried forward

### R2-add NI-dependence pattern — confirmed FOUR times

Across memory (mem:5-8), Taylor feeling (feel:13), mother feeling (feel:14), and NI (narrator:22, 23, 24, 25; narrator:26 the lone exception), R2 graph-aware authoring systematically loosens rubric discipline. The R2 author uses NI/co-located facets as anchor for description-drafting, producing near-paraphrase rather than register-independent constructions. This is robustly systematic, not facet-specific.

The fix landed across each affected facet in defense passes. The PROCESS protocol fix — "R2-adds receive a mandatory blind §Form + Q1 + Q2 re-test before round close" — is captured at URI-007 item 9 but NOT yet wired into `/and-facets-r2.md`. Worth wiring in next session as a structural prevention rather than per-round remediation.

### Worm-canon-pedant is the dominant attack lens across all facets

Memory: 5 of 8 strongest seams. Feeling: 7 of 12. NI: 13 of 24. Voice-precision against character-card vocabulary is the most consistently productive attack vector. Pulp-enthusiast was weakest on vibes specifically (no purchase on bias-layer). Dark-fantasy-reader cuts deepest on AP8 token-prose because long prose-tokens read as MBA-deck taxonomy.

This pattern is itself signal: a future tighter-audience build that specializes the wcp-equivalent further may produce sharper attacks. The dfr-equivalent for vibes is the natural next specialization target.

### Process gaps surfaced (some fixed, some pending)

Fixed in-session:
- **Dramatist Read-only** — orchestrator writes from dramatist's payload (Step A — `/and-facets-r1` + master).
- **Per-character impersonator briefs need explicit absolute paths** (caught during R3.3a Taylor feeling — agent refused on path-resolution; re-dispatched with paths in the brief).
- **Audit STRUCTURAL over-strict on per-section ID monotonicity** (URI-004; doc-only resolution; `/and-facets-audit.md` should be amended next session to formalize).

Pending:
- **NI Phase E artifact omission** — agent didn't write `ni-tuning-defense.md` initially; I checked and saw it was absent, then it landed late. The check-too-early failure is a process gap. Future practice: trust agent self-reports; verify by reading the artifact after the agent reports completion.

### Critic ecosystem now has 4 explicit tiers

| Tier | Scope | Examples |
|---|---|---|
| Per-facet critics | content quality on a specific facet | sensory-{disambiguation-pedant, modality-coverage, old-state-reader} |
| Stitcher-side audience | final prose | dark-fantasy-reader, pulp-enthusiast, worm-canon-pedant |
| Auditor | mechanical 11-class scan | the auditor agent |
| Orchestrator-critic | pipeline performance (results + runtime) | and-facets-orchestrator-critic |

Each has explicit `scope:` discipline; no overlap. The architecture is solid.

---

## Files of interest for next session

```
.claude/commands/and-facets.md              — master chain (R1 + R2 + audit; R3 default-skip)
.claude/commands/and-facets-r1.md           — Round 1 only (callable for resume)
.claude/commands/and-facets-r2.md           — Round 2 only
.claude/commands/and-facets-r3.md           — Round 3 only (default-skipped)
.claude/commands/and-facets-audit.md        — 11-class final audit

active-project/staff/showrunner/memory.md   — current state (audited-r5; tuning_rounds_complete; orchestrator_critic SUCCESS)
active-project/staff/cite-index/build_cite_index.py — cite-index builder
active-project/staff/auditor/facets-final-audit.md  — audit-r5 report
active-project/staff/auditor/orchestrator-critic-verdict.md — first verdict + re-fire SUCCESS

active-project/theater/facets/              — 9 facet files + _cite-index.md (post-tuning + post-housekeeping)
active-project/theater/proto-lines/s01e01.md — citation-accrued; sensory:4 at @61

design/shoot-v2/
├── tighter-audiences-architecture.md       — pivot proposal
├── upstream-tuning-queue.md                — URI-001 through URI-008
├── and-season-tuning-packet.md             — kickoff prompt for separate session
├── memory-tuning-r2-{seams,defense,final}.md
├── feeling-tuning-{seams,defense-{taylor,mother,father},final}.md
├── ni-tuning-{seams,defense,final}.md
├── vibes-tuning-{seams,defense,final}.md
└── sensory-tuning-{seams,defense,final}.md

staff/audience/
├── and-facets-orchestrator-critic/card.md  — pipeline success gate
├── sensory-disambiguation-pedant/card.md   — meta-tuned mid-session
├── sensory-modality-coverage/card.md
└── sensory-old-state-reader/card.md        — meta-tuned mid-session
```

---

## Recommended next-session opening move

Read this debrief. Read `design/shoot-v2/upstream-tuning-queue.md`. Pick from the high-priority queue:

- **If continuing facet tuning under tighter pattern**: pilot on state-updates (22 entries; mechanic-rated; would test pattern at larger corpus). Author 3 specialist critic cards; run Phases C–F; audit-r6.
- **If addressing the architectural gap**: build counter-training-of-critics adversarial pattern. Author a meta-critic; have it attack the existing per-facet critic cards; observe seam quality; revise cards.
- **If pivoting to season scope**: kick off `/and-season` tuning per the packet — separate session.
- **If addressing the upstream protoline gap**: URI-002 (CURVE-SHAPE SHAPE-FAIL); requires dramatist re-pass on s01e01 protolines with scene-exception authority. Heavier work but resolves both CURVE-SHAPE and FREQUENCY-BAND audit findings.

The orchestrator-critic verdict on s01e01 is SUCCESS. No remediation required to ship this episode's facets. Next session is purely forward motion.
