# shoot-v2

Workspace for redesigning the shoot phase of the and-shoot pipeline.

## Why

`/and-shoot` and `/and-wrap` have been archived (`archive/commands/`) as of 2026-05-06.

Trigger: review of `active-project/theater/s01e01-archive/show.md`. Audience flags rewrites on most of the first ~50 lines. Taylor's voice does not come through — the prose reads as competent Westerosi narration rather than her specific interiority. Planning quality is judged solid. The failure is downstream of the bullet plan.

A patch to the impersonator was rejected as insufficient. The shoot phase is being redesigned.

## Working thesis

1. **Move effort earlier.** The bulk of authoring work happens at proto-line construction, not at line-time generation. Proto-lines are SVO bones — single sentence, no modifiers — and pass through several review passes (delete, re-arrange, constraint-check, behavior-check, entertainment-check, etc.) before any prose is written.
2. **Split by concern.** Action proto-lines, dialogue, and facets (tension, interest, memory callbacks, loudness, feeling, metaphor, state, vibes) are authored as independent, citable artifacts. Dialogue in particular is authored per-character across an entire episode, with character card + memory + behavior card stack (per-character + universal/region/class shared cards) + critic + coach — no immersed impersonator. Behavior card carries voice samples, non-verbal tics, and memory-monument register.
3. **Stitch last.** The polished chapter is assembled from proto-lines + dialogue + selected facets only after each artifact has passed its own review. Stitching is its own phase.

## Layout

- `brainstorm.md` — user's seed thoughts, captured verbatim. Input to design, not output.
- `open-questions.md` — what the brainstorm raises but doesn't answer. Worked during design.
- (future) `pipeline.md`, schema drafts, command drafts.

## Status

Design phase. Not yet implemented. Active project state under `active-project/` is untouched; the in-progress s01e06 mid-shoot is paused (not resumable via `/and-shoot` since the command is archived — resumption path is whatever shoot-v2 produces).
