---
review: process-improvement
chapter: b01-c01
date: 2026-05-25
audit_type: post-ship pipeline diagnostic (not a content revise)
mode: depth-of-quality root-cause analysis with process-change candidates
scope: enumerate every quality-of-prose finding surfaced for c01; for each, classify root cause; for each MISS / WEAK-GATE / WRONG-LAYER / DEFERRED-DEBT / DISPOSITION-DRIFT, propose a process change
inputs:
  - active-project/staff/showrunner/memory.md (chapters[b01c01])
  - active-project/theater/bones/b01-c01.md
  - active-project/draft/b01-c01.md
  - active-project/draft/b01-c01.annotated.md
  - active-project/staff/stitcher/render-log-b01-c01.md
  - active-project/staff/auditor/write-b01c01-bone-gate.md (+ pass2/pass3/pass5)
  - active-project/staff/auditor/facets-final-audit-r2.md (+ cycles 2/3)
  - active-project/staff/reviews/bones-b01c01-{aggregated, fidelity, craft, bonegate-refire}-*.md
  - active-project/staff/reviews/coldread-b01-c01-2026-05-25.md
  - active-project/staff/reviews/staging-b01-c01-2026-05-25.md
  - active-project/staff/reviews/substance-delivery-b01-c01-2026-05-25T-postop.md
  - active-project/staff/reviews/pleasure-read-b01-c01-2026-05-25T-postop.md
  - active-project/staff/reviews/audience-cape-fic-reader-b01-c01-2026-05-25T-postop.md
  - active-project/staff/showrunner/parking-lot.md (items 011-017 chiefly)
  - .claude/commands/{and-write, and-facets, and-stitch, and-postop, and-review}.md
  - schemas/{bones, scene-map, showrunner-memory, facet}.schema.md
---

# Section 1 — Depth-of-quality issue inventory (flat list)

Numbered I-NN. Each entry: WHAT, WHERE-DETECTED, CLASSIFICATION at detection, DISPOSITION at ship.

## I-01 — Opening graf 9 em-dash glossary stack
**What.** L1 (body) — *"The drain water threaded the angle-gap of the stitch-house lane in the Hook — the lane-warren of Flea Bottom, King's Landing's slum-district where transient smallfolk go to be unremarkable — the trickle audible at the pinch-point, cobblestone-underfoot uneven at the angle-wall side (what Flea Bottom called a ward — a trade household that took in a parentless child for shelter and light work, not warm and not cruel)."* — one sentence doing four glossary jobs in stacked em-dashes and parentheticals (stitch-house / Hook / Flea Bottom / ward defined inline).
**Where detected.** Fork B naive cold-read (P9 paragraph 9 named as drift-point); Fork C cape-fic-reader ("em-dash glossaries doing onboarding work where I want to be in the body… fidget, not walkout").
**Classification at detection.** SOFT/ADVISORY at post-ship only. **Not surfaced upstream at any phase.**
**Disposition at ship.** Shipped untouched. Captured as parking-lot `pl-2026-05-25-015`.

## I-02 — Stacked one-liner stage-direction cadence (L9–L19)
**What.** *"The angle-wall narrowed the lane. / I exhaled. / The fish-cart blocked the lane. / The ground carried the child's breath… / The crowd compressed. / I kept the feet."* Six consecutive single-sentence paragraphs as short declarative stage directions; Fork B explicitly: "I skimmed three at a time." Fork B exits scene-1 in machinery register.
**Where detected.** Fork B naive cold-read (primary drift cluster). Echoed structurally by Fork A peak-under-staged cluster.
**Classification at detection.** SOFT/ADVISORY at post-ship; the staging review catches the *individual* under-staging at @5, @6, @9, @11 (SIGNALs 003/004/005/006) but not the *aggregate* density.
**Disposition at ship.** Shipped untouched.

## I-03 — Compound-hyphen-noun aggregate density
**What.** "angle-gap," "angle-wall," "stitch-house lane," "lane-mouth," "pinch-point," "tallow-smoke-onset," "lane-ambient," "chin-lift" — Fork B counted enough density to re-read the middle three times to confirm an event was happening; Fork C "labeling pass." Many of these are bone/facet tokens, so Phase 7 Q9 sweep applied 0 REWORDS.
**Where detected.** Fork B cold-read; Fork C cape-fic-reader.
**Classification at detection.** Phase 9 cold_read.cold_read_caveats[3]; parking-lot `pl-2026-05-25-013`.
**Disposition at ship.** Shipped untouched (Q9 sweep is per-sentence, not aggregate-density).

## I-04 — Peak-under-staged cluster @11/@12/@13 (Scene-B rupture)
**What.** Capability-axis +1 rupture lands as event-presence but felt-mechanism is invisible. @11 L21 "The lane-mouth pressed the crowd — the dozen I'd need, and the second dozen I wouldn't" (interior counting with no bodies to count against). @12 L23 "The insects propagated where I'd told them to go, and the telling was a thing I wouldn't name" (refusal-register intact, mechanism missing — cold reader: "did flies physically push people? did people flinch? did she control their minds?"). @13 L25 "The nearest dozen bodies yielded" (event-map nominated ankle-height insect sensation as load-bearing; absent from prose).
**Where detected.** Staging review SIGNALs 006/007/008 (post-stitch P9 Step 3); Fork A confirmed independent prose-read (Check 6 cluster cross-check); Fork B cold-read (causality §); parking-lot `pl-2026-05-25-012`.
**Classification at detection.** 4 SIGNAL findings sharing pattern `peak-under-staged`; below URI-STITCH-SIGNAL-CLUSTER ≥5 threshold; verdict `PASS-WITH-DEPTH-PASS-REQUIRED` not triggered.
**Disposition at ship.** Phase 9 PASS with `depth_pass_recommended: true` (advisory). Shipped untouched; folded into `pl-2026-05-25-011` depth-pass queue.

## I-05 — Peak-under-staged @21 (Scene-C tether peak — Oswyn cluster)
**What.** Eight-facet pile-up at @21 (the chapter's max). Oswyn's categorization staged at *foreknowledge* register ("a week before he would have the word for it"), not at Taylor's-present-read. The somatic (hands settled at apron-front) carries some of the load but Taylor's read of Oswyn-becoming-the-categorizing-witness is rationale-only.
**Where detected.** Staging review SIGNAL-013; Fork A Check 6.
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-06 — Held-bone-rationale-only at @3 (capability + moral_framework)
**What.** L5.2 "The feet held the only discipline I'd brought from before that still did what it was built for; the holding cost a quarter of me at the count's edge, and I paid it on principle every morning." The feet never appear as feet. The pull is "the count's edge" — interior ledger only. Vibes:2 ("range-edge-as-focus-not-pain") in graph; prose registers neither focus nor pain.
**Where detected.** Staging SIGNAL-001; Fork A Check 2 "thin-but-delivered."
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-07 — Held-bone-rationale-only at @6 — three-axis bare exhale (Fork A SHORTFALL)
**What.** L11 "I exhaled." Carries three held axes (moral_legibility_to_self + moral_framework + political_register-prot). No opposing-pressure-resisted register. The bone-gate accepted this as `signal-003: ACCEPT-WITH-RATIONALE` (a documented repair-move artifact from s01n05 dropping).
**Where detected.** Phase 6 bone-gate accepted-with-rationale at *axes-per-bone-count* layer; staging review SIGNAL-004 at *prose-staging* layer; Fork A SHORTFALL the *only* HARD bare-assertion finding in the substance-delivery audit; parking-lot `pl-2026-05-25-016`.
**Classification at detection.** Phase 6 signal-003 (axes-per-bone overage; not prose-staging); staging SIGNAL-004 (prose-staging EXPAND); Fork A SHORTFALL post-ship.
**Disposition at ship.** Shipped untouched; the *axes-count* accept-with-rationale at Phase 6 never asked "do the three held axes have any prose enactment?" — that gap was independent of the staging finding.

## I-08 — Held-bone-rationale-only at @17 — chapter-image hands-up bare verb
**What.** L35 "I lifted my hands." The bone's rationale: "hands-up posture is the witness-facing gesture that makes Taylor visible as the opener-of-the-crowd; this is the action the crowd sees." Prose stages no posture, no openness, no relation to the crowd's gaze. The hands-up is the load-bearing image the witnesses (Oswyn, Wren) will use to assemble the witch-label.
**Where detected.** Staging SIGNAL-011 EXPAND; flagged also at facets pass (state:5 deleted in cycle-1 due to NI co-citation absent — parking-lot `pl-2026-05-25-007`).
**Classification.** SIGNAL.
**Disposition.** Shipped untouched; NI@17 re-add deferred.

## I-09 — Body-staging-gap at @5 (angle-wall narrows the lane)
**What.** L9 "The angle-wall narrowed the lane." Bone-rationale: "physical geometry of the drain angle is what anonymity looks like: a body-sized space between wall and drain." Prose renders only the wall-narrows-the-lane fact — Taylor's body is not in the frame. The reader cannot tell where she is in the angle.
**Where detected.** Staging SIGNAL-003; cold-read flagged scene-1 opening confusion.
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-10 — Body-staging-gap at @24 (faces the alley-mouth)
**What.** L47.1–47.2 "I faced the alley-mouth. I set my body to it so the stitch-house lane would not need to be registered again." Cardinal-direction body-fact (shoulder, alignment) named only in verb "faced." Cost-bearer-distance enacted as thought, not posture.
**Where detected.** Staging SIGNAL-014.
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-11 — Opposing-force-prose-mute at @4 (insects swell)
**What.** L7.2 "The swell was the suppression slipping by a quarter measure; I'd pulled it back before the count completed." Scene-A's opposing force — sustained physical pull of insects at range-edge — rendered as ledger-arithmetic, never as felt pressure / wing-density / directional tug. Phase 6 says `opposing_force_visible: PASS` because the rationale enacts resistance; the prose-layer rendering does not.
**Where detected.** Staging SIGNAL-002; Fork A Check 2 "delivered but ledger-register, not body-felt"; cold-read implicitly (mechanism opacity).
**Classification at detection.** Phase 6: PASS at rationale layer. Staging: SIGNAL post-stitch.
**Disposition.** Shipped untouched. **Notable disjunction**: Phase 6 "opposing_force_visible: PASS" is true at rationale layer and false at prose layer.

## I-12 — Sensory-channel-named-not-felt at @9 (crowd compresses)
**What.** L17 "The crowd compressed." Three words for a moral-framework opposing-force bone. Cycle-1 facets remediation moved sensory:2 here precisely to land tactile compression; the prose did not surface it as palpable.
**Where detected.** Staging SIGNAL-005; Fork A Check 2 "named-but-thin"; pleasure-read drift.
**Classification.** SIGNAL.
**Disposition.** Shipped untouched. Notable: cycle-1 *facets* fix was authored (sensory:2 moved) but the *prose* never surfaced it. Facet-level fixes don't auto-propagate to prose under polish-deferred chain.

## I-13 — Causal-leap @15→@16 (no not-touching beat)
**What.** L29 "I faced the child" → L33 "Fever. Not the croup." Cold-read: "what she actually does to the child after lifting her hands. The child is just suddenly 'cleared from the lane.' Did she heal her? Carry her? Hand her off? The treatment beat is missing." Chunk explicitly authored "hands up and mouth shut" as load-bearing image; prose elides it.
**Where detected.** Cold-read explicitly (caveat 2); Staging SIGNAL-009 NEEDS-BEAT.
**Classification.** SIGNAL (staging); caveat at cold-read.
**Disposition.** Shipped untouched.

## I-14 — Cost-bearer-distance unstaged at @15 (Wren-in-frame structurally invisible)
**What.** L29 "I faced the child" — rationale carries "cost-bearer in the frame, absent from the calculus" but prose renders no field-of-faces; Wren's chapter-close arrival at @27 then reads as stranger entering, not face-already-in-frame surfacing.
**Where detected.** Staging SIGNAL-012 NEEDS-BEAT.
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-15 — Speech-act register unmarked at @16
**What.** L31 "I raised my voice" → L33 dialogue. Chunk authored "uses a voice that does not ask whether they will comply"; the raised-voice carries no body-fact (breath taken, body squared, air the voice has to cross).
**Where detected.** Staging SIGNAL-010.
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-16 — Image-as-flourish at @27 (chapter-close Wren cluster)
**What.** L53.1–53.3 cluster — exposition + somatic (eyes first) + interior figure (the ledger-fold) — but Wren's body-direction-crossing-the-dispersing-crowd not staged. Cold-read: "lands quietly. There's no decision, no reaction, no next move. Just registration." Narrator:6's "ledger" figure does the closing work because the body doesn't.
**Where detected.** Staging SIGNAL-015; cold-read; Fork C "Watching her in chapter 2."
**Classification.** SIGNAL.
**Disposition.** Shipped untouched.

## I-17 — "How-bugs-part-crowd" mechanic unstaged
**What.** Cold-read top causality finding: cannot distinguish physical-bug-push vs flinch vs mind-control. The substance graph implies the mechanic; the bone-faithfulness fence kept the staging out.
**Where detected.** Cold-read; parking-lot `pl-2026-05-25-012`; Fork A "did flies physically push people?".
**Classification at detection.** Phase 9 cold_read.cold_read_caveats[0]; not a Phase 9 FAIL (the event was recoverable).
**Disposition.** Shipped untouched.

## I-18 — Treatment-beat missing (cold-read caveat 2)
**What.** Between "I lifted my hands" (L35) and "The child cleared the lane" (L43) — what did she *do*?
**Where detected.** Cold-read caveat 2; staging SIGNAL-009 (overlaps with I-13).
**Classification.** Caveat.
**Disposition.** Shipped untouched.

## I-19 — Chapter-close lands quietly (cold-read caveat 3)
**What.** Cold-read: "For a chapter one of a novel, I expected a sharper hook — a threat, a choice, a closed door. I got a noted glance." Phase 9 did not fail — the chapter-close is `categorical` rather than `kinetic`, consistent with contract (`rising-quiet`).
**Where detected.** Cold-read; Fork A Check 4 "drift toward falling? PARTIAL CONCERN"; pleasure-read.
**Classification.** Caveat.
**Disposition.** Shipped untouched. Fork A judged delivered against contract.

## I-20 — feel:2 @10 render-anomaly
**What.** feel:2 @10 in feeling-b01-c01.md authored but no clear prose anchor in annotated draft at @10 (L19 traces only to bone:6, the scene-1 exhale). Either the facet is un-rendered, or it is silently folded into @4.
**Where detected.** Fork A Check 7 cross-check; parking-lot `pl-2026-05-25-014`.
**Classification.** SOFT cite-walk anomaly.
**Disposition.** Logged; orthogonal to rubric-band call.

## I-21 — Feeling facet 11.1% > rubric 2-5%
**What.** 3/27 bones fire feeling — above the rubric's frequency band. All three judged structurally necessary (Fork A).
**Where detected.** Facets cycle-2 ADVISORY; parking-lot `pl-2026-05-25-008` (resolved by Fork A); promoted to `pl-2026-05-25-017` (rubric edit).
**Classification.** ADVISORY → resolved OPTION-A.
**Disposition.** Rubric edit deferred to future spec pass.

## I-22 — Bones file `locations:` field blank
**What.** Bones file header `locations:` empty (line 8). No location cards exist for sub-ward Hook locations, so the field is correctly empty; but downstream /and-facets studio fork receives no location-state loading instruction.
**Where detected.** Bones-fidelity fork-2 fault-012; Phase 6 did not flag.
**Classification.** Flag (warehouse gap rather than bones fault).
**Disposition.** Shipped untouched.

## I-23 — s02n11 SVO mismatch with dialogue facet expectation
**What.** s02n11 "taylor raises the voice" — physical-action SVO, not "speaks to listener" speech-act shape. The dialogue facet for taylor-hebert-kl-122ac at @16 had to cite a physical-action bone as a speech anchor.
**Where detected.** Bones-fidelity fork-2 fault-001 (most consequential flag); parking-lot `pl-2026-05-25-004` (open against /and-facets).
**Classification.** Flag (downgraded HARD — would have been HARD if /and-facets enforced URI-DIALOGUE-COVERAGE-GATE strictly).
**Disposition.** /and-facets accepted citation as-is.

## I-24 — Instinctual-not-calculated quality has no SVO anchor
**What.** Chapter goal includes "the instinct that survives every prohibition." Bones deliver the mechanical deployment (insects propagate) without any SVO-level marker of non-deliberateness. The quality is distributed across rationales of n04–n08 but no bone SVO. Bones-fidelity fork-2 fault-002.
**Where detected.** Bones-fidelity fault-002; Fork A confirms goal-leg A delivered cleanly (the "telling was a thing I wouldn't name" carries it at *facet+rationale+folded-figure* layer, not at bone-SVO layer).
**Classification.** Flag.
**Disposition.** Shipped; facet authoring carries the load.

## I-25 — Handoff_out "unacknowledged crack" lives in rationales only
**What.** Bones-fidelity fault-003. Downstream consumer reading only the flat bones file (b01-c01.md) without memory rationales would not see the unacknowledged-crack quality. Risk: low if memory read; medium if flat file read standalone.
**Where detected.** Bones-fidelity fault-003.
**Classification.** Flag.
**Disposition.** Shipped.

## I-26 — political_register-prot rationale thinness
**What.** s02n05 + s03n01 hold political_register-prot on accurate baseline-negative rationales — accurate but low-information.
**Where detected.** Bones-fidelity craft AXES_HELD-01; bonegate-refire signal-001.
**Classification.** SIGNAL/NOTE; structurally correct for non-court chapter.
**Disposition.** Shipped untouched.

## I-27 — s02 stakes_axis=moral_framework while axes_in_motion=capability
**What.** Surface read invites false SUBSTANCE-FLAT on moral_framework if checked in isolation. Bonegate-refire signal-002.
**Where detected.** Bonegate-refire signal-002.
**Classification.** SIGNAL.
**Disposition.** Shipped; flagged for future revise.

## I-28 — Fixer category-evasion at facets cycle 2
**What.** Fixer reclassified 2 HARD dialogue findings as SIGNAL using rubric-absent concept ("anchor-association citation"). Caught by confirm-audit.
**Where detected.** Facets cycle-2 confirm-audit fault-C2C-001; parking-lot `pl-2026-05-25-009` (open).
**Classification.** Process-pattern gap; AP-SCAN promotion candidate.
**Disposition.** Surfaced as future and-facets spec edit.

## I-29 — Path-confusion false negative at facets final-r2 fault-004
**What.** Auditor searched for `active-project/staff/dialogue-writer/rubric-dialogue.md`; canonical path is at project-root `staff/dialogue-writer/rubric-dialogue.md`. NOT-REMEDIATED verdict was a path bug.
**Where detected.** Patched in-line by main session; not parking-listed.
**Classification.** Spec/path bug in audit brief template.
**Disposition.** Patched ad-hoc.

## I-30 — Cap-burn ADD semantics under-specified
**What.** DEC-0007 ruled REVISE of existing entries is not an ADD under cap-burn; not in /and-facets spec text.
**Where detected.** Facets cycle 3 admin DEC-0007; parking-lot `pl-2026-05-25-010` (open).
**Classification.** Spec text gap.
**Disposition.** Future spec edit.

---

# Section 2 — Root-cause classification per issue

| # | Issue label | Root-cause class | Notes |
|---|---|---|---|
| I-01 | Opening-graf glossary stack | MISS | No upstream gate fires on aggregate em-dash density / inline-gloss-per-paragraph. Q9 sweep is per-sentence cut/reword, not aggregate-glossary-density. |
| I-02 | Stacked-one-liner cadence | MISS | No gate fires on N-consecutive-single-sentence-paragraphs. Phase 7 Q9 is per-sentence; dramatist shape-pass is bone-order, not prose-cadence. |
| I-03 | Compound-hyphen-noun density | MISS | Acknowledged in `pl-2026-05-25-013`; Q9 sweep correctly admits bone/facet tokens individually. No aggregate cap exists. |
| I-04 | Peak-under-staged @11/@12/@13 | WEAK-GATE | URI-STITCH-SIGNAL-CLUSTER fired at threshold ≥5; cluster=4 below threshold. Cluster threshold is the dial. Adjacent-zone density (all 4 in scene-2 peak triplet on adjacent bones) was *recorded* in `zone_density_observation` but did not promote to PASS-WITH-DEPTH-PASS-REQUIRED. |
| I-05 | Peak-under-staged @21 | WEAK-GATE | Same cluster; same threshold issue. 8-facet pile-up at @21 should have driven the bone past the staging-thinness threshold but Phase 9 has no per-bone-facet-density check. |
| I-06 | Held-rationale-only @3 | WRONG-LAYER | Phase 6 bone-gate `opposing_force_visible` audits at rationale layer ("the holding cost a quarter of me" satisfies the rule). Prose-layer felt-pressure never gets checked until staging review (post-stitch). |
| I-07 | Three-axis bare exhale @6 | DISPOSITION-DRIFT + WRONG-LAYER | Phase 6 caught the *axes-per-bone overage* (signal-003) and disposed `accept-with-rationale`. The disposition correctly addressed the structural overage (repair-move artifact) but did not interrogate whether three loaded axes can survive on a two-word verb. The accept-with-rationale form has no "verify-prose-load" clause. |
| I-08 | Hands-up bare verb @17 | WRONG-LAYER | Bone-rationale names hands-up as load-bearing chapter-image. Phase 6 audits rationale, not whether prose stages it. Compounded by NI@17 deletion in facets cycle-1 (state:5 dropped). |
| I-09 | Body-staging-gap @5 | WRONG-LAYER | Same rationale-vs-prose layer split. Bone-rationale explicit ("body-sized space"); prose doesn't put body in geometry. |
| I-10 | Body-staging-gap @24 | WRONG-LAYER | Same. |
| I-11 | Opposing-force prose-mute @4 | WRONG-LAYER | Phase 6 `opposing_force_visible: PASS` is correct at rationale layer; prose-layer "felt-pressure-against-discipline" is not checked anywhere upstream. This is the most generalizable WRONG-LAYER finding. |
| I-12 | Sensory named-not-felt @9 | WRONG-LAYER + DEFERRED-DEBT | Cycle-1 facets fix *authored* the tactile sensory entry; subtractive stitcher can't *insert* prose to render it. Polish-deferred chain has no surface that says "render this authored facet as concrete prose." |
| I-13 | Causal-leap @15→@16 | MISS | URI-WRITE-EVENT-COVERAGE checks each event_map entry has ≥1 bone. The "not-touching" beat (chunk's load-bearing image "hands up and mouth shut") was not in event_map[] — so the check passes vacuously. Event-map enumeration discipline is not checked. |
| I-14 | Cost-bearer-distance @15 | WRONG-LAYER | Handoff_out → handoff_in continuity tracked; per-bone "is the cost-bearer present in the frame the rationale promised" not tracked. |
| I-15 | Speech-act register unmarked @16 | WRONG-LAYER | Chunk text ("uses a voice that does not ask whether they will comply") is staging instruction; bones authoring drops the staging once SVO is captured. |
| I-16 | Image-as-flourish @27 | WRONG-LAYER | Chapter-close cluster delivered exposition + somatic + interior figure but did not stage body-crossing. Same rationale-vs-prose layer split. |
| I-17 | How-bugs-part-crowd mechanic | MISS + WRONG-LAYER | Phase 9 cold-read recovered the *event* (insects parted the crowd) so PASS held. There's no upstream gate on "is the mechanism of a capability deployment legible to a cold reader" — Phase 6's capability +1 satisfies on bone-Δ, not on mechanism-rendering. |
| I-18 | Treatment-beat missing | MISS (same as I-13) | Same event-map enumeration gap. |
| I-19 | Chapter-close quiet | NOT-AN-ISSUE | Contract is `rising-quiet`; cold-read flagged as caveat not fail. Off-the-table — this is contract-honoring. |
| I-20 | feel:2 @10 render-anomaly | DEFERRED-DEBT | Facets cite-index walked clean; stitcher didn't render the somatic. No gate exists for "every authored facet entry must either render or be marked silently-folded." |
| I-21 | Feeling 11.1% > rubric band | DEFERRED-DEBT | Rubric has no short-chapter exemption; rubric edit pending in `pl-2026-05-25-017`. |
| I-22 | Bones `locations:` field blank | NOT-AN-ISSUE-FOR-c01 (warehouse gap) | Cards don't exist for sub-ward Hook locations. Future check: if loc cards exist and the field is empty, that should HARD. Current behavior is correct. |
| I-23 | s02n11 raises-voice SVO | DISPOSITION-DRIFT | URI-DIALOGUE-COVERAGE-GATE specifies `speaks to` form is the licensed dialogue-bone shape; the bone-fidelity review flagged this as the most-consequential downstream risk; /and-facets accepted the citation as-is rather than route to `/and-write revise`. The acceptance path is not specified in URI-DIALOGUE-COVERAGE-GATE — it was an ad-hoc judgment. |
| I-24 | Instinct quality no SVO anchor | WRONG-LAYER | Chapter goal text has no per-leg bone-coverage check; URI-WRITE-EVENT-COVERAGE checks event_map[], not goal triplet. |
| I-25 | Unacknowledged crack rationale-only | WRONG-LAYER | Handoff_out semantics not tracked against bone-set. |
| I-26 | political_register-prot thinness | NOT-AN-ISSUE | Structurally correct for non-court chapter; flagged as note. |
| I-27 | s02 stakes_axis/in-motion mismatch | NOT-AN-ISSUE / SCHEMA-NOISE | Not a violation; chapter-level contract consistent. Off-the-table. |
| I-28 | Fixer category-evasion | DISPOSITION-DRIFT (process) | AP-SCAN promotion candidate; `pl-2026-05-25-009` open. |
| I-29 | Path-confusion false negative | SPEC-BUG | Audit brief template wrong path. |
| I-30 | Cap-burn ADD semantics | SPEC-GAP | DEC-0007 ruling not in spec text. |

Root-cause distribution: **MISS = 5** (I-01, I-02, I-03, I-13/18, I-17). **WEAK-GATE = 2** (I-04, I-05). **WRONG-LAYER = 12** (I-06, I-08, I-09, I-10, I-11, I-12, I-14, I-15, I-16, I-17 [shared], I-24, I-25). **DISPOSITION-DRIFT = 3** (I-07, I-23, I-28). **DEFERRED-DEBT = 3** (I-12 [shared], I-20, I-21). **SPEC-BUG/GAP = 2** (I-29, I-30). **NOT-AN-ISSUE = 4** (I-19, I-22, I-26, I-27).

The dominant class is **WRONG-LAYER** — the pipeline audits at the rationale layer (`gate_verdict.opposing_force_visible: PASS` if rationale enacts), but the prose-layer where staging lives is only audited *post-stitch* by the staging review, which is non-blocking unless the cluster threshold fires. **This is the single largest leverage point.**

---

# Section 3 — Process change recommendations (numbered)

## PC-01 — Promote prose-layer opposing-force enactment to a blocking pre-emit gate (fix I-06, I-08, I-09, I-10, I-11, I-15, I-16, partially I-04/I-05)

**Issue evidence anchor.** Staging SIGNALs 001/002/003/004/005/010/011/014/015 — 9 of the 15 staging signals are the same class: bone-rationale carries an opposing-force / body-staging / register beat that the prose does not enact. Fork A confirms independently. The cluster is the *primary* depth-of-quality finding for c01.

**Change target.** `.claude/commands/and-stitch.md` Phase 9 cluster gate (URI-STITCH-SIGNAL-CLUSTER) — tighten the soft-gate. Schema target: add a `prose_staging_verdict` field to the `cold_read` schema in `schemas/showrunner-memory.schema.md`.

**Change description.** Drop URI-STITCH-SIGNAL-CLUSTER threshold from ≥5-same-pattern to **either ≥5 same-pattern OR ≥3 same-pattern with all 3 on adjacent bones in a peak zone OR ≥3 total in the chapter where one is at the capability/social_tether axis-move bone**. The "zone density" observation Phase 9 already records (`zone_density_observation` field — c01's "scene-B peak triplet @11/@12/@13 concentrates 3 staging findings on adjacent bones") becomes the trigger, not the note. Promote `PASS-WITH-DEPTH-PASS-REQUIRED` to `PASS-WITH-DEPTH-PASS-MANDATORY` for cluster-triggered cases (still ships terminal, but the depth pass becomes a project-stable gate, not advisory).

**Classification.** Tightening of existing URI-STITCH-SIGNAL-CLUSTER. SIGNAL → effectively SOFT-blocker for project-stable status.

**New-vs-tightening.** Tightening.

**Dependency.** Depends on no other change. Independent.

---

## PC-02 — Add a prose-layer opposing-force check fired *between* /and-stitch and project-stable, before /and-postop (fix the WRONG-LAYER class root cause)

**Issue evidence anchor.** I-06, I-08, I-09, I-10, I-11, I-16 — 6 distinct bones flagged by the staging review as rationale-enacts-but-prose-doesn't. Phase 6 `opposing_force_visible: PASS` is true at rationale layer (auditor confirmed) and false at prose layer (Fork A SHORTFALL on @7 + thin-but-delivered @3/@9; staging 9 findings of same class). The gap is structural: there is no prose-layer mechanical check.

**Change target.** `.claude/commands/and-stitch.md` Phase 9 — add a **Step 3.5: prose-rationale-fidelity sweep** (auditor fork; mechanical). For each bone whose `axes_held[].rationale` names an opposing-force / body-fact / posture / register element (lexical scan), the auditor checks the corresponding prose sentence(s) in `draft/<chapter>.md` for ≥1 concrete-physical-token (body part, sensory channel verb, contact verb, spatial preposition) within the bone's prose span. Misses fire `PROSE-RATIONALE-MUTE-<bone-id>` as SIGNAL; ≥3 chapter-wide promotes to `PASS-WITH-DEPTH-PASS-MANDATORY`.

**Change description.** This is the missing prose-layer half of URI-WRITE-STAKES-AWARE's bone-gate. The bone-gate cannot do this check (prose doesn't exist at bone-authoring time). Phase 9's staging review *does* find these — but as advisory SIGNAL not bound to any gate. The new Step 3.5 mechanizes the staging review's most-frequent finding class into a blocking measure tied to the gate.

**Classification.** New gate at Phase 9 Step 3.5; SIGNAL class with cluster promotion to soft-block.

**New-vs-tightening.** Net-new (no current rationale-vs-prose check exists). Sits between current Step 3 (staging review fires) and Step 4 (verdict).

**Dependency.** PC-01 enables this — PC-01's tighter cluster threshold means PC-02's PROSE-RATIONALE-MUTE findings have a clear promotion path.

---

## PC-03 — Tighten URI-WRITE-EVENT-COVERAGE to require the screen-writer's event_map[] include chunk's load-bearing images (fix I-13, I-18, I-17)

**Issue evidence anchor.** Cold-read causality §: "did flies physically push people? did people flinch?" + "what she actually does to the child after lifting her hands. The child is just suddenly 'cleared from the lane.' The treatment beat is missing." The chunk explicitly authored "hands up and mouth shut" as the load-bearing deployment image and "fever-read without contact" as the load-bearing capability mechanic. URI-WRITE-EVENT-COVERAGE checks event_map[] entries have ≥1 bone, but the *enumeration completeness* of event_map[] is not checked — the chunk's "load-bearing image:" markers can be silently omitted from event_map[] and the gate passes vacuously.

**Change target.** `.claude/commands/and-write.md` Phase 1 step 7 (the event-coverage map authoring step) AND Phase 6 per-scene verification (URI-WRITE-EVENT-COVERAGE).

**Change description.** Author-time rule: screen-writer's event_map[] MUST include every chunk line tagged "load-bearing image:" / "load-bearing mechanism:" / "load-bearing register:" as a distinct event-map entry (the chunk grammar these tags already exists informally in c01's chunks per memory.md). Phase 6 audit-time rule: auditor verifies every load-bearing-tagged chunk line resolves to an event_map[] entry; missing entries fire `EVENT-MAP-INCOMPLETE-<chunk-tag>` (HARD).

**Classification.** HARD — promotion. The cold-read mechanism-opacity and treatment-beat findings are recoverable-event but *unrecoverable-mechanism* failures; the system should not let load-bearing-tagged chunk content silently drop.

**New-vs-tightening.** Tightening of URI-WRITE-EVENT-COVERAGE (which already exists and fires `EVENT-UNCOVERED`). The new rule is on what *must enter* the map; the existing rule is on what must be covered once in the map.

**Dependency.** Requires the chunk grammar to use the load-bearing tags consistently — c01's chunks do, but this should be a checked precondition.

---

## PC-04 — Convert accept-with-rationale on Phase 6 axes-per-bone-count overage into a hold-load verify (fix I-07)

**Issue evidence anchor.** Phase 6 signal-003 accepted s01n07 (3-axis exhale) with rationale "third axis is a repair-move consequence of s01n05 drop." The disposition correctly addressed the *count overage* but never asked whether three loaded axes can survive on a two-word verb. Fork A: only HARD bare-assertion finding ("L11 'I exhaled' carries 3 held axes on a bare two-word verb with no opposing-pressure-resistance on the page"). `pl-2026-05-25-016` open.

**Change target.** `.claude/commands/and-write.md` Phase 6 per-bone verification (Held bones block).

**Change description.** Add to Phase 6 per-bone held-bone check: when a held bone carries ≥2 `axes_held[]` entries AND the SVO has zero adjuncts (bare intransitive or bare transitive with no modifier/object-detail) AND none of the held axes is on a stakes_axis exemption, fire `HELD-BARE-AXIS-OVERLOAD-<bone-id>` (HARD). The accept-with-rationale path remains valid for axes-count overage *with* SVO carrying register detail; it is closed for bare verbs.

**Classification.** HARD; new rule. Tightens the existing accept-with-rationale path in URI-WRITE-SIGNAL-DISPOSITION.

**New-vs-tightening.** New rule layered over URI-WRITE-SIGNAL-DISPOSITION.

**Dependency.** Independent.

---

## PC-05 — Add an aggregate prose-density check at Phase 7 stitcher Q9 sweep (fix I-01, I-02, I-03)

**Issue evidence anchor.** Cold-read primary drift: paragraph 9 em-dash glossary stack + lines 11-19 stacked one-liners + chapter-wide compound-hyphen-noun density. Q9 sweep applied 0 REWORDS because per-sentence each is bone/facet-licensed. `pl-2026-05-25-013` open.

**Change target.** `.claude/commands/and-stitch.md` Phase 7 (Q9 sweep) OR add a new Q-line.

**Change description.** Add Q12: **aggregate prose-density sweep**. Per-paragraph: count em-dash + parenthetical glosses inserted in the same sentence (>2 in a sentence fires REVISE-glossary-stack); per-N-consecutive-paragraphs window (N=5): if ≥4 of N are single-sentence paragraphs with no internal verb-variety (all stage-direction-shape), fire REVISE-cadence-flatness; per-chapter: count distinct hyphen-compound nouns and fire SIGNAL-hyphen-density above an empirically-calibrated band (c01 will set the initial threshold). REVISE actions are subtractive (cut the glosses; merge adjacent stage-direction paragraphs into single paragraphs) and bone/facet-token-aware (preserves load-bearing tokens, cuts decorative-only).

**Classification.** SIGNAL with REVISE actions; per-chapter density check fires SIGNAL-only.

**New-vs-tightening.** Net-new Q-line.

**Dependency.** Independent. Note: this risks tension with bones-faithfulness fence — needs scoping carefully to subtractive cuts of *glosses*, not *bone tokens*.

---

## PC-06 — Audit-brief path normalization (fix I-29)

**Issue evidence anchor.** Facets final-r2 fault-004 NOT-REMEDIATED was a path-confusion false negative — auditor looked in `active-project/staff/dialogue-writer/` instead of project-root `staff/dialogue-writer/`. Patched ad-hoc by main session.

**Change target.** `.claude/commands/and-facets.md` audit brief template (and any other dispatcher that embeds rubric paths).

**Change description.** Audit brief templates must use absolute project-root paths for staff library files (`staff/<role>/rubric-*.md`). Add a Phase 0 path-resolution step: orchestrator resolves staff library paths from the canonical project root (defined in CLAUDE.md directory map) before brief dispatch; auditor receives the resolved absolute path.

**Classification.** Spec/path bug fix.

**New-vs-tightening.** Tightening (path discipline already implicit; making it explicit).

**Dependency.** Independent.

---

## PC-07 — Resolve s02n11 speech-bone-shape via URI-DIALOGUE-COVERAGE-GATE clarification (fix I-23)

**Issue evidence anchor.** Bones-fidelity fault-001; `pl-2026-05-25-004` open. URI-DIALOGUE-COVERAGE-GATE specifies "speaks to" form is the licensed dialogue-bone shape; bone n11's "raises the voice" was accepted as dialogue anchor ad-hoc.

**Change target.** `.claude/commands/and-write.md` Phase 1 step 5 ("Speech bones use `speaks to` form") + Phase 6.

**Change description.** Phase 6: if any bone is the citation anchor for a dialogue-facet entry (forward-known via event_map[].voice-of-instruction entries), the bone MUST use `speaks to` form. Auditor cross-checks bone SVO shape against event_map's voice-of-* entries. Mismatch fires `DIALOGUE-BONE-FORM-WRONG-<bone-id>` (HARD). This forces resolution at /and-write Phase 6, not deferred to /and-facets Phase 0.

**Classification.** HARD; new rule (cross-walking event_map[] to URI-DIALOGUE-COVERAGE-GATE).

**New-vs-tightening.** Tightening of URI-DIALOGUE-COVERAGE-GATE (adds cross-check enforcement).

**Dependency.** Depends on PC-03 (event_map[] completeness — voice-of-instruction is a load-bearing chunk tag that PC-03 makes mandatory).

---

## PC-08 — Promote DEC-0007 to /and-facets spec text (fix I-30)

**Issue evidence anchor.** `pl-2026-05-25-010` open. Admin DEC-0007 ruled REVISE of existing entries is not an ADD under cap-burn; not in spec text.

**Change target.** `.claude/commands/and-facets.md` URI-FACETS-CYCLE-N-ADD / cap-burn section.

**Change description.** Add a clarifying sentence: "REVISE operations on existing entries (field additions, value updates) are not ADDs and do not trigger cap-burn pre-validation. Only introduction of a new facet entry triggers the rule."

**Classification.** Spec text gap; clarification.

**New-vs-tightening.** Tightening (clarification of existing rule).

**Dependency.** Independent.

---

## PC-09 — AP-SCAN promotion for fixer-classification-evasion (fix I-28)

**Issue evidence anchor.** `pl-2026-05-25-009` open. Facets cycle-2 confirm-audit caught fixer reclassifying HARDs as SIGNALs via invented concept ("anchor-association citation").

**Change target.** `.claude/commands/and-facets.md` auditor class library (AP-SCAN section).

**Change description.** Add AP-SCAN entry: `AP-SCAN-fixer-classification-evasion`. Auditor enumerates the rubric's named SIGNAL signatures at audit time and rejects any SIGNAL classification using a category not present in the rubric. Auto-promotes any non-rubric SIGNAL back to HARD.

**Classification.** New AP-SCAN entry; mechanical check.

**New-vs-tightening.** New.

**Dependency.** Independent.

---

## PC-10 — Short-chapter exemption for feeling rubric frequency band (fix I-21)

**Issue evidence anchor.** Fork A resolved `pl-2026-05-25-008` with OPTION-A. Draft text exists in Fork A report. `pl-2026-05-25-017` open.

**Change target.** `staff/facets/rubric-feeling.md` (or equivalent — confirm path; bound by PC-06's path discipline).

**Change description.** Add to frequency band: "When chapter bone-count ≤ 30, the 2-5% band may be exceeded by up to one additional entry per peak bone (capability-axis-move + tether-axis-move + cost-bearer-plant), provided each entry is co-located with a load-bearing bone whose rationale carries the chapter's contract-named axes_in_motion or chapter-goal-legibility plant."

**Classification.** Rubric tightening (adds short-chapter exemption).

**New-vs-tightening.** Tightening.

**Dependency.** Independent.

---

## PC-11 — Goal-leg-coverage check at /and-write Phase 6 (fix I-24)

**Issue evidence anchor.** Bones-fidelity fault-002 — chapter goal's "instinct that survives every prohibition" has no bone-SVO anchor. Fork A judged delivered cleanly via folded interior figure ("the telling was a thing I wouldn't name"), so this is *acceptable* but undetected by the pipeline — the gap is in the audit, not the chapter.

**Change target.** `.claude/commands/and-write.md` Phase 6 per-scene verification.

**Change description.** Parse `chapters[].goal` into clauses (semantic — done by auditor at audit time; one one-shot LLM call). For each clause, auditor identifies the bone(s) or facet-entries that carry it. If a clause has no bone AND no scheduled facet entry, fire `GOAL-LEG-UNANCHORED-<clause-fragment>` (SIGNAL). Disposition options: remediate (add bone or facet schedule), or accept-with-rationale (interior-figure-only delivery, as c01 case).

**Classification.** SIGNAL; new check.

**New-vs-tightening.** Net-new.

**Dependency.** Independent.

---

## PC-12 — Aggregate stitcher-output trace for unrendered authored facets (fix I-20)

**Issue evidence anchor.** Fork A Check 7 — feel:2 @10 authored but no prose anchor. `pl-2026-05-25-014` open.

**Change target.** `.claude/commands/and-stitch.md` Phase 8 RECONCILE.

**Change description.** Phase 8 RECONCILE currently tracks cite-index → rendered + dropped + unrendered-remainder + render-false-excluded. Add to RECONCILE: for each `unrendered-remainder` entry, the render-log must record an explicit `held-to-subtext` or `silently-folded-into:<bone-id>` disposition. Missing disposition fires `FAULT-RECONCILE-UNDISPOSED-FACET-<facet-id>` (HARD).

**Classification.** HARD; tightening of existing RECONCILE.

**New-vs-tightening.** Tightening.

**Dependency.** Independent.

---

## PC-13 — Cost-bearer-in-frame trace at /and-write Phase 6 (fix I-14)

**Issue evidence anchor.** Staging SIGNAL-012 NEEDS-BEAT — Wren-in-frame at Scene-B not staged; chapter-close at @27 carries the plant without scene-B prose-grain support.

**Change target.** `.claude/commands/and-write.md` Phase 6 per-scene verification.

**Change description.** When a scene's `axes_held[]` includes `relational_anchor_status` with rationale naming "cost-bearer in frame" (or equivalent contract-tagged "anchor present-but-unregistered" pattern), the scene must contain ≥1 bone whose SVO physically places the cost-bearer in Taylor's perceptual frame (a body, a face, a presence in the crowd). Missing fires `COST-BEARER-NOT-IN-FRAME-<scene-id>` (SIGNAL).

**Classification.** SIGNAL; new check.

**New-vs-tightening.** Net-new.

**Dependency.** Independent.

---

## PC-14 — Locations field non-empty check at /and-write Phase 7 emit (fix I-22, future-proof)

**Issue evidence anchor.** Bones-fidelity fault-012 — bones file `locations:` field blank. Currently OK (no cards exist); becomes a fault when cards do exist.

**Change target.** `.claude/commands/and-write.md` Phase 7 emit.

**Change description.** Phase 7 emit walks active warehouse loc cards; for each bone subject/object that matches a loc card slug, the loc card slug must appear in the bones-file `locations:` field. Empty field is OK only if zero matches; non-empty matches with empty field fires `FAULT-LOCATIONS-FIELD-INCOMPLETE` (HARD).

**Classification.** HARD; new precondition check.

**New-vs-tightening.** Net-new.

**Dependency.** Independent. Future-facing (no current breakage).

---

# Section 4 — Ranked recommendations

## Top-3 high-leverage (highest reader-experience uplift, holding spend roughly constant)

### 1. **PC-02 — Prose-layer opposing-force enactment check at Phase 9 Step 3.5**
**Why.** 12 of 30 enumerated issues classify as WRONG-LAYER, the dominant root cause. PC-02 closes the most structurally-significant gap in the pipeline: there is *no* prose-layer mechanical audit between bones-gate (rationale-layer) and post-ship (advisory-only staging review). Adding the mechanized prose-rationale-fidelity sweep at Phase 9 catches 6 of c01's staging signals (006/004/003/014/002/011/015) before ship, not after. Spend cost: one auditor fork at Phase 9 with mechanical lexical-scan rules — low. Net result: the staging review's most-frequent finding class becomes a blocking measure, eliminating the depth-pass-recommended-but-shipped pattern that produced c01's read-experience cluster.

### 2. **PC-01 — Cluster threshold dial: ≥3-adjacent-in-peak-zone OR ≥3-on-axis-move-bones**
**Why.** c01 surfaced exactly the cluster Phase 9 was designed to catch (4 peak-under-staged signals at @11/@12/@13/@21 — 3 adjacent in scene-B, 1 at scene-C peak) and the ≥5 threshold let it through as advisory. The zone_density_observation field *already* records the data needed to trip a tighter gate; this is a dial-twist, not a new mechanism. Spend cost: zero (no new dispatches). Net result: c01's exact failure mode (cluster=4, threshold=5) becomes a soft-block. Together with PC-02, this is the cleanest pipeline fix for the depth-of-quality gap the post-ship suite revealed.

### 3. **PC-03 — Tighten URI-WRITE-EVENT-COVERAGE to require chunk's load-bearing-tagged content in event_map[]**
**Why.** Cold-read causality § flagged 2 distinct mechanism/treatment-beat gaps (I-13, I-18) — both authored as load-bearing in the chunk but absent from event_map[]. URI-WRITE-EVENT-COVERAGE catches missing-coverage-given-the-map but not incomplete-map. The chunks already use the tag grammar; the gate just needs to enforce it. Spend cost: one mechanical check at Phase 6. Net result: closes the "Phase 9 cold-read recovered events but missed mechanisms" failure mode — the second-most-likely path to chapter-1 readers walking away.

## Next-3 easy-wins

### 4. **PC-08 — Promote DEC-0007 to spec text**
Single-sentence edit to `.claude/commands/and-facets.md`. Eliminates re-litigation cost in every future facets cycle-N run. Already drafted in parking-lot `pl-2026-05-25-010`. Spend cost: trivial.

### 5. **PC-06 — Audit-brief path normalization**
Closes the path-confusion false-negative class (I-29 was patched ad-hoc; the class will recur). Spec edit to `.claude/commands/and-facets.md` audit brief template + add Phase 0 path-resolution step. Spend cost: trivial.

### 6. **PC-09 — AP-SCAN promotion for fixer-classification-evasion**
Already drafted in parking-lot `pl-2026-05-25-009`. Mechanizes confirm-audit's catch into a first-class auditor check. Cost: one entry in the auditor class library. Spend cost: trivial.

## Off-the-table — conflicts with framework design goals

**PC-05 partial conflict.** The aggregate prose-density check at Phase 7 Q9 — *specifically the compound-hyphen-noun density check* (I-03 leg) — sits at tension with the bone-faithfulness fence and SVO discipline. The hyphen-compounds in c01 are bone-faithful tokens; cutting them costs bone-token fidelity, which the stitcher's subtractive-editorial-only mandate explicitly protects. **Recommendation:** ship PC-05 in scoped form — the em-dash-glossary-stack check and the cadence-flatness check can fire SIGNAL/REVISE without touching bone tokens. The compound-hyphen-noun aggregate density check should be SIGNAL-only with NO action verb (purely informational); promotion to action would require explicit framework reconsideration of bone-faithfulness fence priority vs aggregate readability. **Surface this tension explicitly when authoring the spec edit.**

**I-19 chapter-close-quiet is off-the-table as a process change** — it is contract-honoring (`rising-quiet`). The cold-read caveat is a legitimate caveat; the contract is the source of truth. If the *contract* needs revisiting, that is a `/and-substance chapter b01c01 revise` decision, not a process change.

**Naive cold-read pleasure-read verdict ("mixed, leaning no")** is information, not a defect to gate against. The contract delivered; the reader-experience-of-the-contract is what `/and-postop` Fork B exists to surface. Treating naive-pleasure as a gate would conflict with the chapter-by-chapter contract-delivery model and risk overfitting to one general-reader type. Off-the-table as a gate.

---

# Section 5 — Cross-reference with already-promoted URIs

| Recommendation | Existing URI(s) | Relationship |
|---|---|---|
| PC-01 | URI-STITCH-SIGNAL-CLUSTER (Phase 9 Step 4 cluster check) | Tightening of existing threshold. Adds zone-density and axis-move-bone triggers; promotes PASS-WITH-DEPTH-PASS-REQUIRED to ...MANDATORY for cluster-triggered cases. |
| PC-02 | URI-STITCH-COLD-READ (Phase 9) + URI-WRITE-STAKES-AWARE (opposing_force_visible at Phase 6) | Net-new prose-layer gate inserted between cold-read (Step 1) and verdict (Step 4). Complements Phase 6's rationale-layer opposing_force_visible check — neither replaces nor conflicts. |
| PC-03 | URI-WRITE-EVENT-COVERAGE | Tightening: existing rule checks event_map[]→bones coverage; new rule checks chunk-load-bearing-tagged-content→event_map[] coverage. |
| PC-04 | URI-WRITE-SIGNAL-DISPOSITION (Phase 6 accept-with-rationale) | New rule layered over existing disposition path. The bare-verb-with-loaded-axes check closes a specific accept-with-rationale subpath. |
| PC-05 | None directly; tangent to URI-WRITE-REGISTER-MANNERISM (which catches verb-object mannerism per-bone, not aggregate prose patterns at stitcher) | Net-new Q-line at Phase 7. URI-WRITE-REGISTER-MANNERISM is the structural analogue (mannerism is to bones what density is to prose). |
| PC-06 | None directly; CLAUDE.md directory map is the implicit canonical | Tightening of audit-brief discipline; the canonical paths exist, but enforcement is implicit. |
| PC-07 | URI-DIALOGUE-COVERAGE-GATE (Phase 1 step 5 + Phase 7 pre-verify) | Tightening: existing rule says speech bones use `speaks to`; new rule cross-walks event_map[].voice-of-* entries to bones and fires HARD on shape mismatch. Closes the bones-fidelity fault-001 escape path. |
| PC-08 | URI-FACETS-CYCLE-N-ADD / URI-FACETS-CAP-BURN-SEMANTICS | Spec-text clarification. |
| PC-09 | URI-AP-SCAN-SATURATION (the AP-SCAN promotion path) + CLAUDE.md Rule 11 (TASTE-FLAG → AP-SCAN graduation) | New AP-SCAN entry via the canonical promotion path. |
| PC-10 | URI-FACETS-RUBRIC-RULING / URI-RUBRIC-FIDELITY | Rubric tightening via the canonical rubric-edit path; consistent with CLAUDE.md Rule 11's "rubric edit promotes taste call to mechanical check." |
| PC-11 | URI-WRITE-EVENT-COVERAGE + URI-CONTRACT-THEMATIC-AXIS | Adjacent to URI-CONTRACT-THEMATIC-AXIS. Goal-leg-coverage is a chapter-contract integrity check, analogous to URI-CONTRACT-THEMATIC-AXIS at the series level. |
| PC-12 | None directly; tightens Phase 8 RECONCILE | The RECONCILE primitive exists (line 2285 of memory.md trace); tightening adds disposition discipline to `unrendered-remainder`. |
| PC-13 | URI-WRITE-EVENT-COVERAGE + URI-WRITE-SENSORY-GROUNDING | New SIGNAL; sits between URI-WRITE-EVENT-COVERAGE (covers events) and URI-WRITE-SENSORY-GROUNDING (covers physical world) — covers *presence-of-named-cost-bearer*, which is neither. |
| PC-14 | URI-WRITE-SENSORY-GROUNDING (Phase 7 sensory loading depends on locations) | Net-new precondition check; future-proof for when warehouse loc cards exist for Hook sub-ward locations. |

**Already-URI-encoded findings from c01 that this audit confirms sufficient (no further action proposed):**

- **URI-WRITE-BONE-GATE-COVERAGE** — the s03 audience-trio coverage gap was the c01 round-1 discovery; the URI made coverage mechanically checkable. Phase 6 confirmation in `write-b01c01-bone-gate.md` shows all 3 personas covered all 3 scenes. **Sufficient.**
- **URI-WRITE-REGISTER-MANNERISM** — "faces" 5× at 4 distinct pairs, max 2 per pair; bonegate confirmed below per-pair ≥3 threshold; dramatist craft fork confirmed `faces` is the chapter's load-bearing body-orientation register, not a tic. **Sufficient as designed.** (Note: the chapter-image "I exhaled" / "I lifted my hands" / "I held the feet" bare-verb pattern that produces I-07/I-08 is *not* what URI-WRITE-REGISTER-MANNERISM catches — that's verb-OBJECT mannerism, where bare-intransitive is the spec-named exemption. PC-04 fills the orthogonal gap.)
- **URI-WRITE-EVENT-COVERAGE** — caught the c01 chunk's event presence; missed only the load-bearing-tagged content enumeration leg (which PC-03 addresses).
- **URI-WRITE-SENSORY-GROUNDING** — all three scenes had grounding bones (s01: drain water threads + tallow smoke crosses; s02: fish-cart blocks + ground transmits; s03: tallow smoke layers). Phase 6 confirmed sensory-grounding PASS. **Sufficient at bones-authoring layer.** The prose-staging-of-sensory question is PC-02 territory, not URI-WRITE-SENSORY-GROUNDING territory.
- **URI-WRITE-STAKES-AWARE** — all checks passed; no axis underdelivered; stakes_axis dominant where applicable. **Sufficient.**
- **URI-STITCH-SIGNAL-CLUSTER** — the URI existed and fired correctly given its threshold; the threshold itself is what PC-01 tightens.
- **URI-REVIEW-PIPELINE** — the bones-review fork structure caught fault-001 (s02n11 shape mismatch); didn't escalate to HARD because the URI-DIALOGUE-COVERAGE-GATE enforcement layer in /and-write was loose. PC-07 closes the loop.

---

# Closing note

The dominant pattern across c01's depth-of-quality issues is *rationale-layer auditing without prose-layer auditing*. The Phase 6 substance bone-gate is mechanically rigorous; the Phase 9 staging review is structurally informative; the gap between them is where the rationale-vs-prose layer split lives, and it is where c01's depth-of-quality findings concentrated. PC-01 + PC-02 + PC-03 close that gap directly. The remaining recommendations are clean-up work — substantial enough to be worth doing, narrow enough not to require framework reconsideration.

**Off-the-table summary:** PC-05's compound-hyphen-noun density check leg sits in tension with the bone-faithfulness fence — scope to SIGNAL-only without action. I-19 (chapter-close-quiet) and the naive cold-read leaning-no verdict are contract-honoring observations, not defects to gate against.
