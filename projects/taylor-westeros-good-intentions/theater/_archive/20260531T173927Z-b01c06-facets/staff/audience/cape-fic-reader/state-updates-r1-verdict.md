---
reviewer: cape-fic-reader
facet: state-updates
target: b01c04
mode: facet-adversarial (Phase 5b)
timestamp: 2026-05-27
verdict: revise
---

# Cape-Fic-Reader — State-Updates Adversarial Review (b01c04)

## Reading stance

I'm here for the canonical write-back layer — the actual board-state changes. What I need from state-updates is simple: it has to tell me what changed, when, and whether the facet knows its own rules. I read this like a fight choreographer watching a scene where powers get used: if the established costs get honored, I lean forward. If a flip fires on a bone where nothing actually flipped, I flag it. If the old-value is wrong, the whole chain downstream is corrupt and I don't care how nice the prose will be.

I have the auditor's Phase 5 report alongside me. The mechanical scan caught faults 001-008 and eleven flags. The seams the scan can't reach — whether the field-extension cluster holds on hostile reading, whether the compound value on Wren's knowledge entry is clean, whether the carve-out at 36% env-density is load-bearing or a rationalization — those are mine.

---

## Entry-level callouts

**[state-updates:1] @1 — chapter-open time-of-day reset**

`studio.time_of_day: third-bell-noon → first-bell-morning`

Chapter-close-to-chapter-open delta. The canonical clock has to land somewhere. Legitimate write-back. The @9 back-citation of this entry (state:1 pulled as context into the acceptance peak) is non-standard but produces no contradiction — auditor flag-011 correctly calls it advisory. Accept.

**[state-updates:3,4,7] @15, @22, @27 — coverage_active_range field-extension triple**

`studio.coverage_active_range: [progressive geographic expansion across three bones]`

Three fires on a field that did not exist before this chapter. Field-extension protocol applies; carve-out preamble is present; per-entry annotations are in the file. My hostile read: is `coverage_active_range` a genuine environment-observable fact, or is it Taylor's capability tracking wearing a studio costume?

Author's defense: `actor:taylor.capability` tracks deployment scale; `studio.coverage_active_range` tracks which ward-zones are under live feed as an env-observable fact. The distinction is real but strained — if Taylor goes down mid-chapter, `coverage_active_range` collapses with her. The field tracks Taylor's operational status expressed as environmental footprint. Studio authority is thin at the boundary.

But the alternative is worse: pushing this into `actor:taylor.capability` loses the geographic specificity the ward-expansion arc requires. Structural necessity justifies the extension. The mechanical scan passed the carve-out preamble. Accept with notation — the authority boundary is strained but the extension is defensible.

**[state-updates:23,24] @9 — dual peak-bone fire (position_in_kl + arrangement-state)**

`actor:taylor.stats.position_in_kl: smallfolk-anonymous → named-conduit-at-courier-tier`
`actor:taylor.knowledge.arrangement-state: licensed-exception-considered → licensed-exception-active`

@9 is the acceptance peak. Scene-map marks it peak-bones-class for scene-A; strong-expect satisfied. Both changes persistent past @9. Strip test passes both independently — without these fires, Taylor carries wrong state through the remainder of the chapter. The `position_in_kl` jump is large (smallfolk-anonymous to named-conduit-at-courier-tier in one bone), but peak-bones are allowed to carry consequence-class changes. Accept.

Converges with: auditor pass-004 — NI co-citation via narrator:3 @9 satisfied. Contract held.

**[state-updates:25] @15 — capability_axis +1 first fire**

`actor:taylor.stats.capability_axis: 2 → 3`

@15 bone: "extends the insect-range." Transition-verb. Field persists to @27. Strip test passes — without this entry, @27's +1 fires from 2 to 4 (wrong). NI co-citation via narrator:11 @15. Accept.

**[state-updates:26] @18 — oswyn-as-unknowing-coverage-node knowledge flip**

`actor:taylor.knowledge.oswyn-as-unknowing-coverage-node: absent → present`

@18 bone: "the insect-feed returns oswyn." Insect-feed finds him. Irreversible knowledge — once seen in the feed, persists. Field-extension justified. Strip test passes. NI co-citation via narrator:4 @18. The cull-log correctly deleted the corresponding `actor:taylor.location` @14 entry to avoid density-on-flat contamination — the oswyn-knowledge flip is different register than a location echo. Accept.

**[state-updates:27] @22 — wren-in-coverage-map knowledge flip — REVISE TRIGGER**

`actor:taylor.knowledge.wren-in-coverage-map: absent → present-but-outside-report`

@22 bone: "the insect-feed returns wren-stitch-maker." Taylor finds Wren in the coverage grid. Here is the seam the mechanical scan missed.

The field value is compound: `present-but-outside-report`. The "outside-report" component is not a knowledge registration — it is an active exclusion decision. Wren is in the feed AND Taylor has decided not to include her in the intelligence product she is about to hand Jarvis. Those are two separable facts with separable canonical consequences.

Strip test on the compound value: if this entry fires as written, the showrunner's canonical write-back records a single field that merges registration with decision. Downstream chapters that need to distinguish "Taylor knew Wren was in the feed" from "Taylor chose to exclude Wren" cannot do so. This matters concretely: if Wren's faction status changes, if Wren is later endangered by something Taylor's feed spotted, if an antagonist discovers that Taylor knew and didn't report — the showrunner needs the two facts separated.

The rubric's frugality axis says one entry per real change. The compound value packs two changes into one field. The field-extension protocol covers the field's existence, not the compound encoding of a decision inside a knowledge-state value. The carve-out preamble does not address this.

This is not in the auditor's findings. The auditor flagged SEAM-WREN-ANCHOR-DISCIPLINE as a cross-facet concern; it did not examine the compound value shape.

Minimum fix: split into two entries.
- At @22: `actor:taylor.knowledge.wren-in-coverage-map: absent → present` (the knowledge registration — she's in the feed)
- At @31 or @33: `actor:taylor.knowledge.wren-report-inclusion: na → excluded` (the exclusion decision — realized at the delivery bone, not the observation bone)

The second entry is a field-extension (new knowledge sub-field), but it passes the field-extension protocol: tracked-state-aspect, not mood or register, load-bearing for handoff_out (the chapter goal explicitly calls this "load-bearing future-cost-collateral plant"). Flagging for fixer.

**[state-updates:28] @27 — capability_axis +1 second fire**

`actor:taylor.stats.capability_axis: 3 → 4`

Mirrors @15. Four-ward-complete extension. +2 cumulative = chapter contract target. Strip test passes. NI co-citation via narrator:13 @27. Accept.

**[state-updates:29] @31 — intelligence-routing-state flip**

`actor:taylor.knowledge.intelligence-routing-state: dormant → routing-to-jarvis-active`

@31 bone: "taylor delivers the report-sheet." Routing-state flips from dormant to active — operational realization of the @9 arrangement. Distinct from `arrangement-state` (@9 = the permission flip; @31 = the operational flip). The cull-log correctly defends deleting the @31 arrangement-state re-fire as parasitic. NI co-citation via narrator:7 @31. Accept.

**[state-updates:10,11] @31, @32 — prop:oc-report-sheet.holder chain**

`prop:oc-report-sheet.holder: taylor → in-transit-yard-air → jarvis-coat`

Two-bone decomposition, one entry per field flip. Correct per rubric's multi-beat compound transition rule. oc- slug present in carve-out preamble; explicit scene presence. Studio authority. Accept.

**[state-updates:22] @36 — exposure_risk flip (Jarvis)**

`actor:jarvis-coin-kl-courier.stats.exposure_risk: latent → operational`

Jarvis exits carrying the report. Exposure state flips. Persists past chapter. Jarvis fork writes Jarvis state — correct authority. No NI co-citation required (non-POV actor). Accept.

**Forward-citation faults confirmed (auditor fault-002, fault-003):**

`[state:2]` on proto-line @9 is a forward-citation — state:2 anchors at @13 (pig-tallow-lane location; scene-B open), four bones after @9 (scene-A acceptance peak). The stitcher rendering @9 receives pig-tallow-lane as active location context while the scene is at the cooper's yard. Spatial contradiction in rendered prose. Hard fault — strip `[state:2]` from proto-line @9.

`[state:5]` on proto-line @22 is a forward-citation — state:5 anchors at @25 (day-2 temporal transition), three bones after @22 (scene-B, day-1 morning). The Wren-anchor-discipline bone receives next-day temporal context at a bone that is on day-1. Hard fault — strip `[state:5]` from proto-line @22.

Both faults require cite-index regeneration after removal. No dispute with auditor on these.

---

## Seams the mechanical scan missed

**SEAM-A: wren-in-coverage-map compound value encodes a decision, not just a state registration.**

Called out at entry 27 above. This is the primary seam. The `present-but-outside-report` value packs a knowledge registration and an active exclusion decision into a single canonical field value. The canonical consequences downstream are separable; the current encoding does not preserve that separation. Revise trigger.

**SEAM-B: intelligence-routing-state @31 vs arrangement-state @9 — two names for the same flip?**

Hostile read: both track the licensing arrangement for intelligence routing. Author's defense: arrangement-state tracks the moral_framework license (permission layer); routing-state tracks first-upward-routing operational status (actual use of that license). @9 = permission flip; @31 = operational flip. The chapter structure supports the distinction — you can hold a license without activating it. Accept. Not a revise trigger.

**SEAM-C: @36 peak-bone — Taylor's silence is correct.**

The Taylor slice SKIP-log defends SKIP @36 because the world-axis pivot (intelligence enters Otto's channel) is studio's or world-axis authority, not Taylor's actor-state. Taylor is stationary from a canonical-state perspective. State:12 (actors_in_yard update) and Jarvis's exposure_risk entry cover @36 with legitimate state-update fires. Taylor's silence at the world-axis bone is rubric-correct. Not a revise trigger.

**SEAM-D: cull-log deletions — all six survive hostile review.**

DEL @3, @14, @26 (actor:taylor.location — density-on-flat; studio carries location): correct.
DEL @15, @27 (actor:taylor.stats.coverage_wards — invented field; capability_axis numeric carries): correct. The coverage-set extension would break bone-level magnitude anchoring.
DEL @31 (arrangement-state re-fire — parasitic against routing-state flip): correct.
No incorrect culls found.

---

## Verdict breakdown

**Revise trigger — SEAM-A: entry 27 compound-value encoding**

`actor:taylor.knowledge.wren-in-coverage-map: absent → present-but-outside-report` at @22 merges a state registration with an active decision in one canonical field value. The showrunner cannot distinguish "Taylor knew Wren was in the feed" from "Taylor chose not to report Wren" without the separation. Split into: `wren-in-coverage-map: absent → present` at @22, and a new `wren-report-inclusion: na → excluded` (or equivalent) at @31. Fixer action required.

**Forward-citation faults (auditor fault-002, fault-003) — confirmed hard faults**

`[state:2]` stripped from proto-line @9. `[state:5]` stripped from proto-line @22. Cite-index regenerated after both removals. These are cite-graph faults in the proto-lines file, not state-updates body faults.

**Everything else holds**

The capability-axis double-fire is earned. The prop handoff chain is correctly decomposed. The env-slice density carve-out is structurally justified on a per-author-class reading. The four knowledge-* field-extensions on Taylor are collectively defensible by structural necessity. The actors_in_yard tracking is accurate. The Jarvis exposure_risk flip is legitimate. The cull-log is clean.

Note for downstream: the field-extension cluster on Taylor (four new knowledge-* sub-fields in one chapter) is bulky. If this pattern recurs in b01c05+, a margit referral to formalize the knowledge sub-schema is appropriate. Not a current revise trigger — downstream watch item.

---

VERDICT: revise

Revise targets:
1. Entry 27 — split `wren-in-coverage-map: absent → present-but-outside-report` into registration entry at @22 (`wren-in-coverage-map: absent → present`) and decision entry at @31 (`wren-report-inclusion: na → excluded` or equivalent field-extension).
2. Proto-line @9 — strip `[state:2]` forward-citation.
3. Proto-line @22 — strip `[state:5]` forward-citation.
4. Cite-index — regenerate after items 2 and 3.
