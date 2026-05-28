---
facet: state-updates
sources: [env, taylor-hebert-kl-122ac]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates (env)
episode: b01c05
author: studio
scope: studio.* and prop:oc-* entries only — actor:* entries authored by per-character dialogue-writer fork
---

# rubric-carve-out — oc-slug prop field-extensions
#
# design/shoot-v2/rubric-state-updates.md § Field-extension protocol
#
# Carve-out scope: prop:oc-enforcement-report-entry.* and prop:oc-courier-body-map.*
# Carve-out rule: Neither prop has an authored card in cards/props/ or active-project/warehouse/ yet
#   (Rushwick oc-cards are margit parking-lot SOFT per /and-write Phase 7 emit note). Studio authors
#   these as project-original props under the oc-* slug convention with field-extension notation on each
#   entry. Fields used: .state (tracked record-state; matches the pattern of prop:oc-report-sheet.state
#   established in b01c04). Frugality: both props are created (absent -> X) and mutated within this
#   chapter; the schema permits first-touch baseline authoring in this facet.
# Coverage justification: the enforcement-report-entry and courier body-map are bureaucratic
#   irreversible mutations called out in the dispatch brief and grounded in bones @16 and @18/@27
#   respectively. Refusing would leave load-bearing records absent from canonical memory.
#
# Per-entry annotations:
# - state:1 @2: anchor corrected from @1 to @2; @1 is world-before-protagonist establishing beat
#   (hill's stone skirt meets lane-mouth); location flip fires at @2 when Taylor enters (anti-pattern #7 avoided)
# - state:3 @16: field-extension: prop:oc-enforcement-report-entry.state (new prop; first-touch baseline)
# - state:4 @18: field-extension: prop:oc-courier-body-map.state (new prop; first-touch baseline)
# - state:5 @20: field name corrected from active_location to location (matches studio state.md schema)
# - state:7 @27: extends state:4 on same prop field; prop established at @18

1 @2 studio.location: oc-stitch-house-lane -> the-rushwick
2 @3 studio.coverage_active_range: four-ward-complete -> rushwick-included
3 @16 prop:oc-enforcement-report-entry.state: absent -> filed-with-jarvis # field-extension: prop:oc-enforcement-report-entry.state (new prop; first-touch baseline; oc-card pending margit)
4 @18 prop:oc-courier-body-map.state: absent -> initiated # field-extension: prop:oc-courier-body-map.state (new prop; first-touch baseline; cf-d10 thread anchor; oc-card pending margit)
5 @20 studio.location: the-rushwick -> taylor's-lodging
6 @20 studio.time_of_day: morning -> evening
7 @27 prop:oc-courier-body-map.state: initiated -> filed

# source: taylor-hebert-kl-122ac
facet: state-updates
episode: b01c05
author: taylor-hebert-kl-122ac (impersonator, facet-authoring mode)
scope: actor:taylor-hebert-kl-122ac entries only
---

8 @2 actor:taylor-hebert-kl-122ac.location: flea-bottom-hook-district -> the-rushwick
9 @3 actor:taylor-hebert-kl-122ac.feed-coverage.rushwick: not-yet-acquired -> active   # field-extension: feed-coverage.<ward> (operational coverage map per persona card §Action Menu)
10 @18 actor:taylor-hebert-kl-122ac.knowledge.body-map.courier: absent -> recurring-with-enforcement-attached   # field-extension: knowledge.body-map.<entity> (intelligence-routing tracked surveillance memory per persona card §Action Menu)
11 @20 actor:taylor-hebert-kl-122ac.location: the-rushwick -> taylor-lodging-room-floor
12 @21 actor:taylor-hebert-kl-122ac.evening-review.state: closed -> open   # field-extension: evening-review.state (nightly operational accounting procedure per persona card §Off-Screen Cadence)
13 @25 actor:taylor-hebert-kl-122ac.political_register_prot_axis: 1 -> 2.5   # cl-d05 first tranche; +1.5 axis-move; peak-bones; neutral-instrumentally-observant foreclosed
14 @26 actor:taylor-hebert-kl-122ac.evening-review.state: open -> closed
15 @27 actor:taylor-hebert-kl-122ac.knowledge.body-map.courier: recurring-with-enforcement-attached -> canonical-file-cf-d10-thread-open   # body-record canonical filing; cf-d10 thread confirmed open
