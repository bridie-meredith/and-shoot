---
reviewer: cape-fic-reader
facet: state-updates
episode: b01c01
cycle: r1
date: 2026-05-19
verdict: revise
---

# Cape-Fic Reader — state-updates adversarial verdict

## Stance

Who-knows-what-when coherence is my ground. State-updates is a promise ledger — what fields are set, at what beat, by which author, with what canonical authority. I'm reading this as a tracking sheet and I want it to be clean. It is not clean.

---

## Callouts

### [state-updates:7] @2 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.social-tether.coll-block-presence: none -> paying-resident-at-corner-room`

The rubric is explicit: every `actor:<POV>.*` entry requires a narrator-interest co-citation on the same beat. The cite-index shows narrator fires at @1 and @8. Nothing at @2. This entry ships a field mutation on Taylor's actor-state with no narrator-interest spine. Per the rubric's cross-facet test: "If the entry is `actor:<POV-character>.*` [...] narrator-interest co-citation on the same beat is REQUIRED. Absence = REJECT or flag back to narrator-interest author." That's not a soft advisory. This is a rule.

Convergence-trace: overlaps with auditor S-002 (multi-frontmatter structural issue) insofar as consolidation may have obscured the cross-facet check; but the co-citation gap is a substance failure the auditor's CONSTRAINT pass did not enumerate per-entry. Auditor r2-verify confirms mem:2 @23 is satisfied but does not enumerate @2 or @3 or @5 as verified.

### [state-updates:8] @3 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.knowledge.coll-as-vouching-vector: unmapped -> registered-as-block-fixture-with-verbal-contact`

Narrator does not fire at @3. The cite-index shows @3 carries: coll-net-mender-flea-bottom:1, exposition:2, state:1, state:2, vibes:5 — no narrator entry. Taylor's knowledge state is being written back as canonical without the POV-interest spine. This is the same rule failure as entry 7.

Additionally: `registered-as-block-fixture-with-verbal-contact` is reading like a perception label, not a clean state value. The rubric flags registration-as-state (anti-pattern #1). The field name is `knowledge.coll-as-vouching-vector` and the new value is `registered-as-block-fixture-with-verbal-contact` — I'd argue the field is defensible (knowledge is tracked-state), but the new-value phrasing smuggles registration language into the state record.

Convergence-trace: the rubric's §Reality REJECT signatures name "Registration-as-state" first. Auditor's AP-SCAN did not enumerate this per-entry in state-updates scope.

### [state-updates:9] @5 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.work-role.coll-block: outside -> needle-handler-at-coll-block`

Narrator does not fire at @5. The cite-index shows @5 carries: state:3 (back=N) and state:9 (back=N) — no narrator entry. Same rule failure pattern. @5 is "taylor-hebert-kl-122ac takes the needle" — this IS a real state change (she now has the needle; her work-role shifts). The reality axis holds. But the cross-facet contract is broken: no narrator co-citation.

### [state-updates:13] @18 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.work-role.coll-block: needle-handler-at-coll-block -> recurring-needle-handler-coll-block`

Narrator does not fire at @18. Cite-index at @18: state:5 (back=Y), state:7 (back=N), state:13 (back=N). No narrator. This is a POV actor-state write-back with no narrator spine.

The field value shift is also borderline — `needle-handler` to `recurring-needle-handler` reads as intensity-of-pattern, not a clean binary field flip. The persistence test: does "recurring" persist? Or does it describe the end of a session (nets set down = work session complete per entry 5)? If the work session just ended, the transition to "recurring" at the moment of set-down is pre-empting — the pattern is asserted before it's observable at next-episode scale.

Convergence-trace: auditor TF-001 flags stitch-input guidance gap for @16-@17 bare bones but does not flag this entry's pre-emption risk.

### [state-updates:14] @22 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.knowledge.wren-presence: unregistered -> face-with-voice-registered`

Narrator does not fire at @22. Cite-index at @22: state:8, vibes:14, vibes:15, wren-stitch-maker-flea-bottom-ward:1 — no narrator. The new-value `face-with-voice-registered` is knowledge-state not mood, so the field is defensible (knowledge is tracked). But no narrator co-citation on a POV actor-state entry.

Additionally this value reads as a perception landing (`registered`). The question is whether "Taylor now has a face-with-voice record of Wren" is actually a persistent field change or registration-as-state. I'd read it as borderline: if this knowledge value persists to next chapter and conditions Taylor's behavior, it's real state. If it's just logging that Taylor noticed Wren, it's registration-as-state contamination.

### [state-updates:16] @25 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.relational-anchor-status.wren: stranger -> face-not-node`

Narrator does not fire at @25. Cite-index at @25: state:10, taylor-hebert-kl-122ac:1, vibes:21 — no narrator. This is a Taylor actor-state write-back without the POV-interest spine.

The field `relational-anchor-status.wren` and value `face-not-node` is doing real work (it tracks Taylor's social-graph categorization of Wren, which has downstream consequences for the prohibition chapters). The field is defensible on reality and authority grounds. But the cross-facet contract is broken: no narrator at @25.

Convergence-trace: no auditor finding maps here — the auditor's per-entry POV co-citation check appears to have been satisfied at @23 (mem:2/NI spine) but not enumerated for @25 specifically.

### [state-updates:17] @26 — missing narrator co-citation on POV actor-state
`actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper`

Narrator does not fire at @26. Cite-index at @26: state:11, vibes:18, vibes:20 — no narrator. Same rule failure. Taylor's knowledge is being written back canonical without the POV interest chain.

Also, `ward-layer-deeper` as a field value is loose — it's directional ("deeper") rather than a clean state label. Compare to the rubric's examples: `provisional-labor-eligible`, `name-on-line-with-parallel-margin-marks`. This reads like a gradient note, not a field value.

### [state-updates:6] @3 — registration-as-state risk on Coll field-extension
`actor:coll-net-mender-flea-bottom.block_baseline_new_faces: none-this-week -> one-new-face-fish-gate-lane`

The rubric says state-updates is not perception, not registration. The field-extension comment reads: "tracks Coll's accumulating non-interpretive register of new presences on the block." That sentence contains the word "register." This field is Coll's awareness-count of new faces — which is a perception/registration, not a structural delta on a canonical field. The rubric explicitly names "Registration-as-state" as anti-pattern #1.

The field-extension defense would need to show this is tracked-state-aspect (knowledge, mask-state, exposure-state, posture, inventory) — not perception. I'm not persuaded. Coll noticing Taylor is a registration event; the appropriate home is narrator-interest (if it were Coll's POV) or a third-party observation field. Shipping this to canonical write-back means the showrunner will set a `block_baseline_new_faces` counter on Coll's card — which feels like a perception log being laundered into state.

Convergence-trace: auditor found no finding on entry 6. This is a seam the mechanical scan missed.

### [state-updates:19] @22 — registration-as-state on Wren stats field
`actor:wren-stitch-maker-flea-bottom-ward.stats.taylor_awareness: unencountered -> noticed-as-presence-on-block`

`noticed-as-presence-on-block` is a perception event dressed as a state field. Wren noticing Taylor at @22 is a registration — it's Wren's awareness-event, not a structural delta on a canonical field in the tracked-state sense. The rubric's §Reality REJECT signatures: "Registration-as-state. The proto-line is a *perception* beat — the POV character notices something — but no field on any target changes."

The field-extension defense is that `stats.taylor_awareness` is an ongoing tracking field on Wren's card. The rubric's test: "if the field on the target would still be in the `<new>` state at the next beat without this entry having fired, the entry is parasitic." The answer here is: does Wren's `taylor_awareness` change from `unencountered` to `noticed` regardless of whether this entry fires? Yes — the scene happened. The field is recording perception-state, not causing structural change. This is registration laundered as state.

Convergence-trace: no auditor finding on entry 19. Seam missed by mechanical scan.

---

## Summary

7 POV actor-state entries (7, 8, 9, 13, 14, 16, 17) lack narrator-interest co-citation at their anchor beats, in direct violation of the rubric's cross-facet requirement. 2 entries (6, 19) ship as registration-as-state (anti-pattern #1). Entry 13 has a pre-emption risk and entry 17 has a loose field-value label.

The auditor confirmed the overall curve shape is OK and the two HARD findings were remediated. But the per-entry POV co-citation check was not enumerated for the majority of Taylor actor-state entries — that's the seam the mechanical scan missed, and it's the seam this audience attacks.

verdict: revise
