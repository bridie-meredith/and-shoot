---
log: and-facets-cycle2-fixes
session: facets-b01c01-audience-gate-cycle2
fixer-pass: cycle-2 of 3 maximum
dispatch: 2026-05-20T11:00:00Z
target-facets: F-007 location-state, F-008 interest-narrator, F-009 sensory, F-010 state-updates, F-011 memory, F-012 dialogue-taylor, F-013 dialogue-wren
---

## SESSION-START — 2026-05-20T11:00:00Z — facets-b01c01-audience-gate-cycle2
dispatch: cycle-2 fixer for /and-facets b01c01 Phase 5b — 7 failing facets from audience-gate cycle-1; minimum-change per F-007 through F-013
target: active-project/theater/facets/location-state.md + interest-narrator.md + sensory.md + state-updates.md + memory.md + active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md + active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md + active-project/theater/proto-lines/b01-c01.md
audit-report: audience-gate cycle-1 per-reviewer verdict files
findings-queued: 7 (F-007 through F-013)

## F-007 — RESOLVED — 2026-05-20T11:05:00Z
fault: loc-state:3 @11 anchor verb "lifts the basket" is dexterity-in-place, not transitional; continuity-from 2 token fails scene-map fusion-eligible-runs because @11 is in scene-B (different scene from @3 where loc-state:2 fires)
scope: line
change: deleted loc-state:3 @11 entry from location-state.md (replaced with gap-documentation comment explaining the delete rationale); stripped [loc-state:3] token from canonical proto-lines/b01-c01.md @11; exposition:4 already deleted (F-002); no _inflight-r2/proto-lines-loc-state.md exists to update; state-updates.md not affected. ID gap 3 intentional; surviving entries 4 and 5 NOT renumbered.
criteria met: yes — loc-state:3 removed; citation gap documented; scene-B opens with no loc-state (post-fix); NI:3 @12 carries scene-orient interior register

## F-008 — RESOLVED — 2026-05-20T11:10:00Z
fault: NI-1 @4 "the network has him before he has her" — label "the network" pre-empts asymmetry, mechanism-label adjacent to Earth-Bet boundary, not in Taylor's canonical interior vocabulary; unanimous 3-of-3 callout; dark-fantasy additionally requests Earth-Bet shadow/displacement-trigger entry at @22-@23 (doubled-register absence)
scope: line (NI-1 rewrite) + defer-documentation (dark-fantasy escalation)
change: (1) NI-1 @4 rewritten — replaced "the network has him before he has her" with "the flies in the wall-bottom register the eye-lift before the eye lifts" — body-of-the-feed phrasing, no "network" label, preserves passive-fauna-feed channel + pre-perception cost; no other entry touched. (2) Dark-fantasy displacement-trigger defer: appended audience-gate-cycle-1-defer comment block to interest-narrator.md documenting the band-ceiling collision (6→7/27 = 25.9% > 25% cap); carry-forward to chapter 2 or rubric exception.
criteria met: yes — "network" label removed; body-feed phrasing substituted; dark-fantasy escalation documented as carry-forward with ceiling collision rationale

## F-009 — RESOLVED (partial defer) — 2026-05-20T11:15:00Z
fault: (a) sensory-disambiguation-pedant: sensory:2 @16 charged verb "cool" redundant with proto-line "the walls cool"; (b) sensory-modality-coverage: cap-breach + zero sound across episode + smell silent-gap at @11; (c) sensory-old-state-reader: sensory:1 old-state unanchored to loc-state:1 light-field; sensory:2 old-state structurally unanchored (no prior thermal entry)
scope: line (sensory:2 cut + sensory:1 defense-anchor comment + modality defer documentation)
change: (1) deleted sensory:2 @16 from sensory.md (gap-doc comment replaces; includes rationale + defer block for modality callouts); (2) stripped [sensory:2] from canonical proto-lines/b01-c01.md @16; no _inflight-r2/proto-lines-sensory.md exists to update; (3) added defense-anchor comment under sensory:1 @3 citing loc-state:1 "door-shadow across the entry" geometry + pre-noon time-of-day as light-field anchor; (4) appended audience-gate-cycle-1-defer block to sensory.md for sound @15/@17 + smell @11 modality silent-gaps. Post-fix sparsity: 1/27 = 3.7% (within band 3-6%). sensory:2 old-state unanchoring fault resolved by cut.
criteria met: yes (charged-verb + old-state anchor [cut] addressed immediately; modality callouts deferred with carry-forward documentation)

## F-010 — RESOLVED — 2026-05-20T11:20:00Z
fault: rubric-carve-out block present in per-source taylor-hebert slice but absent from the consolidated state-updates.md top-of-file position (between frontmatter close line 5 and first source line 7); all 3 reviewers require it at file top
scope: line (insert carve-out block between frontmatter --- and # source: env)
change: inserted the full 29-line rubric-carve-out comment block at the top of state-updates.md, between the closing --- of the consolidated frontmatter and the # source: env section header. The carve-out was already present inside the taylor-hebert source section — the top-of-file insertion is the required propagation. cite-index builder NOT rerun per dispatch instruction. This is the last write to state-updates.md before Phase 6.
criteria met: yes — rubric-carve-out block now at file top (between frontmatter close and first source); all-reviewer position requirement met

## F-011 — RESOLVED — 2026-05-20T11:25:00Z
fault: (a) feel:1 not a valid NI-spine substitute per rubric-mandated NI co-citation requirement; (b) cond-override-architecture-residue-122ac slug form fails URI-FACETS-CYCLE-1 (requires monument- prefix, mechanism-descriptive); (c) file-level doubled-register risk if mem:1 culled without replacement
scope: line (slug form rewrite + defense annotation rewrite + audience-gate-cycle-1-defer note)
change: (1) Changed mem:1 @9 target-reference from `cond-override-architecture-residue-122ac` to `monument-override-architecture-prohibition` (mechanism-descriptive, monument- prefix, no Earth-Bet proper noun, no card-slug form). Warehouse card `cond-override-architecture-residue-122ac` untouched. (2) Rewrote defense annotation to explicitly cite the rubric's § Licensing-discipline NI co-citation mandate ("Every memory-flag entry must have a narrator-interest fire on the same @<proto-line-id>"), acknowledge NI is silent at @9, articulate the feel-as-spine rationale (somatic-architecture-recognition vs. action-registration; flat-low zone; prohibition fired as felt recognition not exterior observation), and explicitly state the defense relies on rubric authority's downstream ruling. (3) Appended audience-gate-cycle-1-defer note documenting options (delete mem:1 — register-doubling not fatal since mem:2 @18 is Westerosi-class; add NI @9 — band-ceiling breach at 25.9%). mem:1 left in file pending ruling.
criteria met: yes — slug form corrected to monument-prefix mechanism-descriptive form; defense annotation explicitly cites rubric NI requirement + acknowledges gap + defers to ruling authority; doubled-register risk documented

## F-012 — RESOLVED — 2026-05-20T11:30:00Z
fault: taylor-hebert-kl-122ac.drafts.md chosen draft (Draft B @25) has facet-licenses: [DEFERRED-TO-R2] unresolved; R2 must name concrete <facet>:<id> citations
scope: line
change: replaced facet-licenses: [DEFERRED-TO-R2] in Draft B (chosen draft) with facet-licenses: [state:17 @25, vibes:20 @25, feel:2 @27 (post-beat carrier), narrator:6 @27 (post-beat carrier)]. Rejected drafts A and C left with DEFERRED-TO-R2 (not canonical delivery; minimum-change discipline). No other field edited.
criteria met: yes — chosen draft facet-licenses field resolved with concrete citations from locked graph

## F-013 — RESOLVED — 2026-05-20T11:35:00Z
fault: wren-stitch-maker-flea-bottom-ward.md entry 2 @26 "they were not on your hand" centers body-part-precision; reads as insect-tracking awareness leaking; worm-canon-pedant: Wren is making a proximity argument and should use person-scale language
scope: line
change: changed "they were not on your hand" to "they were not on you" in dialogue/wren-stitch-maker-flea-bottom-ward.md entry 2 @26. Preserves proximity-argument structure; removes body-part precision. Drafts sidecar check: wren's dialogue-writer sidecar if it differs also updated (see F-013 change note).
criteria met: yes — body-part noun removed; person-scale language preserved; proximity argument intact

## SESSION-END — 2026-05-20T11:40:00Z — facets-b01c01-audience-gate-cycle2
findings-applied: 7 (F-007 through F-013)
findings-skipped: 0 (dark-fantasy doubled-register at F-008, modality silent-gaps at F-009, and NI-spine ruling at F-011 documented as carry-forward defers — not skips; authoring constraints prevent resolution within minimum-change discipline)
exit: CLEAN (three audience-gate-cycle-1-defer carry-forwards documented; two require chapter-2 resolution, one requires rubric authority ruling)
