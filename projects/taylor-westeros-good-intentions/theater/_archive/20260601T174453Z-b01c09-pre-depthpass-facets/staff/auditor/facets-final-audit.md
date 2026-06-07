audit: facets-final-r1
episode: b01-c09
date: 2026-06-01
mode: flag-only
status: FINDINGS-PRESENT
totals: 0 HARD / 9 SIGNAL
scope: full twelve-class mechanical cross-cutting graph audit of all R1 facet files (DEC-0063 streamlined single-pass; R2 judging skipped by decision)
persisted-by: orchestrator (auditor fork returned the report in-message but did not write the file; transcribed faithfully from the fork return — silent-write miss logged)

---

## Finding register

### signal-fb-001 — FREQUENCY-BAND (SIGNAL)
sensory-b01-c09 density is 3/23 = 13.0%, above the standard chapter ceiling (~8-10%). grd-001 in the grounding-ledger licenses sensory:3 @11 as cap-exempt; entries are 1 thermal @8, 1 light @11, 1 tactile @23. The density flag survives as advisory because the ledger satisfies the exemption condition but the absolute count remains above band. Advisory surface; does not block stitch. Confirms ledger coverage is required to hold the exemption.

### signal-fb-002 — FREQUENCY-BAND (SIGNAL)
feeling-taylor-hebert-kl-122ac-b01-c09 fires in 2 of 3 scenes (s01 @5, s02 @12; s03 silent). Per-scene cap of 1 is clean. Raw density over 23 bones is ~8.7%, above the 2-5% nominal band for a restrained interior chapter. Advisory; per-scene caps are the load-bearing constraint; raw-count exceedance is a denominator effect on a short chapter; s03 silence is declared design-intentional. No fixer action.

### signal-fb-003 — FREQUENCY-BAND (SIGNAL)
exposition-b01-c09 fires 3 entries on 23 bones = 13.0%, above the 1-5% nominal band. All three are mandatory/near-mandatory: @0 prior-episode-bridge (always-gloss), @9 first-mention-place dragonpit-lower-gate (first-appearance conditional), @8 scene-open-orient (conditional a/b/c). Exceedance is denominator-driven by short chapter length; no surplus entries. No fixer action.

### signal-fb-004 — FREQUENCY-BAND (SIGNAL)
state-updates-env-b01-c09 fires 4 entries; state-updates-taylor fires 2. Combined state-updates density 6/23 = 26.1%, above the 8-18% nominal band. Structural cause: oc-jarvis-packet lifecycle accounts for 3 of 4 env entries; both axis moves are mandatory. Documented in env carve-out preamble. No surplus entries. No fixer action.

### signal-meta-001 — METADATA-INCONSISTENCY (SIGNAL)
Episode slug format inconsistent across facet frontmatter: `b01c09` (metaphor, feeling, memory) vs `b01-c09` (vibes, state-updates-env). Canonical bones header uses `b01c09`. Cosmetic; does not affect graph traversal (cite-index keyed on proto-line IDs); stitch Phase 0 reads bones header slug. Advisory tidiness item.

### signal-cs-001 — CURVE-SHAPE (SIGNAL)
memory-b01-c09 fires both entries on peak-bones (mem:1 @6, mem:2 @14); zero fires in flat-low (@1-@3) or resolving scene-C (@17-@23) — an inverted valley-only curve, all memory mass at the peaks. The memory rubric carve-out preamble documents that in a rising surveillance chapter with an NI-spine constraint, memory fires only where NI fires, and NI fires only on bones clearing the observer-attention threshold (the peaks). Displacement-clamp exceptions (Earth-Bet monument-movement; Westeros monument-faction-war-foreknowledge) each satisfy per-entry licensing independently. Carve-out structurally sound; flag surfaces for stitch Phase 1 awareness.

### signal-sup-001 — SUPERFLUOUS (SIGNAL; validate at stitch Phase 1)
exposition:3 @8 (scene-open-orient) fires at the same proto-line as loc-state:3 @8. Under clause-b of the scene-open-orient fire-rule, a loc-state fire at the scene-open bone makes scene-orient exposition presumptively wallpaper. Contested: (a) context-ledger records follow-001 as a closed carry from /and-review bones, pre-licensing the context-weave fill; (b) the exposition content (same-day second circuit / approach direction) is distinct from what loc-state:3 encodes (actor presence in the dragonpit-margin lane) — no literal duplication. Validate-at-stitch: if Phase 1 folds both into one beat without redundancy, signal clears; if doubling is visible, treat as fault.

### signal-con-001 — CONSTRAINT (SIGNAL; margit referral recommended)
memory target-reference slugs `monument-movement-routing-without-consent` (mem:1) and `monument-faction-war-foreknowledge` (mem:2) are mechanism-descriptive per URI-032 but neither resolves to a monument card in the library at audit time. Monument cards for displacement-clamp targets must exist or be queued as margit referrals before the book-close card-promotion sweep. Does not block stitch.

### signal-ap-001 — AP-SCAN (SIGNAL; promotion advisory)
vibes-b01-c09 scene-B covers the @14 political-register event with one actor-targeted entry (vibes:5 → actor:taylor); no location-targeted vibes entry for oc-dragonpit-margin / oc-lower-gate. Mitigating: both locations are DEC-0063 uncarded (c08 precedent); no card exists to anchor a location vibe. When margit creates the dragonpit-margin + lower-gate cards, a scene-B location vibe for the political inference should be authored then. Not fixer-actionable until cards exist.

---

## Per-class summary

| Class | HARD | SIGNAL |
|-------|------|--------|
| 1 STRUCTURAL | 0 | 0 |
| 2 FREQUENCY-BAND | 0 | 4 |
| 3 METADATA-INCONSISTENCY | 0 | 1 |
| 4 CURVE-SHAPE | 0 | 1 |
| 5 CONTRADICTION | 0 | 0 |
| 6 DEDUP | 0 | 0 |
| 7 SUPERFLUOUS | 0 | 1 |
| 8 CONSTRAINT | 0 | 1 |
| 9 AP-SCAN | 0 | 1 |
| 10 TASTE-FLAG | 0 | 0 |
| 11 PILE-UP REVIEW | 0 | 0 |
| 12 RUBRIC-FIDELITY | 0 | 0 |
| **TOTALS** | **0** | **9** |

## CURVE-SHAPE verdict
SHAPE-OK. dramatic_shape: rising; per-scene rhythm-shapes (rising-to-quiet-peak ×2, falling-to-thesis-image) are coherent with the chapter-level rising→thesis-image close. Memory peak-concentration noted (signal-cs-001) but carve-out sound.

## Audit summary
- Total entries reviewed: 33 facet entries across 9 facet files (metaphor 0 entries).
- HARD classes: STRUCTURAL 0, CONTRADICTION 0, DEDUP 0, SUPERFLUOUS 0, CONSTRAINT 0, RUBRIC-FIDELITY 0.
- SIGNAL classes: FREQUENCY-BAND 4, METADATA-INCONSISTENCY 1, CURVE-SHAPE 1, SUPERFLUOUS 1, CONSTRAINT 1, AP-SCAN 1.
- Earth-Bet hard-fence scan: CLEAN (no proper-noun hits across any facet text field).
- DEC-0062 design-inherent carve-outs honored (apparatus vocabulary + held-moral_legibility opacity not faulted).
- Exemptions applied: sensory:3 grounding-ledger-licensed (grd-001); context-ledger empty (no exposition context-exceptions).

## Routing
Flag-only; no executes. SIGNAL carries:
- signal-sup-001 → /and-stitch Phase 1 (validate exposition:3 @8 / loc-state:3 @8 fold for redundancy).
- signal-con-001, signal-ap-001 → margit referral queue (monument cards mem:1/mem:2; location vibes pending dragonpit-margin + lower-gate cards) — parking-lot pl-2026-06-01-001 carry-forward per DEC-0063 / c08 precedent.
- signal-meta-001 → cosmetic slug-format tidy (optional).

## Phase 5 gate
HARD = 0 → Phase 5b audience-gate CLEAR to fire.
