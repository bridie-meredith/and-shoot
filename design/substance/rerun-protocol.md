# Re-run Protocol — Phase 0 Shared Shape

Every re-runnable command (`/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review`) implements the same Phase 0 shape. This doc is the canonical reference; per-command specs reference this file rather than duplicating it.

`/and-project` is the **exception** — it hard-aborts on existing scope. Project scope is foundational; revising it requires a new project.

---

## Phase 0 — four steps

1. **Read upstream inputs.** Abort if upstream is missing or incomplete. The abort message names the missing field + the upstream command that produces it. Example: `/and-substance book b01 Phase 0 abort: project.series_audit.approved_at is missing — run /and-cast Phase 5 first.`

2. **Check own output.** Inspect showrunner memory for the block this command writes. If empty, proceed to fresh-authoring mode. If populated, prompt for re-run mode (see below).

3. **Cascade warning + staleness-marking.** If downstream artifacts derive from the about-to-change output, surface them (see `staleness-cascade.md`). Default action is `mark-stale`. User may pick `keep-fresh` or `abort`. Choice is recorded in `staff/showrunner/staleness-log.md`.

4. **Run.** Enter the command's authoring phases.

---

## Re-run modes

Three verbs, used consistently across all re-runnable commands:

| mode | semantics |
|---|---|
| `revise` | Refine in place. Same children/scope; retune contracts, regenerate prose, address review feedback. Existing slugs preserved; flat IDs preserved where applicable. |
| `add` | Append new sub-units without touching existing ones. Only meaningful where the output is a list (chunkers that produce child chunks; `/and-cast` adding actors). Next index continues monotonically. |
| `redo` | Replace all children. Existing set is preserved as prior (e.g. decommissioned actor dirs, archived cards) so the user can compare; new authoring runs from scratch. |

Not every command supports all three. The per-command spec lists which modes apply.

---

## Mode syntax (G2 — positional + interactive prompt, both supported)

Every re-runnable command accepts the mode as an optional positional argument after the subject slug, OR via interactive Phase 0 prompt when omitted:

| invocation | behavior |
|---|---|
| `/and-write b01c01` | If output exists, Phase 0 prompts `revise` / `redo`; user picks. |
| `/and-write b01c01 revise` | Mode preselected; Phase 0 prompt skipped; goes straight to scope-selection. |
| `/and-write b01c01 redo` | Mode preselected; Phase 0 prompt skipped. |
| `/and-cast`, `/and-cast revise`, `/and-cast revise --retire <slug>` | Same pattern; flags layer on top of positional mode. |
| `/and-substance series add` | `add` mode (chunkers that support `add`). |

---

## Mode-specific extras

**`/and-write revise` — `--from-signals` flag.** When the prior `/and-write` run recorded SIGNAL-classified bone-gate findings, `--from-signals` (or, by default at Phase 0, an interactive prompt when SIGNALs are present) scopes revise to only the SIGNAL-flagged bones / scenes. The user can pick any subset. Without the flag, revise scopes to explicitly-named scenes or bone ranges.

**`/and-write revise` — per-scene gate-verdict clear.** Phase 0 clears `gate_verdict` only on bones inside scenes scoped by the revise target. Scenes not in scope keep their prior `gate_verdict.bonefide: true` / `flat: false`. Phase 6 re-runs the bone-gate against the union of (revised scenes' new bones) + (unchanged scenes' existing bones), but only the revised-scene bones can produce new gate_verdict writes.

**`/and-cast revise` — `--retire` / `--add` / `--swap` flags.** Drives scripted revise without an interactive editor. In the absence of flags, Phase 0 enters an interactive editor that prints the current roster and accepts a multi-line block. Retired actors are decommissioned by margit to `actors/<slug>-decommissioned-<timestamp>/`. Added actors get fresh provisioning. Untouched actors are left as-is.

**`/and-cast redo`** — margit decommissions the full current roster; Phases 1-4 re-run from scratch.

**`/and-substance series redo`** stale-marks every `books[*]` block downstream. `/and-substance book b01 redo` stale-marks every `chapters[*]` under b01. `/and-substance chapter b01c01 redo` stale-marks every `/and-write` bones file whose source scenes sit under b01c01.

---

## Verdict invalidation

Any `/and-substance` or `/and-write` re-run scoped at-or-under a book that already has an `orchestrator_critic_verdict.ruling` set MUST stale-mark that verdict block (`books[<slug>].orchestrator_critic_verdict.stale_since: <iso-timestamp>`). A PASS verdict sitting on top of substance that has been redone underneath is a false signal; the stale flag forces re-judgment via `/and-review verdict <book>` before the verdict is trusted again. `/and-review verdict` Phase 0 warns (not blocks) if it sees an existing stale verdict; re-running it clears the stale flag on PASS/PASS-WITH-NOTES/FAIL re-issue.

---

## Idempotent commands

`/and-review` is idempotent. Any subcommand can be re-fired any number of times. Each invocation persists a new timestamped report; nothing else is mutated. The `verdict` subcommand updates `books[<slug>].orchestrator_critic_verdict` in place.

`/and-stitch` and `/and-facets` are re-runnable but not idempotent — re-running re-runs the full pipeline phases and overwrites their outputs. Phase 0 resets `chapters[].status` to the earliest value the command owns; staleness-cascade rules apply.
