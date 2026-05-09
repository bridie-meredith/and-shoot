---
audit:
  scope: facet-phase-review
  target: design/shoot-v2/phase1-vibes-baseline-naive.md
  timestamp: 2026-05-07
  phase: phase1-vibes-baseline-review
  rubric: design/shoot-v2/rubric-vibes.md
  corpus: design/shoot-v2/vibes-corpus.md
---

# Phase 1 Vibes-Updates Baseline Review

## Headline

**Accept rate: 0/29 = 0%.**

Every entry fails gate 4 (licensed-by absent). No entry reaches consideration of other gates.
Baseline-to-beat for Phase 2: 0 correct out of 29 attempted entries.

---

## Per-fire verdict table (29 entries)

All entries use a malformed content shape — fused `target:keyword` with `+` after the bracket, absent `| licensed-by:` field. The V1 schema shape is `<target> <op> <keyword>: [tokens] | licensed-by: <source>`. The baseline omits the licensed-by clause universally and mis-arranges target/op/keyword. Each entry therefore carries at minimum AP4 (gate 4 fail). Secondary faults are noted per entry.

| # | Beat | Baseline fires on | Faults | Notes |
|---|------|-------------------|--------|-------|
| 1 | @11 | episode:the-machinery-arrives | **AP4** (no licensed-by) | Tokens match corpus quality; scope target itself is valid; all 4 entity co-targets of E1 missing (AP12 at event level) |
| 2 | @13 | episode:the-machinery-arrives | **AP4, AP5** | AP5: entry 1 already added this keyword to episode; second `+` should be `++`; token `bureaucratic-momentum-indifferent-to-the-person` restated in entry 25 |
| 3 | @18 | episode:the-naming | **AP4** | Beat anchor @18 is outside the naming event window (@47-@48); premature firing |
| 4 | @23 | episode:the-naming | **AP4, AP5** | AP5: entry 3 already added keyword; beat @23 still pre-naming |
| 5 | @26 | episode:the-naming | **AP4, AP5** | AP5: third `+` on episode:the-naming |
| 6 | @28 | episode:the-letter | **AP4** | First letter fire; scope target valid; entity target actor:taylor missing |
| 7 | @33 | episode:the-septon-as-absence | **AP4** | Tokens match corpus entry 12 quality; scope valid; entity co-targets (actor:taylor, actor:septon-dying-protector) missing |
| 8 | @33 | season:the-septon-dying | **AP4, AP9** | AP9: entity actor:septon-dying-protector is the correct target; displacing to season scope when the entity target fits is abstract-scope-when-entity-fits |
| 9 | @38 | episode:the-letter | **AP4, AP5** | AP5: entry 6 already added keyword |
| 10 | @41 | episode:the-letter | **AP4, AP5** | AP5: third `+` on episode:the-letter |
| 11 | @44 | episode:the-letter | **AP4, AP5** | AP5: fourth `+` on episode:the-letter |
| 12 | @47 | episode:the-naming | **AP4, AP5** | AP5: fourth `+` on episode:the-naming; beat @47 is correct naming-event anchor |
| 13 | @48 | episode:the-naming | **AP4, AP5** | AP5: fifth `+` on episode:the-naming; token `the-door-that-closes-on-its-own-momentum` already in entry 3 (AP11 on any extension) |
| 14 | @48 | season:the-census | **AP4** | Season scope; AP9 partial: the census event has entity targets (actor:taylor, actor:census-officer) that were never written |
| 15 | @48 | series:impressment | **AP4** | Series scope; token `bureaucratic-violence` is AP7 (vague, no operator can act on it specifically) |
| 16 | @52 | episode:the-yard-as-witness | **AP4** | First yard fire; token quality acceptable; actor:taylor, actor:mira, actor:edric co-targets all missing |
| 17 | @52 | season:invisibility | **AP4** | Season scope; token `the-performance-of-ordinary` has acceptable quality |
| 18 | @55 | episode:the-yard-as-witness | **AP4, AP5** | AP5: second `+` on episode:the-yard-as-witness |
| 19 | @57 | episode:the-yard-as-witness | **AP4, AP5** | AP5: third `+` on episode:the-yard-as-witness |
| 20 | @57 | season:invisibility | **AP4, AP5** | AP5: second `+` on season:invisibility |
| 21 | @64 | episode:the-naming | **AP4, AP5** | AP5: sixth `+` on episode:the-naming; beat @64 is outside naming event window |
| 22 | @64 | season:the-census | **AP4, AP5** | AP5: second `+` on season:the-census |
| 23 | @64 | series:blood-legitimacy | **AP4, AP8** | AP8: token `the-game-she-was-not-born-into` is prose narration, not word-algebra compression |
| 24 | @66 | series:impressment | **AP4, AP5, AP8** | AP5: second `+` on series:impressment; AP8: token `what-happens-to-people-without-protection` is multi-clause prose token |
| 25 | @73 | episode:the-machinery-arrives | **AP4, AP5** | AP5: third `+` on episode:the-machinery-arrives; token `bureaucratic-momentum-indifferent-to-the-person` is a duplicate of entry 2 (AP11) |
| 26 | @73 | episode:the-septon-as-absence | **AP4, AP5** | AP5: second `+` on episode:the-septon-as-absence; beat @73 is outside event window (@31-@33) |
| 27 | @74 | episode:the-letter | **AP4, AP5** | AP5: fifth `+` on episode:the-letter; tokens `held-at-her-side` and `the-useless-object` are duplicates of entries 6 and 11 (AP11) |
| 28 | @77 | series:survival | **AP4** | New series keyword; token quality is the strongest in the file (`functional-under-impossible-conditions`, `adaptation-as-armor` are word-algebra, operator-actionable) |
| 29 | @77 | season:invisibility | **AP4, AP5, AP8** | AP5: third `+` on season:invisibility; AP8: `building-before-you-can-build` is borderline prose-narration |

---

## Per-skip verdict table (corpus fires never attempted)

The corpus identifies 16 gold-standard fires across 6 entity targets and episode scope. The baseline fires 0 entity-target entries — all 11 entity-target fires from the corpus are SKIP-MISSED.

| Corpus entry | Target | Event keyword | SKIP verdict | Calibration anchor? |
|---|---|---|---|---|
| REF-C1a | actor:taylor-hebert-westeros | the-machinery-arrives | **SKIP-MISSED** | C1 |
| REF-C1b | actor:mira-stonefield | the-machinery-arrives | **SKIP-MISSED** | — |
| REF-C1c | actor:edric-cray | the-machinery-arrives | **SKIP-MISSED** | — |
| REF-C1d | actor:census-officer | the-machinery-arrives | **SKIP-MISSED** | — |
| REF-C2a | actor:taylor-hebert-westeros | the-letter | **SKIP-MISSED** | — |
| REF-C3a | actor:taylor-hebert-westeros | the-naming | **SKIP-MISSED** | — |
| REF-C4a | actor:taylor-hebert-westeros | the-septon-as-absence | **SKIP-MISSED** | — |
| REF-C4b | actor:septon-dying-protector | the-septon-as-absence | **SKIP-MISSED** | C2 |
| REF-C5a | actor:taylor-hebert-westeros | the-yard-as-witness | **SKIP-MISSED** | — |
| REF-C5b | actor:mira-stonefield | the-yard-as-witness | **SKIP-MISSED** | C3 |
| REF-C5c | actor:edric-cray | the-yard-as-witness | **SKIP-MISSED** | — |

All four calibration anchors (C1 entity fan-out, C2 absent-actor co-target, C3 non-POV co-target, C4 scope stratification) were tested by the baseline:

- **C1**: episode scope was reached but all 4 entity co-targets missed. Fan-out failed.
- **C2**: actor:septon-dying-protector never fired. Season:the-septon-dying wrote to the wrong scope (AP9) instead of the entity.
- **C3**: actor:mira-stonefield and actor:edric-cray never fired on any event.
- **C4**: episode scope targets were authored correctly in principle (episode:the-naming was attempted). Scope-stratification concept was present but was the ONLY mode used (entity targets absent entirely).

---

## File-shape verdict

**SHAPE-FAIL.**

Two structural failures:

1. **Content shape malformed throughout.** V1 schema shape is `<target> <op> <keyword>: [tokens] | licensed-by: <source>`. The baseline uses `<target>:<keyword> + [tokens]` — target and keyword are fused by `:` with no space separation, the `+` op appears after the keyword (not before it), and the `| licensed-by:` clause is absent from all 29 entries. This is not a minor formatting variance; the schema shape is the machine-readable contract.

2. **Missing licensed-by universally.** The `| licensed-by:` field is structurally absent from every entry, not merely incorrect. The baseline author did not know the field existed (rubric-blind; schema-current text does not surface the licensed-by requirement in the same explicit form as the rubric).

Frontmatter is present and complete (`facet`, `episode`, `author`, `phase`, `note` fields). This is SHAPE-PASS on the header block only.

---

## Systemic faults

**SF-1: Licensed-by universally absent (gate 4 / AP4).**
All 29 entries lack `| licensed-by:` field. This is the single largest contamination vector. The schema-current text does not foreground the licensed-by requirement as strongly as the rubric; the rubric-blind author had no basis to know it was required. 29/29 entries fail this gate.

**SF-2: Entity targets entirely absent (gate 7 / AP12).**
Zero entity-target fires (`actor:`, `loc:`, `prop:`). All 29 entries target episode, season, or series scope. The rubric specifies 70-90% of entries should be entity-target adds. The baseline inverts this completely (0% entity, 100% scope). Fan-out coherence fails at the event level for all five events.

**SF-3: Cascading duplicate-adds instead of `++` extensions (AP5 / AP10).**
The author treats each new token for a keyword as a fresh `+` fire rather than an `++` extension. This produces 5-6 `+` fires on episode:the-naming, 5 on episode:the-letter, 3 on episode:the-machinery-arrives, etc. At minimum 15 entries (entries 2,4,5,9,10,11,12,13,18,19,20,21,22,24,25,26,27,29) should have been `++` or refused. The schema-current text describes `++` but the author did not model it.

**SF-4: Content shape malformed (schema-current-text mismatch).**
The fused `target:keyword` construction and displaced `+` position deviate from V1 schema. This likely traces to the author reading the schema's keyword examples as prose description rather than as a strict positional grammar. All entries would fail a mechanical schema-shape validator.

**SF-5: Scope-only authoring displaces entity-bound events to abstract scope (AP9).**
Several events that have clear entity targets (septon-dying-protector for E4, census-officer for E1) are displaced to season scope (`season:the-septon-dying`, `season:the-census`). This compounds the entity-target absence: instead of the correct entity being named, the event leaks upward to a scope target that cannot carry individual actor operator-bias.

**SF-6: Beat anchor scatter — fires spread across the entire episode rather than pinned at event windows.**
The baseline spreads 29 fires across beats @11-@77, anchoring to individual beats as if each beat is a new vibe-cause rather than anchoring vibe-fires to the event's peak beat as the rubric specifies. This produces spurious pre-event fires (entries 3,4,5 anchor the-naming at @18, @23, @26 — before the naming event at @47-@48) and spurious post-event fires (entry 26 anchors the-septon-as-absence at @73, long after the event at @31-@33). The correct pattern is to anchor at the event's closing beat (per corpus: most fires anchor at the last beat of the event window).

---

## Verdict

**Phase 1 baseline accept rate: 0/29 = 0%.**

This matches the pre-Phase-0 corpus expectation (anticipated 0-25%; feeling and metaphor both came in at 0%). The failure is systemic, not marginal: the rubric-blind author had no visibility into (a) the licensed-by field requirement, (b) the entity-target primacy rule, or (c) the `++` extension model. Token quality is mixed but occasionally strong (entries 1, 7, 28 have corpus-quality tokens buried under gate failures). The structural frame is entirely wrong.

Phase 2 rubric-aware fork must correct all six systemic faults simultaneously to reach the expected 14-20 entry range with ~14-16 correct fires.
