# Archived commands

Slash commands shelved out of `.claude/commands/` so the harness no longer surfaces them. Files preserved here (with full git history) for reference and potential reactivation.

## Contents

- `and-shoot.md` — full episode shoot orchestrator (pre-shoot-v2). Per-line shoot via coach + impersonator + audience review.
- `and-wrap.md` — pre-shoot-v2 manuscript finalizer (`show.md` consumer).
- `and-project-pre-substance.md` — pre-substance project activation. Owned scope + audience selection + series planning + per-season chunk authoring + series-level audit. Replaced by the trio `/and-project` (scope + staff) + `/and-series` (chunk + structure) + `/and-substance series` (signature + per-book Δ) + `/and-cast` (roster + audit). Series Plan section is the lift source for `/and-series` Phase 2-4; Phase 2 1c is the lift source for `/and-cast` Phase 1-4; Phase 3 Present-results is the lift source for `/and-cast` Phase 5.
- `and-season-dissolved.md` — pre-substance season orchestrator. Dissolved into `/and-substance` (chunker recursion at book/chapter/scene) + `/and-write` (bone-writing). Phase 1 is the lift source for `/and-substance` Phases 1-2; Phase 3 sweep-A is the lift source for `/and-substance` Phase 5; Phase 6 is the lift source for `/and-review verdict`; Pass S10 bone-gate is the lift source for `/and-write` Phase 6 substance bone-gate; Phase 7 emission is the lift source for `/and-write` Phase 7.
- `and-wrap-polish-deferred.md` — post-shoot-v2 editor pass (v2, URI-WRAP-V2). Polish concerns deferred entirely under the substance overhaul until upstream chain produces substantively-right drafts. Phase 1 (audience review) + Phase 2 (8-class auditor pass) + Phase 3 (editor allowed-moves contract + procedure) are the **un-defer lift targets** for `/and-review prose <chapter>` and any future polish revival. Do NOT mark as dissolved — the spec is the deferral artifact.
- `and-protolines-pre-substance.md` — pre-shoot-v2 two-phase proto-line authoring (the v1 protolines command). Superseded by `/and-protolines-v2` then by `/and-write` under the substance overhaul.
- `and-protolines-v2-lifted-to-and-write.md` — five-pass SVO-writer pipeline (v2). Lift source for `/and-write` Passes 1-5 verbatim (inventory → constraint → shape → trim → continuity).
- `and-protolines-season-v2-lifted-to-and-substance-cascade.md` — per-episode loop pattern. Lift source for `/and-substance --cascade`.

## Archive suffix conventions

- **`-pre-substance`** — overhaul or rename of a command that has a successor (`/and-project`, `/and-protolines`).
- **`-dissolved`** — command whose jobs migrated piecewise into other commands and isn't coming back as a standalone (`/and-season`).
- **`-polish-deferred`** — command whose spec is intentionally preserved for future revival (`/and-wrap`). The Phase 2 + Phase 3 specs are the un-defer lift targets.
- **`-lifted-to-<command>`** — command body is the primary lift source for a successor (`/and-protolines-v2` → `/and-write`; `/and-protolines-season-v2` → `/and-substance --cascade`). The archive copy is the canonical reference the implementer reads while writing the successor.

## 2026-05-17 — Substance overhaul

Two reasons. (1) The pre-substance chain optimized per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but had no declared substance contract; episodes shipped through it were structurally clean and substance-flat. (2) `/and-project` conflated scope with series content; `/and-season` conflated recursive chunking (book→chapter→scene) with bone-writing and emission; `/and-wrap`'s editor pass produced marginal lift on top of `/and-stitch`'s existing Phase 7 editorial reflection.

**Replacement chain:** `/and-project` (scope + staff) → `/and-series` (series chunk + structural prompts) → `/and-substance series` (signature + per-book Δ) → `/and-cast` (roster + series-level audit checkpoint) → `/and-substance book/chapter` (recursive chunker; three invocation levels; four chunk levels stopping at scene) → `/and-write` (scene-decomposition into bones-with-deltas + five-pass SVO + substance bone-gate; emits flat-integer-ID bones file + scene-map facet; replaces `/and-protolines`) → `/and-facets` (tensometer dropped; scene-map derivation downgraded to validation) → `/and-stitch` (tensometer-fallback removed from Phase 0; speaker-paragraph rule + scene-callout suppression added).

**The bone is the smallest substance unit** — it carries its own declared axis-movement; the former "beat chunk" planning level is collapsed into the bone itself. `/and-review` is the universal review primitive with subcommand router (includes `verdict <book>`, absorbing the former `/and-judge-book`).

**Dissolved:** `/and-season` (into `/and-substance` + `/and-write`); `/and-wrap` (polish concerns deferred entirely until upstream substance machinery is proven; `/and-stitch`'s `draft/<chapter>.md` is the terminal deliverable); `/and-judge-book` (into `/and-review verdict` — note this command was never written as a standalone; its content lived inside `/and-season.md` Phase 6).

**Renamed-overhauled:** `/and-protolines` → `/and-write`.

**URI-026 tens-gate replaced** by `/and-write` substance bone-gate; tensometer facet retired. See `design/substance/`.

## Reactivation

Each archived command can be restored by `git mv archive/commands/<name> .claude/commands/<original-name>` — but do not reactivate without a recorded decision in `design/`. Pre-substance commands are not directly compatible with the substance chain's showrunner-memory schema or the renamed bones path (`theater/bones/<book>-<chapter>.md` vs. `theater/proto-lines/<slug>.md`); reactivation requires schema-shim work.
