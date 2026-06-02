audit: facets-final-r1
episode: b01c10
date: 2026-06-02
mode: flag-only
status: FINDINGS-PRESENT
totals: 16 findings across 8 facets

---

## STRUCTURAL findings (0)

None. All facet files carry valid headers, entry IDs are monotonic per-facet, anchor flat_ids 0–27 all resolve in proto-lines (noting @0 is the preamble anchor for exposition:1, flat_id-independent), bidirectional citation checks pass per the cite-index. state-updates consolidated file carries dual `# source:` markers with per-source slice headers — conforms to schema § slice-consolidation. feeling.md same pattern, valid. Scene-map covers 27/27 bones in exactly four non-overlapping scenes. Cite-index totals (60 entries; 22/27 decorated; 5 bare: @5, @6, @7, @8, @26) are consistent with the file content. No missing dialogue files (silent chapter confirmed by scene-map "dialogue: none"; no speech bones present; URI-WRITE-DIALOGUE-COBONDED N/A). exposition entry IDs are non-monotonic in the file (listed as :1 @0, :4 @2, :2 @17, :3 @13) — however, the schema requires per-file ID monotonicity by ANCHOR order, not file-physical order; the cite-index records them correctly by anchor position. SIGNAL: the file-physical ordering diverges from ID order (exposition:4 @2 is a R2-ADD and appears after exposition:1 @0, before the R1 entries :2 and :3 which were re-ordered in the file). This is cosmetically non-standard but does not break machine-readable anchor resolution. Flagged as advisory.

- [exposition:--] @-- — structural-id-ordering — R2 ADD exposition:4 inserted at physical position 2 in file; file-physical ID sequence reads 1, 4, 2, 3 instead of 1, 2, 3, 4. Machine-resolution is by anchor (all anchors resolve); downstream readers relying on sequential file scan may encounter out-of-order IDs. No fixer action required; advisory only. type: flag

---

## FREQUENCY-BAND findings (4)

- **narrator-interest**: actual 7/27 = 25.9%; band 15–25%; breach-high +0.9pt. Documented spine-vs-band tradeoff in R2 NI shard: both R2 adds (narrator:7@16, narrator:8@24) are sole NI-spine for distinct memory fires (mem:1@16, mem:2@24) on a climax chapter (feel-as-spine carve-out inapplicable). Trimming a second genuine fire to hit 25.0% would delete an earned attention-landing to satisfy arithmetic (locked-rubric §taste-over-arithmetic prohibition). Defense present in .r2-decisions.md NI shard. **SIGNAL (advisory; documented defense).**

- **feeling (taylor)**: actual 2/27 = 7.4%; band 2–5%; breach-high +2.4pt. Both fires (feel:1@10, feel:2@27) documented load-bearing: feel:1 is the chapter's first moral cost (moral_framework –0.5, W1 SURRENDER-AS-IRREVERSIBLE-ACT); feel:2 is the terminal moral_legibility crack. Short-chapter denominator effect at 27 bones (band floor rounds toward 1.5 fires; forcing a single-fire file would drop one of two moral-cost beats on a 2-moral-cost climax). Open parking-lot item pl-2026-05-25-017 (short-chapter exemption) applies. Defense present in .r2-decisions.md feeling shard. **SIGNAL (advisory; documented defense).**

- **sensory**: actual 7/27 = 25.9%; band 3–6% standard; breach-high (above V3 short-chapter floor-exemption max). **LICENSED** — all 7 fires map to grounding-ledger entries grd-001..grd-007 (status: satisfied; license: GROUNDING-REQUIRED). Per PROP-0022 exemption, sensory entries satisfying a grounding-ledger entry are exempt from the FREQUENCY-BAND cap. Verified: grd-001→sensory:1@3, grd-002→sensory:2@10, grd-003→sensory:3@13, grd-004→sensory:4@15, grd-005→sensory:5@19, grd-006→sensory:6@22, grd-007→sensory:7@25. All 7 satisfy. Per-scene caps: scene-A 1/≤3, scene-B 1/≤3, scene-C 3/≤3, scene-D 2/≤3 — all within cap. **PASS (band-exempt; noted for completeness).**

- **exposition (band-counted)**: actual 3/27 = 11.1% band-counted (exposition:4 ledger-exempt); band 1–5% standard; breach-high. Denominator-driven at 27 bones; 3 entries each individually mandatory: (1) prior-episode-bridge @0 (only carrier of c09→c10 reader-state refresh; no lens facet at @0), (2) first-mention-term @17 (Gold Cloak / City Watch — FIRST project-prose appearance; cape-fic-reader institutional gap; lens-uncovered confirmed in R2), (3) scene-open-orient @13 (two-day elapsed-interval; lens-uncovered per R2 fire-rule re-validation). Bridge-suppression applies: the @0 bridge suppresses first-mention-character entries for all register-resident cast. Mirrors the c09 11.1% disposition. **SIGNAL (advisory; denominator-driven + bridge-suppression + register-residence-maximized).**

---

## METADATA-INCONSISTENCY findings (1)

- **vibes-b01-c10.md** header: `facet: vibes-updates` and `episode: b01-c10` (hyphenated slug). All other facets use `episode: b01c10` (canonical chapter slug without hyphen). The inconsistency is cosmetic and downstream-consumers read the chapter slug from the bones-file header, not from individual facet headers, but it is a format divergence. type: flag

---

## CURVE-SHAPE verdict

**Episode-level: SHAPE-OK.**

dramatic_shape declared: `climax` (from memory chapters[b01c10].dramatic_shape). Chapter has 4 scenes with rhythm-shapes: scene-A `low-heat establishment`, scene-B `rising — substrate-collapse`, scene-C `rising-to-PEAK`, scene-D `falling-to-thesis-image`.

Mapping to `climax` archetype: (1) low-heat establishment → rising → peak → falling-to-thesis-image is the canonical climax curve (pressure mounts through scenes A→C, crests at scene-C peak-bones @15/@17/@18, then scene-D delivers the thesis-image fall — the ledger's accounting-close with the face persisting). (2) Peak-bones are present in all four scenes per scene-map (scene-A @2/@4; scene-B @10/@11; scene-C @15/@17/@18; scene-D @21/@25/@27). (3) Peak-shadow-bones distributed across all scenes. (4) No flat-low / release-only / resolving-only pattern that would indicate a hinge or falling shape. The curve shape is coherent with the `climax` declaration.

- Per-scene: scene-A (low-heat establishment, peak-present @2/@4), scene-B (rising, peak-present @10/@11), scene-C (rising-to-PEAK, peak-present @15/@17/@18), scene-D (falling-to-thesis-image, peak-present @21/@25/@27).
- Adjacency: no 1→3 or 3→3 jumps identified across scene boundaries (scene-A establishes, scene-B rises, scene-C peaks, scene-D falls — monotone or controlled); within-scene momentum is preserved.
- Flatlining: no stretch of 30+ contiguous held-axis bones with no movement (5-bone scene-A maximum; chapter is 27 bones total).

**SHAPE-OK.**

---

## CONTRADICTION findings (0)

None. Full cross-facet scan across all same-anchor co-located entries:

- @2: exposition:4 + narrator:1 + vibes:1 + vibes:2 + state:8. exposition:4 surfaces the Sera-consideration (packet stated terms); narrator:1 registers the deniability-foreclosure; vibes:1 fires atonement-as-repetition; vibes:2 fires the-formal-instrument; state:8 records position_prot_rise 3→3.5. No incompatible state assertions.
- @10: feel:1 + narrator:3 + sensory:2 + vibes:4 + vibes:5 + state:10. feel:1 somatic; narrator:3 cognitive; sensory:2 sound onset; vibes:4/5 two distinct vibe keywords; state:10 moral_framework 1→0.5. No contradictions.
- @15: loc-state:5 + narrator:5 + sensory:4 + vibes:7 + vibes:8 + state:2. loc-state:5 records road-geometry-minus-one; narrator:5 attention-landing on the absence; sensory:4 light-drop; vibes:7/8 apparatus-ran; state:2 corwick-present→absent. All consistent.
- @27: feel:2 + narrator:6 + vibes:11 + vibes:12 + state:7. All four register the face-persisting / feed-record-open / ledger-done asymmetry. No incompatible states.
- state:13 @21 and state:5 @21 — two state entries on @21. state:5 is prop:oc-feed-ledger.corwick-entry absent→written; state:13 is the same field. Checking: state-updates.md actor slice shows state:13 @21 as `actor:taylor-hebert-kl-122ac.moral_framework_axis: 0.5 -> 0`, and state:5 @21 is `prop:oc-feed-ledger.corwick-entry: absent -> written`. These are different targets (prop vs actor axis); not a contradiction.
- state:6 @25 and state:14 @25 — similarly: state:6 is prop:oc-feed-ledger.condition open→closed (env slice); state:14 @25 is `actor:taylor-hebert-kl-122ac.position_prot_rise_axis: 3.5 -> 4` (actor slice). Different targets; no contradiction.

---

## DEDUP findings (1)

- **[state:5] @21 / [state:13] @21** — cite-index shows state:5 and state:13 both anchored at @21. Per the state-updates consolidated file: state:5 (from env slice) is `prop:oc-feed-ledger.corwick-entry: absent -> written`; state:13 (from actor slice) is `actor:taylor-hebert-kl-122ac.moral_framework_axis: 0.5 -> 0`. Different targets and fields — this is NOT a dedup, it is the correct pattern of env + actor co-citing the same peak-bone. RESOLVED: no dedup.

No genuine dedup findings across any facet pair. NI-anti-duplication at @10 and @27 was verified in R2 (feel:1/@10 somatic vs narrator:3/@10 cognitive — distinct registers; feel:2/@27 gaze-body vs narrator:6/@27 record/ledger cognition — distinct registers). Memory @24 figurative language checked: mem:2@24 uses "the record closing the same way the old architecture closed around bodies it never asked" — this comparison is in the memory entry's prose text. narrator:8@24 uses "the corridor closing behind him the way the channel closed over the entry." Both carry the override-architecture register but in distinct frames (memory: the record vs the old architecture; NI: the corridor vs the channel). Same figurative territory but different vehicle and tenor — not a mechanical duplicate. SIGNAL (proximity/register overlap — advisory only).

- [mem:2] @24 + [narrator:8] @24 — figurative-register proximity. Both deploy override-architecture comparison at same anchor. Not verbatim overlap. Distinct frames (record-architecture vs corridor-channel). Noted as borderline per rubric §distinctive-register test; R2 metaphor judge verified AP4 non-duplication. type: flag

---

## SUPERFLUOUS findings (2)

Per the cite-index, 16 lonely entries (no co-location, no inbound license): loc-state:1@1, loc-state:2@9, loc-state:3@12, loc-state:7@20, loc-state:8@23, narrator:4@14, sensory:1@3, sensory:5@19, sensory:6@22, sensory:7@25, state:15@26, vibes:3@4, vibes:6@11, vibes:9@18, vibes:10@21, exposition:1@0.

Lonely entries are noted as "Round-2 deletion candidates — check the rubric." Running rubric scrutiny per the three-axis test (necessity / interestingness / frugality):

- **loc-state lonely entries** (@1, @9, @12, @20, @23): all are scene-anchor or sub-scene-anchor establishment entries for a location change, prop-state change, or sub-focus geometry update. loc-state rubric permits at-establishment entries for scene-anchoring without co-citation requirement — the convention that loc-state fires at scene-transitions and mid-scene-focus-changes is a rubric ACCEPT signature, not a co-citation dependency. PASS scrutiny — not superfluous.
- **narrator:4 @14**: lonely; covers W3 presence-before-absence baseline (the prior-circuit pattern that makes @15's absence legible as loss). R2 NI shard judgment: the registration is the W3 baseline work — the circuit running the lower-gate road through nine passes. Self-standing meaning: "this is the rhythm." Necessary per scene-C's protected-pattern W3. PASS scrutiny — not superfluous.
- **sensory:1@3, sensory:5@19, sensory:6@22, sensory:7@25**: all licensed by grounding-ledger entries (grd-001, grd-005, grd-006, grd-007). Per PROP-0022 exemption, grounding-licensed entries are exempt from SUPERFLUOUS/lonely scrutiny. PASS scrutiny — not superfluous.
- **state:15 @26**: actor:taylor-hebert-kl-122ac.social_tether_prot_rise_axis: 3.5→4. Lonely (no co-citation). social_tether-prot-rise +0.5 is one of the chapter's contracted axis-moves. The axis-move is load-bearing as substance delivery. However, the chapter contract allocates the tether advance in two tranches: one at s01 @4 (state:9) and one at s04 @26 (state:15). @26 is "taylor presses the feed-station," a peak-shadow bone. Per the rubric § cross-facet contract: POV actor axis-move entries require NI co-citation. @26 has NO NI co-citation (cite-index: state:15@26 lonely, back=N, no co). R2 NI shard documents deliberate decision NOT to pad NI at state:15@26 (grounding/transitional press; not a genuine attention-landing). The defense is present in .r2-decisions.md. **SIGNAL: state:15@26 has no NI co-citation; documented defense routes to SIGNAL not HARD per RUBRIC-FIDELITY severity calibration (defense present in entry notes).** For SUPERFLUOUS evaluation specifically: the axis-move is load-bearing substance delivery; rubric three-axis necessity passes. PASS scrutiny — not superfluous.
- **vibes:3@4, vibes:6@11, vibes:9@18, vibes:10@21**: all entity-targeted vibe-cloud updates on peak-bones or adjacent peak-shadow bones. vibes:3@4 (rising entrapment — fold-as-body-enactment); vibes:6@11 (rising entrapment — channel-receives-first-named-commission); vibes:9@18 (rising entrapment — feed-confirms-apparatus-as-actor); vibes:10@21 (atonement-as-repetition — named-person-closed-entry-in-ledger). All carry distinct new event-frame tokens; no string overlap within existing bundle documented. Vibes rubric requires entity-targeted cloud updates at peak-bones for affected entities per fan-out coherence gate (AP9). PASS scrutiny — not superfluous.
- **exposition:1@0**: prior-episode-bridge. @0 is preamble territory with no lens facet operating. The bridge is the sole carrier of the c09→c10 reader-state refresh. Lonely is expected and correct for a preamble entry (no co-citations inbound; it is the pre-graph territory). PASS scrutiny — not superfluous.

Two remaining concerns surfaced during scrutiny:

- **[narrator:4] @14** — narrator:4 is lonely with no inbound license. Per rubric, a lonely NI entry survives if it is self-standing. The R2 NI shard documents the W3 baseline-provision function. However, note that @14's bone ("corwick walks the errand-corridor") has Corwick as SVO — per scene-map protected-pattern, "corwick-feed-image @14 (Corwick-as-SVO = feed-recalled prior-circuit pattern, past-feed framing)." The narrator fires a feed-track read of the prior-circuit rhythm ("the supply cart, then the man at the post: the circuit runs the lower-gate road the way it has run it through nine passes, his mark in the geometry as fixed as the stone-post, the rhythm steady enough that she has stopped counting it"). This is a legitimate attention-landing. PASS on scrutiny — not superfluous. Advisory note only: the lonely state is expected for a baseline-provision fire. type: flag

- **[vibes:9] @18** — vibes:9 fires on `actor:taylor-hebert-kl-122ac ++ rising entrapment: [feed-confirms-apparatus-as-actor, the-cage-is-demonstrably-operational, network-executed-without-her-consent-or-design]`. @18 is a scene-C peak-bone (social_tether-antag +1.0). Lonely (no co-citation beyond its own license-out). For vibes, AP9 fan-out coherence requires firing on affected entities at apparatus-ran events; Taylor is the primary affected entity at @18. The token is new event-frame vs existing bundle. PASS scrutiny — not superfluous. type: flag

---

## CONSTRAINT findings (4)

**1. [state:8] @2 / [state:9] @4 / [state:10] @10 / [state:11] @11 / [state:12] @18 / [state:13] @21 / [state:14] @25 / [state:15] @26 — actor-state NI co-citation (partial)**

Per `rubric-state-updates.md § Cross-facet contract`: every `actor:<POV>.*` axis-move entry REQUIRES a narrator-interest co-citation on the same anchor. Checking:
- state:8 @2 (position_prot_rise 3→3.5): cite-index co=[exposition:4, narrator:1, vibes:1, vibes:2] — narrator:1 PRESENT. ✓
- state:9 @4 (social_tether_prot_rise 3→3.5): cite-index co=[vibes:3] — narrator: ABSENT. @4 bare of NI.
- state:10 @10 (moral_framework 1→0.5): cite-index co=[feel:1, narrator:3, sensory:2, vibes:4, vibes:5] — narrator:3 PRESENT. ✓
- state:11 @11 (social_tether_antag 2→2.5): cite-index co=[vibes:6] — narrator: ABSENT. @11 bare of NI.
- state:12 @18 (social_tether_antag 2.5→3.5): cite-index co=[vibes:9] — narrator: ABSENT. @18 bare of NI.
- state:13 @21 (moral_framework 0.5→0): cite-index co=[vibes:10] — narrator: ABSENT. @21 bare of NI.
- state:14 @25 (position_prot_rise 3.5→4): cite-index co=[sensory:7] — narrator: ABSENT. @25 bare of NI.
- state:15 @26 (social_tether_prot_rise 3.5→4): lonely — narrator: ABSENT. @26 bare of NI.

Six actor-state axis-move entries (@4, @11, @18, @21, @25, @26) lack NI co-citation.

**Documented defense (R2 NI shard, .r2-decisions.md §Flagged seam 3):** deliberate decision NOT to pad NI at these entries — @11 is under apparatus-muffle (the route is the surrender's delivery half, peak, must not carry a significance fire), @18 is the apparatus-ran confirmation under the same muffle, @21 is the writes-corwick peak under Khepri-ABSENT fence (a fire risks affirmation-by-naming), @25 is a grounding/transitional close, @26 is a grounding/transitional press. None is a genuine attention-landing. c09 precedent: c09 shipped with actor-state entries lacking NI (c09 state:5@8 had no NI). The co-citation rule scopes to perception-fields where NI would represent genuine attention; apparatus-muffle and protected-pattern override entries are out of scope for mandatory NI.

**Severity per RUBRIC-FIDELITY calibration rule: "defense present in entry notes → accept as SIGNAL, not HARD."** Defense is present in .r2-decisions.md.

- [state:9] @4 — constraint-cross-facet-co-citation — actor:taylor.social_tether_prot_rise axis-move lacks NI co-citation; documented defense (fold-as-body-enactment: somatic body gesture, apparatus-muffle-adjacent; not a genuine attention-landing per R2 NI shard judgment + vibes:3 carries the vibe-cloud update). type: flag

- [state:11] @11 — constraint-cross-facet-co-citation — actor:taylor.social_tether_antag axis-move lacks NI co-citation; documented defense (apparatus-muffle: route is the surrender's delivery half; @11 under W1 SURRENDER protected-pattern). type: flag

- [state:12] @18 — constraint-cross-facet-co-citation — actor:taylor.social_tether_antag axis-move lacks NI co-citation; documented defense (apparatus-muffle: apparatus-ran confirmation; central-event-muffle Phase 8.5 armed; Phase 8.5 guards apparatus-muffle for @18). type: flag

- [state:13] @21 — constraint-cross-facet-co-citation — actor:taylor.moral_framework axis-move lacks NI co-citation; documented defense (Khepri-ABSENT fence: a NI fire at the writes-corwick beat risks affirmation-by-naming on the override register the chapter must echo unnamed; inscription act is a peak-bone under specific protected-pattern; vibes:10 carries the vibe update). type: flag

- [state:14] @25 — constraint-cross-facet-co-citation — actor:taylor.position_prot_rise axis-move lacks NI co-citation; documented defense (grounding/transitional close; not a genuine attention-landing; sensory:7 carries the sound-drop perceptual inflection at ledger-close). type: flag

- [state:15] @26 — constraint-cross-facet-co-citation — actor:taylor.social_tether_prot_rise axis-move lacks NI co-citation; documented defense (grounding/transitional press; no genuine attention-landing per R2 NI shard). type: flag

Note: All six are SIGNAL per documented-defense severity rule. None escalates to HARD.

**2. [mem:1] @16 / [mem:2] @24 — memory NI-spine verification**

Per memory rubric: every KEEP memory entry on a climax chapter (feel-as-spine carve-out inapplicable) requires NI co-citation. R2 memory shard flagged this as a Phase-5-verifiable dependency. Checking cite-index:
- mem:1 @16: cite-index co=[narrator:7]. narrator:7 @16 EXISTS (R2 NI ADD confirmed). ✓ NI-SPINE SATISFIED.
- mem:2 @24: cite-index co=[narrator:8]. narrator:8 @24 EXISTS (R2 NI ADD confirmed). ✓ NI-SPINE SATISFIED.

**NI-SPINE DEPENDENCY RESOLVED.** Both memory entries ship spined. This is a PASS, not a finding. Noted here for the auditor's verification record.

**3. [mem:1] @16 / [mem:2] @24 — memory target-reference card-resolution (SIGNAL)**

Both memory entries cite project condition cards (`cond-override-architecture-residue-122ac`, `cond-kl-witch-label-formation-122ac`) rather than monument-*-class slugs. Per rubric: monument-card-resolution test prefers `monument-*`-class slugs; these are `cond-*`-class law cards.

Checking warehouse resolution: the dispatch brief and memory.md both confirm `cond-kl-witch-label-formation-122ac` and `cond-override-architecture-residue-122ac` are in `series.laws` (memory.md lines 68–72). The cards are listed as canonical law slugs at the series level. They exist in the project; re-gloss is not a dangling reference.

Per RUBRIC-FIDELITY § card-resolution: "Free-text glosses with no resolvable slug → HARD." These ARE resolvable slugs (they resolve in the series.laws list and warehouse). This is a class-question (cond-* vs monument-*) NOT a resolution failure.

Open parking-lot item pl-2026-05-25-005 tracks this as a margit-referral for whether a monument-* alias should be authored. Consistent with SIGNAL disposition.

- [mem:1] @16 — constraint-card-resolution-class — target-reference cites cond-kl-witch-label-formation-122ac (law card class, not monument class); card resolves in series.laws + warehouse; margit-referral open (pl-2026-05-25-005). type: flag

- [mem:2] @24 — constraint-card-resolution-class — target-reference cites cond-override-architecture-residue-122ac (law card class, not monument class); card resolves in series.laws + warehouse; margit-referral open (pl-2026-05-25-005). type: flag

**4. Exposition first-mention-character coverage check**

Per CONSTRAINT § exposition first-mention-character coverage: every named individual appearing in narrator-prose for the first time requires a `first-mention-character` exposition entry.

Cast: jarvis-coin-kl-courier, taylor-hebert-kl-122ac, corwick. All three are register-resident per glossed-terms.md and exposition:1 bridge restatement (Jarvis: b01c03:3 register-resident; Corwick: b01c08-graph-resident + c09 first-prose-appearance; Taylor: POV — excluded). New named individuals in proto-line prose: proto-line @17 mentions "Gold Cloak pair" — this receives first-mention-term exposition:2 @17. No other new named individuals appear. No first-mention-character HARD fault detected.

PASS.

---

## AP-SCAN findings (2)

**1. AP-SCAN: narrator-interest AP-010 (sentence-final "is what / is the X" collapse)**

R2 NI shard pattern-scan notes: "No 'is what' / 'is the X' sentence-final collapses across the file — the two adds were deliberately built off the chassis to avoid it." Manual scan of all 7 NI entries:
- narrator:1 @2: "the deniability she had been carrying is what the words spend" — contains "is what." One instance.
- narrator:3 @10: no "is what/is the X" collapse.
- narrator:4 @14: no collapse.
- narrator:5 @15: no collapse.
- narrator:6 @27: no collapse.
- narrator:7 @16: no collapse.
- narrator:8 @24: no collapse.

1/7 = 14% — below the 40% saturation threshold for escalation to HARD. SIGNAL.

- [narrator:1] @2 — AP-010 sentence-final-is-what — "the deniability she had been carrying is what the words spend"; one instance of 7 (14%); below saturation threshold. type: flag

**2. AP-SCAN: exposition anti-jargon / hollow-prose scan**

Scanning exposition entries for Earth-Bet proper nouns (full scan below) and hollow-prose patterns:
- exposition:1 @0: "the harm I can prevent is still the only column that closes" — register-resident accounting vocabulary; not hollow. "The courier has a name now" — clear. No jargon.
- exposition:2 @17: "a Gold Cloak pair — the City Watch, the crown's armed guard in King's Landing — posted at the junction, at rest, not passing through" — institutional orientation; first-mention inline-appositive form; no jargon.
- exposition:3 @13: "Two days later." — bare temporal marker. Clean.
- exposition:4 @2: "the packet sets it plainly: the protection over Sera continues as the consideration the function is owed against" — "the consideration the function is owed against" is late-positioned prepositional inversion; borderline dense but traceable to Taylor's accounting register and the packet's stated terms; not hollow prose per se. SIGNAL-advisory.

- [exposition:4] @2 — AP-SCAN voice-register-density — "the consideration the function is owed against" is inverted-prepositional construction; borderline Taylor-accounting register vs reader-accessible rendering; /and-stitch Phase 4 voice-embodiment may wish to smooth. type: flag

---

## Earth-Bet hard-fence proper-noun scan

Full scan across every text field of every facet entry:

**location-state** (all 8 entries): no Khepri, Gold Morning, Scion, Skitter, Brockton Bay, PRT, Endbringer, Cauldron, or any Earth-Bet proper noun found. Stone-post, bay-cold, wax-sealed, Gold-Cloak-pair-posted — all Westerosi/common-English. CLEAN.

**interest-narrator** (all 7 entries): narrator:1 @2 — "deniability"; narrator:3 @10 — "the months of it come up out of the feed-record in her hand... the conversion priced and paid in the one motion that cannot be unmade"; narrator:4 @14 — "the circuit runs the lower-gate road the way it has run it through nine passes"; narrator:5 @15 — "the road comes back a body short and the short is a positive fact"; narrator:6 @27 — "the posture squares again in the feed-record after the entry is closed... the ledger does not ask her to stay"; narrator:7 @16 — "the geometry of it is older than the work she does in it"; narrator:8 @24 — "the corridor closing behind him the way the channel closed over the entry." No Earth-Bet nouns. CLEAN.

**sensory** (all 7 entries): thermal, sound, smell, light, tactile entries. "stylus-on-channel-surface," "supply-cart-odor," "bay-cold-pressing-lower-road," "stone-cold-firm-under-wrist" — all environment-register. No Earth-Bet nouns. CLEAN.

**memory** (both entries): mem:1 @16 — "a machinery this old empties a corridor of one body and leaves the stone unmarked -> cond-kl-witch-label-formation-122ac"; mem:2 @24 — "the record closing the same way the old architecture closed around bodies it never asked -> cond-override-architecture-residue-122ac." Checking slug components: `cond-kl-witch-label-formation-122ac` — no Earth-Bet substring (kl=King's Landing, witch-label=Westerosi, 122ac=date); `cond-override-architecture-residue-122ac` — "override" is Earth-Bet-adjacent vocabulary (Khepri's override power), but the SLUG component is "override-architecture-residue" which is project-coined law-card vocabulary, NOT a proper noun (Khepri ABSENT; no "Gold Morning," no "Scion," no "Skitter"). The narrative text: "the old architecture closed around bodies it never asked" — "architecture" is common English used in the project register to mean surveillance architecture; not a proper noun. Khepri ABSENT verified. CLEAN.

**metaphor**: 0 entries. N/A. CLEAN.

**vibes** (all 15 entries, including off-anchor vibes:13–15): scan covers entity-target fields and keyword text. vibes:13 (episode + accounting-close-with-name), vibes:14 (actor:corwick + detained-through-the-channel), vibes:15 (loc:the-feed-station + accounting-workspace-weight). All keyword tokens: "cold-formalization-to-irreversible-surrender," "body-mapped-across-months-delivered-through-taylor-channel," "accounting-workspace-weight" — project-register vocabulary, no Earth-Bet proper nouns. Checking vibes:1–12: "atonement-as-repetition," "the-formal-instrument," "rising entrapment," "cost-made-visible-to-the-ledger," "the-apparatus-ran," "cold-utilitarian interiority," "the-closed-entry-that-stays" — all project keywords. No Brockton Bay, Skitter, Khepri, Gold Morning, Scion, Cauldron, PRT, Endbringer, or parahuman register. CLEAN.

**feeling** (both entries): feel:1 — "her breath shortens once over the body-map before her hands move to the channel"; feel:2 — "her gaze stays on the lower-gate posture in the feed-record and does not turn away when the ledger has closed." No Earth-Bet nouns. "body-map" is project-coined register for physical observation record, not Earth-Bet jargon. CLEAN.

**state-updates** (all 15 entries, env + actor): state field names (wax-condition, fauna_sense_status, spatial_layout, oc-feed-ledger, oc-feed-record, position_prot_rise_axis, social_tether_antag_axis, moral_framework_axis, social_tether_prot_rise_axis). Old/new values: pliable→dry, corwick-present→absent, unposted→Gold-Cloak-pair-posted, closed→open, absent→written, open→closed, logged-withheld→persisting-post-closure. All values project-register or common-English. No Earth-Bet proper nouns. "override" in field extension note ("social_tether_antag_axis") — this is project-coined axis name, not an Earth-Bet proper noun. CLEAN.

**exposition** (all 4 entries): scanned above in AP-SCAN voice section. confirmed CLEAN above — "Crone's stretch / first bell / Corwick / Jarvis / the Hook / lower-gate / Queen's business / Gold Cloak / City Watch / King's Landing / Sera / the protection / the function" — all Westerosi-Faith/Westerosi-political/register-resident vocabulary; no Earth-Bet proper nouns. CLEAN.

**Earth-Bet scan verdict: CLEAN across all 9 facets. 0 HARD findings.**

---

## TASTE-FLAG findings (1)

- **[exposition:1] @0** — voice-fidelity — the prior-episode-bridge uses "the harm I can prevent is still the only column that closes." This is Taylor's accounting register (clinical-instrument vocabulary). However, the clause "the harm I can prevent" followed by "is still the only column that closes" has a slightly abstract syntax; the gap between the real-world goal (prevent harm) and the accounting register (the column that closes) may read as an expository reach rather than felt conviction in Taylor's cold voice. The sentence follows Taylor's accounting convention faithfully, but "column" + "closes" together create a near-rhyme that may call attention to the construct at a preamble moment. Advisory. type: flag

---

## PILE-UP REVIEW (2 pile-ups)

Cite-index identifies 2 pile-ups (>4 co-located facets):

**@10 (5 facets): feel:1, narrator:3, sensory:2, vibes:4, vibes:5**
Bone: `taylor-hebert-kl-122ac translates the body-map`
- feel:1: somatic breath-shortening before the channel act.
- narrator:3: the cost as accounting (months / conversion priced and paid).
- sensory:2: sound onset (stylus-on-channel-surface) disambiguating the physical act.
- vibes:4: atonement-as-repetition ++ (body-map-translated-across-substrate-boundary).
- vibes:5: cost-made-visible-to-the-ledger + (first-named-commission-priced).

Assessment: @10 is the chapter's first moral cost (moral_framework –0.5), the W1 SURRENDER-AS-IRREVERSIBLE-ACT peak-bone. Each of the 5 fires is doing distinct work: feel covers the body, narrator covers the cognition, sensory covers the physical act's audible dimension (apparatus-muffle support), vibes:4 advances the atonement-as-repetition cloud, vibes:5 opens the cost-made-visible-to-the-ledger keyword. No content overlap between layers; no entry is displacing another's register. All grounding-ledger coverage confirms sensory:2 at @10 is grd-002 licensed (surrender renders as physical irreversible act, not substrate transaction). **WARRANTED.** The density is structural to the chapter's central surrender beat.

**@15 (5 facets): loc-state:5, narrator:5, sensory:4, vibes:7, vibes:8**
Bone: `the lower-gate road loses corwick`
- loc-state:5: road-geometry-minus-one (corwick-absent as place-state).
- narrator:5: attention on the positive-fact absence (the empty has the shape of an action).
- sensory:4: light drop (negative-space perceptual read against ordinary circuit baseline).
- vibes:7: episode + the-apparatus-ran (apparatus-ran operational consequence).
- vibes:8: actor:taylor + the-apparatus-ran (feed-confirmed-downstream-consequence).

Assessment: @15 is the chapter's central event of scene-C (position-world +1.0 peak-bone). Each layer contributes: loc-state marks the geometric state change; narrator registers Taylor's perceptual attention-landing; sensory delivers the perceptual-negative-space read (supporting apparatus-muffle: "NOT 'the feed flags the detention'"); vibes:7 fires the episode-scope apparatus-ran keyword; vibes:8 fires the actor-scope consequence-landing keyword. No register overlap; the grounding-ledger confirms sensory:4 at @15 is grd-004 licensed. **WARRANTED.** The density is structural to the chapter's operative detention confirmation.

---

## RUBRIC-FIDELITY findings (1)

**1. vibes target-validity — corwick and the-feed-station (gate 1 carve-out, SIGNAL)**

Per rubric-vibes.md § Required gates, gate 1: target slug must exist in card library. vibes:14 targets `actor:corwick`; vibes:15 targets `loc:the-feed-station`. Neither has a formal card in `cards/personas/`, `active-project/actors/`, `cards/locations/`, or `active-project/warehouse/`.

The vibes file itself documents this via a rubric-carve-out preamble citing the c08 precedent (vibes-b01-c08.md, carve-out for loc:the-hook-ward). The fan-out coherence gate (rubric gate 7) requires firing on affected entities; corwick is the detained party and this is the chapter's apparatus-ran event. The feed-station is a recurring accounting workspace. Both carve-outs are structurally justified.

Per RUBRIC-FIDELITY § severity calibration: "when defense is present in the entry's notes, accept as SIGNAL." The defense is present in the vibes file preamble.

- [vibes:14] @-- — rubric-fidelity-card-resolution — gate-1 target actor:corwick has no formal card (cards/personas/ or active-project/actors/); carve-out documented per c08 precedent + fan-out-coherence gate 7; margit-referral candidate: corwick.card.md. type: flag

- [vibes:15] @-- — rubric-fidelity-card-resolution — gate-1 target loc:the-feed-station has no formal card (cards/locations/ or active-project/warehouse/); carve-out documented per c08 precedent + recurring-anchor-first-vibe justification; margit-referral candidate: the-feed-station.card.md. type: flag

**2. scene-map protected-pattern "marks"-verb variation check**

Scene-map notes a marks-verb variation advisory: "@13 marks-lower-gate-road / @16 marks-side-exit + @7 marks-body-map — 3 'marks' instances across the chapter, vary at least one at prose layer." This is a /and-stitch advisory (the facet layer has no authority over prose verb choices), not an auditor RUBRIC-FIDELITY finding at this phase. Noted as a VF (voice-fixable) carry for /and-stitch Phase 4 per context_followability.voice_fixable_carry. No finding at Phase 5.

**3. state-updates rubric-fidelity — anti-pattern #1 registration-as-state check**

Scanning state-updates entries for registration vocabulary in `<new>` values: all new-values are physical/quantitative states (dry, absent, written, open, closed, persisting-post-closure, decimal rank values). None contain "noticed," "registered," "awareness," "baseline-new-faces" or other registration vocabulary. PASS.

**4. loc-state continuity-carry entry check (URI-SCENE-RHYTHM)**

loc-state has no continuity-carry entries (`continuity-from <id>:` notation absent from all 8 loc-state entries). PASS.

**5. memory doubled-register test**

Rubric file-level gate: at least one Earth-Bet displacement AND at least one Westerosi-monument clamp. mem:1 @16 → cond-kl-witch-label-formation-122ac (Westerosi clamp: KL disappearance-apparatus / witch-label formation). mem:2 @24 → cond-override-architecture-residue-122ac (Earth-Bet displacement: override-architecture-residue, Khepri-logic echoed without naming). Doubled-register SATISFIED. PASS.

**6. sensory modality distribution check**

5 distinct modalities: thermal @3/@19, sound @10/@25, smell @13, light @15, tactile @22. Modality floor ≥2: PASS. Dominance ceiling: thermal appears 2/7 = 29% (below 67% ceiling); sound 2/7 = 29%; no single modality ≥ 67%. PASS.

---

## Audit summary

- Total entries reviewed: 60 facet entries across 9 facets (location-state 8, narrator-interest 7, sensory 7, state-updates 15, memory 2, feeling 2, metaphor 0, vibes 15, exposition 4)
- Cite-index: 60 entries; 22/27 protolines decorated (81.5%); 5 bare (@5 @6 @7 @8 @26)

**HARD count: 0**

- STRUCTURAL: 0 HARD (1 flag — exposition ID file-physical ordering advisory)
- FREQUENCY-BAND: 0 HARD (4 signals — NI breach-high +0.9pt documented defense; feeling breach-high +2.4pt documented defense; sensory band-exempt grounding-licensed; exposition 11.1% denominator-driven)
- METADATA-INCONSISTENCY: 0 HARD (1 flag — vibes episode slug hyphenation inconsistency)
- CURVE-SHAPE: SHAPE-OK
- CONTRADICTION: 0
- DEDUP: 0 HARD (1 flag — mem:2/@24 + narrator:8/@24 figurative-register proximity advisory)
- SUPERFLUOUS: 0 HARD (2 advisory flags — narrator:4@14 lonely/warranted; vibes:9@18 lonely/warranted)
- CONSTRAINT: 0 HARD (6 flags — actor-state NI co-citation on @4/@11/@18/@21/@25/@26; all documented defense → SIGNAL; 2 flags — memory cond-* vs monument-* card class → SIGNAL with margit-referral)
- AP-SCAN: 0 HARD (2 flags — narrator:1 AP-010 one instance/7 below saturation; exposition:4 inverted-prepositional advisory)
- TASTE-FLAG: 1 flag (exposition:1 @0 voice-fidelity advisory)
- PILE-UP REVIEW: 2 pile-ups, both WARRANTED
- RUBRIC-FIDELITY: 0 HARD (2 flags — vibes:14/@15 gate-1 carve-out margit-referrals, documented defense)

**Total findings: 16 (all type: flag; 0 type: fault; 0 type: escalate)**

**SIGNAL class counts:** FREQUENCY-BAND 4, METADATA-INCONSISTENCY 1, AP-SCAN 2, TASTE-FLAG 1, CONSTRAINT 8 (all flags/signal per documented defense), RUBRIC-FIDELITY 2 (signal per documented defense)

## Routing

All 16 findings are type: flag (advisory). HARD count = 0.

- **FREQUENCY-BAND flags (4):** advisory to showrunner; NI/feeling/exposition short-chapter denominator effects documented. No fixer dispatch.
- **METADATA-INCONSISTENCY flag (1):** cosmetic; vibes episode-slug author. No fixer dispatch.
- **DEDUP flag (1):** mem:2/@24 + narrator:8/@24 figurative-register proximity; advisory to /and-stitch Phase 4 voice-embodiment discipline (ensure the two comparisons read as deliberate rhyme, not accidental echo). No fixer dispatch.
- **SUPERFLUOUS flags (2):** narrator:4@14 and vibes:9@18 lonely entries verified as warranted; advisory only.
- **CONSTRAINT flags (8):** six actor-state NI co-citation absences all carry documented defense (apparatus-muffle / Khepri-ABSENT fence) → route to showrunner awareness + margit for monument-card class question on memory targets.
- **AP-SCAN flags (2):** narrator:1 AP-010 one-instance (below saturation threshold); exposition:4 inverted-prepositional density → advisory to /and-stitch Phase 4.
- **TASTE-FLAG (1):** exposition:1 @0 voice-fidelity advisory → /and-stitch Phase 1 render.
- **RUBRIC-FIDELITY flags (2):** vibes:14 + vibes:15 gate-1 carve-out → margit-referral for corwick.card.md + the-feed-station.card.md.
- **Earth-Bet scan:** CLEAN across all 9 facets. Khepri ABSENT confirmed at @24 NI and memory.

**Phase 5 gate: HARD = 0. Phase 5b (audience-gate) may proceed.**
