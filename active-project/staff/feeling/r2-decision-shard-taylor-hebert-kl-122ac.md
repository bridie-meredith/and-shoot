---
facet: feeling
phase: r2-judge
persona: taylor-hebert-kl-122ac
episode: b01-c02
bones_count: 47
cite_index_hash: <sha-pending-build_cite_index-emit-for-47-bone-graph>
inputs_loaded:
  - active-project/theater/facets/feeling-taylor-hebert-kl-122ac.md (R1 slice; 2 entries)
  - active-project/theater/proto-lines/b01-c02.md (47-bone graph with facet-citation surface)
  - design/shoot-v2/rubric-feeling.md (V1 LOCKED 2026-05-07)
forbidden_loaded:
  - other R2 judges' outputs
  - named-feeling vocabulary
  - similes / comparisons / hedges / metaphors
mode: facet-judge
supersedes: prior-session-r2-shard-2026-05-25 (29-bone graph; bones re-emitted to 47-bone graph; that shard's @17/@24 anchors no longer correspond to the current bones; this shard re-runs against the live graph)
---

# R2 feeling judge — taylor-hebert-kl-122ac slice (b01-c02, 47-bone graph)

## Tally

- K: 1
- D: 1
- A: 0
- net entries before → after: 2 → 1
- density before → after: 0.043 → 0.021

## Per-entry decisions

### feel:1 @10 — DELETE

R1 text: "her attention pulls toward the dropped quadrant before her head turns | expressed: no"

Anchor: bone 10 "the alley-back drops from the feed [feel:1] [state:3] [vibes:1]" — peripheral-loss beat; no NI co-cite at this anchor.

Form-discipline failure on two counts:
1. **Abstraction-noun subject.** "her attention pulls" — "attention" is a cognitive/perceptual abstraction, not the body. The licensed clause subject must be a body part doing a body action. This entry occupies NI's slot (cognition/perception) under feeling's name.
2. **Compound second clause exiting body-register.** "before her head turns" is temporal-latency observation about head-orientation timing — the canonical URI-FACETS-CYCLE-1 REJECT signature (sentence-final non-body clause naming the rule/timing/latency, not the body-doing-the-action). The connector `before` joins a cognitive observation to a body micro-action and converts the entry from somatic-tell to author-voice gloss about how-the-body-lags-the-cognition.

Even on Q1, the proto-line already carries the loss-event ("drops from the feed"); the somatic body-cost of peripheral loss is left unwritten and would need a fresh single-clause body-register entry (e.g., hand finding the dropped quadrant, weight catching) — not a cognitive frame.

VERDICT: DELETE.

### feel:2 @23 — KEEP

R1 text: "her weight settles back onto the rear foot | expressed: partial"

Anchor: bone 23 "taylor-hebert-kl-122ac yields the alley-mouth [feel:2] [narrator:4]" — co-fired with NI.

Form clean: subject (her weight) + verb (settles back) + locator (onto the rear foot). One clause. No named-feeling vocab. No simile. No hedge. No metaphor. No compound second-clause exiting register. No rule-statement.

Persona-card match: Taylor's surveillance-under-threat weight-shift / retreat-readiness signature — body-prepared-to-cede before the cognition issues the yield.

Q1 passes: proto-line "yields the alley-mouth" carries the social/spatial act; the body's pre-decision rearward weight-shift is the cost-of-the-act NI does not carry at this anchor. NI:4 fires registration-of-yielding-as-decision (cognitive); feel:2 shows body-already-shifted (somatic). Distinct jobs. Non-redundant per cross-facet contract.

Q2 passes: scene-B's pivot — the moment Taylor cedes alley-mouth ground to the ward-junction body she has just begun to track. Structural to the chapter's surveillance-vs-civic-presence arc and the c03 patron-arrival setup.

Multi-justification 5/5:
1. Somatic-card-match (Taylor weight-shift signature).
2. Q1 passes (audience-cannot-otherwise-read body-precedes-decision).
3. Q2 passes (scene-B pivot).
4. Scene-eligible (per-scene cap unused in scene-B before this fire).
5. Functional-register: painting-characterization + realization (the body knows before the head does the calculation).

VERDICT: KEEP.

## Adds (cap 5, used 0)

Scanned anchors with memory or NI co-cite where somatic register would land:

- @12 draws the line [mem:1][narrator:3] — proto-line carries the act; NI:3 carries the registration; mem:1 carries the callback. Body-cost interior to NI's territory at this beat. Refuse.
- @27 files the ward-junction contact [mem:2][narrator:6] — subject is "the insects"; Taylor's body not the proto-line subject, but multi-justification thin (no Taylor-card body register clearly licensed at this beat; cognitive-recognition is NI:6's job + mem:2's job). Refuse.
- @40 stalls the count [narrator:8] — Q1 redundancy risk: "stalls" is already the somatic-cognitive surface at NI's register; restating in tighter body-frame is C1/C2 calibration violation.
- @41 holds the breath [narrator:9] — Q1 fails; proto-line IS the somatic act (C1/C2 pattern).
- @43 closes against the drain angle — Q2 weak; small body act among many in scene-C accounting; not structural pivot.
- @47 exhales — Q1 fails; proto-line IS the somatic act.

No add beats the silence default. Per rubric: "Sparse by design. Most beats fire nothing." "Default to silence when uncertain."

## NI non-redundancy verification (per anchor)

- @23 feel:2 ↔ NI:4 — VERIFIED non-redundant. NI=cognition-of-yielding-decision; feel=body-weight-already-shifted-rearward as pre-decision somatic.
- @10 feel:1 DELETED — anchor has no remaining feeling fire; no live POV-redundancy surface.

All KEPT entries verified POV-non-redundant per anchor.

## File-shape audit (post-pass)

| Metric | Value | Verdict |
|---|---|---|
| Per-character per-scene cap (≤1, hard) | A=0, B=1, C=0 | PASS |
| Per-scene total cap (≤3, soft) | max 1 | PASS |
| Per-episode sparsity (2-5% target) | 0.021 (1/47) | UNDER-BAND — honored silence default per rubric |
| Vocabulary distinctness (per-character, hard) | n=1, no saturation possible | PASS |
| Tens distribution (soft) | single fire; advisory | N/A |
| Functional-register ≥2 of 4 (hard) | feel:2 satisfies | PASS |

The 0.021 density sits just below the 2-5% target band. This is rubric-aligned: over-firing to hit a numeric target is anti-pattern; "Sparse by design. Most beats fire nothing." The deleted feel:1 was form-failed, not silence-failed; honoring its removal without manufactured replacement is the correct discipline.

## Caveats

- `cite_index_hash` placeholder pending build_cite_index.py emit confirmation against the 47-bone graph. Anchor-level non-redundancy verification used the [facet:id] citation surface embedded in `theater/proto-lines/b01-c02.md` (canonical source-of-truth for which facets fire at which anchor).
- Full R1 graph text for NI / memory / sensory / state / loc-state / vibes / exposition slices was not surfaced to this fork at dispatch; redundancy adjudication relied on bone-level citation co-presence + rubric contracts (NI=cognition; feeling=somatic). If full-text NI:4 ever reads as a weight-shift observation (which would be a NI form violation, not a feeling problem), escalate feel:2 to DELETE at Phase 5b.
- Prior-session shard at this path referenced a 29-bone graph with anchors @17/@24 that no longer correspond to the live 47-bone graph. This pass supersedes that shard.
