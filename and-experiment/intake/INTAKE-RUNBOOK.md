# OUTLINE-INTAKE RUNBOOK

**For Claude, in a fresh session.** When the principal brings a **tentative outline** (a whole-book
or whole-series draft — not a single chapter note) and wants to **adapt or remove the existing
run-02 planning** to receive it — run this protocol. Do not improvise a different process; do not
silently discard existing work.

Trigger phrases: "here's a tentative outline" · "intake this outline" · "rework the planning around
this" · "adapt or remove the existing planning" · `/and-reoutline`.

> **Not this runbook:** a single messy chapter *note* → use `design/run-02/idea-inbox.md` (the
> small-grain loop). This runbook is for a **re-baseline**: a new outline that may supersede the
> chapter structure (and possibly the premises) wholesale.

---

## 60-second orientation (read in order, stop when you can act)

1. **`intake/tentative-outline.md`** — the principal's incoming draft (the dropbox). Read it first;
   note its **scope** (full series / one book / fragmentary) and whether it carries chapter headers.
2. **`intake/GUARDS-register.md`** — the ratified premises the incoming outline must be checked
   against (era, cultivation rules, fences, structural invariants).
3. **`intake/reconciliation-worksheet.md`** — the per-artifact disposition + GUARD-reconciliation
   worksheet you will fill in. If a prior intake started, its in-progress worksheet is here.
4. **`design/run-02/README.md`** — what the current working layer is and how it's organized.
5. `git log --oneline -12` — recent CL-/intake history.

If `intake/tentative-outline.md` is still the empty template: the outline hasn't been dropped yet —
ask the principal to paste it (or paste it for them), then proceed.

---

## The two branches (settle FIRST — Phase 0)

Ask the principal one scoping question before touching anything:

- **REVISION** — the new outline keeps the ratified **premises** (GUARDS: era, cultivation rules,
  family, fences) and replaces / reshapes the **chapter structure**. → GUARDS carry over; reconcile
  structure only.
- **REBOOT** — the new outline **re-opens premises** too. → Each GUARD is back on the table; expect
  RE-RATIFY / DROP decisions in Phase 2.

Default if unstated: **REVISION** (cheaper, preserves hard-won ratifications). State the assumption,
let them override.

---

## Process

### Phase 0 — Receive & scope
- Confirm the outline is in `intake/tentative-outline.md` (capture it there if pasted in chat).
- Record: scope, granularity, and the branch (REVISION / REBOOT).
- **Nothing is changed or deleted in this phase.**

### Phase 1 — Inventory & propose dispositions
Walk the **Artifact manifest** (below). For each existing artifact, propose one disposition against
the new outline, into the worksheet:
- **KEEP** — still correct as-is.
- **ADAPT** — mostly right; needs edits to match the new outline.
- **SUPERSEDE** — replaced by a new artifact the intake will create.
- **RETIRE** — no longer applies; archive (never delete).

### Phase 2 — GUARD reconciliation
For every entry in `GUARDS-register.md`, mark the new outline as **HONORED / RE-RATIFY / CONTRADICTED**:
- HONORED → carry it forward unchanged.
- RE-RATIFY (REBOOT) / CONTRADICTED (any branch) → **surface to the principal**; on their ruling,
  write a **new GUARD** (supersedes the old, old kept in history). A contradiction is never applied
  silently. Also re-check the **hard fences** and **structural invariants** the same way.

### Phase 3 — Reconcile with the principal (decision gate)
Present: (a) the disposition table, (b) the GUARD reconciliation, (c) every contradiction needing a
ruling. Get adapt-vs-remove decisions. **This is the one human gate** — migration waits on it.

### Phase 4 — Migrate (after sign-off)
- **Establish the new working layer**: create the next `design/run-NN/` (run-02 → run-03 …). The
  adopted outline becomes its canonical `book-<x>-outline.md` (or `series-outline.md`), **tokenized**
  for the checker — chapter headers `### <Book>.<n> · <slug>`, `PLANT[...]`/`FIRE[...]`, `Rung Rk`
  lines, and forward-bridge stubs so the causal graph closes.
- **Carry over** KEEP/ADAPT artifacts (copy + edit): GUARDS register → new run's GUARD section;
  thread-config (adapt the aliases / plant-only / payoff-only to the new token set); timeline/family
  if premises held.
- **Archive** RETIRE/SUPERSEDE artifacts to `intake/retired/<date>-<name>/` with a one-line
  tombstone (what it was, why retired, what replaced it). **Do not delete.** The frozen
  `convergence/` baseline is never edited — leave it as the historical record.
- Re-found or migrate the **state-ledger** (the change-propagation/working-memory instrument) onto
  the new structure; start its change-log at the intake entry.

### Phase 5 — Verify
- Run the checker on the new outline:
  `python3 scripts/check-threads.py <new-outline> --config <new-config>` → must **PASS**
  (orphans / unplanted fires / gift→spend order / R0–R4 present).
- Append a reconciliation digest to `convergence/convergence-ledger.md` (next Round N) recording the
  intake: branch, dispositions, GUARD changes, what was retired, checker result.

### Phase 6 — Exit summary (one block)
Report: branch taken · new run-NN created · KEEP/ADAPT/SUPERSEDE/RETIRE counts · GUARD changes (with
new GUARD IDs) · checker PASS/FAIL · open forks still pending · suggested next step.

---

## Decision rules
- **Provenance is sacred.** Archive, never delete. The `convergence/` baseline stays frozen; every
  retired run-02 artifact lands in `intake/retired/` with a tombstone.
- **Premises beat structure.** A GUARD contradiction is escalated and ratified before any structural
  migration proceeds (Rule: convergence-process "ratify smuggled premises explicitly").
- **The new outline is allowed to be tentative.** Tokens/rungs can be *added during migration* — you
  don't reject a draft for missing PLANT/FIRE tags; you tokenize it as part of Phase 4.
- **Reuse > rebuild.** Prefer ADAPT over SUPERSEDE; only RETIRE what genuinely no longer applies.
- **One human gate** (Phase 3). Everything before it is read-and-propose; everything after is
  execute-and-verify.

---

## Artifact manifest (current planning + default disposition)

*Defaults assume the **REVISION** branch; a REBOOT will push several toward ADAPT/RE-RATIFY.*

| Artifact | What it is | Default disposition |
|---|---|---|
| `convergence/chapters/round-02/fusion.md` | frozen 30-ch baseline (pre-run-02) | **KEEP** (frozen, never edit) |
| `convergence/convergence-ledger.md` | cumulative ratification record | **KEEP** (append the intake round) |
| `design/run-02/book-i-outline.md` | re-fused clean Book I (11 ch) | **ADAPT → SUPERSEDE** by the new outline's Book I |
| `design/run-02/book-i-state-ledger.md` | state + blast-radius + CL log + GUARDS + bridge | **ADAPT** (migrate to new run; carry GUARDS + entity registry) |
| `design/run-02/timeline-and-family-tree.md` | era + family + magic rules | **KEEP/ADAPT** (KEEP if premises hold; ADAPT on RE-RATIFY) |
| `design/run-02/thread-config-book-i.txt` | checker config for the re-fused outline | **ADAPT** (to the new token set) |
| `design/run-02/thread-config.txt` | checker config for the frozen baseline | **KEEP** (pairs with the frozen baseline) |
| `design/run-02/idea-inbox.md` | small-grain chapter-note front door | **KEEP** (still the note loop) |
| `intake/GUARDS-register.md` | ratified-premise snapshot | **ADAPT** (update as GUARDs change) |
| `design/run-01/*`, `design/cultivation-library/*` | bible / source material | **KEEP** (reference) |
| `design/counterfactual-life/*` | exterior-well source material (Gael's ordinary princess life — servants / day / expectation-script + the seam map) | **KEEP** (reference; additive — carry forward frozen) |
| `design/counterfactual-baseline-process.md` | reusable negative-space-worldbuilding process | **KEEP** (process doc) |
| `scripts/check-threads.py` | mechanical thread checker | **KEEP** (tool) |

*(Refresh this table at the start of each intake; the repo may have moved on.)*

---

## Scaffold map (`intake/`)
- `INTAKE-RUNBOOK.md` — this file.
- `README.md` — one-screen orientation + pointer here.
- `tentative-outline.md` — the dropbox (with a format guide). The principal pastes here.
- `reconciliation-worksheet.md` — the per-artifact + GUARD worksheet you fill in.
- `GUARDS-register.md` — ratified-premise snapshot to reconcile against.
- `retired/` — created on first retirement; archived artifacts + tombstones.
