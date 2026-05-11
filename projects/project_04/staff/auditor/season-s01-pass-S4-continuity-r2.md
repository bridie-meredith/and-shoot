```yaml
audit:
  scope: season
  target: s01
  pass: S4-continuity-r2
  timestamp: 2026-05-09
  verdict: SEASON-CONTINUITY-OK
  prior-audit: season-s01-pass-S4-continuity.md (SEASON-CONTINUITY-OK; 1 fault S4-S-001 + 7 advisory flags)
  note: >
    Re-verification pass. Scope limited to: (1) S4-S-001 closure confirmation via bone 925,
    and (2) state/reference/POV sweep of new bones 925–933. All four prior-audit sweeps
    (reachability, state, reference, POV) remain unmodified in their verdicts unless a new
    bone disturbs a prior finding. No prior findings are revisited except S4-S-001.

  findings:

    # ── S4-S-001 CLOSURE VERIFICATION ─────────────────────────────────────────

    - id: R2-CLOSE-001
      type: pass
      what: >
        Bone 925 (insert-at: 217): `taylor-hebert-jaehaerys lays the volume`.
        Bone 217 is `taylor-hebert-jaehaerys exits the sept`. Insert-at convention
        places bone 925 immediately after bone 217 in sequential read order, making
        the exterior sept lane the disposition site. Sequence: 217 (exits sept) →
        925 (lays the volume) → 218 (gap). The gifted volume (bones 206–208 open,
        217 exit carrying) now has a recorded disposition at the earliest subsequent
        bone after Taylor's sept exit.
      why: >
        S4-S-001 fault criteria required a recorded disposition before or at the
        moment Taylor exits, or at the earliest subsequent bone where Taylor's
        possession state is established. Bone 925 satisfies the "earliest subsequent
        bone" condition. The prop chain closes: take at 207 → grip at 208 → exit
        carrying at 217 → lay at 925. No downstream ambiguity remains.
      routing: ~

    # ── NEW BONES 925–933: STATE SWEEP ────────────────────────────────────────

    - id: R2-S-001
      type: pass
      what: >
        Bone 925 SVO form: `taylor-hebert-jaehaerys lays the volume`. Subject
        (actor slug), verb (concrete physical action), object (named prop). No
        copula, no negation, no modifier. Form is clean.
      why: ~
      routing: ~

    - id: R2-S-002
      type: pass
      what: >
        Bone 926 (insert-at: 126): `taylor-hebert-jaehaerys enters the workshop`.
        Taylor is established in the workshop context from earlier in the aggregate
        (bones 4, 20, 84, 102 sequence). Frame-anchor placing Taylor in the workshop
        before bone 127 (oc-craftsman-mother speaks to oc-craftsman-father) is
        location-coherent and state-consistent.
      why: ~
      routing: ~

    - id: R2-S-003
      type: pass
      what: >
        Bone 927 (insert-at: 219): `taylor-hebert-jaehaerys reaches the sept lane`.
        Taylor has just exited the sept at bone 217 and laid the volume at bone 925.
        The sept lane is the exterior space adjacent to the sept. Bone 927 restores
        content at the gap position previously identified as absent ID 219 (S4-REF-003).
        Location is coherent with the exit-then-walk-home narrative at this position.
      why: ~
      routing: ~

    - id: R2-S-004
      type: pass
      what: >
        Bone 928 (insert-at: 233): `taylor-hebert-jaehaerys enters the sept`. The
        aggregate at 234 opens with `septon-rowan draws a volume` and the subsequent
        scene (234–250) is a literacy-test beat in the sept. Taylor is confirmed at
        home/workshop between bones 220–232 (post-sept exchange with Elara), so a
        re-entry bone before 234 is location-coherent. Form is clean SVO.
      why: ~
      routing: ~

    - id: R2-S-005
      type: pass
      what: >
        Bones 930 (insert-at: 43), 931 (insert-at: 51), 932 (insert-at: 618): all
        three are blank numbered lines (time-skip markers with no content). Schema
        permits blank numbered lines as time-skip markers. No state implications.
      why: ~
      routing: ~

    - id: R2-S-006
      type: pass
      what: >
        Bone 933 (insert-at: 300): `taylor-hebert-jaehaerys holds the face`. The
        `holds the face` form is established across the aggregate at bones 303, 321,
        and 637 — all existing bones, not new. Form is consistent with the narrow
        `holds` license (body part of subject, stillness-against-pressure). Taylor
        is in the market square at bones 298–327; the insert at 300 is location-
        coherent.
      why: ~
      routing: ~

    # ── NEW BONES 925–933: REFERENCE SWEEP ────────────────────────────────────

    - id: R2-REF-001
      type: pass
      what: >
        All insert-at anchor bones for the new set (925–933) are present in the
        aggregate: 217 (present), 126 (present), 219 (absent but referenced as the
        "restores gap" position — insert-at 219 is a positional marker not requiring
        bone 219 to exist), 233 (present), 43 (present), 51 (present), 618 (present),
        300 (present). All FIX annotations resolve to the fault IDs or plan labels
        they cite (FIX-4 → S4-S-001; FIX-5-E/G/H/O → S7 fault-001 through 004;
        FIX-7a/b/c → S7 fault-006/007; FIX-8 → S7 fault-008). No orphan inserts.
      why: ~
      routing: ~

    # ── NEW BONES 925–933: POV SWEEP ──────────────────────────────────────────

    - id: R2-POV-001
      type: flag
      what: >
        Bone 929 (insert-at: 564): `mira-stonefield-jaehaerys enters the alley`.
        Annotation labels it "mira-POV frame-anchor; establishes alley location
        under mira POV." The POV switch from Taylor to Mira (`# pov: mira-
        stonefield-jaehaerys`) appears in the aggregate at line 620, immediately
        before bone 565. Insert-at 564 places bone 929 after the gap bone 564 and
        before the POV switch line — making bone 929 the last bone under Taylor's
        POV, not the first under Mira's POV. The annotation's "under mira POV"
        claim is therefore imprecise: the bone lands under Taylor's POV. The action
        itself (Mira entering the alley) is observable from Taylor's POV — Taylor
        follows Mira into the alley at bone 563, so Mira's entry at bone 929 is
        both location-coherent and POV-permissible under Taylor. No POV violation
        exists. The annotation mislabels the POV regime the bone lands in.
      why: >
        If Phase 4 split uses the annotation label to determine which POV block
        contains bone 929, it will attribute the bone to the Mira interlude rather
        than the Taylor-POV pre-switch zone. The bone itself is clean; the annotation
        is the confusion risk. Advisory to Phase 4 split operator to treat bone 929
        as a Taylor-POV bone when computing interlude boundaries. Prior finding
        S4-POV-003 (Mira interlude range 565–643 must not be bisected) is not
        affected — bone 929 lands outside that range.
      routing: Phase 4 split operator (advisory)

    - id: R2-POV-002
      type: pass
      what: >
        Bones 925, 926, 927, 928, 933 all occur within established Taylor-POV
        zones. Bone 925 is at the sept exit (Taylor-POV throughout the sept scene,
        bones 151–217). Bone 926 is at the workshop morning zone (Taylor-POV,
        bones 1–151). Bone 927 is between bones 217 and 220 (Taylor-POV). Bone 928
        is between bones 233 and 234 (Taylor-POV). Bone 933 is at bones 298–327
        (Taylor-POV). No POV violations in any of these five.
      why: ~
      routing: ~
```

---

## Summary

**File-level verdict: SEASON-CONTINUITY-OK**

**S4-S-001 closure:** Confirmed closed. Bone 925 (`taylor-hebert-jaehaerys lays the volume`, insert-at 217) places a volume disposition bone immediately after Taylor's sept exit, satisfying the fault criteria. The prop chain from take (207) through exit-carrying (217) to lay (925) is complete.

**Bones 925–933 sweep:** No new faults. One advisory flag (R2-POV-001): bone 929's annotation claims "under mira POV" but the bone lands under Taylor's POV per the aggregate's POV switch position. The bone itself is location-coherent and POV-permissible; the annotation mislabels the regime. Routed to Phase 4 split operator as advisory. All other new bones are state-clean, reference-clean, and POV-clean.

Prior findings S4-R-002, S4-R-004, S4-S-002, S4-S-005, S4-REF-003, S4-POV-003, S4-POV-004 remain open and unmodified. No new faults introduced by fixer round 10.
