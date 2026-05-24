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


