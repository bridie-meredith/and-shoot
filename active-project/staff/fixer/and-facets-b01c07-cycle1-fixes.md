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
