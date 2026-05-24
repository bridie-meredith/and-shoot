# Render-log — b01-c01

generated: 2026-05-24
slug: b01-c01
profile: schema defaults (no episode/project profile authored)
persona: neutral
narrator: taylor-hebert-kl-122ac
voice: first-person past-tense, contractions on (schema default)
phase-7-mode: per-scene (3 scene-forks; sentences walked serially inside each)
phase-1-mode: scene-window (default; boundaries from scene-map-b01-c01.md)
flags: cap-burn-aware (cycle-3 DELETE on coll-net-mender-flea-bottom:1 @8; bare-speech-bone @8 ACCEPTED-AT-CAP-BURN; see staff/auditor/facets-cap-burn-b01c01-20260524T021822Z.md)
prior_run: render-log-b01-c01.PRIOR.md (2026-05-19/20 — superseded by cycle-3 cap-burn redo; prior chain halted pre-Phase-1)

---

## Phase 0 — Validate + Load

- bones file present: `active-project/theater/bones/b01-c01.md` (27 bones; flat IDs 1-29 with time-skip blanks at @10, @21; aggregate_range 1-29 per header)
- cite-index present: `active-project/theater/facets/_cite-index.md` (49 facet entries; cap-burn DELETE on `coll-net-mender-flea-bottom:1 @8` already cascaded — @8 surfaces in Bare protolines list with zero citations)
- scene-map present: `active-project/theater/facets/scene-map-b01-c01.md` (3 scenes — scene-A @1-9, scene-B @11-20, scene-C @22-29; all three `rhythm-shape: flat-low`; no peak-bones; fusion-eligible-runs declared per scene; coverage 27/27)
- exposition present: `active-project/theater/facets/exposition-b01-c01.md` (3 live entries: 1 @1, 2 @4, 5 @22; entries 3 @9 + 4 @18 DELETED at R2.5 — lens covers)
- dialogue files present: 3 files
  - `coll-net-mender-flea-bottom.md`: BODY-EMPTY (cap-burn DELETE marker only); 0 utterances — bare-speech-bone @8 (ACCEPTED-AT-CAP-BURN per fault-030/031)
  - `taylor-hebert-kl-122ac.md`: 1 utterance (@25)
  - `wren-stitch-maker-flea-bottom-ward.md`: 2 utterances (@23, @26)
- profile: no episode/project profile — schema defaults resolved
- persona: no project-scoped persona card, no project profile declaring non-neutral → resolved `neutral`. No `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT`.
- POV: `narrator: taylor-hebert-kl-122ac` from bones header
- feedback file: absent
- showrunner memory chapters[b01c01] read OK
  - status: `audited-r1` (cap-burn cycle 3 complete; orchestrator-critic verdict NOT-SUCCESSFUL — NOT a HARD-BLOCK against /and-stitch per URI-FACETS-CAP-BURN-SEMANTICS A2)

State machine: stitched: false → in-progress

---

## Phase 0.5 — Pre-flight summary

```
/and-stitch pre-flight for b01-c01:
  persona:          neutral          # OK — no project-scoped persona declared
  voice:            first-person past-tense, contractions on
  POV:              taylor-hebert-kl-122ac
  anchors:          27               # bones file (3 deleted slugs at trim; 27 live; flat ids 1-29 with 2 time-skip blanks)
  scenes:           3                # scene-A @1-9, scene-B @11-20, scene-C @22-29
  phase-1 forks:    3 scene-forks    # serialize across scenes; back-look + forward-look context
  phase-7 forks:    3 scene-forks per-sentence inside
  anti-jargon:      (none — project.anti-jargon empty under schema defaults)
  hollow patterns:  (none — project.hollow-prose-patterns empty under schema defaults)
  asinine patterns: (none — project.asinine-patterns empty under schema defaults)
  bone-fence:       enforced (dialogue=no, body=no, spatial=no, route=no, scene-prose=no, cognitive=no)
  feedback-file:    absent
  exposition:       present (3 live entries; preamble pool = 0 episode-open entries — series opener but R2 declined; first-mention pool = 3 entries at @1, @4, @22, all em-dash-fold)
                    cross-episode register: 0 prior reader-resident terms (series opener)
  phase-1-mode:     scene-window (boundaries from scene-map facet; tensometer-fallback removed under URI-SUBSTANCE-OVERHAUL 2026-05-17)
  output-dir:       active-project/draft/  (terminal deliverable under polish-deferred chain)
  dialogue:         present (3 character files; 3 total utterances)
                    anchors covered: 3 of 4 speech bones (@23 wren, @25 taylor, @26 wren) — @8 (coll) is BARE per cap-burn DELETE
                    unmoored utterances: 0
                    bare speech bones: 1 — @8 (coll speaks to taylor); ACCEPTED-AT-CAP-BURN per fault-030; Phase 1 fork @8 will render silent action only, log `LEGACY-SILENT-SPEECH @8` + `BARE-SPEECH-BONE-CAP-BURN @8` (NOT `FAULT-DIALOGUE-MISSING` — disposition is upstream-ACCEPTED)
```

**Dialogue gate (URI-DIALOGUE-COVERAGE-GATE):** the bare-speech-bone @8 would HARD-ABORT under default semantics. The cap-burn report (`staff/auditor/facets-cap-burn-b01c01-20260524T021822Z.md`) ACCEPTS @8 as a structural trade-off; the downstream-impact section explicitly states `/and-stitch b01-c01 is NOT blocked`. The stitcher proceeds with @8 rendered as silent action under the cap-burn license — equivalent to `--allow-bare-speech` semantics, scoped to this single bone, sourced from the cap-burn disposition (NOT a command-line flag).

Gate PASS — proceed.

---

## Phase 0.6 — Exposition consumption

Exposition facet read: `active-project/theater/facets/exposition-b01-c01.md`.

Categorized live entries:
- **Episode-open pool** (preamble): empty — series opener but R2.5 elected no episode-open / prior-episode-bridge entry. The chapter opens directly on the bone-rendered prose.
- **Per-anchor first-mention pool**:
  - entry 1 @1 (first-mention-place; kings-landing-122ac / flea-bottom / copper-currency-star-penny; em-dash-fold)
  - entry 2 @4 (first-mention-character; coll; em-dash-fold)
  - entry 5 @22 (first-mention-character; wren; em-dash-fold)
- **Per-anchor scene-orient pool**: empty (R2.5 fire-audit REFUSED all 3 scene-opens — loc-state covers @1 / @11 / @22)
- **Refused/dropped**: 2 deletions at R2.5
  - entry 3 @9 (the-prohibition) — DELETED, lens covers (NI:2 + mem:1 + feel:1 + vibes:3 + vibes:4)
  - entry 4 @18 (the-city-watch + the-hook) — DELETED, loc-state:6 covers

Voice-mismatch check: no preamble to validate; first-mention entries are em-dash-folds inside body sentences and inherit POV/voice from the bone they fold into. No `FAULT-EXPOSITION-VOICE-MISMATCH`.

No preamble file written (no episode-open content to assemble). Phase 8 will NOT prepend a preamble — the body is the whole.

Cross-episode register: series opener; glossed-terms.md will be appended at Phase 8 with the 4 KEEPs (kings-landing-122ac, flea-bottom, copper-currency-star-penny, coll) plus 1 KEEP (wren). The STRIKE entries (the-prohibition, the-city-watch, the-hook) are not added to the register.

Anchor pools staged for Phase 1:
- scene-A fork: exposition:1 @1 (em-dash-fold), exposition:2 @4 (em-dash-fold)
- scene-B fork: (no exposition entries)
- scene-C fork: exposition:5 @22 (em-dash-fold)

---

## Phase 0.7 — Dialogue intake

Dialogue files loaded:
- `theater/dialogue/coll-net-mender-flea-bottom.md`: BODY-EMPTY (cap-burn DELETE marker on `coll-net-mender-flea-bottom:1 @8`); 0 utterances; behavior-card=coll-net-mender-flea-bottom
- `theater/dialogue/taylor-hebert-kl-122ac.md`: 1 entry; behavior-card=taylor-hebert-kl-122ac
- `theater/dialogue/wren-stitch-maker-flea-bottom-ward.md`: 2 entries; behavior-card=wren-stitch-maker-flea-bottom-ward

dialogue-by-anchor lookup:
- @23: wren:1 "You walked the block three times this morning. I wasn't looking for you."
- @25: taylor:2 "Nothing for you here. Go on."
- @26: wren:2 "There were flies on the meat-stall. There weren't any on your hand."

Cross-validation:
- speech bones in bones file: @8 (coll), @23 (wren), @25 (taylor), @26 (wren) — 4 total
- anchors covered: 3 of 4 ✓ (@8 BARE per cap-burn DELETE — ACCEPTED-AT-CAP-BURN, fault-030)
- bare speech bones: 1 (`BARE-SPEECH-BONE-CAP-BURN @8` — Coll silent-action only at Phase 1; not `FAULT-DIALOGUE-MISSING`)
- unmoored utterances: 0
- speaker mismatches: 0

URI-DIALOGUE-COVERAGE-GATE: PASS-WITH-CAP-BURN (1 bare bone admitted under cap-burn license per `staff/auditor/facets-cap-burn-b01c01-20260524T021822Z.md` § Downstream impact).

Anchor pools staged for Phase 1:
- scene-A fork: @8 bare (cap-burn) → silent-action render only; log `LEGACY-SILENT-SPEECH @8` + `BARE-SPEECH-BONE-CAP-BURN @8`
- scene-C fork: dialogue:wren:1 @23, dialogue:taylor:2 @25, dialogue:wren:2 @26

---

## Phase 1 — Lens-anchored render (scene-window mode)

Three scene-forks, serialized across scenes (back-look requires prior scene's rendered prose). Dispatched as general-purpose Agent forks under the stitcher-card protocol (no stitcher subagent type registered; general-purpose with full inline protocol).

### fork-001 — scene-A bones=@1-@9 — scene-window-render

bones-consumed: @1, @2, @3, @4, @5, @6, @7, @8, @9
back-look: empty (first scene)
forward-look: scene-B (bones @11-20; opens on "taylor threads the needle" — no clash with @9 held-feet close)

lens-decider-trace:
- @1: 1 lens fires (loc-state:1); exposition:1 em-dash-fold staged. 1-lens rule → fuse with bone via em-dash. Lens: loc-state fold. Co-cites: loc-state:1, exposition:1. (state:1/2, vibes:1/2 schema-forbidden.)
- @2: 2 lenses fire (narrator:1, loc-state:2). Rule 1 fires: foreknowledge-clamp ("already counted"). Lens: narrator leads. Co-cites: narrator:1, loc-state:2.
- @3: 0 lenses. Bone-only.
- @4: 0 lens-facets; exposition:2 graph-resident em-dash-fold. (Held bone; exposition payload IS the holding-quality.)
- @5: 0 lenses, 0 facets. Bone-only.
- @6: 2 lenses fire (sensory:1, loc-state:3). Rule 2 does NOT fire (sensory tag `up`, not spike/drop). Rule 4 default kinetic: sensory leads. Co-anchor fold applied (em-dash + comma-appositive).
- @7: 0 lenses. Bone-only (state:3 forbidden).
- @8: BARE-SPEECH-BONE-CAP-BURN per cap-burn DELETE (fault-030 ACCEPTED-AT-CAP-BURN); LEGACY-SILENT-SPEECH. Render silent acknowledgment per cap-burn license.
- @9: 3 renderable lenses (feel:1, mem:1, narrator:2). Rule 1 does NOT fire (no foreknowledge clamp). Rule 2 does NOT fire (no sensory). Rule 3 does NOT fire (no peak). Rule 4 default kinetic: feel leads, NI + mem fold after. Rule 5 damping not needed. Co-cites: feel:1, mem:1, narrator:2. (state:9, vibes:3/4 forbidden.)

variance-moves:
- Fused @1 + loc-state:1 + exposition:1 em-dash-fold into one entry-beat sentence (fusion-eligible-run opener license; flat-low aggressive posture).
- Split @2 across L2/L3: narrator:1 foreknowledge-clamp + loc-state:2 yard-crossing kept verbatim across two sentences rather than compression-fused.
- @4 folded exposition:2 verbatim via em-dash + semicolon; voice-transformed to first-person past-tense.
- L6/L7 opener-variance: short standalone "I circled the block." vs heavy em-dash-folded "I passed the tallow-stall —" gives bone-percussion break inside the @1-6 fusion-eligible run.
- @6 sensory+loc-state co-anchor fold applied as em-dash + comma-appositive perceptual unit.
- @9 held-bone given dedicated 2-sentence beat (L10 feel-body land, L11 NI+mem cognition land); paragraph break after @8 enforces held-bone discipline.
- L11 surfaces both narrator:2 and mem:1 verbatim per Phase-1-renders-both discipline; redundancy-cull deferred to Phase 2.

refusals:
- Did not invent dialogue for @8 — BARE per cap-burn (fault-030 ACCEPTED-AT-CAP-BURN); rendered as silent needle-action with attention-not-landing per prompt's explicit cap-burn license example. No quoted speech; the deleted line "There's mending if you can hold a needle." does not surface.
- Did not fuse @8/@9 despite no peak-shadow declared — held-discipline at scene-close carries anti-fusion weight.
- Did not render vibes:1/2/3/4 — schema-forbidden bias-only.
- Did not render state:1/2/3/6/7/8/9 — schema-forbidden continuity-only.
- Did not collapse mem:1 against narrator:2 at L11 — Phase 2 redundancy cull is the correct downstream resolution for the doubled register.
- Did not invent body / spatial / route / scene-prose / cognitive detail beyond cited facets — bone-faithfulness fence held throughout.

bone-walk:
- @1 → L1 (fused: bone + loc-state:1 + exposition:1 em-dash-fold)
- @2 → L2-L3 (split: narrator:1 foreknowledge-clamp at L2; bone + loc-state:2 at L3)
- @3 → L4 (bone-only)
- @4 → L5 (held; bone + exposition:2 em-dash-fold)
- @5 → L6 (bone-only; opener-variance pivot)
- @6 → L7 (sensory:1 + loc-state:3 co-anchor fold)
- @7 → L8 (bone-only chatter; state:3 forbidden)
- @8 → L9 (BARE-SPEECH-BONE-CAP-BURN; LEGACY-SILENT-SPEECH; silent needle-action per cap-burn license)
- @9 → L10-L11 (held; feel:1 body-land at L10; narrator:2 + mem:1 cognition-fold at L11)

drift-risk: minor — L11 surfaces narrator:2 and mem:1 verbatim and the two facets are deliberately near-duplicates (NOTE-001 doubled-register design). Cold-read will register the redundancy; the correct resolution is Phase 2 redundancy cull, not Phase 1 invention-side compression. Flagged as expected, not as fault.

cap-burn-handling:
- @8 rendered silent per cap-burn license (fault-030 ACCEPTED-AT-CAP-BURN); no invented speech content; deleted utterance does not appear; render-form follows prompt's example template (needle-continues-working + attention-not-landing-on-POV-face).

### fork-002 — scene-B bones=@11-@20 — scene-window-render

bones-consumed: @11, @12, @13, @14, @15, @16, @17, @18, @19, @20
back-look: scene-A rendered prose (3 paragraphs; L1-L11)
forward-look: scene-C (bones @22-@29; feel:3 @26 / narrator:5 @24 / narrator:6 @26 / loc-state:7 @22 / exposition:5 @22 / dialogue @23/@25/@26) — scene-B closes on @20 day-held ledger; scene-C opens on @22 Wren's alley-mouth entry — no clash.

lens-decider-trace:
- @11: rule 4 default; loc-state:4 leads (place-anchor first-beat in scene; sensory at @12 follows kinetic open). Co-cites: loc-state:4.
- @12: rule 2 fires (sensory:2 tag=spike). Lens: sensory leads. Co-cites: sensory:2.
- @13: rule 4 default; NI leads (narrator:3 passive fauna-feed). Co-cites: narrator:3.
- @14: rule 2 fires (sensory:3 tag=spike). Lens: sensory leads. Co-cites: sensory:3.
- @15: rule 4 default; loc-state:5 leads (well-step). Co-cites: loc-state:5.
- @16: rule 5 recent-focus damping away from sensory/loc; held-bone discipline; mem:2 + feel:2 co-cite — fork CHOSE to render mem:2 verbatim and proactively cull feel:2 (see DRIFT below).
- @17: rule 4 default (NOT rule 2 — sensory:4 tag is `up`, not spike/drop; fork's lens-trace MIS-CITED rule 2). Sensory leads regardless under default kinetic. Co-cites: sensory:4. **LENS-TRACE-MIS-CITATION (minor; outcome correct).**
- @18: rule 4 default; loc-state:6 leads (Hook's bend at-establishment). Co-cites: loc-state:6. NO Watch/Hook gloss added (exposition entry 4 DELETED at R2.5; loc-state carries verbatim).
- @19: 0 facets co-cite (narrator:4 was DELETED at R2.1). Bone-only; held-discipline at watch-pressure-moment. Stands alone.
- @20: rule 4 default; narrator:7 leads (day-close ledger). Co-cites: narrator:7. (state:5, state:10 forbidden.)

variance-moves:
- @11+@12 chain-folded with colon → em-dash (fusion-eligible run @12-19 license; @11 outside run but cadence-fold via colon).
- @13 standalone (NI verbatim — held line-break preserves the cognitive content).
- @14+@15 fused with comma-and chain (eligible run; thermal + loc-state co-flow on ambient-drift beat).
- @16 held standalone (anti-fusion at held-bone; mem:2 verbatim renders the held-state cognition).
- @17+@18 fused (watch-pass pressure audible: boot-strike → patrol-naming on loc-state verbatim).
- @19 held standalone ("I held the eyes" — three-word sentence; pressure-and-discipline beat lands).
- @20 split across L10/L11 (Coll-fold bone L10; narrator:7 fused L11 — day-close ledger gets dedicated sentence).
- Anti-repetition vs scene-A: opening kinetic hand-work distinct from scene-A's "I paid" / "The drain channel" / "I dropped" openers; no "sense ran the walls" echo; "held the eyes" new bone-object distinct from scene-A's "held the feet".

refusals:
- Did not add Watch / Hook gloss at @18 (exposition entries 3, 4 DELETED at R2.5; loc-state covers).
- Did not invent NI at @19 (narrator:4 was deleted; held-bone stands alone; no fabricated cognition).
- Did not render schema-forbidden vibes:5/6/7/8/9 or state-updates entries.
- Did not invent body / dialogue / spatial / cognitive content beyond cited facets.

bone-walk:
- @11 → L1 (fused: bone + loc-state:4)
- @12 → L2 (sensory-led)
- @13 → L3 (NI-led standalone)
- @14 → L4 (sensory-led)
- @15 → L5 (loc-state-led fused with @14)
- @16 → L6 (held; mem:2 verbatim)
- @17 → L7 (sensory)
- @18 → L8 (loc-state verbatim)
- @19 → L9 (bone-only held; three-word standalone)
- @20 → L10-L11 (bone L10 + narrator:7 L11)

drift-risk: **MODERATE — three flags surfaced for Phase 2/Phase 7 reconciliation**:

1. **DROP-FACET feel:2 @16** (Phase-1-proactive-cull). The fork rendered mem:2 verbatim ("the hands are on the needle...") and CULLED feel:2 ("holds both hands flat against the mesh") rather than rendering both. Phase 1 contract is to render all facet content and defer redundancy decisions to Phase 2. Fork's rationale: feel:2 + mem:2 + bone-V "holds the hands" at the same anchor would AP-stack the held-discipline beat. Phase 2 redundancy cull or Phase 5 un-merge license should validate the cull or rescue feel:2. If feel:2 is restored, the held-bone clause becomes: `I held both hands flat against the mesh. The hands were on the needle and the needle was what they were for today, and this was what having hands was, here, in this place, at this work.` Recovery is mechanical.

2. **FAULT-PHASE-1-REWORD at L1**: loc-state:4 verbatim ends "the working position's spatial anchor established" — fork rendered "settled" instead. Unlicensed REWORD at Phase 1. Phase 7 Q9 (awkward words) or Phase 2 fidelity check should revert "settled" → "established". Near-synonym; meaning preserved; surface deviation noted.

3. **LENS-TRACE-MIS-CITATION @17**: fork's trace claimed rule 2 fires on `tag=up`; rule 2 fires ONLY on `tag=spike` or `tag=drop`. The correct trace is rule 4 default kinetic (only sensory fires at @17 among the lens decider's domain; sensory leads trivially). Render outcome identical; auditor-trace correction only.

(None of these block downstream phases. All are recoverable.)

cap-burn-handling:
- N/A for scene-B (no bare-speech bones).

### fork-003 — scene-C bones=@22-@29 — scene-window-render

bones-consumed: @22, @23, @24, @25, @26, @27, @28, @29
back-look: scene-A + scene-B rendered prose (4 paragraphs scene-B + 3 paragraphs scene-A = 7 paragraphs; L1-L22 across forks-001-002)
forward-look: none (last scene of chapter)

lens-decider-trace:
- @22: rule 4 default; loc-state:7 leads (alley-mouth entry); exposition:5 em-dash-fold rides inside the same sentence at first mention of Wren. Co-cites: loc-state:7, exposition:5.
- @23: dialogue-bone; speaker-paragraph rule yields lens-decider; Wren utterance verbatim. No facet co-cite.
- @24: rule 1 fires — foreknowledge-clamp ("had already mapped... before"). NI leads. Co-cites: narrator:5.
- @25: dialogue-bone; speaker-paragraph rule yields lens-decider; Taylor utterance verbatim.
- @26: dialogue-bone primary (Wren utterance verbatim, own paragraph); feel:3 folds as Wren's pre-speech body-show (before utterance); narrator:6 folds as Taylor-interior receipt at end of paragraph (inverted-predicate cap consumed). Foreknowledge "should have returned" register present but yields to dialogue primacy under speaker-paragraph rule.
- @27: 0 facets co-cite (feel-taylor:3 @27 DELETED at R2.3 on §Form temporal-latency; vibes:9 schema-forbidden). Bone-only held; rule catches.
- @28: 0 facets. Chatter bone-only (Wren-crosses-street).
- @29: 0 facets. Bone-only held closing; the rule's verdict.

variance-moves:
- @22 aggressive em-dash-fold: exposition:5 placed as em-dash phrase immediately after "Wren" first-mention; loc-state:7 alley-mouth content folds at sentence tail. One sentence, ~50 words — earned by the cost-bearer-introduction load-bearing status.
- Speaker-paragraph rule enforced: @22 own paragraph; @23 own; @24 own (held + NI); @25 own; @26 own (feel:3 + Wren-utterance + narrator:6 fold); @27+@28 fused (held + motion-chatter; @28 is not a speaker turn, so speaker-paragraph rule does not bar); @29 own.
- Close-register variance: chapter closes on flat declarative "I lifted the needle." — distinct from scene-A "block was not requiring anything..." and scene-B "the day held under the count..." cadences. Brevity-as-tell.
- Opener anti-repetition: scene-C opens with "A girl stepped into the alley-mouth" — subject = Wren, not "I"; breaks the back-look "I + verb" chain run.

refusals:
- Did not invent interior content at @27 (no facet fires; bone S+V+O only).
- Did not expand @29 beyond held SVO; brevity-as-tell is the chapter-close discipline.
- Did not name Khepri anywhere in interior; narrator:5/6 verbatim already compliant.
- Did not use non-basic attribution verb at any dialogue beat ("said" throughout; no preferred-attribution-verbs section on either character card).
- Did not render exposition:5 a second time (em-dash-fold once at @22).
- Did not fuse @23 with @22 or @25 with @24 (speaker-paragraph rule).
- Did not fuse @24 with @23 (held-bone anti-fuses).
- Did not render schema-forbidden vibes:7/8/9/10 or state-updates entries.

bone-walk:
- @22 → L1 (entry; exposition:5 em-dash-fold inside the bone-rendered sentence at "Wren" first-mention; loc-state:7 alley-mouth body folds at sentence tail)
- @23 → L2 (Wren speech verbatim; own paragraph)
- @24 → L3-L4 (NI-lead foreknowledge-clamp at L3; held bone S+V+O at L4)
- @25 → L5 (Taylor speech verbatim; own paragraph)
- @26 → L6-L8 (feel:3 body-show at L6; Wren utterance verbatim at L7; narrator:6 inverted-predicate fold at L8)
- @27 → L9 (held; rule catches)
- @28 → L10 (chatter; shares paragraph with @27)
- @29 → L11 (held closing needle-lift; standalone paragraph)

drift-risk: **MODERATE — three small fidelity slips flagged for Phase 2/Phase 7**:

1. **loc-state:7 RESTRUCTURED at L1**: facet verbatim ends "narrow enough that approach reads as deliberate, not incidental"; fork rendered "the approach read as deliberate, not incidental, in the narrowness of the way." The "narrowness of the way" is a noun-phrase paraphrase of "narrow enough that..." restructured for syntactic-fit with the surrounding em-dash-folded sentence. Information preserved; surface form deviates. Phase 7 Q9 / Phase 2 reconciliation could revert to closer verbatim.

2. **feel:3 SURFACE SUBSTITUTION at L6**: facet verbatim is "wren-stitch-maker-flea-bottom-ward: moves the eyes to Taylor's hands before speaking". Faithful past + POV resolution would render: "Wren moved the eyes to my hands before speaking" (or "She moved the eyes to my hands before she spoke"). Fork rendered: "She moved her eyes to my hands before she spoke." Substituted "the eyes" → "her eyes" (idiom-fit but the project's bone-object-policy is `verbatim` and the chapter uses "the eyes / the hands / the feet" form consistently). Surface-form deviation; meaning preserved. Phase 7 Q9 could revert "her eyes" → "the eyes".

3. **narrator:6 PAST-PERFECT INTERPRETATION at L8**: facet verbatim "what the girl saw is what the read should have returned — the girl arrived at it without the insects". Voice-transform to past would yield "...the girl arrived at it..." (simple past). Fork rendered "the girl had arrived at it" (past-perfect). Defensible as voice-transform interpretation (prior-action sequencing), but strictly the verbatim is simple past after voice-shift. Minor.

(None block downstream phases.)

dialogue-handling:
- @23 wren:1 verbatim "You walked the block three times this morning. I wasn't looking for you." — attribution: "said"; speaker-name first-mention "she" (Wren just introduced in @22's paragraph; pronoun OK after immediate adjacency).
- @25 taylor:2 verbatim "Nothing for you here. Go on." — attribution: "I said".
- @26 wren:2 verbatim "There were flies on the meat-stall. There weren't any on your hand." — attribution: "she said".

exposition-handling:
- @22 exposition:5 em-dash-fold rendered verbatim modulo voice-transform: gloss inserted as em-dash phrase immediately after "Wren" first-mention; phrase carries ward-of-stitch-maker's-household + light-work-for-shelter-and-two-meals + stitches-trim-ends + has-been-here-long-enough + watches-before-acting. Tense shifted to past throughout. Rendered once; never restated.

cap-burn-handling:
- N/A for scene-C.

---

## Phase 1 — completion summary

- 3 scene-forks dispatched, all returned successfully.
- 27 bones rendered (per bone-walk: @1-9, @11-20, @22-29). 0 bones missing.
- 11 + 11 + 11 = 33 sentences (rough; final line-ID count at Phase 8).
- Schema-forbidden vibes + state-updates not rendered (correctly suppressed by all three forks).
- Cap-burn @8 silent-action rendered per license.
- Dialogue utterances verbatim across @23, @25, @26.
- Exposition em-dash-folds at @1, @4, @22 verbatim modulo voice-transform.

**Phase 1 drift consolidated for Phase 2/7 reconciliation:**

| Flag | Anchor | Class | Recovery path |
|---|---|---|---|
| FACET-DEFERRED feel:2 | @16 (scene-B L6) | Phase-1-proactive-cull (feel:2 subsumed into mem:2) | Phase 2 redundancy cull validates or Phase 5 un-merge rescues |
| FAULT-PHASE-1-REWORD "established" → "settled" | @11 loc-state:4 (scene-B L1) | Unlicensed REWORD | Phase 7 Q9 or Phase 2 fidelity check reverts |
| LENS-TRACE-MIS-CITATION rule 2 | @17 (scene-B) | Auditor-trace; outcome correct | Render-log correction only; no prose change |
| loc-state:7 RESTRUCTURED "narrowness of the way" | @22 (scene-C L1) | Paraphrase for syntactic fit | Phase 7 Q9 may revert |
| feel:3 "the eyes" → "her eyes" | @26 (scene-C L6) | Surface substitution (bone-object-policy `verbatim` deviation) | Phase 7 Q9 reverts |
| narrator:6 "arrived" → "had arrived" | @26 (scene-C L8) | Past-perfect interpretation | Defensible voice-transform; flag for Phase 7 |

All flags are recoverable downstream. No bone missing, no invented dialogue, no schema-forbidden facets rendered.

State machine: Phase 1 → in-progress (Phase 2 next).

---

## Phase 2 — Redundancy cull

Detector set per schema defaults: closing-phrase-echo + image-set-overlap. Echo-window 1 (same-anchor only). Preserve-anchor: narrator.

Walked the Phase 1 draft per-anchor; ≥2-facet co-anchors enumerated against the cite-index.

Decisions:

- `KEEP-BOTH @1` — loc-state:1 + exposition:1 — different content classes (place-anchor vs first-mention gloss); no closing-phrase-echo, no image-set overlap. Em-dash-folded into one sentence already at Phase 1.
- `KEEP-BOTH @2` — narrator:1 (foreknowledge-clamp) + loc-state:2 (yard-crossing). Different content. No overlap.
- `KEEP-FOLD @6` — sensory:1 + loc-state:3 already folded as one perceptual unit at Phase 1; co-anchor fold preserved.
- `NO-CULL @11` — loc-state:4 only co-cite at this anchor (no co-anchor cull candidate).
- `NO-CULL feel:2 @16 (already-culled at Phase 1; un-merge candidacy at Phase 5)` — feel:2 was proactively-culled by fork-002 at Phase 1; Phase 2 defers rescue-decision to Phase 5 un-merge license, the canonical mechanism for facet rescue. Logged here as no-op; the rescue is executed at Phase 5.
- `NO-CULL @18` — only loc-state:6 lives at @18 (state:4 schema-forbidden).
- `NO-CULL @20` — only narrator:7 lives at @20 (state:5 schema-forbidden).
- `KEEP-BOTH @22` — loc-state:7 + exposition:5 — different content classes (place-anchor vs cost-bearer first-mention). Already em-dash-folded into one cost-bearer-introduction sentence.
- `KEEP-ALL @26` — feel:3 + narrator:6 + wren:2 dialogue. Three different surfaces (pre-speech body-show + post-speech receipt + verbatim utterance). No overlap.
- `DROP-IMAGE-OVERLAP mem:1 @9` — at scene-A L11, narrator:2 + mem:1 are both surfaced verbatim with strong image-set overlap (`the sense ran the [walls|block]` repeats) and closing-phrase echo (`what I was not doing` ↔ `what I was no longer doing`). Per `preserve-anchor: narrator`, narrator:2 wins; mem:1 is DROPPED. Cull validates the Phase 1 fork-001 drift-risk note ("redundancy cull is the correct downstream answer").
  - original (L11): `The sense ran the walls and the walls gave it back unchanged, because nothing here had called for what I was not doing; the sense ran the block and the block was what it was, and the block was not requiring anything of the kind I was no longer doing.`
  - revised: `The sense ran the walls and the walls gave it back unchanged, because nothing here had called for what I was not doing.`

Total culls: 1 (mem:1 @9). All other co-anchor pairs preserved.

---

## Phase 3 — Compression

Profile: same-subject-merge=true; pronoun-substitution=after-first; flat-low-run-collapse=preserve-buildups; exit-trio-merge=true; zero-cite-bone-policy=render.

Walked the draft for compression candidates. Decisions:

- `NO-MERGE scene-A @1-@2` — different actions (paid / crossed / circled / passed); not a continuous-action sequence.
- `NO-MERGE scene-A @8-@9` — different subjects (Coll silent / Taylor held); held-discipline at @9 carries anti-fusion weight (already enforced at Phase 1).
- `NO-MERGE scene-B @11-@12` — different subjects (Taylor threaded the needle / the needle crossed the mesh); chain-folded at Phase 1 via colon → em-dash, but not merged into one clause.
- `NO-MERGE scene-B @14-@15` — different subjects (walls cooled / I passed); already chain-folded at Phase 1 with comma-and.
- `NO-MERGE scene-C *` — speaker-paragraph rule (Phase 5 enforced) bars cross-speaker merges; @22/@23/@24/@25/@26 are speaker-bounded.
- `SUBSTITUTE-PRONOUN Coll → he` (after-first) — scene-A: "Coll lifted his eyes" (L4 first-mention) → "He worked the net..." (L5 second-mention, already pronouned at Phase 1) ✓. At L9 ("Coll's needle moved..."), the second-paragraph-onset resets first-mention semantics under the after-first rule; "Coll's" preserved for paragraph-anchored clarity. No additional substitutions.
- `NO-COLLAPSE flat-low-run` — scene-map declares no protected patterns; chapter is all flat-low; aggressive collapse would over-thin a ~34-sentence chapter. `preserve-buildups` posture honors the low bone-density already in place.
- `NO-MERGE exit-trio` — no exit-trio pattern present in this chapter.
- `NO-MERGE-TIMESKIP @9 ↔ @11` — held discipline at scene-A close; opener kinetic at scene-B; distinct scenes across the time-skip blank.
- `NO-MERGE-TIMESKIP @20 ↔ @22` — day-close ledger at scene-B close; cost-bearer entry at scene-C open; distinct scenes.

Total compression moves: 0 (all candidates considered, all rejected). The draft was already at compression equilibrium post-Phase-1.

---

## Phase 4 — Voice transform

Profile: tense=past; person=first; contractions=true; bone-object-policy=verbatim; feeling-clause-pov-resolution=auto; sensory-arrow-rendering=prose-template.

Decisions:

- `TENSE-OK` — full draft scan: no present-tense leakage. Phase 1 forks worked under past-tense throughout. No `TENSE-SHIFT` needed.
- `PERSON-OK` — full draft scan: no third-person leakage on Taylor-POV interior passages. POV pronouns ("I", "my") consistent. No `PERSON-SHIFT-POV` needed.
- `CONTRACTION-WAIVE was-not @9` — narrator:2 facet verbatim is `she is not doing`; voice-shifted to first-person past renders `I was not doing`. Schema default `voice.contractions: true` would suggest `wasn't`. However, the facet's authoritative surface is `is not` (uncontracted) and `bone-object-policy: verbatim` requires minimal-shift fidelity. DECISION: keep `was not` uncontracted to honor verbatim discipline. Logged as `CONTRACTION-WAIVE was-not @9 (verbatim-fidelity)`. Same waiver applies to `had not done` at scene-B L11 (narrator:7 verbatim register).
- `POV-PRONOUN-RESOLVE-OK` — no third-party pronoun resolution issues found.
- `REVERT-BONE-OBJECT-VERBATIM established @11 loc-state:4` — Phase 1 drift flag #2. Scene-B L1 rendered `settled` for loc-state:4's verbatim `established`. Unlicensed REWORD; near-synonym but surface-deviation. Reverted.
  - original (scene-B L1): `...midday under overcast, the working position's spatial anchor settled.`
  - revised: `...midday under overcast, the working position's spatial anchor established.`
- `SENSORY-PROSE-FIT-OK` — sensory:1 (@6), sensory:2 (@12), sensory:3 (@14), sensory:4 (@17) all rendered as prose-template at Phase 1; perceptual content surfaces faithfully without arrow-notation residue. Validated.
- `BONE-OBJECT-IDIOM-FIT-OK` — bone-object surfaces (eyes / hands / feet / needle / pack / net / boots / cobbles) all carry `the X` definite-article convention from the chapter's bone-object policy. No idiom-fit substitutions needed at Phase 4 (the `her eyes` and `had arrived` substitutions are handled at Phase 5 REVERT moves per the Phase 1 drift consolidation table).

Total Phase 4 moves: 1 REVERT-BONE-OBJECT-VERBATIM, 2 CONTRACTION-WAIVE (explicit log of decisions), all other checks OK.

---

## Phase 5 — Local flow + speaker-paragraph

Profile: window-size=3; sensory-deferral-cap=2; ni-promotion-cap=1; within-anchor-order=em-dash-fusion; un-merge-license=true; speaker-paragraph-rule=enforced.

Decisions:

- `SPEAKER-PARAGRAPH-BREAK-OK scene-C` — re-verified scene-C paragraph structure: @22 own ¶, @23 own ¶ (wren:1), @24 own ¶ (NI+held), @25 own ¶ (taylor:2), @26 own ¶ (feel:3 + wren:2 + narrator:6), @27+@28 fused ¶, @29 standalone closing ¶. URI-SUBSTANCE-OVERHAUL speaker-paragraph rule honored throughout. No new breaks needed.
- `WITHIN-ANCHOR-REORDER-OK` — em-dash-fusion default applied at @4, @6, @22 at Phase 1; @9, @22 used compound clauses; nothing to reorder.
- `REFUSE-MIGRATE-SENSORY-FORWARD` — sensory:2 @12, sensory:3 @14, sensory:4 @17 each at-anchor with bone; no migration candidate within the 3-bone window without disrupting bone-anchored beat. Cap-2 unused.
- `REFUSE-MIGRATE-NI-BACKWARD` — narrator:1 @2 already at @2 leading position; narrator:3 @13 leading at-anchor; narrator:5 @24 leading at-anchor with foreknowledge-clamp; narrator:6 @26 in receipt position (fork-003 placement). No backward promotion candidates. Cap-1 unused.
- `UN-MERGE-RESCUE feel:2 @16` — canonical rescue path for Phase 1 drift flag #1. feel:2 ("holds both hands flat against the mesh") is the body-anchored discipline beat that lands the held bone-V "holds" physically. Without it, the bone-V surfaces only through mem:2's cognition — `RENDERED-ILLEGIBLE` risk per URI-STITCH-ACCOUNTING-HONESTY. Inserted a feel:2-rendered sentence BEFORE the mem:2 sentence at scene-B paragraph 3 (the @16 anchor).
  - original (scene-B L6, single sentence): `The hands were on the needle and the needle was what they were for today, and this was what having hands was, here, in this place, at this work.`
  - revised (scene-B L6, two sentences): `I held both hands flat against the mesh. The hands were on the needle and the needle was what they were for today, and this was what having hands was, here, in this place, at this work.`
  - Rationale: bone-V "holds" lands in feel:2 clause; mem:2 monument-cognition lands second; no RENDERED-ILLEGIBLE on bone-V. Redundancy concern noted; Phase 7 Q-check will validate the un-merge is not over-stacked.
- `REVERT-PARAPHRASE loc-state:7 @22` — Phase 1 drift flag #4. Restructured `narrowness of the way` reverted to closer-to-verbatim `alley-mouth was narrow enough that approach read as deliberate, not incidental`. Bone-faithfulness fence's verbatim discipline preserved.
  - original (scene-C L1 tail): `...and the approach read as deliberate, not incidental, in the narrowness of the way.`
  - revised: `...and the alley-mouth was narrow enough that approach read as deliberate, not incidental.`
- `REVERT-SURFACE-SUBSTITUTION feel:3 @26` — Phase 1 drift flag #5. `her eyes` reverted to `the eyes` per bone-object-policy `verbatim` and the chapter's consistent `the eyes / the hands / the feet` convention.
  - original (scene-C L6): `She moved her eyes to my hands before she spoke.`
  - revised: `She moved the eyes to my hands before she spoke.`
- `REVERT-VOICE-TRANSFORM narrator:6 @26` — Phase 1 drift flag #6. `had arrived` (past-perfect interpretation) reverted to `arrived` (simple past) per facet verbatim shifted under the past-tense voice-transform.
  - original (scene-C L8 tail): `...the girl had arrived at it without the insects.`
  - revised: `...the girl arrived at it without the insects.`
- `SPEAKER-PARAGRAPH-RECHECK post-un-merge` — un-merge at @16 added one sentence inside the existing scene-B paragraph 3; no new speaker; speaker-paragraph rule unaffected.

Total Phase 5 moves: 1 UN-MERGE-RESCUE, 3 REVERT-* (paraphrase + surface-substitution + voice-transform). All operations within license.

---

## Phase 6 — Buildup preservation

Profile: protected-patterns=none for this chapter per scene-map (`scene-A: protected-patterns: none`, `scene-B: protected-patterns: none`, `scene-C: protected-patterns: none`).

Scan:

- `NO-PATTERNS-DECLARED-OR-DETECTED` — scene-map declares no protected patterns across all three scenes. No protected-pattern abandonment risk. No new structural pattern detected on the flat-low chapter that warrants `NEW-PATTERN-CANDIDATE` flag.
- `PATTERN-OK *` — no-op pass.

Total Phase 6 moves: 0. Phase 6 is near-no-op as predicted by scene-map state.

---

## Phase 6 — completion summary

- Phase 6 draft: `active-project/draft/b01-c01.phase-6.draft.md`
- word count: 551
- sentence-terminator count: 37 (approximate sentence count ~34, allowing for em-dash internal pauses)
- paragraph count: 14 (scene-A 4 ¶, scene-B 3 ¶, scene-C 7 ¶)
- bones preserved: 27/27 (no cuts; Phase 7 has cut-license, Phases 2-6 do not)
- redundancy culls: 1 (mem:1 @9)
- compression merges: 0
- voice reverts: 1 (`established` @11)
- un-merge rescues: 1 (feel:2 @16)
- paraphrase reverts: 1 (loc-state:7 @22)
- surface-substitution reverts: 1 (feel:3 `her eyes` → `the eyes` @26)
- voice-transform reverts: 1 (narrator:6 `had arrived` → `arrived` @26)
- protected-pattern actions: 0

All six Phase 1 drift flags addressed:
1. feel:2 @16 → RESCUED via UN-MERGE at Phase 5 ✓
2. `settled` → `established` @11 → REVERTED at Phase 4 ✓
3. LENS-TRACE-MIS-CITATION @17 → render-log-only correction; no prose change required (acknowledged from Phase 1 log) ✓
4. loc-state:7 RESTRUCTURED @22 → REVERTED at Phase 5 ✓
5. feel:3 `her eyes` @26 → REVERTED at Phase 5 ✓
6. narrator:6 `had arrived` @26 → REVERTED at Phase 5 ✓

State machine: Phase 6 → complete (Phase 7 per-sentence editorial reflection next).

---

## Phase 7 — editorial reflection

profile: phase-7.enabled=true; questions=Q1-Q9 standard; cut-aggressiveness=strict; reshow-min-sources=2; reword-density-cap=2 per sentence; bones-cuttable=anchor-cut-only; borderline-policy=reject (EXPOSITION-DERIVED + DIALOGUE-UTTERANCE-DERIVED borderlines = KEEP).
persona: neutral (defers to profile defaults).
project lists: anti-jargon / hollow-prose-patterns / asinine-patterns ALL empty (schema defaults). Q5/Q8/Q9 calls based on rubric definitions, not project-specific lists.

Sentence inventory: 37 sentences across 14 paragraphs (¶1: 1 / ¶2: 6 / ¶3: 4 / ¶4: 3 / ¶5: 4 / ¶6: 3 / ¶7: 2 / ¶8: 1 / ¶9: 2 / ¶10: 2 / ¶11: 2 / ¶12: 4 / ¶13: 2 / ¶14: 1). All 37 walked serially below.

### Q-walk

```
[¶1 S1] "I paid the building-keeper at the corner-room threshold..." anchor=@1(bone+lens+exposition-derived)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @1 + loc-state:1 + exposition:1 em-dash-fold; exposition-policy pre-clears Q1/Q5/Q8 borderlines; em-dashes carry licensed gloss, not reached-for; "subsistence-class permanent" / "anonymous copper-star transaction" graph-resident verbatim — no Q9 fault.

[¶2 S1] "The drain channel put the yard on one side..." anchor=@2(bone+lens)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @2 + narrator:1 foreknowledge-clamp (verbatim "she has already counted what is between them" → first-person past). Semicolon-spine licensed by NI rubric post-2026-05-23 directive. Counterfactual cut loses the egress-pre-count signal that establishes Taylor's resting mode.

[¶2 S2] "I crossed — wet stone gap at the yard crossing..." anchor=@2(bone+lens)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone-V "crossed" + loc-state:2 verbatim. The "footing cost a stride's width" carries the navigation cost. Em-dash punctuation necessary for apposition; not reached-for.

[¶2 S3] "Coll lifted his eyes." anchor=@3(bone-only)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @3 SVO; first concrete Coll-action; non-cuttable counterfactually (without it Coll's @4 first-mention has no co-located action-frame).

[¶2 S4] "He worked the net — net-mender, same corner since before I arrived..." anchor=@4(exposition-derived)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @4 + exposition:2 verbatim em-dash-fold (first-mention-character Coll). Exposition-policy: Q1/Q5/Q8 pre-cleared. Q9 check: "net-mender" is establishment-anchored (graph-resident); "noticed without registering as notable" is verbatim gloss prose. No FAULT-EXPOSITION-AUDIT-MISS. Semicolon-spine carries the range-of-interest payload; necessary punctuation.

[¶2 S5] "I circled the block." anchor=@5(bone-only)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @5 SVO; opener-variance pivot inside fusion-eligible run @1-6 (Phase 1 variance-move); short standalone provides bone-percussion break. Cutting violates Phase 1 deliberate variance.

[¶2 S6] "I passed the tallow-stall — the smoke-funnel drawing within arm's reach..." anchor=@6(bone+lens)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @6 + sensory:1 (smell olfactory inflection) + loc-state:3 ("smoke-funnel" verbatim graph-resident). "tallow-stall" / "smoke-funnel" are Westerosi-establishment + facet-anchored compounds; KEEP per prompt's Q9-scrutiny list.

[¶3 S1] "I dropped the pack." anchor=@7(bone-only)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @7 SVO; physical settle-into-work beat; counterfactual cut removes the day's transition into the working-corner-posture. Brevity sets up the held-bone landing at @9.

[¶3 S2] "Coll's needle moved, his attention not landing on my face." anchor=@8(bone+cap-burn-silent)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @8 rendered silent under BARE-SPEECH-BONE-CAP-BURN license (cap-burn DELETE on coll-net-mender-flea-bottom:1; fault-030 ACCEPTED-AT-CAP-BURN). The needle-action + attention-not-landing carries the silent-acknowledgment per cap-burn license example. Q1: load-bearing — without it the speech-bone's absence registers as missing rather than as silent-action-substituted. KEEP is mandatory.

[¶3 S3] "I set both feet even on the flagstones." anchor=@9(feel:1 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: feel:1 @9 verbatim (taylor-hebert-kl-122ac: sets both feet even on the flagstones). Held-bone body-landing for mem:1's monument-cognition that follows. Counterfactual cut removes the chapter's first held-discipline beat body-anchor.

[¶3 S4] "The sense ran the walls and the walls gave it back unchanged, because nothing here had called for what I was not doing." anchor=@9(narrator:2 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: narrator:2 @9 verbatim (NI-spine for mem:1; cap-burn-preserved as the chapter's NOTE-001 override-architecture-residue cognition). mem:1 was already culled at Phase 2 (DROP-IMAGE-OVERLAP). The remaining narrator:2 surface stands alone as the absence-attending cognition. CONTRACTION-WAIVE "was not" honored per Phase 4 verbatim-fidelity decision.

[¶4 S1] "I threaded the needle, working corner off the Hook, Coll's net-frame at the far edge: midday under overcast, the working position's spatial anchor established." anchor=@11(bone+lens)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @11 + loc-state:4 verbatim (already REVERTED at Phase 4 from "settled" → "established"). "spatial anchor established" register noted in prompt as slightly clinical (Q8 candidate); per loc-state:4 graph-resident verbatim, KEEP unless clear FAULT-LOC-STATE-AUDIT-MISS — no such fault declared. Colon-and-comma punctuation chains the place-anchor first-beat sequence; not reached-for.

[¶4 S2] "The needle crossed the mesh — thread-resistance and metal-smoothness, the hand-sensation taking its first count of the day." anchor=@12(bone+sensory:2)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: yes
  → REWORD: "the hand-sensation taking its first count of the day" → "the hand taking its first count of the day"
  rationale: sensory:2 verbatim is "tactile: working-corner-open-air -> needle-through-mesh # tag: spike" — the arrow renders as the "thread-resistance and metal-smoothness" pair (faithful prose-template). "hand-sensation" is stitcher prose interpreting the sensory arrow's destination; not graph-resident. Q9 hit: invented hyphenated nominalization compound. Clean substitution drops "-sensation" (the "count" already carries the sensory reading); meaning preserved; ≤2 substitutions per sentence (1 used). Per prompt's scrutiny list ("consider REWORD; or accept as fold variant") — strict default + neutral persona → REWORD applied. Q9-density cap (3+ → RESHOW) not approached.

[¶4 S3] "Every warm body in the block was legible at the work-level density I was not working against." anchor=@13(narrator:3 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: narrator:3 @13 verbatim (passive fauna-feed channel; chapter opposing-force interior register). "work-level density" graph-resident per prompt; KEEP. CONTRACTION-WAIVE "was not" honored. Counterfactual: removing loses the chapter's opposing-force visibility (the insect-fill against which held bones operate).

[¶5 S1] "The walls cooled, releasing day-warmth into the overcast." anchor=@14(bone+sensory:3)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @14 + sensory:3 thermal inflection (verbatim arrow "flea-bottom-midday-overcast-ambient -> walls-releasing-day-warmth # tag: spike") rendered as prose-template. The participial "releasing day-warmth" carries the arrow destination cleanly; no invented compound.

[¶5 S2] "I passed the well-step, the stone wet from mid-morning draws — sidefoot past the standing pool." anchor=@15(bone+loc-state:5)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @15 + loc-state:5 verbatim ("the well-step stone wet from mid-morning draws; passage is sidefoot to avoid the standing pool"). "well-step" Westerosi-establishment-anchored; "sidefoot" is loc-state verbatim. Em-dash punctuation for navigation-cost apposition; not reached-for.

[¶5 S3] "I held both hands flat against the mesh." anchor=@16(feel:2 verbatim; UN-MERGE-RESCUED at Phase 5)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: feel:2 @16 verbatim (taylor-hebert-kl-122ac: holds both hands flat against the mesh). Body-anchor for held-bone "holds"; without it the bone-V would surface only via mem:2 cognition (RENDERED-ILLEGIBLE risk). Phase 5 UN-MERGE-RESCUE was the canonical mechanism. Confirmed not over-stacked: the body-press + cognition pair lands cleanly across two sentences.

[¶5 S4] "The hands were on the needle and the needle was what they were for today, and this was what having hands was, here, in this place, at this work." anchor=@16(mem:2 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: mem:2 @16 verbatim (graph-resident; monument-cognition; Earth-Bet displacement override-architecture-instrument-withheld). Counterfactual: removing loses the chapter's mid-day held-discipline monument-callback. The chapter's central characterization (architecture-residue held in body) needs this cognition; feel:2 above is body-anchor, mem:2 here is structural-meaning layer. Q3 (boring/repetitive): the doubled-register echoes "hands" but each clause does distinct register-work (hands-as-current-instrument / hands-as-essence). Strict default would consider; held-monument design forbids over-cut on a hinge-chapter quiet-by-design beat (prompt's final discipline reminder). KEEP.

[¶6 S1] "The boots struck the cobbles." anchor=@17(bone+sensory:4)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @17 + sensory:4 (auditory inflection boot-strike-on-cobbles). Short kinetic SVO; watch-pass approach-signal opener. Anti-fusion against @18's loc-state-led pressure beat.

[¶6 S2] "The city-watch passed the Hook's bend: four-body patrol in gold cloaks, the working corner with unobstructed line-of-sight to the bend." anchor=@18(loc-state:6 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: loc-state:6 verbatim (exposition entry 4 was DELETED at R2.5; loc-state carries both Watch and Hook glosses). "four-body patrol in gold cloaks" carries the Watch designation; "Hook's bend" anchors place. Colon punctuation chains the patrol-naming after the place-anchor; not reached-for.

[¶6 S3] "I held the eyes." anchor=@19(bone-only held)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @19 SVO held; three-word standalone pressure-and-discipline beat. narrator:4 was DELETED at R2.1 so the bone stands alone by design. Brevity-as-tell discipline. Counterfactual cut removes the watch-pressure-moment held register.

[¶7 S1] "Coll folded the net." anchor=@20(bone-only)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @20 first-half (Coll-action exit signal at scene-B close); concise kinetic SVO. Counterfactual cut removes the day-close pivot that motivates narrator:7's ledger-fold next sentence.

[¶7 S2] "The day held under the count I had been running, and the weight of what I had not done was in the count." anchor=@20(narrator:7 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: narrator:7 @20 verbatim (day-close ledger; NOTE-002 carrier; G5 hold-live "nothing had been moved that needed not to be moved"). CONTRACTION-WAIVE "had not done" per Phase 4 verbatim-fidelity decision. Counterfactual: removing loses the chapter's cost-tracking ledger-close — the prohibition's continuing intactness register.

[¶8 S1] "A girl stepped into the alley-mouth from the meat-stall direction — Wren, ward of the stitch-maker's household two buildings over..." anchor=@22(bone+lens+exposition-derived)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @22 + loc-state:7 verbatim (REVERTED at Phase 5 from "narrowness of the way" → verbatim form) + exposition:5 verbatim em-dash-fold (first-mention-character Wren cost-bearer-introduction). Long sentence (~70 words) earned by cost-bearer load-bearing status. Exposition-policy: Q1/Q5/Q8 pre-cleared. Q6 check: two em-dashes + one semicolon — necessary to fold gloss inside the entry-sentence + chain loc-state tail; not reached-for. Q9 check: "stitch-maker" is common-English compound; "Flea Bottom" / "ward" on register; "trim-ends" is establishment-anchored craft-vocabulary. No FAULT-EXPOSITION-AUDIT-MISS.

[¶9 S1] "\"You walked the block three times this morning,\" she said." anchor=@23(dialogue-utterance + dialogue-attribution)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: wren:1 @23 utterance verbatim (DIALOGUE-UTTERANCE-DERIVED → Q1/Q5/Q8/Q9/Q6 ALL pre-cleared). Attribution clause "she said" subject to all Q-checks normally: Q1 load-bearing (first speaker-introduction in scene; pronoun anchors Wren as recently-introduced); not redundant.

[¶9 S2] "\"I wasn't looking for you.\"" anchor=@23(dialogue-utterance continuation)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: wren:1 @23 second utterance-sentence verbatim. Dialogue-utterance-derived → all Q pre-cleared. No surrounding attribution to audit.

[¶10 S1] "I had already mapped the observation-radius and run the circuit count before the held label registered that I had." anchor=@24(narrator:5 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: narrator:5 @24 verbatim (pre-calc surfacing + foreknowledge-clamp channel). "the held label" graph-resident per prompt; KEEP. Counterfactual: removing loses the chapter's structural-collision register (assessment-fired-without-permission). Semicolon-free; complex sentence with one foreknowledge-clamp; passes "one observation per fire" check from NI rubric.

[¶10 S2] "I lifted my eyes." anchor=@24(bone S+V+O held)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @24 held body-action; short standalone landing-beat after narrator:5 cognition. Counterfactual cut: removes the physical orienting-toward-Wren that sets up @25's dismissive line. Note: "my eyes" not "the eyes" here — bone-V is "lifts" with no facet co-cite at the body-action; the "my eyes" form is bone-rendered without bone-object-policy override (no feel facet fires at @24). Acceptable.

[¶11 S1] "\"Nothing for you here,\" I said." anchor=@25(dialogue-utterance + dialogue-attribution)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: taylor:2 @25 utterance verbatim (DIALOGUE-UTTERANCE-DERIVED). Attribution "I said" Q-checked normally: Q1 load-bearing (first Taylor speech in chapter; speaker disambiguation needed); not redundant.

[¶11 S2] "\"Go on.\"" anchor=@25(dialogue-utterance continuation)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: taylor:2 @25 second utterance-sentence verbatim. Dialogue-utterance-derived; all Q pre-cleared.

[¶12 S1] "She moved the eyes to my hands before she spoke." anchor=@26(feel:3 verbatim)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: feel:3 @26 verbatim (REVERTED at Phase 5 from "her eyes" → "the eyes" per bone-object-policy verbatim discipline + chapter's "the eyes / the hands / the feet" convention). Pre-speech eye-move body-show; Wren's card §Look signature in physical operation. Load-bearing: NOTE-003 cost-bearer-seed delivery body-anchor.

[¶12 S2] "\"There were flies on the meat-stall,\" she said." anchor=@26(dialogue-utterance + dialogue-attribution)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: wren:2 @26 utterance verbatim. Dialogue-utterance-derived; all Q pre-cleared. Attribution "she said" Q1-checked: load-bearing for speaker-disambiguation following Taylor's @25 turn.

[¶12 S3] "\"There weren't any on your hand.\"" anchor=@26(dialogue-utterance continuation)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: wren:2 @26 second utterance-sentence verbatim — the chapter payload observation. Dialogue-utterance-derived; all Q pre-cleared.

[¶12 S4] "What the girl saw was what the read should have returned — the girl arrived at it without the insects." anchor=@26(narrator:6 verbatim; inverted-predicate cap)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: narrator:6 @26 verbatim (REVERTED at Phase 5 from "had arrived" → "arrived" per simple-past voice-transform). Inverted-predicate form is the one allowed use per file; foreknowledge-clamp register cap consumed legitimately. Counterfactual: removing loses the Taylor-interior receipt of Wren's observation — the chapter's payload-cognition register.

[¶13 S1] "I held the eyes." anchor=@27(bone-only held; vibes:9 schema-forbidden)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @27 SVO held; the deleted feel-taylor:3 @27 was the proto-receipt body-pair to feel:3 @26 — its deletion (R2.3 §Form temporal-latency seam) leaves @27 with only the bone surface. The held-eyes is the live downstream signal of receipt-without-filing. Counterfactual cut: removes the chapter's discipline-holding registration of the payload moment. Brevity-as-tell.

[¶13 S2] "She crossed the street." anchor=@28(bone-only chatter)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @28 SVO; Wren-exit kinetic. Counterfactual: removes Wren's physical departure-from-scene — Wren must exit on-page; cutting leaves her standing in the alley-mouth as the chapter closes.

[¶14 S1] "I lifted the needle." anchor=@29(bone-only held closing)
  Q1: yes  Q2: yes  Q3: no   Q4: no
  Q5: no   Q6: no   Q7: no   Q8: no   Q9: no
  → KEEP
  rationale: bone @29 SVO closing; held-needle-lift chapter-close. Brevity-as-tell per Phase 1 (the rule's verdict — return to work after the payload-collision). Counterfactual cut: removes the chapter's closing return-to-discipline beat.
```

### Phase 7 — completion summary

- sentences Q-walked: 37 of 37 (¶1: 1 / ¶2: 6 / ¶3: 4 / ¶4: 3 / ¶5: 4 / ¶6: 3 / ¶7: 2 / ¶8: 1 / ¶9: 2 / ¶10: 2 / ¶11: 2 / ¶12: 4 / ¶13: 2 / ¶14: 1)
- moves applied (count per move-class):
  - KEEP: 36
  - REWORD: 1 (¶4 S2 @12: "the hand-sensation" → "the hand")
  - CUT: 0
  - CUT-CLAUSE: 0
  - CUT-ASININE: 0
  - CUT-BONE: 0 (bones-cuttable license anchor-cut-only; no protective facets cut at Phase 7)
  - RESHOW: 0 (no Q8 triggers; Q9-density never approached the 3+ escalation threshold)
  - SIMPLIFY-PUNCT: 0 (em-dash + semicolon usage all licensed by exposition em-dash-fold, NI rubric post-directive, and lens-fold variance-moves; no "reached-for" punctuation found)
- FAULT-EXPOSITION-AUDIT-MISS: 0 (Q9 + Q6 checks on exposition-derived sentences ¶1 / ¶2 S4 / ¶8 all PASS)
- FAULT-DIALOGUE-AUDIT-MISS: 0 (Q9 checks on dialogue-utterance-derived sentences ¶9 / ¶11 / ¶12 all PASS; no utterance touched)
- FAULT-PHASE-7-NO-SWEEP: false (37 Q-lines emitted; one per sentence)
- bones-cuttable license invocation: NOT invoked (no PATTERN-ABANDONED bones from Phase 6; bone-CUT unauthorized)
- borderline-policy applied: strict-reject default + EXPOSITION-DERIVED/DIALOGUE-UTTERANCE-DERIVED carve-out KEEP — all borderlines on graph-resident lens + exposition + dialogue content resolved KEEP per policy
- persona discipline: neutral defers to profile defaults; no persona-specific bias applied

### Q9 rationale shard — ¶4 S2 hand-sensation REWORD

The single move-of-substance in this Phase 7 sweep is the REWORD at ¶4 S2 @12. Recording the full reasoning here because it is the only edit:

- **Facet verbatim:** sensory:2 reads `tactile: working-corner-open-air -> needle-through-mesh # tag: spike` (per `active-project/theater/facets/sensory-b01-c01.md` line 78). The arrow's tactile destination is "needle-through-mesh"; the modality-flag is "tactile".
- **Phase 1 fork-002 rendered:** "The needle crossed the mesh — thread-resistance and metal-smoothness, the hand-sensation taking its first count of the day." (scene-B L2).
- **Faithful prose-template rendering** of the arrow would have produced the perceptual pair (thread-resistance + metal-smoothness) — both are tactile particulars of needle-through-mesh, graph-resident-faithful. The trailing clause "the hand-sensation taking its first count of the day" is **stitcher prose** interpreting the modality-flag (tactile → hand-sensation) and adding the temporal frame (first count of the day) which is itself a chapter-register echo.
- **Q9 hit:** "hand-sensation" is an invented hyphenated nominalization compound (Q9 definition: invented compounds, jargon-ish nominalizations). Not graph-resident; not Westerosi-establishment-anchored; not facet-verbatim.
- **Substitution surface:** "the hand taking its first count of the day". The "-sensation" nominalization is dropped; "the hand" alone reads cleanly because (a) the preceding em-dash-folded pair "thread-resistance and metal-smoothness" already named the sensory particulars, (b) "count" carries the rhythmic-register continuity with @20's "count I had been running" and the chapter's cost-tracking ledger framing, and (c) "the hand" preserves the chapter's "the hands / the eyes / the feet" definite-article convention.
- **Density cap:** 1 substitution of ≤2 allowed per sentence. Q9-density did not approach the 3+ → RESHOW escalation threshold.
- **License:** Q9 REWORD per `staff/stitcher/card.md` § Phase 7 — a single-word/phrase meaning-preserving common-English equivalent substitution. Logged here.
- **Phase 7 draft delta:** `active-project/draft/b01-c01.phase-7.draft.md` differs from `active-project/draft/b01-c01.phase-6.draft.md` at exactly one location: ¶4 S2 (line 7 of the draft file), `"the hand-sensation taking its first count"` → `"the hand taking its first count"`. All other 36 sentences are byte-identical.

### Phase 7 draft

Phase 7 draft written: `active-project/draft/b01-c01.phase-7.draft.md`
- word count: 549 (Phase 6: 551; delta -2 from "-sensation" removal)
- sentence count: 37 (unchanged)
- paragraph count: 14 (unchanged)
- bones preserved: 27/27 (no cuts)
- moves: 1 REWORD; 0 other move-class moves

State machine: Phase 7 → complete (Phase 8 finalize + scene-callout strip + RECONCILE next).

---


