# Feeling-Flags Corpus — s01e01

Stratification of s01e01 (77 proto-lines) for the **feeling-flags** facet tuning. Phase 0.

---

## Scope

Feeling-flags fire when a character (POV or non-POV) **shows** an interior state through a somatic tell — body, gesture, posture, breath, gaze, micro-action — and the audience cannot read that interior from the proto-line content + already-existing facet citations alone. The somatic tell IS the entry; the named feeling is forbidden in description.

Per-character per-scene cap: **≤1**. POV (narrator/Taylor) and each on-screen non-POV character each get at most one fire per scene. Make it count.

Schema content shape (revised; ships at Phase 5 with facet file):

```
<id> @<proto-line-id> <character-slug>: <somatic-tell-one-clause> | expressed: <yes|partial|no>
```

The `| feels: ... |` metadata field from the schema's prior shape is **removed**. Naming the feeling is forbidden. The somatic tell carries it.

`expressed:` denotes whether the in-scene audience (other characters present) can read the tell — `yes` (visible to others present), `partial` (visible to attentive observer), `no` (interior-only; tell is for narrator-perception, not in-scene-perception). The reader (audience) always sees it; the field tracks in-scene legibility.

---

## Scene partition

| Scene | Beats | Locale | On-stage characters |
|---|---|---|---|
| 1 — Approach / Arrival | 1–13 | sept yard, exterior | mira, edric, clerk, officer (entering); osmynd off-stage behind sept door |
| 2 — Line / Processing | 14–48 | yard | taylor, mira (adjacent), edric (peripheral, then off-stage), clerk, officer |
| 3 — Aftermath / Dictation | 49–67 | yard | taylor, mira, edric (in/out via door), clerk, officer |
| 4 — Departure / Crossing | 68–77 | yard → sept threshold → interior | taylor; clerk + officer departing; mira off-stage |

Note: scene boundaries are pre-cut estimate, will be confirmed against location-state file at Phase 2 writer-fork load. Edric exits to sept @57 then likely returns or remains inside.

---

## Per-character candidate beats

### Taylor (POV; ≤1/scene, ≤4 episode)

Loads narrator-interest as cross-facet anchor (mandatory check; feeling-flag for POV must NOT redundantly cover NI's existing fire).

- **Scene 1 (1–13):** Taylor not on stage. **0 candidates.**
- **Scene 2 (14–48):**
  - @14–15 (cross / enters line): default body-motion; Q1-interior probably reads from proto-line + NI. Likely refuse.
  - @19 (stops in line): default. Refuse.
  - @37–39 (steps into officer's path / puts letter in air / sets feet where his next pace commits): commit-stance. **Strong candidate** — the body-set at @39 carries the choice; "sets her feet" is somatic-show-of-resolve; NI may register the cost-tracking but does not show the body-commit. Audience needs the show.
  - @45 (palm closes on letter): possible. Probably proto-line carries.
- **Scene 3 (49–67):**
  - @50–51 (turns to mira / speaks): the turn is the somatic-show-of-asking; NI may register hope but not the body-pivot. **Candidate.**
  - @54 (speaks across yard to edric): similar pattern.
  - @61–66 (officer speaks to her, twice): no candidate; she is target, not actor.
- **Scene 4 (68–77):**
  - @70–73 (turns to sept door / steps on dirt / steps on stone / steps into shadow of frame): the threshold-cross; sequence carries the cost. **Candidate** — possibly @73 (steps into shadow, lit/lit-out shift) or @77 (goes through the door). Need disambiguation: NI likely fires on the threshold; does feeling-flag duplicate?
  - @74 (fist holds the letter): grip-on-document; somatic tell of held-cost. Candidate; weaker than threshold.
  - @75–77 (finds latch / lifts latch / goes through door): mechanical actions; @77 carries weight.

**Estimated Taylor fires: 2–4 across 4 scenes (cap 4).**

### Mira-stonefield (≤1/scene)

Persona card §"Voice / The stillness beat" + §"Look / Stillness when assessing": her dominant tell is a stillness pause before responding. Forbidden registers (per card): performing fear, sentimentality, gratitude.

- **Scene 1 (1–13):**
  - @5 (sets the bucket): default; refuse.
  - @6 (straightens): the assessment-stillness candidate per signature-move-1 ("the stillness beat"). **Candidate** — depends on whether @6 captures the assessing pause or just the physical straightening.
  - @7 (speaks to the yard): speech action; tells live in dialogue, not feeling-flags. Refuse unless body-tell precedes speech.
- **Scene 2 (14–48):**
  - @16 (elbow presses near taylor's shoulder): proto-line IS the somatic tell of practical-support. Q1-interior fails. Refuse.
- **Scene 3 (49–67):**
  - @52 (drops eyes to flagstones): proto-line IS the tell. Per user's example forbidding redundant flagging on already-shown feelings. Refuse.
  - @53 (holds eyes on flagstones): the held-pose extends @52's drop. This may license a fire that COMPOUNDS @52: the holding amplifies what the drop alone does not say (sustained refusal-to-look = refusal-to-witness, not just shame). **Candidate** — depends on whether holding adds disambiguation that drop alone lacks.
- **Scene 4 (68–77):** mira off-stage. **0 candidates.**

**Estimated Mira fires: 0–2 (cap 4).**

### Edric-cray (≤1/scene)

Persona card §"Voice": low register; does not perform fear or courage; specific stillness when assessing per §"Look". §"Signature Moves / The exit check first": exits-thinking is structural.

- **Scene 1 (1–13):**
  - @8 (holds eyes on road past cart): proto-line IS the refusal-to-look-at-officer; carries the assessment-stillness directly. Q1 fails. Refuse.
- **Scene 2 (14–48):** edric peripheral; no fire-eligible beats.
- **Scene 3 (49–67):**
  - @54 (taylor speaks to him): target, not actor.
  - @55 (looks at officer): registration; not yet a feeling-show.
  - @56 (looks at taylor): the look is the moment of decision. Possible candidate.
  - @57 (steps back through the door): the retreat. **Strong candidate** — the step-back is the somatic-show of withdrawal-for-self-preservation; the cost is the act itself; proto-line carries the act but not the cost. NI likely registers his retreat as cost-tracking from Taylor's POV but doesn't carry HIS interior. Feeling-flag licenses it.
- **Scene 4 (68–77):** edric off-stage. **0 candidates.**

**Estimated Edric fires: 0–1 (cap 4; only Scene 3 plausible).**

### Census-officer (≤1/scene)

Persona card §"Voice / Forbidden registers": cruelty, hostility, relish, contempt, hesitation, **personal interest in Taylor as a person.** §"Hard Fences / He is not malicious. He does not take pleasure." Card structurally forbids interior performance.

- All scenes: officer's interior is procedural-flat by card. Multi-justification fails (no Q2-meaningful interior to show). **0 candidates across 4 scenes.**

**Estimated officer fires: 0** (rubric-correct refusal; the character's card structurally forbids feeling-show; the procedural register IS the feeling-flat character).

### Clerk (≤1/scene)

Persona card §"Voice / Forbidden registers": friendliness, malice, curiosity, apology. §"Hard Fences": professional reflex, not personal interest.

- @22 (stylus follows dictation), @24 (stylus stops on board), @58 (resumes), @63 (stops at margin), @64 (marks two parallel lines): all professional reflex; card forbids interior performance. **0 candidates across 4 scenes.**

**Estimated clerk fires: 0** (same as officer; card forbids feeling-show).

### Osmynd (off-stage)

No persona card authored. Off-stage at @33–34 (door stays shut; beetles hold osmynd on the pallet). The door staying shut MAY be a somatic-show-through-absence (he cannot come), but:
- No persona card → would require oc-* slug + margit referral (state-updates pattern).
- Off-stage interior is a Reading-C edge case; default refuse for s01e01.
- Card-less + off-stage + uncertain license → **refuse for s01e01.** Revisit if osmynd becomes on-stage in a later episode.

**Estimated osmynd fires: 0.**

---

## Decision matrix (Phase 0 estimate)

| Character | Sc1 | Sc2 | Sc3 | Sc4 | Total est. |
|---|---|---|---|---|---|
| taylor | — | 0–1 | 0–1 | 0–1 | 2–3 |
| mira | 0–1 | — | 0–1 | — | 0–2 |
| edric | 0 | — | 0–1 | — | 0–1 |
| officer | 0 | 0 | 0 | 0 | 0 |
| clerk | 0 | 0 | 0 | 0 | 0 |
| osmynd | — | — | — | — | 0 |

**Estimated total fires: 2–6.** Best estimate **3–4** (sparsity 4–5%).

This is sparser than NI (20 fires, 26%), denser than memory-flags (3 fires, 3.9%), close to sensory (5 fires, 6.5%). Frugal-by-design via per-character per-scene cap × low-fire-eligible-character count (officer + clerk + osmynd contribute zero by character-card structure).

---

## Cross-facet relationships expected

- **NI (POV):** mandatory check at Phase 2 — Taylor feeling-flag fires must NOT duplicate NI fires on the same beat. Distinct jobs: NI = what Taylor's attention lands on (cognition / perception / memory); feeling-flag (POV) = the somatic SHOW of her interior. Co-citation permitted; redundancy forbidden.
- **State-updates:** unrelated; feeling-flags is non-canonical (selection signal only); state-updates is canonical-write.
- **Sensory:** unrelated; feeling-flags is interior; sensory is environmental.
- **Loc-state:** soft alignment for scene boundaries.
- **Tensometer:** observation-only correlation expected. Some feeling-fires may correlate with high-tens beats (commit-stance @39 is t≥2 territory; threshold-cross @77 is high-tens); some with low-tens reflective beats (mira's stillness @6 may be t=1). **Tens-independence** like sensory; not gating.
- **Memory-flags:** independent. Memory-flags is licensing-layer for figurative; feeling-flags is registration of interior-show. No co-citation requirement either direction.

---

## Anti-patterns expected (rubric draft input)

1. **Labeled-feeling-leak.** "mira feels sad" / "edric feels afraid" / "taylor feels resolve" — even with somatic tell present. Description must contain ZERO named-feeling vocabulary. Anti-pattern #1.
2. **Audience-already-can-tell redundancy.** Firing on a beat where the proto-line + sensory + dialogue already convey the interior. The proto-line @52 "mira drops her eyes to the flagstones" IS the tell; firing feeling-flag at @52 is redundant. Anti-pattern #2 (Q1-interior).
3. **Cross-character omniscience.** Per-character fork licenses only its own character's feeling-flags. A taylor-fork firing for mira is authority violation. Anti-pattern #3.
4. **Off-stage feeling fire (without card).** Osmynd is off-stage; absent card; refuse. Anti-pattern #4.
5. **Procedural-flat-character forced into feeling-show.** Officer and clerk persona cards forbid interior performance. Firing feeling-flags for them is character-violation. Anti-pattern #5.
6. **Duplicate-with-NI for POV.** Taylor feeling-flag must distinguish from NI; if NI on the same beat already shows what feeling-flag would show, refuse. Anti-pattern #6.
7. **Vocabulary saturation.** Same somatic-tell verb across multiple characters or scenes (everyone "goes still", everyone "drops eyes", everyone "steps back"). Per-character behavior-card vocabulary distinct. Anti-pattern #7.
8. **Per-scene cap violation.** Two fires for one character in one scene. Hard refuse. Anti-pattern #8.
9. **Single-justification fire.** A fire with only one defending reason (e.g., "tens=3 so feeling fires"). Multi-justification gate (≥3) requires somatic-tell-card-match + Q1-audience-cant-otherwise-read + Q2-meaningful + scene-eligible + fork-of-record + ≥2 functional-register hits. Anti-pattern #9.
10. **Density-on-flat-tens.** Feeling-flags clustering on transition/peak beats only. Tens-independent rule says fires distribute across the curve; some at quiet beats (mira's stillness @6), some at peaks (commit-stance @39). Anti-pattern #10.

---

## Calibration anchors

For Phase 2 writer-fork:

- **Anchor (refuse):** @8 "edric holds his eyes on the road past the cart" — proto-line IS the tell; Q1-interior fails; refuse. Use as control: any writer firing this beat has Q1 calibration off.
- **Anchor (refuse):** @52 "mira drops her eyes to the flagstones" — same as above; the user's pre-Phase-0 framing names this case structurally.
- **Anchor (fire):** @57 "edric steps back through the door" — the act is in the proto-line but the cost-of-the-act is interior; feeling-flag licenses the show of withdrawal-cost. Multi-justification: edric-card §exit-check + Q1-interior (audience reads retreat but not its weight) + Q2-meaningful (scene's witness-or-not pivot) + scene-eligible (Sc3) + fork-of-record (edric).
- **Anchor (fire, POV):** @39 "taylor sets her feet on the dirt where his next pace commits" — body-commit; Q1 distinguishes from NI's cost-tracking on adjacent beats; Q2 is the episode's structural pivot (refusal-to-yield).

These four anchors calibrate the gate. A writer-fork that lands all four (refuse @8, refuse @52, fire @57, fire @39) has the rubric internalized.
