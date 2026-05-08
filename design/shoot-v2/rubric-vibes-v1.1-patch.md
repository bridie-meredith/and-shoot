# Vibes-Updates Rubric — V1.1 Patch

Applied to: `design/shoot-v2/rubric-vibes.md` (V1 LOCKED 2026-05-07)
Patch authored: Phase 4 (post-RF-001 resolution + Phase 3 seam findings)
Ship protocol: V1.1 text ships same commit as Phase 5 facet file, per schema-revision-at-ship pattern.

---

## Patch 1 — §"Required gates" gate 2 amendment: pre-seeded project behavior

**Location:** §"Required gates", gate 2 (Op coherence), after the existing three-bullet list.

**Add the following sub-clause:**

> **Pre-seeded projects.** Where world-build or project-activation populates vibe-cloud files (`actors/*/vibes.md`, `staff/studio/vibes.md` EPISODE_N_VIBES / SEASON_N_VIBES / SERIES_VIBES sections) prior to the first episode's facet authoring, those bundles constitute authoritative existing state at the time of facet authoring. Gate 2 applies to all targets without exception — including episode-scope, season-scope, and series-scope targets. Pre-loaded = present. `+` on a pre-loaded keyword is AP5 regardless of whether the pre-loading occurred via world-build or via prior episode authoring.
>
> In pre-seeded projects, the predominant episode-facet operations are:
> - `++` — extend a pre-loaded keyword with genuinely on-screen-licensed non-duplicate tokens
> - `+` — fresh add on targets whose vibe-sets do not yet carry the keyword (empty entity vibe-sets: locations, props, actors not yet pre-loaded)
> - skip — if the pre-loaded bundle already covers the event's full qualitative-consequence range and on-screen beats add no non-duplicate tokens
>
> The showrunner must check each target's cloud file before firing any `+` entry. The check is required for actor targets AND episode/season/series scope targets. Failure to extend the gate-2 check to episode-scope targets is the specific failure mode identified in Phase 2 (RF-001).

---

## Patch 2 — §"Anti-patterns" AP8 amendment: sentence-parsability as the formal test

**Location:** §"Anti-patterns", AP8 entry. Replace the current AP8 text with:

> **AP8 prose-token.** Full-sentence tokens, soft connectives, narrator-voice prose. Tokens are hyphenated word-algebra only. Multi-clause-as-token forbidden.
>
> **The formal test is sentence-parsability, not token length.** A token is AP8 if it can be parsed as a complete sentence with a standalone subject, finite verb, and object — regardless of how it is hyphenated. Length is a heuristic signal, not a gate. Long word-algebra compressions are not automatically AP8. Examples:
>
> - `the-cost-of-what-she-built-made-visible-to-strangers` (9 segments) — noun-phrase with participial modifier; reads as a noun-phrase not a sentence; PASS.
> - `the-door-she-can-open-after-the-machine-leaves` (9 segments) — noun-phrase with relative + temporal clause compressed; no standalone main predicate; reads as a noun-phrase; PASS.
> - `the-officer-was-efficient-and-she-knew-it` — sentential; subject (`the-officer`) + finite verb (`was`) + coordinate clause; FAIL.
> - `efficient-not-hostile` (3 segments) — compressed predicate-nominative; PASS.
>
> **Advisory for long tokens (8+ segments):** The token must be a single noun-phrase with compressed modifiers (participial, prepositional, relative, as-predicate). A sequence of two independent compressed clauses joined by a hyphen is AP8 even if individually each clause is short. The test is always: "Can this token be parsed as a sentence with a main predicate?" If yes, refuse.
>
> **AP13 cross-reference:** AP13 (prose-narration-in-tokens) is a stricter form of the same gate — a token that reads as a sentence the narrator might say fails AP8 by construction. AP8 is the formal gate; AP13 is the prose-register sub-test.

---

## Patch 3 — §"Anti-patterns" AP11 amendment: formal/advisory split

**Location:** §"Anti-patterns", AP11 entry. Replace the current AP11 text with:

> **AP11 token-overlap on `++`.** Tokens appended via `++` that duplicate tokens already in the existing bundle.
>
> **Formal gate (mechanic-checkable):** string-overlap. The token-set difference required is exact-string. A new token that shares no string with any existing bundle token passes the formal AP11 gate.
>
> **Advisory (author responsibility, not a mechanic gate):** Where new tokens are semantically adjacent to existing tokens — same qualitative register, different event-frame — the author should verify that the event-frames are genuinely distinct and that a downstream operator would generate different behavior from the new token versus the existing one. If the operator would generate identical behavior, the new token is a semantic duplicate and should be refused even though it passes the string test. When semantic-adjacency is present, authors may add a comment-line justifying the event-frame distinction.
>
> The formal string-overlap test governs mechanic review. The semantic-adjacency advisory governs authoring quality and Phase 5 review. A token that passes string-overlap but fails semantic-adjacency advisory is a soft flag, not a formal fault.

---

## Patch 4 — §"Cross-facet contract" addition: pre-render hazard clause

**Location:** §"Cross-facet contract", end of the section (after the final existing bullet). Add:

> **Pre-render hazard — `++` extensions from locked upstream facets.**
>
> `++` extensions authored in the vibes-updates facet may derive their licensing events from locked upstream facets (state-updates, memory-flags, feeling-flags). These upstream facets were authored BEFORE the vibes-updates facet. The question: do vibes-updates `++` extensions retroactively require those locked facets to be re-run?
>
> **No.** The vibes-updates facet is a write-side product; it records operator-bias state. The locked upstream facets are content-layer authority for their own scope. The two layers do not conflict:
>
> - Locked upstream facets (state-updates, memory, feeling) are authoritative for what happened on-screen in the episode.
> - The vibes-updates facet is authoritative for what operator-bias state each target carries after the episode.
> - A stitcher reading both simultaneously receives content-layer authority (from locked facets) and bias-layer context (from vibes-updates). Where they address the same event, they address different aspects of it. No retroactive invalidation occurs.
>
> `++` extensions do NOT retroactively change what locked upstream facets should have produced. The `++` extension is a write-side bias for FUTURE renders and FUTURE episode operators (s01e02+). It does not alter the s01e01 locked facet record.
>
> The locked facets remain canonical for s01e01. Showrunner does not re-run, re-review, or re-file locked facets on the basis of vibes-updates `++` extensions.

---

## Summary of changes

| Patch | Location | Type | Seam resolved |
|---|---|---|---|
| 1 | §"Required gates" gate 2 | Addition (sub-clause) | RF-001 — world-build pre-load behavior |
| 2 | §"Anti-patterns" AP8 | Replacement | SEAM 6 — AP8 formal test commitment |
| 3 | §"Anti-patterns" AP11 | Replacement | SEAM 4 — string-overlap vs semantic-overlap split |
| 4 | §"Cross-facet contract" | Addition | SEAM 7 — pre-render hazard clause |

No other V1 text is changed. All V1 gates, anti-patterns, functional registers, sparsity/volume guidelines, and author-privilege clauses remain in force.
