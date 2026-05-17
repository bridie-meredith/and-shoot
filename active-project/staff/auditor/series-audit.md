```yaml
audit:
  scope: series
  target: witch-of-flea-bottom
  timestamp: 2026-05-17
  findings:

    # --- PASS findings (no action) ---

    - id: fault-001
      type: pass
      what: brief fidelity — protagonist
      why: Taylor Hebert, post Gold Morning, confirmed in memory.md plot.start and cast_roster (taylor-hebert-flea-bottom-mirror, role: protagonist). Card confirms post-Gold-Morning state, Shard-mediated deposit, weeks in KL.

    - id: fault-002
      type: pass
      what: brief fidelity — start-location
      why: King's Landing confirmed in memory.md lore ("Start-location: King's Landing") and in series-plan.md throughout.

    - id: fault-003
      type: pass
      what: brief fidelity — time-period (before Dance of Dragons)
      why: memory.md lore confirms "pre-Dance, Viserys I declining court, factions forming." series-plan.md Silverwing footnote anchors to 100–129 AC window. Lore-consistent.

    - id: fault-004
      type: pass
      what: brief fidelity — theme ("road to hell paved with good intentions")
      why: memory.md theme field states this verbatim and extends the mechanism correctly. series-drama.md carries it as the central architecture. Fully traceable.

    - id: fault-005
      type: pass
      what: brief fidelity — "taylor does bad things for a good reason which later turns out to be bad"
      why: The kill-Vaegon / wrong-rider mechanism directly satisfies the brief's causal requirement. Each bad act is locally defensible (memory.md behaviors — moral framing constraint). The "later turns out to be bad" mechanism is unambiguous: Ulf claims Silverwing, Lyra dies, Dance begins.

    - id: fault-006
      type: pass
      what: brief fidelity — one book long series
      why: memory.md plot.protagonist_arc is a single closed arc. series-drama.md explicitly states "Single closed arc. The Dance begins in the closing pages but is not followed in." Three-season structure mapped to single novel scope. Consistent.

    - id: fault-007
      type: pass
      what: schema compliance — memory.md required fields
      why: All required fields from showrunner-memory.schema.md are present: routing (4 subfields), series (theme, laws, lore, behaviors, plot with all 4 subfields, cast_roster, stage_elements), seasons (3 entries each with slug/chunk/status), active (season/episode). No required field is absent.

    - id: fault-008
      type: pass
      what: schema compliance — routing field format
      why: routing.season_plan is set to ~ (null) which is correct pre-season-planning. routing.show_file and routing.episode_plan are present. Consistent with schema note that season_plan points to season-<slug>-plan.md once created.

    - id: fault-009
      type: pass
      what: carry-forward #1 — flicker discipline
      why: memory.md behaviors entry 1 ("flicker discipline (binding): involuntary, unreliable, costs interpretively; near-dragon louder NOT clearer; no reliable deployment; no distinguishing correct flicker from misfire") is present and accurate against world-notes Behavior entry and carry-forward demand #1.

    - id: fault-010
      type: pass
      what: carry-forward #2 — Silverwing canon-assignment
      why: memory.md lore entry 3 names the 100–129 AC unclaimed window, Alysanne's death, Ulf's claim date. series-plan.md Silverwing footnote provides full canon basis. Carry-forward #2 satisfied at series level.

    - id: fault-011
      type: pass
      what: carry-forward #3 — cost-legibility
      why: memory.md plot.end states the causal chain unambiguously: Taylor kills Vaegon → Silverwing falls to Ulf → Lyra dies → Dance beginning. series-plan.md s03 chunk names the same chain. No ambient-chaos evasion.

    - id: fault-012
      type: pass
      what: carry-forward #4 — irony-closure demand (snob, binding)
      why: memory.md plot.end names chronicler coda naming counterfactual explicitly. memory.md behaviors entry 2 ("two-register architecture (binding)") captures the register-break mechanism. series-plan.md s03 stages recognition before coda. The chronicler-before-cost-bearer ordering is preserved in series-plan.md s03 chunk ("The chronicler coda names Vaegon's counterfactual; the cousin dies cold in the closing image"). Carry-forward #4 ordering requirement is satisfied.

    - id: fault-013
      type: pass
      what: carry-forward #6 — dragon-bonding canon-fence
      why: memory.md laws entry 3 ("Targaryen blood prerequisite for dragon-bonding; claiming-window mechanics post-bonder-death; no invented bonding rules (cond-dragon-bonding-claiming-rules)") is present, citing the condition card. Vaegon card stats confirm thin Targaryen blood sufficient for attempt. Ulf card confirms Targaryen blood. No invented rules introduced.

    - id: fault-014
      type: pass
      what: carry-forward #7 — patron amplification-theory as wrong-and-invisible
      why: memory.md behaviors entry 2 ("patron amplification-theory (binding): Rhaenys believes dragon-proximity amplifies Taylor's flicker; the theory is WRONG and invisible-while-operating; no scene where the patron acknowledges the wrong-theory during alignment phase") is present verbatim. Rhaenys card Hard Fence #2 confirms the honest-intellectual-error framing. No contradiction found.

    - id: fault-015
      type: pass
      what: carry-forward #8 — two-register architecture
      why: memory.md behaviors entry 3 captures the two-register architecture binding. series-drama.md Closure mechanism section describes the register-break. Taylor card Hard Fence #5 requires close-third exclusive. Edwyn card requires coda-only appearance. Consistent across all documents.

    - id: fault-016
      type: pass
      what: carry-forward #9 — Vaegon doppelganger weight
      why: Vaegon card contains the full "Doppelganger Mirror" section with on-page visibility requirement: at minimum one scene at Silverwing's distance, one scene with Lyra protection, one scene with prevention-reasoning visible. The structural overlap is explicitly specified. memory.md season chunks for s02 confirm perception of Vaegon's action-pattern before the lock completes.

    - id: fault-017
      type: pass
      what: carry-forward #10 — Edwyn deduction-path
      why: Edwyn card "Fiction Role Overlay — Deduction-path required in coda" specifies a 6-step chain from documented household records to counterfactual inference, labeled as deduction not speculation. The binding constraint is preserved.

    - id: fault-018
      type: pass
      what: architectural coherence — three-season structure
      why: s01 = wrong-theory installed and conditions for correction destroyed (alignment phase). s02 = doppelganger-lock complete (accumulation phase; no escape route past this point). s03 = detonation + recognition + coda (cost-confirmation). The accumulation structure maps cleanly to road-to-hell accumulation: each season closes with what cannot be undone.

    - id: fault-019
      type: pass
      what: architectural coherence — recognition staging in s03
      why: The recognition (Taylor sees wrong rider above smoke, understands her own kill produced the configuration) is explicitly staged BETWEEN the kill and the chronicler coda in series-plan.md s03 chunk. The dramatist's attempt-1 gap is addressed. The protagonist-as-antagonist beat is the climax; the chronicler coda follows it.

    - id: fault-020
      type: pass
      what: cast-roster coherence — all series-plan roles covered
      why: All roles from world-notes archetype roster are filled: protagonist (taylor-hebert-flea-bottom-mirror), false-ally (rhaenys-targaryen), opposite-number (oc-vaegon-targaryen), cost-bearer (oc-lyra-targaryen-ward), wrong-rider (ulf-the-white), witness/chronicler (oc-maester-edwyn), true-ally/Flea-Bottom inner circle (oc-renderer-flea-bottom, oc-flea-bottom-boy, oc-apothecary-assistant). memory.md cast_roster lists all nine.

    - id: fault-021
      type: pass
      what: cast-roster coherence — access chain for Taylor-to-cousin
      why: world-notes Batch D carry-forward requires patron as bridge between Taylor and Vaegon/Lyra. Rhaenys card Relationships confirms she brings Taylor into household-adjacent contact with Vaegon and Lyra. Lyra card confirms Taylor encounters her "through the patron." The access chain is intact.

    - id: fault-022
      type: pass
      what: binding-fact coverage — no parahuman infrastructure
      why: memory.md laws entry 2 names this law explicitly with downstream consequence ("Taylor's errors cannot be corrected by a system that understands her"). Taylor card Hard Fence #7 ("She has no one who understands what she is") confirms at card level.

    - id: fault-023
      type: pass
      what: binding-fact coverage — ASOIAF world physics
      why: memory.md laws entry 1 present ("ASOIAF Westeros physics — magic scarce, dragons real, no parahuman ecosystem"). No contradiction in plan documents.

    - id: fault-024
      type: pass
      what: binding-fact coverage — protagonist-arc shape
      why: memory.md plot.protagonist_arc states the competence-as-catastrophe mechanism. Consistent with series-drama.md and prompt-binding.md boundaries.

    - id: fault-025
      type: pass
      what: binding-fact coverage — closing image order (HARD requirement from world-notes)
      why: world-notes Batch D states "Closing-image ordering chronicler-before-cost-bearer is HARD requirement." series-plan.md s03 chunk confirms order: "The chronicler coda names Vaegon's counterfactual; the cousin dies cold in the closing image with the wrong dragon above." Order preserved.

    - id: fault-026
      type: pass
      what: carry-forward #5 — propositional-statement risk (advisory)
      why: series-plan.md bridging notes close on event-sequence language ("the cousin's death is the cost the reader exits on"). No near-thesis propositional statement found in bridging notes or coda specification. The series question appears only in memory.md plot.series_question (appropriate location). Risk is held.

    # --- FLAG findings ---

    - id: fault-027
      type: flag
      what: memory.md cast_roster format — entries use extended object form, not one-line slug form
      why: The schema shows cast_roster as "- <actor-slug>: <one-line role description>" (flat). memory.md uses a multi-field object form with slug, role, and type subfields. This is an enriched format, not a schema violation (the schema says "one line per item unless a pointer is needed"), but it diverges from the example format shown in the schema. No downstream agent depends on a specific parse of cast_roster at this stage — season planning does not yet consume this. Flag for awareness; not blocking.
      criteria: ~

    - id: fault-028
      type: flag
      what: memory.md stage_elements format — entries use descriptive strings, not slug-colon-purpose format
      why: The schema shows stage_elements as "- <location | prop | condition slug>: <one-line purpose in series>" (slug-first). memory.md entries combine slug and purpose in a single string (e.g., "loc-flea-bottom (+ loc-flea-bottom-mirror overlay) — Taylor's operational base"). The schema intent is preserved in content but the format is non-standard. No blocking downstream consequence at series level. Flag.
      criteria: ~

    - id: fault-029
      type: flag
      what: seasons[].title fields are all set to ~ (null) in memory.md
      why: The schema does not require title fields, but absent titles mean season-plan files will need to assign them at season-planning time. This is expected behavior pre-season-planning. Noting that all three seasons lack titles in case downstream processes expect them.
      criteria: ~

    - id: fault-030
      type: flag
      what: memory.md seasons[].episodes[] absent for all three seasons
      why: Schema note says episodes are populated by /and-season Phase 5 after split, so absence is expected at series-plan stage. Confirming expected state; not a fault.
      criteria: ~

    # --- FAULT findings ---

    - id: fault-031
      type: fault
      what: constraint-card alignment — warehouse condition cards for mirror-tragedy project not physically present at any tested path
      why: memory.md laws entry 3 cites "(cond-dragon-bonding-claiming-rules)" as the backing constraint. memory.md behaviors entries cite the behavior constraints by name but do not name backing cards. The conditions INDEX (cards/conditions/INDEX.md) lists the following mirror-tragedy warehouse-only cards that should exist in active-project/warehouse/: cond-dance-faction-state-previserys, cond-dragon-bonding-claiming-rules, cond-flea-bottom-social-physics, cond-flicker-discipline-mirror, cond-kl-feudal-physics-mirror, cond-kl-witch-label-formation, cond-patron-amplification-theory-mirror, cond-series-tone-mirror, cond-shard-deposit-mechanics-mirror, cond-smallfolk-court-access-mirror. None of these files resolve at active-project/warehouse/ (flat or in a conditions/ subdirectory). Without these cards in the active warehouse, downstream agent dispatch (coach, impersonator, studio) cannot read the binding behavior constraints they encode. The cards exist as INDEX entries but not as physical files.
      criteria: All ten mirror-tragedy warehouse-only condition cards must resolve as readable files in active-project/warehouse/ (or its conditions/ subdirectory) before /and-season s01 proceeds. The card content must match the behavior constraints recorded in world-notes.md and memory.md.

    - id: fault-032
      type: fault
      what: constraint-card alignment — location cards for mirror-tragedy not confirmed in active-project/warehouse/
      why: memory.md stage_elements lists five locations: loc-flea-bottom, loc-velaryon-kl-townhouse, loc-dragonpit-exterior, loc-dragonpit-interior, loc-sept-of-baelor-margin, loc-kl-burning-street. The locations INDEX confirms all six exist in the library (cards/locations/INDEX.md, quality: full). However, the active-project/warehouse/ directory does not resolve any location files at tested paths. For downstream shoot, impersonators and studio need the location cards physically present in the active warehouse. If the warehouse directory for this project is empty or unpopulated, this blocks episode-level execution. Note: persona cards ARE present in active-project/actors/ (confirmed by reading all nine cast cards), so the actors promotion completed. The warehouse promotion for condition and location cards may be the missing step.
      criteria: All six series-critical location cards (loc-flea-bottom, loc-velaryon-kl-townhouse, loc-dragonpit-exterior, loc-dragonpit-interior, loc-sept-of-baelor-margin, loc-kl-burning-street) must be present in active-project/warehouse/ before /and-season s01 proceeds. A physical file at the correct path, not INDEX-only presence, is required.

    # --- SIGNAL findings ---

    - id: fault-033
      type: flag
      what: SIGNAL — one-book scope vs. three-season structure tension
      why: The brief specifies "one book long series." The plan implements this as three seasons. Series-drama.md explicitly states "Single closed arc. The Dance begins in the closing pages but is not followed in." The season structure maps s01/s02/s03 to act-1/act-2/act-3 of a single novel arc, not three book-length volumes. This is architecturally sound. Noting it because downstream agents (screen-writer at season planning, orchestrator-critic at Phase 6) should hold the one-book framing — each season is an act, not a book. No fault; SIGNAL for season-planning orientation.
      criteria: ~

    - id: fault-034
      type: flag
      what: SIGNAL — true-ally archetype role unresolved in cast
      why: world-notes archetype roster includes "True-ally: single low-status loyalist whose loyalty is the cost-bearer." prompt-binding.md lists it as a taste-judge pick. The memory.md cast_roster does not contain a slot labeled "true-ally." The three Flea Bottom inner-circle OCs (renderer, boy, apothecary-assistant) are atmospheric, transactional, or cover-maintenance; none is labeled as the single low-status loyalist. The cost-bearer role is filled by Lyra, but the "whose loyalty is the cost-bearer" phrasing suggests a true-ally who pays a cost, which may or may not map to Lyra. If the true-ally role is intended to be Lyra herself (the child Taylor extends reflexive protection to), the cast is complete. If it requires a separate low-status adult loyalist, the cast has a gap. This is an interpretive question for season-planning to resolve, not a series-plan fault. SIGNAL.
      criteria: ~

    - id: fault-035
      type: flag
      what: SIGNAL — snob advisory carry-forward active into episode execution
      why: series-plan-log.md carry-forward #5 (propositional-statement risk, advisory) is active and will require enforcement at every coda draft in s03. The series-level documents pass the check, but the advisory flag is live and must be re-verified at episode-plan audit and wrap audit for any s03 episode containing coda material.
      criteria: ~
```

---

## Orchestrator verification — appended 2026-05-17 post-audit

**fault-031 and fault-032 dismissed as false positives.**

Direct `ls active-project/warehouse/` confirms physical presence of all 10 mirror condition cards (`cond-dance-faction-state-previserys`, `cond-dragon-bonding-claiming-rules`, `cond-flea-bottom-social-physics`, `cond-flicker-discipline-mirror`, `cond-kl-feudal-physics-mirror`, `cond-kl-witch-label-formation`, `cond-patron-amplification-theory-mirror`, `cond-series-tone-mirror`, `cond-shard-deposit-mechanics-mirror`, `cond-smallfolk-court-access-mirror`) AND all 6 location cards (`loc-dragonpit-exterior`, `loc-dragonpit-interior`, `loc-flea-bottom-mirror`, `loc-kl-burning-street`, `loc-sept-of-baelor-margin`, `loc-velaryon-kl-townhouse`). No fixer dispatch required.

Three SIGNAL items remain noted, not blocking:
- one-book-as-three-acts framing for /and-season scope-holding
- true-ally archetype slot to clarify at season-planning (likely realized through Vaegon's protection-relationship with Lyra; not a separate cast role)
- snob propositional-statement advisory live for s03 coda drafting

**Series-level audit verdict (final): PASS-WITH-NOTES, no blocking faults.**
