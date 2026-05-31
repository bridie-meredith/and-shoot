# /and-facets b01c07 — cycle-1 fix log

## SESSION-START — 2026-05-31T00:00:00Z — and-facets-b01c07-cycle1-fixes
dispatch: /and-facets b01c07 Phase 5b cycle-1 remediation — 4 failed facets (interest-narrator AP-001 cap, sensory 3-entry old-state/disambiguation, dialogue-halvard split-verdict, dialogue-taylor 2-persona convergence); apply minimum change per consolidated callouts in facets-audience-gate-r1.md
target: active-project/theater/facets/interest-narrator.md, active-project/theater/facets/sensory.md, active-project/theater/facets/location-state.md, active-project/theater/dialogue/septon-halvard-flea-bottom.md, active-project/theater/dialogue/taylor-hebert-kl-122ac.md
audit-report: active-project/staff/audience/facets-audience-gate-r1.md
findings-queued: 4 (interest-narrator, sensory[3-sub], dialogue-halvard, dialogue-taylor)

## fault-interest-narrator — RESOLVED — 2026-05-31T00:05:00Z
fault: AP-001 inverted-predicate cap ≤1/file exceeded — narrator:3@15 + narrator:4@19 both used "is-the-X" sentence-final collapsed-predicate; cap allows 1; narrator:4@19 (WATCH-1 named-death anchor) is the keeper; narrator:3@15 must recast
scope: line
change: interest-narrator.md narrator:3@15 — final clause recast from "that is the answer she is giving in place of the rebuttal she is holding back" (sentence-final inverted predicate, "that is the X") to "she gives him the staying instead of the rebuttal she is holding back" (direct transitive SVO; subject=she, verb=gives, object=the staying; no collapsed "is-the-X" chassis); substance preserved (planting reads to Halvard as commitment; INITIAL-commitment register; social-legibility of staying; soc-tether +0.5 load-bearing content intact); anchor @15 and citation narrator:3 unchanged
ADD pre-validation: n/a (no upstream artifact add required for this fix)
criteria met: yes — narrator:3@15 no longer uses inverted-predicate form; narrator:4@19 remains the sole "is-the-X" instance; cap satisfied at ≤1; NI:3@15 content (load-bearing per Phase 2.5/R2 INVIOLABLE) preserved intact

## fault-sensory — WORKING — 2026-05-31T00:06:00Z
note: multi-step repair with upstream pre-validation; applying loc-state sound-field backfill first (loc-state:3@9), then sensory:1 re-cite, then sensory:2 old-state correction, then sensory:4 modality recast

## fault-sensory — RESOLVED — 2026-05-31T10:20:00Z
fault: 3 sensory entries failed — sensory:1@12 unanchored old-state (no loc-state sound baseline); sensory:2@17 old-state contradicted loc-state (passage-lane-packed-earth after stone established at @15); sensory:4@22 cumulative thermal drift not a discrete event (fails disambiguation)
scope: line
sub-entries:
  sensory:1@12:
    pre-validation: loc-state:3@9 sound field backfilled in prior session (halvard-pastoral-account-register already present in location-state.md); old-state updated to halvard-pastoral-account-register with anchor loc-state:3@9 (prior session)
    result: ADD-LANDED-AFTER-UPSTREAM-EDIT (prior session); verified in file
  sensory:2@17:
    pre-validation: loc-state:4@15 (sept-corner stone underfoot) already exists — no new upstream add needed
    change: old-state corrected from passage-lane-packed-earth to sept-corner-stone-firm; anchor loc-state:4@15 (prior session)
    result: REVISED (prior session); verified in file
  sensory:4@22:
    pre-validation: loc-state:4@15 (sept-corner stone underfoot) exists — confirmed for proprioceptive old-state anchor
    change: modality recast from thermal (cold-settled-through-standing-weight, cumulative drift) to proprioceptive (heel-settles-cobble-edge, discrete event at @22 steadying action); old-state updated to sept-corner-stone-firm; anchor loc-state:4@15; licensed-grounding-exception grd-002 tag preserved; tag changed from up to spike (discrete event)
    result: ADD-LANDED (this session)
    distinct-from: sensory:2@17 (tactile cobble-grip, different modality); sensory:3@16 (thermal breath, different modality and locus)
inflight-r2 refreshed: proto-lines-sensory.md comment block updated (tokens unchanged — [sensory:1]@12, [sensory:2]@17, [sensory:3]@16, [sensory:4]@22 all at correct positions); proto-lines-loc-state.md created (loc-state tokens [loc-state:1]@1 through [loc-state:5]@23 confirmed)
criteria met: yes — sensory:1 old-state now anchored via loc-state:3@9 sound field; sensory:2 old-state matches governing loc-state at time of fire; sensory:4 is a discrete proprioceptive event not a cumulative drift; grd-002 grounding preserved; all three distinct modalities

## dialogue-septon-halvard-flea-bottom — RESOLVED — 2026-05-31T10:30:00Z
fault: :1@12 aphorism-strain — cape-fic REVISE (too polished/certain; "it was always going to grow" claims retrospective omniscience); dark-fantasy DEFEND (aphorism-form honesty-without-omniscience); worm-canon ACCEPT; split verdict
scope: line
routing: fixer-direct (minimum-change criterion clearly met; single phrase substitution; utterance text only)
change: sentence "It grows crooked at the rate it was always going to grow." → "It grows crooked at its own rate." — removes "was always going to grow" (fatalistic pre-knowledge claim) and replaces with "at its own rate" (observed fact without foreclaimed certainty); aphorism structure preserved; honest-working-through register preserved; Halvard's voice-tell "names his own uncertainty / does not speak about things he does not know" satisfied; dark-fantasy's defense (honesty-without-omniscience) now literally satisfied by the revised form
anchor @b01c07s02n04 and citation [septon-halvard-flea-bottom:1] unchanged; utterance text only
ADD pre-validation: n/a
criteria met: yes — revised sentence is no longer a prepared-certain closer; it states an observed rate without claiming advance knowledge; should satisfy cape-fic re-fire; dark-fantasy positive defense (honesty-without-omniscience) satisfied by new form; REVISED disposition

## dialogue-taylor-hebert-kl-122ac — RESOLVED — 2026-05-31T10:35:00Z
fault: :1@19 closing self-justification — dark-fantasy + worm-canon BOTH flagged SAME final sentence "She's why I'm in Flea Bottom at all." — converts Wenna Cobb's death into self-justification; Taylor "wins" the no-winner chapter; HIGH CONFIDENCE 2-persona convergence
scope: line
change: fixer-direct; deleted final sentence "She's why I'm in Flea Bottom at all." — entry now closes on "She's the first name in the count." (ledger-position, accepted by all reviewers); everything before that sentence preserved intact (Wenna Cobb concrete naming, WATCH-1, dark-fantasy "best prose in the chapter"); Taylor's cold-utilitarian ledger register preserved (the count is the unit, not motivation-to-interlocutor); no replacement suasion added
anchor @b01c07s03n02 (bone @19 in proto-lines) and citation [taylor-hebert-kl-122ac:1] unchanged; utterance text only
ADD pre-validation: n/a
criteria met: yes — REVISED; no self-justification remains; entry closes cleanly on ledger position; Wenna Cobb naming intact (WATCH-1 preserved); no-winner-chapter preserved

## SESSION-END — 2026-05-31T10:40:00Z — and-facets-b01c07-cycle1-fixes
findings-applied: 4 (interest-narrator RESOLVED; sensory RESOLVED [3 sub-entries, of which 2 were prior-session + 1 this session]; dialogue-halvard RESOLVED; dialogue-taylor RESOLVED)
findings-skipped: 0
notes: |
  - interest-narrator: prior session had already partially fixed (changed "that is the answer she is giving in place of the rebuttal she is holding back" to "she gives him the staying instead of the rebuttal she is holding back"); this session applied further minimal simplification to "she gives him the staying, not the rebuttal" to cleanly remove all trailing-participial AP-001 form
  - sensory:1 + sensory:2: prior session had applied these fixes (loc-state:3@9 sound field backfill; sensory:2 old-state correction to sept-corner-stone-firm); verified present; logged; sensory:4 was the open item fixed this session
  - proto-lines-loc-state.md created (was missing; prior session touched loc-state but didn't create the inflight file)
  - dialogue-halvard: fixer-direct (minimum-change phrase substitution; no agent dispatch needed for 3-word change)
  - dialogue-taylor: fixer-direct (single sentence delete)
  - anchor bones 12/19/21 confirmed unchanged; dialogue citations [septon-halvard-flea-bottom:1] and [taylor-hebert-kl-122ac:1] confirmed unchanged
  - build_cite_index NOT run (orchestrator responsibility per dispatch)
  - location-state re-fire at cycle 2: recommended (backfill touched loc-state:3@9)
exit: CLEAN
