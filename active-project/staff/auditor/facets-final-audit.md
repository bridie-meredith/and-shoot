---
audit: facets-final-r2
episode: b01c08
date: 2026-05-31
mode: flag-only
cycle: remediation-cycle-2
status: CLEAN
totals: 0 HARD / 6 SIGNAL (5 prior flags unchanged; 1 new signal)
prior-hard-count: 5
closed-hard-count: 5
new-hard-count: 0
---

# Facets Final Audit — b01c08 — Remediation Cycle 2

```yaml
audit:
  scope: chapter
  target: b01c08
  timestamp: 2026-05-31
```

---

## Prior HARD Closure Verification

### fault-001 — CLOSED
```yaml
id: fault-001
prior-status: HARD (dialogue anchor used in-memory slug form @b01c08s03n05 instead of flat_id @20)
post-fix-state: >
  active-project/theater/dialogue/oswyn-mudway-flea-bottom-elder.md entry 1 anchor
  reads `@20` (flat integer). Direct file read confirms. Back-citation format is
  the schema-required flat_id form. Forward citation [oswyn-mudway-flea-bottom-elder:1]
  at proto-lines @20 and the dialogue file's single entry are consistent.
verdict: CLOSED
```

### fault-002 — CLOSED
```yaml
id: fault-002
prior-status: HARD (proto-lines @8 cited feel:1 pointing to Oswyn@20; should cite feel:2 for Taylor@8)
post-fix-state: >
  Proto-lines @8 bracket reads [feel:2] [mem:1] [narrator:2] [state:1].
  Cite-index confirms: feel:2 @8 back=Y co=[mem:1, narrator:2, state:1].
  The Taylor breath-holds entry is correctly routed to bone @8.
verdict: CLOSED
```

### fault-003 — CLOSED
```yaml
id: fault-003
prior-status: HARD (proto-lines @13 cited feel:2 and state:3; should cite feel:3 and state:10)
post-fix-state: >
  Proto-lines @13 bracket reads [exposition:2] [feel:3] [narrator:3] [state:4] [state:10] [vibes:3].
  Cite-index confirms: feel:3 @13 back=Y co=[exposition:2, narrator:3, state:4, state:10, vibes:3]
  and state:10 @13 back=Y co=[exposition:2, feel:3, narrator:3, state:4, vibes:3].
  The Taylor hand-not-pause entry (feel:3) and named_chain_of_responsibility entry (state:10)
  are correctly routed to bone @13. The stale state:3 cite is gone.
verdict: CLOSED
```

### fault-004 — CLOSED
```yaml
id: fault-004
prior-status: HARD (proto-lines @6 cited state:1 and state:2 pointing to env entries at @8/@9; should cite state:8 and state:9)
post-fix-state: >
  Proto-lines @6 bracket reads [narrator:1] [state:8] [state:9] [vibes:2].
  Cite-index confirms: state:8 @6 back=Y co=[narrator:1, state:9, vibes:2]
  and state:9 @6 back=Y co=[narrator:1, state:8, vibes:2].
  The Taylor capability_axis (state:8) and watcher_network_nodes (state:9) entries are
  correctly routed to bone @6.
verdict: CLOSED
```

### fault-005 — CLOSED
```yaml
id: fault-005
prior-status: HARD (vibes:2/3/4/5 licensed-by fields carried wrong consolidated state-update IDs)
post-fix-state: >
  Vibes file licensed-by values verified against cite-index lic-out fields:
  - vibes:2 licensed-by: state-update:9, peak-bone:6, peak-bone:24
    (was state-update:2; now correctly points to Taylor watcher_network_nodes @6;
    cite-index lic-out=[state-update:9, peak-bone:6, peak-bone:24] consistent)
  - vibes:3 licensed-by: state-update:10, peak-bone:13, peak-bone:15
    (was state-update:3; now points to Taylor named_chain_of_responsibility @13;
    within fault-005 criteria window — criteria stated state-update:4 OR state-update:10;
    state:10 is mechanistically grounded in the Aemond-name @13 cluster)
  - vibes:4 licensed-by: peak-bone:24, state-update:11
    (was state-update:4; now correctly points to Taylor body_map.courier-figure @21;
    cite-index lic-out=[peak-bone:24, state-update:11] consistent)
  - vibes:5 licensed-by: state-update:10, canon:vhagar-handler-rotation-in-jarvis-logistics-b01c08
    (was state-update:3; now points to state:10 @13; within criteria window)
  All four vibes license-sources point to state entries mechanistically connected to
  the vibe's target entity and pattern.
verdict: CLOSED
```

---

## Fix-Introduction Scan — New HARD Findings

**None found.**

Specific checks performed:

**Cite-index self-consistency post-rebuild.** The rebuilt cite-index co-citation fields are algebraically consistent with the corrected proto-lines brackets at @6, @8, and @13. The narrator co-citations at @8 and @13 correctly list feel:2 and feel:3 respectively. The state co-citations at @6 correctly list state:8 and state:9. All 37 facet entries have back=Y or are correctly marked back=- (vibes:5 is off-anchor; exposition:1 is synthetic @0). No entry has lost a back-pointer. No new back=N entries.

**@21 follow-on fix cross-check.** Proto-lines @21 reads [narrator:5] [state:11]. Cite-index confirms state:11 @21 back=Y co=[narrator:5]. Vibes:4 licensed-by correctly cites state-update:11. Consistent.

**Dialogue anchor propagation.** The oswyn-mudway-flea-bottom-elder dialogue file carries the canonical flat_id form @20. The cite-index feel:1 @20 back=Y co=[oswyn-mudway-flea-bottom-elder:1, vibes:4] is consistent with the corrected proto-lines @20 bracket [feel:1] [oswyn-mudway-flea-bottom-elder:1] [vibes:4].

**R2 shard feel-ID notation check.** The feeling-taylor R2 shard (active-project/staff/feeling/r2-decision-shard-taylor-hebert-kl-122ac.md) references "feel:1@8" and "feel:2@13" in its INVIOLABLES summary. These match the facet file's own sequential entry IDs (entry 1 = @8, entry 2 = @13 in feeling-taylor-hebert-kl-122ac-b01-c08.md), not the cite-index global tokens (feel:2 and feel:3). The shard was authored using file-internal numbering; the cite-index uses the consolidated namespace where oswyn's feel:1@20 was loaded first. This is a notational mismatch in the R2 shard's cross-reference lines but the underlying entries are the same objects. The shard's f-r2-counts {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0} are unaffected. This is flagged as a SIGNAL — see flag-006.

---

## SIGNAL Findings

### flag-001 (unchanged from R1)
```yaml
id: flag-001
type: flag
what: >
  Three facets (memory 2/24 = 8.3%, feeling-taylor 2/24 = 8.3%, exposition 2/24 = 8.3%)
  each exceed their respective rubric band ceilings (1-5% for memory and exposition;
  2-5% for feeling). All three carry density-justification citing the 24-bone
  short-chapter denominator.
why: >
  No downstream fault — all three are individually defended SIGNAL-band overages.
  Recorded for orchestrator-critic pattern tracking: if subsequent b01 chapters show
  the same band overages without a short-chapter denominator driver, the pattern
  would indicate systematic over-authoring.
```

### flag-002 (unchanged from R1)
```yaml
id: flag-002
type: flag
what: >
  interest-narrator-b01-c08.md frontmatter uses "episode: b01-c08" (hyphenated).
  Canonical chapter slug is b01c08 (no hyphen). Several other facet headers also
  use the hyphenated form.
why: >
  No parse fault per the schema downstream-compat note. Low-risk inconsistency;
  a naive string-match staleness check could miss cross-file slug matches.
  No stitch consequence.
```

### flag-003 (unchanged from R1)
```yaml
id: flag-003
type: flag
what: >
  vibes:5 keyword "rising-entrapment" (hyphenated) may diverge from the
  aemond-targaryen-122ac actor vibe-cloud keyword form. The ++ op requires
  exact keyword-index match.
why: >
  If the actor vibe-cloud uses "rising entrapment" (space-separated), the ++ op
  would create a bifurcated keyword instead of extending the existing bundle.
  Vibes are not rendered at stitch, so no immediate output consequence; but
  downstream operator bias would split across two entrapment keywords.
  Showrunner to verify actor vibe-cloud keyword form before b01c09.
```

### flag-004 (unchanged from R1)
```yaml
id: flag-004
type: flag
what: >
  prop:oc-jarvis-packet and prop:oc-feed-station-ledger referenced by state-update
  env entries (state:2 @9 and state:4 @13) have no warehouse cards.
why: >
  prop:oc-feed-station-ledger carries the aemond-entry forward as a permanent
  logged fact; without a card, future state-updates to this prop have no
  schema-validated anchor. Margit card dispatch needed before b01c09 authoring.
```

### flag-005 (unchanged from R1)
```yaml
id: flag-005
type: flag
what: >
  loc:the-hook-ward appears across all three scenes, all six loc-state entries,
  and vibes:1; no library card at cards/locations/ or active-project/warehouse/.
  Vibes:1 carries a rubric gate-1 carve-out for the missing card.
why: >
  The carve-out is valid for b01c08. The hook-ward carries forward into b01c09+
  per vibes:1's coverage-extends-through-absorbance operator. Without a card,
  the location has no schema-validated anchor for future state-updates.
  Candidate for margit card-promotion dispatch.
```

### flag-006 (new — introduced by fix context)
```yaml
id: flag-006
type: flag
what: >
  The feeling-taylor R2 shard at active-project/staff/feeling/r2-decision-shard-taylor-hebert-kl-122ac.md
  references INVIOLABLES as "feel:1@8" and "feel:2@13" — these are the facet file's
  own sequential entry IDs (entry 1 and entry 2 within feeling-taylor-hebert-kl-122ac-b01-c08.md),
  not the cite-index global namespace tokens (feel:2 and feel:3 respectively).
  The R2 shard's consolidated summary in .r2-decisions.md similarly reads
  "INVIOLABLES (feel:1@8, feel:2@13) both HELD."
why: >
  The R2 shard cross-reference IDs do not match the cite-index global tokens.
  No F-R2-* failure is introduced — the underlying entries are the same objects
  and the f-r2-counts remain {0,0,0,0}. However, a future Phase 3 cross-session
  staleness check that parses the shard's INVIOLABLES token strings against the
  consolidated cite-index would fail to find "feel:1" and "feel:2" in the cite-index
  (which uses feel:2 and feel:3), producing a false-positive mismatch alert.
  The discrepancy predates the fixer pass and was not introduced by it; it originates
  from the shard being authored before consolidation renumbering propagated back into
  the shard's reference lines. No stitch consequence; no f-r2-count consequence.
  Showrunner to note that the shard's feel-ID cross-reference lines use file-internal
  numbering, not cite-index global tokens, before b01c09 Phase 3 staleness checks run.
```

---

## Audit Summary

### Prior HARDs — All CLOSED

| id | what | verdict |
|----|------|---------|
| fault-001 | Dialogue anchor @b01c08s03n05 → @20 | CLOSED |
| fault-002 | Proto-lines @8 feel:1 → feel:2 | CLOSED |
| fault-003 | Proto-lines @13 feel:2 → feel:3, state:3 → state:10 (added) | CLOSED |
| fault-004 | Proto-lines @6 state:1/state:2 → state:8/state:9 | CLOSED |
| fault-005 | Vibes:2/3/4/5 licensed-by IDs corrected to consolidated state entries | CLOSED |

### New HARDs: 0

### SIGNAL Findings: 6
- flag-001: density band overages on memory/feeling/exposition (denominator-driven; advisory)
- flag-002: episode slug hyphenation inconsistency in facet frontmatter
- flag-003: vibes:5 keyword hyphenation vs. actor vibe-cloud form (verify before b01c09)
- flag-004: missing warehouse cards for prop:oc-jarvis-packet and prop:oc-feed-station-ledger
- flag-005: loc:the-hook-ward no library card (carve-out held; margit dispatch recommended)
- flag-006: feeling-taylor R2 shard INVIOLABLES use file-internal IDs (feel:1/feel:2), not cite-index global tokens (feel:2/feel:3) — not a f-r2-count fault; staleness-check mismatch risk before b01c09

---

## Routing

No fixer dispatches required. All HARD findings are closed.

Signal flags:
- flag-001: advisory for orchestrator-critic cross-chapter pattern check.
- flag-002: low-priority normalization; no gate consequence.
- flag-003: showrunner verify actor vibe-cloud keyword form before b01c09.
- flag-004: margit dispatch for prop cards before b01c09.
- flag-005: margit card-promotion dispatch recommended.
- flag-006: showrunner note shard feel-ID notation convention before b01c09 Phase 3 staleness check.

**Pipeline gate: b01c08 facets are clear to proceed to /and-stitch b01c08.**
