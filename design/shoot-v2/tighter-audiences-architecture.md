---
design: tighter-audiences + antagonistic-generation
date: 2026-05-10
status: PROPOSAL — awaiting user confirmation before pivot
trigger: user direction 2026-05-10g — "use antagonistic generation and feedback, based on tighter audiences rather than formulaic rulesets"
relates-to: antagonistic-tuning-plan.md, facet-tuning-process.md, rubric-*.md, /and-facets-*.md
supersedes-pattern: rule-based facet generation + 3-persona-uniform adversarial review
---

# Tighter Audiences + Antagonistic Generation

A pivot from the rule-based + general-audience pattern that produced memory + feeling + NI tuning (which worked but ran against formulaic rulesets) toward audience-driven authoring and review with **specialized per-facet reviewers** and **adversarial pressure at draft time**.

## What we built (legacy pattern)

The pattern that shipped memory + feeling + NI tuning:

1. **Locked rubrics per facet** (`design/shoot-v2/rubric-*.md`) with named anti-patterns (AP1, AP2, …) and quantitative gates (sparsity bands, channel coverage, multi-justification ≥3 of 5).
2. **Generation** by per-facet authors against the locked rubric. Authors produce; rubric is the gate.
3. **Audience review** by the same 3 general-purpose personas (dark-fantasy-reader, pulp-enthusiast, worm-canon-pedant) applied uniformly to every facet. Attack format: "rubric §AP-N — <description>."
4. **Audit** scans for rubric anti-pattern violations mechanically (AP-SCAN class).

This worked. memory + feeling + NI all shipped through 3-of-3 phases with measurable lift. Bidirectional audit + tuning loop validated three times.

But it has structural limits the user surfaced:

- **Formulaic ruleset grounding.** "rubric §AP-N" is a meta-language that drifts from the actual reading experience. The audience attacks become rule-citations rather than direct adversarial readings. The defenses become rule-defenses rather than work-defenses.
- **General audience applied uniformly.** The same 3 personas attack every facet. But the failure modes of vibes are different from feeling are different from NI. A persona that's productive on memory monument-callback may be THIN on vibes token-quality. Uniform audience means uniform attack quality regardless of facet.
- **Review is post-hoc.** Generation completes; then the audience attacks. The author has no live adversarial pressure during draft time. Drafts that look right to the author commit; the audience finds the seams afterward; defense or revise spends another full dispatch.

## What the pivot proposes

### 1. Tighter audiences — per-facet specialized

Replace the 3-persona uniform audience with **facet-specialized adversarial reviewers.** Each facet gets its own audience set, calibrated to its specific failure modes.

Example specialization (illustrative; cards to be authored if pivot accepted):

- **Memory** audience: a monument-fidelity pedant (sharper than worm-canon-pedant); a smallfolk-frame reader (atmosphere lens specific to Westerosi register); a callback-economy critic (does this monument actually earn this fire, or is it ornament?).
- **Feeling** audience: a card-text grammarian (does the somatic tell match the character card vocabulary?); a stitch-render reader (does this read as somatic or as somatic-disguise of a thought?); a per-character voice critic (specialist for Taylor / mother / father).
- **NI** audience: a doubled-register reader (foreknowledge / mask-thinning specialist); a perceptual-access pedant; a channel-distinctness critic.
- **Vibes** audience: a token-quality grammarian (sentence-parsability mechanic); a licensing-meaningfulness critic (do these `licensed-by:` chains earn the keyword?); a cross-cutting-bias reader (does this vibe actually bias future generation, or is it a thematic label?).

The 3 general personas remain useful as a "stitcher-side" audience — readers of the eventual prose. But for facet-level adversarial work, the tighter audiences fire.

### 2. Antagonistic generation — adversarial pressure at draft time

Currently: author writes the entry → audience attacks afterward.

Proposed: author writes a draft → tighter-audience persona attacks live → author revises in the same dispatch → final commit.

Implementation options:

- **Single-author + persona-side-fork.** The author dispatch holds two channels: generation and adversarial. Each draft goes through both before commit.
- **Two-dispatch handshake.** Author writes draft to a scratch file; persona reads scratch, attacks; author revises; commits.
- **Authoring with persona-card loaded as critic.** The author loads its target persona AND a critic-persona simultaneously; the brief instructs adversarial self-critique before commit.

Concrete shape TBD; the principle is that the audience pressure shifts left from review-time to draft-time.

### 3. Less formulaic ruleset reliance

Rubric files remain as baseline reference (the work is grounded; the rubrics describe what good looks like). But:

- **Audience attacks should NOT primarily cite rubric clauses.** "rubric §AP-N" is a fallback when the audience can't articulate the seam directly. Primary attacks are direct readings: "this entry doesn't land because the body register is doing what the proto-line already does, so the entry is paraphrase rather than addition."
- **Defense should NOT primarily cite rubric clauses.** A defense that says "AP §3 licenses this" is weaker than a defense that names the specific reading the entry is doing.
- **Audit's AP-SCAN class is fine to keep** for mechanical coverage, but it's no longer the source-of-truth for "is this entry good." TASTE-FLAG and audience-driven findings are the substantive layer.

## Migration path

If the pivot is accepted:

### Step 1 — Author tighter-audience cards

Create per-facet audience persona cards under `staff/audience/`:

- `staff/audience/memory-monument-fidelity/card.md`
- `staff/audience/memory-callback-economy/card.md`
- `staff/audience/memory-smallfolk-frame/card.md`
- `staff/audience/feeling-card-grammarian/card.md`
- `staff/audience/feeling-stitch-render/card.md`
- `staff/audience/feeling-taylor-voice/card.md` (and per-character cards)
- (and for NI, vibes, etc.)

Each card: persona definition, attack vector specialization, rubric reference (still grounded), example seams from prior tuning runs (calibration).

These are facet-tuning audiences, separate from the existing 3 stitcher-side audiences in `active-project/audience/`.

### Step 2 — Update tuning command shape

`/and-facets-tune-<facet>` (per-facet tuning command, not yet built) loads the tighter audience set for that facet and runs Phases C-F with the specialized critics.

The existing 3-persona dispatch shape is retained as a fallback for cross-facet pile-up review (audit-level) and for the eventual stitcher-prose review (and-wrap stage).

### Step 3 — Pilot on one facet

Run the new pattern on one facet that hasn't been tuned yet — vibes is the natural pilot since it's the next in sequence and has facet-specific failure modes (token-quality, licensing-meaningfulness) that the general audience cannot cleanly attack.

Compare the new pattern's output against what the in-flight vibes adversarial pass produces (the latter using the legacy 3-persona pattern). The comparison is the validation data.

### Step 4 — Update authoring shape

If antagonistic-generation is wanted, retrofit the per-facet authoring dispatches (impersonator / showrunner / studio etc.) to either:
- Load a critic-persona alongside the author-persona, OR
- Run a draft → critique → revise loop within a single dispatch.

This is the larger architectural change. Ship Step 1-3 first; revisit Step 4 once tighter audiences are validated.

### Step 5 — Audit re-tuning

The auditor itself (still flag-only per Step G) becomes a candidate for the antagonistic-generation pattern. Currently the auditor's outputs are rubric-citation-grounded; under the pivot, audit findings should also be direct adversarial readings, with rubric citations as supplementary grounding.

## Open questions

1. **Pilot facet** — vibes (per Step 3 above), or pick a different first target?
2. **Audience-card source** — author from scratch? or refine the existing 3-persona cards into specializations?
3. **Antagonistic-generation timing** — defer Step 4 until tighter-audiences are validated, or design + ship together?
4. **Existing rubric edits** — should URI-001 / URI-007 carry-back rubric V2.1 work proceed, or be deferred indefinitely under the pivot? The rubric edits would deepen the formulaic ruleset; under the pivot, that's the wrong direction. But they capture validated audience signal that's useful even if the rubric isn't the primary source-of-truth going forward.
5. **Legacy pattern continuity** — memory + feeling + NI shipped under the legacy pattern. Do they get re-tuned under the new pattern, or accepted as-is?

## What this pivot is and isn't

- **Is:** an architectural shift toward audience-driven adversarial work with specialized per-facet reviewers.
- **Is not:** a rejection of the locked rubrics. Rubrics still ground the work; they just stop being the primary attack/defense citation language.
- **Is not:** a restart. The three facets that shipped under the legacy pattern keep their tuning artifacts and audited state. The pivot applies to the next facet onward (and to re-tuning if requested).
- **Is not:** an immediate change to the agent definitions. The audience agent is config-loaded; the tighter-audience pattern needs new persona cards but doesn't require changing the audience agent's tool set.

## Risks

- **Tighter audiences may be over-fit per facet.** A monument-fidelity-pedant attacks memory well but contributes nothing to feeling. The corpus of audience cards grows.
- **Audience-card authoring is meta-work.** Each card is itself a tuning target; if the cards are bad, the audience attacks are bad.
- **Defense quality depends on audience quality.** A weak audience produces weak seams produces weak defense. The 3 general personas have been tuned over months; new specialized cards are unproven.
- **Antagonistic-generation may collapse the author/critic distinction.** If the author has the critic loaded, "blind authoring" becomes harder; the author may pre-anticipate and self-censor in ways that weaken the work.

## Recommendation

1. Confirm pivot scope with user before re-architecting. The pivot is real but the scope (which facets, which audiences, when antagonistic-gen lands) needs a decision.
2. Let the in-flight vibes dispatch return as comparison data. Do NOT cancel.
3. If pivot confirmed: pilot on a NEXT facet (e.g., sensory or state-updates, both untouched) under the tighter-audience pattern, then compare to vibes (legacy pattern) to validate the architectural shift.
4. URI-001 / URI-007 rubric carry-back: defer until pivot direction confirmed. The rubric edits remain valuable as documentation of validated audience signal even if they stop being source-of-truth.

The user has been pacing fast; ask once, then proceed.
