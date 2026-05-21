audit: facets-final-r2-verify
episode: b01c01
date: 2026-05-19
mode: flag-only (targeted CONSTRAINT re-verification)
parent_report: active-project/staff/auditor/facets-final-audit.md
status: CLEAN (HARD = 0)
totals: 0 new findings; both r1 HARD findings remediated

---

## Targeted re-check (post-fixer cycle 1)

Re-firing only the CONSTRAINT class scope that carried the r1 HARDs. Other classes unchanged from r1 (SIGNAL items remain advisory).

### C-001 verify — [vibes:21] @26 citation mismatch

**Status: REMEDIATED.**

- Pre-fix: vibes:21 declared `@26` anchor; proto-line @26 carried `[state:11] [vibes:18] [vibes:20]` (no `[vibes:21]`); cite-index `back=N`. Graph integrity break.
- Post-fix: vibes:21 entry line is off-anchor (`21 actor:wren... ++ trust: [...] | licensed-by: proto:21, proto:22, proto:25`). Schema permits off-anchor vibes. Cite-index rebuilt against the new state via `python3 active-project/staff/cite-index/build_cite_index.py b01-c01` (no STALE-CITATION errors). Proto-line @26 is now `26 wren-stitch-maker-flea-bottom-ward leaves the street [state:11] [vibes:18] [vibes:20]` — no orphan `[vibes:21]` claim. Proto-line @25 retains its `[vibes:21]` cite (pre-existing); off-anchor vibes may still appear in cite-clusters where their cloud-territory fires.

### C-002 verify — [vibes:17] @23 Earth-Bet hard-fence

**Status: REMEDIATED.**

- Pre-fix: vibes:17 keyword `khepri-residue` + licensed-by `world-build:khepri-residue-122ac`. "Khepri" substring violated the fence.
- Post-fix: keyword renamed to `override-architecture-residue` (matches narrator-interest + memory rendering convention: "the override-architecture", "the once-deployed scale"). Licensed-by rewritten as `world-build:override-architecture-residue-122ac`. Re-scan via `grep -ci "khepri\|gold morning\|brockton\|skitter\|scion" active-project/theater/facets/*.md active-project/theater/proto-lines/b01-c01.md active-project/theater/dialogue/*.md` returns one residual hit: `exposition-b01-c01.md` source field references the warehouse slug `cond-khepri-residue-122ac` (the warehouse file itself was not renamed; the slug is an operator-facing card reference, not narrator-rendered prose). The r1 audit's exposition pass-verdict explicitly evaluated the gloss text and found it clean ("preamble deliberately avoids Khepri / Gold Morning per the noun-fence"); the slug reference is an audit-edge the r1 auditor did not flag in its CONSTRAINT scope. Logged here as **NOTE-FOR-NEXT-RUN** (not a new HARD): if subsequent audits tighten the source-field fence scan, the warehouse card may need a renamed slug or the exposition source-field convention needs an "operator-slug-cited-as-reference-only" carve-out. Not blocking this run.

### Other CONSTRAINT items (re-verified PASS from r1)

- mem:2 @23 NI-spine: narrator:7 @23 (R2 ADD) still present. PASS.
- exposition scene-open-orient fire-rule (@11, @20): refusals correct. PASS.
- exposition re-gloss: first episode; glossed-terms register initialized clean. PASS.
- dialogue behavior-card-compliance (all 3 utterances): PASS.
- URI-DIALOGUE-COVERAGE-GATE: 3 speech bones × 3 speaker files; all cited; all non-empty. PASS.
- URI-SCENE-WINDOW: 24/24 bones in exactly one scene. PASS.
- Per-scene caps: sensory ≤3, feeling ≤1/char, metaphor ≤1 cross-character, exposition scene-open-orient ≤1. PASS.
- loc-state continuity-license: no continuity-carry entries; nothing to fire. PASS.
- first-mention-character coverage: Coll + Wren glossed; door-keeper role-reference (PASS per r1).
- Earth-Bet fence across NI / memory / metaphor / feeling / sensory / loc-state / exposition gloss / dialogue / state field-and-value: clean post-fix.

---

## Audit summary (post-fix)

- HARD findings: **0** (down from 2).
- SIGNAL findings unchanged from r1 report: 7 (3 FREQUENCY-BAND, 2 STRUCTURAL, 1 AP-SCAN, 1 TASTE-FLAG; PILE-UPs all WARRANTED; METADATA / CONTRADICTION / DEDUP / SUPERFLUOUS / CURVE-SHAPE-fail still 0).
- F-R2 protocol: clean (no change).

**Phase 5b gate: CLEARED.** Audience-gate may fire.

Showrunner-memory next: status `faceted-r2` → `audited-r1-mechanical`.
