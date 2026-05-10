---
run: and-season-tuning-r1
date: 2026-05-10
status: ACTIVE
parent-packet: design/shoot-v2/and-season-tuning-packet.md
tuning-corpus-anchor: HEAD = c22d26e7fc8236be6e5346a66040eb530a4d52ee
locked-command-hash: cd4aa6595c701483d17ff3b90ab46fd7f11d5ca4 (.claude/commands/and-season.md)
---

# /and-season tuning — Run R1 — Decisions

The packet (`design/shoot-v2/and-season-tuning-packet.md`) names four open questions for the kickoff session. These are the decisions for Run R1.

## Q1. Defense/revise authoring agent

**Decision:** **showrunner** acts as the lead author for season-scope decisions (escalation curve, episode boundary placement, cross-episode continuity, season memory). Where a seam pressures specifically the SVO-level prose of an episode boundary, showrunner may surface a sub-task to **screen-writer**; where a seam pressures dramatic shape inside a stretch, showrunner may surface a sub-task to **dramatist**. The packet's recommended default ("showrunner with explicit override of read-only-orchestrator role") is accepted.

**Override note:** the showrunner agent definition declares it does NOT have the Agent tool and is a memory-holder only. For Phase E we are dispatching **showrunner in author mode for tuning purposes only** — Phase E is the only place this override applies; orchestration of the rest of the run still goes through the main session, not through showrunner.

## Q2. Tuning corpus scope

**Decision:** **s01 only.** The aggregate (`active-project/theater/proto-lines/s01.aggregate.md`, 900 numbered lines + 5 inline `# pov:` markers) and the per-episode split (`s01e01.md`–`s01e06.md`) are the corpus. Cross-season validation is deferred to a future R2 once s02 lands.

## Q3. Build /and-season-tune as a command up front?

**Decision:** **Ad-hoc this run.** Capture the actual flow as design docs under `design/shoot-v2/and-season-tuning-r1/`; command-ize after R1 produces working artifacts. Mirrors the /and-facets build trajectory (Step A → Step D → Step G → consolidation).

## Q4. Rubric source-of-truth

**Decision:** **Extract before Phase A.** /and-season's nine-pass review currently lives inline in the command body (`.claude/commands/and-season.md` lines 96–238) plus Phase 4 split criteria (lines 246–310). For this run, the locked rubric is `design/shoot-v2/and-season-tuning-r1/rubric-and-season.md` — a verbatim lift of the relevant sections, with the command-file hash captured above as anchor. The rubric does not move during this run; carry-back edits are queued for a future V2 in Phase H.

---

## Output location

All R1 artifacts under `design/shoot-v2/and-season-tuning-r1/`:

| File | Phase |
|---|---|
| `00-decisions.md` | this file |
| `rubric-and-season.md` | locked rubric for the run |
| `A-corpus.md` | Phase A corpus prep |
| `B-baseline.md` | Phase B reviewer baseline + gap analysis |
| `C-seams.md` | Phase C+D adversarial seams (per-persona + aggregated) |
| `E-defense.md` | Phase E defend/revise/withdraw decisions |
| `F-final.md` | Phase F final adjudication |
| `G-audit.md` | Phase G auditor 11-class scan |
| `H-carry-back.md` | Phase H rubric edit candidates |

Auditor report under `active-project/staff/auditor/season-tuning-r1-audit.md` (named with `-tuning-r1-` prefix to avoid colliding with prior `season-final-audit.md` slot from the packet draft, and with the existing nine-pass per-pass reports under the same dir).

---

## Commit cadence

One commit per phase. Branch: `claude/review-tuning-season-3YGPw`.

Push at end of run (or at any phase if user requests checkpoint).
