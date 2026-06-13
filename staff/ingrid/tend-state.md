# /and-tend — work-queue + cadence ledger

The state that lets `/and-tend` run several times a day without redoing work. Cadence is decoupled from frequency: each scan-class has a cadence; each run drains what's *due* within budget. Edit the cadences here to retune — no command-body edit needed.

Read by `/and-tend` Phase 0; written by Phase 4. Owned by ingrid; format owned by oskar.

---

## Config

```yaml
budget_default: 12          # max dispatches per run
defer_on_cascade: true      # skip state-writing modules while a chapter cascade is in flight
```

## Scan-class cadences + last-run

```yaml
scan_classes:
  - id: taxonomy_audit        # artur — cards/ drift (6 sub-scans)
    cadence: 7d
    last_run: null
  - id: index_sweep           # artur — INDEX integrity
    cadence: 7d
    last_run: null
  - id: stm_sweep             # artur — agent-memory bloat / prepend-roll
    cadence: 3d
    last_run: null
  - id: parking_lot_hygiene   # artur — parking-lot schema hygiene
    cadence: 1d
    last_run: null
  - id: state_sync            # artur — state-file structural reconciliation
    cadence: 3d
    last_run: null
  - id: proposal_triage_prep  # read process-proposals: deferred-past-date / rising recurrence
    cadence: 1d
    last_run: null
  - id: pattern_promotion     # oskar patterns.md at/over threshold
    cadence: 1d
    last_run: null
  - id: persona_efficiency    # margit — card-bloat trim
    cadence: 14d
    last_run: null
  - id: forge_editor          # /and-forge editor — when new draft signal accrued
    cadence: 14d
    last_run: null
  - id: forge_fixer           # /and-forge fixer (revisor)
    cadence: 14d
    last_run: null
  - id: retrospective         # ingrid — also event-driven at book/series close
    cadence: book-boundary
    last_run: null
```

## Carried work queue

```yaml
queue: []   # items surveyed-but-not-yet-drained; each: {id, finding, route, impact_cost, status: open|resolved}
```

## Run history (tail)

```yaml
runs: []    # each: {ts, modules_ran, findings, fixed, forge, proposals, escalates, budget_used, outcome}
```

---

(seeded 2026-06-13; first run will stamp last_run values.)
