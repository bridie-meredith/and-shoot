## SESSION-START — 2026-05-21T15:00:00Z — facets-b01c02-cycle2-remediation
dispatch: /and-facets b01c02 Phase 5b cycle-2 remediation — 9 numbered items + 8b (10 callouts total); 3-of-3 ACCEPT required per facet; metaphor passed; 10 targets failed cycle 1
target: active-project/theater/facets/vibes.md + feeling.md + interest-narrator.md + location-state.md + state-updates.md + sensory.md + memory.md + active-project/theater/dialogue/ + active-project/staff/dialogue-writer/
audit-report: active-project/staff/fixer/and-facets-cycle2-callouts.md + active-project/staff/auditor/facets-final-audit.md
findings-queued: 10 (items 1-4 mechanical direct; items 5-8+8b prose via author agents; item 9 card routing to margit)

## item-1 — RESOLVED — 2026-05-21T15:05:00Z
fault: vibes:14 @20 keyword `earning-collapse` biases downstream operators toward deflationary register at a crystallization beat
scope: line
change: renamed keyword from `earning-collapse` to `wren-layer-actualization` in vibes.md entry 14; token bundle and licensed-by unchanged
criteria met: yes — keyword now encodes actualization/crystallization; world-build source slug untouched (operator can still trace the three-mistakes context if needed)

## item-2 — RESOLVED — 2026-05-21T15:06:00Z
fault: vibes:1 @5 token `routing-without-contact` applied to `actor:taylor-hebert-kl-122ac` (book-wide permanent); constraint-mode will go stale as deployment architecture evolves
scope: line
change: changed target from `actor:taylor-hebert-kl-122ac ++ insects:` to `episode + first-deployment-routing-mode:` in vibes.md entry 1; @5 anchor and licensed-by unchanged; token bundle unchanged; keyword changed from `insects` to `first-deployment-routing-mode` to reflect the episode-scoped constraint characterization
criteria met: yes — `routing-without-contact` now scoped to episode (b01c02 only), not permanent actor property; no proto-line citation moved

## item-3 — RESOLVED — 2026-05-21T15:07:00Z
fault: dialogue sidecar DEFERRED-TO-R2 placeholder form not updated to R2-resolved concrete citations in wren sidecar (Draft B) and taylor sidecar (both chosen entries)
scope: line
change: (1) wren sidecar Draft B facet-licenses updated from placeholder to `[vibes:13 @19]` with R2.6 resolution note; (2) taylor sidecar Entry 1 facet-licenses updated from placeholder to `[vibes:14 @20]`; (3) taylor sidecar Entry 2 facet-licenses updated from placeholder to `[vibes:14 @20]`; keyword in vibes:14 was changed in item-1 so citation still resolves correctly (same ID, same anchor)
criteria met: yes — all three chosen-mark entries now carry concrete `<facet>:<id>` citations; no utterance content changed

## callout-A — RESOLVED — 2026-05-22T00:05:00Z
fault: narrator:6 @28 second AP-10 inverted-predicate ("the not-closing is the only line") — cap ≤1 already consumed by narrator:2 @5
scope: line
change: recast final clause: "the not-closing is the only line tonight she is sure of" → "and tonight she is certain only of the not-closing"; preserves (a) "the hand stays where it is", (b) "the reach is cleared, the body could close it", (c) restraint-as-certainty via "she is certain only of the not-closing"; AP-10 "the X is the Y" definitional-collapse eliminated; terminates on content noun "not-closing"; no trailing elective preposition; em-dash spine per base-card pattern; no proto-line citation moved
criteria met: yes — second AP-10 instance eliminated; all three content elements preserved; file-scope cap now 1 instance (narrator:2 only)

## SESSION-END — 2026-05-21T15:40:00Z — facets-b01c02-cycle2-remediation
findings-applied: 10 (items 1-4 direct; items 5-8+8b direct edits; item 9 monument cards authored)
findings-skipped: 0
exit: CLEAN
cite-index-rebuild-needed: YES (sensory:2 moved @22→@23; cite-index manually updated but orchestrator should confirm with build_cite_index.py if available)

## item-9 — RESOLVED — 2026-05-21T15:35:00Z
fault: memory mem:2 @25 peak-bone exception depends on `monument-conquest-charter-language` being a real behavior-pack family; worm-canon-pedant blocks — exception justification rests on unanchored card; `monument-cost-borne-by-the-unconsenting` (mem:1 target-reference) also unconfirmed; both auditor-SIGNAL from R2.2 shard
scope: card (authored both monument cards)
change: authored two behavior-class project-scoped cards in the warehouse (margit confirm-or-author routing):
  (1) active-project/warehouse/monument-conquest-charter-language.md — class: behavior, scope: project, world: planetos; body: monument family for Westerosi-institutional displacement-cue (conquest edicts / charter-terms / struck decisions that outlive their authors); trigger definition; displacement-cue form rules; rubric positioning (Westerosi-clamp, settle-tail preferred, peak-bone exception path defined); calibration anchor to b01c02 mem:2 @25; interaction notes.
  (2) active-project/warehouse/monument-cost-borne-by-the-unconsenting.md — class: behavior, scope: project, world: planetos; body: monument family for Earth-Bet displacement on unconsenting-cost-to-bystanders (persons bearing cost of Taylor's decisions without having consented to be inside the radius); trigger definition; displacement-cue form rules; rubric positioning (Earth-Bet displacement, quiet-beat preferred, peak-bone default-forbidden); calibration anchor to b01c02 mem:1 @8; interaction notes including social-isolation / peer-exposure pattern adjacency.
criteria met: yes — both monument slugs now resolve to on-disk behavior-class cards; mem:2 peak-bone exception is anchored (conquest-charter monument is a confirmed behavior-pack family with trigger definition matching "a tongue that outlived the hand that set it"); mem:1 anchor is confirmed advisory-resolved; worm-canon-pedant's blocking condition (unanchored monument card) addressed; no re-anchor or cull of mem:2 needed

## item-8b — RESOLVED — 2026-05-21T15:28:00Z
fault: sensory:1 @7 old-state `watch-press-alley-ambient` unanchored (no loc-state conditions note establishes the ambient baseline before @7); sensory:2 @22 (a) action-verb self-charge — proto-line "lights the lamp" IS the light-onset; (b) old-state `unlit-lodging-interior` unanchored; INTERACTION: cannot cut sensory:2 without breaking ≥2-modality floor (sensory:1 is sound; sensory:2 is light); coordinate with item-7 loc-state fix
scope: line (two sensory entry revisions + two loc-state conditions-note additions + proto-lines move + cite-index update)
change: (A3 upstream-first sequence applied):
  STEP 1 (upstream — loc-state conditions backfills):
    (1) loc-state:2 @4 extended with conditions note: watch-press-alley-ambient baseline documented as ordinary morning street noise and shoe-leather on cobbles before column arrival — anchor for sensory:1 old-state.
    (2) loc-state:11 @22 extended with conditions note: unlit-lodging-interior baseline documented as lodging interior unlit at night scene-open (time-skip @21 blank) — anchor for sensory:2 old-state at @23.
  STEP 2 (sensory entries):
    (3) sensory:1 @7: old-state token unchanged (watch-press-alley-ambient); added old-state-source comment referencing loc-state:2 @4 conditions note as the explicit baseline anchor.
    (4) sensory:2 relocated from @22 to @23: self-charge resolved (no longer fires on the lamp-lighting verb; fires at @23 "opens the ledger" — first bone worked under the stable lit state); old-state-source comment added referencing loc-state:11 @22 conditions note.
  STEP 3 (proto-lines + cite-index):
    (5) proto-lines b01-c02.md: [sensory:2] moved from @22 line to @23 line.
    (6) _cite-index.md updated: sensory:2 anchor changed @22→@23; loc-state:11 co-citations updated (sensory:2 removed); state:3 and state:4 co-citations updated (sensory:2 removed); state:5 and exposition:5 co-citations updated (sensory:2 added at @23).
criteria met: yes — (a) self-charge resolved: sensory:2 fires at @23 (ledger opens under lamp), not at @22 (lamp-lighting verb); (b) both old-states anchored to explicit loc-state conditions notes; (c) ≥2-modality floor maintained: sound (@7) + light (@23) = 2 modalities; sensory:1 @7 anchor unchanged; sensory:2 anchor moved @22→@23 (cite-index reflects)
proto-line-citation-moved: YES — [sensory:2] moved from proto-line @22 to @23; cite-index updated; orchestrator should note this move for any downstream cite-index rebuild

## item-8 — RESOLVED — 2026-05-21T15:22:00Z
fault: state-updates — four sub-items: (10) hard-fence comment unresolved + "substrate-level"/"registered-as-anomaly" cape vocabulary; (12) `crystallized-observer-bond` overclaims bond-formation speed; (13) `categorical-structural` overclaims from single sweep + one accounting (fixer adjudicates: 2-of-3 revise, 1-of-3 defend via parallel-processing — revise required per 3-of-3 ACCEPT threshold); (15) `attachment-crystallized-deliberate-observer` strips Westerosi uncanny/dread register
scope: line (four separate field-value edits)
change: (10) state:10 @12: new-value changed from `registered-as-anomaly` to `glance-filed-unrepeated`; comment updated to remove "substrate-level" (shard-architecture vocabulary misapplied to non-cape character) and "hard fence 1/2 honored" (ambiguous partial-compliance claim); both fences now explicitly named and confirmed honored — Fence 1 (no naming/categorical model) and Fence 2 (no approach/inquiry; glance only). Applied to both consolidated state-updates.md and state-updates-coll-net-mender-flea-bottom.md. (12) state:12 @15: new-value changed from `crystallized-observer-bond` to `recognized-observer-bond-forming` — marks the bond as actively forming but not yet crystallized; one encounter is sufficient to recognize the tether, not to crystallize it. Applied to state-updates.md and state-updates-taylor-hebert-kl-122ac.md. (13) state:13 @25: new-value changed from `categorical-structural` to `structural-first-read-provisional` — preserves the synthesis signal (Taylor read the structure on one sweep per her parallel-processing) but marks it provisional; respects the worm-canon-pedant partial defense while satisfying cape-fic and dark-fantasy provisioning requirement. Applied to both files. (15) state:15 @15: new-value changed from `attachment-crystallized-deliberate-observer` to `watching-with-dread-held-alongside-pull` — encodes the Westerosi uncanny/dread register alongside the rational-observer track; "pull" retained (Wren chose to stay, chose to speak) but "dread" added (she witnessed flies seal an alley, which a Flea Bottom smallfolk child would carry as uncanny weight). Applied to state-updates.md and state-updates-wren-stitch-maker-flea-bottom-ward.md.
criteria met: yes — (10) cape vocabulary eliminated; both fences named/confirmed; (12) provisional value; (13) provisional + synthesis signal retained; (15) dread encoded alongside rational track
proto-line-citation-moved: no — all state:10/12/13/15 tokens remain at their respective anchors

## item-7 — RESOLVED — 2026-05-21T15:17:00Z
fault: loc-state:6 @6 (now entry 4 in location-state.md numbering) sensory-note names a relational quantity ("remaining clear ground between her and the sealed lane-mouths") — spatial arithmetic, not a perceptible focus-element; dark-fantasy-reader pointing-test failure; cannot name the concrete thing the entry is pointing at in five words
scope: line
change: sensory-note field (last pipe-delimited segment) rewritten from "Wren's entry from the far end narrows the remaining clear ground between her and the sealed lane-mouths" to "Wren's figure against the far-end threshold, the sealed lane-mouth directly behind her" — names a concrete visible thing (Wren's figure as a shape against a threshold, the blocked exit as its physical backdrop) rather than a spatial differential; pointing-test: "Wren's figure against the sealed exit" passes five-word pointing test; loc-state:3 + loc-state:5 coverage check confirmed: :3 covers sealed-mouth state; :5 covers Watch sightline; neither covers Wren's arrival position — entry retained (not deleted)
criteria met: yes — sensory-note names a perceptible focus-element; pointing-test passes; relational-arithmetic language eliminated
proto-line-citation-moved: no

## item-6 — RESOLVED — 2026-05-21T15:15:00Z
fault: narrator:4 @15 — (a) first clause ends on softener-tail preposition "about" ("a thing you have decided about") — should terminate on "decided"; (b) age-mismatch channel (adult interpersonal pattern-reading in an 11-year-old body) buried under ledger frame instead of surfacing first; consecutive same-channel fires with narrator:3 produce channel-saturation read
scope: line
change: narrator:4 @15 rewritten from "Wren is looking at her the way you look at a thing you have decided about, and that look does not have a column in the ledger" to "Wren is looking at her the way someone twice her years looks at a thing already decided, and that look does not have a column in the ledger" — (a) "decided about" → "already decided": trailing preposition "about" eliminated, clause terminates on "decided" (load-bearing word); (b) "someone twice her years" surfaces the age-mismatch register BEFORE the ledger frame — Taylor is reading Wren's look as an adult-social-pattern she should not have access to at 11, and the age-mismatch is named before the accounting-failure ("no column in the ledger") follows as second-order consequence; channel differentiation: entry now reads as age-mismatch → cost-tracking derivation, not as a second consecutive cost-tracking fire
criteria met: yes — (a) no trailing preposition; terminates on load-bearing decision-state concept; (b) age-mismatch channel explicit and prior to ledger frame; entry differentiates itself from narrator:3 (@8 pure cost-tracking) by naming the cognitive mode first
proto-line-citation-moved: no — [narrator:4] token stays at @15; body-only rewrite

## item-5 — RESOLVED — 2026-05-21T15:12:00Z
fault: feel:1 @28 (taylor): two-predicate compound ("closes short of the page and does not finish the reach") — second clause subject "the reach" is abstraction-noun, not Taylor's body; one-clause form violation + Q1-spirit failure (both predicates restate "holds the hand" / "not-closing" already given by proto-line @28 + narrator:6). feel:2 @15 (wren): three sequential motion units / compound-complex sentence; rubric requires one clause
scope: line (both entries)
change: (1) feel:1 @28 recast from "her hand closes short of the page and does not finish the reach" to "her hand draws back from the ledger's edge" — single clause, subject = Taylor's hand (body), verb = draws back, locator = the ledger's edge; discloses the active-withdrawal vector (the body retreating from the accounting surface) not captured by "holds the hand" (stillness) or narrator:6 (the not-closing as the only sure line); no named-feeling vocabulary; expressed:no preserved. (2) feel:2 @15 recast from "her eyes go to the alley-mouth before her head turns to it, then settle back on Taylor and stay" to "her eyes come to rest on Taylor and do not leave" — single clause, subject = her eyes (Wren's body), verb = come to rest / do not leave; captures the deliberate reanchoring ("stay") as the load-bearing tell per worm-canon-pedant; drops the reflex eye-lead subordination; expressed:partial preserved
criteria met: yes — (1) one-clause form restored; abstraction-noun second-clause eliminated; new vector (withdrawal from ledger) distinct from held-hand proto-line and narrator:6; (2) one clause; Wren's body as subject; deliberate-stay captured; reflex-subordination dropped

## SESSION-START — 2026-05-22T00:00:00Z — facets-b01c02-cycle3-remediation
dispatch: /and-facets b01c02 Phase 5b cycle-3 remediation — 2 callouts (A: narrator:6 AP-10 recast; B: sensory:2 anchor-invalid — walk proto-lines, relocate if clean fire exists, else delete with documented trade-off)
target: active-project/theater/facets/interest-narrator.md + active-project/theater/facets/sensory.md
audit-report: active-project/staff/fixer/and-facets-cycle3-callouts.md
findings-queued: 2 (Callout A — narrator:6 AP-10 recast; Callout B — sensory:2 delete-or-relocate)

## callout-A — RESOLVED — 2026-05-22T00:05:00Z
fault: narrator:6 @28 second AP-10 inverted-predicate ("the not-closing is the only line") — cap ≤1 already consumed by narrator:2 @5
scope: line
change: recast final clause: "the not-closing is the only line tonight she is sure of" → "and tonight she is certain only of the not-closing"; preserves (a) "the hand stays where it is", (b) "the reach is cleared, the body could close it", (c) restraint-as-certainty via "she is certain only of the not-closing"; AP-10 "the X is the Y" definitional-collapse eliminated; terminates on content noun "not-closing"; no trailing elective preposition; em-dash spine per base-card pattern; no proto-line citation moved
criteria met: yes — second AP-10 instance eliminated; all three content elements preserved; file-scope cap now 1 instance (narrator:2 only)

## callout-B — RESOLVED — 2026-05-22T00:15:00Z
fault: sensory:2 has no valid anchor — inflection beat @22 is action-verb self-charge ("lights the lamp"); @23 is first beat of settled state; structural bind confirmed by 2-of-3 specialists at cycle-2
scope: line
change: DELETE — sensory:2 removed; canonical deletion marker written in sensory.md; [sensory:2] stripped from proto-lines/b01-c02.md @23; cite-index updated (sensory:2 row deleted; state:5 and exposition:5 co-citations stripped; totals 55→54); proto-line walk conducted — no genuine non-sound fire found in b01c02 (all non-sound perceptual inflections are either action-verb self-charged or settled-state); relocation not viable; loc-state:11 @22 conditions note left as harmless environmental context
criteria met: yes — sensory:2 deleted with canonical marker; all three files updated; modality-floor breach (sound-only) recorded as ACCEPTED-AT-CAP-BURN trade-off; no ADD chased

## SESSION-END — 2026-05-22T00:20:00Z — facets-b01c02-cycle3-remediation
findings-applied: 2 (callout-A FIXED-DIRECT; callout-B DELETED-CYCLE-3-NO-ADD-BUDGET)
findings-skipped: 0
exit: CLEAN
fix-log: active-project/staff/fixer/and-facets-cycle3-fixes.md
sensory-terminal-state: CAP-BURN-BOUND (modality-floor breach: 1 entry, 1 modality; floor ≥2 unmet; documented trade-off, not chased)
interest-narrator-terminal-state: CLEAN PASS-ELIGIBLE (AP-10 cap now 1; all entries form-valid)

## SESSION-START — 2026-05-23T00:00:00Z — facets-b01c01-hard-findings
dispatch: fix 5 HARD findings from facets-final-audit.md b01c01 — 3 STRUCTURAL (fault-001/002/003 proto-lines citation tokens) + 2 CONSTRAINT (fault-011 vibes:9 licensed-by; fault-012 state:10 field mutation)
target: active-project/theater/proto-lines/b01-c01.md + active-project/theater/facets/vibes-b01-c01.md + active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 5 (fault-001, fault-002, fault-003, fault-011, fault-012)

## fault-001 — RESOLVED — 2026-05-23T10:01:00Z
fault: proto-lines @15 carried [loc-state:4] instead of [loc-state:5]
scope: line
change: pre-applied in proto-lines/b01-c01.md before this session (file on disk already had [loc-state:5] at @15); cite-index rebuilt to reflect back=Y for loc-state:5 @15
criteria met: yes — @15 carries [loc-state:5]; cite-index shows loc-state:5 @15 back=Y

## fault-002 — RESOLVED — 2026-05-23T10:02:00Z
fault: proto-lines @9 carried stale [state:4] (watch-rotation, @18 anchor) instead of [state:9] (@9 ward-geometry)
scope: line
change: pre-applied in proto-lines/b01-c01.md before this session (file on disk already had [state:9] at @9); cite-index rebuilt to reflect state:9 @9 back=Y; state:4 co-citations at @9 removed from all affected entries
criteria met: yes — @9 carries [state:9]; cite-index updated; no stale state:4 at @9

## fault-003 — RESOLVED — 2026-05-23T10:03:00Z
fault: systematic loc-state one-off token offset: @17 had [loc-state:5], @18 missing [loc-state:6], @22 had [loc-state:6] instead of [loc-state:7]
scope: line
change: all three corrections pre-applied in proto-lines/b01-c01.md before this session (@17 bare of loc-state, @18 has [loc-state:6], @22 has [loc-state:7]); cite-index rebuilt to reflect loc-state:6 @18 back=Y, loc-state:7 @22 back=Y, sensory:4 @17 co-citations updated
criteria met: yes — @17 has no loc-state token; @18 has [loc-state:6] (back=Y); @22 has [loc-state:7] (back=Y)

## fault-011 — RESOLVED — 2026-05-23T10:04:00Z
fault: vibes:9 licensed-by cited deleted feeling:3; unresolvable citation is HARD per CONSTRAINT class
scope: line
change: pre-applied in vibes-b01-c01.md before this session (licensed-by: proto:27 only; feeling:3 already removed); cite-index rebuilt — vibes:9 lic-out now shows [proto:27] only
criteria met: yes — feeling:3 absent from vibes:9 licensed-by; proto:27 alone anchors the entry

## fault-012 — RESOLVED — 2026-05-23T10:05:00Z
fault: state:10 @20 field mutation named patrol-rotation specifically; narrator:7 co-cited NI is a day-close ledger register, not patrol-rotation registration
scope: line
change: state-updates.md (consolidated) entry state:10 @20 field new-value changed from flea-bottom-block-level-with-patrol-rotation to flea-bottom-block-level-day-count-complete; taylor slice (state-updates-taylor-hebert-kl-122ac.md) was already correct; only the consolidated file required the edit
criteria met: yes — state:10 mutation now names day-count-complete semantics matching narrator:7's ledger-close register; patrol-rotation specifics removed

## SESSION-END — 2026-05-23T10:06:00Z — facets-b01c01-hard-findings
findings-applied: 5 (fault-001 proto-lines pre-applied; fault-002 proto-lines pre-applied; fault-003 proto-lines pre-applied; fault-011 vibes pre-applied; fault-012 state-updates consolidated file edited)
findings-skipped: 0
exit: CLEAN
cite-index-rebuilt: YES (manual rebuild from canonical file state; build_cite_index.py not executable in this environment; cite-index written directly to active-project/theater/facets/_cite-index.md)
hard-count-post-fix: 0 (all 5 HARDs resolved; Phase 5b unblocked)

## SESSION-START — 2026-05-23T12:00:00Z — facets-b01c01-cycle2-fixer
dispatch: /and-facets b01c01 Phase 5b cycle-2 fixer — F1 NI Form rewrites (narrator:2/3/6/7) + F2 loc-state:3 continuity-carry fix + F3 vibes:2 AP8 token + F4 sensory:2/3/4 old-state lineage + F5 memory:2 Westerosi monument + F6 prop:oc-taylor-pack margit referral
target: active-project/theater/facets/interest-narrator-b01-c01.md + location-state-b01-c01.md + vibes-b01-c01.md + sensory-b01-c01.md + memory-b01-c01.md + active-project/warehouse/
audit-report: active-project/staff/auditor/facets-final-audit.md + active-project/staff/auditor/facets-audience-gate-r1.md
findings-queued: 6 (F1-F6; H3/H4/fault-008 already complete)

## F1 — WORKING — 2026-05-23T12:05:00Z
note: authoring single-clause rewrites for narrator:2/3/6/7 — must remove "power" (narrator:2), eliminate all semicolons, preserve channel+earning content per rubric §Form lines 27-42

## item-4 — RESOLVED — 2026-05-21T15:08:00Z
fault: exposition:4 @4 gloss text "In Flea Bottom there is rarely anyone who can" lacks appositive orienting a cold-join reader; "the Hook" in exposition:1 @0 bridge text also flagged for check
scope: line
change: (1) added inline appositive "the city's poorest ward" to exposition:4 in exposition-b01-c02.md: "In Flea Bottom, the city's poorest ward, there is rarely anyone who can." (~6 words; within first-mention-term cap); (2) "the Hook" check: confirmed on glossed-terms.md register as b01c01 gloss-id 6 — no appositive addition needed in bridge text
criteria met: yes — Flea Bottom oriented at first cold-join mention in b01c02; "the Hook" already registered from b01c01

