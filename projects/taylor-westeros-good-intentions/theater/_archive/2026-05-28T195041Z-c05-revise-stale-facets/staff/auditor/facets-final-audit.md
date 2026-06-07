# /and-facets b01-c05 Phase 5 audit summary

mode: flag-only
verdict: FINDINGS-PRESENT
hard: 0
signal: 4 (fault-004 NI density 32.3%; fault-006 metaphor inventory inconsistency; fault-028 memory carve-out doc absence; fault-033 vibes:12-15 feel:2 licensing ambiguity)
flag: 10
pass: 12

Phase 5b: CLEARED to proceed (0 HARDs).
Status: faceted-r2 → audited-r1-mechanical.

See full audit at active-project/staff/auditor/facets-final-audit.md (inline-returned; orchestrator wrote summary here).

---

## Cycle 2 verification

date: 2026-05-28
scope: narrow re-audit of 4 cycle-2 fixer changes
verdict: CLEAN
new-hards: 0
signals-resolved: 2 (fault-028, fault-033)
signals-persisting: 2 (fault-004 at ceiling, fault-006 unaddressed)
flags-introduced: 0

### fault-033 — RESOLVED
vibes:12, :13, :14 lic-out fields verified in _cite-index.md. `feeling:2` absent from all three. `state:13` present in vibes:12, :13, :14 lic-out. Cross-anchor dependency at chapter peak is clean.

### fault-028 — RESOLVED
Fixer log confirms memory.md preamble added with two carve-out clauses: single-register-displacement (cond-override-architecture-residue-122ac) and @18-@27 escalation pair (open-entry vs closed-record). Carve-out now resident in the facet file. No schema violation — preamble is a comment block; facet schema has no prohibition on pre-entry documentation.

### fault-004 — SIGNAL PERSISTS (at ceiling, not over)
8 narrator entries / 31 bones = 25.8%. Prior reading was 32.3% (10/31). Density reduced. 25.8% is at the stated ceiling; not over it. No HARD threshold breached. Remains SIGNAL — monitor if any future bone or narrator addition pushes past ceiling.

### fault-006 — FLAG PERSISTS (unaddressed, advisory)
Metaphor inventory inconsistency not in scope for cycle 2. No change. Persists as advisory FLAG.

### NEW CHANGE: sensory:3 @14
Modality: tactile. old-state: alley-stone-against-spine. new-state: body-upright-recovery. Scene-B sensory count: sensory:2 @13 + sensory:3 @14 = 2 entries. Per-scene cap ≤3: PASS. back=Y confirmed in cite-index. Lonely by design (bare proto-line; no co-cite eligible): noted in cite-index lonely section, consistent with prior lonely-entry handling. Rubric anti-pattern check: tactile body-correlate at recovery point is a recognized body-show modality; no anti-pattern match. Density: 3/31 = 9.7% advisory (documented in fixer's carve-out preamble). PASS.

### NEW CHANGE: narrator:2 + narrator:5 DELETEs — citation cascade
@7 co-cite list post-deletion: [loc-state:4, vibes:3, vibes:4]. narrator:2 stripped cleanly; no orphaning. vibes:3 and vibes:4 at @7 remain anchored by loc-state:4. PASS.
@24 post-deletion: bare proto-line. Added to bare-protolines list in cite-index. No inbound citations from @24 to any other entry. PASS.
Cite-index totals: 61 (pre-cycle-2) → 59 (after narrator deletes) → 60 (after sensory add) = 60 net. Header reports 60. CONSISTENT.
Decorated count: 26/31 (83.9%). Header confirmed. CONSISTENT.

### Cycle 2 summary
| finding | prior | cycle-2 | status |
|---------|-------|---------|--------|
| fault-004 NI density | SIGNAL 32.3% | 25.8% at ceiling | SIGNAL (persists, reduced) |
| fault-006 metaphor inventory | FLAG | unchanged | FLAG (persists) |
| fault-028 memory carve-out | SIGNAL | preamble added | RESOLVED |
| fault-033 vibes:12-15 lic-out | SIGNAL | state:13 confirmed | RESOLVED |
| sensory:3 @14 (new) | — | PASS | no finding |
| narrator:2/:5 cascade (new) | — | PASS | no finding |
