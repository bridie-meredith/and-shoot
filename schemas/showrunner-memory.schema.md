# Showrunner Memory Schema

Showrunner memory is series-scoped and cross-session. It is the index and fast-lookup layer that lets showrunner reconstruct a full working context at the start of any session, without reading every card or plan file from scratch.

File location: `active-project/staff/showrunner/memory.md`

Updated by showrunner at: episode close, season transitions, and after any significant planning decision.

Optimized for Claude, not for human reading. Keep entries compact — one line per item unless a pointer is needed.

---

## Format

```yaml
# showrunner memory

routing:
  show_file: active-project/theater/show.md
  episode_plan: active-project/theater/episode-plan.md
  series_plan: active-project/staff/showrunner/series-plan.md
  season_plan: active-project/staff/showrunner/season-<slug>-plan.md

series:
  theme: <one line — what this story is about>
  laws:
    - <non-standard physics, magic system, hard world rule — one line each>
  lore:
    - <background fact, history, what happened before — one line each>
  behaviors:
    - <character behavior constraint — one line each>
  plot:
    start: <one line — where the story begins>
    end: <one line — where the story ends or is heading>
    protagonist_arc: <one line — how the protagonist changes>
    series_question: <one line — central dramatic question spanning the whole story>
  cast_roster:
    - <actor-slug>: <one-line role description>
  stage_elements:
    - <location | prop | condition slug>: <one-line purpose in series>

seasons:
  - slug: s01
    status: active | complete | planned
    chunk: <one-to-two sentence chunk statement — what this season delivers to the series>
    episodes:
      - slug: s01e01
        status: written | active | planned
        chunk: <one sentence — what this episode delivers to the season>
    next_season_sketch: <one sentence only — horizon rule; no more than this>

active:
  season: s01
  episode: s01e01
```

---

## Field notes

**routing** — absolute paths from repo root to all active working files. Showrunner reads these at session open to locate the current show file, episode plan, and season plan without guessing.

**series.laws** — non-standard rules only. Standard physics doesn't need listing. One line per law; if detail is required, the pointer is `active-project/staff/showrunner/series-plan.md`.

**series.lore** — background facts that could cause a constraint violation if forgotten. One line per fact. Detailed lore lives in the series plan file.

**series.behaviors** — character behavior constraints that span the whole series. "X never kills unless provoked" level. Scene-specific behavior is on the actor's card.

**series.plot** — four one-line fields that hold the shape of the whole story. If these can't be expressed in one line each, the planning isn't done yet.

**cast_roster** — slugs of all actors in the series, with one-line role description. Not an episode-cast list — the full series roster.

**stage_elements** — locations, props, and conditions that appear across the series and carry narrative weight. Not every prop — only ones that matter to the long game.

**seasons** — one entry per season, planned or complete. The `chunk` is the chunk statement the season delivers to the series arc. The `next_season_sketch` is exactly one sentence — no more, per the horizon rule.

**active** — the currently running season and episode slugs. Updated at each episode close and each season transition.

---

## Companion file: series-plan.md

The memory file above is the index. The detail lives in `active-project/staff/showrunner/series-plan.md` — a prose document containing:
- Full law descriptions (where the one-line summary is insufficient)
- Full lore entries
- Full behavior constraint explanations
- Season drama descriptions
- Cast biographies (pointers to actor cards)

When showrunner needs detail beyond the one-line summary, it reads the series plan. The memory file is the fast path; the series plan is the authority.
