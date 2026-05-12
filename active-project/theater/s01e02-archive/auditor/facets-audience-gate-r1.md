---
audit: facets-audience-gate-r1
episode: s01e02
date: 2026-05-11
cycle: 1
mode: blocking
status: FINDINGS-PRESENT — 6 of 9 facets revise; 3 facets clean
totals:
  facets-accept-3-of-3: 3   # metaphor, feeling, vibes (single-reviewer)
  facets-revise: 6          # tensometer, location-state, interest-narrator, sensory, state-updates, memory
  facets-fail: 0
  reviewers-fired: 14 (3 active-audience personas × 6 fallback facets + 3 sensory specialists + 2 undermanned single-reviewer for tensometer & vibes)
  verdict-files-written: 24 (cape-fic-reader: 8 facets reviewed; dark-fantasy-reader: 8; worm-canon-pedant: 6; 3 sensory specialists: 1 each)
---

# Phase 5b cycle 1 — audience adversarial gate aggregate report

## Per-facet aggregate verdicts

| Facet | Reviewers | cape-fic | dark-fantasy | worm-canon | Aggregate |
|-------|-----------|----------|--------------|------------|-----------|
| tensometer | 1 (cape-fic; undermanned) | REVISE | — | — | **REVISE** |
| location-state | 3 active | accept | revise | accept | **REVISE** |
| interest-narrator | 3 active | revise | revise | revise | **REVISE 3/3** |
| sensory | 3 specialists | accept (disambiguation-pedant) | accept (modality-coverage) | revise (old-state-reader) | **REVISE** |
| state-updates | 3 active | accept | revise | accept | **REVISE** |
| memory | 3 active | revise | revise | revise | **REVISE 3/3** |
| metaphor | 3 active | accept | accept | accept | **ACCEPT 3/3** |
| feeling | 3 active | accept | accept | accept | **ACCEPT 3/3** |
| vibes | 1 (dark-fantasy; undermanned) | — | pass-with-notes | — | **ACCEPT** (single-reviewer; no formal fault) |

## Critical findings (audience-only / auditor-miss)

### Two Earth-Bet proper-noun hard-fence violations the Phase 5 CONSTRAINT scan failed to catch

**HARD-FENCE-1: narrator:27 @149 — "Khepri-threshold"**
- Caught by all 3 active-audience personas (cape-fic, dark-fantasy, worm-canon).
- The R2 NI judge had explicitly flagged this for "dialect-audience cross-check at Phase D" — the audience overruled the "variant's-internal-mechanic-per-persona-card" defense unanimously.
- Auditor-miss: "Khepri" appears in the auditor's own Earth-Bet proper-noun scan exemplar list, but no finding was produced. CONSTRAINT scan should match against the proper-noun list as a substring check in NI entry content; recommended calibration note.

**HARD-FENCE-2: mem:10 @125 — "Gold Morning" in free-text target-reference gloss**
- Caught by worm-canon-pedant.
- mem:10 is one of the four R2 memory-judge ADDs. The judge's hard-fence scan reportedly cleared; the audience found it didn't.
- Auditor-miss with the same shape as HARD-FENCE-1: free-text gloss in a memory target-reference slipped past the CONSTRAINT scan.

Both findings are HARD by rubric definition (Earth-Bet proper noun hard-fence absolute). The Phase 5 auditor returned 0 HARD post-fix; the audience found 2 HARD-class violations the mechanical scan missed.

## Per-facet revision briefs

### tensometer — REVISE (cape-fic single-reviewer, undermanned)

- [tens:70] @83 — r=1 misrating under stakes-visibility axis. narrator:15 @83 fires "the lords-man's gait has the wrong leverage-load for an Eastern-Quarter alley" — a watch-cost / stakes-visibility signal that the rubric's r=2 exemplar pattern matches. Currently rated r=1 by dramatist.
- **Full convergence with auditor r1 A-001 (1→3 adjacency gap @83-@85 latch-break) + T-001 (eviction-approach @83-@84 momentum-stall candidate).**
- Fix: retune @83 from r=1 to r=2 in `tensometer.md` (and the upstream `tensometer-s01e02.md` slug-suffixed source). Closes A-001, T-001, and the audience callout simultaneously.

### location-state — REVISE (dark-fantasy revise; 2 accepts)

Atmosphere-thin sensory notes on three entries:
- [loc-state:5] @83 — names the lintel rather than the door-latch-intact condition about to matter. Eviction approach atmospherically inert at episode's highest-stakes beat. **Partial convergence with auditor T-001.**
- [loc-state:7] @132 — restates the condition field instead of naming what shutness means perceptibly.
- [loc-state:9] @156 — "narrow between buildings" generic; Eastern Quarter's discriminating sensory register absent.

Fix: rewrite sensory notes on the 3 entries with location-specific atmospheric content. R1 author can re-author with locked graph awareness.

### interest-narrator — REVISE 3-of-3

- **[narrator:27] @149 — HARD-FENCE-1** (see Critical findings above). 3-persona convergence. Label-swap: replace "Khepri-threshold" with foreknowledge-clamp language that holds threshold-excess registration without naming the monument. Earning basis (channel + tens=2 anchor + mem:11 + state:1 co-cites) survives; only the label is faulted.
- [narrator:32] @177 — earning test (dark-fantasy only). Channel (apparatus-log-as-instrument) has fired 3 prior times in episode. Author must name a distinct charge between @173's registration and @177's log-write or delete. Routes to NI author for defense; delete is default.

### sensory — REVISE (sensory-old-state-reader revise; 2 specialist accepts)

- [sensory:3] @125 — loc-state-gap. Old-state `stylus-on-wax-rhythm` unanchored. Most recent prior loc-state is loc-state:6 @97 (junction, morning) — wrong location + wrong time for @125's base-interior late-evening writing scene. No loc-state entry anchors Taylor's return to base in the @110→@132 window.
- Fix: requires loc-state author to add a re-entry loc-state entry covering Taylor's return to loc-flea-bottom-base (movement-verb gate; the R1 author had refused this on "narrator has no explicit re-entry verb" grounds — see R1 flagged seam #3). Either loc-state needs a soft re-entry beat added, OR sensory:3's old-state needs re-anchoring to a loc-state slug + adjacency note.

### state-updates — REVISE (dark-fantasy revise; 2 accepts; 3 convergent flags)

Three convergent flags requiring fix:
1. **[state:8 stance-on-tya-category old-state] @22** — `privately-concluded-not-tya` is production scaffolding without canonical anchor in actor card or state.md baseline. **Convergent: dark-fantasy + worm-canon** (different paths, same finding). Fix: defend against actor card or rename old-state value to something the card supports.
2. **[state:6 fauna_control_radius_m] @117** — beat asymmetry: studio fires the same conceptual 300→400 transition at @73; Taylor's actor-state fires at @117. **Convergent: cape-fic notes & accepts + worm-canon flags as potential lagging-violation.** Fix: either co-fire at @73 or document @117 as distinct second-expansion beat.
3. **[state:1 record_anomoly_logged] @149** (broken-maester slice) — type mismatch: old-state `true` (boolean) → new-state `phrase-isolated` (string ordinal). Cannot be cleanly applied as canonical write-back. **Worm-canon hard flag.** Fix: rename old-state to `anomaly-noted` as part of field-extension, or re-model as new field `record_anomaly_detail`.

### memory — REVISE 3-of-3 (most extensive findings)

Per-entry findings:
- **mem:2 @30** — 3-persona REJECT. Condition card is not monument authority. **Cull.**
- **mem:9 @87** — 2-persona REJECT (placement); 1 fidelity-only NOTE. Tens=3 placement + no displacement-clamp construction. Monument family correct (fauna-silence → Endbringer-parallel) but at wrong beat. **Relocate** to @89-@90 (trailing edge of eviction peak).
- **mem:10 @125 — HARD-FENCE-2** (see Critical findings). 3-persona REJECT, three different axes (tens=3 placement / clamp-absent / Earth-Bet proper noun in free-text). **Relocate** to @126-@127 + **rewrite** description with explicit displacement-clamp construction + **repair** target-reference removing "Gold Morning" Earth-Bet proper noun.
- **mem:12 @173** — CONTESTED. Requires author ceiling-defense memo: witness/action distinction (POV is witness not action-carrier at @173), resonance-not-action argument, why @174 doesn't serve better. If defense holds, KEEP; if not, cull.

File-level structural findings:
- **Single-register file (hard fail per rubric doubled-register requirement).** Zero Westerosi-monument clamp fires in 8 entries across 155 proto-lines. All fires are Earth-Bet displacement or Earth-Bet callback. **Add at least one Westerosi-monument clamp fire.** Candidates: broken maester's Citadel-form correspondence; tanner-family customary-wage-claim language; phrase the beetles carried @149.
- **Inverted-tens-density misalignment.** 3 of 8 entries at tens=3 (mem:9, mem:10, mem:12) inverts rubric's required inverted-tens-density (fires cluster in 1-zones; tens=3 fires default-forbidden). Two of three are culled-or-relocated above; mem:12 pending contest resolution.
- **Margit referral.** mem:3 and mem:7 monument families ("pre-deployment ritual survival", "swarm-feed as parallel-track cognition") draw authority from §"Non-verbal tics" and §"Voice tells" rather than §"Memory monuments" proper. Submit to margit for canonicalization as mechanism-descriptive monument slugs.

## ACCEPT-3-of-3 facets

- **metaphor** — single surviving entry meta:1 @89 simile clean across all 3 personas. AP7 R2-defense unanimously sustained (AP7 is peak-zone prohibition, inapplicable at tens=1; not a waived prohibition).
- **feeling** — 9 entries clean across all 3 personas. @87 expressed:no identified by 2 personas as file's strongest asymmetry beat. F-002 5.8% advisory not escalated. Zero forbidden-vocab violations.
- **vibes** — single-reviewer dark-fantasy PASS-WITH-NOTES. Thematic coherence, AP8 token-form, licensed-by anchors, cross-target fan-out all clean. Two soft style-ceiling notes (vibes:12 / vibes:18) advisory.

## Convergence trace (vs. Phase 5 auditor r1)

- Auditor r1 HARD: 1 (metaphor:2 unresolvable anchor — RESOLVED by fixer DELETE between r1 and r2 audit).
- Auditor r1 SIGNAL: 7 (S-002, F-002, M-001, M-002, A-001, A-002, T-001).
- Audience-gate cycle-1 findings (deduped across reviewers): ~14 distinct callouts across 6 facets.
- **Shared findings (audience + auditor on same entry):** A-001 + T-001 ↔ tensometer @83 audience callout (full convergence). T-001 ↔ location-state:5 @83 (partial convergence — same anchor, different facet).
- **Audience-only findings:** 12 (HARD-FENCE-1 narrator:27 Khepri; HARD-FENCE-2 mem:10 Gold Morning; location-state:7 @132; location-state:9 @156; narrator:32 @177; sensory:3 @125 loc-state-gap; state:8 stance-on-tya; state:6 fauna-radius asymmetry; state:1 record_anomaly type mismatch; mem:2 cull; mem:9 relocate; mem:12 contest).
- **Auditor-only findings:** 5 SIGNAL classes still advisory (S-002, F-002, M-001, M-002, A-002 — none re-classified by audience).
- **Bidirectional loop verdict: VALIDATED.** Shared findings: A-001/T-001 ↔ tens:70 @83 cape-fic-reader callout (full convergence on same entry across both paths). Phase 5b's structural promise (each path independently surfacing real findings, with at least one shared finding) is met for this episode.

## Remediation routing — cycle 2 candidates

The fixer's "minimum change required" scope handles cleanly:
- tens:70 @83 retune r=1 → r=2 (single cell)
- narrator:27 @149 label swap (Khepri-threshold → foreknowledge-clamp synonym)
- mem:10 @125 deletion (cleanest — entry has 3 independent rejection axes)
- mem:2 @30 deletion (3-persona reject)
- state:1 record_anomoly type mismatch repair (field-extension rename)

Exceeds minimum-change fixer scope:
- Memory revisions in aggregate (relocate mem:9, contest mem:12, add Westerosi clamp) — requires R2 memory judge re-dispatch with revision brief.
- Location-state sensory-note rewrites (3 entries) — requires loc-state R1 author re-dispatch.
- Sensory:3 loc-state-gap — requires loc-state R1 author to add a re-entry beat (or sensory R1 author to re-anchor).
- State:8 stance-on-tya old-state grounding — requires tanner-father impersonator to defend old-state value against card.
- State:6 fauna_control_radius asymmetry — cross-fork coordination (taylor + studio).
- Narrator:32 @177 earning-test defense — requires NI judge or author.

## Auditor calibration notes (carry-forward)

Two CONSTRAINT-scan misses on Earth-Bet proper-noun hard-fence:
1. "Khepri" at narrator:27 @149 (in NI entry content).
2. "Gold Morning" at mem:10 @125 (in memory target-reference free-text gloss).

Both proper nouns appear in the auditor's own scan exemplar list ("Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT"). The CONSTRAINT scan should match against the proper-noun list as a substring check across all facet entry content fields — not just structural headers or state-update field names. Filed as URI-AUDITOR-CONSTRAINT-CALIBRATION (pending URI assignment).

## Verdict

**Phase 5b cycle 1: BLOCKED.** 6 of 9 facets need revision. 2 HARD-fence violations require fix before any subsequent audit pass. Cycle 2 remediation required to clear the gate; cycle cap is 3.
