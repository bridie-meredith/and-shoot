---
facet: state-updates
phase: 4 (defense/revise — studio batch)
author: studio
episode: s01e01
rubric: design/shoot-v2/rubric-state-updates.md (V2 locked)
source-phase2: design/shoot-v2/phase2-state-updates-output-studio.md
source-audit: active-project/staff/auditor/phase2-state-updates-audit.md
source-seams: active-project/staff/auditor/phase3-state-updates-seams.md
---

## 1. Header note — prop slug rename

Per Phase 3 file-level seam and Phase 2 audit: `prop:letter` and `prop:district-ledger` lack `oc-` prefix.
The rubric §Authority REJECT signatures state: "Studio may extend with `oc-*` for genuine project-originals,
but extension must be flagged."

Both props are project-originals introduced in s01e01. Neither has a formal card in `cards/props/`
(INDEX.md is empty). Both are confirmed project-original props with implicit warehouse presence in s01e01
per the episode's own proto-line record. The `oc-*` extension is rubric-licit when flagged.

Resolution applied throughout this file:
- `prop:letter` → `prop:oc-letter`
- `prop:district-ledger` → `prop:oc-district-ledger`

Margit referral note at §5 below.

---

## 2. Per-entry defense / revise / cull

### ID-1 — @9 `prop:oc-district-ledger.physical-condition: rolled -> unrolled`

**Phase 3 seam (STRONG):** prop slug lacks `oc-` prefix and warehouse-presence documentation.

**DEFEND** with rename.

The slug concern is resolved by renaming to `prop:oc-district-ledger` throughout (see §1). The
warehouse-presence documentation is: this prop is a project-original introduced by proto-line @9 ("the
clerk unrolls the parchment"); it appears in the rubric's own calibration anchor at @48 and @64, which
establishes it as the rubric's working reference for the episode. The `oc-*` extension is flagged (see §5
margit referral). The seam does not contest the Reality or Frugality axes, and both pass: "unrolls" is an
explicit physical-condition transition verb; `<old>=rolled` is first-touch with no prior entry on this
field. Entry survives with slug rename.

**What changed:** `prop:district-ledger` → `prop:oc-district-ledger`. No other change.

---

### ID-2 — @30 `prop:oc-district-ledger.taylor-entry: absent -> name-inscribed-pending-dictation`

**Phase 3 seam (STRONG):** `<old>=absent` drift-old risk; @30 may not be first-touch; calibration anchor
at @48 uses `<old>=pending`, implicitly acknowledging the name may pre-date @30.

**CULL.**

The seam is correct and the guidance concurs. Reading the proto-line sequence carefully:

- @18: "the ledger holds a name on the top line" — a name is already on the ledger (another ward's name
  pre-entered before Taylor joined the line).
- @20–@22: "the officer works the line / speaks to each ward / the clerk's stylus follows the dictation"
  — the clerk is recording entries for the line as the officer works it. Taylor is in the line at @15.
- @30: "the stylus moves on taylor's name" — this is the clerk following dictation on Taylor's existing
  entry, not necessarily a first-touch inscription. "Moves on" is motion-over, not inscription-of.

The Phase 2 calibration anchor for @48 explicitly uses `<old>=pending` — the rubric's own authority
for this chain labels the pre-@48 state as `pending`, which is consistent with the name being on the
ledger prior to @30 (possibly inscribed during the officer's @20–@22 line-work). If the name was on the
ledger before @30, `<old>=absent` is drift-old (anti-pattern #5) and corrupts the chain.

Culling ID-2 is the correct move. The @30 proto-line "stylus moves on taylor's name" is a motion verb
on an existing entry, not an inscription verb creating a new entry. The Reality axis fails on first-touch
claim.

**Consequence for ID-8:** with ID-2 culled, ID-8's `<old>` reverts to `pending` per the calibration
anchor's own phrasing. This repairs ID-8's chain without requiring further revision.

---

### ID-3 — @38 `prop:oc-letter.holder: taylor -> mid-air-between-them`

**Phase 3 seam (MODERATE):** "mid-air-between-them" may not be a valid holder value; prop holders are
typically actor slugs or location slugs, not relational-spatial strings.

**REVISE.**

The seam identifies a genuine weakness: the rubric's holder field domain is actor slugs and location
slugs, not relational-spatial descriptions. "Mid-air-between-them" is not a slug value on any actor or
location. The defense in Phase 2 leaned on the calibration anchor's own phrasing — but the calibration
anchor uses "mid-air-between-them" as a descriptive label in an example, not as a validated holder-value
slug in a schema-correct entry.

The instruction guidance recommends: use a defensible holder value like `extended-by-taylor` or
`mid-presentation`. The proto-line @38 is "taylor puts the letter into the air in front of the officer"
— the letter is extended by Taylor, still under her agency, not yet received. The letter has not been
released to a canonical holder (not in a location, not in the officer's hand). Taylor is still the agent;
she has extended it into the presentation position.

Revised value: `extended-by-taylor` (Taylor holds it extended; she has not released it to a location or
to the officer; the holder field admits an extension-state value in the holder namespace when the prop
is in a transitional but Taylor-controlled position).

**Consequence for ID-4 and ID-6:** ID-4's `<old>` must update to `extended-by-taylor` (from
`mid-air-between-them`). ID-6 is unaffected (its `<old>=officer` traces from ID-4's `<new>`).

**What changed:** `<new>` value from `mid-air-between-them` to `extended-by-taylor`. Entry survives;
slug updated to `prop:oc-letter`.

---

### ID-4 — @40 `prop:oc-letter.holder: extended-by-taylor -> officer`

**Phase 3 seam (MODERATE):** receipt may occur at @39 (forbidden by STATE-UPDATE NOTE), creating a
paradox where the fire is either at @39 (forbidden) or lagging at @40.

**DEFEND.**

The seam's paradox dissolves under the strict proto-line reading. @39 is "taylor sets her feet on the
dirt where his next pace commits" — this is Taylor's act, not the officer's. The officer does not appear
in the @39 proto-line; there is no officer-receipt verb at @39. The officer's first action after @38 is
@40: "the officer unfolds the letter." Unfolding presupposes physical possession. There is no proto-line
between @38 and @40 that establishes the officer receiving the letter. The receipt-beat is the unfold-beat
(@40), because that is the first verb establishing the officer has physical control of the prop.

The STATE-UPDATE NOTE on @39 forbids canonical state-update co-citation on @39-class beats — but @39
is not a beat where the officer receives anything; @39 is Taylor's feet-set. The paradox the seam
describes does not exist in the proto-line record: the officer's receipt is established at @40 by his
action on the prop, not at @39. Filing at @40 is not lagging; it is the beat where the field flips.

`<old>` updates to `extended-by-taylor` per ID-3 revision.

---

### ID-5 — @41 `prop:oc-letter.seal-condition: intact -> broken`

**Phase 3 seam (MODERATE):** same prop-slug authority concern as ID-1 (`prop:letter` without `oc-`).

**DEFEND** with rename.

Identical resolution to ID-1: slug renamed to `prop:oc-letter` throughout; warehouse-presence documented
as project-original (see §1 and §5). The Reality axis is uncontested: "the seal breaks" is named
explicitly as an ACCEPT signature in the rubric ("breaks the seal"). Frugality passes: `<old>=intact`
is first-touch, no prior seal-condition entry. Authority: studio owns prop physical fields.

**What changed:** slug only.

---

### ID-6 — @45 `prop:oc-letter.holder: officer -> taylor`

**Phase 3 seam (MODERATE):** chain-collapse risk if ID-3 is culled.

**DEFEND** (chain repaired by ID-3 revision, not cull).

ID-3 was revised, not culled. The holder chain runs: `taylor` (episode-start) → `extended-by-taylor`
(@38) → `officer` (@40) → `taylor` (@45). The chain is intact; each link is valid. `<old>=officer`
traces correctly from ID-4's `<new>`. The calibration anchor explicitly authorizes this entry on @45 as
the flip-beat. No revision needed beyond slug rename.

**What changed:** slug only.

---

### ID-8 — @48 `prop:oc-district-ledger.taylor-entry: pending -> dictated-provisional`

**Phase 3 seam (STRONG):** chain dependency on ID-2; if ID-2 culled, `<old>` must revert to `pending`.

**REVISE** (auto-repair from ID-2 cull).

ID-2 is culled. The `<old>` for ID-8 reverts to `pending` — which matches the calibration anchor's own
phrasing exactly: "prop:district-ledger.taylor-entry: pending -> dictated-provisional." This is now
a first-touch entry on this field (the name was on the ledger in some pre-dictation state before @30;
`pending` is the rubric's canonical label for the pre-@48 state of Taylor's ledger entry). No chain
corruption. Entry survives with `<old>=pending` and slug rename.

**What changed:** `<old>` from `name-inscribed-pending-dictation` to `pending`; slug to `prop:oc-district-ledger`.

---

### ID-9 — @57 `studio.doors_and_shutters.cottage-door: closed -> open`

**Phase 3 seam (STRONG):** drift-old on `<old>=closed` (sourced from s01e06 state.md, not s01e01
episode-open baseline); Reality axis also strained (door-crossing verb is not a door-opening verb).

**CULL.**

The Phase 2 audit already marked this INCORRECT-REALITY, and Phase 3's adversarial pressure confirms
both failure axes simultaneously.

First, `<old>=closed` is not established by any s01e01 proto-line or s01e01 episode-open state file.
The s01e06 `state.md` records `cottage-door: CLOSED` for a scene set episodes later — using it as the
s01e01 baseline is anti-pattern #5 (drift-old). There is no s01e01 episode-open state that establishes
the cottage door as closed at the start of this scene.

Second, the Reality axis: "edric steps back through the door" is a crossing verb, not a door-state verb.
A door can be stepped through while already open. The rubric's ACCEPT signatures name explicit transition
verbs ("closes the door"); a crossing-verb does not establish a door-opening event.

Culling ID-9 means the cottage-door state is not written back for s01e01. This is correct: the s01e01
proto-line record does not establish the cottage-door state at any point. The SM-2 continuity gap (door
left unresolved) is a known Phase 4 advisory: no proto-line exists to anchor either a door-open or
door-close entry for s01e01. The write-back gap is preferable to a drift-old entry. Showrunner must
confirm s01e01 episode-open door state from sources other than this file before any door entry can ship.

**Consequence:** the studio.* target class loses its only entry. See §3 (file-level seam response) for
the new studio.* fire.

---

### ID-11 — @64 `prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`

**Phase 3 seam (MODERATE):** two-step chain dependency (ID-2 and ID-8); if upstream seeded incorrectly,
ID-11's `<old>` is tainted.

**DEFEND.**

The chain concern dissolves with ID-2's cull and ID-8's repair. The repaired chain is:

- @48: `prop:oc-district-ledger.taylor-entry: pending -> dictated-provisional` (ID-8, now first-touch)
- @64: `prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin` (ID-11)

Both links are clean. ID-11's `<old>=dictated-provisional` traces directly from ID-8's `<new>`, which
is now an unambiguous first-touch from `pending`. The calibration anchor explicitly authorizes ID-11 as
the canonical state-update beat ("FIRE: prop:district-ledger.taylor-entry: dictated-provisional ->
marked-parallel-margin"). Tensometer @64=3, STATE-UPDATE NOTE "co-citation strongly expected" is
honored. Irreversible; absolute persistence.

**What changed:** slug to `prop:oc-district-ledger`.

---

### ID-13 — @68 `prop:oc-district-ledger.physical-condition: unrolled -> folded-or-stored`

**Phase 3 seam (STRONG):** the board is distinct from the district ledger; firing on the wrong target
(`prop:oc-district-ledger.physical-condition`) when the proto-line says "the clerk folds the board" may
be a wrong-target fire or compound-entry variant.

**REVISE.**

The seam is correct on the target-precision issue. The Phase 2 author acknowledged "the board is distinct
from the ledger" but chose to treat the board-folding as closing the ledger's physical-condition field.
This is a wrong-target fire: the district ledger's parchment physical-condition (unrolled) is not
directly established as changing by the board-folding verb — the board can fold while the parchment
remains on it or separately. These are two distinct props.

However: the board itself is also a project-original prop with no formal card (same warehouse-presence
situation as `prop:oc-district-ledger`). The board appears at @17 ("the clerk balances the ledger on
the board against his hip") and is folded at @68. If a board-fire is authored, it would be:
`prop:oc-clerks-board.physical-condition: open -> folded`.

But the instruction guidance recommends: cull ID-13 if the seam reveals wrong-target and revision cannot
save it. The alternative — firing `prop:oc-clerks-board.physical-condition: open -> folded` — is a new
prop introduction at the final entry, requiring a margit referral for the clerks-board card. The ledger
chain's @9 open (rolled → unrolled) does not have a matching close in the proto-line record that can be
anchored cleanly: the parchment's re-rolling is not established by any verb at @68 (the board folds; the
parchment's fate is unspecified).

Decision: CULL ID-13. The @9 field (`prop:oc-district-ledger.physical-condition: rolled -> unrolled`)
remains open at episode close — the parchment stays unrolled as far as the proto-line record establishes.
The board-folding event is a real state-change on a different prop (`prop:oc-clerks-board`), but
authoring a new prop entry in Phase 4 without a card is margit-referral territory. Adding a
`prop:oc-clerks-board` margit referral to §5.

---

## 3. File-level seam response

**Seam (STRONG):** the file's only `studio.*` entry (ID-9) is INCORRECT-REALITY; culling it leaves zero
verified `studio.*` fires; real target diversity drops to 2 classes (prop + actor), failing the rubric's
≥3-class requirement.

**Response: add one studio.* fire.**

The rubric §Authority ACCEPT signatures lists `studio.actors_in_yard` as a named studio field. The
proto-line record establishes a clear, persistent, irreversible change in the spatial composition of the
yard: at @11 the officer comes through the gate; at @57 Edric steps back through the door; at @65 the
officer's shoulder turns toward the gate, departing shortly after; by @68 the administrative party has
dispersed. The strongest candidate for a studio.* fire is the spatial-composition change at @57 when
Edric withdraws: the yard loses its last non-officer adult cover (per narrator-interest @57: "the door
takes the last adult cover with it"). The Edric-fork already fires on `actor:edric-cray.sublocation`
at @57; studio's contribution to the same beat is the environment-level consequence.

**New studio fire — @57:**

`@57 studio.actors_in_yard: officer+taylor+mira+edric -> officer+taylor+mira`

- Reality: Edric's withdrawal from the yard at @57 is established by the proto-line verb "steps back
  through the door." The yard's actor-composition changes persistently at @57: Edric is gone. The change
  persists through @65 (officer departs), @68 (clerk folds board), @70–@77 (Taylor moves to sept door);
  Edric does not return to the yard during s01e01. Strip test: remove the entry — the field would still
  be at `<new>` (Edric absent from yard) at all subsequent beats. The entry is not parasitic.
- Authority: `studio.actors_in_yard` is a named field on `staff/studio/state.md` (listed in the rubric's
  ACCEPT signatures). Studio is the licensed author.
- Frugality: `<old>=officer+taylor+mira+edric` is the yard-composition state that has held since @11
  (officer entered) and @14–@15 (Taylor and Mira entered the line); this is the established cast of the
  yard through the confrontation cluster. `<new>=officer+taylor+mira` reflects the one-person reduction.
  No prior state-update has fired on this field, making this first-touch from the project-setup baseline.
- Cross-facet: tensometer @57=2 (reversal-proximity; "this IS the social reversal — Edric's retreat");
  narrator-interest @57 fires ("the door takes the last adult cover with it"). Studio.* entries do not
  require narrator-interest co-citation; alignment is clean.
- Anti-pattern check: not registration-as-state (the yard composition genuinely changes, persists, and
  is a tracked spatial field). Not actor-state authoring (the entry is studio.actors_in_yard, not
  actor:edric.*; that field is studio's domain). Not compound (one field, one delta).

**ID-9 is culled; new @57 studio.actors_in_yard fire replaces it.** The studio.* target class now has
one verified fire with clean Reality, Authority, and Frugality.

**Refusal seam S6 (@43 spatial-state) — THIN, maintain NONE.**

The seam argues for a `studio.spatial_layout.officer-orientation` entry at @43. This is too granular:
officer orientation within the yard is an actor-position aspect (officer fork's domain) and the officer
fork is not dispatched in this batch. Studio's `spatial_layout` field tracks room geometry and furniture,
not individual actor facing. The seam is THIN; the refusal stands. No studio spatial-layout entry at @43.

**Refusal seam S5-close (@57 door-close) — maintain NONE.**

The seam argues that "steps back through the door" plus the Edric destination "past threshold" is
sufficient establishment of a door-close at @57. Studio maintains the strict proto-line reading: the
crossing verb establishes position-change, not door-state. "Past threshold" in the Edric-fork entry
describes sublocation, not door mechanism. The rubric's ACCEPT signatures name explicit transition verbs
for door-state ("closes the door"); a crossing-verb compound-read is not sufficient. Refusal stands.
The SM-2 write-back gap is a known advisory: showrunner must source the door-close from a non-proto-line
baseline before write-back.

---

## 4. Final revised entry list

(Monotonic IDs, schema form, pure. Entries 3b/4b/6 carried unchanged except slug. Culled entries omitted.
New fire added as ID-10.)

```
1  @9  prop:oc-district-ledger.physical-condition: rolled -> unrolled
       # field-extension: physical-condition (first-touch; ledger deployed at @9; no close entry
       # in s01e01 proto-line record; field stays at unrolled through episode close)
       # oc-flag: prop:oc-district-ledger is a project-original prop; margit referral §5

2  @38 prop:oc-letter.holder: taylor -> extended-by-taylor
       # oc-flag: prop:oc-letter is a project-original prop; margit referral §5

3  @40 prop:oc-letter.holder: extended-by-taylor -> officer

4  @41 prop:oc-letter.seal-condition: intact -> broken

5  @45 prop:oc-letter.holder: officer -> taylor

6  @48 prop:oc-district-ledger.taylor-entry: pending -> dictated-provisional
       # field-extension: taylor-entry (first-touch from pending; calibration anchor phrasing
       # for @48 uses <old>=pending; ID-2 from Phase 2 culled; this is the correct first-touch)

7  @57 studio.actors_in_yard: officer+taylor+mira+edric -> officer+taylor+mira
       # new fire added at Phase 4 to restore studio.* target-class coverage
       # edric exits through cottage door at @57; yard composition changes persistently

8  @64 prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin
       # field-extension: taylor-entry (irreversible parallel-marks; tensometer @64=3,
       # STATE-UPDATE NOTE "co-citation strongly expected" — honored)
```

**Final count: 8 entries.**

**Distribution:**
- `studio.*`: 1 entry (@57 actors_in_yard)
- `prop:oc-letter.*`: 3 entries (@38, @40, @41, @45 — 4 entries)

Wait — recount:
- `studio.*`: 1 entry (@57 — new fire)
- `prop:oc-letter.*`: 4 entries (@38, @40, @41, @45)
- `prop:oc-district-ledger.*`: 3 entries (@9, @48, @64)

**Total: 8 entries / 77 beats = 10.4% — within the 8–18% sparsity band.**

**Target diversity:** 2 target classes in studio's batch (studio.*, prop:oc-*). Combined with actor:*
entries from the Taylor and Edric forks (IDs 7, 10, 12, 14, SM-1 from the canonical merged list), the
file-level target diversity across all forks reaches ≥3 classes. Studio's own batch is 2 classes; the
file-level is satisfied by the multi-fork structure.

**Curve check:**
- Approach zone @1–@22: 1 entry (@9). 1/22 = 4.5%. PASS (permitted-silent).
- Confrontation zone @23–@68: 7 entries (@38, @40, @41, @45, @48, @57, @64). PASS.
- Release zone @69–@77: 0 entries. PASS (no prop or studio state changes in the release zone per
  proto-line record).

**Corrected entry list (clean):**

```
1  @9  prop:oc-district-ledger.physical-condition: rolled -> unrolled
       # field-extension: physical-condition (first-touch; project-original prop; oc-flag)

2  @38 prop:oc-letter.holder: taylor -> extended-by-taylor
       # project-original prop; oc-flag

3  @40 prop:oc-letter.holder: extended-by-taylor -> officer

4  @41 prop:oc-letter.seal-condition: intact -> broken

5  @45 prop:oc-letter.holder: officer -> taylor

6  @48 prop:oc-district-ledger.taylor-entry: pending -> dictated-provisional
       # field-extension: taylor-entry (first-touch from calibration-anchor-canonical <old>=pending)

7  @57 studio.actors_in_yard: officer+taylor+mira+edric -> officer+taylor+mira
       # Phase 4 new fire; studio.* target coverage

8  @64 prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin
       # field-extension: taylor-entry (irreversible; tensometer @64 STATE-UPDATE NOTE honored)
```

---

## 5. Margit referral note

**MARGIT REFERRAL — Phase 5 advisory (non-blocking):**

Two project-original props used across studio's s01e01 state-updates entries have no formal card in
`cards/props/` (INDEX.md is empty). Both are rubric-licit under `oc-*` extension when flagged. Cards
should be authored before write-back to canonical state files.

| Prop slug | First appearance | Used in entries |
|-----------|-----------------|-----------------|
| `prop:oc-letter` | s01e01 @28 ("taylor presses the letter forward") | IDs 2, 3, 4, 5 |
| `prop:oc-district-ledger` | s01e01 @9 ("the clerk unrolls the parchment") | IDs 1, 6, 8 |

Additionally, a third project-original prop was identified during Phase 4 review:

| Prop slug | First appearance | Status |
|-----------|-----------------|--------|
| `prop:oc-clerks-board` | s01e01 @17 ("the clerk balances the ledger on the board against his hip") | Not used in final entry list (ID-13 culled); board-folding event at @68 is a real prop state-change on this prop; card authoring would enable a `prop:oc-clerks-board.physical-condition: open -> folded` entry at @68 in a subsequent revision pass |

Card class for all three: `prop`. These are props in the westerosi administrative scene — a sealed
letter, a parchment assessment ledger, and a clerk's writing board. Minimal card schema requirements
apply (class, slug, world, description, first-appearance episode, warehouse-presence note).

**This referral does not block Phase 5 shipping.** The `oc-*` extension is flagged per rubric; entries
are valid as authored. Card authoring is a margit task to be run at the next available slot before
canonical write-back.
