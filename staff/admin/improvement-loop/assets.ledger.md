# Assets Improvement Ledger

Oskar-maintained. One entry per pass. Schema: asset, change, rationale, next candidate.

---

## 2026-06-12 — Pass 1

**Asset:** `design/shoot-v2/rubric-narrator-interest.md` — Anti-patterns §

**Change:** Added Anti-pattern #11 — *Apparatus-as-subject register (DEC-0115 — HARD)*. Prohibits NI entries whose grammatical subject is the apparatus/count/feed/network/abstraction. REJECT examples: *the count closes*, *the feed flags the contact*, *the gap propagates*. Re-author rule: use the lens's concrete output as subject. Explicitly preserves inventory-tell register ACCEPT signatures (cost-language, pre-calc, weight-in-the-body) — those fire on concrete subjects and are unaffected. Paired-gate citations: `/and-write` Phase 6 `ABSTRACTION-AS-SUBJECT` (upstream) + `/and-stitch` Phase 4 `LEDGER-REGISTER` (downstream).

**Why top-ranked:**
- DEC-0115 (2026-06-08) explicitly mandates the apparatus-register fence "at every authoring surface." The NI rubric is the primary authoring surface for narrator-interest entries; the gap meant apparatus-register in NI could only be caught at `/and-stitch` Phase 4, not at the facets layer where it originates.
- The `/and-facets` Phase 4 auditor enumerates rubric §Anti-patterns automatically (CLAUDE.md Rule 11 + and-facets.md §RUBRIC-FIDELITY source-enumeration note); adding the anti-pattern to the rubric is the zero-overhead promotion path — no auditor-class-library edit required, new rule picked up on next run.
- Cost: one bounded rubric entry (~150 words). No persona voice content touched. No cross-file cascade.
- Failure mode it closes: NI entries authored with apparatus-as-subject survive facets unchanged, only surface at stitch as `LEDGER-REGISTER`, and route upstream — the roundtrip cost is one full `/and-write revise`. Catching it at rubric-fidelity time eliminates the roundtrip.

**Next candidate:**
- Feeling rubric (`rubric-feeling.md`): DEC-0115 check — does it cover apparatus-as-subject in somatic-tell descriptions? Feeling entries that describe a sensation via apparatus (*the count holds at zero; something loosens*) would not be caught by the current rubric. Lower priority than NI because the feeling facet is less apparatus-prone by design (it fires on somatic/emotional response, not on perceptual registration), but worth a targeted scan.
- Sensory rubric (`rubric-sensory.md`): AP-SCAN entry #14 (cycle-N ADD pre-validation) — verify it cross-references the fixer-ADD pre-validation rule in `and-facets.md` Phase 4 footnote cleanly. Observed mild terminology drift in prior passes.
