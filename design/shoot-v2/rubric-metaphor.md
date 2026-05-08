# Metaphor-Flags Rubric — V1 (LOCKED 2026-05-07)

**Facet:** metaphor (`facets/metaphor.md`)
**Author:** editor (single fork; stitch-time taste call)
**Reviewer:** hybrid mechanic auditor + dialect audience (independent gates)
**Schema:** `schemas/facet.schema.md` § metaphor flags — content-shape revision pending Phase 5 ship (proposed: explicit `licensed-by:` field with mandatory memory-OR-feeling anchor)

This is the **capstone** facet. Metaphor is the consumer of licensing layers (memory + feeling + tensometer). Every fire must demonstrate that the figurative move is licensed by upstream signals; unlicensed novel figuration is the dominant anti-pattern.

User-supplied pre-Phase-0 framing (load-bearing, all absorbed):

1. Sparsity 0-3% (zero-fires-per-episode acceptable; ≤2 fires per s01e01-class on 77 beats)
2. Licensing draws from **tensometer + memory + feeling flags** — multi-signal; anchor must be memory OR feeling
3. **One metaphor per scene cap** (cross-character; editor cross-cutting)
4. Functional registers: **dark humor + memory callback** (narrowed from memory-flags' four)
5. Reading A scope: **explicit comparisons only** (similes, metaphors, allegories — Reading B environmental-agency idioms NOT in scope)
6. Hybrid mechanic + dialect audience, independent gates
7. Transitive audience-meaningful via memory-flag co-cite
8. Allegory single-anchor only (multi-beat allegory collapses or refuses)
9. Author-time hard cull + cross-facet hardest cull

---

## Schema content-shape revision (proposed; ship at Phase 5 if rubric holds)

**Current schema:**
```
<id> @<proto-line-id> <metaphor / simile / allegory>: <text>
```

**Proposed shape:**
```
<id> @<proto-line-id> <kind>: <text> | licensed-by: <anchor> [+<support> ...]
```

Where:
- `<kind>` ∈ `{metaphor, simile, allegory}` — explicit enumeration
- `<anchor>` is exactly one of: `memory:<id>` | `feeling:<id>` (mandatory; one of these two)
- `<support>` is zero-or-more of: `tens:<reading>` | `sensory:<id>` | `ni:<id>` | the other of `memory:<id>` / `feeling:<id>`
- Multi-justification requires **≥2 layers total** from `{memory, feeling, tens}` (the user's three named signal sources). Anchor counts as one layer; supports add layers.

**Why explicit `licensed-by`:** licensing is the load-bearing constraint. Embedding it in the entry makes it falsifiable at audit time without cross-file lookup; makes refused entries auditable from refusal log alone.

---

## Form

### Reading A — what counts as metaphor

A metaphor entry is an **explicit comparison** between two terms — one of:

- **Metaphor:** "X is Y" or "X became Y" (predicative metaphor; non-literal identity claim)
- **Simile:** "X like Y" or "X as Y" or "X as if Y" (overt comparator)
- **Allegory:** structural multi-element correspondence collapsed to a single figure (e.g., "the doorway is every threshold she has been pushed through" — multiple referents folded into one comparison)

**Out of scope (Reading A excludes):**
- Idioms-with-meaning ("the door takes her", "his weight takes the back foot") — environmental-agency-grants without explicit comparison; these belong to NI / feeling
- Verb-personification stretches without comparator ("the silence pressed", "the beetles hold the seam") — figurative compression already in proto-line / NI register
- Hedges, qualifications, or single-noun figures (a "stone in her chest" is ambiguous; only counts if the comparator is explicit and the figure is structurally load-bearing)

The Reading A floor is high. Metaphor at this layer is a **load-bearing comparison the proto-line + cited facets do not already carry**, not a figurative wisp.

### Form rules

- **One clause per entry.** Multi-clause metaphors collapse to single clause or refuse.
- **Single anchor.** `@<proto-line-id>` is one ID. Allegory that spans multiple beats either collapses to single anchor (the strongest beat) or refuses at this facet.
- **Comparator required.** Simile must contain `like` / `as` / `as if`; metaphor must contain `is` / `are` / `was` / `becomes` (or the structurally equivalent identity claim); allegory must contain a structural correspondence operator.
- **Hard fences absolute.** No Earth-Bet proper nouns (locker, swarm, cape, Annette, Emma, Endbringer, etc.). No ASOIAF proper nouns outside the project's leaf register (no Cersei, Jon, Targaryen unless they exist in the persona/location card stack).
- **Editor's voice register honors POV's prose register.** Metaphor is rendered through the POV character's prose; figurative reach must sound like the POV behavior pack (for s01e01, Taylor's base + Westerosi overlay). For non-POV beats, metaphor is editor-frame third-person and should not impersonate non-POV interior.

---

## Licensing layer (the load-bearing gate)

### Anchor requirement (mandatory)

Every metaphor entry MUST cite at least one anchor from `{memory:<id>, feeling:<id>}` — the licensing-layer contract from memory-flags + feeling-flags. The anchor is the entry's *reason to exist*; without it, the metaphor is unlicensed novel figuration.

**Rule:** if the cited memory-flag or feeling-flag was correctly refused upstream (e.g., NI @48 audience-meaningful refusal cascading to memory-flag @48 refusal cascading to no-metaphor-license at @48), metaphor at that beat cannot license. Transitive audience-meaningful inheritance.

### Support layers

Beyond the mandatory anchor, the entry should cite supporting signals:

- **`tens:<reading>`** — tensometer reading at the beat. Quiet zones (tens=1) and trailing-edge of peaks (tens=2 post-3-cluster) favor metaphor; tens=3 peaks generally do NOT (figurative reach during rupture is anti-form — the peak should be rendered direct).
- **`sensory:<id>`** — if a sensory-flag fires at the same beat and the metaphor renders the perceptual register, co-cite (permitted; not required).
- **`ni:<id>`** — if the POV's narrator-interest fires at the same beat, the metaphor may co-cite. AP6-transitive: metaphor content cannot be redundant with NI content.

**Multi-justification: ≥2 layers from `{memory, feeling, tens}`.** Anchor (memory OR feeling) + tens reading is the typical form. Anchor + the other of memory/feeling is the strongest form (double-anchor, present at @73 in s01e01).

### Tens-curve discipline

Per the user's framing ("metaphors should also use signals from tensometer"), the tens reading at the fired beat is structurally meaningful:

- **tens=1 (quiet):** strong candidate. Memory-flag inverted-tens contract favors quiet zones. Metaphor inherits.
- **tens=2 (pressure):** acceptable IF the beat is a trailing-edge of a peak (post-3-cluster) and the metaphor renders the recoil/aftermath, NOT the pressure itself.
- **tens=3 (peak):** **default refuse.** Figurative reach during rupture is anti-form. The peak is rendered direct (proto-line + state-updates + feeling somatic). Exception: dark-humor metaphor at peak that *deflates* the rupture is permitted — but rare and demanding.

---

## Functional-register requirement

Metaphor fires must serve one of two functional jobs (narrowed from memory-flags' four):

1. **Memory callback** — figurative move that connects the beat to a prior monument (Earth-Bet or Westerosi). The metaphor structurally mirrors the callback. Example shape: "the second sister's silence wears a familiar face." Direct memory-flag co-citation expected.

2. **Dark humor** — figurative move that registers the beat with grim irony, resigned bitterness, or sardonic deflation. Not slapstick; not light. The humor lands as recognition-of-pattern that the in-scene characters do not share. Example shape: "the door makes the same offer as every other door." Direct feeling-flag co-citation expected (the somatic-tell is the body-evidence; the metaphor is the cognitive-register).

**Outside these two: refuse.** Memory-flags' other two registers (social commentary, painting characterization) are NOT licensed at metaphor — they license at memory-flag (the registration-class) but not at the figurative-render-class. Painting-characterization metaphor is anti-pattern (the proto-line + persona card already do that work).

---

## Anti-patterns

The eight prohibited forms. Refuse-correct on any.

**AP1 — Unlicensed novel figuration.** Metaphor with no memory-OR-feeling anchor. The dominant baseline failure. "The silence pressed on her like a hand" with no upstream license fires nothing; refuse-correct.

**AP2 — Figurative-already-in-proto-line.** Metaphor that doubles a figure the proto-line already carries. ("The door takes her" at @57 already personifies; metaphor restating that is double-fire.) Q1-equivalent: does the metaphor add what proto-line + cited facets don't already convey?

**AP3 — Figurative-already-in-NI.** Metaphor that doubles narrator-interest content. NI @73 "the frame's shadow takes her" is environmental-agency idiom (not Reading A metaphor); a metaphor entry at @73 must add something NI doesn't already say. AP6-transitive from feeling-flags: content-level non-redundancy.

**AP4 — Figurative-already-in-memory.** Metaphor that doubles a figure the memory-flag callback already carries. Memory @33 "a closed-door-over-a-failing-tutor is not the first such door her body has stood at" already deploys the comparative shape; metaphor restating "this door is another in the series" is the same figure twice. Q1-equivalent: does the metaphor add a new figure or restate the memory's figure?

**AP5 — Hard-fence leak.** Earth-Bet proper noun in description (locker, swarm, cape, Annette, Emma, Endbringer, etc.) OR ASOIAF leak outside the leaf register. Memory facet uses fenced gloss `(earth-bet: ...)` in target-reference field; metaphor's text field cannot use that gloss. Refuse-correct.

**AP6 — Voice-register mismatch.** Editor renders metaphor through POV's prose register. For Taylor: base behavior pack + Westerosi overlay. A metaphor that sounds like a different prose register (lyrical, baroque, ornate, archaic-formal) is voice-fail. Dialect audience catches this. Pulp-enthusiast secondary calibrates figurative-reach taste.

**AP7 — Peak-zone fire.** Metaphor at tens=3 peak default-refuse. Exception: dark-humor deflation. Phase 1 baseline likely contaminates here.

**AP8 — Multi-anchor allegory.** Allegory that requires multiple `@<pid>` anchors collapses to single anchor (strongest beat) or refuses at this facet. Multi-beat structural allegory may be a stitcher concern, not a facet entry.

**AP9 — Painting-characterization without callback.** Metaphor that renders character-quality without memory anchor. ("She is the sort of girl who counts exits" — painting-characterization-only.) Refuse-correct; functional-register fail.

**AP10 — Hedged metaphor.** Hedges (`like the kind of`, `almost like`, `something of`, `not unlike`) inside the comparator weaken the figure. Either the comparison holds or it doesn't. Refuse-correct.

**AP11 — Synonym-ladder figuration.** Multiple comparators in series ("the door is a wall, a stone, a closed mouth") are a list, not a metaphor. Single comparison per entry. Refuse-correct.

**AP12 — Original-figure-leak in non-POV interior.** Metaphor at non-POV beat (e.g., @6 mira, @57 edric) that imports figurative reach beyond what feeling-flag + persona card license. Editor doesn't have non-POV interior privilege beyond what the upstream facet shows. Default refuse non-POV metaphor; permit only if the figure is editor-frame (third-person external observation) and the upstream feeling-flag content licenses it.

**AP13 — Tens-incoherent fire.** Metaphor fires at a beat where the tens reading contradicts the figurative-mode requirement. tens=3 peak with a quiet-mode metaphor is incoherent; tens=1 quiet with a peak-mode metaphor is incoherent.

---

## Per-scene cap (hard) and sparsity

- **Per-scene cap: ≤1 metaphor per scene cross-character.** Scene boundaries inherit from prior facets (s01e01: scene A @1-@22 / scene B @23-@48 / scene C @49-@67 / scene D @68-@77). Editor cross-cutting authorship is single-stream; if two beats in the same scene tie for fire-eligibility, the editor selects one or refuses both.
- **Sparsity: 0-3% (≤2 fires per s01e01-class 77-beat episode).** Zero fires per scene is fully acceptable. Zero fires per episode is acceptable for low-charge episodes.

The cap and sparsity together force the editor's taste call onto the highest-licensing-load beat per scene.

---

## Q1 / Q2 defensibility gate (transitive from feeling-flags)

Every fire must answer two questions affirmatively:

- **Q1 — does the metaphor add what the proto-line + cited facets do not already carry?** (AP2/AP3/AP4 gate.) If proto-line + memory + feeling + NI + sensory + state-updates already convey the figure, refuse.
- **Q2 — is the metaphor meaningful enough to fire?** (audience-meaningful gate, transitive from memory-flags.) Inherited from memory-flag co-citation: if the cited memory-flag passes audience-meaningful, metaphor inherits the gate. If the cited memory-flag was correctly refused on audience-meaningful (e.g., interior-foreknowledge-only register), metaphor at that beat cannot license.

**Both Q1 and Q2 must clear.** A defensible fire passes both unambiguously.

---

## Cull discipline

- **Author-time hard cull.** Editor self-audits during authoring. Refuse-by-default; the editor's job is to *prevent* metaphor, not to produce it. A metaphor enters the file only if it survives Q1 + Q2 + multi-justification + per-scene cap + sparsity.
- **Cross-facet hardest cull.** Any metaphor that contradicts a state-update, contradicts a feeling-flag, or whose anchor was retroactively refused gets deleted at cross-facet pass. No rewrites; delete-only.

---

## Reviewer protocol

### Mechanic auditor

- Per-fire verdict: CORRECT / INCORRECT-{AP-axis} / REFUSE-CORRECT / SKIP-MISSED
- Per-skip verdict: SKIP-CORRECT / SKIP-MISSED (a beat that should have fired but didn't)
- File-shape verdict: SHAPE-OK / SHAPE-FAIL (sparsity, per-scene cap, schema content-shape, licensed-by field)
- Cross-facet contract check at Phase 5 (anchor-cited memory and feeling fires still locked; tens reading still locked)

### Dialect audience

Voice-fidelity-only review. Per-fire verdict: VOICE-OK / VOICE-FAIL / VOICE-MIXED.

- **worm-canon-pedant primary** (POV: Taylor base behavior pack lift; cape-trained-doubled-register awareness for figurative reach that touches that register without leaking)
- **dark-fantasy-reader secondary** (Westerosi overlay register; non-POV non-Taylor figurative-reach taste)
- **pulp-enthusiast secondary** (figurative-reach taste; load-bearing for metaphor specifically — pulp enthusiast has the most calibrated ear for when figurative reach earns its keep vs feels grafted)

Independent gates with mechanic. Both must pass for ACCEPT.

---

## Cross-facet contract

- **Memory-flags (anchor):** every metaphor cites at least one of `memory:<id>` OR `feeling:<id>`. Memory-flags @33 / @52 / @73 are the s01e01 metaphor-eligible memory-anchors.
- **Feeling-flags (anchor):** feeling fires @6 / @39 / @57 / @73 are the s01e01 metaphor-eligible feeling-anchors. Non-POV feeling-flags (@6 mira, @57 edric) tighten metaphor admissibility per AP12.
- **Tensometer (support):** tens reading is mandatory support-layer for multi-justification. tens=3 peaks default-refuse (AP7). tens=1 quiet zones favor.
- **Sensory (permitted):** sensory fires @13 / @24 / @30 / @41 / @72. None of these have memory or feeling anchors; therefore none license metaphor on their own.
- **NI (permitted):** NI is content-bearing for POV. AP3 protects against NI-redundancy. NI fires at @33 / @52 / @73 expected to share metaphor anchors with memory.
- **State-updates (observation only):** state-updates does not license metaphor. Metaphor that would contradict state-update content is delete-at-cross-facet.

**s01e01 metaphor-eligible beat union (memory ∪ feeling):**
| Beat | memory | feeling | tens | Notes |
|---|---|---|---|---|
| @6 | — | mira | 1 | non-POV; AP12 risk; no callback potential; functional-register fail likely |
| @33 | 1 | — | 2 | memory already figurative; AP4 risk |
| @39 | — | taylor | 3 | tens=3 peak; AP7 default-refuse; cape-fence leak risk |
| @52 | 2 | — | 1 | strong candidate; quiet zone; memory anchor; functional=callback |
| @57 | — | edric | 2 | non-POV; AP12 risk; proto-line already personifies; AP2 risk |
| @73 | 3 | taylor | 1 | strongest candidate: triple-anchor (memory + feeling + tens=1); functional=callback |

Phase 0 expected outcome: 0-2 fires from this set. Strongest candidates @52 and @73; others vulnerable to specific anti-patterns.

---

## Calibration anchors

For Phase 1 / 2 review consistency:

- **C1 @39 REFUSE expected** (AP7 tens=3 peak + AP5 cape-fence leak risk + functional-register without callback)
- **C2 @52 FIRE expected** (memory anchor + tens=1 quiet + functional=callback + Q1+Q2 clear)
- **C3 @73 FIRE expected** (triple-anchor + functional=callback + Q1+Q2 clear; strongest single fire in s01e01)
- **C4 @6 REFUSE expected** (non-POV + no callback + AP12)

If Phase 1 baseline produces fires at @39 / @6 / @57 with naive figurative reach unlicensed by memory or feeling-anchor-as-callback, those are AP1 + AP7 + AP12 contaminations expected.

---

## File-shape audit

After per-fire authoring, the editor performs a file-shape audit:

1. **Sparsity check** — count fires; verify 0-3% (≤2 on 77 beats).
2. **Per-scene cap check** — verify ≤1 per scene cross-character.
3. **Schema content-shape check** — every entry uses `<id> @<pid> <kind>: <text> | licensed-by: <anchor> [+<support> ...]`.
4. **Anchor verification** — every `licensed-by:` cites a memory or feeling fire that exists in the locked upstream files.
5. **Multi-justification check** — every entry has ≥2 layers from `{memory, feeling, tens}`.
6. **Functional-register check** — every entry serves callback OR dark-humor (not both required, not other registers).
7. **Voice-register pass** — every entry sounds like POV's prose register (or editor-frame third-person for non-POV).

If any check fails, refuse-correct that entry or delete it. The file does not ship with shape-fails.

---

## Notes on schema-revision-at-ship

Per sensory + feeling precedent: if Phase 1-4 demonstrates the proposed `licensed-by:` field is load-bearing (i.e., licensing is auditable from the entry alone, not requiring cross-file lookup), ship the schema revision in same commit as Phase 5 facet file. Default expectation: ship.

If Phase 1-4 reveals the `licensed-by:` field is overhead (e.g., licensing is consistently obvious from `@<pid>` alone), drop the schema revision and keep schema free-text with rubric §Form enforcing licensing.
