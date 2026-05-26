```yaml
audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-25
  cycle: 2
  prior_audit: active-project/staff/auditor/facets-final-audit-r2.md
  cite_index_checked: active-project/theater/facets/_cite-index.md
  mode: full-eleven-class rescan post cycle-1 fixer pass
  findings:

    - id: fault-C2-001
      type: fault
      what: >
        vibes-b01-c01.md entry 11 — licensed-by field cites `state:4` as a licensing
        source. state:4 was DELETED in cycle-1 state-updates remediation
        (and-facets-cycle1-fixes-state-updates.md, fault-SU-001). state:4 no longer
        exists in state-updates-taylor-hebert-kl-122ac.md, state-updates.md
        (consolidated), or _cite-index.md. The cite-index confirms: state section
        shows entries state:1/2/3/7/9 only; state:4 is listed only under the
        DELETED comment block.
      why: >
        A licensed-by citation that does not resolve to an existing facet entry
        is a HARD finding under rubric-vibes.md §Required gates gate 4
        ("Licensed-by resolvable — each source points to an existing facet entry,
        proto-line, or named canon/world-build context"). The stitcher and any
        downstream consumer reading the license chain for vibes:11 cannot validate
        the claimed provenance. The vibe entry's add-validation log (fixer log
        and-facets-cycle1-fixes-vibes.md, ADD vibes:11) named state:4 @12 as one
        of four licensing sources; with state:4 deleted, only three sources remain
        (proto:12, proto:13, state:3). The entry may still be licensable via those
        three, but the broken citation must be cleaned from the file on disk.
      criteria: >
        vibes:11 licensed-by field must not reference state:4. Remove the state:4
        citation. Verify the remaining three sources (proto:12, proto:13, state:3)
        are sufficient to license the entry under rubric gate 4 and that the
        pre-validation arguments in the fixer log hold without state:4.

    - id: fault-C2-002
      type: fault
      what: >
        active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md,
        Entry 3 (known-adult routing), facet-licenses field:
        "sensory:2 @16 + state:5 @17".
        Two independent breakages in this single field:
        (a) sensory:2 anchor moved @16→@9 in cycle-1 sensory remediation
        (and-facets-cycle1-fixes-sensory.md). sensory:2 no longer fires at @16;
        it fires at @9. The proto-lines file confirms [sensory:2] is absent from
        @16; the cite-index confirms sensory:2 back=Y @9.
        (b) state:5 was DELETED in cycle-1 state-updates remediation
        (and-facets-cycle1-fixes-state-updates.md, fault-SU-002). state:5 no
        longer exists in any state-updates slice or the consolidated file.
        The citation-completeness check at the bottom of the sidecar
        ("entry 3 cites sensory:2 @16 + state:5 @17") reflects the pre-cycle-1
        state of the graph and was not updated when cycle-1 fixes landed.
      why: >
        rubric-dialogue.md CONSTRAINT §citation-completeness, clause promoted
        from URI-FACETS-CYCLE-1: "Every facet-licenses citation must resolve to
        an actual entry on disk ... A citation that names an anchor where the
        cited facet does not fire (cite-index walk fails to resolve) is HARD per
        entry." Both citations in entry 3's facet-licenses fail:
        sensory:2 @16 fails because sensory:2 no longer fires at @16 (cite-index
        walk: sensory:2 back=Y @9, not @16); state:5 @17 fails because state:5
        is deleted (cite-index walk: no state:5 entry). HARD for each broken
        citation, both in the same entry. This is a post-cycle-1-fix citation-
        staleness failure — the sidecar's citation-completeness summary was not
        updated when cycle-1 changes landed on the sensory and state-updates facets.
      criteria: >
        Entry 3 facet-licenses must resolve against the current locked graph.
        sensory:2 @16 must be replaced with sensory:2 @9 (the current anchor per
        cycle-1 sensory fix) or an alternative resolvable citation. state:5 @17
        must be removed (deleted entry; cannot be cited). If the entry retains a
        facet-license citation, fixer must verify it resolves via cite-index walk.
        If no resolvable facet-license remains for entry 3, the citation-
        completeness axis may show a SIGNAL gap (one axis populated, one empty)
        rather than HARD — auditor notes this is fixer's determination to make after
        the broken citations are cleared.

    - id: fault-C2-003
      type: fault
      what: >
        _cite-index.md header reports: vibes section "10 entries" and totals
        "41 facet entries (44 original minus 4 state-updates deletions plus 1
        loc-state addition in cycle-1)". The vibes facet file (vibes-b01-c01.md)
        contains 12 entries after cycle-1 vibes additions (vibes:11 ADD-LANDED
        and vibes:12 ADD-LANDED per and-facets-cycle1-fixes-vibes.md SESSION-END).
        The cite-index does not reflect vibes:11 or vibes:12. Neither entry
        appears in the cite-index per-facet vibes section. The density distribution
        table carries a header note "pending regeneration" but does not account
        for the two new vibes entries in the totals or per-facet counts. Correct
        total should be 43 (41 + 2 new vibes entries), not 41.
      why: >
        The cite-index is the canonical reference for cite-index DAG validation
        and for /and-stitch Phase 0 hash check. A cite-index that does not
        enumerate vibes:11 and vibes:12 means: (a) back=Y has not been asserted
        for either new entry; (b) their proto-line anchor back-links and co-citation
        lists are missing; (c) pile-up count at @12 and @21 is understated (vibes:11
        fires at @12 adding to the 5-entry pile-up; vibes:12 fires at @21 adding to
        the 6-entry pile-up); (d) the vibes:11 fixer log names state:4 as a
        licensed-by source, which is already a fault (fault-C2-001), but that fault
        can only be properly tracked if vibes:11 appears in the cite-index with
        correct back-links; (e) /and-stitch Phase 0 re-hash will fail if the
        cite-index used for hashing does not match the file on disk.
      criteria: >
        _cite-index.md must be updated to include vibes:11 and vibes:12 with
        correct per-entry lines (anchor, back=Y, co-list), updated totals (41→43),
        updated vibes section entry count (10→12), and updated pile-up records
        for @12 (now 6 entries: narrator:4, state:3, vibes:3, vibes:4, vibes:8,
        vibes:11) and @21 (now 7 entries: exposition:8, feel:1, narrator:5, state:1,
        vibes:5, vibes:6, vibes:7, vibes:12). The density distribution table must
        be regenerated or the "pending" note resolved. The cite-index totals line
        must be corrected.

    - id: fault-C2-004
      type: fault
      what: >
        memory-b01-c01.md R2 stamp (lines 11-18) contains the text: "co-cited with
        state:2 + state:6 confirming graph spine of the categorization event."
        state:6 was DELETED in cycle-1 state-updates remediation
        (and-facets-cycle1-fixes-state-updates.md, fault-SU-003). The R2 stamp's
        citation of state:6 as spine confirmation is stale. The current graph
        shows mem:2 @26 back=Y co=[narrator:9, state:2] — state:6 is absent from
        the co-list.
      why: >
        The R2 stamp is the authoritative per-facet decision record read by
        /and-facets Phase 6 orchestrator-critic verdict and by downstream consumers
        of `.r2-decisions.md`. A stamp that cites a deleted entry as spine
        confirmation contradicts the current cite-index co-list for mem:2 and
        will cause confusion for any audit or reviewer reading the stamp after
        cycle-1. While mem:2's spine is now correctly provided by narrator:9 @26
        (confirmed in the fixer log and cite-index), the stale stamp must be
        corrected to not reference state:6 as a spine source.
      criteria: >
        memory-b01-c01.md R2 stamp entry for mem:2 must be corrected: replace
        "co-cited with state:2 + state:6 confirming graph spine" with the current
        graph state — co-cited with narrator:9 @26 (NI spine, added by cycle-1
        memory fix) and state:2 @26. The deletion of state:6 and the addition of
        narrator:9 as the correct spine must be reflected in the stamp body.

    - id: flag-C2-001
      type: flag
      what: >
        sensory-b01-c01.md carve-out header claims the unanchored-old-state
        exemption on the basis that "no loc-state file entries exist for b01c01."
        This was the factual basis at the time of original sensory authoring.
        cycle-1 loc-state remediation added loc-state:1 @1 (oc-stitch-house-lane |
        morning | none | stitch-house-lamp-burning | drain-water trickle audible
        at the angle-gap pinch-point). The carve-out header has not been updated
        to reflect that a loc-state entry now exists.
      why: >
        The carve-out rationale ("treat scene-internal sensory anchors as
        scene-tier sensory when the locations: header is empty") was predicated
        on an empty loc-state. Now that loc-state:1 @1 exists, the rubric's
        preferred old-state lineage for sensory entries is from the loc-state
        baseline, not from scene-internal inference. The sensory entries themselves
        are not broken — sensory:1 @2 sourcing from bone-1-pre-smoke remains
        correct (loc-state:1 records lamp-burning and drain-water trickle, no smoke
        baseline; smoke onset at @2 is the first smell event, consistent with the
        loc-state), and sensory:2 @9 tactile old-state sourcing from bones-1-8-
        occupancy is consistent with loc-state:1's implicit crowd-not-yet-compressed
        ambient. However, the carve-out header should be updated to reflect the
        current factual state: loc-state is no longer empty; the carve-out applies
        narrowly because loc-state:1 does not establish a prior sensory entry on
        the smell or tactile modalities, so the lineage resolution for the first
        fire on each modality still falls to scene-internal context.
      why: >
        If the sensory carve-out header is read by a future auditor or the stitcher
        without knowing the loc-state has changed, it will appear to rest on an
        incorrect factual premise. Advisory only — no rubric constraint is currently
        broken; the practical effect is correct. No fixer dispatch required; update
        recommended at the next sensory or loc-state touch.

    - id: flag-C2-002
      type: flag
      what: >
        _cite-index.md pile-up section records @21 as having "(6)" entries:
        exposition:8, feel:1, narrator:5, state:1, vibes:5, vibes:6, vibes:7.
        The feel:3 deletion in cycle-1 feeling remediation (removed feel:3 @24,
        not @21) does not affect the @21 pile-up count. However, state:6 was
        deleted and had back=Y @21 co-listed against the @21 pile-up members
        (state-updates fixer log confirms: state:6 @21 deleted, "state:1 co-list
        updated to remove state:6; narrator:5 co-list updated to remove state:6;
        feel:1 co-list updated to remove state:6; vibes:5/6/7 co-lists updated
        to remove state:6; exposition:8 co-list updated to remove state:6").
        The pile-up section itself does not name state:6 in the @21 pile-up (it
        lists 6 entries, which is correct post-deletion: state:6 is absent), so
        the pile-up count is actually already correct at 6 for the current graph
        state. This finding confirms the @21 pile-up is consistent with the
        current graph.
      why: >
        Informational. @21 pile-up count of 6 is correct for the post-cycle-1 state
        (state:6 was the deleted 7th member; the pile-up section already lists only
        the surviving 6). When vibes:12 @21 is added per fault-C2-003, the @21
        pile-up will rise to 7 again. No action required beyond the cite-index
        update mandated by fault-C2-003.

    - id: flag-C2-003
      type: flag
      what: >
        state-updates fixer log (and-facets-cycle1-fixes-state-updates.md) records
        a cross-facet-impact note: "narrator-interest author MUST add @17 NI entry
        before state:5 (taylor.posture) can be re-added; @17 is now a bare
        protoline." The state:5 deletion was a direct consequence of the rubric's
        POV co-citation contract (POV actor-state requires NI co-citation at the
        same anchor). @17 is confirmed bare in the current cite-index. No NI entry
        at @17 exists in interest-narrator-b01-c01.md (entries are: @4, @8, @11,
        @12, @21, @27, @3, @24, @26 — no @17 entry). This means the posture
        state-change at bone 17 ("taylor lifts the hands") — identified in the
        fixer log as "the chapter's key public-frame transition" — has no
        state-updates coverage and no NI coverage.
      why: >
        The public-frame transition at @17 is substantively load-bearing per the
        fixer log's own characterization. The bare-protoline at @17 with no NI and
        no state coverage means the stitcher has no facet signal at this bone.
        This is advisory — the deletion was correct, and the re-add path is
        documented. The gap will persist until an NI entry is authored at @17 and
        state:5 is re-authored. The parking lot or a future narrator-interest
        authoring pass should address this. Not a blocking fault for the current
        cycle; state:5's re-add path is explicitly flagged for the NI author.

    - id: flag-C2-004
      type: flag
      what: >
        vibes-b01-c01.md entry 12 — licensed-by cites proto:26 as a licensing
        source. The cite-index pile-up section shows vibes:9 @27 co includes
        lic-out=[proto:27, proto:2, proto:25] and vibes:10 @27 co includes
        lic-out=[proto:27, proto:2, proto:15], but no lic-out to proto:26 from
        these entries. vibes:5 @21 has lic-out=[proto:21, proto:26] and vibes:12
        @21 licenses through proto:21 and proto:26. proto:26 is bone 26
        "oswyn-mudway-flea-bottom-elder lifts the chin" — on-screen beat. The
        licensed-by citation of proto:26 for vibes:12 (which fires @21) means
        the entry is licensed partly by a downstream protoline (proto:26 fires
        after vibes:12's anchor @21). This is not a hard-fence violation under
        rubric-vibes.md (licensed-by may cite any proto-line), but it creates a
        forward-looking license where the vibe fires at @21 but is grounded in
        part by a beat that occurs at @26. Since vibes:5 also uses this same
        pattern (licensed-by includes proto:21 and proto:26 while anchored @21),
        it appears to be an established pattern for this episode. Advisory for
        the fixer to review whether the forward-license is intentional.
      why: >
        Advisory. The forward-citation pattern for vibes:12 mirrors vibes:5 and
        is therefore consistent with established authoring practice in this file.
        No rubric gate bars forward proto-line citations in licensed-by. Noting
        for completeness; no action required unless the vibes author wishes to
        revise the licensing basis.

    - id: flag-C2-005
      type: flag
      what: >
        memory-b01-c01.md carries flag-013 (SIGNAL from all three cycle-1 reviewers
        per fixer log and-facets-cycle1-fixes-memory.md) on both entries:
        mem:1 targets cond-override-architecture-residue-122ac (expected
        monument-* form per URI-032); mem:2 targets cond-kl-witch-label-formation-122ac
        (expected monument-* form). The fixer documented a margit referral as
        required. No margit referral has landed in this cycle. The SIGNAL persists.
      why: >
        rubric-memory-flags.md §Licensing-discipline cross-axis test (monument-card
        resolution): "Every memory-flag entry's target-reference must name a monument
        card slug that resolves in the card library via margit referral. A bare gloss
        text in target-reference without a margit-resolved slug fails the
        licensing-discipline axis: the monument is asserted, not anchored. SIGNAL if
        the gloss is structurally clear and the card is queued; HARD if the gloss is
        opaque and no margit referral exists." Both entries use cond-* form rather
        than monument-* form. All three reviewers rated SIGNAL. Fixer correctly
        carried forward as SIGNAL and flagged for margit. Margit referral has not
        been executed in this cycle. This SIGNAL persists until margit either
        (a) authors monument-class cards for both targets, or (b) confirms cond-*
        form is canonical for this slug class and updates URI-032 rubric accordingly.
        Advisory; does not block Phase 5 clearance.
```

---

## Audit summary

```yaml
hard_count: 4
signal_count: 5
hard_findings:
  - fault-C2-001: vibes:11 licensed-by cites deleted state:4 (dangling citation, rubric gate 4 fail)
  - fault-C2-002: sidecar entry 3 facet-licenses cite sensory:2 @16 (moved to @9) + state:5 @17 (deleted); both resolve failures per dialogue CONSTRAINT §citation-completeness
  - fault-C2-003: cite-index does not reflect vibes:11 or vibes:12 ADD; vibes count off (10 vs 12); totals off (41 vs 43); pile-up sections stale for @12/@21
  - fault-C2-004: memory-b01-c01.md R2 stamp cites deleted state:6 as spine confirmation for mem:2
signal_findings:
  - flag-C2-001: sensory carve-out header factual premise stale (loc-state now exists); no rubric breach; advisory update recommended
  - flag-C2-002: cite-index @21 pile-up count confirmed correct (6, not 7); informational
  - flag-C2-003: @17 bare-protoline gap (no NI, no state coverage at bone 17 — public-frame transition); re-add path documented but not yet executed
  - flag-C2-004: vibes:12 forward-license on proto:26 advisory (consistent with vibes:5 pattern; no rubric gate bars forward citation)
  - flag-C2-005: flag-013 margit referral (monument-class slug form) persists on mem:1 + mem:2 target-references; SIGNAL only; fixer carried forward correctly; margit referral not yet landed
routing: HARD > 0 — route to fixer; cycle-2 audience-gate does not fire until all 4 HARDs are cleared
```
