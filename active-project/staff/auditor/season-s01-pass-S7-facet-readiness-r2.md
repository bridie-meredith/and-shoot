audit:
  scope: season
  target: s01 aggregate (active-project/theater/proto-lines/s01.aggregate.md)
  timestamp: 2026-05-09
  pass: FACET-READY
  prior_pass: FACET-GAPS (season-s01-pass-S7-facet-readiness.md)
  fixer_round: 10

  verification:

    # --- FRAME-ANCHOR INSERTS (IDs 926-929) ---

    - id: verify-926
      type: pass
      what: ID 926 — insert-at 126 — `taylor-hebert-jaehaerys enters the workshop` — inserts before beat 127, establishing workshop as active location for Scene E
      why: Prior fault-001 criteria satisfied; frame-anchor now exists at or before beat 127

    - id: verify-927
      type: pass
      what: ID 927 — insert-at 219 — `taylor-hebert-jaehaerys reaches the sept lane` — inserts at gap position 219, before beat 220, naming a slug-resolved exterior location for Scene G
      why: Prior fault-002 criteria satisfied; exterior location now anchored for Scene G open

    - id: verify-928
      type: pass
      what: ID 928 — insert-at 233 — `taylor-hebert-jaehaerys enters the sept` — inserts before beat 234, re-establishing the sept as active location for Scene H after Scene G exterior
      why: Prior fault-003 criteria satisfied; re-entry beat now exists at or before beat 234

    - id: verify-929
      type: pass
      what: ID 929 — insert-at 564 — `mira-stonefield-jaehaerys enters the alley` — inserts at gap position 564, immediately before the mira POV segment opens at beat 565
      why: Prior fault-004 criteria satisfied; alley location now anchored under mira POV at scene open

    # --- DIALOGUE SLUG RESOLUTION (354 / 398) ---

    - id: verify-354-398
      type: pass
      what: Beat 354 now reads `oc-lords-steward calls`; beat 398 now reads `oc-lords-steward calls` — listener slug `the dock crowd` removed from both
      why: Prior fault-005 criteria satisfied; both beats are now intransitive proclamation beats carrying no listener slug, removing the unresolvable-listener-card fault

    # --- OVER-DENSE REGIONS (32-60 and 599-626) ---

    - id: verify-930-931
      type: pass
      what: IDs 930 and 931 — blank time-skip inserts at positions 43 and 51 — two internal markers now break the 32-60 range into sub-scenes; first break after the ruffles-hair cluster, second at the tallow-lamp/candle sequence open
      why: Prior fault-006 criteria satisfied; at least 2 internal time-skip markers now present in the 32-59 range

    - id: verify-932
      type: pass
      what: ID 932 — blank time-skip insert at position 618 — one internal marker now breaks the 599-626 range at the folio-marking procedural commit
      why: Prior fault-007 criteria satisfied; at least 1 internal time-skip marker now present in the 599-626 range

    # --- UNDER-DENSE STRETCH (299-301) ---

    - id: verify-933
      type: pass
      what: ID 933 — insert-at 300 — `taylor-hebert-jaehaerys holds the face` — content beat inserted between beats 298 and 302, anchoring Taylor's passive-perception state during the fence-climb interval
      why: Prior fault-008 criteria satisfied; at least 1 content beat now exists in the 299-301 interval; holds licensed (body-part subject, stillness-against-pressure)

    # --- NEW BONES WALK (IDs 926-933) ---

    - id: new-bones-926
      type: pass
      what: ID 926 `taylor-hebert-jaehaerys enters the workshop` — clean SVO, physical motion verb, slug-resolved location as direct object; no introduced continuity gap; Taylor's last explicit exit prior to Scene E was within workshop/yard context
      why: No facet-readiness fault introduced

    - id: new-bones-927
      type: pass
      what: ID 927 `taylor-hebert-jaehaerys reaches the sept lane` — transitive form, `reaches` takes `the sept lane` as direct object; consistent with Taylor exiting the sept at beat 217; exterior location coherently placed at gap position 219
      why: No facet-readiness fault introduced; `reaches <destination>` is a valid transitive arrival form per schema

    - id: new-bones-928
      type: pass
      what: ID 928 `taylor-hebert-jaehaerys enters the sept` — clean SVO; correctly placed after Scene G exterior (oc-craftsman-mother enters the workshop at beat 232); Taylor's transition from sept lane to sept interior is now explicit
      why: No facet-readiness fault introduced

    - id: new-bones-929
      type: pass
      what: ID 929 `mira-stonefield-jaehaerys enters the alley` — clean SVO; placed at gap position 564 immediately after beat 563 (taylor follows mira) and immediately before the mira POV segment; coherent directional continuation
      why: No facet-readiness fault introduced

    - id: new-bones-930-932
      type: pass
      what: IDs 930, 931, 932 — blank numbered time-skip lines; valid per schema; introduce no content and cannot produce SVO faults
      why: No facet-readiness fault introduced

    - id: new-bones-933
      type: pass
      what: ID 933 `taylor-hebert-jaehaerys holds the face` — `holds` licensed under narrow holds license (body part of subject, stillness-against-pressure); consistent with existing pattern at beats 321, 395, 637, 700; no introduced continuity gap
      why: No facet-readiness fault introduced

    # --- INHERITED ADVISORY FLAGS (UNCHANGED FROM R1) ---

    - id: carry-flag-001
      type: flag
      what: Scene G (beats 220-232) — no environmental sensory-inflection beat; advisory from prior audit; ID 927 adds a location frame-anchor only, does not add a sensory beat
      why: Carried forward; not a facet-readiness fault; advisory for editor/dramatist

    - id: carry-flag-002
      type: flag
      what: Scene M (beats 521-540) — no non-sound, non-tactile sensory anchor; advisory from prior audit; unaffected by fixer round 10
      why: Carried forward; advisory only

    - id: carry-flag-003
      type: flag
      what: Scene C (beats 62-80) — no 3-rated tensometer beat; dramatist must mark as scene-as-respite or identify the peak beat; advisory from prior audit; unaffected by fixer round 10
      why: Carried forward; advisory only

    - id: carry-flag-004
      type: flag
      what: Scene G (beats 220-232) — same tensometer gap; dramatist must flag as scene-as-transit; advisory from prior audit; ID 927 does not resolve the tensometer concern
      why: Carried forward; advisory only

    - id: carry-flag-005
      type: flag
      what: Mira-POV (beats 565-643) and oc-craftsman-mother POV (beats 701-787) — no NI rubric instances authored for these POV characters; process gap; advisory from prior audit; unaffected by fixer round 10
      why: Carried forward; advisory only; NI rubric authoring required before facet authoring for these segments

    - id: carry-flag-006
      type: flag
      what: Swarm-rupture aftermath (beats 480-519) — thin quiet-beat zone for memory-flag monument anchor; advisory from prior audit; unaffected by fixer round 10
      why: Carried forward; advisory only

    - id: carry-flag-007
      type: flag
      what: Scene E density (beats 127-149) — 23 consecutive content beats; advisory from prior audit; fixer round 10 did not insert an additional break at the candle-transition (143-145); still borderline but functional
      why: Carried forward; advisory only

    - id: carry-flag-008
      type: flag
      what: Numbering gaps (389, 219, 901-903) — confirmed intentional deletions; advisory from prior audit; ID 927 reuses gap 219 as an insert position, which is consistent with the intent noted in prior flag-009
      why: Carried forward; gap 219 is now occupied by the Scene G frame-anchor insert (ID 927); no new numbering fault introduced
