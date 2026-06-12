# Aggregate State Schema

Rolling forward-feed channel for cross-chapter narrative continuity. One file per project: `active-project/staff/showrunner/aggregate-state.md`. Records the *actually-true* state of the book at close of the most recently threaded chapter — axis state, open forward-hooks, character reader-legibility, terrain/calendar/prop state, and a revision-layer log of presentation-reinforcement edits applied post-stitch.

**Purpose.** Closes the upstream/draft divergence that the polish-deferred chain creates (see `staff/admin/process-proposals.md` PROP-0031). Replaces back-propagation with forward-feed: chapter-close threading edits and post-ship cohere convergence both emit here; downstream `/and-substance chapter` reads here and prefers it over book-chunk `handoff_in` predictions on conflict.

**Producers.** Two:
1. **`/and-stitch` Phase 10 (forward-thread)** — fires on every Phase 9 PASS or PASS-WITH-DEPTH-PASS-REQUIRED. Emits per-chapter close-state + any presentation-reinforcement revision-layer entries from the threading pass. Tags entries with `last_updated_by: and-stitch-phase-10`.
2. **`/and-cohere` Phase 6.5 (aggregate-emit)** — fires at PASS-COHERE on a converged stretch. Walks the stretch end-to-end and writes/updates the file with stretch-close state + any presentation-reinforcement revision-layer entries from the cohere iteration. Tags entries with `last_updated_by: and-cohere`.

When both producers have written entries, source is traceable per-entry via `last_updated_by`. Cohere may overwrite stitch-Phase-10 entries it disagrees with (cohere has cold-read advantage over a stretch); per-entry conflicts are logged in the entry's `conflict_log[]`.

**Consumer.** `/and-substance chapter b<NN>c<MM>` Phase 0 reads this file if present, in addition to `handoff_in` from `chapters[b<NN>c<MM-1>].handoff_out` in the book chunk. On conflict: aggregate value wins, conflict logged in the chapter chunk's metadata. On unacknowledged substantive revision-layer entries: HARD-aborts until principal acknowledges (stamps `acknowledged: true`).

**Fallback.** If this file does not exist (no cohere has run AND `/and-stitch` Phase 10 has not been implemented yet OR no chapter has been threaded yet — e.g., pre-c01), Phase 0 falls back to `handoff_in`-only behavior. Purely additive: presence enriches Phase 0; absence is identical to today.

**Lifecycle.**
1. First produced at `/and-stitch` Phase 10 of `c01` (initial state, no prior to read).
2. Updated at every subsequent `/and-stitch` Phase 10 success.
3. Optionally overwritten/revised at `/and-cohere` Phase 6.5 PASS-COHERE.
4. Read at every `/and-substance chapter` Phase 0 for c02+.
5. Survives book transitions: `through_book` advances on first-chapter emit of new book; prior book's close-state retained in `books[<prev>]` block.

---

## Format

```yaml
aggregate_state:
  version: 1
  project: <slug>                       # e.g. taylor-westeros-good-intentions
  through_book: <slug>                  # most recent book covered, e.g. b01
  through_chapter: <slug>               # most recent chapter close-state recorded, e.g. b01c07
  last_updated: <ISO timestamp>
  last_updated_by: and-stitch-phase-10 | and-cohere

  # Per-axis close-state at through_chapter.
  # One entry per axis in series.substance.state_axes[].
  axis_state:
    - axis: <slug>                      # e.g. moral_framework
      rank: <number>                    # current rank at chapter close (may be fractional, e.g. 4.5)
      start_rank: <number>              # from series.substance.state_axes[<axis>].start_rank
      delta_since_start: <number>       # rank - start_rank
      last_movement_at: <chapter-slug>  # most recent chapter the axis moved
      last_updated_by: and-stitch-phase-10 | and-cohere
      notes: <string|null>              # optional, e.g. "peaked c05 evening replay; held flat c06-c07"

  # Open forward-hooks: promises made but not yet paid.
  # Items removed only on payoff (stamped paid_at) or formal abandonment (stamped abandoned_at + reason).
  open_hooks:
    - hook_id: hook-<NNNN>
      description: <string>             # e.g. "Rushwick courier-attack thread filed at recurring-Rushwick-resident anchor"
      introduced_at: <chapter-slug>
      expected_payoff: <chapter-range>  # e.g. c08-c10, or null if unscoped
      status: open | paid | abandoned
      paid_at: <chapter-slug|null>
      abandoned_at: <chapter-slug|null>
      abandonment_reason: <string|null>
      last_updated_by: and-stitch-phase-10 | and-cohere

  # Characters with their accumulated reader-legibility through through_chapter.
  characters:
    - slug: <character-slug>            # e.g. wren-stitch-maker
      introduced_at: <chapter-slug>
      last_appearance: <chapter-slug>
      reader_legibility: high | partial | cipher
      legibility_notes: <string|null>   # what the reader knows; e.g. "name + occupation + Taylor's debt to her"
      last_updated_by: and-stitch-phase-10 | and-cohere

  # Terrain / location / prop / calendar state at chapter close.
  world_state:
    - key: <slug>                       # e.g. the-chandler-corner, calendar, the-feed-station
      kind: location | calendar | prop | condition
      state: <string>                   # e.g. "established as Halvard's recurring fixture corner"; "third-month-second-week, year of grace 174"
      last_changed_at: <chapter-slug>
      last_updated_by: and-stitch-phase-10 | and-cohere

  # Revision-layer log: presentation-reinforcement edits applied at /and-stitch Phase 10
  # or /and-cohere iteration that downstream chunkers need to treat as established.
  # Substantive edits do NOT land here — they surface as parking-lot HARD items
  # targeting upstream re-run (per PROP-0031 Amendment 2 Phase 10 Step 3c).
  revision_layer:
    - entry_id: rev-<NNNN>
      chapter: <chapter-slug>           # the chapter the edit applied to
      hunk_summary: <string>            # e.g. "added Wren chain naming at recognition moment (c06 line 7)"
      class: presentation-reinforcement | substantive
      acknowledged: <bool>              # principal-acknowledge for substantive entries; auto-true for presentation-reinforcement
      acknowledged_at: <ISO timestamp|null>
      applied_at: <ISO timestamp>
      applied_by: and-stitch-phase-10 | and-cohere
      target_consumer_chapter: <chapter-slug|null>  # the next chapter this should inform; null = general

  # Per-entry conflict log: when /and-cohere overrides /and-stitch-phase-10 entries,
  # or when /and-substance chapter Phase 0 detects aggregate vs handoff_in disagreement.
  conflict_log:
    - conflict_id: conf-<NNNN>
      detected_at: <ISO timestamp>
      detected_by: /and-substance chapter <slug> | /and-cohere | /and-stitch-phase-10
      conflict_type: aggregate-vs-handoff_in | cohere-overrides-stitch-phase-10 | stitch-phase-10-vs-prior-cohere
      description: <string>
      resolution: aggregate-wins | cohere-wins | held-for-principal
      affected_entries: [<entry refs into axis_state | open_hooks | characters | world_state | revision_layer>]

  # Optional per-book close-state archive for completed prior books.
  books:
    - book: <slug>
      closed_at: <chapter-slug>
      axis_state_at_close: [<copy of axis_state at book close>]
      open_hooks_at_close: [<open_hooks unresolved at book close>]

  # Consecutive-caveat circuit-breaker tracking (PROP-0048 / CLAUDE.md Rule 22).
  # Per defect-class counter: how many consecutive chapters the class has shipped as
  # PASS-WITH-DEPTH-PASS-REQUIRED without a depth-pass resolving it.
  # Updated at /and-stitch Phase 9 Step 4 (increment on PASS-WITH-DEPTH-PASS-REQUIRED;
  # reset to 0 on clean PASS). At consecutive_count > 2 the chapter is CIRCUIT-BREAKER-BLOCKED.
  design_inherent_tracking:                        # optional block; absent = no tracked classes yet
    - defect_class: <string>                       # e.g. "readability-axis-AIRLESS", "cluster:body-staging-gap"
      consecutive_count: <integer>                 # chapters since last clean PASS for this class
      last_incremented_at: <chapter-slug>          # most recent chapter that incremented this counter
      last_reset_at: <chapter-slug|null>           # most recent chapter that reset this counter; null if never
      auto_promoted_at: <chapter-slug|null>        # chapter where consecutive_count first exceeded 2; null if not yet
      principal_escalated_at: <chapter-slug|null>  # principal explicit acknowledgment; null until set out-of-band
```

---

## Conflict resolution rules

**Aggregate vs `handoff_in` (at `/and-substance chapter` Phase 0).** Aggregate wins. Conflict logged in chapter chunk metadata. Book-chunk `handoff_in` stays as historical prediction; not mutated.

**Cohere overrides stitch-Phase-10 (at `/and-cohere` Phase 6.5).** Cohere wins (cold-read advantage on stretch). Per-entry: the older entry is replaced; the conflict is appended to `conflict_log[]`. `last_updated_by` flips to `and-cohere`.

**Two stitch-Phase-10 entries on the same key.** Most recent wins (one chapter can update a key it previously emitted, e.g., terrain-state change). No conflict logged — this is normal accumulation.

**Two cohere entries on the same key.** Most recent wins. No conflict logged.

---

## Substantive vs presentation-reinforcement classification

Producers (`/and-stitch` Phase 10 + `/and-cohere`) classify each edit per the same scheme:

- **`cosmetic`** — sentence-rhythm, paragraph joins, redundancy cuts. No reader-facing new content. NOT logged to `revision_layer[]`.
- **`presentation-reinforcement`** — character callbacks, sensory anchors, calendar anchors, plant-establishing prose that reinforces but does not add substance. Reader-facing but no new axis-movement, no new declared events. Logged to `revision_layer[]` with `acknowledged: true` (auto), `class: presentation-reinforcement`.
- **`substantive`** — new events, new axis-movement, new opposing-force resolution, new character introduction, declared-fact reframe. **NOT applied at draft layer.** Surfaced as parking-lot HARD items targeting upstream re-run. If somehow a substantive entry does land here (e.g., from a prior session pre-policy or from an unusual `/and-cohere` iteration), `class: substantive` + `acknowledged: false` blocks the next chapter's `/and-substance chapter` Phase 0.

Producers MUST declare classification per edit. Uncertain-classification edits are held for principal acknowledge, not applied.

---

## Validation rules

1. `through_chapter` advances monotonically (chapter ordering = chapter slug ordering within a book; book advancement at first-chapter emit of new book).
2. Every `axis_state[].axis` must exist in `series.substance.state_axes[]`.
3. Every `open_hooks[].introduced_at` must be ≤ `through_chapter`.
4. Every `open_hooks[].paid_at` (if set) must be ≤ `through_chapter` AND > `introduced_at`.
5. Every `characters[].introduced_at` must be ≤ `through_chapter`.
6. Every `revision_layer[].chapter` must be ≤ `through_chapter`.
7. `revision_layer[].class: substantive` with `acknowledged: false` → blocks `/and-substance chapter <next>` Phase 0 (HARD-abort).
8. `conflict_log[]` is append-only. Resolution updates allowed; entry removal not allowed.
9. `design_inherent_tracking[].consecutive_count > 2` → `auto_promoted_at` MUST be stamped. Any entry with `auto_promoted_at` non-null AND `principal_escalated_at` null is circuit-breaker-blocked: the chapter may not ship without a depth-pass (which resets the counter on clean re-stitch) or explicit principal acknowledgment (which sets `principal_escalated_at`). `/and-review verdict` HARD-aborts if any chapter in the book scope carries an unresolved circuit-breaker entry.

---

## Compatibility with absence

If `aggregate-state.md` does not exist at `/and-substance chapter` Phase 0, behavior is identical to pre-PROP-0031 (`handoff_in` only). Presence is purely additive. This file should NOT be created speculatively — only by `/and-stitch` Phase 10 or `/and-cohere` Phase 6.5 on first PASS.
