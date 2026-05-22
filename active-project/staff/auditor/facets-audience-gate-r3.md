# Facets Audience-Gate Report — b01c02

report: facets-audience-gate
episode: b01c02
date: 2026-05-22
cycles: 3 / 3
mode: facet-adversarial (per-reviewer verdicts, strict 3-of-3 ACCEPT per URI-AUDIENCE-AGGREGATION-RULE)
result: ACCEPT — all 11 review targets pass 3-of-3; no cap-burn

---

## Reviewer assembly

- sensory facet: 3 specialists — sensory-disambiguation-pedant, sensory-modality-coverage,
  sensory-old-state-reader (target-facet specialists fired).
- all other facets + dialogue: active-project audience trio — cape-fic-reader,
  dark-fantasy-reader, worm-canon-pedant (fallback, graph-aware adversarial mode).

## Per-facet aggregate (final-cycle verdict)

| target | cycle cleared | final aggregate |
|--------|---------------|-----------------|
| location-state    | 2 | accept (3-of-3) |
| interest-narrator | 3 | accept (3-of-3) |
| sensory           | 3 | accept (3-of-3) |
| state-updates     | 2 | accept (3-of-3) |
| memory            | 2 | accept (3-of-3) |
| feeling           | 2 | accept (3-of-3) |
| metaphor          | 1 | accept (3-of-3) |
| vibes             | 2 | accept (3-of-3) |
| exposition        | 2 | accept (3-of-3) |
| dialogue — taylor-hebert-kl-122ac | 2 | accept (3-of-3) |
| dialogue — wren-stitch-maker-flea-bottom-ward | 2 | accept (3-of-3) |

All 9 facets + both per-character dialogue files cleared. No facet cap-burned.

## Cycle history

- **Cycle 1:** metaphor passed 3-of-3. 10 targets failed (location-state, interest-narrator,
  sensory, state-updates, memory, feeling, vibes, exposition, dialogue ×2). Consolidated
  callouts → fixer cycle-2 remediation.
- **Cycle 2:** 8 of the 10 re-fired targets passed (location-state, state-updates, feeling,
  exposition, memory, vibes, dialogue ×2). 2 failed: interest-narrator (narrator:6 @28 — a
  second AP-10 inverted-predicate surfaced on adversarial re-read) and sensory (sensory:2
  structural anchor bind). → fixer cycle-3 remediation.
- **Cycle 3:** both re-fired targets passed. interest-narrator — narrator:6 recast cleared
  the AP-10. sensory — sensory:2 deleted (no valid anchor exists in b01c02; cycle-3 A3
  no-ADD-budget); all 3 specialists accepted the documented sound-only file as the correct
  terminal disposition. NB: the sensory:2 DELETE leaves a modality-floor breach (1 modality)
  recorded as an ACCEPTED-AT-CAP-BURN-style trade-off — but the facet PASSED 3-of-3 at
  cycle 3, so this is a clean pass on a documented terminal file, NOT a cap-burn.

## Remediation summary

- Cycle-2 fixer: 10 callouts — vibes keyword rename + retarget, dialogue sidecar
  facet-license resolution, exposition appositive, feeling one-clause recast, narrator:4
  softener-tail + age-mismatch, loc-state perceptible-element reword, state-updates
  overclaim provisionalising, sensory:2 relocation, two monument cards authored.
- Cycle-3 fixer: 2 callouts — narrator:6 AP-10 recast (FIXED-DIRECT); sensory:2 DELETE
  (no valid anchor; modality-floor breach documented).
- Phase 5 re-audits: cycle 2 (HARD=0), cycle 3 (HARD=0), cycle 4 (HARD=0). No HARD finding
  survived any remediation pass.

## Convergence trace

- Auditor findings (Phase 5, final state): 0 HARD, 5 SIGNAL (flag-001, flag-002, flag-005,
  flag-008, flag-010 — all advisory carry-forward).
- Audience callouts cycle 1 (deduped, across all reviewers): 10 facets with blocking callouts.
- **Shared findings — auditor AND audience independently flagged the same entry:**
  - `[vibes:14]` keyword `earning-collapse` — auditor flag-006 (TASTE-FLAG) + audience vibes 3-of-3 revise.
  - `[vibes:1]` `routing-without-contact` actor-scope staleness — auditor flag-007 (PILE-UP) + audience vibes 3-of-3 revise.
  - dialogue sidecar facet-license DEFERRED placeholders — auditor flag-009 (RUBRIC-FIDELITY) + audience dialogue (worm-canon-pedant, both characters) revise.
  - `[exposition:4]` "Flea Bottom" cold-join orientation — auditor flag-004 (CONSTRAINT/CN-002) + audience exposition 3-of-3 revise.
- Audience-only findings: loc-state:6 spatial-arithmetic; narrator:4 channel-ambiguity +
  softener-tail; narrator:6 AP-10 (cycle-2 surface); sensory:1/:2 old-state + self-charge;
  state:10/12/13/15 value overclaims; feeling:1/:2 one-clause form; memory mem:2 monument-card dependency.
- Auditor-only findings: flag-001, flag-002, flag-005, flag-008, flag-010 (SIGNAL advisories).
- **Bidirectional loop verdict: VALIDATED** — 4 shared findings across the mechanical-scan
  and adversarial-reading paths; both paths fired and produced overlapping findings.

## Carry-forward SIGNAL advisories (non-blocking)

- flag-001 STRUCTURAL — state-updates.md multi-block frontmatter (schema-coverage).
- flag-002 METADATA — R2.3 Taylor shard internal citation stale (shard-only, not deployed graph).
- flag-005 AP-SCAN — cost/count vocabulary cluster; carry to b01c03 authoring brief.
- flag-008 RUBRIC-FIDELITY — state-updates density advisory for short chapters.
- flag-010 CONSTRAINT/schema — the two new monument cards lack a `## Direct samples` section
  (margit hygiene; non-blocking for monument-resolution use).
- sensory modality-floor breach — sound-only file; ACCEPTED documented terminal trade-off.
