# Fixer Log — 1d constraint-consistency check
session: 2026-05-09

---

## fault-001 — RESOLVED
fault: actor card cost curve diverges from warehouse cond-fauna-control-rules (10/20/30 vs 3/10/20 breakpoints)
scope: card
change: No edit required. cards/personas/taylor-hebert-jaehaerys.card.md already carries the correct child-body numbers (3–10 min headache, 10–20 nosebleed, 20+ blackout) in both the ambient_vs_directed NOTE (Stats block) and the Action Costs section. These match the warehouse card exactly. The provisioned copy in active-project/actors/ is a stub pointing to the library card and does not independently state the cost curve. Criterion met as-is.
criteria met: yes

---

## fault-002 — RESOLVED
fault: library cond-fauna-control-rules scoped to wrong project (taylor-hebert-westeros) with dead cross-references
scope: card
change: No edit required. cards/conditions/cond-fauna-control-rules.card.md already carries scope: library with no project field. Interaction Notes reference cond-westerosi-customary-authority-jaehaerys (correct 84 AC slug) and do not contain cond-impressment-census-120ac or the generic cond-westerosi-customary-authority. Criterion met as-is.
criteria met: yes

---

## fault-003 — RESOLVED
fault: library cond-no-parahuman-infrastructure and warehouse copy have inverted scope values; library body references 120 AC and taylor-hebert-westeros
scope: card
change: No edit required. cards/conditions/cond-no-parahuman-infrastructure.card.md already carries scope: library with no project field; title reads "Hard World-Law (Planetos)" with no taylor-hebert-westeros or 120 AC reference. active-project/warehouse/cond-no-parahuman-infrastructure.card.md already carries scope: project and project: taylor-hebert-jaehaerys. Criterion met as-is.
criteria met: yes

---

## fault-004 — RESOLVED
fault: both copies of condition-swarm-in-foreign-ecology contain dead cross-references (condition-language-barrier, condition-war-of-five-kings-riverlands); warehouse copy lacks project-scope metadata
scope: card
change: Library card (cards/conditions/condition-swarm-in-foreign-ecology.card.md) — confirmed no dead references present; Interaction Notes section already clean (scene-level use only). Warehouse copy (active-project/warehouse/condition-swarm-in-foreign-ecology.card.md) — two edits applied directly: (1) frontmatter updated from scope: library / no project field to scope: project / project: taylor-hebert-jaehaerys / overrides: condition-swarm-in-foreign-ecology; (2) dead Interaction Notes entries for condition-language-barrier and condition-war-of-five-kings-riverlands removed and replaced with a single era-correct entry referencing cond-westerosi-superstition-frame.
files changed: active-project/warehouse/condition-swarm-in-foreign-ecology.card.md
criteria met: yes

---

## fault-005 — RESOLVED
fault: Stage 4 age annotation in cond-suppression-policy-progression reads "Taylor age ~21" for 98–101 AC; correct is ~14–17
scope: card
change: No edit required. active-project/warehouse/cond-suppression-policy-progression.card.md Stage 4 header already reads "Taylor age ~14–17". cards/conditions/cond-suppression-policy-progression.card.md Stage 4 header carries no age annotation (not ~21). Neither copy contains the erroneous ~21 annotation. Criterion met as-is.
criteria met: yes

---

# Fixer Log — series-level audit
session: 2026-05-09

---

## series-fault-001 — RESOLVED
fault: series-plan.md Section 6 power-mechanics block referenced "10/20/30-minute" actor-card ceilings instead of correct child-body breakpoints "3/10/20-minute"
scope: line
change: No edit required. series-plan.md Section 6 power-mechanics project-decision sentence already reads "the 3/10/20-minute actor-card ceilings shift upward on a schedule season planning must specify." Confirmed against warehouse cond-fauna-control-rules.card.md (age ~9 active-control curve: 3 min headache onset, 10 min nosebleed onset, 20 min blackout risk). The correction was applied during Revision attempt 2 of the series plan. Criteria met as-is.
criteria met: yes

---

## series-fault-002 — RESOLVED
fault: series-plan.md Section 6 Laws listed unsuffixed cond-westerosi-customary-authority (120 AC, Harrenhal, impressment census) alongside the correct Jaehaerys variant
scope: line
change: No edit required. series-plan.md Section 6 Laws block contains only cond-feudal-hierarchy-law and cond-westerosi-customary-authority-jaehaerys. The unsuffixed slug is not present. memory.md series.laws block similarly contains only the Jaehaerys variant; no drift to correct there either. Criteria met as-is.
criteria met: yes

---

## series-fault-003 — RESOLVED
fault: memory.md missing schema-required fields: season-level chunk, episode-level chunk on all 8 episodes, and next_season_sketch
scope: line
change: No edit required. memory.md already contains: seasons[s01].chunk (two-sentence form drawn from series-plan.md S1 chunk); chunk fields on all eight episodes s01e01–s01e08 (verbatim from season-s01-plan.md episode chunks); next_season_sketch at s01 level (drawn from series-plan.md S2 chunk opening). All three missing fields per the audit finding are present and populated. Criteria met as-is.
criteria met: yes

---

## series-fault-004 — RESOLVED
fault: memory.md cast_roster and stage_elements used YAML comment syntax (slug # description) instead of schema-required mapping syntax (slug: description)
scope: line
change: No edit required. memory.md cast_roster entries already use mapping syntax (e.g., "- taylor-hebert-jaehaerys: lead — Taylor reborn ..."). stage_elements entries already use mapping syntax (e.g., "- loc-river-market-town: Fairstead — composite primary setting ..."). No comment-syntax entries present. Schema requires "- <actor-slug>: <one-line role description>" and both sections comply. Criteria met as-is.
criteria met: yes

---

# Fixer Log — season s01 Pass 2 constraint audit
session: 2026-05-09

## s01-fault-001 — RESOLVED
fault: ID 124 "taylor-hebert-jaehaerys holds the swallow neutral" — unlicensed holds on external fauna plus modifier
scope: line
change: Recast to "the swallow holds position" (fauna-direction expressed as the swallow's physical act; modifier stripped)
criteria met: yes

## s01-fault-002 — RESOLVED
fault: IDs 194, 264 "taylor-hebert-jaehaerys holds the fly" — unlicensed holds on directed fauna
scope: line
change: ID 194 recast to "the fly holds the basin rim"; ID 264 recast to "the fly holds the pen rail edge"
criteria met: yes

## s01-fault-003 — RESOLVED
fault: IDs 722, 797 "[subject] holds the bench edge" — stative grip on external object, outside narrow license
scope: line
change: ID 722 recast to "oc-craftsman-mother grips the bench edge"; ID 797 recast to "taylor-hebert-jaehaerys grips the bench edge"
criteria met: yes

## s01-fault-004 — RESOLVED
fault: IDs 258, 301, 560, 650, 820, 828 "[subject] holds the pace" — abstract noun as object, interiority
scope: line
change: IDs 258, 301, 650, 820, 828 converted to time-skip markers (content wiped). ID 560 not actioned — file already contains "holds the feet" at that ID (pre-existing fix).
criteria met: yes

## s01-fault-005 — RESOLVED
fault: IDs 635, 713 "[subject] holds the pause" — abstract duration as object, interiority
scope: line
change: IDs 635 and 713 converted to time-skip markers
criteria met: yes

## s01-fault-006 — RESOLVED
fault: IDs 490, 519 "taylor-hebert-jaehaerys holds the temple pressure" — internal sensation, interiority
scope: line
change: IDs 490 and 519 converted to time-skip markers
criteria met: yes

## s01-fault-007 — RESOLVED
fault: ID 79 "taylor-hebert-jaehaerys releases the radius check" — abstract cognitive act, interiority
scope: line
change: ID 79 converted to time-skip marker
criteria met: yes

## s01-fault-008 — RESOLVED
fault: ID 14 "taylor-hebert-jaehaerys holds the chin level" — "level" is an adverb/adjective modifier
scope: line
change: Stripped modifier; line now reads "taylor-hebert-jaehaerys holds the chin"
criteria met: yes

## s01-fault-009 — RESOLVED
fault: ID 53 "taylor-hebert-jaehaerys releases the angle" — abstract positional descriptor as object, interiority
scope: line
change: ID 53 converted to time-skip marker (delete option chosen; adjacent lines provide context)
criteria met: yes

## s01-fault-010 — RESOLVED
fault: ID 284 "oc-child-peer tilts the head again" — "again" is an adverb modifier
scope: line
change: Stripped modifier; line now reads "oc-child-peer tilts the head"
criteria met: yes

## s01-fault-011 — RESOLVED
fault: ID 191 "septon-rowan points the finger at the line" — prepositional phrase of direction is padding
scope: line
change: Stripped prepositional phrase; line now reads "septon-rowan points the finger"
criteria met: yes

## s01-fault-012 — RESOLVED
fault: IDs 219, 428 "oc-craftsman-mother waits" — stative verb
scope: line
change: IDs 219 and 428 converted to time-skip markers (delete default per criteria)
criteria met: yes

## s01-fault-013 — RESOLVED
fault: IDs 300, 556 "the square fills with [midday/morning] traffic" — environment-state assertion
scope: line
change: IDs 300 and 556 converted to time-skip markers
criteria met: yes

## s01-fault-014 — RESOLVED
fault: ID 750 "the lane empties" — environment-state description
scope: line
change: ID 750 converted to time-skip marker
criteria met: yes

## s01-fault-015 — RESOLVED
fault: IDs 28, 71 "taylor-hebert-jaehaerys releases the fly/moth" — cognitive/directive act on swarm-controlled fauna
scope: line
change: ID 28 recast to "the fly lifts from the ink-pot rim"; ID 71 recast to "the moth departs the vent"
criteria met: yes

## s01-fault-016 — RESOLVED
fault: ID 249 "taylor-hebert-jaehaerys releases the pen grip" — "pen grip" is abstraction-as-phrase
scope: line
change: Recast to "taylor-hebert-jaehaerys releases the pen"
criteria met: yes

## s01-fault-018 — RESOLVED
fault: ID 439 "oc-craftsman-father advances the queue" — abstraction-as-object
scope: line
change: Recast to "oc-craftsman-father steps forward"
criteria met: yes

## s01-fault-020 — RESOLVED
fault: IDs 10, 432, 903 "the swarm-sense fills the radius" — internal cognitive faculty as subject, interiority
scope: line
change: IDs 10 and 432 converted to time-skip markers. ID 903 not present in file (pre-existing gap between 900 and 904); treated as already resolved.
criteria met: yes

## s01-fault-021 — RESOLVED
fault: IDs 158, 262, 819 "the swarm-sense maps the [location]" — perception/cognitive verb on internal faculty
scope: line
change: IDs 158, 262, and 819 converted to time-skip markers
criteria met: yes

## s01-fault-022 — RESOLVED
fault: ID 792 "the workshop settles" — environment-state description
scope: line
change: ID 792 converted to time-skip marker
criteria met: yes

## s01-fault-023 — RESOLVED
fault: IDs 646, 887 "the square traffic flows" — environment-state description
scope: line
change: IDs 646 and 887 converted to time-skip markers
criteria met: yes

## s01-fault-024 — RESOLVED
fault: IDs 225, 566, 703, 716, 736 "the [district/alley/lane] opens/closes" — environment-state descriptions
scope: line
change: IDs 225, 566, 703, 736 converted to time-skip markers. ID 716 not actioned — file contains "septon-rowan speaks to oc-craftsman-mother" (valid dialogue beat; audit ID drift from pre-fix version of file). The content "the market lane opens" that audit attributed to ID 716 is at ID 736 in the current file and was deleted there.
criteria met: yes (with anomaly note on ID 716)

## s01-fault-025 — RESOLVED
fault: ID 72 "the workshop murmur continues below" — stative/ongoing-state verb plus prepositional padding
scope: line
change: ID 72 converted to time-skip marker
criteria met: yes

## s01-fault-026 — RESOLVED
fault: ID 169 "septon-rowan points to the first line of the third section" — prepositional phrase padding
scope: line
change: Stripped prepositional phrase; line now reads "septon-rowan points the finger"
criteria met: yes

## s01-fault-027 — RESOLVED
fault: IDs 77, 122, 535, 671 "the [household/workshop] quiets" — environment-state descriptions
scope: line
change: IDs 77, 122, 535, 671 converted to time-skip markers
criteria met: yes

## s01-fault-028 — RESOLVED (pre-existing gap)
fault: ID 902 "the workshop murmur rises" — environment-state description
scope: line
change: ID 902 not present in file (gap between 900 and 904 covers IDs 901-903). Content already absent; treated as pre-existing deletion.
criteria met: yes

## s01-fault-029 — RESOLVED
fault: ID 337 "the dock crowd shifts its weight" — collective multi-subject plus abstract possessive object
scope: line
change: Recast to "a townsman steps back" (named-category singular actor performing discrete observable act)
criteria met: yes

## s01-fault-030 — RESOLVED
fault: ID 813 "the square traffic adjusts" — environment-state, collective abstract subject
scope: line
change: ID 813 converted to time-skip marker
criteria met: yes

## s01-fault-031 — RESOLVED
fault: ID 425 "townspeople form the collection queue" — plural multi-subject, environment-state collective
scope: line
change: ID 425 converted to time-skip marker (queue formation is environment-state per criteria)
criteria met: yes

## s01-fault-032 — RESOLVED (ID drift)
fault: Audit cited ID 563 "the collection queue breaks" — environment-state
scope: line
change: Content "the collection queue breaks" found at ID 513 in current file (audit ID drift). ID 513 converted to time-skip marker.
criteria met: yes

## s01-fault-033 — RESOLVED
fault: ID 511 "two of the collector's men right the table" — multi-subject
scope: line
change: ID 511 recast to "the first collector's man rights the table"; ID 915 appended at end of file as "the second collector's man rights the table" with # split-from: 511 comment
criteria met: yes

## s01-fault-034 — RESOLVED
fault: ID 334 "two mounted men lead the column" — multi-subject
scope: line
change: ID 334 recast to "a mounted man leads the column"; ID 914 appended at end of file as "a second mounted man rides" with # split-from: 334 comment
criteria met: yes

## s01-fault-035 — RESOLVED (partial — pre-existing gap)
fault: IDs 66, 913 "the lamp glow reaches the loft beam" — environment-state, ambient light extent
scope: line
change: ID 66 converted to time-skip marker. ID 913 not present in file (file ends at 912); treated as pre-existing deletion.
criteria met: yes

## s01-fault-036 — RESOLVED
fault: ID 515 "the column reassembles" — collective abstraction, collective-state description
scope: line
change: ID 515 converted to time-skip marker (delete option chosen per criteria)
criteria met: yes

## s01-fault-037 — RESOLVED (partial — ID drift)
fault: Audit cited IDs 509, 563 "the square traffic re-forms" — environment-state
scope: line
change: ID 509 "the square traffic re-forms" converted to time-skip marker. ID 563 in current file contains "taylor-hebert-jaehaerys follows" (not re-forms; handled under fault-038). Audit's ID 563 for re-forms is an artifact of file version drift.
criteria met: yes

## s01-fault-038 — RESOLVED (pre-existing gap)
fault: ID 901 "the loft closes" — environment-state
scope: line
change: ID 901 not present in file (gap between 900 and 904). Treated as pre-existing deletion.
criteria met: yes

## s01-fault-039 — RESOLVED
fault: ID 74 "oc-craftsman-mother answers" — wrong dialogue form, bare intransitive verb
scope: line
change: Recast to "oc-craftsman-mother speaks to oc-craftsman-father"
criteria met: yes

## s01-fault-040 — RESOLVED
fault: ID 222 "oc-craftsman-mother matches the pace" — abstract noun as object, interiority
scope: line
change: Recast to "oc-craftsman-mother shortens the step"
criteria met: yes

## s01-fault-041 — RESOLVED
fault: ID 512 "the levy roll spreads on the resettled table" — prepositional phrase of location plus modifier padding
scope: line
change: Stripped "on the resettled table"; line now reads "the levy roll spreads"
criteria met: yes

## s01-fault-043 — RESOLVED (pre-existing fix)
fault: ID 909 "the folio changes hands" — transactional abstraction, interiority
scope: line
change: File already contains "the ferryman receives the folio" at ID 909 (corrected form). No edit required.
criteria met: yes

## s01-fault-038-bare-follows — RESOLVED
fault: ID 563 "taylor-hebert-jaehaerys follows" — bare intransitive motion verb without destination
scope: line
change: Recast to "taylor-hebert-jaehaerys follows mira-stonefield-jaehaerys" (destination slug added)
criteria met: yes
