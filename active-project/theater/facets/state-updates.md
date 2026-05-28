---
facet: state-updates
sources: [b01-c05-taylor-hebert-kl-122ac, env-b01-c05]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: b01-c05-taylor-hebert-kl-122ac
facet: state-updates
episode: b01-c05
author: taylor-hebert-kl-122ac (impersonator, facet-authoring override mode)
scope: actor:taylor-hebert-kl-122ac.* only (studio + props authored by studio fork)
---

# rubric-carve-out — field-extensions for c05 recognition apparatus
#
# rubric-state-updates.md (design/shoot-v2/rubric-state-updates.md) § Field-extension protocol
#
# Carve-out scope: three new fields on actor:taylor-hebert-kl-122ac
#   (a) stats.political_register_prot_axis — already canonical in state.md, scalar move
#   (b) discipline_state.neutral-instrumental-read — new field-extension
#   (c) knowledge.body-map.rushwick-courier — new field-extension under knowledge.body-map
#   (d) knowledge.courier-body-record — new field-extension (record-state analog to s01e01 anchor)
# Carve-out rule: each extension documented inline; each defensible as tracked-state aspect
#   (knowledge, discipline-state, exposure-state ARE tracked per rubric ACCEPT signatures;
#   mood/register/voice-tone are NOT — none of these are those).
# Coverage justification: the c05 chapter-goal is the apparatus-level foreclosure of neutral-
#   instrumental reading; without these fields the canonical write-back surface cannot record
#   the irreversible move the chapter exists to deliver. Margit referral to add these to the
#   card schema is the appropriate downstream cleanup; the c05 facet fires under extension.
#
# Per-entry annotations:
# - state:2 @28: field-extension discipline_state.neutral-instrumental-read (new field; tracked-state aspect — disability-of-read-mode, not perception)
# - state:3 @29: scalar-axis move on existing stats.political_register_prot_axis (canonical field, no extension); paired with discipline-state foreclosure on same beat per cross-author dependency
# - state:1 @21: field-extension knowledge.body-map.rushwick-courier (new sub-key under knowledge.body-map; tracked-state aspect — body-map composition)
# - state:4 @31: field-extension knowledge.courier-body-record (new field; tracked-state aspect — record-state knowledge, analog to s01e01:64 actor:taylor.knowledge.record-state anchor)

1 @21 actor:taylor-hebert-kl-122ac.knowledge.body-map.rushwick-courier: absent -> present-unnamed-figure-junction-corner-22nd
2 @28 actor:taylor-hebert-kl-122ac.discipline_state.neutral-instrumental-read: available-for-rushwick-content -> apparatus-failing-color-persists-across-retry
3 @29 actor:taylor-hebert-kl-122ac.stats.political_register_prot_axis: 1.0 -> 2.5
4 @29 actor:taylor-hebert-kl-122ac.discipline_state.neutral-instrumental-read: apparatus-failing-color-persists-across-retry -> foreclosed-for-rushwick-content
5 @31 actor:taylor-hebert-kl-122ac.knowledge.courier-body-record: absent -> filed-as-cf-d10-thread-anchor

# source: env-b01-c05
facet: state-updates
episode: b01c05
author: studio
scope: environment + prop (no actor-state; actor:taylor.* is dialogue-writer fork authority)
---

# rubric-carve-out — field-extension for oc-prop targets pending margit cards
#
# design/shoot-v2/rubric-state-updates.md § Authority / Field-extension protocol
#
# Carve-out scope: entries targeting prop:oc-enforcement-report-entry and prop:oc-courier-body-map
# Carve-out rule: both are project-original props (oc-* slug class) with no card yet authored;
#   prop cards are pending margit referrals per studio state.md (SEAM-002 + SEAM-003).
#   Authority § "Studio may extend with oc-* for genuine project-originals, but extension must be flagged."
#   Each entry carries an inline # field-extension comment per rubric protocol.
# Coverage justification: oc-enforcement-report-entry is first-touched at @17 (filing event, irreversible
#   bureaucratic mutation; rubric calibration anchor: "irreversible bureaucratic / record / knowledge events
#   strongly expect a state-update entry"). oc-courier-body-map is first-touched at @21 (body-record initiation,
#   cf-d10 thread anchor; persists to b01c06+). Both props are tracked-state-aspects with genuine persistence.
#   Refusing on no-card-yet grounds would miss irreversible record-events the rubric explicitly flags for co-citation.
#
# Per-entry annotations:
#   state:3 @17: carve-out clause A — oc-enforcement-report-entry, field-extension, SEAM-002 pending
#   state:4 @21: carve-out clause B — oc-courier-body-map first-touch, field-extension, SEAM-003 pending
#   state:7 @31: carve-out clause B — oc-courier-body-map field-transition, SEAM-003 pending

6 @2 studio.location: oc-stitch-house-lane -> the-rushwick
7 @3 studio.coverage_active_range: four-ward-complete -> rushwick-included
8 @17 prop:oc-enforcement-report-entry.state: absent -> filed-with-jarvis # field-extension: state (new prop; first-touch @17; oc-card pending margit SEAM-002; irreversible filing event)
9 @21 prop:oc-courier-body-map.state: absent -> initiated # field-extension: state (new prop; first-touch @21; cf-d10 anchor; oc-card pending margit SEAM-003)
10 @23 studio.location: the-rushwick -> taylor-lodging
11 @23 studio.time_of_day: morning -> evening
12 @31 prop:oc-courier-body-map.state: initiated -> filed # field-extension: state (cf-d10 thread confirmed; SEAM-003 pending)
