cascade:
  root: b01c11
  invoked_at: 2026-06-02T21:35:00Z
  invoked_command: "produce-chapter-protocol b01c11 (fresh run; resume of c10-c20 cascade intent)"
  mode: unattended
  current_run:
    command: produce-chapter-protocol b01c11
    started_at: 2026-06-02T21:35:00Z
    pre_flight: |
      GREEN. series-audit APPROVED 2026-05-24 (stale null). aggregate-state PRESENT through c10,
      0 unack substantive (rev-0001..0004 all acknowledged:true; the two SUBSTANTIVE c10 forward-thread
      findings route to parking-lot, not revision_layer). voice-exemplar PRESENT. Two HARD parking-lot
      items in scope (pl-2026-06-02-stitch-thread-001 Halvard hook-0007 + -002 cl-d06 second tranche),
      BOTH targeting /and-substance chapter b01c11 Phase 3 — surfaced at Phase 0, resolve AT Phase 3.
    chain: "/and-substance chapter b01c11 --cascade -> write -> review bones -> facets -> stitch (P9 + P10)"
  run_intent: |
    Multi-chapter cascade. c09 COMPLETE. Now producing c10..c20 end-to-end per RUNBOOK
    chapter-production protocol (R1–R5). Book b01 chapter_count = 20. Drive as far as
    feasible; halt cleanly with a checkpoint on cap-exhaustion / hard-block / practical
    session limit.
  last_completed:
    level: chapter-complete   # b01c10 COMPLETE end-to-end: substance + write + bones-review + facets + stitch (P1-9 + P10). draft/b01-c10.md TERMINAL (1074 words).
    slug: b01c10
    completed_at: 2026-06-02T04:15:00Z
  next:
    command: produce-chapter-protocol b01c11
    args: [b01c11]
  reason: chapter-complete-practical-limit   # c10 shipped this session (resumed from bones-complete; ran facets+stitch = the larger half). c11 is a fresh chapter-production run — best with fresh budget given this session's spend (~50+ dispatches across the full facets+stitch pipeline). Two HARD parking-lot items gate c11 Phase 3 (see pending_threading_holds).
  failure: null
  pending_depth_passes: [b01c10]   # PASS-WITH-DEPTH-PASS-REQUIRED (spine-staging-gap acts-of-commission + readability AIRLESS). /and-write b01c10 revise --from-signals before book-close. NON-blocking for c11 production.
  pending_threading_holds: [b01c10]   # Phase 10 HOLD-THREAD: pl-2026-06-02-stitch-thread-001 (Halvard hook-0007) + -002 (cl-d06 tranche) -> resolve at /and-substance c11 Phase 3.
  pending_cohere: "DEC-0070 (admin Phase 9.5): apparatus-density c06-c10 now N=5; DEC-0067 threshold N=6. Schedule /and-cohere b01 before the book advances past c11 (if c11 also ships apparatus-register, N=6 reached). PROP-0030/0031 recurrence_count=3, triage urgency HIGH."
  c10_progress: |
    b01c10 ~60% through the chapter-production chain — ALL COMMITTED + PUSHED:
      [DONE] /and-substance chapter b01c10 — 4 scenes, climax/d10, roll-up exact, Phase-5 ACCEPT
             (3-of-3 SUBSTANCE-FELT), cold-read PASS-CHUNK-VOICE-RISK.
      [DONE] /and-write b01c10 — 27 bones / 4 scenes, silent chapter, bone-gate PASS (0 HARD after
             cycle-1 fix, 7 SIGNAL dispositioned), bones file + scene-map emitted, persisted to memory.
      [DONE] /and-review bones b01c10 — PASS-WITH-NOTES, follow_check PASS-WITH-NOTES (/and-facets cleared).
      [NEXT] /and-facets b01c10 — Phase 0 will read bones_review (fresh, present) + scene-map (present).
             Carry into Phase 2.5 context-weave (from bones_review.carry_to_facets_phase_2_5):
               HIGH: B->C surrender->detention causal seam (context-ledger candidate)
               MEDIUM: beat-(a) formalization opacity @2
               exposition: s01 Sera-as-stated-consideration
               grounding-ledger: scene C aliveness (BONES-AIRLESS-RISK)
             Apply per-persona SPLIT dispatch at Phase 5b (PROP-0036; trio-in-one dies — proven twice).
      [THEN] /and-stitch b01c10 (Phase 9 cold-read + Phase 10 forward-thread).
  resume: /and-facets b01c10  (then /and-stitch b01c10)
  pending_depth_passes: []   # b01 ZERO unresolved depth passes (c09 DEC-0068 resolved).
  pending_cohere: "consecutive-airless c06-c09 (DEC-0066/0067) — book-level /and-cohere concern; re-evaluate depth-pass-pending accumulation at N>=6 (DEC-0067). c10 chunk_cold_read PASS-CHUNK-VOICE-RISK (airlessness design-inherent for this climax) extends the watch — candidate cohere window after c10-c11."
  c10_substance: |
    /and-substance chapter b01c10 COMPLETE (2026-06-02). 4 scene chunks emitted + per-scene
    substance_delta + scene_conflict persisted to chapters[b01c10].scenes (memory.md). Climax
    chapter (d10 — first Dance-pressure pulse). dramatic_shape=climax, scene_count=4.
    Roll-up: all 7 axes_in_motion sum EXACT to chapter targets (position-prot-rise +1.0,
    social_tether-prot-rise +1.0, social_tether-antag +1.5, position-world +1.0,
    political_register-world +1.0, moral_framework -1.0, moral_legibility +0.5).

    Phase 5 gate (3 reviewers): dramatist ACCEPT (sound climax shape); auditor 0 HARD / 3
    advisory flags + 4 pass; audience 3-of-3 SUBSTANCE-FELT (split single-persona dispatch
    after two trio-dispatch deaths — socket-close + timeout; c09-precedent split remediation
    worked, ~85s each). Notes-fixes applied at persist: cl-world-d07 "completed"→first-tranche
    +1.0/+2.0 (aggregate confirms political_register-world at start_rank 5); s02 Corwick-Oswyn
    [mechanism:] tag added; s04 cl03a disambiguated (-1.0/-2.0, not closed); handoff_out ranks
    corrected vs aggregate-state (social_tether-antag 6→5, political_register-world 7→6;
    position-world rank 7 confirmed correct).

    Phase 5.5 chunk cold-read: PASS-CHUNK-VOICE-RISK (Signal A excused under-motivated
    Corwick-surrender + Signal B abstraction-lean). Arms /and-stitch Phase 8.5 Check 3
    (voice_risk_carry: verify s02 surrender + s03 detention land concretely, not as
    procedural-clause / data-transaction). Recorded in chapters[b01c10].chunk_cold_read.

  carry_to_write: |
    Bones-execution watches for /and-write b01c10 (pl-2026-06-02-001 — convergent across
    cold-read + all 3 personas):
      W1 (s02): ENACT the Corwick body-map surrender as an irreversible act with a physical
        correlate (months visible AS months before line-item); substrate-split/translation a
        distinct cognitive bone BEFORE the routing bone. Not a clean procedural clause.
      W2 (s04): the face is the chapter's TERMINAL weight, a physical feed-datum (posture-class/
        gait-signature persisting), NOT interior emotional realization. Two distinct bones
        (ledger-closes / record-remains); 3 "he did not consent" beats stay 3 bones; face LAST.
      W3 (s03): enact prior-circuit presence-count BEFORE absence reads as deviation.
      W4: aliveness — silent chapter (4 single-POV scenes, no dialogue); keep formalization +
        detention concrete + grounded; detention as perceptual feed-event not data-transaction.
    cape-fic also: s02 substrate-collapse must read irreversible not routine filing.
    SOFT ledger watch pl-2026-06-02-002: cl-antag-d10 journey-required cl04 deferred-draw plan
    to be stated when relational_anchor_status next moves (c11+).

  prior_chapters_note: |
    c09 COMPLETE: draft/b01-c09.md TERMINAL + DEPTH-RESOLVED; Phase 10 PASS-THREAD;
    aggregate-state through b01c09 + rev-0003. (Full c09 record in git history /
    memory.md chapters[b01c09].)
