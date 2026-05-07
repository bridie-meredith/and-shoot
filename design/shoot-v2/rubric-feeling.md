# Feeling-Flags Rubric — V1 (LOCKED 2026-05-07)

Authority for the **feeling-flags** facet. POV-character-aware; per-character per-scene-capped; somatic-tell-only content discipline.

Authority chain:
- This rubric.
- Per-character persona card (§Voice / §Look / §Signature Moves / §Hard Fences / §Forbidden registers) — the character's somatic-tell vocabulary.
- For POV: also the behavior pack (`cards/dialects/<pov>.card.md` + variant), as in narrator-interest.
- Locked NI file (cross-facet contract for POV non-redundancy).

---

## What feeling-flags is for

A feeling-flag captures a character **showing** an interior state through a somatic tell — body, gesture, posture, breath, gaze, micro-action — when the audience cannot read that interior from the proto-line content + already-cited facets alone. The somatic tell IS the entry. The named feeling is **forbidden** in description.

Feeling-flags is the **show-not-tell licensing layer for interior**. The stitcher reads fires as render-weight signals: a fired beat gets the somatic tell rendered in full at stitch-time; a silent beat does not.

Sparse by design. Most beats fire nothing.

### Distinction from adjacent facets

- **NI** (POV-only): what the narrator's attention lands on — broader; cognition + perception + memory monuments. Feeling-flags (POV) = the somatic SHOW of the narrator's own interior, captured separately. NI registers the cost; feeling-flag shows the body-bearing-of-the-cost.
- **Sensory** (environmental): perceptual cues from the world. Feeling-flags is interior, not environmental.
- **State-updates** (canonical state-write): mood/register/voice-tone are NOT tracked-state per state-updates rubric. Feeling-flags lives in the perception-layer; state-updates lives in the canonical-state layer.
- **Memory-flags** (POV): callback to prior story content. Feeling-flag may co-fire when a memory-trigger produces a somatic tell, but neither requires the other.

---

## The two-question defensibility gate (Q1 + Q2)

Every fire must answer both, AND-gated:

- **Q1 — Audience-cannot-otherwise-read.** Without this flag, can the audience read the character's interior from the proto-line + sensory-flags + dialogue + (for POV) NI alone? If YES → refuse (redundant with proto-line / cross-facet). If NO → Q1 passes; the flag licenses interior the rendered prose otherwise leaves invisible.
- **Q2 — Meaningful-enough.** Is the interior meaningful enough to render? Render-weight in the stitched output: this fire will get a clause; is the interior worth a clause? If trivial → refuse. If structural to the scene's pivot, the character's arc, the episode's stakes → fire.

Default to silence when uncertain.

---

## Multi-justification gate (≥3 of 5)

A fire must defend with at least three of the following, named explicitly:

1. **Somatic-tell-card-match.** The tell matches the character's persona-card §Voice / §Signature Moves / §Look vocabulary. (For POV: behavior-pack + persona-card.)
2. **Q1-interior passes** (audience-cannot-otherwise-read).
3. **Q2-meaningful passes** (interior is structural).
4. **Scene-eligible** (per-character per-scene cap not yet used; if used, this fire is the better choice — selection criterion).
5. **Functional-register: ≥2 of 4** — { realization | grim humor | social commentary | painting characterization }. Painting-characterization is the structural default; the others require explicit register-hit.

Single- or two-justification fires fail the gate. Default to silence.

---

## Form discipline

### Required content shape

```
<id> @<proto-line-id> <character-slug>: <somatic-tell-one-clause> | expressed: <yes|partial|no>
```

- **`<character-slug>`** — the character whose interior is shown. Must match the fork-of-record (the per-character writer-fork that authored the entry).
- **`<somatic-tell-one-clause>`** — the body-show. Subject + verb + (object/locator). NO named-feeling vocabulary.
- **`expressed:`** — `yes` (in-scene audience reads the tell), `partial` (visible to attentive observer), `no` (interior-only; reader sees, in-scene characters miss).

### Forbidden in description

- **Named-feeling vocabulary.** Hard ban: { sad / sadness / sorrow / grief / mourn / mourning / afraid / fear / fearful / scared / frightened / anxious / anxiety / angry / anger / rage / wrathful / ashamed / shame / shameful / proud / pride / hopeful / hope (as feeling) / despair / desperate / desperately / resolve / resolved / resolute / determined / determination / love / loving / hatred / hate / disgust / disgusted / contempt / pity / pitying / regret / regretful / yearning / longing / dread / dreadful / horror / horrified / joy / joyful / happy / unhappy / miserable / glad / lonely / loneliness / bitter / bitterness / weary / wearied / desolate / desolation }.
- **"feels" verb** in description.
- **Direct address of the interior** ("she felt the X", "he was X").
- **Hedges and softeners.** Hard ban: { like / as if / as though / kind of / sort of / somewhat / almost / nearly / a bit / something like / a kind of / a sort of / faintly / vaguely / barely-X / half-X }. The somatic tell is direct or refused; never qualified.
- **Comparisons and similes.** Hard ban: any "X like Y" / "X as Y" / "X as if Y" construction. The body action is what it is, not what it resembles.
- **Metaphor for feeling-show.** Forbidden: figurative-naming of the feeling through a fixed or original figure ("his face fell" — fall-as-sadness; "her heart sank"; "his eyes burned"; "she went cold"). Body actions named in their own register only.
- **Compound naming.** "X-tinged", "X-edged", "X-shadowed", "shade of X" — refuse.
- **Synonym ladder.** Synonym substitution for a banned named-feeling (melancholy for sadness, fury for anger, panic for fear) — refuse. The list is a ban on the SEMANTIC SLOT, not on the surface tokens.

### Permitted in description

- Body actions (sets her feet / drops eyes / steps back / wipes eyes / goes still / breath hitches / hand closes / shoulder turns).
- Postural / orientation changes (turns toward / turns away / shifts weight to / leans toward).
- Gaze and breath (looks at / does not lift gaze / breath catches / pauses one beat).
- Verbalized-but-not-emotional micro-actions ("does not speak again" / "does not respond").

The somatic tell must be SHOWN, not implied.

---

## Per-scene + per-episode + per-season caps

- **Per-scene per-character cap: ≤1.** Hard. Each character may fire at most once per scene.
- **Per-scene total cap: ≤3.** Soft. Multi-character scenes (confrontation-class) may exceed if each character's fire stands on its own.
- **Per-episode total: 2-5%** sparsity (1.5–4 fires per ~77-beat episode; longer episodes scale linearly).
- **Per-season distribution:** at least 3 different character-slugs across episodes 1–6. Single-character-monoculture (all fires on POV) signals under-coverage.

POV gets ≤1 per scene like every other character (≤4 per episode given 4 scenes; rarely all four spent).

---

## Curve-shape rubric (tens-independent)

Feeling-flags fire across the tens curve, not concentrated at peaks. Some fires are quiet-beat (assessment stillness, refusal-to-look-extended, threshold-cross before-the-act); some are peak-beat (commit-stance, retreat, rupture-bearing).

**Tens-independence rule:** feeling-flags do NOT gate on tensometer ≥ 2 (sensory precedent). Correlation-only observation. The expected file-shape distributes fires across t=1, t=2, t=3 per the natural distribution of somatic-show in the episode.

---

## Cross-facet contract

### NI (mandatory for POV; soft for non-POV)

- **POV non-redundancy** (mandatory). A POV feeling-flag at @N must NOT duplicate the NI fire at @N. Distinct jobs: NI = registration / cognition; feeling-flag = somatic-show. Co-citation permitted; redundancy forbidden. The Q1-interior gate enforces this for POV.
- **Non-POV** (soft). Non-POV feeling-flags do NOT cite NI; NI is POV-only. Feeling-flag for non-POV character is the only facet capturing that character's interior (state-updates excludes mood/register; sensory excludes interior; memory is POV-only).

### Sensory (unrelated)

Independent. Some feeling-fires may co-occur with sensory-fires (a sensory inflection at a peak beat may correlate with a feeling-show beat); not contracted.

### State-updates (separation contract)

Mood / register / voice-tone are NOT canonical state per state-updates rubric. Feeling-flag is selection-signal only. State-updates does NOT consume feeling-flag entries.

### Loc-state (soft alignment)

Scene boundaries inherited from loc-state. Feeling-flag respects scene boundaries for the per-scene cap.

### Memory-flags (independent)

A memory-flag (POV monument trigger) may correlate with a POV feeling-flag (the trigger produces a somatic tell). Neither requires the other. Co-citation permitted.

### Tensometer (observation-only, like sensory)

Independent. Tens-correlation observed at audit but never gated.

---

## Authorship

Per-character writer-fork model (state-updates pattern). One writer per character authors only that character's feeling-flags.

- **POV (taylor-hebert-westeros):** dialogue-writer fork in feeling-show output mode. Loads behavior pack + persona card + locked NI (mandatory non-redundancy check) + locked sensory (soft) + locked state-updates (soft) + this rubric.
- **Non-POV (mira-stonefield, edric-cray, census-officer, clerk):** dialogue-writer fork per character. Loads only that character's persona card + this rubric. No NI, no memory.
- **Off-stage characters (osmynd):** no fire unless persona card authored AND on-stage feeling-show is licensed by the character's card. Default refuse for off-stage.

Cross-license writing is authority violation (anti-pattern #3).

Two-pass authoring per fork:
- **Pass 1 (per-beat):** evaluate each candidate beat against Q1 + Q2 + multi-justification.
- **Pass 2 (file-shape):** verify per-character per-scene cap, sparsity 2-5%, vocabulary distinct (anti-pattern #7), no labeled-feeling-leaks (anti-pattern #1).

---

## Anti-pattern catalog

1. **Labeled-feeling-leak.** Named feeling in description (sad, afraid, etc.) or "feels" verb. Hard refuse.
2. **Audience-already-can-tell redundancy** (Q1 fail). Proto-line + cross-facet already convey the interior.
3. **Cross-character omniscience.** Fork firing for a character it does not license.
4. **Off-stage feeling fire** (without card).
5. **Procedural-flat-character forced.** Firing for a character whose persona card forbids interior performance (officer, clerk).
6. **POV duplicate-with-NI.** Taylor feeling-flag where NI on same beat already shows what feeling-flag would show.
7. **Vocabulary saturation.** Same somatic-tell verb across multiple fires (everyone "goes still", everyone "drops eyes").
8. **Per-scene cap violation.** Two fires for one character in one scene.
9. **Single-justification fire.** Fewer than 3 of 5 multi-justification slots filled.
10. **Density-on-flat-tens.** Fires concentrated at peaks only; tens-monoculture.
11. **Direct interior-narration ("she felt").** Form violation.
12. **Hedged feeling vocabulary** ("a kind of sadness", "something like resolve"). Hedged ≠ unnamed; refuse.
13. **Idiomatic feeling-naming** ("his face fell", "her heart sank"). Idiom names through metaphor; refuse.
14. **Simile / comparison.** "Like X" / "as if X" / "as Y" structures used to render feeling-show. Hard refuse — body action is what it is, not what it resembles.
15. **Hedge / softener language.** "almost", "nearly", "kind of", "sort of", "somewhat", "faintly", "vaguely" — refuse. The somatic tell is direct or absent.
16. **Original-figure metaphor.** Original (non-idiom) metaphors that picture the feeling ("a stone fell into her chest", "the floor pulled at his shoes") — refuse. Body register only.
17. **Synonym-ladder evasion.** Substituting a synonym (melancholy / fury / panic) for a banned named-feeling. Refuse — the ban is on the SEMANTIC SLOT, not the surface token.

---

## Calibration anchors

| Anchor | Beat | Verdict | Why |
|---|---|---|---|
| C1 | @8 edric holds eyes on road past cart | refuse | Proto-line IS the refusal-to-look tell. Q1 fails. |
| C2 | @52 mira drops eyes to flagstones | refuse | Proto-line IS the tell. Q1 fails. User's pre-Phase-0 framing. |
| C3 | @57 edric steps back through the door | fire | Edric §exit-check signature; proto-line carries the act, feeling-flag carries the cost-of-the-act; multi-justification stacks. |
| C4 | @39 taylor sets her feet on the dirt where his next pace commits | fire | Body-commit; distinguishes from NI's cost-tracking on adjacent beats; episode's structural refusal pivot. |

A writer-fork passing all four anchors has the rubric internalized.

---

## Review architecture (hybrid; independent gates)

- **Mechanic auditor.** Form (somatic-only, no labeled-feeling-leak), Q1 + Q2, multi-justification, per-scene/per-character/per-episode caps, fork-of-record citation, anti-pattern check, curve-shape, cross-facet contract.
- **Dialect audience** (worm-canon-pedant + dark-fantasy-reader + pulp-enthusiast, voice-fidelity-only mode, calibrated per character).
  - For taylor: §Voice / §Signature Moves on base + variant card.
  - For mira: §Voice / §Look / §Signature Moves on her card.
  - For edric: §Voice / §Look / §Signature Moves on his card.
  - For officer / clerk: §Voice / §Forbidden registers; expected verdict mostly NEAR-MISS-skip-correct.
- **Independent gates.** Both must pass for ACCEPT. They cannot substitute. Voice-fidelity is the dialect audience's exclusive scope; mechanic does not adjudicate voice; dialect does not adjudicate firing decision.
- **Adversarial pass (Phase 3).** Mechanic auditor in hostile mode. One strongest seam per entry + curve seam + cross-facet seam + Q1-interior-integrity seam + per-character-vocabulary-saturation seam.

---

## Sparsity / coverage targets (file-shape audit)

| Metric | Target | Hard / Soft |
|---|---|---|
| Per-character per-scene cap | ≤1 | hard |
| Per-scene total cap | ≤3 | soft (warn at audit) |
| Per-episode sparsity | 2-5% | target (3-6 fires on 77 beats) |
| Per-season character distribution | ≥3 distinct character-slugs across e01-e06 | advisory tracking |
| Vocabulary distinctness (per-character) | each character's tells use that character's card vocabulary | hard |
| Tens distribution | distribute across t=1, t=2, t=3 | soft |
| Functional-register | ≥2 of 4 per fire | hard |

---

## Locked notation

This rubric is V1 LOCKED 2026-05-07. Subsequent phases (Phase 1 baseline review, Phase 2 writer-forks, Phase 3 seams, Phase 4 defense, Phase 5 final) must reference this version. Mid-tuning rubric changes require re-running affected phases (memory-flags precedent: tightening at Phase 4 lives in Phase 4 alone; tightening at Phase 5 requires restart).

User-supplied tightenings absorbed pre-Phase-0:
1. Frugal (per-character per-scene cap ≤1; sparsity 2-5%).
2. Disambiguation-on-interior (Q1).
3. Somatic-tell-not-labeled (form discipline).
4. POV included (Reading B-with-cap; Taylor gets feeling-flags too, capped per-scene).
5. Make it count (multi-justification ≥3 of 5).
6. **No naming the feeling at all** (schema field `feels:` removed; description forbids named-feeling vocabulary; idiom-naming and hedged-naming both refuse).
7. **No comparisons, similes, hedges, metaphors.** Hard ban on { like / as if / as though / kind of / sort of / somewhat / almost / nearly / faintly / vaguely } and on figurative-feeling-naming. Body register only; the action is what it is, not what it resembles.

Schema edit (caveat-pre-ship): `schemas/facet.schema.md` § feeling flags content shape will be revised to drop `feels <feeling>` field; ships with Phase 5 facet file commit (sensory precedent).
