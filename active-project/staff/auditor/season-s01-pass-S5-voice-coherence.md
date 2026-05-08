# Pass S5 Voice Coherence Review — Season 01

```
scope: season
target: proto-lines chapters 01–10 + 3 interludes
pass: S5 (voice register coherence)
timestamp: 2026-05-07
verdict: REVISE
narrator-inventory:
  taylor-hebert-westeros: ch01, ch02, ch03, ch04, ch06, ch07, ch08, ch09, ch10
  septon-rowan: ch05
  ser-harwick-plumm: ch03-interlude
  oc-castellan-harrenhal: ch07-interlude, ch08-interlude
```

---

## Method

Cold-read verb inventory per character across all chapters they appear in, whether as narrator or as third-party-observed actor. Test: can a reader identify Plumm vs. the Castellan from verb register alone? Can Rowan's writing-sequence verbs be distinguished from Plumm's at the verb level? Does Taylor's register hold consistent across 9 narrator chapters?

---

## Character verb inventories

### taylor-hebert-westeros

**Fauna-control (Taylor-exclusive):** `dispatches`, `repositions`, `withdraws`, `directs`, `drives`, `routes`, `redirects`, `spreads`, `pulls`, `releases`, `recalls`.

**Physical cost (Taylor-exclusive):** `presses the temples`, `presses the knuckles`, `pinches the nose bridge`, `tilts the head`, `blood reaches the lip`, `exhales`, `drops` (collapse-adjacent), `stills the hands`.

**Hold (Taylor's suspension form):** `holds the feet`, `holds the chin`, `holds the hands`, `holds the eyes`, `holds the spine`.

**Traversal/posture:** `crosses [space]`, `enters/exits`, `reaches`, `faces`, `turns`, `kneels`, `rises`, `lifts the chin`, `lowers the eyes`, `grips`.

**Document:** `opens a book`, `places the book`, `opens the septon's ledger`, `closes the septon's ledger`, `takes the septon's materials`.

**Verdict: consistent** across 9 narrator chapters.

### ser-harwick-plumm

**Precision writing (Plumm-exclusive):** `draws the record book`, `uncaps the stylus`, `touches the page`, `writes the name`, `writes the sept entry`, `numbers the entry`, `lifts the stylus`, `dips the stylus`, `presses the seal`, `lifts the seal`.

**Document management:** `produces`, `opens/closes/pockets the record book`, `rolls`, `presents`, `marks the page`.

**Verdict: consistent.** Almost entirely ledger-on-desk register. No spatial-character traversal. Plumm-proxy in ch02 (`marks`, `traces`, `opens the satchel`, `closes the ledger`, `stills the hand`) transfers register cleanly to outdoor-circuit context.

### oc-castellan-harrenhal

**Supervisory/spatial:** `walks the nave/yard`, `crosses the hall/yard`, `retreats`, `steps back`, `faces`, `turns`, `returns to the table`.

**Document review (handler, not writer):** `produces`, `unfolds`, `turns the page`, `lifts the page`, `sets`, `stacks`, `closes the document`, `covers the page`.

**Command/control:** `speaks`, `raises a hand`, `enters/exits`.

**Verdict: consistent.** Reviewer/handler verbs only — never writes, marks, numbers, dips, or seals.

### septon-rowan

**Conscience/weight (Rowan-exclusive):** `drops the travel pack`, `drops the eyes`, `lowers the eyes`, `holds the eyes` (sustained moral attention), `touches the ledger` (moral gesture, ch05 ID 85), `kneels`.

**Document drafting (ch06 claim petition):** `draws the parchment`, `dips the stylus`, `writes the heading/claimant entry/grounds clause/closing line`, `lifts the parchment`, `blows the ink`, `folds`, `seals the fold`.

**Stylus-management hesitation rhythm (ch06):** `takes the stylus`, `places the stylus`, `takes the stylus` again — moral-ambiguity register in action.

**Verdict: consistent.** Distinct from Plumm's procedural efficiency.

---

## Voice-collapse tests

**T1 — Plumm vs. Castellan document handling:** NO COLLAPSE. Plumm creates record content (draws, uncaps, writes, numbers, presses seal); Castellan positions and reviews (unfolds, turns, lifts, sets, stacks, covers).

**T2 — Rowan vs. Plumm writing sequence:** NEAR-MISS. Both `draw`, `dip`/`uncap`, `write`, `lift the stylus`. Object vocabulary rescues the distinction (Rowan: document sections; Plumm: record slots; Rowan also `blows ink`, `folds`, `seals`; Plumm `numbers`, `pockets`). Flag for prose-pass: maintain object specificity or registers will blur.

**T3 — `stills` cross-register use:** plumms-man `stills` (environmental freeze, no object); Taylor `stills the hands` (cost-manifestation, body-part object). Disambiguated by object. Maintain in prose.

---

## Drift findings

### DRIFT-01 — `taylor-hebert-westeros flips the document` (ch07 ID 63)

`flips` is an administrative-handling verb belonging to Plumm/Castellan register. Taylor's document verbs elsewhere are `opens`, `places`, `takes`, `closes`. Single occurrence at the ch07 emotional peak (Taylor reading the document that confirms the claim is lost) — disproportionate weight at the SVO layer.

**Fix:** `taylor-hebert-westeros turns the document` or `taylor-hebert-westeros opens the document`.

### DRIFT-02 — `taylor-hebert-westeros crosses the sept door` (ch07 ID 91)

`crosses [space]` requires a traversable space; `door` is a fixed point, not a space. ID 90 already places her exiting; ID 91 ambiguous between lateral pass-by and reversal. Spatial-vocabulary ambiguity at SVO layer propagates to facet loc-state assignments.

**Fix:** `taylor-hebert-westeros passes the sept door` or `taylor-hebert-westeros reaches the sept door`.

---

## Flat-affect test

**FAULT-VOICE-COLLAPSE: NOT triggered.** Three mechanisms prevent flat affect:
1. Taylor's fauna-control verbs (no other character uses them)
2. Plumm's precision recording verbs (specialist register)
3. Rowan's weight/conscience verbs (distinct from both Taylor's cost and Plumm's procedure)

**Castellan note:** weakest voice of the four — `walks/crosses/retreats/faces/raises a hand` are generic motion. Distinguishable from Plumm (never writes) and Taylor (no cost vocabulary), but solo-scene voice will depend on prose context rather than bone vocabulary. Not a collapse; prose-pass risk only.

---

## Verdict

**REVISE** — two targeted fixes, both in ch07.

| ID | Chapter | Line | Verb | Fix |
|----|---------|------|------|-----|
| DRIFT-01 | ch07 | 63 | `flips` | `turns` or `opens` |
| DRIFT-02 | ch07 | 91 | `crosses the sept door` | `passes` or `reaches` |

**Prose-pass advisories (non-blocking):**
- Rowan/Plumm writing-sequence near-miss: maintain object specificity.
- `stills` cross-character use: maintain object distinction.
- Castellan thin solo-scene register: prose-layer markers required.
