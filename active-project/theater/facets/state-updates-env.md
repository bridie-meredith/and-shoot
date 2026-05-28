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
# - state:3 @16: field-extension: prop:oc-enforcement-report-entry.state (new prop; first-touch baseline)
# - state:4 @18: field-extension: prop:oc-courier-body-map.state (new prop; first-touch baseline)
# - state:7 @27: extends state:4 on same prop field; prop established at @18

1 @1 studio.active_location: oc-stitch-house-lane -> the-rushwick
2 @3 studio.coverage_active_range: four-ward-complete -> rushwick-included
3 @16 prop:oc-enforcement-report-entry.state: absent -> filed-with-jarvis # field-extension: prop:oc-enforcement-report-entry.state (new prop; first-touch baseline; oc-card pending margit)
4 @18 prop:oc-courier-body-map.state: absent -> initiated # field-extension: prop:oc-courier-body-map.state (new prop; first-touch baseline; cf-d10 thread anchor; oc-card pending margit)
5 @20 studio.active_location: the-rushwick -> taylor's-lodging
6 @20 studio.time_of_day: morning -> evening
7 @27 prop:oc-courier-body-map.state: initiated -> filed
