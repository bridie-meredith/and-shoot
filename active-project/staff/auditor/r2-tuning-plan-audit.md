---
audit: R2 judge tuning plan
date: 2026-05-10
target: design/shoot-v2/r2-judge-tuning/PLAN.md
auditor: auditor (subagent dispatch)
---

# Audit Report — R2 Judge Tuning Plan

**Scope:** Design document review
**Target:** `design/shoot-v2/r2-judge-tuning/PLAN.md`
**Supporting files reviewed:** A-corpus.md, B-locked-rubric.md, C-arbiter-protocol.md, upstream-tuning-queue.md (URI-023, URI-025), `.claude/commands/and-facets-r2.md`, memory-tuning-r2-final.md, feeling-tuning-final.md, facet-tuning-process.md

---

## Findings

### HARD-001 — Baseline metric is post-revision, not pre-revision

PLAN.md line 14 states the baseline is "75% clean / 25% caveat" from "memory's dedicated R2 cycle." This characterizes that figure as a baseline for R2 judge performance. It is not. Per `memory-tuning-r2-final.md` lines 81–84, that 75% clean figure is the *post-tuning result* after Phase-4 revision and Phase-5 audience adjudication. The 8 entries were already revised by R2 authors and then adjudicated; the 75% measures how many of those *already-revised* entries came out clean. R2's raw judge accuracy — how many of its unrevised decisions survived audience review — is not measured anywhere in the corpus.

**Why this matters:** the entire metric design rests on this baseline. If the baseline is actually a post-revision acceptance rate, then the ≥80% target in Action 4 is comparing a post-revision outcome to another post-revision outcome, which cannot isolate R2 judge improvement. The project's success metric is structurally incoherent against its stated goal.

**Criteria for resolution:** identify what R2's raw decisions were before Phase-4 revision and how many of those were accepted without modification. If that data doesn't exist, the plan must acknowledge it has no clean baseline and recalibrate the metric accordingly.

### HARD-002 — "No command edit" exit branch contradicts URI-023 commitment

PLAN.md lines 61–62 contain this decision point for Action 3: "if Action 2 didn't surface a single failure mode that the existing R2 prompt fails to gate, no command edit lands." This is directly inconsistent with URI-023 item 9 in `upstream-tuning-queue.md` (lines 272–277), which states that item 9 — "R2-adds receive a mandatory blind §Form + Q1 + Q2 re-test before round close" — is the load-bearing R2 finding and is specifically being addressed by this tuning project. The queue entry explicitly names Action 3's output (`.claude/commands/and-facets-r2.md`) as the landing target. The "no command edit lands" path contradicts a prior commitment that is already recorded in the queue.

**Why this matters:** if the plan runs Action 2 and finds nothing new, the author may close without landing URI-023 item 9. That leaves a confirmed, audience-validated finding unacted on, and the queue item open indefinitely.

**Criteria for resolution:** narrow the "no command edit" path. If Action 2 surfaces no *additional* failure modes beyond what URI-023 item 9 already names, Action 3 still lands item 9. The decision point should read: "if Action 2 produces no findings *beyond* URI-023 item 9, Action 3 lands item 9 only and the project closes."

### HARD-003 — G4-drop instruction misreads its own supporting document

PLAN.md lines 74–75 say to drop G4 because "the thresholds (≥2 same-strategy, ≥3 instances) are exactly the mechanical contraband." But those count-thresholds do not exist in the current G4. `B-locked-rubric.md` lines 80–87 show G4 already reformulated as a taste-question: "does anything feel formulaic?" with explicitly no counting. The count-thresholds the PLAN cites as the reason to drop G4 were from an earlier design draft, not the locked rubric. The PLAN is arguing against a version of G4 that B already discarded.

**Why this matters:** the instruction to drop G4 will be read as operating authority. If Action 3 drops G4 from the command, the command loses the cross-character pattern-blindness gate (F-R2-4), which is a confirmed failure mode with 4+ instances in the corpus (A-corpus.md lines 113–118). The plan would be undoing the fix for a confirmed failure because it misread its own supporting document.

**Criteria for resolution:** correct the "drop G4" instruction. Either acknowledge G4 is already non-mechanical and remove the drop instruction, or name a different reason to drop G4 grounded in the current B-locked-rubric.md text.

### SIGNAL-001 — Audience personas evaluate entry quality, not decision quality

Action 2 (PLAN.md lines 43–44) instructs audience personas to ask per entry "did this R2 decision earn its place? Free-form justification — taste only, no rubric checklist." The 3 audience personas were tuned during R1 facet work against per-entry content (a feeling flag, an NI spotlight, a memory entry). They have no stated competence for evaluating a judge's decision-making process. They can say whether a facet entry is good; the question Action 2 asks is whether the judge's *reason for producing it* was honest. These are different tasks. An audience persona is not equipped to distinguish "R2 added this entry for a niche-driven reason but the entry turned out good" from "R2 added this entry for at-rest evidence and it's also good."

**Why this matters:** Action 2 is the primary validation gate. If the personas can only evaluate entry quality (not decision quality), Action 2 collapses into a standard R1-style audience review. It cannot distinguish a well-disciplined R2 from a lucky R2 that happened to produce good entries for bad reasons. F-R2-2 (multi-justification under-strictness) and F-R2-3 (lonely-entry adjacent-context dependency) are specifically about decision discipline, not entry quality — they would be invisible to an audience review that only asks "is the entry good?"

### SIGNAL-002 — Arbiter triggers calibrated for wrong reviewer type when applied to audience

C-arbiter-protocol.md lines 36–38 define Trigger T1 as firing when a verdict contains "primarily rubric citations (AP labels, Q gates, named anti-patterns) without naming concrete content." This is calibrated for R2 author decision logs. PLAN.md Action 2 also runs the arbiter against audience persona verdicts. But audience personas do not produce rubric-label-heavy justifications — they produce taste verdicts in conversational register. Per feeling-tuning-final.md throughout, persona output is prose reasoning, not labeled checkboxes. Trigger T1 will not fire on persona output because that output doesn't use rubric labels. The arbiter protocol is calibrated for the wrong reviewer type when applied to audience personas.

**Why this matters:** the arbiter checking for mechanical persona output will either never intervene (T1 never fires on taste prose) or will have to invent criteria not in the protocol. C-arbiter-protocol.md's triggers T1, T3, T5 are designed for someone who has a rubric open in front of them. Personas don't. The arbiter intervention layer for audience review has no workable trigger set.

### SIGNAL-003 — Narrow-scope path validates against the same data it tuned on

PLAN.md lines 38–39 define the Action 1 scope-narrowing trigger: "if R2-touched entry count across non-memory-non-feeling facets is < 20, narrow scope and skip Action 4." But if scope narrows to memory + feeling only, Action 4 validation runs against the same corpus that was already adjudicated. Those files represent the end-state of tuning on those facets, including revisions. A re-run of R2 on already-adjudicated data is not an independent validation; it measures whether a retrained R2 reproduces the cleaned output, not whether it generalizes. If this path triggers, the plan has no independent validation gate.

**Why this matters:** a project that closes with "we validated on the same data we tuned on" has no evidence the improvement generalizes. The narrow-scope path needs either a genuinely held-out corpus or an acknowledgment that the validation result is corpus-internal.

### SIGNAL-004 — Decision-log labeled fields partially produce the behavior arbiter is trying to suppress

B-locked-rubric.md's "Core principle" (lines 16–18) states that G1–G3 require "taste-argument with reasoning" rather than checklist work. But the G1 justification format (lines 44–46) asks for "2–3 sentences explaining what the cold-read produces." G2 (lines 58–60) asks for "4–8 sentences tracing the motive." These are paragraph-length requirements with word-count bands. The decision log format (lines 92–115) requires labeled subfields (`Cold-read verdict:`, `Motive:`, `At-rest test:`). Reviewers fill in named fields rather than writing free prose. The distinction between "taste-argument" and "checklist" is thinner than the rubric claims once the decision log format is applied.

**Why this matters:** if the arbiter is checking that reviewers don't recite rubric labels, but the decision log template requires labeled fields in a fixed format, the arbiter will struggle to distinguish structural-format compliance from genuine taste-argument. The rubric's own log format partly produces the behavior the arbiter is trying to suppress.

### SIGNAL-005 — Risk 5 introduces unauthorized parallel path against URI-025

URI-025 in `upstream-tuning-queue.md` lines 305–310 states tensometer promotion to mandatory gate in Pass S9.5 is "contingent on R2 tuning Phase F validation passing." PLAN.md Risk 5 (lines 84–85) names this dependency but describes it as: "may be worth promoting tensometer to S9.5 in parallel under a 'best-effort R2' caveat rather than gating on this project." This contradicts the user direction recorded in URI-025, which established the contingency explicitly.

**Why this matters:** the PLAN is generating an unauthorized parallel path against a stated dependency. If someone acts on the PLAN's Risk 5 language rather than URI-025's contingency clause, tensometer gets promoted before R2 discipline is established, which is exactly the condition URI-025 was designed to prevent.

---

## Clean

- **Scope calibration (4 actions vs. 7 phases):** simplification correctly motivated. Sequencing data-gathering first, validation second, intervention only if warranted is sound. Decision points are real branch points except the URI-023 problem in Action 3.
- **Session budget table:** credible. Dispatch estimates internally consistent with C's arbiter overhead model.
- **Risk register:** Risks 1–4 honestly named. Risk 1 (corpus thinness) accurate; plan has structural response. Risk 4 (R2 not facets-shaped) correctly identifies analogy-strain.
- **Arbiter as main session:** correct architectural choice; subagent arbiter would lose state between interventions.
- **Self-scoped deletion + fence discipline in and-facets-r2.md:** clean. Not a surface this project needs to touch.
