# Problems Log

Issues that impeded intended function during activation. Ordered by severity.

---

## P1 — Audience/dramatist review loops not recorded (BLOCKER for verification)

**Where:** and-plan.md steps 2 and 3 (series plan, season plan)
**What should happen:** Screen-writer produces plan; audience and dramatist run as parallel persistent subagents and return accept/revise verdicts; revisions iterate; both must accept (or 3-try budget exhausted) before plan is finalized.
**What happened:** Showrunner returned with no escalations, implying loops ran. But no verdicts were written anywhere. All three `active-project/audience/*/memory.md` files are empty stubs. There is no dramatist working memory location in the scaffold (dramatist is marked "stateless" in CLAUDE.md). There is no record of how many iterations ran, what feedback was given, or what the final verdicts were.
**Impact:** Cannot verify audience/dramatist acceptance. Human audit has no evidence to review.
**Fix applied:** Added a standing audience memory rule to the and-project planning dispatch: audience reads their STM before each review (for prior-feedback context) and writes session verdicts to `active-project/audience/<slug>/stm.md` after each planning loop completes. A step whose audience dispatch did not write STM is explicitly marked incomplete. Verdicts continue to go to the per-step log files as before; STM captures the accumulated feedback record across iterations.
**Status:** RESOLVED

---

## P2 — Formal series-level audit not run (BLOCKER for audit checkpoint)

**Where:** and-plan.md step 4
**What should happen:** Showrunner dispatches audience + dramatist + auditor for a formal pre-human-checkpoint review. Auditor returns a classified report (pass/flag/fault/escalate) to `active-project/staff/auditor/`.
**What happened:** Showrunner returned directly to the caller after season planning. `active-project/staff/auditor/` is empty.
**Impact:** The human audit checkpoint has nothing to review against. The series-level audit is the only required human gate; running it without the formal report means the gate is nominal.
**Fix applied:** The and-project command includes the formal series-level audit step with explicit log file requirement (`active-project/staff/auditor/series-audit.md`) and the "even a clean pass must produce a report" constraint. This was already in the command text; the problem was a showrunner skip. The explicit log file name and the clean-pass rule are the enforcement mechanism.
**Status:** RESOLVED (in command; watch for recurrence on next activation)

---

## P3 — Auditor constraint-consistency report not saved (step 1d)

**Where:** and-plan.md step 1d
**What should happen:** Auditor runs a constraint-consistency check on the full constraint card set; findings saved to `active-project/staff/auditor/`.
**What happened:** Showrunner acknowledged that auditor caught the Bonesaw ambiguity (which was resolved via law amendment). But no report file exists in `active-project/staff/auditor/`.
**Impact:** Audit trail broken. The amendment is in world-notes.md but the auditor's full finding is lost.
**Fix applied:** The and-project command includes the 1d log file requirement (`active-project/staff/auditor/1d-audit.md`) with "even a clean pass must produce a report." This was already in the command text; the problem was a showrunner skip. Same enforcement mechanism as P2.
**Status:** RESOLVED (in command; watch for recurrence on next activation)

---

## P4 — cards/locations/planetos/ subdir still exists (PATH MISMATCH)

**Where:** `cards/locations/planetos/` — three files:
- `forest-clearing-dusk.card.md`
- `westerosi-smallfolk-dwelling-interior.card.md`
- `westerosi-smallfolk-village-common.card.md`
**What should happen:** All location cards flat under `cards/locations/` (prior restructure decision per memory).
**What happened:** Old subdir was never cleaned up. `cards/locations/INDEX.md` lists these slugs as planetos-world entries without subdir path, so it treats them as flat. Agents reading the index and constructing paths as `cards/locations/<slug>.card.md` will 404.
**Impact:** Three existing location cards are unreachable by slug-based lookup.
**Fix applied:** All three files moved to `cards/locations/` root. `cards/locations/planetos/` subdir removed. INDEX.md already listed slugs without subdir prefix — no index change needed.
**Status:** RESOLVED

---

## P5 — Audience stm.md stubs missing

**Where:** `active-project/audience/cape-fic-reader/`, `worm-canon-pedant/`, `dark-fantasy-reader/`
**What should happen:** Each audience dir has a memory.md (done) and a stm.md stub.
**What happened:** stm.md files were not created. Margit.memory.md notes: "stm.md stub needed" for all three.
**Impact:** Audience agents reading their own STM will 404 on first reference.
**Fix applied:** stm.md stubs created in all three audience dirs with minimal-valid content (`# Audience STM — <slug>\nSTM:`). The and-project scaffold already specifies creating these stubs — the active-project was created before that spec was complete.
**Status:** RESOLVED

---

## P6 — No episode-start command exists

**Where:** `.claude/commands/`
**What should happen:** There should be an episode-start command (e.g., `/and-shoot` or `/and-episode-start`) that dispatches showrunner to run the episode-start pattern (screen-writer expands chunk, audience/dramatist review, cast and studio prepped, show file opened).
**What happened:** Only `/and-project` exists. Episode start is documented in and-plan.md but has no command entrypoint.
**Impact:** To start episode 1, showrunner must be dispatched manually with a bespoke prompt — no repeatable command, no format contract.
**Status:** RESOLVED — `/and-shoot` command exists at `.claude/commands/and-shoot.md`.

---

## P7 — Showrunner memory-read not enforced at dispatch time

**Where:** Every showrunner dispatch, including the one in and-project.md
**What should happen:** CLAUDE.md states "Showrunner memory is cross-session — memory.md is read at every session open." This means any showrunner dispatch must include an instruction to read `active-project/staff/showrunner/memory.md` before acting.
**What happened:** The and-project dispatch prompt does not include this instruction. During activation this was fine (memory was being built, not read). But subsequent dispatches — including episode start — will not automatically load series context unless the dispatch prompt explicitly tells showrunner to read the memory file. The showrunner agent has no self-executing behavior; it reads what the dispatch prompt tells it to read.
**Impact:** A showrunner dispatch in a new session without the memory-read instruction starts blank. Series continuity breaks silently.
**Status:** RESOLVED — `and-shoot.md` dispatch prompt opens with the memory-read instruction. `and-project.md` also includes it.

---

## P8 — /and-project command args not parsed from command line

**Where:** `.claude/commands/and-project.md` invocation
**What should happen:** First arg = title slug. Next args (middle) = brief (quoted). Last three = audience slugs.
**What happened:** User wrote `for a test spin, using this prompt: <brief>` with no slug or audience slugs on the command line. Title slug (`dead-capes-in-westeros`) and audience trio (`cape-fic-reader`, `worm-canon-pedant`, `dark-fantasy-reader`) were inferred from session memory. Would silently fail on a clean session.
**Impact:** Command is not reliably invocable without prior session context. A new user or new session would need to know to provide memory context separately.
**Fix applied:** The and-project command validates all five args on entry and prints usage + halts if any are missing or invalid. This was already in the command text at time of review — the original failure was a usage error, not a missing validation.
**Status:** RESOLVED (validation already present in command)

---

## P9 — hopefuls/ empty; candidate menu not saved

**Where:** `active-project/hopefuls/`; step 1c
**What should happen:** Margit produces a candidate menu; candidates not selected land in hopefuls/ for potential future use.
**What happened:** hopefuls/ is empty. No candidate menu was saved. No record of what was considered and passed over.
**Impact:** Low severity — doesn't break function. But the hopefuls pool as a feature is unused and its purpose isn't met.
**Note:** The and-project 1c step now saves the full menu to `active-project/staff/showrunner/1c-candidate-menu.md`. The hopefuls/ dir purpose is still ambiguous — it may be intended for mid-episode cast additions rather than activation leftovers. No fix applied pending a decision on what hopefuls/ is actually for.
**Status:** OPEN (low priority — decision needed on hopefuls/ purpose)

---

## Summary table

| # | Problem | Severity | Status |
|---|---------|----------|--------|
| P1 | Audience/dramatist verdicts not recorded | High | RESOLVED |
| P2 | Formal series-level audit not run | High | RESOLVED |
| P3 | Auditor 1d report not saved | Medium | RESOLVED |
| P4 | planetos/ subdir cards unreachable | Medium | RESOLVED |
| P5 | Audience stm.md stubs missing | Medium | RESOLVED |
| P6 | No episode-start command | Medium | RESOLVED |
| P7 | Showrunner memory-read not enforced | High | RESOLVED |
| P8 | Command arg parsing fails clean session | Medium | RESOLVED |
| P9 | hopefuls/ empty, menu not saved | Low | OPEN — decision needed |
