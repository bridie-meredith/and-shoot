---
reviewer: cape-fic-reader
facet: state-updates
episode: b01-c01
cycle: r1
verdict: revise
date: 2026-05-25
---

# Cape-Fic Reader — State-Updates Adversarial Verdict

## Stance

Reads mechanically. State-updates is the write-back layer — wrong entries corrupt the board, and I track who knows what and what the state actually is at every beat. Lore leaks and invented knowledge are walkouts; invented fields that write fake values into canonical state are the same class of fault. Nine entries, nine targets.

## Per-entry reading

**[state-updates:1] @21 oswyn.location: mudway-alley-hook-district -> lane-mouth-of-rescue-site**

Bone 21: "oswyn takes the lane-mouth." Location genuinely changes. Persists through chapter close (handoff_out confirms Oswyn stationed at lane-mouth watching Taylor). Field is a real tracked-state field. Authority: oswyn fork. NI not required (non-POV). Back=Y in cite-index. Strip test: if the entry doesn't fire, Oswyn's canonical location stays wrong in downstream chapters. Passes all three axes.

`CORRECT`

**[state-updates:2] @26 oswyn.relationship_to_taylor: regular-contact-no-awareness-of-function -> categorized-known-unknown-witch-adjacent**

Bone 26: "oswyn lifts the chin." The comment defends this as a field-extension (relationship_to_taylor value-space extended to carry categorization-shift). Persistence: handoff_out specifies "Hook precinct knows the foreign woman who moved the crowd" — the categorization does persist. The field-extension is tracking a social-cognition state (awareness shift), which the rubric permits (knowledge, mask-state, exposure-state ARE tracked). Not mood, not register. The value format "categorized-known-unknown-witch-adjacent" is compound but names one state. Authority: oswyn fork, oswyn actor, non-POV.

The question: is "relationship_to_taylor" a legitimate extension or an invented-social-cognition field? The rubric's accepted extension examples include `knowledge.rider-departed` — a knowledge sub-field. This is structurally equivalent: Oswyn's knowledge/category of Taylor. The author documented the extension in the entry comment. I'll pass it under ceiling-defense: the categorization IS a persistent state change that the showrunner needs to track for downstream Oswyn scenes.

`CORRECT`

**[state-updates:3] @12 taylor.deployment-state: passive-subsistence-range -> active-crowd-yield-deployment**

Bone 12: "the insects propagate." The canonical axis-move anchor for capability+1. Field-extension: deployment-state as a tracked-state aspect of Taylor's insect-network posture. The rubric explicitly lists "deployment-state" as an example of a tracked-state aspect in the entry's own comment. The persistence note says "absolute through chapter close — deployment is acknowledged-active in handoff_out." Handoff_out confirms "capability rank 3 (one deployment)." Authority: taylor fork. NI co-citation at @12: narrator:4 is present (cite-index confirms co-citation). Cross-facet test passes.

But here's my concern: is deployment-state distinct from the capability_axis stat entry (state:4)? The rubric says one entry per real change. If deployment-state and capability_axis are two separate tracked fields that each genuinely change at @12, two entries are licit. The rubric's s01e01:48 example explicitly fires two entries on two targets at the same beat. I need to determine whether deployment-state and capability_axis track different things — they do: deployment-state is the operational posture (active vs. suppressed), capability_axis is the rank-tier. These are independent tracked fields.

`CORRECT`

**[state-updates:4] @12 taylor.capability_axis: 2 -> 3**

Bone 12: the canonical axis-move, substance_delta capability+1 at b01c01s02n06. NI co-citation: narrator:4 at @12, present. This is the entry I'm most suspicious of. The rubric says the field must exist on the target's state schema. `capability_axis` as a named field on `actor:taylor-hebert-kl-122ac`'s state.md — is that established?

The substance axes live in showrunner memory, not in actor state.md. The rubric's accepted fields are: position, inventory, knowledge.*, mask-state, exposure-state, posture, administrative-status — not axis ranks. The rubric's worked example at s01e01:48 fires `administrative-status` as a field-extension, but that is a genuine external-world bureaucratic status change. `capability_axis: 2 -> 3` is writing a substance tracking number directly into the actor's canonical state as if it were a real-world field.

I know this: there is a real change happening at @12 (deployment begins, capability-as-demonstrated rises). But `capability_axis` as a value-2-to-3 tracker is substance-layer infrastructure, not a canonical-state field on the actor. The right state-layer entry for the capability move at @12 is state:3 (deployment-state: passive -> active), which already fires. `capability_axis: 2 -> 3` is either a duplicate of what state:3 captures, or it is writing the substance contract's axis rank directly into actor state — which is an invented-field violation under anti-pattern #6 unless the actor's state.md contains a `capability_axis` field.

This is a genuine authority/field question. The entry passes reality (something real changed) but fails authority (the field may not exist on the actor's state.md schema, and if it does, it is the substance rank — which is showrunner memory's domain, not actor state-updates' domain).

**`FLAG: state:4 — possible invented-field (capability_axis rank as actor.state field); state:3 deployment-state already captures the same @12 change in a more defensible form. If capability_axis is a confirmed field on taylor-hebert-kl-122ac/state.md, this is correct; if not, this is anti-pattern #6.`**

`CONTESTED — authority/field verification needed`

**[state-updates:5] @17 taylor.posture: in-the-gap -> hands-up-mouth-shut-witness-facing**

Bone 17: "taylor lifts the hands." The hands-up posture persists from @17 through at least @22 (handoff language: "the foreign woman who made the opening with her hands up and her mouth shut"). Persistence is established. Field-extension: posture is explicitly listed as a tracked-state field in the rubric. The posture persists across multiple beats and is load-bearing (it's what the witnesses categorize and what the chunk text makes explicit).

BUT: the auditor's flag-021 is an unresolved finding — no NI or feeling co-citation at @17. The rubric says: "If the entry is `actor:<POV-character>.*`, narrator-interest co-citation on the same beat is REQUIRED. Absence = REJECT or flag back to narrator-interest author." The cite-index shows state:5 @17 back=Y co=[] — no co-citations at all. The NI file fires at @12 and @21; it is silent at @17.

This is not a "flag for consideration." The rubric is explicit: required, not recommended. The co-citation is absent. The rubric's cross-axis test says "If you cannot point to a narrator-interest entry at the same beat, REJECT or flag back to narrator-interest author."

**`CALLOUT: [state-updates:5] @17 — POV actor-state posture-shift; NI co-citation REQUIRED per rubric §cross-facet test but absent. Auditor flag-021 identified this gap and it was not remediated. The posture is real and persistent, the field-extension is defensible, but the cross-facet contract is broken. This entry cannot ship without an NI co-citation at @17 being added to interest-narrator.`**

`REJECT on cross-facet grounds`

**[state-updates:6] @21 taylor.social_tether_prot_axis: 1 -> 2**

Same question as state:4 but for social_tether_prot_axis. NI co-citation: narrator:5 is present at @21. The cross-facet co-citation requirement is satisfied (unlike state:5). The substance match: social_tether-prot-rise +1.0 at b01c01s03n04.

But same invented-field concern: social_tether_prot_axis as a rank-value field on the actor's state.md. If it doesn't exist on the actor's state schema, this is anti-pattern #6.

I'm less worried here because state:6 has co-citation and has the peak-bone (peak anchor @21) strongly expecting state-update per the rubric. But the field-on-schema question remains.

`CONTESTED — same authority/field concern as state:4; NI co-citation present which resolves one gap but not the schema-field gap`

**[state-updates:7] @24 taylor.body-orientation: facing-the-child -> facing-the-alley-mouth-away-from-stitch-house**

Bone 24: "taylor faces the alley-mouth." Field-extension: body-orientation as "the cardinal direction of attention." NI co-citation at @24: narrator:8 present. Feeling co-citation: feel:3 present. Persistence: "through chapter close" — handoff_out confirms "Taylor does not look toward the stitch-house."

The rubric's concern: is "body-orientation" different from "posture" (state:5), and is the cardinal-direction-of-attention a tracked state aspect? The entry's comment distinguishes it from posture ("this is the cardinal direction of attention"). The not-looking-toward-stitch-house is load-bearing for relational_anchor_status dormancy. It persists and it matters.

NI co-citation present. Field-extension documented. Persistence established. The strip test: without this entry, the showrunner doesn't have a canonical record that Taylor's orientation at chapter-close excludes the stitch-house — which matters for downstream chapters where Wren is in range.

`CORRECT`

**[state-updates:8] @26 taylor.ward-recognition: invisible-foreign-woman -> categorized-by-oswyn-as-something-other**

Bone 26: "oswyn lifts the chin." The comment says "the ward's category for Taylor." This field is on taylor's actor record. The auditor's flag-012 names the NI spine gap: no NI fires at @26.

The rubric's cross-facet test: POV actor-state shift on the POV character requires NI co-citation. Is ward-recognition a POV actor-state field? It's filed on actor:taylor. The rubric says "every `actor:<POV>.*` entry" — there are no carve-outs for externally-facing status fields. If it's on actor:taylor, NI co-citation is required.

No NI fires at @26. Auditor confirmed this as flag-012 (not remediated). Same structure as state:5 — the rubric says REQUIRED.

**`CALLOUT: [state-updates:8] @26 — POV actor:taylor field (ward-recognition) filed on POV actor without NI co-citation. Auditor flag-012 identified this; not remediated. Cross-facet contract broken. Same ruling as state:5.`**

Additionally: I question whether "ward-recognition" is tracking a real field or is a perception-side-effect-as-state. The rubric's anti-pattern: "the count of allies in the yard drops to one" — Taylor's perception of Oswyn's categorization is the same class of thing. The canonical state-change here is on Oswyn's awareness (state:2 already captures that). What state:8 captures is Taylor's awareness that the categorization happened — which is a knowledge change (`actor:taylor.knowledge.ward-category-for-self: unknown -> categorized-witch-adjacent`), not a "ward-recognition" field.

`REJECT: no NI co-citation + perception-side-effect-as-state concern`

**[state-updates:9] @27 wren.relational_anchor_to_taylor: nascent -> observation-traced-d01-deterrence**

Bone 27: "wren faces taylor." Field-extension: relational_anchor_to_taylor. Non-POV actor. No NI co-citation required. Does this field exist on wren's state schema? The value "nascent" suggests it was established at project-setup baseline (or initialized as nascent at chapter open). The entry changes it to "observation-traced-d01-deterrence."

Persistence: this is chapter-close, so it persists into b01c02. The handoff_out says "Wren has seen Taylor's face in the crowd; no exchange, no names" — consistent with the entry but the field name "relational_anchor_to_taylor" is a field-extension. The value "observation-traced-d01-deterrence" is odd — what does "d01-deterrence" mean? Is this a chapter-label (d01 = chapter 1 event)? The rubric expects field values to be canonical-correct and parseable by the showrunner. "d01-deterrence" reads as an internal authoring note, not a clean state value.

I'll pass this on reality grounds — the state change is real (Wren has seen Taylor; her relational status has moved from nascent to observed). But the value format is sloppy. The "d01-deterrence" suffix is not a clean state descriptor; it is an authoring annotation embedded in a state value.

`CORRECT (with note: value format "observation-traced-d01-deterrence" contains an authoring annotation; prefer "observation-traced" as the clean state value)`

## Aggregated per-entry verdicts

| Entry | Verdict |
|-------|---------|
| state:1 @21 oswyn.location | CORRECT |
| state:2 @26 oswyn.relationship_to_taylor | CORRECT |
| state:3 @12 taylor.deployment-state | CORRECT |
| state:4 @12 taylor.capability_axis | CONTESTED (field-on-schema) |
| state:5 @17 taylor.posture | REJECT (missing NI co-citation) |
| state:6 @21 taylor.social_tether_prot_axis | CONTESTED (field-on-schema) |
| state:7 @24 taylor.body-orientation | CORRECT |
| state:8 @26 taylor.ward-recognition | REJECT (missing NI co-citation + perception-as-state) |
| state:9 @27 wren.relational_anchor_to_taylor | CORRECT (note: value format) |

## Callouts

**[state-updates:5] @17** — POV actor posture-shift, NI co-citation absent. Auditor flag-021, not remediated. Rubric says REQUIRED. Routes to narrator-interest author for co-citation add at @17, or entry must be removed pending that add.

**[state-updates:4] @12 + [state-updates:6] @21** — axis rank values written into actor state. If `capability_axis` and `social_tether_prot_axis` are confirmed fields on `active-project/actors/taylor-hebert-kl-122ac/state.md`, both entries are CORRECT. If they are not (i.e., they exist only in showrunner memory substance_delta), both are anti-pattern #6 invented-field violations. Verification required before these entries can ship.

**[state-updates:8] @26** — POV actor field, NI co-citation absent. Auditor flag-012, not remediated. Additionally, the field may be a perception-side-effect-as-state (Taylor's awareness of how the ward sees her) rather than a canonical state-change.

## Convergence-trace

- state:5 callout overlaps auditor flag-021 exactly.
- state:8 callout overlaps auditor flag-012 exactly.
- state:4 / state:6 field-on-schema question is a new audience attack not fully surfaced by the auditor (auditor pile-up review flag-020/019 treated these as CORRECT by ID). This is the seam the mechanical scan could not close: the auditor verified IDs and co-citations but did not verify whether `capability_axis` and `social_tether_prot_axis` are actual fields on the actor's state.md file.

## File-level curve assessment

The curve is consistent with rising dramatic_shape. Entries concentrate at @12 (scene-B peak), @17 (scene-B close), @21 (scene-C peak), @24/@26 (trailing edge), @27 (chapter-close). Scene-A is correctly silent. The env carve-out is well-defended. Target diversity: two actor targets (taylor, oswyn) + one wren entry. The absence of studio.* and prop.* is defended by the env carve-out. No density-on-flat violation. Curve shape: PASS conditional on the entry-level findings being resolved.

## Verdict

**REVISE**

Two REJECT entries (state:5, state:8) — both on cross-facet NI co-citation grounds. Two CONTESTED entries (state:4, state:6) — on field-on-schema grounds requiring verification. Any one of these failing is sufficient for revise under the facet-adversarial mode.

The facet cannot ship with state:5 and state:8 in their current form. The state:4/state:6 question must be resolved by verifying the actor's state.md.
