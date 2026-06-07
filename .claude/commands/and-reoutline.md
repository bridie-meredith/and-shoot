---
description: Intake a tentative outline (whole-book/series) into the and-experiment design track and adapt-or-retire the existing planning to receive it. A re-baseline, not a chapter note. Runs the OUTLINE-INTAKE RUNBOOK. Usage: /and-reoutline
---

Re-baseline the and-experiment plot planning around a **tentative outline** the principal brings.
This is the big-grain intake (a whole book/series draft that may supersede existing planning) — NOT
the single-chapter-note loop (`and-experiment/design/run-02/idea-inbox.md`).

**Execute `and-experiment/intake/INTAKE-RUNBOOK.md` verbatim.** Do not improvise a different process;
do not delete existing work (archive, never delete).

## Orientation (read in order)
1. `and-experiment/intake/tentative-outline.md` — the incoming draft (the dropbox). If it's still the
   empty template, ask the principal to paste the outline (or paste it for them), then proceed.
2. `and-experiment/intake/GUARDS-register.md` — ratified premises the new outline must be reconciled against.
3. `and-experiment/intake/reconciliation-worksheet.md` — the worksheet you fill in.
4. `and-experiment/intake/INTAKE-RUNBOOK.md` — the full phased process (this is authoritative).

## The shape (full detail in the runbook)
- **Phase 0** — receive + scope; settle the branch: **REVISION** (keeps premises, replaces structure)
  vs **REBOOT** (re-opens premises). Default REVISION; state the assumption.
- **Phase 1** — inventory existing artifacts; propose KEEP / ADAPT / SUPERSEDE / RETIRE.
- **Phase 2** — reconcile the outline against every GUARD/fence/invariant: HONORED / RE-RATIFY /
  CONTRADICTED. Surface contradictions; never break a GUARD silently.
- **Phase 3** — present dispositions + contradictions; get the principal's adapt-vs-remove rulings.
  **This is the one human gate.**
- **Phase 4** — migrate: create the next `design/run-NN/`, tokenize the adopted outline as canonical,
  carry over KEEP/ADAPT instruments, archive RETIRE/SUPERSEDE to `intake/retired/` with tombstones,
  re-found the state-ledger.
- **Phase 5** — `python3 scripts/check-threads.py <new-outline> --config <new-config>` → PASS;
  append a convergence-ledger round digest.
- **Phase 6** — one exit-summary block (branch, run-NN, disposition counts, GUARD changes, checker
  result, open forks, next step).

Provenance is sacred: archive, never delete; the `convergence/` baseline stays frozen.
