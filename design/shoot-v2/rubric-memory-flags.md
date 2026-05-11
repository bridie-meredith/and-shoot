# Memory-Flags Facet Rubric

Authoring + review rubric for `facets/memory.md` entries. Phase 1 reviewer-tuning artifact for the shoot-v2 facet-tuning process. Authority for the dialogue-writer Taylor-POV fork (interiority output mode, monument-licensing output mode) when authoring memory-flag entries, and for the mechanic auditor + dialect audience when reviewing them.

Status: V1 draft (Phase 0). Will be locked at end of Phase 1.

The rubric is **POV-character-specific** — each project's POV character gets its own memory-flags rubric instance because the behavior pack §"Memory monuments" is the authoring authority. This rubric instance is for `taylor-hebert-westeros` (s01e01–e06). Reusing the structure for a different POV character requires re-authoring §"Monument inventory" and the calibration anchors against that character's behavior pack.

The rubric depends on the locked tensometer file, the locked narrator-interest file, and the base + variant behavior cards' §"Memory monuments" sections. It does NOT depend on (and must not be folded into) the open V3 rubric work for tensometer.

---

## What memory-flags is for

Memory-flags is the **licensing layer** for callback and figurative reach in the stitched output. Entries mark beats where a behavior-pack monument (Earth-Bet trauma-monument, Westerosi historical monument, local-current monument) lights against a proto-line — either by *displacement* (an Earth-Bet pattern surfaces through a Westerosi event) or by *clamp* (proximity to a Westerosi monument triggers foreknowledge that the interior knows and the spoken layer never tells) or by *callback* (intra- or cross-episode reference to prior story content).

It serves four jobs, in priority order:

1. **Sole stitcher-license for metaphor and callback.** Per `schemas/facet.schema.md` §metaphor: "sparse by design — almost never used in end state unless dark humor or memory callback." Memory-flags fires ARE the *callback* half of that license, and the metaphor facet's editor-authored entries cannot ship on a beat without memory-flag co-citation. Everywhere else the stitcher produces no simile, no allegory, no callback. **Under-firing forbids the stitcher from licit metaphor; over-firing dissolves the licensing-layer function.** A file where every interesting beat fires has the same effect as a file where no beat fires — the gradient is destroyed, and the stitcher has nothing to cite.

2. **Monument-pressure register for the doubled-register character.** For `taylor-hebert-westeros` the doubled register (Earth-Bet shadow + Westerosi-mask cover + Dance-foreknowledge clamp) only fully shows where the monuments touch the proto-line. Narrator-interest exposes interior register; memory-flags expose the *content of the load* the interior is carrying. Without memory-flags, the doubled register reads as quiet interiority; with memory-flags, the doubled register reads as load-bearing.

3. **Quiet-beat anchor.** Memory and monument fire when the foreground tension is low enough for the interior to reach into accumulated weight. **Memory-flags concentrate in tens=1 beats and at the trailing edge of tens=2 beats. They are forbidden by default at tens=3 except under explicit displacement-clamp construction.** This is the **inverse** of narrator-interest's tens-alignment — narrator-interest fires on transitions and peaks; memory-flags fire in the gaps. Where narrator-interest reads forward (the next beat is about to commit), memory-flags reads backward and outward (this beat lights something already standing). The two facets together produce the stitcher's render-grammar: peaks render in full (narrator-interest), gaps render with weight (memory-flags).

4. **Cross-facet anchor for monuments.** Memory-flags is the spine entry for the metaphor facet, an input to the stitcher's render-density gradient, and a downstream consumer of narrator-interest's spotlight (mandatory co-citation). It is the canonical record of *which monument lit, where, and how* across an episode.

Memory-flags is **not** narration. It is not paraphrase of the SVO. It is not an inventory of the interior's mood. It is a one-clause licensing entry plus a target-reference field, fired sparsely on beats where a behavior-pack monument earned its weight.

**The test for any beat is simple: does a behavior-pack monument light *here*, in a way that earns the stitcher's license to render figurative reach or callback against this beat? AND is the foreground charge quiet enough that the interior has room to reach for the monument?** If yes, fire. If the monument is candidate-active but the foreground is at peak and the interior is fully committed, silence — the load is being carried but not registered here. If no monument is plausibly active, silence — the default.

---

## Form

Per `schemas/facet.schema.md`:

```
<id> @<proto-line-id> <one-clause description of the callback> -> <target reference>
```

- **`<id>`** monotonic positive integer scoped to this file.
- **`@<proto-line-id>`** required anchor to a proto-line.
- **One-clause description** — the displacement-cue, the clamp construction, or the callback gloss in POV-character base register. **Hard fence binds here:** no Earth-Bet proper noun, no Dance specifics named, no monument named outside the licit Westerosi-cover register. The description is what the stitcher may quote or paraphrase into the stitched output.
- **`->`** literal arrow separator.
- **`<target reference>`** — the metadata field naming the monument explicitly. Acceptable forms:
  - **Card slug**: mechanism-descriptive form is mandatory (URI-032, 2026-05-11). `cond-fauna-control-rules`, `monument-fauna-silence-at-scale`, `monument-failed-recognition-by-dying-parent`, `monument-enclosed-space-with-helplessness`, `monument-conquest-charter-language`, `monument-dance-succession-language`, `monument-harrenhal-precinct`, `monument-doom-pattern`, `monument-mass-casualty-foreshadow`, etc. **Earth-Bet proper nouns are forbidden as slug components**, even though the target-reference field is metadata-only (not prose-facing). Forbidden: `monument-locker`, `monument-annette-death`, `monument-gold-morning`, `monument-endbringer-arrival`, `monument-bakuda-bombing`, `monument-prt-trigger-period`, `monument-khepri-period`, `monument-coil-dinah-resolution`, `monument-leviathan-arrival`, `monument-behemoth-pattern`. Replace with the mechanism form. The fence applies because margit ingests these as card slugs — Earth-Bet-named cards would propagate the proper noun into the warehouse, downstream agents, and stitcher routing. The fence applies symmetrically to **Dance-of-Dragons proper-noun proper nouns when they appear as slugs:** `monument-dance-of-dragons`, `monument-hour-of-the-wolf` etc. are admissible because they are Westerosi-monument names (not Earth-Bet); the fence is specifically against Earth-Bet proper nouns crossing into the slug surface. (Some monument cards may not exist yet — the rubric admits a margit referral if a slug is referenced without a card; the entry ships flagged.)
  - **Prior proto-line ID**: `e01:33`, `e02:14` for intra- and cross-episode callbacks. (For s01e01 — first episode — there are no cross-episode anchors. Most s01e01 fires will use card slugs or free-text glosses.)
  - **Free-text gloss**: `(earth-bet: dying-tutor-figure pattern)`, `(westeros: harrenhal-precedent)` when no formal card exists. Free-text glosses are the soft path; the conservative move is a margit referral to author the missing monument card with a mechanism-descriptive slug. **The free-text gloss content may use Earth-Bet category terms (`earth-bet:`, `dying-tutor`, `helpless-protector`) but must NOT use Earth-Bet proper nouns (no Annette, Endbringer, Bakuda, Skitter, etc.).** Earth-Bet proper nouns are restricted to behavior-card §"Memory monuments" prose and the impersonator's internal reasoning, not to facet-level metadata.

Form is necessary but not sufficient — a well-formed entry that fails monument-trigger, displacement-discipline, or licensing-discipline is still a violation.

### Hard-fence asymmetry between fields

The **description** field holds displacement-cue discipline: no proper noun, no specific name. *She has heard the shape of that word before in another tongue* (narrator-interest @48 construction) is the licit shape; *she remembers the Hour of the Wolf* and *she thinks of the locker* are prohibited.

The **target-reference** field is metadata. It may name the monument explicitly: `monument-hour-of-the-wolf`, `monument-enclosed-space-with-helplessness`. The stitcher reads target-reference for routing (which metaphor facet entries can co-cite this fire) but does not surface it in stitched prose.

This asymmetry is load-bearing. Authors must not collapse the two fields. A description that names a monument is a hard-fence violation; a target-reference that names a monument **by mechanism form** is the metadata working as designed. A target-reference that names a monument **by Earth-Bet proper noun** (e.g. `monument-locker`, `monument-annette-death`) is a slug-surface fence violation (URI-032) — flag and rename.

---

## V1 rubric (locked at end of Phase 1) — three axes

A memory-flag entry passes review iff it **affirmatively demonstrates** at least one signature on each of three axes (monument-trigger, displacement-discipline, licensing-discipline) and does not violate any anti-pattern.

### 1. Monument-trigger

Does a behavior-pack monument plausibly light at this beat?

The authoring authority for monument inventory is `cards/dialects/taylor-hebert.card.md` §"Memory monuments" (Earth-Bet) and `cards/dialects/taylor-hebert-westeros.card.md` §"Memory monuments" (Westerosi + local-current). Monument extension goes through margit, not through this rubric.

Three trigger classes earn a fire:

- **Earth-Bet displacement.** A Westerosi proto-line exhibits a pattern that traces back to an Earth-Bet monument:
  - *Enclosed-space + helplessness* → locker pattern, trigger-event-adjacent.
  - *Cruelty-as-entertainment + child-harm* → locker pattern, S9-pattern.
  - *Helpless-protector-figure / dying-tutor* → Annette-death pattern, the locker's tutor-side, possibly Coil-Dinah-resolution pattern.
  - *Sudden fauna silence at scale* → Endbringer-arrival pattern.
  - *Fire-at-scale* → Bakuda-bombing pattern, possibly Behemoth-pattern.
  - *Institutional record-cruelty / administrative-violence* → PRT-trigger-period pattern.
  - *Mass-casualty foreshadowing / inevitable-disaster register* → Gold Morning / Khepri-period load.
  - *Deliberate isolation by adult authority* → school-locker-period social-isolation pattern.
- **Westerosi-monument clamp.** A proto-line is adjacent to a Westerosi monument that the interior knows from foreknowledge:
  - *Conquest-dating cue (provisional, charter, decree, succession-language)* → Conquest / Dance succession-clamp.
  - *Dragonriding / dragon-mention / Targaryen succession* → Dance-of-Dragons clamp.
  - *Northern-loyalty / cold-justice register* → Hour-of-the-Wolf clamp.
  - *Harrenhal-precinct cues / curse-language / castle-as-precedent* → Harrenhal-burning clamp.
  - *Faith-Militant adjacency / sword-bearing-septs cue* → Maegor-period clamp.
  - *Doom-pattern (sudden-disaster-of-civilization, vanished-empire register)* → Doom-of-Valyria clamp.
- **Intra- or cross-episode callback.** A proto-line lights a prior fire (memory-flag, narrator-interest, state-update) by direct continuity:
  - Calling back to a prior memory-flag's monument family in a way that updates or re-triggers it.
  - Calling back to a prior proto-line by event-rhyme (e.g., second confrontation echoes first).
  - For s01e01, intra-episode callbacks are the only callback class available. Cross-episode callbacks become eligible from s01e02 onward.

ACCEPT signatures:
- The entry's target-reference names the monument or callback target precisely. The description names the *cue* the proto-line provides without naming the monument.
- The trigger is plausibly active at this beat. (Example: @33 *the door stays shut* with Osmynd dying behind it lights the helpless-protector / dying-tutor pattern; @50 *taylor turns to mira* does not light any monument.)
- The cue mode (displacement / clamp / callback) is identifiable from the description's construction, even when not explicitly labeled.

REJECT signatures:
- **No-monument fire.** The entry fires on a beat where no behavior-pack monument is plausibly active. (E.g., a fire on @1 *the cart sits outside the timber gate* — there is no Earth-Bet pattern here, no Westerosi-monument adjacency, no callback target.)
- **Monument fabrication.** Citing a monument that is not in the behavior pack §"Memory monuments". Extension goes through margit; this rubric admits no on-the-fly monument additions.
- **Forced-fit.** Stretching a behavior-pack pattern to license a fire on a beat where the cue is not really present. *the beetles hold the seam* (@4) is the passive fauna-feed — this is base behavior, not a monument-trigger by default. A fire here would need an explicit Endbringer-pattern displacement cue (sudden silence, mass disturbance), which @4 does not exhibit.

### 2. Displacement-discipline

Does the description field hold the hard-fence discipline (no proper noun, no monument named) while still demonstrably carrying the monument's weight?

The base-card rule is explicit: "Surface as displacement only. … The interior knows; the spoken line does not name. The reader feels the weight without the cause being articulated." (`taylor-hebert-westeros.card.md` §"Memory monuments / Earth-Bet monuments".) The variant card's "negation-by-naming permitted at low frequency" carve-out applies only to *interior-circling* constructions like *this was not the year [X]* — and is reserved for prose contexts, not for memory-flag descriptions.

ACCEPT signatures:
- **Displacement-cue construction.** The description names the *shape* of the monument without naming the monument. Licit constructions:
  - *the door stays shut and what is on the other side stays the size she will not name* (refusal-to-look on enclosed space + dying-tutor).
  - *she has heard the shape of that word before in another tongue* (foreknowledge-clamp on a word that travels — narrator-interest @48 exemplar).
  - *the frame's shadow holds the size it has been* (refusal-to-look + doubled-register; narrator-interest @73 exemplar).
  - *the word is older than this country's name for it* (Westerosi-monument-clamp without naming the monument).
- **Clinical-of-the-horrible.** When the registration is dark, the prose stays flat. The gap between the content and the register is the load.
- **Inventory-tell carry.** What the fauna are doing under the monument's pressure, what the body is doing, what the cost is — instead of what the feeling is. Base-card register honored.
- **POV-restriction.** The description is from the POV character's interior. No third-person omniscient memory-flag, no "the officer remembers".

REJECT signatures:
- **Monument-leak.** Description names an Earth-Bet proper noun or Dance-specific (date, name, content) or any other behavior-pack monument explicitly. Hard fence; reject.
- **Stage-named cue.** *she remembers her old life* / *she thinks of home* / *the memory rises*. Naming the *act* of remembering rather than producing the displacement. The description should be the *cue*, not a label saying "this is a memory."
- **Affirmation-by-naming.** *this is the locker again* / *Bakuda's fire* / *the Dance is nine years out*. Hard fence; reject. (Even the variant card's "negation-by-naming permitted at low frequency" carve-out is for prose, not memory-flag descriptions.)
- **Mask-bleed.** Writing the description in spoken Westerosi-mask register (apologetic, deferent, *if it please you ser* tone) instead of base-register interiority. The interior does not perform. Reject.
- **Generic monument-gloss.** *something old surfaces* / *a memory presses* — generic monument-language without producing a specific cue. The displacement must produce the *shape* of the specific monument; otherwise the entry is a non-fire dressed as a fire.

### 3. Licensing-discipline

Does the entry honor the licensing-layer function — sparse, quiet-beat-anchored, narrator-interest co-cited, audience-meaningful, per-scene-capped?

This is the axis most novel to memory-flags. The other facets do not carry licensing-layer weight; memory-flags does. Authoring discipline reflects the stake.

ACCEPT signatures:
- **Quiet-beat anchor.** The fire's anchor proto-line is at tens=1 OR at the trailing edge of a tens=2 (release-zone, settling-after-the-spike). Tens=3 fires are forbidden by default; an exception requires explicit displacement-clamp construction AND a defensible argument that the monument lit *because* of the peak's discharge (narrator-interest carries the peak; memory-flags carries the resonance after).
- **Narrator-interest co-citation.** Mandatory. Every memory-flag entry must have a narrator-interest fire on the *same* `@<proto-line-id>`. The narrator-interest entry is the spine; memory-flags is the spine's monument-content. A memory-flag without a co-cited narrator-interest entry is suspicious — the narrator should have registered the trigger before the memory fired.
- **Audience-meaningfulness (load-bearing).** The fire's anchor proto-line must be a beat where **both** the POV interior registers monument-pressure AND the audience would feel the beat as load-bearing. A beat where only the narrator's interior reaches a monument (interior foreknowledge invisible to a reader without source-material fluency) does NOT earn a fire — the licensing layer is for content the stitcher will render in a way the audience can feel, and a monument-fire that only insiders can perceive does not earn the stitcher's metaphor / callback license. The both-meaningful test is the audience-side complement to the narrator-interest spine: spine = interior; meaningfulness = exterior; both must fire on the same beat.
- **Functional-register fire (load-bearing).** The fire must land at a beat that is doing one of four functional jobs at the storytelling level — and at least two of them simultaneously, not just one:
  - **Moment of realization** — the beat reveals something to the POV character that the audience also catches.
  - **Grim humor** — dark-comic pressure where the gap between content and register is the load (clinical-of-the-horrible register surfacing).
  - **Social commentary** — institutional / structural critique surfaces through the cue (administrative-violence pattern; peer-betrayal-as-cost; smallfolk-curse-as-history).
  - **Painting characterization** — the cue does work that establishes or reveals character (Taylor's monument-history; or a non-POV character's role surfacing).
  A beat that does only one of these four jobs is not yet earning the licensing layer's render-weight; the entry should refuse and let the beat carry surface-level prose alone. A beat that does two or more is candidate-eligible; if four converge, the fire is structurally overdetermined and almost certainly correct.
- **Multi-justification gate.** Each fire must produce **several converging justifications** for attaching the flag. A single justification (just spine present, just monument-trigger lit, just functional-register hit) is insufficient. The author must be able to name multiple converging reasons at ceiling-defense time: monument-trigger + spine-present + audience-meaningful + ≥2 functional-register hits + scene-eligible (no prior fire in scene). If the author cannot defend with several justifications, REFUSE. **The default is silence.**
- **Per-scene cap.** **At most one memory-flag entry per scene.** A scene with two or more memory-flag fires is over-firing the licensing layer for that scene; the stitcher cannot meaningfully gate metaphor / callback density across multiple licensed beats in a single scene. Scene boundaries follow the dramatist's locked scene-frame definitions where available, or the tensometer-derived structural marks (long-flat-then-charged-then-released cycle). Two co-fired entries on a *single beat* (the doubled-register exemplar pattern from earlier rubric drafts) are also forbidden under per-scene cap — one beat is a member of one scene, and the scene gets one fire.
- **Sparsity discipline.** The file fires on **1–5% of proto-lines** for episode-length corpora (~1–4 entries on 77 beats for s01e01; ~3–10 entries on a 232-beat episode like s01e03). The earlier 5-12% draft band was too generous; the per-scene cap and both-meaningful criterion together pull the density floor down. Sparsity is *the* load-bearing rubric property. Far better to under-fire and miss a monument than over-fire and dissolve the licensing layer.

REJECT signatures:
- **Per-scene over-firing.** Two or more entries in a single scene. Cull to the strongest fire (most audience-meaningful, most distinct cue, strongest monument family).
- **Narrator-only fire.** A fire on a beat that lights monument-pressure interior-only (only Worm-fluent or ASOIAF-fluent readers can perceive the cue). Reject; the beat is correctly silent at the licensing layer.
- **Density-on-flat / density-inflation.** Firing on every quiet beat to hit coverage. The licensing-layer function depends on contrast.
- **Single-register file (file-level, soft).** A single episode that fires only Earth-Bet OR only Westerosi may be acceptable when the both-meaningful gate forces single-register selection (Westerosi monuments are by-construction interior-foreknowledge and frequently fail the audience-meaningfulness test; Earth-Bet displacements more frequently survive both-meaningful gating). **Doubled-register coverage is per-season, not per-episode.** A season that ends with one register having zero fires is the file-level kickback signal; an episode that lands single-register is acceptable when the both-meaningful test demands it.

REJECT signatures:
- **Peak-anchored fire without displacement-clamp argument.** A fire on a tens=3 beat where the interior is fully committed to the action and no displacement / clamp construction earns the resonance. Reject.
- **Missing narrator-interest co-citation.** A fire on a beat where narrator-interest is silent. The narrator must have registered the trigger first; if she didn't, the memory-flag is firing without spine. Reject or flag back to narrator-interest author for missed-fire repair.
- **Density-inflation.** Firing on every quiet beat to hit a coverage target. The licensing-layer function depends on contrast; saturating the file destroys the gradient as surely as silence does.
- **Single-register file.** All fires on one register (all Earth-Bet displacement, no Westerosi clamp; or vice versa). File-level reject; the doubled register is the load-bearing structure.
- **Persistent-monument-firing.** Same monument lighting on consecutive beats with the same cue. One fire per monument-trigger; the next fire on the same monument must register a *change* in how the monument lights (intensification, release, displacement-shift), not a repetition.

---

## Cross-axis tests

- **The monument-name test.** Name the monument family in five words or fewer (e.g., *locker — enclosed + helplessness*; *Dance-clamp on succession-word*; *Harrenhal-precinct curse-language*). If you cannot name the monument family, do not fire.
- **The displacement-cue test.** Read the description aloud. Does it name a *shape* without naming the monument? If a behavior-pack-trained reader recognizes the monument from the cue, the description passes. If the description either names the monument or fails to produce the shape, it fails.
- **The licensing test.** Strip the entry. Without it, can the stitcher produce metaphor or callback at this beat? If no (licensing-layer working), the entry is doing real work. If yes (the beat already licenses figurative reach by other route — e.g., editor-only taste-call), the entry is parasitic.
- **The quiet-beat test.** Look up the beat's tensometer rating. If 1, default-licit. If 2 (trailing edge — release-zone), defensible with cue. If 2 (rising edge — approach to peak), contested; require explicit argument that the monument is reaching backward, not forward. If 3, default-forbidden; require explicit displacement-clamp construction and resonance-not-action argument.
- **The narrator-interest spine test.** Locate the beat in the locked narrator-interest file. If silent, REJECT or flag back. If fired, the memory-flag entry must be consistent with what the narrator-interest entry registers — they cannot contradict on which channel/trigger lit.
- **The doubled-register test (file-level).** Across the file, at least one Earth-Bet displacement fire AND at least one Westerosi-monument clamp fire. A file with only one register visible is a fail.
- **The hard-fence test.** Search the description field for proper nouns (Earth-Bet specifics: locker, Bakuda, Leviathan, Khepri, Annette, Brockton, S9, Endbringer, Cauldron, PRT, Wards, etc.; Dance specifics: Aegon, Rhaenyra, Aemond, Vhagar, Dance, Hour, Doom, etc. by name) and post-Conquest-dating-stamps that name the year. If any present, REJECT.

---

## Anti-patterns (named for the rubric)

These are the contamination patterns the writer must resist and the reviewer must call out.

1. **Monument-leak.** Description names an Earth-Bet proper noun or Dance-specific. Hard fence. Reject.
2. **Affirmation-by-naming.** *This is the locker again.* Hard fence. Reject.
3. **Stage-named cue.** *She remembers ... / a memory rises ...* — labeling rather than producing the cue.
4. **Generic monument-gloss.** *Something old surfaces.* No specific shape.
5. **Forced-fit / no-monument fire.** Firing where no behavior-pack monument is plausibly active.
6. **Peak-fire without resonance argument.** Fire on tens=3 beat where the interior is fully committed and no displacement-clamp construction earns the load.
7. **Spineless fire.** Memory-flag fire on a beat where narrator-interest is silent. The narrator must register the trigger first.
8. **Density-inflation.** Firing on every quiet beat to hit doubled-register coverage. Saturation destroys the licensing-layer gradient.
9. **Single-register file (file-level).** All Earth-Bet, no Westeros, or vice versa. The doubled register is load-bearing.
10. **Mask-bleed.** Description in spoken Westerosi-mask register instead of base-register interiority. The mask is performance; interior does not perform.
11. **Persistent-monument-firing.** Same monument lighting on consecutive beats with the same cue. One fire per trigger; next fire registers change.
12. **Author-vocabulary leak.** Reaching for a stock pattern under pressure (cf. narrator-interest's *stays the size [X]* watch). Memory-flag descriptions echoing each other across an episode is a kickback signal.
13. **Cross-POV memory.** A memory-flag for a non-POV character's interior. Memory-flags are POV-restricted; non-POV interior memory is feeling-flags' or that character's narrator-mode-fork's territory.
14. **Target-reference erosion.** The target-reference field becoming sloppy across a file (free-text glosses where card slugs exist; missing target-references; vague glosses like *(earth-bet)* without specifying which monument family). The metadata is the stitcher's routing surface; sloppy metadata breaks the metaphor-facet contract.

---

## Curve-shape rubric (file-level)

The memory-flags file as a whole must demonstrate licensing-layer shape across the episode. The mechanic auditor checks the curve in addition to per-entry correctness.

### Episode-level shape

The full memory-flags file across an episode must satisfy:

- **Sparsity.** 5–12% of proto-lines fire (s01e01 expected: ~4–9 entries on 77 beats). Sparsity is the load-bearing rubric property.
- **Inverted tens-density alignment.** Memory-flags fires cluster in 1-zones and 2-zone trailing edges. Ratio of fires-per-beat in 1-zones (and tens=2 release-zones) to fires-per-beat in tens=3 zones should be **at least 3×** (ideally infinite — zero tens=3 fires). This is the inverse of narrator-interest's curve. The mechanic auditor checks this explicitly.
- **Doubled-register visibility (file-level).** At least one Earth-Bet displacement fire AND at least one Westerosi-monument clamp fire. A file with only one register is a fail. (For s01e01 expectations: at least one Earth-Bet displacement on @33/@34 region — dying-tutor / refusal-to-look — and at least one Westerosi-monument clamp on @48/@63 region — Conquest-dating / record-monument.)
- **Monument-family diversity.** Across an episode of >50 beats, expect at least three distinct monument families exercised across the fires (e.g., refusal-to-look-on-dying-tutor, Conquest-clamp-on-record-language, frame-shadow-displacement). A file that uses only one or two monument families is undercovering — even if the registers are doubled, the monument inventory is impoverished.
- **Quiet-beat distribution.** Fires distribute across the episode's tens=1 zones, not concentrated in one stretch. A file where all memory-flags fire in @50–@77 (release-zone) is back-loading; a file where all fires cluster at @1–@22 (approach-zone) is front-loading. Both fail file-level: the doubled register should show across the whole episode.

### Scene-level shape

For each scene (per tensometer's scene-frame definition):

- **At most one fire per scene per monument family.** A scene that fires the locker pattern at @33 and again at @34 is over-firing the same monument. Cull to the strongest fire; the second beat is silent.
- **Approach-zone permitted-sparse but eligible.** Long approach zones (@1–@22 in s01e01) are eligible for memory-flag fires when the monument lights — the cart, the gate, the empty yard can all carry monument-pressure (foreknowledge-clamp on the institution-arrival, Endbringer-pattern in fauna-silence). The default expectation is sparse, not zero.
- **Release-zone is the highest-density zone.** Memory and monument fire when the foreground tension releases. Expect the @70–@77 close-zone (s01e01) to carry the highest density of memory-flag fires per beat — but still constrained by sparsity.

### When curve-shape fails

The author's response to a failing curve is **not** to inflate fires to hit density. The response is:

- **Doubled-register fix.** If only one register fires, audit which monument-family-adjacent beats were skipped. Add fires where the cue is genuine.
- **Monument-family-diversity fix.** If the file fires only on one monument, audit which other monuments could have lit and were skipped. Add fires where genuinely earned.
- **Quiet-beat-distribution fix.** If front-loaded or back-loaded, audit the unfired half for monument-adjacent beats. Add fires where genuinely earned.
- **Tens-inversion fix.** If fires cluster on tens=3 beats, the file is misreading the rubric. Strip the tens=3 fires (none should survive ceiling-defense unless explicit displacement-clamp construction and resonance-not-action argument hold).

Inflating fires to hit density without earning each fire on all three axes is the prohibited move.

---

## Cross-facet contract

Memory-flags' upstream and downstream consumers.

### Anchor expectations (consumer side)

- **Narrator-interest (locked, upstream).** Mandatory @-co-citation. Every memory-flag entry must have a narrator-interest fire on the same `@<proto-line-id>`. The narrator-interest fire is the spine; memory-flags is the monument-content layer. A memory-flag without spine is an authority violation. The narrator-interest cross-facet contract notes name @33, @34, @48, @73 as strongest memory-flag anchor candidates; @48 specifically as foreknowledge-clamp on "provisional" — Earth-Bet shadow + Dance-timeline-brush co-citation expected.
- **Tensometer (locked, upstream — inverted contract).** Memory-flags fires concentrate in tens=1 zones and tens=2 trailing edges. Tens=3 fires are forbidden by default. The tensometer cross-facet contract is the inverse of narrator-interest's: where narrator-interest aligns to peaks, memory-flags aligns to gaps. Tensometer's @39 STATE-UPDATE NOTE forbids canonical state-update co-citation; the same beat's memory-flag eligibility is contested (held-against-turn class, peak — default-forbidden for memory-flags; possible exception under explicit foreknowledge-clamp resonance argument, but the default is silence). Tensometer's @64 STATE-UPDATE NOTE expects state-update co-citation; memory-flags at @64 is also contested (peak — default-forbidden; the resonance fires after, at @65+). Authors should default to firing in the *aftermath* of peaks, not on them.
- **Behavior pack (authority).** §"Memory monuments" of `cards/dialects/taylor-hebert.card.md` and `cards/dialects/taylor-hebert-westeros.card.md` is THE list. Monument extension goes through margit, not through this rubric.

### Back-contract (what memory-flags owes downstream)

- **Stitcher (primary consumer).** Memory-flags fires license the stitcher to render figurative content (callback, simile, allegory, dark-humor) at the fired beat. **Absent fires forbid such content.** The stitcher reads memory-flags as the gating boolean for the metaphor facet.
- **Metaphor facet (downstream, editor-authored).** Editor authors metaphor entries against memory-flag fires. A metaphor entry on a beat without a memory-flag is a cross-facet violation; cross-facet consistency culls it (per schema's contradiction rule: delete both, flag re-author).
- **Audience-interest flags (advisory).** Audience personas may have interest-flag fires on memory-flag-fired beats; aggregate audience-interest density on memory-flag fires is expected to be elevated (the beats *are* monument-loaded; multiple audience perspectives notice).
- **State-updates (no relationship).** Memory-flags is a registration facet, not a structural-delta facet. State-updates do not condition on memory-flags and vice versa.

### What memory-flags does NOT condition

- Tensometer (forward). Memory-flags does not change tens. If a beat's memory-flag entry suggests higher charge than its tens scalar, the auditor flags for cross-facet review — but tens stays locked.
- Narrator-interest (forward). Memory-flags does not change narrator-interest. (It does *require* a narrator-interest fire on the same beat; missing co-citation is a kickback to narrator-interest, not a fork-and-author by memory-flags.)
- Vibes-updates. Vibe shifts are showrunner's call.

---

## Calibration anchors (drawn from s01e01 corpus)

Six worked examples spanning the rubric. Used during Phase 1 reviewer tuning and Phase 2 writer-fork.

- **`s01e01:33 the door stays shut` — FIRE.** Tensometer=2 (stakes-visibility on Osmynd's unavailability newly registered as public fact). Narrator-interest @33 fires (refusal-to-look + clinical-of-the-horrible). Monument: Earth-Bet displacement on dying-tutor / helpless-protector pattern (locker-adjacent: enclosed-space + helplessness; also Annette-death-adjacent: parent-figure failing). Description shape: *the threshold holds and what is on its other side is the size she will not name* (echoes the narrator-interest entry; the memory-flag entry can reference the registration without naming the monument). Target-reference: `monument-locker` or free-text gloss `(earth-bet: dying-tutor / helpless-protector pattern)` if the monument card doesn't yet exist (margit referral candidate). ACCEPT.

- **`s01e01:48 the officer dictates taylor's name as provisional labor-eligible` — FIRE.** Tensometer=2 (stakes-visibility on formal dictation; documents prior turn — release-zone of the @38–@39 cluster). Narrator-interest @48 fires (foreknowledge-clamp on "provisional"). Monument: Westerosi-monument clamp on succession-language — *provisional* is the word that travels (Conquest-charter language, Dance-succession-language; cf. variant card §"Memory monuments / Aegon's Conquest" + §"Dance of the Dragons"). Description shape: *she has heard the shape of that word before in another tongue* (the narrator-interest entry IS this shape; the memory-flag entry can register the monument-pressure underneath). Target-reference: `monument-conquest-charter-language` or `monument-dance-of-dragons` (the word *provisional* lights both — author choice is foreknowledge-direction; default to the closer monument). **NOTE:** the locked narrator-interest cross-facet note specifies "Earth-Bet shadow + Dance-timeline-brush co-citation expected" — the memory-flag for @48 may co-fire with a *second* memory-flag entry routing to Earth-Bet shadow if a distinct displacement cue is present. For s01e01, default to single-entry @48 with target-reference on the Westerosi-monument; the Earth-Bet shadow at @48 is dispersed across the cluster and surfaces more cleanly elsewhere. ACCEPT one fire.

- **`s01e01:73 taylor steps into the shadow of the frame` — FIRE.** Tensometer=1 (release-zone, episode-close approach). Narrator-interest @73 fires (refusal-to-look on the frame's shadow; doubled-register exemplar). Monument: Westerosi-monument clamp on Harrenhal-precinct / threshold-as-monument pattern (variant card: Harrenhal's burning, the local current-pressure monument; the sept doorway is in Harrenhal's shadow), AND Earth-Bet displacement on enclosed-space / refusal-to-look pattern (locker-pattern; the frame is a doorframe is the threshold). Two registers genuinely co-fire here; this is the doubled-register exemplar beat. Description shape: *the frame holds the size it has been; what is on its other side is what she will not name* (narrator-interest entry construction). Target-reference: choose primary monument; secondary is the cross-register note. Default: `monument-harrenhal-precinct` primary; free-text gloss `(earth-bet: enclosed-space displacement)` or second entry on same beat if both registers earn distinct cues. **NOTE:** narrator-interest @73 is flagged in the cross-facet contract notes as a strong memory-flag anchor candidate. Authoring decision: single entry preferred (sparsity discipline); both registers may surface in the description's two-clause shape. ACCEPT.

- **`s01e01:34 the beetles hold osmynd on the pallet` — CONTESTED.** Tensometer=1. Narrator-interest @34 fires (refusal-to-look continuation; passive-fauna register continued). Monument: same as @33 (Earth-Bet displacement on dying-tutor pattern). The contested call is whether @34 is a *second fire on the same monument* (anti-pattern #11 — persistent-monument-firing) or a *change-registration* on the monument (the beetles are now actively holding the dying-tutor frame; the displacement is intensifying, not repeating). Default: REFUSE @34 if @33 fires. The single-fire-per-monument-per-scene rule applies; @33 is the stronger fire. If @33 is not fired (e.g., authoring decision routes the dying-tutor monument to @34 via fauna-feed channel rather than refusal-to-look channel), then @34 fires and @33 is silent. Not both. Refusal-CORRECT for @34 if @33 fires.

- **`s01e01:38 taylor puts the letter into the air in front of the officer` — REFUSE.** Tensometer=3 (climax peak; body-charge + reversal-proximity). Narrator-interest @38 fires (age-mismatch + cost-tracking). Monument: candidates exist (cape-deployment-as-commit pattern → Earth-Bet displacement on cape-context; child-doing-adult-action → age-mismatch already carried by narrator-interest). But the foreground charge is at peak, the body is fully committed to the action, and no displacement-clamp construction earns the resonance — the interior is in the *act*, not in the load behind the act. The licensing-discipline axis fails on quiet-beat anchor: tens=3 default-forbidden, and no explicit displacement-clamp construction earns the exception. Refusal-CORRECT. The monument resonance, if it surfaces, lights at @40–@41 (release after the commit) or @43 (officer's response) where tens drops back to 1.

- **`s01e01:50 taylor turns to mira` — REFUSE.** Tensometer=1. Narrator-interest @50 silent (refusal-CORRECT per the locked file's @50 calibration anchor: turning is transitional, no channel lights). Monument: no behavior-pack monument plausibly active (peer-interaction in release-zone; no cue surfaces). Refusal-CORRECT on the no-monument-fire test. (Note: spineless-fire test would also reject any fire here, since narrator-interest is silent.)

---

## Author / reviewer notes

- **Author:** dialogue-writer fork for the POV character (interiority output mode of the same fork that writes spoken dialogue and authors narrator-interest). For `taylor-hebert-westeros`, the fork loads: base behavior card (§"Memory monuments / Earth-Bet monuments"), Westeros-variant card (§"Memory monuments / Westerosi monuments + local-current"), persona card, the locked tensometer file (for inverted-tens-density check), the locked narrator-interest file (mandatory spine co-citation), the locked location-state file (soft alignment), and this rubric. **Two-pass authoring:**
  1. **Per-beat pass.** Walk the proto-line file. For each beat, decide FIRE or NONE. If FIRE, write the description (displacement-cue discipline), name the monument family in the target-reference field, verify narrator-interest co-citation, verify quiet-beat anchor.
  2. **File-shape pass.** Read the file as a curve. Check episode-level density (5–12%), inverted tens-density (3× or better in 1-zones vs 3-zones), doubled-register visibility (Earth-Bet AND Westerosi clamp both fire), monument-family diversity (≥3 families across the file), quiet-beat distribution (no front- or back-loading). Either fix misfires (NONE→FIRE add for missing coverage; FIRE→NONE strip for density-on-flat-1) or flag screen-writer kickback for structural gaps. **Do not inflate to hit density.**
- **Reviewer (mechanic auditor):** under this rubric. Per-entry verdict for fires: CORRECT (all three axes earned, no anti-pattern fired) or INCORRECT (named axis-failure or anti-pattern). Per-entry verdict for refusals: CORRECT (no monument earned) or MISSED (a monument-family + cue earned a fire that the author skipped). File-level verdict: SHAPE-OK / SHAPE-FAIL with named density / register / family-diversity / tens-distribution failure mode. Cross-facet contract pre-ship check is mandatory (narrator-interest co-citation; tensometer inverted-density alignment; behavior-pack authority).
- **Reviewer (dialect audience):** under this rubric, fidelity-only mode. Worm-canon-pedant primary (calibrated to Earth-Bet monuments per `cards/dialects/taylor-hebert.card.md` §"Memory monuments"); dark-fantasy-reader and pulp-enthusiast secondary (calibrated to Westerosi-monument fidelity AND figurative-reach taste — does the description carry the dark-fantasy weight without over-flowering or under-firing). Per-entry verdict: VOICE-OK / VOICE-FAIL / VOICE-MIXED with citation to behavior-pack §. The dialect audience does NOT adjudicate the firing decision (mechanic does), the quiet-beat anchor (mechanic does), the licensing-discipline curve (mechanic does), or the cross-facet contract (mechanic does). Their domain is monument-fidelity and displacement-cue voice.
- **Verdict combination.** Mechanic + dialect verdicts are independent gates. Both must pass; either reject = revise. They cannot substitute. Same architecture as narrator-interest.
- **Cull:** memory-flags has per-file cull (per `schemas/facet.schema.md`). Cull is delete-only — entries that fail any axis or any anti-pattern are deleted. No rewrites at cull time. The Phase 2 writer-fork output IS the cull-stage authoring; revision happens in Phase 4 only.
- **Floor defense.** If the author defends a NONE against a reviewer push to FIRE by citing rubric (no monument earned, no displacement-cue lights, peak-without-resonance), accept the defense. Sparsity is load-bearing; over-firing dissolves the licensing layer.
- **Ceiling defense.** If the author defends a FIRE that the reviewer would push to NONE, the burden is on the author to name (a) the monument family, (b) the cue (displacement / clamp / callback), (c) the narrator-interest co-citation, (d) the quiet-beat anchor justification, (e) the cross-facet contract slot the entry serves (which metaphor / callback content the licensing fire enables for the stitcher). A FIRE that survives ceiling defense should also pass the doubled-register file-level test and the hard-fence test.
- **Cross-author dependencies.** Memory-flags is single-author (POV-character fork). No cross-author dependency check at Phase 5; the cross-facet contract check (vs. narrator-interest, tensometer, behavior pack) replaces it.

---

## V1 lenient form (retained for lift comparison only)

V1: ACCEPT iff the entry is form-correct (well-formed description, target-reference, anchor-to-real-proto-line) AND any monument-family is plausibly invoked at any reading. No displacement-discipline check, no licensing-discipline check, no curve-shape check, no narrator-interest co-citation requirement, no hard-fence check.

V1 exists only to produce a baseline accept-rate for round-trip comparison after writer-tuning. It is not an authoring target. Do not soften V2 toward V1 between rounds.

---

## What memory-flags is not

- Not narration. Not paraphrase of the SVO. Not author-monument-cataloguing.
- Not editable after cross-facet consistency. Once locked, entries are an input to the stitcher and to metaphor-facet authoring; cannot be retuned without restarting the consistency pass.
- Not the only locus of monument-presence in the prose. Narrator-interest carries the registration of monument-pressure (the *shape* the interior reaches around); behavior-pack §"Voice tells" instructs the impersonator on how the voice carries the monument when speaking. Memory-flags is the *licensing-layer index* specifically — the citable record of which monument lit where, for which the stitcher reads as gate.
- Not symmetric across POV characters. Each POV character's memory-flags rubric instance must be re-authored against that character's behavior pack §"Memory monuments". The structure transfers; the monument inventory and calibration anchors do not.
- Not a metaphor file. Editor authors metaphors against memory-flag co-citation. Memory-flags' description field uses displacement-cue construction (which can be mistaken for metaphor), but the description is a *registration of the cue*, not a metaphor for the proto-line. The metaphor facet is downstream and editor-authored.
