facet: state-updates-env / episode: b01-c15 / author: studio / ---

# rubric-carve-out — single-location chapter; no time-of-day disambiguation on scene-open (@1 fires both fields together
#
# design/shoot-v2/rubric-state-updates.md § Frugality / field-extension protocol
#
# Carve-out scope: @1 carries two entries (studio.location + studio.time_of_day) on the same bone
# Carve-out rule: multi-field fires on the same bone are licit per rubric §Frugality "one entry per
#   real change... if a beat changes multiple fields on the same target, multiple entries are licit"
# Coverage justification: @1 is the scene-open anchor; both location and time-of-day flip simultaneously
#   from c14 chapter-close (the-channel-station / evening) to c15 chapter-open (the-passage-adjacent-ward / morning)
#
# Per-entry annotations:
# - state:1 @1: two-field scene-open fire; rubric §Frugality explicitly licenses multiple entries per beat
#   when multiple fields change; no frugality conflict; licit.
# - state:2 @1: same bone as state:1; different target field (time_of_day vs location); licit.

# Field-extensions (new fields this chapter):
#   studio.ambient_conditions.thermal-rise-status (new sub-field; tracks Vhagar-backwash thermal event)
#   studio.fauna_sense_status.eastern-fringe-interference (new sub-field; tracks fringe thermal-noise condition)
#   studio.fauna_sense_status.feed-density (new sub-field; tracks scan-density state; carried from c15 baseline)
#   prop:oc-coverage-record (new oc-prop; Taylor's internal circuit coverage-record for this morning's session)
#   prop:oc-coverage-record.site-condition-entries.thermal-rise (new field on new prop)
#   prop:oc-coverage-record.eastern-boundary-entry (new field on new prop)
#   prop:oc-coverage-record.final-notation (new field on new prop)
#   prop:oc-coverage-record.condition (new field on new prop; tracks open/closed lifecycle)
# Margit referrals needed: prop:oc-coverage-record.card.md (new prop, 4 fields);
#   studio.ambient_conditions.thermal-rise-status (new field);
#   studio.fauna_sense_status.eastern-fringe-interference (new field);
#   studio.fauna_sense_status.feed-density (new field; reconcile with b01c12+ fauna_sense_status schema)

1  @1  studio.location: the-channel-station -> the-passage-adjacent-ward
2  @1  studio.time_of_day: evening -> morning
3  @12 studio.fauna_sense_status.feed-density: elevated-court-observation -> routine-scan
4  @22 prop:oc-coverage-record.site-condition-entries.thermal-rise: absent -> marked
5  @23 studio.ambient_conditions.thermal-rise-status: active -> normalized
6  @31 prop:oc-coverage-record.eastern-boundary-entry: absent -> written
7  @33 studio.fauna_sense_status.eastern-fringe-interference: active -> cleared
8  @36 prop:oc-coverage-record.final-notation: absent -> written
9  @37 prop:oc-coverage-record.condition: open -> closed
10 @38 studio.fauna_sense_status.feed-density: backwash-disrupted -> routine-coverage
11 @40 studio.time_of_day: morning -> afternoon
