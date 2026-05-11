---
audit: facets-final-r2
episode: s01e01
date: 2026-05-11
mode: flag-only / re-audit-after-remediation
status: FINDINGS-PRESENT
totals: 1 residual finding (1 UPHELD-HARD)
---

# Facets Final Audit R2 — s01e01

Auditor: cross-cutting graph auditor fork (Phase 5 re-audit)
Mode: FLAG-ONLY. Targeted verification of 9 findings addressed by fixer remediation pass (C1–C5). Out-of-scope findings (flag-003, flag-006, flag-007, flag-009, flag-013) not re-examined.

Independent count performed on tensometer.md body before verdict. Entry totals: 141 entries confirmed (IDs 1–78 = 78; 81–92 = 12; 93–128 excl. 123 = 35; 130–142 = 13; 144–146 = 3). 3s = 7, 2s = 21, 1s = 113. Figures match the file's self-reported frequency-band section.

---

## Verdict blocks

### flag-001 — CLEARED
- id: flag-001
- initial severity: HARD STRUCTURAL
- verdict: CLEARED
- evidence: tensometer.md body contains no anchor IDs outside aggregate range 1–155. Anchors @495, @504, @506, @516, @517, @518, @525 are absent from the entry list. The frequency-band section at line 154 documents the removal ("strip of 8 out-of-range anchor entries per C1 remediation"). No residual out-of-range anchor in the body.

### flag-002 — CLEARED
- id: flag-002
- initial severity: HARD STRUCTURAL
- verdict: CLEARED
- evidence: tensometer.md body contains no entry with ID `123a`. The non-monotonic mid-body insertion is absent. Entry sequence jumps from ID 122 (@131) to ID 124 (@132), which reflects the strip of the former ID-123 entry (@506, out-of-range); the former `123a` (@518, out-of-range) is also gone. No schema monotonicity fault remains.

### flag-004 — CLEARED
- id: flag-004
- initial severity: SIGNAL STRUCTURAL
- verdict: CLEARED
- evidence: interest-narrator.md line 50 reads: `# Density: 38/155 ≈ 24.5% [SUPERSEDED — pre-R2 figure; see post-R2 density below]`. SUPERSEDED marker is present and explicit. The stale-data seam is resolved.

### flag-005 — UPHELD-HARD
- id: flag-005
- initial severity: HARD FREQUENCY-BAND
- verdict: UPHELD-HARD
- evidence: Independent count confirms 2s = 21/141 = 14.9%. This is 5.1 percentage points below the 20% floor (the strip worsened the ratio from the initial reading of 17.4% because stripped entries were disproportionately 1s, diluting the 2s share further). The fixer documented an exemption note in the frequency-band section: "opening-window low-charge; structural per orchestrator-verdict; below-floor by 8 entries at 20% floor threshold."
- rationale: The exemption note is present but insufficient to close the HARD. The rubric's FREQUENCY-BAND gate does not enumerate "opening-window low-charge" as a named exception class. The reference to "orchestrator-verdict" is not accompanied by a quoted passage from the orchestrator-critic card confirming that this pattern earns a below-floor pass for W1 episodes. The exemption claim is a self-defense assertion by the tensometer author; it has not been confirmed by the orchestrator-critic verdict at the per-episode facet level. A HARD FREQUENCY-BAND gate failure requires either (a) rubric-level enumeration of the exception class, or (b) a direct pass from the orchestrator-critic on this specific file. Neither is present. The finding is upheld.

### flag-008 — CLEARED
- id: flag-008
- initial severity: SIGNAL METADATA-INCONSISTENCY
- verdict: CLEARED
- evidence: The `123a` non-monotonic entry is absent. The frequency-band section's claimed total of 141 is verified by independent count (confirmed 141). The former "includes interpolated IDs 495, 504, 506, 517, 518, 525" language in the header is gone; the frontmatter now states `bones: 1–155` without that parenthetical. No total-count ambiguity remains.

### flag-010 — CLEARED
- id: flag-010
- initial severity: HARD SUPERFLUOUS
- verdict: CLEARED
- evidence: All six superfluous out-of-range entries (tens:79 @495, tens:80 @504, tens:123 @506, tens:143 @516, tens:147 @517, tens:148 @525) plus the non-monotonic tens:123a @518 are absent from the tensometer.md body. No entry anchors to a proto-line ID outside s01e01's aggregate range (1–155).

### flag-011 — CLEARED
- id: flag-011
- initial severity: SIGNAL CONSTRAINT
- verdict: CLEARED
- evidence: mem:7 @98 now reads: "the name of the city holds a season she has not entered and the season she has not entered is the one she knows the shape of." narrator:25 @98 now reads: "King's Landing arrives as a city she has already named, in a season she has not yet reached." The shared date-arrives-at-a-hand-holding-the-book simile construction is gone from both entries. The memory entry carries the foreknowledge-clamp via the "knows the shape of" register; the NI entry carries the perceptual-arrival via the "already named / not yet reached" register. The two entries are non-redundant on distinct channels at the same anchor.

### flag-012 — CLEARED
- id: flag-012
- initial severity: HARD-proximity CONSTRAINT
- verdict: CLEARED
- evidence: memory.md margit-referral slugs examined: mem:4 @134 now carries `monument-fauna-silence-at-scale`; mem:6 @43 now carries `monument-failed-recognition-by-dying-parent`. The Earth-Bet proper nouns "Endbringer" and "Annette" no longer appear as slug components in any margit-referral parenthetical. All nine memory entries scanned; no Earth-Bet proper-noun slug name found.

### flag-014 — CLEARED
- id: flag-014
- initial severity: SIGNAL AP-SCAN
- verdict: CLEARED
- evidence: narrator:25 @98 now reads: "King's Landing arrives as a city she has already named, in a season she has not yet reached." This is a single appositive structure, not a two-part simile. The "the way a date in a book arrives at a hand that holds the book" construction is absent. SEAM-3 note in interest-narrator.md confirms: "rewritten to one-clause form per C4 remediation (simile structure removed; foreknowledge-clamp content preserved)." One-clause form-discipline satisfied.

---

## Summary

**HARD findings remaining (from initial 4 HARD + 1 HARD-proximity):**
- flag-005 UPHELD-HARD (FREQUENCY-BAND: 2s at 14.9%, below 20% floor; exemption note present but not rubric-confirmed)
- flag-001: CLEARED
- flag-002: CLEARED
- flag-010: CLEARED
- flag-012: CLEARED

Count: **1 HARD remaining**

**SIGNAL findings remaining (from the 9 targeted):**
- flag-004: CLEARED
- flag-008: CLEARED
- flag-011: CLEARED
- flag-014: CLEARED

Count: **0 SIGNAL remaining from targeted set**

**Residual classes that may still need fixer or rubric attention:**

| Class | Finding | Status | Action needed |
|-------|---------|--------|---------------|
| FREQUENCY-BAND | flag-005 | UPHELD-HARD | Rubric-level enumeration of opening-window exception class, or orchestrator-critic explicit per-episode-facet pass, required to close |
| STRUCTURAL | flag-003 | Not re-examined (out of scope this pass) | Multi-source concatenated state-updates.md format deviation; carried forward from r1 |
| FREQUENCY-BAND | flag-006 | Not re-examined | NI density 25.2% at upper-edge ceiling; carried forward from r1 |
| FREQUENCY-BAND | flag-007 | Not re-examined | feeling per-character below-floor for 4 of 6 characters; rubric calibration needed |
| CURVE-SHAPE | flag-009 | Not re-examined | KICKBACK-1 and KICKBACK-2 unresolved; carry-forward to screen-writer |
| CONSTRAINT | flag-013 | Not re-examined | vibes tens:<N> notation ambiguity (reading vs ID); rubric clarification needed |
