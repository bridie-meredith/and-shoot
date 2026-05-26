# Persona-Exemplar Schema

Persona-exemplars are concrete demonstrations of a persona's voice/output in known-good form. They are paired with persona cards (the biography layer) and consumed by agents at dispatch as the **live channel** for voice/output-shape.

Schema authority: this file. Provenance: PROP-0005 / DEC-0016 (2026-05-26), narrowed by PROP-0005-A / DEC-0017 to Tier 1 consumers (voice/judgment-driven agents).

Cross-reference: `schemas/card.schema.md` — the biography layer that persona-exemplars complement.

---

## Architectural premise

A persona card describes the persona at-rest: identity, values, taste, fences, history. The card is authoritative for **identity and fences**.

A persona-exemplar shows the persona in motion: how they actually speak, notice, render, judge. The exemplar is the **live channel** that agents pattern-match against during dispatch.

The split exists because two empirical findings converged in the 2026-05-26 exemplar experiments:

1. **Showing beats describing for voice/judgment-driven consumers.** Renderer, impersonator, and audience all produced sharper output when primed with a concrete exemplar passage than when given an additional description layer on top of their card.
2. **Description-priming on top of an already-rich card causes bloat and over-performance.** The agent demonstrates the described features rather than executing flat — a measurable regression in three of three voice-consumer experiments.

The card's voice and forbidden-registers sections remain authoritative for what the persona *cannot* do. The exemplar augments by showing what they *can* do, in a form that transfers grammar and cadence directly.

---

## Scope (Tier-1)

Per PROP-0005-A / DEC-0017, persona-exemplars are dispatched to:

- **Impersonator** (character-voice primitive) — exemplar passages of the character in-voice. Library at `cards/persona-exemplars/<actor-slug>.md`.
- **Audience** (3-persona reviewer trio + taste-judge override) — exemplar passages of the reviewer in live-read cadence. Library at `cards/persona-exemplars/<audience-slug>.md`.
- **Renderer voice** (PROP-0003-A) — series-level voice exemplar at `active-project/voice-exemplar.md` (project-bound, not library-bound) with optional per-chapter override at `active-project/theater/voice-exemplar-<chapter-slug>.md`. Not a persona-exemplar per this schema; uses a parallel one-passage format. See `.claude/commands/and-stitch.md` Phase 0 step 4a for wiring.

**Tier-2 (deferred):** orchestrator-critic, dramatist, auditor, editor. These are template/structure-driven consumers. The critic experiment found that prose-voice-leading exemplars actively regress structure-driven output. A future Tier-2 exemplar sub-class (template-conforming, not prose-voice-leading) requires its own experiment before dispatch.

**Tier-3 (out of scope):** showrunner, margit, fixer. No persona/voice channel to prime.

---

## Frontmatter

```yaml
---
name: {{slug}}-exemplar
persona-ref: {{persona slug — must match a card in cards/personas/ or active-project/audience/}}
class: persona-exemplar
purpose: {{one-line statement of what the exemplar primes for}}
content-match: {{high | medium | low}} ({{one-line description of the scene/context demonstrated}})
authored-by: {{author identity — claude, principal, or other}}
length: ~{{N}} words
fences:
  - {{fence rule — typically including "do not import the specific scene content"}}
  - {{fence rule — typically including "the demonstration is X, not Y"}}
dispatch-status: {{active | excluded}}    # optional; default active
excluded-by: {{decision id}}              # optional; required if dispatch-status=excluded
excluded-reason: |                        # optional; required if dispatch-status=excluded
  {{multi-line reason}}
supersedes: {{prior exemplar slug}}       # optional
superseded_by: {{new exemplar slug}}      # optional
---
```

**Field discipline:**

- `name` — kebab-case slug, conventionally `<persona-slug>-exemplar`. Must be unique within `cards/persona-exemplars/`.
- `persona-ref` — must resolve to an existing card. Margit validates the reference at write-time.
- `class` — always `persona-exemplar`. No subclasses.
- `purpose` — what the exemplar primes for (e.g. "voice prime for taylor-hebert-kl-122ac impersonator", "voice + reading-stance prime for cape-fic-reader audience persona").
- `content-match` — degree to which the exemplar's scene-content overlaps the consumer's target. High = adjacent setting/register/period; low = deliberately distant (used in ablation studies). Per the v16 vs v17 finding (cold-read-report-exemplar-experiment.md), high content-match produces tighter voice transfer.
- `authored-by` — who wrote the passage. `claude (in-session, intended to evoke <X>; not lifted)` is the canonical form for AI-authored exemplars.
- `length` — ~word-count guidance. Recommended range: 150-350 words. Shorter loses grammar-transfer signal; longer dilutes pattern-matching.
- `fences` — explicit constraints on how the exemplar is consumed. At minimum: a no-content-import rule and a what-transfers-vs-what-doesn't rule. Mirrors the surface-convention fence from PROP-0003-A.
- `dispatch-status` — `active` (default) means the dispatcher reads this exemplar when present. `excluded` means the file is retained as a design artifact but never injected into a dispatch payload. Required for any exemplar that fails experimental validation (see `cards/persona-exemplars/orchestrator-critic.md` for the canonical example).
- `excluded-by` + `excluded-reason` — required when `dispatch-status: excluded`. Provides paper trail.

---

## Body

The body is the exemplar passage itself — prose only, no commentary, no annotation.

**Structure:**

```
# Exemplar — <persona display name>

<optional one-line scene-setter in italics, e.g. *[reading a generic capefic chapter: rooftop confrontation between Veil and Cordon]*>

<the passage>
```

**Length guidance:** 150-350 words. Above 350, the exemplar dilutes; below 150, grammar-transfer signal is too thin.

**Content discipline:**

- The passage must be in the persona's voice, demonstrating 2-3 specific load-bearing features the persona card describes.
- The scene/context must be distinct from the consumer's likely target — for impersonator exemplars, a scene NOT in the chapter being rendered; for audience exemplars, a hypothetical artifact NOT the one being reviewed; for renderer voice exemplars, content adjacent-to-but-not-from the project (per the v16 vs v17 finding).
- Honor character fences from the persona card. Hard fences in the card remain hard in the exemplar.
- No meta-commentary. The exemplar shows, it does not describe.
- For audience persona exemplars: include in-character verdict + flag behavior, not just live-read cadence. The reviewer's whole output shape (live-read pass + verdict + flags + what-worked) should be demonstrable from the exemplar.

---

## Surface-convention fence (dispatch-side)

When a consuming agent loads an exemplar, the dispatch prompt MUST inject the following fence:

> The exemplar demonstrates voice and output-shape. Do NOT import the exemplar's specific content (characters, place-names, events, surface conventions like italics formatting, scene-break symbols, or address forms) into your actual output. Only the cadence, sentence-shape, register, and noticing-patterns transfer.

This fence closed the v17 leak in the renderer experiment (where the exemplar's italic-as-memory surface convention bled into the target chapter's first paragraphs). It is non-negotiable wherever exemplars are dispatched.

---

## Margit responsibilities

The card warehouse extends to persona-exemplars:

1. **Validation** — frontmatter conforms to this schema; `persona-ref` resolves to an existing card; `dispatch-status: excluded` exemplars have `excluded-by` + `excluded-reason`; length is within range.
2. **Catalog** — index parallel to `cards/personas/`. Exemplars are visible alongside their referenced cards.
3. **Preservation** — pre/post-mutation preservation discipline applies. Replacing an exemplar requires preserving the prior version via `supersedes` / `superseded_by`.
4. **Promotion** — when an exemplar is authored ad-hoc inside a project workspace (e.g. `active-project/staff/...`), margit promotes the validated version to `cards/persona-exemplars/` for library-wide reuse.

---

## File layout

- **Library**: `cards/persona-exemplars/<slug>.md` — canonical, project-agnostic. Most exemplars live here.
- **Project-bound override**: `active-project/persona-exemplars/<slug>.md` — optional. When present, overrides the library entry for the active project's dispatches only. Useful for project-specific voice tuning that should not pollute the library.
- **Renderer voice** (PROP-0003-A — parallel pattern, separate file): `active-project/voice-exemplar.md` (series-level), `active-project/theater/voice-exemplar-<chapter-slug>.md` (per-chapter override). Not under this schema; uses a one-passage format with explicit `voice-target` and `content-match` fields.

---

## Resolution at dispatch

A consuming agent dispatcher resolves an exemplar path as:

1. Check `active-project/persona-exemplars/<slug>.md`. If present and `dispatch-status` ≠ `excluded`: use this.
2. Else check `cards/persona-exemplars/<slug>.md`. If present and `dispatch-status` ≠ `excluded`: use this.
3. Else: no exemplar. Dispatch proceeds without an exemplar-prime channel (baseline behavior preserved per PROP-0005 null-default).

The resolved path (or absence) is passed to the agent as an optional input field. The agent reads the exemplar after loading the card, applies the surface-convention fence, and pattern-matches throughout generation.

---

## Versioning

Exemplars version independently from their referenced cards. A persona's biography may stay stable across many exemplar iterations; conversely, a card revision may or may not require an exemplar rewrite. When in doubt: re-author the exemplar on card revision; the cost is small and the alternative (drift between described voice and demonstrated voice) is the failure mode this architecture exists to prevent.

Superseded exemplars are preserved per the margit preservation discipline. Use `supersedes` / `superseded_by` frontmatter fields.
