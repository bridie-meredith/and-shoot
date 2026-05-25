---
description: Compose the substance-driven cast roster + fire the series-level audit checkpoint (the only blocking human checkpoint in the chain). Phase 1 substance-driven cast brief. Phase 2 margit candidate menu. Phase 3 screen-writer selection + dramatist viability. Phase 4 margit provisioning. Phase 5 audit checkpoint (y/N/feedback). Usage - /and-cast [revise|redo] [--retire <slug>]... [--add <slug>]... [--swap <old>=<new>]...
---

Authors `series.cast_roster` and fires the series-level audit checkpoint. The audit checkpoint is the only blocking human checkpoint in the chain — everything from `/and-substance book b01` onward is agent-resolved unless an escalation requires human decision.

You are the orchestrator. Dispatches: screen-writer, margit, dramatist, audience, auditor, fixer. All dispatches use the Agent tool.

Re-runnable. See `design/substance/rerun-protocol.md`.

## Args

```
/and-cast [revise|redo] [--retire <slug>]... [--add <slug>]... [--swap <old>=<new>]...
```

- `$1` (optional positional) — `revise` or `redo`. If omitted and roster populated, Phase 0 prompts.
- `--retire <slug>` (repeatable, revise mode) — retire the named actor; margit decommissions to `actors/<slug>-decommissioned-<timestamp>/`.
- `--add <slug>` (repeatable, revise mode) — add a new actor by persona-card slug.
- `--swap <old>=<new>` (repeatable, revise mode) — sugar for `--retire <old> --add <new>` in one pass.

---

## Phase 0 — Validate + mode select

1. Read `staff/showrunner/memory.md`. Confirm `series.chunk.path`, `series.chunk.prose`, `series.structure.*`, `series.substance.*` are populated. If any missing, abort: `/and-cast Phase 0 abort: <field> missing — run <upstream-command> first.` (Schema note: `series.chunk` is structured under `/and-series` v2; v1-compat consumers read `series.chunk.prose` for the string form.)
2. Inspect `series.cast_roster`:
   - **Empty:** proceed to fresh-authoring mode.
   - **Populated, `$1` = `revise`:** read `--retire` / `--add` / `--swap` flags if present, else prompt with current roster + multi-line entry block.
   - **Populated, `$1` = `redo`:** confirm with user; margit decommissions full current roster; Phases 1-4 re-run from scratch.
   - **Populated, `$1` omitted:** prompt `revise` / `redo`.
3. Cascade warning per `design/substance/staleness-cascade.md`. Any cast change stale-marks `project.series_audit` (the audit checkpoint must be re-approved before downstream can re-run).
4. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-cast` + `target.scope` slug-or-wildcard + `status: open`): HARD → abort unless this run resolves; SOFT → carry to Phase 7 summary. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.
5. Run.

---

## Phase 1 — Substance-driven cast brief

Dispatch **screen-writer** with:
- `series.chunk.prose` + `series.chunk.path` + `series.chunk.trajectory`
- `series.substance.*` (signature: state_axes, cost_ledger, antagonist_pressure, chunk_targets)
- `project.brief` + `project.constraints.*`
- `series.structure.*` (POV pattern affects narrator-carrier requirements)
- `series.laws`, `series.lore`, `series.behaviors`

**Screen-writer brief.** Compose a cast brief naming:
- Which axes need which carriers (protagonist for emotional / community / agency axes; antagonist for reputation / agency pressure; supporting cast for community + trust axes; world-perspective axes may need named institutional embodiments).
- Required role count per perspective.
- Tonal/voice register needs (the signature implies voice load — a story whose `community` axis is in motion needs cast members who carry community-presence; a story whose `agency` axis is pressured needs antagonists with institutional weight).

In **revise** mode, the brief is scoped to the requested `--retire` / `--add` / `--swap` delta only — not the full roster.

Output: `staff/showrunner/cast-brief.md`.

---

## Phase 2 — Margit candidate menu

Dispatch **margit**. Margit reads `cards/personas/INDEX.md` filtered by:
- World/canon fit (the brief's source-material if applicable).
- Tonal fit (per `cast-brief.md` voice register).
- Axis coverage (the brief's required carriers).

Margit produces a candidate menu — per-axis grouping, with 3–6 candidates per axis-slot. Save to `staff/showrunner/cast-candidate-menu.md`.

Skipped for actors being retired in revise mode.

---

## Phase 3 — Screen-writer selection + dramatist viability

1. Dispatch **screen-writer** with: cast-brief + candidate-menu + `series.substance.*` + (revise mode) current-roster delta.
   - Screen-writer selects per axis-slot.
   - Screen-writer reviews for dramatic range — does the selected roster cover the tension axes the series needs?
2. Dispatch **dramatist** in parallel to verify viability. Dramatist reads: proposed roster + `series.substance.*` + `series.structure.*`. Viability check: does the roster have carriers for every signature axis perspective? Are there any axis-orphans (signature axes with no named carrier)? Are there structural conflicts (multiple carriers wanting the same archetype)?

Standard accept/revise loop (3-try cap). On the third revise, ship with reviewer flags annotated and proceed.

In revise mode, dramatist verification considers the **full post-revise roster** (untouched + added + swapped — minus retired), not only the added actors.

---

## Phase 4 — Margit provisioning

Dispatch **margit** for each actor in the final roster. Per actor:

1. Create `active-project/actors/<slug>/` directory. **Dir name MUST match the card's `name` field** — variant cards use the variant slug.
2. Copy `cards/personas/<slug>.md` → `active-project/actors/<slug>/card.md`.
3. Write `active-project/actors/<slug>/{ltm,stm,state,vibes}.md` stubs per `schemas/memory.schema.md`.
4. Populate `vibes.md`. Read the card + series vibe-cloud. Derive personal vibe-cloud:
   - Which world keys does this character activate?
   - What are their private associations?
   - For characters with defined power/ability mechanics: add a vibe key encoding how the power presents (ambient vs directed, cost signature, what it is NOT).
   - For characters arriving from source material with significant audience weight: reflect what they are carrying from history, not only situation at story open.

In **revise** mode:
- Added actors: full fresh provisioning (steps 1-4).
- Retired actors: decommission. Move `active-project/actors/<slug>/` → `active-project/actors/<slug>-decommissioned-<timestamp>/`.
- Untouched actors: left as-is.

In **redo** mode: full decommissioning of every current actor before fresh provisioning of the new roster.

Write final roster to `series.cast_roster` in showrunner memory:
```yaml
cast_roster:
  - slug: <actor-slug>
    role: <one-line role description from screen-writer brief>
    perspective: protagonist | antagonist | supporting | world
```

Margit logs all provisioning + decommissioning to `staff/margit/margit.memory.md`.

---

## Phase 5 — Series-level audit checkpoint

This is the **only blocking human checkpoint** in the chain.

Dispatch **auditor** (fork) against the full picture:
- `project.brief` + `project.constraints.*`
- `series.chunk.path` + `series.chunk.trajectory` + `series.chunk.prose` + `series.structure.*`
- `series.substance.*` (signature + cost ledger + antagonist pressure)
- `series.laws`, `series.lore`, `series.behaviors`
- `series.cast_roster` (just-finalized)
- `series.vibe_cloud`

Auditor produces a classified report per `schemas/audit-report.schema.md`. Save to `staff/reviews/series-audit-<timestamp>.md`.

Phase 5 ends with the binary prompt:

```
Series-level audit complete. <N> findings (<H> HARD, <S> SIGNAL, <T> TASTE).
Report: staff/reviews/series-audit-<timestamp>.md

Approve and proceed? [y/N/feedback]
```

**On `y`:**
- Persist `project.series_audit.{approved_at: <iso-timestamp>, approved_by: user, report_path: <path>, stale_since: null}` to showrunner memory.
- Print: `Series audit approved. next: /and-substance book b01`.
- Exit cleanly.

**On `N` (default, including empty input):**
- Exit without approval. `project.series_audit.approved_at` stays null.
- Print: `Series audit not approved. Review the report, then run /and-cast revise / /and-substance series revise / /and-series revise as appropriate. /and-substance book b01 cannot run until approval lands.`

**On `feedback`:**
- Open a free-text entry. User types notes. Notes save to `staff/reviews/series-audit-<timestamp>-feedback.md`.
- Print: `Feedback recorded at <path>. Run the appropriate revise command; that command will read the feedback file.`
- Exit.

---

## Re-run notes

- `revise` without flags enters interactive editor mode: prints current roster, accepts a multi-line block (`retire: <slugs>`, `add: <slugs>`, `swap: <old>=<new>`).
- `revise` scopes Phase 1's brief, Phase 2's candidate menu, and Phase 3's selection to the delta. Phase 3's dramatist viability check considers the full post-revise roster. Phase 5 audit must re-approve.
- `redo` is destructive: full decommissioning of the existing roster. Use sparingly.
- Any cast change (revise or redo) stale-marks `project.series_audit` per `design/substance/staleness-cascade.md`.
- `/and-substance book b01` Phase 0 HARD-aborts if `project.series_audit.approved_at` is missing or `stale_since` is set.
