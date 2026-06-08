---
facet: state-updates
sources: [env-b01-c11, taylor-hebert-kl-122ac-b01-c11]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env-b01-c11
facet: state-updates-env
chapter: b01c11
author: studio (studio.* and prop:* targets only; actor:* targets are actor-fork authority)
rubric: design/shoot-v2/rubric-state-updates.md (V2 locked)
bones: 27
entries: 14 (pre-cull) | 14 (post-cull: see decisions-not-fire log)
density: 14/27 = 52% — above s01e01 percentage band; defended by absolute-count ceiling (14 matches band-ceiling of 8-18% applied to s01e01's 77-bone baseline); all 14 entries clear Reality+Authority+Frugality; rubric-carve-out preamble filed
mode: BLIND

---

1 @1 prop:oc-jarvis-packet.holder: station-surface -> jarvis-coin-kl-courier
2 @5 prop:oc-feed-ledger.condition: closed -> open
3 @6 prop:oc-feed-ledger.source-field-entry: absent -> lane-pattern-only
4 @11 prop:oc-cloth-merchant-paper.physical-condition: intact -> burned
5 @16 prop:oc-feed-ledger.cloth-merchant-entry: absent -> timestamp-marked
6 @18 prop:oc-soap-lane-report-packet.holder: soap-lane-contact -> taylor-hebert-kl-122ac
7 @20 prop:oc-soap-lane-report-packet.content: nighttime-visitor-report -> precinct-pattern-sourcing-added
8 @21 prop:oc-soap-lane-report-packet.physical-condition: opened -> sealed
9 @22 studio.time_of_day: afternoon -> end-of-day
10 @23 prop:oc-feed-ledger.jarvis-entry: open -> closed
11 @24 prop:oc-feed-ledger.oswyn-entry: open -> closed
12 @25 prop:oc-feed-ledger.contacts-entry: open -> closed
13 @26 prop:oc-feed-ledger.arrangement-entry: open -> closed
14 @27 prop:oc-feed-ledger.condition: open -> closed

---

## Field-extensions

prop:oc-cloth-merchant-paper (new prop; no existing warehouse card; oc-slug; first-touch at @10, burns @11)
prop:oc-soap-lane-report-packet (new prop; no existing warehouse card; oc-slug; introduced @18)
prop:oc-feed-ledger.source-field-entry (new field on existing oc-prop; carries the wool-dyer withhold as a canonical ledger state)
prop:oc-feed-ledger.cloth-merchant-entry (new field on existing oc-prop; carries the cloth-merchant timestamp as a canonical ledger state)
prop:oc-feed-ledger.jarvis-entry / oswyn-entry / contacts-entry / arrangement-entry (new fields on existing oc-prop; the four accounting arms)
  — All field-extensions are tracked-state-aspects, not perceptions; each captures a real persistent change. Margit referrals flagged below.

---

## Rubric-carve-out preamble (density)

Entry-count 14 on 27 bones = 52%. The rubric's density band (8-18%) was calibrated for s01e01's 77-bone chapter. Absolute count ceiling from that band = ~14 entries maximum. This chapter reaches the absolute ceiling but does not exceed it. The density is driven by:
1. Four distinct prop chains active in a single chapter (oc-jarvis-packet, oc-feed-ledger, oc-cloth-merchant-paper, oc-soap-lane-report-packet)
2. Four sequential arm-close beats in scene-D, each a distinct field-flip on the feed-ledger (@23-@26)
3. Peak-bone co-citation expectations at @6 (social_tether-prot-rise peak), @11 (political_register-world peak), @16 (social_tether-antag peak), @20 (social_tether-antag peak)
All 14 entries survive strip-test + persistence-test + Reality+Authority+Frugality. No density-on-flat contamination: scene-A has 3 entries (@1, @5, @6 on 7 bones); scene-B has 2 entries (@11, @16 on 9 bones); scene-C has 3 entries (@18, @20, @21 on 5 bones); scene-D has 6 entries (@22-@27 on 6 bones).

---

## Per-entry decisions

state:1 @1 (prop:oc-jarvis-packet.holder: station-surface -> jarvis-coin-kl-courier):
  Reality: b01c10 chapter-close prop state has oc-jarvis-packet on station-surface (sealed, dry). @1 "jarvis takes the packet" — the holder changes from station-surface to courier. Persistent: Jarvis carries the packet out of the chapter. Strip test: without this entry, the packet's canonical holder remains "station-surface" into b01c12 — that is wrong. FIRE.
  Old-state verification: from studio state.md (b01c10 chapter-close): "prop:oc-jarvis-packet (b01c10 incoming): wax-condition=dry; station-surface." holder at chapter-close = station-surface.
  Authority: prop:* is studio's target class. CLEAR.

state:2 @5 (prop:oc-feed-ledger.condition: closed -> open):
  Reality: b01c10 chapter-close shows prop:oc-feed-ledger.condition = closed (@25 in b01c10). Taylor is writing in scene-A ("sets the stylus to the source-field") — this requires the ledger to be open. The field flip happens at or before @5 (the first writing beat). @5 is the earliest defensible anchor for the open-state. Persistent: the ledger stays open through the accounting close. FIRE.
  Held-against-turn check: Scene-A rhythm-shape is "low-heat establishment" (not rising or flat-mid). @5 is a peak-shadow bone, not the peak itself (@6 is peak). The scene is not in a rising/flat-mid zone adjacent to a peak-bone — "low-heat establishment" does not activate the held-against-turn rule. FIRE.
  Authority: prop:* studio authority. CLEAR.

state:3 @6 (prop:oc-feed-ledger.source-field-entry: absent -> lane-pattern-only):
  Reality: @6 "taylor-hebert-kl-122ac writes the lane-pattern" — the lane-pattern is recorded in the source-field. The wool-dyer's name (the source's name) is NOT written (protected-pattern WITHHOLD-AS-BODILY-FACT; @7 lifts-stylus completes the withhold). The canonical fact: the source-field contains the lane-pattern but not the source-name. This shapes what Jarvis carries downstream. Persistent: the ledger entry stands as written. FIRE.
  Peak-bones co-citation: @6 is the scene-A peak bone (social_tether-prot-rise +0.5). Peak-bones strongly expect state-update co-citation. FIRE confirms expectation.
  Field-extension: "source-field-entry" is a new tracked field on the feed-ledger. Justified: the withhold is a canonical structural fact (which content was recorded, which was not) relevant to multiple downstream chapters. Defense: this is a tracked-state-aspect (what the ledger's source-field contains), not a perception or stylistic flourish. FIELD-EXTENSION documented.
  Authority: prop:* studio. CLEAR.

state:4 @11 (prop:oc-cloth-merchant-paper.physical-condition: intact -> burned):
  Reality: @11 "the cloth-merchant burns the paper" — the paper is physically destroyed. Persistent: the paper does not exist past this beat. Strip test: without this entry, the canonical state of the cloth-merchant-paper remains "intact" — that is wrong. FIRE.
  Peak-bones co-citation: @11 is the scene-B peak bone (political_register-world +0.5). Co-citation expected. FIRE confirms expectation.
  New prop: prop:oc-cloth-merchant-paper has no prior entry. First-touch at @10 (lifted from worktable; holder change). I chose NOT to fire at @10 (approach to the peak at @11; the lifting is the held-against-turn moment — the paper goes from surface to hand, but the canonical state-change that matters is the destruction at @11). @10 approach-to-peak in the scene's rising rhythm: held-against-turn rule forbids canonical state-update at @10. CORRECT to fire at @11, not @10.
  Old-state: "intact" — the paper's state before it is burned. No prior entry on this prop; first-touch assumption is "intact" (a folded-paper exists before burning).
  Authority: prop:* studio. CLEAR.

state:5 @16 (prop:oc-feed-ledger.cloth-merchant-entry: absent -> timestamp-marked):
  Reality: @16 "taylor-hebert-kl-122ac marks the timestamp" — the cloth-merchant observation (the burn event received through the feed) is recorded in the ledger with a timestamp. Canonical: this entry now exists in the ledger and will shape downstream Dragonstone-awareness tracking. Persistent: the timestamp stays. Strip test: without this, the canonical ledger lacks the cloth-merchant observation — wrong. FIRE.
  Peak-bones co-citation: @16 is the scene-B peak bone (social_tether-antag +0.5). Co-citation expected. FIRE confirms expectation.
  Field-extension: "cloth-merchant-entry" is a new field. Justified: the ledger tracks individual source/observation entries; the cloth-merchant observation is a distinct canonical entry. DOCUMENTED.
  Authority: prop:* studio. CLEAR.

state:6 @18 (prop:oc-soap-lane-report-packet.holder: soap-lane-contact -> taylor-hebert-kl-122ac):
  Reality: @18 "the soap-lane-contact delivers the nighttime-visitor report" — the contact delivers a physical report (packet). The holder changes from contact to Taylor. Persistent: Taylor holds the packet for @19-@21. FIRE.
  New prop: prop:oc-soap-lane-report-packet. First-touch at @18. No prior entry. Old-state: "soap-lane-contact" (the contact held it before delivery).
  Authority: prop:* studio. CLEAR. (Note: the actor:soap-lane-contact state change would be the contact fork's authority; studio fires the prop-holder change only.)

state:7 @20 (prop:oc-soap-lane-report-packet.content: nighttime-visitor-report -> precinct-pattern-sourcing-added):
  Reality: @20 "taylor-hebert-kl-122ac writes the precinct-pattern sourcing" — the packet's content now includes Taylor's precinct-pattern sourcing in addition to the original nighttime-visitor report. Canonical: this shapes what the sealed packet contains and where it routes. Persistent: the content stays through sealing at @21 and beyond. FIRE.
  Peak-bones co-citation: @20 is the scene-C peak bone (social_tether-antag +0.5). Co-citation expected. FIRE confirms.
  Held-against-turn check: @19 (opens packet) is the approach bone (held-against-turn). Correctly firing at @20 (the canonical content change), not @19 (the opening). Anti-pattern #7 (pre-empt/lag) avoided.
  Authority: prop:* studio. CLEAR.

state:8 @21 (prop:oc-soap-lane-report-packet.physical-condition: opened -> sealed):
  Reality: @21 "taylor-hebert-kl-122ac seals the packet" — the packet is sealed. Persistent: sealed state holds until it is opened by the recipient downstream. Strip test: without this, the canonical packet state remains "opened" — wrong. FIRE.
  Old-state: "opened" — established at @19 (opened from sealed; I did not fire @19 as a state-update per held-against-turn, but the physical act of opening at @19 means the packet IS open from @19-@20; the canonical pre-@21 state is "opened"). Old-state here is derivable from @19's action even without a state-update at @19; no drift issue.
  Authority: prop:* studio. CLEAR.

state:9 @22 (studio.time_of_day: afternoon -> end-of-day):
  Reality: @22 "taylor-hebert-kl-122ac enters the feed-station" — scene-D's opening marks the end-of-day accounting-close. The time-of-day advances from afternoon (scene-C was afternoon) to end-of-day. Canonical: this affects what Taylor does at the station and how the chapter closes. Persistent: end-of-day holds through @27. FIRE.
  Note: Taylor's physical re-entry at @22 ("enters") with an `enters` verb — if she was briefly outside the feed-station for the soap-lane contact meeting, this confirms her return for accounting. Transitional verb licenses the time-of-day advance entry. Authority: studio.* studio. CLEAR.

state:10 @23 (prop:oc-feed-ledger.jarvis-entry: open -> closed):
  Reality: @23 "closes the Jarvis entry" — the Jarvis accounting arm in the ledger closes. Persistent. FIRE.
  Per-beat-decomposition: the four arm-closes (@23-@26) are distinct consecutive field-flips on the feed-ledger. Rubric: "multi-beat compound transitions decompose into per-beat entries on the beat the field actually flips." Each arm-close is one field-flip at its beat. All four are real canonical facts. Authority: prop:* studio. CLEAR.

state:11 @24 (prop:oc-feed-ledger.oswyn-entry: open -> closed):
  Same rationale as state:10. FIRE.

state:12 @25 (prop:oc-feed-ledger.contacts-entry: open -> closed):
  Same rationale. Peak-bones co-citation: @25 is the scene-D peak bone (social_tether-prot-rise +0.5). Co-citation expected at this bone. FIRE.

state:13 @26 (prop:oc-feed-ledger.arrangement-entry: open -> closed):
  Same rationale. FIRE.

state:14 @27 (prop:oc-feed-ledger.condition: open -> closed):
  Reality: @27 "sets the stylus down" — the accounting session ends; the ledger closes. Persistent: ledger closed at chapter-close (b01c12 Phase 0 will inherit closed). Strip test: without this, the ledger's condition remains "open" canonically — wrong. FIRE.
  Terminal bone: @27 is the chapter's terminal image. The ledger-close is the canonical fact the chapter closes on. Authority: prop:* studio. CLEAR.

---

## Decisions-not-fire log (strip-test failures or rubric rejects)

@2 (prop:oc-jarvis-packet.physical-condition: sealed-flat -> folded-for-transit): Jarvis folds the covering-sheet. Reality axis: folding is a real physical change. Strip test: removing this entry leaves the packet's canonical record as "sealed + dry" (from b01c10). The fold is a handling/transport act by Jarvis — fine-grain intermediate. No downstream chapter needs to distinguish "sealed-flat" from "sealed-folded" for Jarvis's delivery. Anti-pattern #10 (stylistic noting). REJECT.

@3 (Oswyn presses cart-frame — grain-measures junction): Actor act (Oswyn's actor state); no studio/prop target. REJECT for studio authority.

@4 (wool-dyer returns observation): Actor dialogue/exchange; no studio/prop target. REJECT.

@7 (stylus lifts — withhold completion): No additional prop state change beyond @6's lane-pattern-only entry. The withhold-as-bodily-fact is substance content, not a studio/prop field-flip. Anti-pattern #10 (stylistic noting of the withhold's physical completion). REJECT.

@8 (cloth-merchant opens back-worktable): studio.cloth-merchant-shop condition. Reality: the worktable-open is real. Strip test: the burn at @11 remains legible without this env-state entry — the action is self-contained. Scene-local env condition (the worktable-open does not persist into downstream chapters; no canonical write-back value). Reality axis: fails persistence past the chapter. REJECT. (Loc-state carries the worktable-open as a place-anchor condition note; no need for state-updates duplication.)

@9 (messenger crosses threshold): studio.cloth-merchant-shop.visitors. Scene-local visitor presence — the messenger departs within the scene (or at least does not persist into downstream chapters). Persistence test fails: the visitor is ephemeral. REJECT.

@10 (cloth-merchant lifts folded-paper): prop:oc-cloth-merchant-paper.holder (worktable-surface -> cloth-merchant-hand). Held-against-turn: @10 is approach-to-peak in a rising rhythm-shape zone adjacent to @11 (peak bone). Canonical state-update co-citation forbidden at approach bone. REJECT per rubric anti-pattern #3.

@12 (iron-dish receives ash): prop:oc-iron-dish.contents (empty -> paper-ash). Reality: the ash-in-dish is real. Strip test: removing this entry — does any downstream canonical state depend on the iron-dish's ash contents? The insect-feed perceives thermal and smoke from the dish (@13/@14) but these are within the chapter. No downstream reference to iron-dish.contents after @14. Persistence: the ash persists physically, but its canonical significance ends at @14. This is scene-local state that does not require canonical write-back. The @4 calibration anchor s01e01:24 (stylus stops — NONE, because no field changes) is analogous: the iron-dish receiving ash is real but does not change a tracked field with downstream relevance. REJECT.

@13/@14 (insect-feed thermal-shift / smoke-curl): Instrument subject ("the insect-feed") — not a studio or prop target. Feed-relay perception beats; actor:taylor* territory for knowledge updates (actor fork's authority). No studio/prop field change at @13/@14. REJECT.

@15 (cloth-merchant squares bolt-ticket): prop:oc-bolt-ticket.status. Strip test: the bolt-ticket squaring is standing protocol / routine return to business. No downstream canonical relevance. Anti-pattern #10. REJECT.

@17 (soap-lane-contact crosses cross-lane): Actor movement (soap-lane-contact's actor state — not studio's authority). Studio: no persistent env change at the cross-lane with downstream relevance. REJECT.

@19 (taylor opens packet): prop:oc-soap-lane-report-packet.physical-condition: sealed -> opened. Held-against-turn: @19 is the approach bone adjacent to @20 (peak bone, social_tether-antag +0.5). In scene-C's rising rhythm-shape, @19 is held-against-turn class. Canonical state-update co-citation forbidden. REJECT per rubric anti-pattern #3. (Note: the old-state for @21's entry — "opened" — is derivable from @19's physical act; no drift.)

---

## Prop-state projection at b01c11 chapter-close

prop:oc-jarvis-packet.holder: jarvis-coin-kl-courier (@1; in transit)
prop:oc-feed-ledger.condition: closed (@27; persistent)
prop:oc-feed-ledger.source-field-entry: lane-pattern-only (@6; wool-dyer-name withheld; permanent)
prop:oc-feed-ledger.cloth-merchant-entry: timestamp-marked (@16; permanent)
prop:oc-feed-ledger.jarvis-entry: closed (@23)
prop:oc-feed-ledger.oswyn-entry: closed (@24)
prop:oc-feed-ledger.contacts-entry: closed (@25)
prop:oc-feed-ledger.arrangement-entry: closed (@26)
prop:oc-cloth-merchant-paper.physical-condition: burned (@11; destroyed — prop exits canonical tracking)
prop:oc-soap-lane-report-packet.holder: taylor-hebert-kl-122ac (@18)
prop:oc-soap-lane-report-packet.content: precinct-pattern-sourcing-added (@20)
prop:oc-soap-lane-report-packet.physical-condition: sealed (@21; persistent into b01c12)
studio.time_of_day: end-of-day (@22; chapter-close)
All b01c10 carry-forward entries unchanged (studio.spatial_layout.lane-junction-patrol: Gold-Cloak-pair-posted; studio.fauna_sense_status.lower-gate-road-coverage: corwick-absent; all b01c09 baseline entries)

---

## Margit referrals

prop:oc-cloth-merchant-paper.card.md — new prop; no warehouse card; oc-slug; burns at @11; exits tracking. Priority: before stitch.
prop:oc-soap-lane-report-packet.card.md — new prop; no warehouse card; oc-slug; introduced @18, sealed @21, persists into b01c12. Priority: before b01c12.
prop:oc-feed-ledger field-extensions (source-field-entry, cloth-merchant-entry, four arm-close fields) — new fields on existing oc-prop established in b01c10; schema extension needed. Priority: before review verdict.
prop:oc-cloth-merchant-paper (from oc-cloth-merchant-shop) — the shop itself may need a location card for margit review (carries the worktable, iron-dish, rushlight props). Priority: before stitch.

---

## Flagged seams for R2

SEAM-C11-ENV-001: prop:oc-cloth-merchant-paper — the paper that is burned. Its physical condition before burning (shape, seal-condition, whether it arrived via the off-hour messenger) is inferred from context. The old-state "intact" is the best canonical assumption but has no prior entry establishing it. R2 reviewer should confirm or request a @10 first-touch entry (which would require a frugality exception to the held-against-turn rejection at @10).

SEAM-C11-ENV-002: prop:oc-soap-lane-report-packet — first-touch at @18. The packet's prior state (sealed, held by contact) is inferred from the delivery act. No prior chapter entry on this prop. Old-state "soap-lane-contact" for holder at @18 is logically entailed by the delivery but has no prior state-updates anchor. R2 reviewer should confirm first-touch logic is sufficient or request a margit card that establishes the prop's prior state.

SEAM-C11-ENV-003: studio.time_of_day advance at @22 (afternoon -> end-of-day). The time-of-day for scene-C was "afternoon" (from scene-map). Was studio.time_of_day explicitly set to "afternoon" at the b01c11 scene-C open? No scene-C place-anchor fired on time-of-day in this chapter (loc-state:4 @17 only anchors the soap-lane location; no time-of-day-advance entry between scene-A morning and scene-D end-of-day). The afternoon old-state at @22 is inferred from the scene-map "early afternoon" for scene-C. R2 reviewer should confirm this inference chain is adequate or request a time-of-day state-update at the scene-B/C transition.

SEAM-C11-ENV-004: the four arm-close fields on prop:oc-feed-ledger (jarvis-entry, oswyn-entry, contacts-entry, arrangement-entry) were "open" at the start of scene-D. The old-state "open" for all four is inferred from the accounting-in-motion posture (@22) — there is no prior state-update explicitly setting these fields to "open." The accounting-open is established at @5 (ledger.condition: open) and the fields are activated by the day's circuit work (scenes A-C). R2 reviewer should confirm that the ledger.condition = open at @5 is sufficient to establish these arm-entry fields as open, or whether individual arm-open state-updates should be back-filled from scenes A-C (e.g., jarvis-entry opens when Jarvis takes the packet at @1; oswyn-entry opens when Oswyn's observation is received; etc.).

# source: taylor-hebert-kl-122ac-b01-c11
facet: state-updates
episode: b01-c11
author: taylor-hebert-kl-122ac (impersonator, facet-authoring override)
character: taylor-hebert-kl-122ac
# field-extension: social_tether_antag_axis (new axis-field for b01c11 antag-tether tranche tracking; relational-state aspect per Otto-leverage accumulation, cl-antag-d10; not a perception)
# field-extension: withholding_pattern (relational withhold-pattern; second consecutive withhold @7->@16 establishes the substrate-split as standing pattern; load-bearing per c11 discipline; not mood)
---
15 @6 actor:taylor-hebert-kl-122ac.social_tether_prot_rise_axis: 3 -> 3.5
16 @16 actor:taylor-hebert-kl-122ac.social_tether_antag_axis: 0 -> 0.5
17 @16 actor:taylor-hebert-kl-122ac.withholding_pattern: single-instance -> established
18 @20 actor:taylor-hebert-kl-122ac.social_tether_antag_axis: 0.5 -> 1.0
19 @25 actor:taylor-hebert-kl-122ac.social_tether_prot_rise_axis: 3.5 -> 4
