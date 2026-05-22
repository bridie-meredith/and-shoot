---
report: facets-cycle2-remediation
episode: b01c01
cycle: 2
date: 2026-05-19
fixer-session: facets-b01c01-cycle2-remediation
driven-by: active-project/staff/auditor/facets-audience-gate-r1.md
status: COMPLETE (one pending action: margit referral for mem:2 monument card)
---

# Cycle-2 Remediation Report — b01c01

## Summary

9 facet failures from audience-gate cycle-1 were processed. All 9 were resolved or substantially addressed in-session. One pending action (margit referral for mem:2 monument card) is flagged for the orchestrator to route before cycle-2 Phase 5 re-fire.

---

## Per-facet remediation

### 1. location-state

**Entries touched:** loc-state:3 (cut), loc-state:4 (cut). Surviving entries renumbered (old 5→3, old 6→4).

**loc-state:3 @11 — CUT.**
- Reason: anchor verb "threads the needle" is dexterity-stillness per rubric URI-FACETS-CYCLE-1 REJECT clause (promoted from cycle-1 audience attack). Dexterity verbs do not license a loc-state fire unless first-beat-in-new-location or carrying a `continuity-from` token. @9 already opened this location-and-moment (scene-B, corner-room-interior). Necessity-axis fails. 2-of-3 dissent (dark-fantasy + worm-canon-pedant).

**loc-state:4 @13 — CUT.**
- Reason: Anti-pattern 3 (persistence-as-state). "The stone of the far wall has begun releasing its morning-caught warmth" describes thermal persistence of a static condition, not a state-change. No new entrant, no condition resolved, no active condition activated. 1-of-3 dissent (dark-fantasy).
- Dependency declared: sensory thermal-gap at @13 depended on this entry naming a thermal event. With loc-state:4 cut, no loc-state thermal event exists at @13 — the gap collapses. Sensory ADD at @13 is not required.

**Justification for both cuts vs. defend:** The default in the dispatch was cut. The rubric's REJECT signatures are unambiguous on both entries. No floor-defense argument was available (strip test passes cleanly on both; neither entry points at a specific perceptible thing the anchor verb requires).

---

### 2. interest-narrator

**Entries touched:** narrator:2 rewritten, narrator:4 rewritten, narrator:5a added (Westerosi-monument), narrator:6 kept.

**AP-10 template cap (≤1 "X is what Y" per file):**
- narrator:2 @8 rewritten: "the flagstones put themselves two meters into her before the discipline catches; the knowledge goes to ground at the seam where the rule says stop" — shows the holding-cost (the map stops at the seam) rather than defining the rule; drops "X is what Y" chassis; drops "today" hedge.
- narrator:4 @15 rewritten: "the Watch column moves at the road-arc and she prices the column from the doorway, not from the column's tally" — one-number register without the inverted-predicate chassis; drops "not the patrol's count of her" explicit-contrast clause.
- narrator:6 @24 KEPT as sole "X is what Y" instance: "face, not node, is what she holds" — structurally load-bearing (node→face suppression is the chapter's hinge function); worm-canon-pedant accepted; content earns the template.

**Westerosi-monument fire ADD:**
- narrator:5a @22 added: "the child is the kind the neighborhood produces and the neighborhood will not keep, and she has read enough records to know the record this one will not appear in."
- Register: Westerosi-monument foreknowledge-clamp; the Watch-register / child-ward who will not appear in the Dance-era survival records; construction holds the foreknowledge without naming the event or any proper nouns; displaced-child trigger (the child-harm adjacency trigger the rubric names as licensed at Wren-adjacency); in-world framing ("read enough records" = Taylor's accumulated social-physics reading in first days); no Earth-Bet proper noun.
- Doubled-register requirement met: Earth-Bet displacement remains (narrator:7 @23 via mem:2 monument rhyme); Westerosi-monument clamp now present (narrator:5a @22).

**Declined to act on:** narrator:3 @12 tail-clause ("the reading is the whole of what she will take") — dark-fantasy flagged this but was 1-of-3 dissent; minimum-change principle does not require acting on 1-of-3 dissent; flagged as watch-item if narrator:3 fails at cycle-2 gate.

---

### 3. sensory

**Dependency resolved:** loc-state:4 @13 cut → thermal silent-gap at @13 no longer exists → sensory ADD at @13 not required. Comment line added to sensory.md documenting the collapse.

**Old-state anchoring repair:**
- sensory:1 @1 old-state `hook-alley-ambient` (smell): no prior loc-state lineage. Fixed by adding sensory-baseline studio notes to location-state.md adjacent to entry 1: smell baseline = tallow-smoke-and-rendered-fat ambient (Hook-alley exterior, morning; sourced from loc-flea-bottom card §Sensory palette + oc-corner-room description). sensory:1 updated with `old-state-source:` token referencing the documented baseline.
- sensory:2 @9 old-state `corner-room-interior-quiet` (sound): no prior loc-state lineage. Fixed by second studio note: sound baseline = corner-room-interior-quiet (before door-open; interior of the corner room before working-hour traffic builds). sensory:2 updated with `old-state-source:` token.
- Approach: documented the baselines in the loc-state file as studio-note comment lines rather than as new loc-state entries (which would have required full three-axis justification and could introduce new frugality violations). The sensory entries reference the documented studio notes.

---

### 4. state-updates

**Entries touched:** 10 (clarified), 11 (flagged for cut), 12 (new-value revised), 13 (new-value revised), 15 (citation added), 17 (cut), 19 (arrival-timing comment added).

**Entry 10 @8 — clarification comment added:**
- `active-holding` ambiguity resolved: "active-holding = management of attentional allocation / deployment decision ONLY — passive insect-sense data continues to arrive (Taylor cannot turn off reception); what is HELD is the act of consciously processing that data into tactical knowledge or directing insect movement." Prevents downstream authors from reading the field as power-suppression (not canon).
- cite-index back=N documented as interior-only state mutation (correct behavior).

**Entry 11 @12 — flagged and effectively cut:**
- cape-fic-reader correct: discipline-hold at @8 with no released-from-hold transition; passive data arrives but should not enter canonical knowledge-state under the hold. Entry flagged with comment marking it for removal; knowledge.hook-block-density-map deferred to post-hold or subsequent chapter.

**Entry 12 @15 — new-value revised:**
- `patrol-pattern-read-passively` → `patrol-first-sighting-logged`. One Watch pass is a single data point, not an established cadence. `patrol-pattern-read` implies recurrence and temporal pattern — not supportable from one sighting.

**Entry 13 @18 — new-value revised:**
- `recurring-needle-handler-coll-block` → `needle-handler-at-coll-block-day-one-complete`. "Recurring" requires ≥2 sessions and a return-expected signal from Coll. Bones show nets set-down at @18 with no Coll utterance inviting return. First session complete; recurrence deferred to subsequent chapter.

**Entry 15 @24 — citation added:**
- `auto-initiating` canon-departure now explicitly marked with `cond-khepri-residue-122ac` citation. The field-extension comment specifies: this is a post-Khepri residue effect (shard architecture altered by Gold Morning scale; pattern-read fires before Taylor's conscious trigger in high-salience contexts); AU departure from baseline Worm canon; marked, not implicit.

**Entry 17 @26 — cut:**
- `ward-layer-deeper` is a direction, not a state value. No bones-supported acquisition at @26 (Wren's departure direction provides no ward-layer signal). Entry fires against its own prohibition-catch at @24. Deferred to subsequent chapter.

**Entry 19 @22 (Wren) — arrival-timing comment added (dialogue-wren state dispatch):**
- Added arrival-timing specification: Wren's arrival established by state:18 @20 (location change); she was NOT present during scene-B (@8-@18); she arrived @20, approached @21, spoke @22; ≤2 bones on-street before speaking; insect-atmosphere is environment she walks into, not duration she has accumulated. Resolves dark-fantasy + worm-canon-pedant specificity gap; "pre-anomaly opener" premise is now state-supported.

---

### 5. memory

**Entries touched:** mem:1 relocated, mem:3 added (Westerosi-monument), mem:2 margit-referral noted.

**mem:1 relocated @15 → @16:**
- Scene-map confirms @16 is quiet-beat eligible (scene-B flat-low, no peak-bones; @16 is post-Watch, nets-work resuming). The patrol-echo arrives in the working-pause after the Watch clears the arc — correct slot for interior-reaching-backward. @15 has 8 co-fires (institutional-pressure peak); the quiet-beat instrument does not belong there.

**mem:3 added @17 (Westerosi-monument):**
- "the column's gold marks the Watch-register as a formation that will exist in the records of this city for forty years and then not, and she has read the interval between the last formation report and the silence"
- Target: `(westeros: gold-cloak-watch-register; conquest-charter-institutional-record; Dance-era administrative-collapse displacement)`
- Monument class: institutional-administrative-record-that-terminates. The Watch-register is the Conquest-charter-adjacent object; Taylor's foreknowledge of the Dance frames the terminal-entry interval. No Earth-Bet proper noun. Westerosi-monument clamp fires in the aftermath zone (@17, flat-low, post-Watch).
- Doubled-register requirement met: both Earth-Bet displacement (mem:1 @16, mem:2 @23) and Westerosi-monument clamp (mem:3 @17).

**mem:2 @23 — margit referral PENDING:**
- Target-reference ships on free-text gloss + `world-build:override-architecture-residue-122ac` stand-in. Rubric requires the target-reference to resolve to a monument card via margit referral.
- **Pending action (for orchestrator to route):** Dispatch margit with the following:
  - Card class: condition (monument-class condition)
  - Candidate slug: `monument-override-architecture-prohibition-122ac`
  - Monument family: Khepri-period mass-control apparatus; the scale-coordinating-override capability and the vow prohibiting its deployment; what Taylor came here to refuse
  - References: `cond-override-architecture-residue-122ac`, `cond-no-parahuman-infrastructure`
  - If margit creates the card: update mem:2's target-reference from `world-build:override-architecture-residue-122ac` to the new monument card slug.
  - If margit declines (card already exists under a different slug or the class is not supportable): update target-reference to the nearest existing card (`cond-override-architecture-residue-122ac`) and note the unresolvable monument-card gap in the cycle-2 report.
- In the interim: target-reference updated in memory.md to `cond-override-architecture-residue-122ac` as the nearest existing card.

---

### 6. feeling

**Entry touched:** feel:1 @23 second clause cut.

- Original: "her hand stills at her side and the turn comes one beat late"
- Cut: "and the turn comes one beat late" (exits body-register; subject "the turn" is temporal-abstraction; latency observation, not somatic action)
- Retained: "her hand stills at her side | expressed: no"
- Form-discipline rule (URI-FACETS-CYCLE-1): one clause, one body action; compound with subject-shift into abstraction-noun is REJECT. Dark-fantasy + worm-canon-pedant 2-of-3 dissent.
- The hand-stilling alone carries the prohibition-catch at the chapter hinge. The latency the second clause was reaching for is already covered by narrator:7 @23 ("the turn comes a beat late because the read has already begun and the rule's catch is the slower mechanism") — feeling does not need to duplicate the NI's latency-naming.

---

### 7. exposition

**Entry added:** exposition:5 @20 — first-mention-place for "the Hook."

- Gloss: "the Hook — one of Flea Bottom's ward-organized precincts; children there work light tasks in exchange for two meals and a sleeping place." (21 words; ≤30 word cap met)
- Scope: first-mention-place. Renders-as: inline-appositive (cheapest).
- Sources: cond-kl-social-physics-122ac, wren-stitch-maker-flea-bottom-ward.description
- Licensed-by: cape-fic-reader (cape-fic-doesnt-know-flea-bottom-ward-labor-exchange-precincts-or-the-hook-as-a-specific-organizational-unit), worm-canon-pedant (worm-canon-doesnt-know-westeros-flea-bottom-ward-labor-arrangements), dark-fantasy-reader (dark-fantasy-needs-the-hook-as-institutional-frame-for-wren-vulnerability)
- Per-anchor cap: @20 now has first-mention-character (exposition:4) + first-mention-place (exposition:5) — allowed pair per rubric.
- Cross-episode register updated with the-hook entry.
- Embedded-noun-gloss-completeness HARD (URI-FACETS-CYCLE-1) resolved.

---

### 8. dialogue-coll

**Two items:**

**(a) Facet-license citation-completeness — RESOLVED:**
- Sidecar coll-net-mender-flea-bottom.drafts.md updated: `facet-licenses` field resolved from locked graph.
- Resolved citations:
  - `state-coll:6 @3` — Coll's block_baseline_new_faces mutation fires at @3 (the verbal offer IS the non-interpretive registration of a new presence)
  - `state-taylor:8 @3` — Taylor's knowledge.coll-as-vouching-vector mutation fires at @3 as direct consequence of the dialogue
- Noted: expected `narrator:<post-payment-arrival>` slot did not materialize (no NI fire at @3 in locked file; nearest entries @1 and @8); two state citations constitute the complete facet-license record for this entry.

**(b) "Needle's been waiting" anticipatory-object ascription — DEFENDED:**
- Cape-fic-reader Stage 2 seam: "Needle's been waiting" attributes anticipatory interiority to the tool ("waiting" implies purposive orientation); inconsistent with Coll's non-interpretive register.
- Defense entered in sidecar: "Needle's been waiting" functions as trade-idiom persistence-state (the needle is idle/available/has-been-here), not genuine purposive attribution. Compare structural equivalents: "The seat's been empty" — no anticipatory-object ascription. The §Hard Fences §2 ban is on interpretive moves about people or situations, not on idiomatic persistence-state language about objects. Draft A held.
- If the defense fails at cycle-2 gate, the line becomes a revise target for cycle-3 (e.g., "Needle's idle. Sit, then.").

---

### 9. dialogue-wren

**Two items:**

**(a) feel-wren citation corrected — RESOLVED:**
- Sidecar wren-stitch-maker-flea-bottom-ward.drafts.md: `feel-wren-stitch-maker-flea-bottom-ward:@22` corrected to `feel-wren-stitch-maker-flea-bottom-ward:@21`.
- feel:2 anchors at @21 (Wren approaches Taylor) in the locked feeling file. The @22 reference was a typo. No ADD of a new feeling entry at @22 required: the @21 approach-tell ("her eyes track Taylor's hands before her head finishes turning toward her") is the correct license for the "observation-before-action" structural claim in the sidecar. The eyes-on-the-knot-before-the-mouth-opens read derives from the approach posture, which fires at @21.

**(b) state-wren:@22 specificity — RESOLVED:**
- Handled above under state-updates entry 19.

---

## Dependency conflicts encountered and resolutions

**Sensory @13 ADD vs. loc-state:4 @13 cut:**
- Gap: sensory thermal-gap at @13 existed because loc-state:4 named a thermal event at @13. Cutting loc-state:4 collapses the thermal event from the facet graph.
- Resolution: cut loc-state:4 (default per dispatch). Sensory ADD at @13 not required. Comment in both files documents the collapse.

**mem:1 relocation vs. scene-map @15-@17 zone classification:**
- Checked scene-map before relocating: scene-B @11-@20, rhythm-shape: flat-low, peak-bones: none. @16 and @17 are flat-low eligible. @15 has 8 co-fires but scene-map does not classify it as a peak-bones entry (the scene-map is a summary classification; @15 is dense but the scene-map shows no peak-bones for scene-B). Relocation to @16 is correct: post-Watch quiet slot, flat-low zone, first available bone after the institutional event.

---

## Items declined to remediate and why

**narrator:3 @12 tail-clause:** dark-fantasy flagged "the reading is the whole of what she will take" as an accounting-close. 1-of-3 dissent only (cape-fic accepted, worm-canon-pedant accepted). Minimum-change principle does not require acting on 1-of-3 dissent at cycle-2. If narrator:3 fails at cycle-2 gate, becomes a cycle-3 item.

**"Needle's been waiting" revision:** Cape-fic-reader only; dark-fantasy + worm-canon-pedant accepted. Defense entered. Not revised at cycle-2 per minimum-change principle (1-of-3 dissent; defense available). Cycle-3 target if defense rejected.

---

## Pending actions for orchestrator

1. **Margit referral — mem:2 monument card:** Route margit to create or locate `monument-override-architecture-prohibition-122ac` (or nearest existing card). If created, update mem:2's target-reference in `active-project/theater/facets/memory.md`. If declined, document gap and update target-reference to `cond-override-architecture-residue-122ac` (nearest existing). This action must complete before cycle-2 Phase 5 re-fire for memory to pass the monument-card requirement.

2. **Do NOT advance phase/status fields in showrunner memory** — orchestrator's job after cycle-2 Phase 5 + 5b complete.

---

## Files modified in this session

- `active-project/theater/facets/location-state.md` — entries 3 and 4 cut; sensory-baseline studio notes added; entry IDs renumbered
- `active-project/theater/facets/feeling.md` — feel:1 @23 second clause cut
- `active-project/theater/facets/interest-narrator.md` — narrator:2 and narrator:4 rewritten; narrator:5a added
- `active-project/theater/facets/sensory.md` — old-state-source tokens added to entries 1 and 2; thermal-gap collapse note added
- `active-project/theater/facets/state-updates.md` — entries 10/12/13/15/19 edited; entries 11 and 17 effectively cut via comment; entry 19 arrival-timing note added
- `active-project/theater/facets/memory.md` — mem:1 relocated @15→@16; mem:3 added @17; mem:2 margit-referral note added
- `active-project/theater/facets/exposition-b01-c01.md` — exposition:5 added @20 (the-hook first-mention-place); cross-episode register updated
- `active-project/staff/dialogue-writer/coll-net-mender-flea-bottom.drafts.md` — facet-licenses field resolved; defense note added for "Needle's been waiting"
- `active-project/staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md` — feel-wren citation corrected @22→@21
