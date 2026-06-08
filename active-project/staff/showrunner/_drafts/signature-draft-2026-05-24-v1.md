# series substance signature — DRAFT (Phase 4a)
# author: screen-writer
# date: 2026-05-24
# project: taylor-westeros-good-intentions
# upstream: series.chunk (path + trajectory) — see active-project/staff/showrunner/{memory.md, series-trajectory.md}
# next: user edits inline; types `accept` to persist to series.substance.*; or `redraft` for a fresh proposal.

## series.substance (proposed)

```yaml
state_axes:

  # ── AXIS 1: moral_framework ─────────────────────────────────────────────────
  # The prohibition against instrumentalizing persons — Khepri-haunted; the
  # rule Taylor came to Westeros to obey. Tracks whether the accounting method
  # still functions as moral compass or only as moral record.

  - slug: moral_framework
    dimension: 'integrity of the anti-instrumentalization prohibition as operating compass'
    one_means: 'prohibition intact and operationally enforced — Taylor refuses every act of directing others'
    five_means: 'prohibition named and believed but licensed exceptions accumulating — first sanctioned breach acknowledged'
    nine_means: 'framework consumed as compass: ledger still runs, all entries rationalized, prohibition the most violated line'
    perspective: protagonist
    start_rank: 2
    end_rank: 8
    class: emotional
    notes: 'monotonic collapse; start 2 not 1 because prohibition is explicit and initially held; d03 is first crack, d12 is irrevocable'
    start_rank_justification: 'series-trajectory start_state: Khepri-haunted refusal-of-control; prohibition stated and operative at open'
    end_rank_justification: 'series-trajectory end_state: framework eaten as compass; d12 irrevocable-Khepri-repetition; LOCKED'

  # Otto holds his own moral framework static — he operates without prohibition;
  # antagonist perspective on this axis is not in motion; omitted to avoid dead axis.
  # world perspective: not applicable — the court has no equivalent prohibition machinery.

  # ── AXIS 2: capability ──────────────────────────────────────────────────────
  # Taylor's insect-control + pattern-reading capability, measured as degree of
  # systematic deployment. Tracks from penance-suppressed dormancy to
  # Khepri-rhyming surveillance architecture fully load-bearing.

  - slug: capability
    dimension: 'scope and systematization of insect-network intelligence deployment'
    one_means: 'fully suppressed by choice — insects kept at subsistence range, no systematic reading'
    five_means: 'localized deployment — Flea Bottom coverage, reading bodies in known wards, not yet feeding a patron'
    nine_means: 'Khepri-rhyming surveillance architecture: full ward coverage, unconsented instrumentalization at scale, network structural to Greens'
    perspective: protagonist
    start_rank: 2
    end_rank: 8
    class: plot
    notes: 'monotonic rise; start 2 not 1 because residue range is intact even while suppressed; end 8 not 9 because network outlasts Taylor not as an ongoing act but as a transferred structure'
    start_rank_justification: 'series-trajectory start_state: capability suppressed by choice; insect control intact at Flea Bottom density; not deploying'
    end_rank_justification: 'series-trajectory end_state: d12 fully-deployed-and-load-bearing; d14 network outlasts architect; LOCKED'

  # antagonist perspective: not applicable — Otto does not operate on this axis;
  # his pressure is positional/tether, not capability-competition.
  # world perspective: not applicable — KL court tracks Taylor's capability only
  # instrumentally (Otto notices it at d03); no world-level capability arc.

  # ── AXIS 3: position ────────────────────────────────────────────────────────
  # Taylor's legibility and standing in the power structure. Measures how
  # visible and useful she is to the court layer that will eventually remove her.

  - slug: position
    dimension: "legibility and standing within the KL court power structure"
    one_means: "smallfolk-anonymous — no rank, no coin above subsistence, invisible to every court layer"
    five_means: "known-quantity-to-one-court-layer — Otto aware of Taylor; function defined; no formal standing"
    nine_means: "Otto's-unofficial-instrument-at-full-load — position-of-no-exit; too legible to be released"
    perspective: protagonist
    start_rank: 1
    end_rank: 1
    class: plot
    notes: "rise-then-collapse; rises to ~6 at d07 (Otto's-unofficial-instrument), peaks near 7 at d10 (position-of-no-exit), collapses to 1 at d14 (dead/expelled); LOCKED end-state"
    start_rank_justification: 'series-trajectory start_state: smallfolk-anonymous; no rank, no coin; invisible'
    end_rank_justification: 'series-trajectory end_state: dead or expelled; position made irrelevant by removal; LOCKED hard fence'

  - slug: position
    dimension: "Green-faction consolidation of KL institutional control"
    one_means: "contested succession, no faction controls court apparatus; council fluid"
    five_means: "Green faction dominant in council but succession unresolved; Viserys alive, Rhaenyra a live claimant"
    nine_means: "Green-faction control of Maegor Holdfast, Small Council, and succession angle — apparatus locked"
    perspective: world
    start_rank: 5
    end_rank: 9
    class: plot
    notes: "monotonic rise; Taylor's intelligence deliveries are the consolidation mechanism; world gains exactly as protagonist pays moral_framework"
    start_rank_justification: "122 AC world-notes: Alicent faction already consolidated by 120 AC; Otto operating advisory off-council; succession contested but Green dominance institutional not informal"
    end_rank_justification: "series-trajectory d13: Green-faction control of Maegor Holdfast, Small Council, succession angle — product of Taylor's trades"

  # ── AXIS 4: social_tether ───────────────────────────────────────────────────
  # Taylor's institutional and relational cover in KL — from nil anonymity through
  # load-bearing apparatus membership to severed. Non-monotonic: rises to
  # near-peak (Otto-embedded) then collapses at d14.

  - slug: social_tether
    dimension: "depth and load-bearing weight of Taylor's relational and institutional ties in KL"
    one_means: "nil — arrived in an alley with nothing; no name anyone will remember; no institutional cover"
    five_means: "smallfolk-embedded and patron-adjacent — Flea Bottom contacts; Otto aware but arrangement not yet structural"
    nine_means: "load-bearing-in-Otto's-architecture — network structural to Greens; Taylor cannot exit without triggering collapse"
    perspective: protagonist
    start_rank: 1
    end_rank: 1
    class: plot
    notes: "rise-then-collapse; rises to ~7 at d04 (load-bearing-in-Otto's-architecture), peaks ~8 at d07, exposed and non-extractable at d10, severed at d14; LOCKED end-state"
    start_rank_justification: 'series-trajectory start_state: Flea Bottom anonymous; arrived with nothing; anonymity is protective and the point'
    end_rank_justification: "series-trajectory end_state: severed — cost-bearer dead, patron channel dissolved, network now Otto's not Taylor's; LOCKED"

  - slug: social_tether
    dimension: "Otto Hightower's leverage over Taylor through the network she builds"
    one_means: "Otto has no knowledge of Taylor; no leverage exists"
    five_means: "Otto has identified the capability and made the offer; leverage embryonic — Taylor could still walk"
    nine_means: "Taylor is too load-bearing to withdraw; Otto's leverage is structural; exit would trigger counter-action"
    perspective: antagonist
    start_rank: 1
    end_rank: 9
    class: plot
    notes: "monotonic rise tracking Taylor's embeddedness; antagonist gains leverage at d03, leverages it fully by d10 (non-extractable confirmed)"
    start_rank_justification: "series-trajectory start_state: Taylor invisible to court layer; Otto has no knowledge of her at open"
    end_rank_justification: "series-trajectory d10: Taylor too load-bearing to withdraw; one channel that might extract cost-bearer is inside Otto's coverage"

  # ── AXIS 5: relational_anchor_status ────────────────────────────────────────
  # Pressure-accumulation axis. Not positional. Tracks the operational weight
  # loading onto the un-priced anchor ([cost-bearer]). Rank 1 = anchor exists,
  # no weight on the unpricing. Rank 9 = unpricing is structurally causal to
  # the catastrophe. Taylor's ledger exclusion is held constant; what changes
  # is what that exclusion costs.

  - slug: relational_anchor_status
    dimension: "operational weight loading onto the un-priced relational anchor ([cost-bearer])"
    one_means: "anchor present; no operational weight — Taylor is attached, [cost-bearer] not yet in any calculus"
    five_means: "anchor inside the protection architecture without [cost-bearer]'s knowledge or consent; Taylor routing around use-vectors"
    nine_means: "[cost-bearer]'s exclusion from the ledger is structurally causal to their death — the un-priced item is the one Taylor could not defend"
    perspective: protagonist
    start_rank: 1
    end_rank: 9
    class: emotional
    notes: "monotonic rise in pressure; the relationship itself does not change — the weight of not-pricing it does; [cost-bearer] never enters the ledger; d14 is the revelation"
    start_rank_justification: "series-trajectory d01-d02: cost-bearer present from near-open; attachment permitted; removal from model noticed but filed as atonement-working"
    end_rank_justification: "series-trajectory end_state: cost-bearer dead before Taylor can spend the protection built; un-pricing retroactively revealed as structural; LOCKED"

  # antagonist perspective: not directly applicable as an axis in motion —
  # Otto never identifies [cost-bearer] as leverage; the pressure is structural not agential.
  # world perspective: not applicable — the world does not track individual un-priced attachments.

  # ── AXIS 6: moral_legibility_to_self ────────────────────────────────────────
  # Taylor's clarity about what she is actually doing. Starts functional-but-
  # deceived (she believes the atonement is working), moves through
  # rationalization stages, arrives at full recognition too late to constitute
  # refusal.

  - slug: moral_legibility_to_self
    dimension: "accuracy and completeness of Taylor's self-accounting against what she is actually doing"
    one_means: 'no accounting at all — operating blind or in full denial; impossible for Taylor; floor is 3'
    five_means: 'rationalizing-each-trade — accounting runs but each entry is filed as acceptable; recognition exists, is suppressed'
    nine_means: 'recognition-too-late: full clarity on the repetition, delivered by the ledger, in time only to be unable to deny it'
    perspective: protagonist
    start_rank: 4
    end_rank: 8
    class: emotional
    notes: 'non-linear but net-positive; atoning-and-aware at 4 (believes she is succeeding); cracks at d02, d06, d10; recognition suppressed at d10; full recognition at d14; 8 not 9 because too-late diminishes usability'
    start_rank_justification: 'series-trajectory start_state: atoning-and-aware; knows what she did at Gold Morning; believes the atonement is working'
    end_rank_justification: 'series-trajectory end_state: recognition-too-late; sees the repetition but too late to undo; accounting delivers final output clearly; LOCKED'

  # antagonist perspective: not applicable — Otto's self-accounting is not in motion;
  # he operates with clear purpose and no comparable prohibition machinery.
  # world perspective: not applicable — the court does not have self-accounting as a tracked state.

  # ── AXIS 7: political_register_toward_elite ─────────────────────────────────
  # Taylor's internal stance toward the Westerosi ruling class — from
  # neutral-instrumentally-observant through readable resentment to fully
  # articulated, named, actionless contempt.

  - slug: political_register_toward_elite
    dimension: "Taylor's stance toward the Westerosi ruling class as revealed by what the insect-feed returns"
    one_means: 'neutral-instrumentally-observant — reads the court as a system; no investment, no contempt, no affect'
    five_means: 'readable-resentment — color has accumulated; not yet named; the insects bring it back and Taylor notices'
    nine_means: 'contempt-without-refusal — fully articulate, cold, named by name, bound to continued service; clarity as its own trap'
    perspective: protagonist
    start_rank: 1
    end_rank: 9
    class: emotional
    notes: 'monotonic rise; d05 resentment readable, d09 articulated-contempt, d13 contempt-without-refusal (LOCKED end); the contempt is the ledger in its final form'
    start_rank_justification: 'series-trajectory start_state: neutral-instrumentally-observant; registers court as system to read; no investment, no contempt'
    end_rank_justification: 'series-trajectory end_state + d13: contempt-without-refusal — fully articulated, fully legible, bound to continued service; LOCKED'

  - slug: political_register_toward_elite
    dimension: "Green-faction succession position — the continuity Taylor's trades guarantee"
    one_means: 'succession unresolved; Greens without institutional advantage; rival claims live'
    five_means: 'Green faction dominant in informal channels; Otto operating effectively outside council'
    nine_means: 'Green-faction position secured — Maegor Holdfast, Small Council, dynastic angle locked; continuity guaranteed until Dance ignites'
    perspective: world
    start_rank: 4
    end_rank: 9
    class: plot
    notes: "monotonic rise; mirrors Taylor's political_register rise — she despises what she is consolidating; world benefits in exact proportion to her contempt growing"
    start_rank_justification: '122 AC: Otto dismissed from council 120 AC but Alicent faction consolidated; succession contested; Rhaenyra at Dragonstone still a live claimant'
    end_rank_justification: 'series-trajectory d13: Taylor reviews what consolidation produced — Green-faction control of Maegor Holdfast, Small Council, succession angle'

cost_ledger:

  - id: cl01
    gain: 'capability +2, social_tether +2'
    cost: 'opportunity-missed: rescue is witnessed; witch-label forms; [cost-bearer] block enters the exposure radius'
    anchor: { book: b01, chapter: null, scene: null }
    notes: "d01 rescue: capability deployed (first use since Gold Morning); social_tether opens into Flea Bottom; witch-label witnesses load the un-priced anchor with its first operational weight — pressure on relational_anchor_status (+2) follows but is accounted for in cl07's tether/anchor cascade, not here, to avoid double-counting"

  - id: cl02
    gain: 'position +4'
    cost: 'moral_framework -3'
    anchor: { book: b01, chapter: null, scene: null }
    notes: 'd03 Otto-offer accepted: position rises from anonymous to known-quantity-to-court-layer; the prohibition sees its first sanctioned exception; two-beat refusal means the breach is legible as a choice'

  - id: cl03
    gain: 'capability +3, social_tether +4'
    cost: 'moral_framework -3'
    anchor: { book: b01, chapter: null, scene: null }
    notes: "d04+d07 network construction: surveillance architecture built and formalized; Taylor becomes Otto's Flea Bottom intelligence apparatus; cost is systematic override rationalized as necessary"

  - id: cl04
    gain: 'relational_anchor_status +3'
    cost: 'opportunity-missed: extraction path before network became non-withdrawable'
    anchor: { book: b01, chapter: null, scene: null }
    notes: 'd10 exit-calculation returns impossible: Taylor prices the exit, finds no path, ratifies the courier detention, closes the ledger; the missed window is the cost'

  - id: cl05
    gain: 'capability +2'
    cost: 'moral_framework -2'
    anchor: { book: b01, chapter: null, scene: null }
    notes: 'd12 full deployment: network pushed to full ward coverage to protect [protect-target]; scale smaller than Gold Morning, moral shape the same; irrevocable-Khepri-repetition confirmed (this is the floor on moral_framework; the prohibition cannot collapse further once the repetition is irrevocable)'

  - id: cl06
    gain: 'political_register_toward_elite +5'
    cost: 'opportunity-missed: contempt arrives with no exit attached; clarity forecloses nothing'
    anchor: { book: b01, chapter: null, scene: null }
    notes: 'd09+d13 contempt arc: articulated contempt is the clearest the ledger ever runs; cost is that clarity has no purchase — she names the empowered, continues serving them; the contempt is not freedom'

  - id: cl07
    gain: 'moral_legibility_to_self +4'
    cost: 'relational_anchor_status +4, social_tether -7, position -6'
    anchor: { book: b01, chapter: null, scene: null }
    notes: 'd14 burn: the final ledger entry cashes everything; [cost-bearer] dead in the mapped streets; Taylor removed; moral_legibility reaches recognition-too-late (which is the only axis that rises — and the rise is itself the recognition that there is nothing left to spend it on; "gain" is technically structured-cost-cashing, but schema-bend retained to honor the structural pattern)'

antagonist_pressure:

  - axis: moral_framework
    pressure_source: 'Otto Hightower — each ask prices a specific protection, making refusal a calculation rather than a prohibition'
    cost_curve: 'escalates monotonically; d03 opens the account, d07 formalizes it, d12 makes it irrevocable; Otto never presses — the calculation does'

  - axis: social_tether
    pressure_source: 'Otto Hightower — the network Taylor builds to survive is simultaneously the architecture that makes her non-extractable'
    cost_curve: "escalates then caps; peaks at d10 (non-extractable confirmed); d14 collapses the tether entirely as the patron channel dissolves with Taylor's removal"

  - axis: position
    pressure_source: 'Otto Hightower — formal legibility as his unofficial instrument; too load-bearing to release, too informal to protect'
    cost_curve: "escalates to d10 peak (position-of-no-exit), then collapses at d14 when Taylor's removal makes the position irrelevant"

  - axis: relational_anchor_status
    pressure_source: "cond-kl-witch-label-formation-122ac — the witch-label social physics that makes Taylor's insect-use publicly visible and routes community suspicion toward her contacts"
    cost_curve: 'escalates monotonically from d01 (witnesses at rescue) through d04 (network threads through wards); caps when Taylor routes around vectors that might expose [cost-bearer] to Otto'

  - axis: relational_anchor_status
    pressure_source: 'Dance-ignition timeline — the structural antagonist Taylor cannot name or see; the background war schedule that makes every protection window provisional'
    cost_curve: "invisible and constant; not escalating in Taylor's perception; catastrophically present at d14 when the timeline's bladed answer moves through the mapped streets"

  - axis: moral_legibility_to_self
    pressure_source: 'Gold Morning memory — internal antagonist; the standard against which Taylor measures every override; the specific shape she is repeating'
    cost_curve: 'oscillates; suppressed at each rationalization beat (d06, d10, d11); surfaces sharply at d09 (articulated contempt) and terminally at d14 (recognition-too-late)'

chunk_targets:
  series:  { delta_per_signature_axis: 4-8, density_target: 0.6-0.9 }
  book:    { delta_per_signature_axis: 3-4, density_target: 0.7-0.9, bone_count: 270-500 }
  chapter: { delta_per_signature_axis: 0.5-1.5, density_target: 0.5-0.9, bone_count: 15-75 }
  scene:   { delta_per_signature_axis: 0-1.5, density_target: 0.6-0.9, bone_count: 5-15 }
  bone:    { delta_per_axis: 1-3, axes_per_bone: 1-2 }
```

---

## At-a-glance axis summary

```
axis                         | perspective  | start | end | delta | curve
─────────────────────────────|──────────────|───────|─────|───────|──────────────────────
moral_framework              | protagonist  |   2   |  8  |  +6   | monotonic collapse
capability                   | protagonist  |   2   |  8  |  +6   | monotonic rise
position                     | protagonist  |   1   |  1  |   0   | rise-then-collapse (peak ~7 at d10)
position                     | world        |   5   |  9  |  +4   | monotonic rise
social_tether                | protagonist  |   1   |  1  |   0   | rise-then-collapse (peak ~8 at d07)
social_tether                | antagonist   |   1   |  9  |  +8   | monotonic rise (Otto leverage)
relational_anchor_status     | protagonist  |   1   |  9  |  +8   | monotonic pressure accumulation
moral_legibility_to_self     | protagonist  |   4   |  8  |  +4   | net-rise with suppression dips
political_register_toward_elite | protagonist |  1  |  9  |  +8   | monotonic rise (contempt arc)
political_register_toward_elite | world      |  5   |  9  |  +4   | monotonic rise (court consolidates)
```

**Total protagonist axis Δ (summed absolute values):** 40 ranks across 7 axes.
**Axes with aggregate net-zero but load-bearing curves:** position (protagonist), social_tether (protagonist) — both rise-then-collapse; the curve IS the story shape.
**Held axes (start = end):** position (protagonist), social_tether (protagonist) — NOTE: "held" here means the curve returns to start; the intermediate motion is the substance-bearing path. These are NOT zero-Δ chapters. Per-chapter contracts must track the rise and the collapse separately.

---

## Cost-ledger summary

```
id   | gain axis(es)                          | cost axis / form                            | trajectory delta(s)
─────|────────────────────────────────────────|─────────────────────────────────────────────|──────────────────
cl01 | capability +2, social_tether +2        | opportunity-missed: rescue witnessed        | d01
cl02 | position +4                            | moral_framework -3                          | d03
cl03 | capability +3, social_tether +4        | moral_framework -3                          | d04 + d07
cl04 | relational_anchor_status +3            | opportunity-missed: extraction path         | d10
cl05 | capability +2                          | moral_framework -2                          | d12
cl06 | political_register_toward_elite +5     | opportunity-missed: contempt as trap        | d09 + d13
cl07 | moral_legibility_to_self +4            | relational_anchor +4, tether -7, pos -6     | d14
```

**Authoring notes (post-fix, 2026-05-24):**

- **cl01:** cost field switched from `relational_anchor_status +2` (schema-bent pressure-increment) to `opportunity-missed: rescue is witnessed; witch-label forms; [cost-bearer] block enters the exposure radius`. The relational_anchor_status pressure accumulation is now accounted for end-to-end in cl07 to avoid double-counting.
- **cl04 / cl06:** `opportunity-missed` form preserved. The cost is exit-foreclosure; no axis decrements.
- **cl05:** dropped the second gain clause (`moral_framework-collapse-confirmed` was descriptive, not an axis+delta). cl05 floors moral_framework at the bottom; that's structural commentary in `notes`, not a tracked axis movement.
- **cl07:** schema-bent retained but reshaped. `gain: moral_legibility_to_self +4` is the only protagonist axis that actually rises at d14 (recognition-too-late is structurally the highest legibility Taylor reaches). The "gain" is technically structured-cost-cashing — the recognition IS the catastrophe legible to her — but the schema-compliant shape preserves the structural pattern that d14 fires its own line in the ledger.
- **slot-deferred names:** all references to specific cast members ([cost-bearer], [protect-target]) use placeholders. `/and-cast` resolves at Phase 4 cast provisioning. Library cards (wren / sera) exist from the prior cycle; the prior selection is not pre-committed.
