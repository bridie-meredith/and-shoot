```yaml
audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-25
  cycle: 2-confirm
  prior_audit: active-project/staff/auditor/facets-cycle2-audit.md
  fixer_log: active-project/staff/fixer/and-facets-cycle2-phase5-fixes.md
  mode: confirmatory re-audit after cycle-2 Phase 5 fixer pass; verification of 4 HARD resolutions + second-order propagation scan + eleven-class spot-check
  findings:

    - id: pass-C2C-001
      type: pass
      what: >
        fault-C2-001 (vibes:11 licensed-by citing deleted state:4).
        Current vibes-b01-c01.md line 50: vibes:11 licensed-by shows
        "proto:12, proto:13, state:3" — state:4 is absent.
        Current _cite-index.md line 78: vibes:11 lic-out=[proto:12, proto:13, state:3] —
        state:4 is absent. All three remaining sources resolve to live entries in the
        cite-index (proto:12 and proto:13 on-screen bones; state:3 @12 back=Y confirmed).
        Rubric-vibes.md gate 4 satisfied.
      why: >
        Fault-C2-001 criteria met. No residual breakage.

    - id: pass-C2C-002
      type: pass
      what: >
        fault-C2-003 (cite-index missing vibes:11 and vibes:12 registrations).
        Current _cite-index.md: vibes section header shows 12 entries; vibes:11 @12
        back=Y co=[narrator:4, state:3, vibes:3, vibes:4, vibes:8]
        lic-out=[proto:12, proto:13, state:3] present; vibes:12 @21 back=Y
        co=[exposition:8, feel:1, narrator:5, state:1, vibes:5, vibes:6, vibes:7]
        lic-out=[proto:21, proto:26] present. Totals header: 43 entries confirmed.
        Pile-up @12 (6): narrator:4, state:3, vibes:3, vibes:4, vibes:8, vibes:11 — correct.
        Pile-up @21 (8): exposition:8, feel:1, narrator:5, state:1, vibes:5, vibes:6,
        vibes:7, vibes:12 — correct member list.
        Co-list propagation at @12 verified: all five co-members' co-lists include vibes:11.
        Co-list propagation at @21 verified: all seven co-members' co-lists include vibes:12.
        Density distribution table regeneration note present.
      why: >
        Fault-C2-003 criteria met. The cite-index now enumerates vibes:11 and vibes:12 with
        correct back-links and co-list propagation. No residual breakage.

    - id: pass-C2C-003
      type: pass
      what: >
        fault-C2-004 (memory-b01-c01.md R2 stamp citing deleted state:6 as spine).
        Current memory-b01-c01.md R2 stamp lines 11-20: mem:2 stamp now reads
        "co-cited with narrator:9 @26 (NI spine, added cycle-1 memory fix: [NI text])
        + state:2 @26 confirming graph spine of the categorization event; state:6 deleted
        in cycle-1 state-updates remediation (invented field + ledger-as-state) — narrator:9
        is the current spine carrier." No reference to state:6 as a spine confirmation source.
        The stamp correctly names narrator:9 as the NI spine carrier per the current
        cite-index co-list (mem:2 @26 co=[narrator:9, state:2]).
      why: >
        Fault-C2-004 criteria met. The R2 stamp is consistent with the current cite-index
        co-list. No residual breakage.

    - id: fault-C2C-001
      type: fault
      what: >
        fault-C2-002 — INCOMPLETELY REMEDIATED. The fixer's C2-002 resolution corrected
        entry 3 of the sidecar (taylor-hebert-kl-122ac.drafts.md) but left entries 1 and 2
        with unresolvable sensory:2 @16 citations.

        Entry 1 facet-licenses (sidecar line 54):
          "sensory:2 @16 (sound: crowd-ambient-murmur -> taylor-raised-voice — ...
          co-cited with this entry at @16 in the locked cite-index)"

        Entry 2 facet-licenses (sidecar line 85):
          "sensory:2 @16 (sound: crowd-ambient-murmur -> taylor-raised-voice — ...
          co-cited at the anchor)"

        Cite-index walk for both: sensory:2 back=Y @9, NOT @16. Proto-lines @16 carries
        only [taylor-hebert-kl-122ac:1] [taylor-hebert-kl-122ac:2] [taylor-hebert-kl-122ac:3]
        — no [sensory:2] decoration at @16. The citation "sensory:2 @16" does not resolve
        in the cite-index.

        The fixer's citation-completeness summary (sidecar line 138) acknowledges both
        citations but classifies them as "SIGNAL gap — anchor-association citation to the
        same speech-act protoline, distinct from the sensory:2 back=Y registration at @9."
        This self-classification is incorrect under the rubric. rubric-dialogue.md
        §V2 facet-citation extension states: "A citation that names an anchor where the
        cited facet does not fire (cite-index walk fails to resolve) is HARD per entry."
        The rubric contains no carve-out for "anchor-association citations." The only
        operative test is cite-index walk resolution. sensory:2 does not fire at @16;
        cite-index walk fails; the finding is HARD, not SIGNAL, for each of the two entries.

        Entry 1 retains a second citation (state:3 @12) that does resolve (state:3 @12
        back=Y confirmed). So entry 1's citation-completeness failure is limited to the
        broken sensory:2 @16 citation, not total loss of facet-license.

        Entry 2 retains no other citation after the sensory:2 @16 failure. Entry 2's
        sole facet-license is the broken citation, leaving it with no valid facet-license
        on the sensory axis and no other axis populated. Missing one axis: SIGNAL per the
        rubric hierarchy, but the citation that was meant to fill that axis fails HARD.
      why: >
        rubric-dialogue.md CONSTRAINT §citation-completeness: "A citation that names an
        anchor where the cited facet does not fire (cite-index walk fails to resolve) is
        HARD per entry." Two entries carry the broken citation; two HARD counts. The fixer's
        classification as SIGNAL did not change the broken state of the citations on disk;
        it only misclassified them. The cycle-2 fixer pass introduced this as a
        second-order fault by resolving entry 3 and leaving entries 1 and 2 in the same
        pre-cycle-1 broken state while documenting a non-rubric-grounded SIGNAL classification
        as cover. The audience-gate cannot fire while entries 1 and 2 carry broken
        facet-license citations under this rubric.
      criteria: >
        Both entry 1 and entry 2 facet-licenses must be corrected so that every cited
        sensory:2 anchor resolves via cite-index walk. For each entry, sensory:2 @16 must
        be replaced with a citation that resolves — either sensory:2 @9 (as was done for
        entry 3) on the same basis the fixer used (the crowd-compression perceptual surface
        active through @9-@16 supports the speech-act that entries 1 and 2 carry), or a
        different resolvable facet-license citation for each entry. The fixer must verify
        that each corrected citation passes cite-index walk on the chosen anchor. The
        citation-completeness summary at the bottom of the sidecar must be updated to
        reflect the corrected state of all three entries without carrying forward the
        non-rubric-grounded "anchor-association" characterization.

    - id: flag-C2C-001
      type: flag
      what: >
        _cite-index.md pile-up @21 count discrepancy between prior audit records and
        current state. flag-C2-002 in the cycle-2 prior audit confirmed "@21 pile-up
        count of 6 is correct for the post-cycle-1 state." But the pre-vibes:12 @21
        members enumerated in fault-C2-003 criteria list 7 surviving members
        (exposition:8, feel:1, narrator:5, state:1, vibes:5, vibes:6, vibes:7) after
        state:6 deletion from an original 8-member pile-up. The fixer implemented @21
        as (8) post-vibes:12, which matches the named member list. The discrepancy
        between the flag-C2-002 "6" count and the 7-member pre-vibes:12 list cannot
        be fully traced without access to the feeling facet file (feel-* file not
        found on disk during this audit). The current cite-index @21 count of 8 is
        internally consistent with all co-lists. No blocking inconsistency observed.
      why: >
        Advisory. The current @21 pile-up is internally self-consistent in the cite-index
        (all 8 members' co-lists corroborate membership). The "6" in flag-C2-002 may
        reflect a prior-state snapshot at a different cycle point, or the feeling facet
        file carries a deletion not captured here. No rubric gate is currently broken.
        If the feeling facet file is accessible in a later session, the pre-cycle-1
        @21 count should be reconciled with the flag-C2-002 note.

    - id: flag-C2C-002
      type: flag
      what: >
        The dialogue sidecar (taylor-hebert-kl-122ac.drafts.md) and the exposition
        facet file (exposition-b01-c01.md) both carry cite_index_hash
        0241e0529031804fa83d25c0fb7a5e0db2491571d2d83d9d9436c734627eca40 as their
        R2-resolution anchor. This is the original pre-cycle-1 hash. The cycle-2
        fixer pass made structural changes to _cite-index.md (adding vibes:11/12,
        updating co-lists, correcting pile-up counts). The current cite-index no
        longer matches this hash.
      why: >
        Advisory. The cite_index_hash fields in R2 decision shards are used by
        /and-facets Phase 3 cross-session stale-shard check. Stale hashes in the
        sidecar and exposition file do not constitute a Phase 5 rubric fault but
        will trigger stale-shard warnings at any subsequent /and-facets invocation.
        The hash fields will need updating if a Phase 3 re-run is performed. No
        blocking issue at current Phase 5 gate.

    - id: flag-C2C-003
      type: flag
      what: >
        Carried forward from prior audit: flag-C2-001 (sensory carve-out header
        factual premise stale), flag-C2-003 (@17 bare-protoline gap; no NI, no state
        coverage at bone 17), flag-C2-004 (vibes:12 forward-license on proto:26),
        flag-C2-005 (flag-013 margit referral on mem:1 + mem:2 monument-slug form).
        None of these flags changed state in the cycle-2 fixer pass. All four remain
        open as advisory signals. No cycle-2 remediation created new instances of
        these patterns.
      why: >
        No new rubric breaches. Prior flags persist unmodified. See facets-cycle2-audit.md
        flag-C2-001 through flag-C2-005 for detail.
```

---

## Audit summary

```yaml
hard_count: 1
signal_count: 3
prior_faults_verified:
  fault-C2-001: RESOLVED — vibes:11 licensed-by state:4 citation removed; three remaining sources resolve
  fault-C2-002: NOT FULLY RESOLVED — see fault-C2C-001; entry 3 fixed; entries 1 and 2 retain sensory:2 @16 (unresolvable, HARD per rubric)
  fault-C2-003: RESOLVED — vibes:11 and vibes:12 registered in cite-index; co-lists propagated; pile-ups updated; totals correct
  fault-C2-004: RESOLVED — memory R2 stamp no longer references state:6; narrator:9 named as spine carrier

new_hard_findings:
  - fault-C2C-001: >
      sidecar entries 1 and 2 retain sensory:2 @16 citations that fail cite-index walk
      (sensory:2 fires at @9, not @16; proto-lines @16 carries no sensory:2 decoration).
      Fixer misclassified these as SIGNAL under a non-rubric-grounded "anchor-association"
      concept. rubric-dialogue.md §citation-completeness: cite-index walk failure is HARD
      per entry. Two entries; two HARD instances. Second-order propagation from C2-002
      partial fix.

signal_findings:
  - flag-C2C-001: @21 pile-up count discrepancy (flag-C2-002 said "6" pre-vibes:12; member list implies 7); internally consistent now; advisory; feeling facet file not accessible
  - flag-C2C-002: cite_index_hash in sidecar + exposition file is pre-cycle-1 hash; stale after cycle-2 cite-index edits; Phase 3 stale-shard warning will fire on next invocation
  - flag-C2C-003: prior flags C2-001/002/003/004/005 carried forward unchanged; no new instances

routing: >
  HARD > 0. fault-C2C-001 routes to fixer: correct entries 1 and 2 in
  active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md.
  Audience-gate does NOT fire until fault-C2C-001 is resolved.
  Faults C2-001, C2-003, C2-004 cleared; C2-002 partial — the per-entry scope of
  C2-002 was narrower than the full breakage in the sidecar.
```
