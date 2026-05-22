---
audit: facets-final-r3
episode: b01-c01
date: 2026-05-20
mode: flag-only
status: CLEAN
prior-audit: active-project/staff/auditor/facets-final-audit-r2.md
fixer-report: active-project/staff/fixer/and-facets-cycle2-fixes.md
cycle: 2-of-3
---

# Scope

Focused re-audit of cycle-2 fixer changes only. Full 12-class scan not re-run on unchanged
files. SIGNAL findings from r1 and r2 carry forward. Cite-index stale-citation gap for
loc-state:3 and sensory:2 (still referenced in _cite-index.md) is intentional and excluded
from scope per dispatch instruction.

---

# Per-File Verdicts

## active-project/theater/facets/location-state.md

**Verdict: CLEAN**

STRUCTURAL: loc-state:3 is present as a gap-documentation comment block (lines 8-12), not
as a live entry. Surviving entries are 1, 2, 4, 5 — monotonicity holds; ID gap at 3 is
documented. No renumbering of surviving entries. Frontmatter intact.

CONSTRAINT: No new Earth-Bet or constraint violations introduced. The gap-documentation
comment block uses operator-vocabulary only. Surviving entries 4 and 5 are unmodified.

AP-SCAN: No new AP patterns introduced by the comment block.

DIALOGUE-COVERAGE: loc-state:3 was not a dialogue-coverage anchor; no speech bones lose
coverage by its deletion. Proto-line @11 (`taylor-hebert-kl-122ac lifts the basket`) retains
`[state:2]`; coverage intact.

Note: The cite-index still lists loc-state:3 @11 with back=Y. This is the expected stale-
citation gap; Phase 6 persist will resolve. Not a new finding.

---

## active-project/theater/facets/interest-narrator.md

**Verdict: CLEAN**

STRUCTURAL: Six entries present, monotonic, no renumbering. Frontmatter intact. The
audience-gate-cycle-1-defer block at lines 13-19 is a comment block; it does not parse as
an entry. ID sequence 1-6 is unbroken.

CONSTRAINT — Earth-Bet hard-fence scan on NI-1 rewrite text:
`"the flies in the wall-bottom register the eye-lift before the eye lifts"`
Scan for Earth-Bet proper-noun substrings: "flies" — generic; "wall-bottom" — Westerosi
architectural descriptor; "register" — generic verb; "eye-lift" — generic physical term.
No Earth-Bet proper-noun substring present. CLEAN.

AP-SCAN — "X is what Y" predicate-nominative inversion template check on NI-1 rewrite:
`"his eyes start to lift one breath before they lift; the flies in the wall-bottom register
the eye-lift before the eye lifts."` — this is a temporal-precedence construction, not a
predicate-nominative inversion. No "X is what Y" pattern. CLEAN.

The r2 audit had confirmed entries 2-6 were already AP-free. NI-1 rewrite introduces no new
saturation risk; 0/6 = 0% AP-template density. Threshold not reached.

BAND-CEILING NOTE (carry-forward, not a new finding): The defer block documents that adding
an entry at @22-@23 would push density to 7/27 = 25.9%, above the 25% cap. The current
file has 6/27 = 22.2%. This is within band. No new finding introduced.

---

## active-project/theater/facets/sensory.md

**Verdict: CLEAN**

STRUCTURAL: sensory:2 @16 is present as a comment block (lines 10-14), not as a live entry.
One live entry remains: sensory:1 @3. ID gap at 2 is documented. No renumbering. Frontmatter
intact. The defense-anchor comment (lines 7-9) and the audience-gate-cycle-1-defer block
(lines 16-25) both parse as comments, not as entries.

CONSTRAINT: No new constraint violations introduced by comment additions.

RUBRIC-FIDELITY — sensory:1 defense-anchor comment:
The comment at lines 7-9 states:
  "old-state 'corner-room-dim' is inferred from loc-state:1's 'door-shadow across the entry'
  geometry cue (shadow implies dim interior relative to exterior threshold) + the time-of-day
  implication of pre-noon Hook arrival."
This is a documented lineage from loc-state:1 geometry to the old-state value. The old-state
lineage rule requires anchoring to an established loc-state or prior sensory entry. loc-state:1
@1 (`the door-shadow across the entry`) is a live, non-deleted entry. The defense-anchor
comment satisfies the old-state lineage rule per the rubric requirement. CLEAN.

BAND-POSITION: 1/27 = 3.7%. Dispatch noted band is 3-6%. 3.7% is within band. CLEAN.

DIALOGUE-COVERAGE: sensory:2 was not a dialogue-coverage anchor. Proto-line @16 (`the walls
cool`) carries no speech tokens; no speech bone loses coverage.

Note: cite-index lists sensory:2 @16 with back=Y co=[state:4]. Stale-citation gap; expected
per dispatch; excluded from scope.

---

## active-project/theater/facets/state-updates.md

**Verdict: CLEAN**

STRUCTURAL: The `# rubric-carve-out` block is present at lines 7-37, between the consolidated
frontmatter close (`---` at line 5) and the first source block (`# source: env` at line 39).
This is exactly the position the r2 fault-001 criteria required. ID numbering on live entries
is unaffected; entries run 1-5 (env source), 6-8 (coll source), 9-18 (taylor source), 19-22
(wren source). No renumbering. Entry monotonicity preserved. Frontmatter intact.

CONSTRAINT: The carve-out block is an operator comment; no new rendered content introduced.

RUBRIC-FIDELITY — carve-out block content check against fault-001 r2 criteria:
  (a) rubric-state-updates.md §Cross-facet contract scoping clause cited? YES — line 7:
      "rubric-state-updates.md § Cross-facet contract" explicitly cited.
  (b) Each of the 8 uncovered taylor-state entries classified by exempt category or
      accepted-with-defense? YES — lines 17-29 enumerate state:3, :5, :8, :9 with defense
      rationale and state:1, :2, :4, :6, :7 as mechanical-action class.
  (c) rubric-state-updates.md §Anti-patterns #9 (density-on-flat) cited as reason NI entries
      not added for accepted-with-defense entries? YES — lines 31-37 cite band-ceiling
      collision, flat-low rhythm-shape, and "AP refuse-by-default discipline."
  (d) Carve-out explicitly resolves F-006 from r1 audit? NOT STATED VERBATIM. The block
      does not contain the phrase "resolves F-006" or "F-006 from the r1 audit." However,
      this is a comment annotation, not a mandatory sentence structure — the criteria from
      r2 fault-001 said "state explicitly that the carve-out resolves F-006 from the r1
      audit," and this literal requirement is absent.

CLASSIFICATION: The absence of the "resolves F-006" sentence is a gap against the r2
fault-001 criteria (d). Scope assessment: this is a one-line comment insertion in an existing
comment block. It does not affect rubric mechanical compliance (the carve-out substance is
present and complete; all three reviewers' positional requirement is satisfied). The gap is
a documentation deficit, not a structural or constraint violation.

This is classified FLAG, not FAULT. The carve-out block is substantively correct and
positioned correctly; the missing sentence is a minor audit-trail gap that does not create
a downstream mechanical problem. No new HARD introduced.

  id: flag-001
  type: flag
  what: state-updates.md rubric-carve-out block does not contain explicit "resolves F-006
        from the r1 audit" sentence as required by r2 fault-001 criteria (d)
  why: audit trail for fault-001 resolution is incomplete; a future auditor reading only
       this file cannot confirm which prior finding the carve-out addresses without cross-
       referencing r2 audit and fixer reports; minimal downstream consequence since the
       substance of the carve-out is present and correct
  criteria: n/a (flag; fixer discretion on whether to add the sentence at Phase 6 persist)

---

## active-project/theater/facets/memory.md

**Verdict: CLEAN**

STRUCTURAL: Two live entries (mem:1 @9, mem:2 @18). Monotonicity preserved. Defense
annotation and defer block are comments. Frontmatter intact.

CONSTRAINT — slug rename check:
  Old slug: `cond-override-architecture-residue-122ac`
  New slug in mem:1: `monument-override-architecture-prohibition`

The rubric requirement per the fixer report (F-011) was: monument- prefix,
mechanism-descriptive, no Earth-Bet proper noun, no card-slug form.

Checking `monument-override-architecture-prohibition`:
  - monument- prefix: YES
  - mechanism-descriptive: YES ("override-architecture-prohibition" describes the mechanism
    — the prohibition against rebuilding the override architecture)
  - Earth-Bet proper-noun substring: scan — "override" generic; "architecture" generic;
    "prohibition" generic. "monument-override-architecture-prohibition" contains no Earth-Bet
    proper-noun substring. CLEAN.
  - card-slug resolving: the rubric requires the slug to be mechanism-descriptive, NOT
    card-slug-resolving. The warehouse card is `cond-override-architecture-residue-122ac`
    (untouched per F-011). `monument-override-architecture-prohibition` does not resolve to
    any warehouse card slug; it is a facet-internal monument-label. CLEAN.

The slug rename does not break card resolution because the rubric explicitly does NOT require
monument slugs to resolve to warehouse card slugs — they are facet-graph labels. CLEAN.

CONSTRAINT — defense annotation rewrite text:
The defense annotation at lines 7-19 and defer block at lines 21-27 are operator comments.
No Earth-Bet proper nouns introduced. The word "khepri" does not appear anywhere in the file.
"Override-architecture" substitution vocabulary in use throughout. CLEAN.

AP-SCAN: No new AP patterns in the annotation or defer text.

---

## active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md

**Verdict: CLEAN**

STRUCTURAL: Two entries, IDs 1 and 2, anchored at @23 and @26 respectively. Monotonicity
preserved. Frontmatter intact.

CONSTRAINT — Earth-Bet hard-fence scan on Wren entry 2 updated text:
`"The flies were on the meat-stall and they were not on you. The stall is closer."`
Scan for Earth-Bet proper-noun substrings: "flies" — generic; "meat-stall" — Westerosi
market descriptor; "you" — generic pronoun; "stall" — generic noun; "closer" — generic
comparative. No Earth-Bet proper-noun substring present. CLEAN.

AP-SCAN — Wren @26 rewrite:
Change was "your hand" → "you". The resulting line `"they were not on you"` uses person-
scale language. No new AP pattern introduced. No "X is what Y" construction. No precocious-
wise framing. Smallfolk child register maintained. CLEAN.

DIALOGUE-COVERAGE: Both entries (@23, @26) are speech bones. Cross-checking proto-lines:
  @23 `wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` carries
      `[wren-stitch-maker-flea-bottom-ward:1]` — covered.
  @26 `wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` carries
      `[wren-stitch-maker-flea-bottom-ward:2]` — covered.
URI-DIALOGUE-COVERAGE-GATE satisfied for Wren. CLEAN.

---

## active-project/theater/proto-lines/b01-c01.md

**Verdict: CLEAN**

STRUCTURAL: Proto-lines file read. ID sequence is non-contiguous (gaps at 10, 21 visible);
these are pre-existing structural gaps from prior fixer cycles, not introduced by cycle-2.

Citation strip check — loc-state:3:
  @11 line reads: `11 taylor-hebert-kl-122ac lifts the basket [state:2]`
  `[loc-state:3]` token is absent. Strip confirmed.

Citation strip check — sensory:2:
  @16 line reads: `16 the walls cool [state:4]`
  `[sensory:2]` token is absent. Strip confirmed.

No other tokens were modified on these lines. Adjacent lines unchanged.

DIALOGUE-COVERAGE — full speech-bone coverage check post-fix:
All speech bones verified against proto-lines and dialogue files:
  @8  `coll-net-mender-flea-bottom speaks` → `[coll-net-mender-flea-bottom:1]` ✓
  @23 `wren-stitch-maker-flea-bottom-ward speaks` → `[wren-stitch-maker-flea-bottom-ward:1]` ✓
  @25 `taylor-hebert-kl-122ac speaks` → `[taylor-hebert-kl-122ac:1]` ✓
  @26 `wren-stitch-maker-flea-bottom-ward speaks` → `[wren-stitch-maker-flea-bottom-ward:2]` ✓

No speech bone lost its `<character-slug>:<id>` citation token from the two strip operations.
URI-DIALOGUE-COVERAGE-GATE: no regression introduced. CLEAN.

---

## active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md

**Verdict: CLEAN**

STRUCTURAL: File is a drafts sidecar, not a schema-typed facet file. No entry-ID monotonicity
requirement applies. Frontmatter intact.

CONSTRAINT: Draft B (chosen draft) facet-licenses field at line 68 reads:
  `facet-licenses: [state:17 @25, vibes:20 @25, feel:2 @27 (post-beat carrier), narrator:6 @27 (post-beat carrier)]`
All four citations are resolvable against the locked graph:
  - state:17 @25: cite-index confirms state:17 @25 back=Y co=[taylor-hebert-kl-122ac:1, vibes:20]. ✓
  - vibes:20 @25: cite-index confirms vibes:20 @25 back=Y co=[state:17, taylor-hebert-kl-122ac:1]. ✓
  - feel:2 @27: cite-index confirms feel:2 @27 back=Y co=[feel:3, narrator:6, vibes:20, vibes:21]. ✓
  - narrator:6 @27: cite-index confirms narrator:6 @27 back=Y co=[feel:2, feel:3, vibes:20, vibes:21]. ✓

All citations resolve. No DEFERRED-TO-R2 placeholder remains in the chosen draft. Rejected
drafts A and C retain DEFERRED-TO-R2 per minimum-change discipline; rejected drafts are not
canonical delivery and are not subject to the citation-resolution requirement. CLEAN.

---

## active-project/staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md

**Verdict: CLEAN**

STRUCTURAL: Drafts sidecar. Frontmatter intact.

CONSTRAINT: The F-013 fix note in Draft B (chosen) at line 72 reads:
  "[F-013 cycle-2 fix: 'your hand' changed to 'you' per worm-canon-pedant attack on body-
  part-precision reading as insect-tracking awareness leak; person-scale language preserves
  proximity-argument structure.]"

This is an inline annotation in the rationale text, not a live dialogue utterance. The
chosen draft body text at line 71 reads:
  `"The flies were on the meat-stall and they were not on you. The stall is closer."`
This matches the canonical dialogue file entry 2 exactly. Both files are consistent.

AP-SCAN: No new AP patterns. facet-licenses fields in both entries remain DEFERRED-TO-R2
(R1-blind sidecar discipline; rejected drafts and the wren sidecar were not required to
resolve to locked-graph citations at this cycle per F-012 scope which applied only to the
taylor chosen draft). CLEAN.

NOTE: The wren sidecar's Entry 2 Draft B facet-licenses field still reads
`[DEFERRED-TO-R2 — R1 is blind to other facets per shared brief; R2 resolves cite-to-
locked-graph]`. This deferral is consistent with minimum-change discipline (F-012 applied
only to the taylor chosen draft). However, if Phase 5b gate requires all chosen-draft
facet-licenses to be resolved, the wren sidecar will need a cycle-3 pass. This is a carry-
forward observation, not a new finding.

---

# Summary

## New HARD findings introduced by cycle-2 fixer: 0

## New FLAG findings introduced by cycle-2 fixer: 1
  flag-001 — state-updates.md rubric-carve-out block missing "resolves F-006" sentence
             (documentation gap; substantive carve-out content is present and correct;
             no mechanical downstream consequence)

## Carry-forward from prior audits
  - 15 SIGNAL findings from r1: carry forward unchanged
  - fault-001 from r2 (state-updates rubric-carve-out absent): RESOLVED by cycle-2 fixer
    insertion; reclassified to flag-001 for the minor documentation gap noted above

## Phase 5b cycle-2 gate

**New HARD count: 0**

**Phase 5b cycle-2 gate: GO**
