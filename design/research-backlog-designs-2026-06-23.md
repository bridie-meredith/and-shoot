# Research-backlog design specs — OOS / follow-on items (2026-06-23)

**Status:** Proposal-ready design specs. Each section is sized to become a `PROP-NNNN`
in `staff/admin/process-proposals.md` with minimal further work (problem → mechanism →
wire-in → finding/gate class → cost → dependencies).

**Scope.** These are the five OOS / follow-on items from `CLAUDE.md` "Not in scope" +
`design/substance/intent-gaps.md` items 5/7/8/10/11 that need a **design call**, not a
live project, to specify. None require a running book to design (they require a decision,
which is what this document produces). All five trace to original user feedback on the
pre-overhaul s01e01–s01e03 run (`design/substance/intent-gaps.md`), which is the evidence
base each problem statement cites.

**Authoring discipline note.** This document is design only. It does NOT modify any command
body, schema, or rubric. Wire-in points are named precisely so the build pass is mechanical.
Each spec picks ONE candidate mechanism and justifies the pick; rejected candidates are noted
so the proposal carries its own design rationale.

**Cross-cutting interaction with DEC-0115 (no-ledger / Rule 22).** Three of these five items
(length, emotional-substance, plot-arc) sit adjacent to the readability overhaul. DEC-0115
fixed *register* (prose renders concrete action, not bookkeeping) and added the **N=2
disposition circuit breaker**. None of the five below is subsumed by DEC-0115 — they address
*volume*, *axis-class coverage*, *arc completeness*, *world-detail*, and *name-novelty*,
which are orthogonal to register. Where a spec leans on the circuit-breaker pattern as
precedent, it says so.

---

## 1. Absolute-length floor mechanism

### (a) Problem statement
The user's headline length complaint on the pre-overhaul run was blunt and repeated: *"All
the episodes were too short"* and *"Way too short. What even was the point of this chapter?"*
(`intent-gaps.md` §"too short", citing s01e02/s01e03). The substance overhaul added bone-count
bands and per-scene density targets (`bones_per_scene: 5-15`), but density is a **ratio** —
a chapter can fully satisfy its substance contract in 800 words and still read as a "puff of
air." No surface in the current chain tracks **absolute volume**. The contract can be green
while the deliverable is a third of the length a reader expects from "a chapter."

### (b) Recommended mechanism
**Estimate at `/and-write` Phase 6 from a bones-count × words-per-bone projection, AND verify
the realized count at `/and-stitch` Phase 8.** Two-point check, not one.

- *Why both points, not just stitch:* a stitch-only floor catches the failure too late — after
  facets and a full render. Re-rendering is the most expensive remediation in the chain. The
  `/and-write` Phase 6 estimate (`projected_words = Σ bones × words_per_bone_estimate`, default
  `words_per_bone_estimate ≈ 45`, calibrated to shipped b01 drafts) catches an under-volume
  contract at the cheapest possible point — before any prose exists — and routes to
  `/and-write revise` to add scene-significant bones (NOT padding; the fix is *more substance*,
  consistent with the bones-first authoring principle in Rule 10).
- *Why also verify realized at stitch:* the estimate can be wrong (dense bones render long,
  sparse bones render short). Phase 8 is post-render, so it knows the true word count. It is the
  backstop.
- *Rejected — schema field only, verified at stitch:* loses the early-catch leverage; makes
  every short chapter a full re-render. *Rejected — pure derived (no explicit field):* the
  intent-gaps note suggested tying the floor to `chunk-count × per-chunk-bones × per-bone-word`
  so it "falls out of the schema," but an explicit declared floor is clearer for the audit and
  lets the principal tune per-series (a flash-fiction series and an epic want different floors).

### (c) Wire-in point
- **Schema:** `schemas/showrunner-memory.schema.md`, `series.structure.book_length` block (line
  78-81). Add two fields:
  - `chapter_word_count_floor: <int>` (default 3000)
  - `scene_word_count_floor: <int>` (default 1500)
  Authored at `/and-series` Phase 4 (structural commitments) alongside the existing
  `chapters_per_book` / `scenes_per_chapter` / `bones_per_scene`.
- **`/and-write` Phase 6** (substance bone-gate, `.claude/commands/and-write.md`): add a
  `LENGTH-PROJECTION-SHORT` check. Compute `projected_words` per scene and per chapter; compare
  to the floors. The estimate is informational-leaning at this stage (it's an estimate) — see (d).
- **`/and-stitch` Phase 8** (finalize, `.claude/commands/and-stitch.md`): add a
  `CHAPTER-BELOW-FLOOR` / `SCENE-BELOW-FLOOR` realized-count check on the finalized
  `draft/<book>-<chapter>.md`. This is the authoritative measurement.

### (d) Finding / gate class + disposition
- `/and-write` Phase 6 `LENGTH-PROJECTION-SHORT` → **SIGNAL** (it is an estimate; per the
  Rule-10 / URI-WRITE-SIGNAL-DISPOSITION pattern it must reach a disposition ∈
  {remediated, accepted} before emit, so it cannot be silently shipped — but it does not HARD-block,
  because the projection can be conservative).
- `/and-stitch` Phase 8 `CHAPTER-BELOW-FLOOR` → **SIGNAL → blocking-on-second-occurrence.**
  Default SIGNAL (one short chapter may be a deliberate hinge/interlude). But the disposition is
  governed by Rule 22's N=2 circuit breaker: a length-floor SIGNAL dispositioned "deliberately
  short / accepted-caveat" at most **N=2 consecutive** chapters; the (N+1)th auto-promotes to
  blocking → `/and-write revise`. This reuses the existing circuit-breaker machinery rather than
  inventing a new escalation path.
- `frame-coda` chapters (Phase 6 frame-coda exemption, `and-write.md:272`) are exempt from the
  floor — interludes are legitimately short.

### (e) Cost: **S**
Two schema fields + one estimate check at Phase 6 + one realized check at Phase 8. No new
dispatch (both checks are mechanical, computed by the command body / auditor). Calibrating
`words_per_bone_estimate` against shipped b01 drafts is a one-time read.

### (f) Dependencies / interactions
- **Rule 22 (DEC-0115 circuit breaker):** reuses the N=2 disposition counter for the stitch-side
  escalation. No new escalation machinery.
- **Rule 10 / URI-WRITE-SIGNAL-DISPOSITION:** the Phase 6 SIGNAL inherits the
  must-reach-disposition-before-emit discipline.
- **`/and-series` Phase 4:** new authoring step (set the floors). Cheap; one prompt-or-default.
- **Interaction with PROP-0052 (structural-sameness):** none direct, but both are "volume/shape"
  metrics computable from bones — they could share a single structural pre-scan dispatch if ever
  consolidated. Out of scope here.
- **OOS-noted as a follow-on by `plan-holes-2026-05-17.md` Hole E item 5** — this spec is the
  design pass that note deferred.

---

## 2. Emotional-substance orthogonality check

### (a) Problem statement
On s01e01 the protagonist returned from the dead after three days and the chapter produced
**zero emotional Δ** — the user flagged *"There should be some harsh feels with protagonist
coming back to life after 3 days"* (`intent-gaps.md` §"emotional-substance"). The substance
signature lists state axes and tags each with an optional `class: plot | emotional`
(`showrunner-memory.schema.md:104` — already present, explicitly labeled *"used by future
emotional-substance orthogonality check (OOS)"*). But nothing **requires** an emotional axis to
move when a plot-stakes event lands. A chapter can satisfy its entire contract on
wealth/community/capability axes through a death or a resurrection and never register a feeling.
The schema field exists; the enforcement does not.

### (b) Recommended mechanism
**Hybrid: a cheap structural span-check at `/and-substance chapter` Phase 5 (require per-chapter
Δ to span ≥2 axis classes when a stakes-event is present), backed by the existing audience
review — NOT a new audience fork.**

- *Why structural-first, audience-backstop:* candidate A (require ≥2 axis classes always) is too
  blunt — a quiet logistics chapter legitimately moves only plot axes. Candidate B (audience
  emotional-resonance fork at the bone-gate) is the most accurate but adds a dispatch and a new
  HARD on a taste call, which the project has been *retiring* (the entire `/and-facets` audience
  gate was killed under DEC-0116). The right shape is the **conditional structural rule**: the
  ≥2-axis-class requirement fires **only when the chapter contract contains a stakes-event**
  (death, return, betrayal, revelation — detectable from `scene_conflict.stakes_axis` +
  `chapter goal`). This is a contract-level mechanical check (does `axes_in_motion[]` include
  ≥1 axis with `class: emotional`?), computable without a fork.
- *Why this is the DEC-0116-aligned choice:* it moves the check **upstream to the contract**
  (where it's a mechanical enumeration) instead of downstream to a prose-quality taste fork. The
  contract either declares an emotional axis on a stakes-event chapter or it doesn't. This mirrors
  the existing THEMATIC-AXIS-UNDECLARED check at the same phase (`and-substance.md:253`), which
  already asks "does the contract declare the axis its goal is about?"
- *Rejected — pure candidate A (always ≥2 classes):* over-fires on logistics chapters.
  *Rejected — pure candidate B (new audience fork):* adds spend + a taste-HARD against the
  DEC-0116 direction of travel.

### (c) Wire-in point
- **`/and-substance chapter` Phase 5** auditor reviewer (`and-substance.md:253`, alongside the
  existing THEMATIC-AXIS-UNDECLARED check): add `STAKES-EVENT-EMOTIONALLY-UNDECLARED`. The auditor
  detects a stakes-event chapter (heuristic: `scene_conflict.stakes_axis` resolves to a
  high-consequence axis OR the chapter `goal` names a death/return/betrayal/revelation/loss) and
  verifies `axes_in_motion[]` (or `axes_held[]`) contains ≥1 axis whose `state_axes[].class ==
  emotional`.
- **Requires axis-class population:** `state_axes[].class` (schema:104) is currently *optional*.
  This spec promotes it to **required** at `/and-substance series` Phase 4 signature authoring (a
  one-time per-series tagging pass), so the check has data to read. The DENSE-matrix discipline
  already in place for `actor_baselines[]` is the precedent for "no cell left un-tagged."

### (d) Finding / gate class + disposition
- `STAKES-EVENT-EMOTIONALLY-UNDECLARED` → **HARD** at chapter-contract level (blocks persist,
  forces revise of the chapter chunk), matching the sibling THEMATIC-AXIS-UNDECLARED disposition
  at the same phase. Rationale: this is a contract under-declaration, not a prose taste call —
  the chapter is structurally about a feeling-bearing event and its contract is silent on
  feeling. Catching it at the contract is cheap and the fix (add the emotional axis to the
  contract, then let `/and-write` deliver it) is clean.
- Missing `class` tag on any axis → schema-validation **HARD** at `/and-substance series` Phase 4
  (cannot persist signature with untagged axes), parallel to the actor_baselines dense-matrix gate.

### (e) Cost: **S**
One auditor check at an existing phase (no new fork — folds into the Phase 5 auditor already
dispatched). One schema change (optional → required on `state_axes[].class`). One added authoring
step at `/and-substance series` Phase 4 (tag each axis's class).

### (f) Dependencies / interactions
- **`state_axes[].class`** (schema:104) — promotes from optional to required. This is the only
  schema mutation. Downstream readers that ignore the field today are unaffected.
- **THEMATIC-AXIS-UNDECLARED** (`and-substance.md:253`) — direct sibling; same phase, same
  reviewer, same HARD disposition. Build alongside it for consistency.
- **DEC-0116 (audience gate retired):** this spec is deliberately *not* an audience fork — it
  honors the "move taste calls to mechanical contract checks" direction.
- **`/and-write` Phase 6:** once the contract declares the emotional axis, the existing
  SUBSTANCE-FLAT-<axis> HARD already guarantees the bones *deliver* movement on it. So this spec
  only needs to fix the *contract*; delivery enforcement already exists. Clean composition.
- **OOS-noted as follow-on by `plan-holes-2026-05-17.md` Hole E item 7.**

---

## 3. Plot-arc-completion dramatist check

### (a) Problem statement
Twice the user asked the unanswerable question: *"What even was the point of this chapter?"* /
*"I'm not really sure what this chapter was supposed to do"* (`intent-gaps.md` §"plot-arc-
completion", s01e02/s01e03). The overhaul added `chapters[].dramatic_shape` (rising / climax /
falling / hinge) and a dramatist shape-check at `/and-substance chapter` Phase 5. But a
shape *tag* is a curve label, not a completeness guarantee. A chapter can be tagged "rising" and
still have no identifiable setup, no complication, and nothing changed by the end — the exact
"puff of air" the tag was meant to prevent. The chapter `goal` field ("what this chapter shows
the audience") names an *intent* but is not verified against an actual *arc*.

### (b) Recommended mechanism
**Add an explicit arc-completion check to the `/and-substance chapter` Phase 5 dramatist
reviewer: verify the chapter chunk exhibits an identifiable (1) setup beat, (2) complication
beat, (3) resolution-or-cliffhanger beat, and require the chunk to carry a one-line
`what_changed_by_end` field that names the net change.**

- *Why dramatist at the chunk layer, not a downstream check:* "what was the point" is a
  *structural* defect, diagnosable at the chunk (the dramatist already reads the chunk for shape
  at this phase). It is cheapest to catch before bones exist. The dramatist is the correct
  reviewer — this is its exact remit (structure, not prose or taste).
- *Why a stored `what_changed_by_end` field, not just a reviewer assertion:* forcing the chunk to
  *carry* the one-line answer makes the defect impossible to paper over — if the author cannot
  write the line, the chapter has no arc. It also gives `/and-stitch` Phase 9 cold-read and
  `/and-postop` a ground-truth statement to test the rendered chapter against ("does the prose
  actually deliver `what_changed_by_end`?"). This is the chunk-level analogue of the existing
  `goal` field, but answerable only *after* the arc is specified.
- *Rejected — fold into the existing shape-check with no new field:* leaves the answer implicit
  and un-auditable downstream. The stored line is the load-bearing part.

### (c) Wire-in point
- **Schema:** `schemas/showrunner-memory.schema.md`, `chapters[]` block. Add
  `what_changed_by_end: <one line>` (sibling to `goal` and `dramatic_shape`). Authored at
  `/and-substance chapter` Phase 4 alongside `dramatic_shape` + `goal` (`and-substance.md:234-236`).
- **`/and-substance chapter` Phase 5** dramatist reviewer (`and-substance.md:252`): extend the
  existing "Chapter dramatic-arc completion?" line (it is *named* there but not specified) into a
  concrete three-beat check + verification that `what_changed_by_end` is populated, non-trivial,
  and consistent with the chunk and the `goal`.
- **Downstream consumers (no build, just availability):** `/and-stitch` Phase 9 cold-read and
  `/and-postop` substance-delivery fork can read `what_changed_by_end` as the ground truth the
  rendered chapter must satisfy.

### (d) Finding / gate class + disposition
- `ARC-INCOMPLETE` (missing an identifiable setup / complication / resolution-or-cliffhanger
  beat) → **HARD** at chapter-chunk level (blocks persist, forces revise) — matches the existing
  Phase 5 dramatist HARD dispositions (handoff-mismatch, scenes-too-small).
- `WHAT-CHANGED-MISSING-OR-TRIVIAL` (field empty, or restates `goal` verbatim, or names no net
  change) → **HARD**. The field's whole value is that it cannot be faked; an empty/trivial value
  is the defect, not a SIGNAL.
- Both are dramatist + chunk-layer, consistent with keeping structural calls upstream and cheap.

### (e) Cost: **S**
One schema field + one authoring line at Phase 4 + extending an already-named (but
under-specified) check in the Phase 5 dramatist that already runs. No new dispatch.

### (f) Dependencies / interactions
- **`chapters[].dramatic_shape` / `goal`** (`and-substance.md:234-236`) — `what_changed_by_end`
  is a third sibling field; author all three together.
- **`/and-substance chapter` Phase 5 dramatist** already lists "Chapter dramatic-arc completion?"
  (`and-substance.md:252`) — this spec is the *specification* of that currently-vague line. Low
  risk: it tightens an existing intent rather than adding a new concern.
- **`/and-stitch` Phase 9 naive-follow (DEC-0115):** strong synergy. The naive-follow gate asks
  "can a naive reader say what physically happens?"; `what_changed_by_end` gives the cold-read a
  declared target to confirm the rendered prose delivers. Consider citing this synergy in the
  proposal — it strengthens an existing gate at zero extra cost.
- **OOS-noted as follow-on by `plan-holes-2026-05-17.md` Hole E item 8.**

---

## 4. World-detail consistency audit

### (a) Problem statement
On s01e01 the user flagged class/economic anachronism directly: *"The bowl is weird"* / *"Do
smallfolk have salt?"* (`intent-gaps.md` §"world-law / setting-detail"). This is finer than a
world-law (condition card) and coarser than a prop card: it asks whether a specific
object/resource *belongs in this setting for this class of character*. The current consistency
surface has no home for it — `/and-project` 1d finalizes world-law condition cards, and
`/and-review consistency` checks cross-level Δ sums and cross-chapter handoff, but neither asks
"does a Flea Bottom ward plausibly have salt." The result is setting-anachronism that no gate
catches.

### (b) Recommended mechanism
**Add a `--world-detail` axis to `/and-review consistency` that dispatches the auditor against
the bones/draft + location card + condition cards + relevant persona cards, checking whether the
per-line props/resources fit the setting at the class/economic level.**

- *Why `/and-review consistency` and not a `/and-write` Phase 5 inline check:* the failure is a
  *consistency* defect (object vs. setting-class), and `/and-review consistency` already owns the
  cross-reference machinery (it reads cards + chunks across a root). A `/and-write` Phase 5 inline
  check would need to re-load all the world cards on every chapter write — duplicating consistency's
  job and bloating the hot path. Making it an **opt-in axis** on the existing consistency review
  (run on demand or before a book) keeps it off the per-chapter critical path while still giving it
  a home.
- *Why an axis, not a separate subcommand:* it composes the same reviewers (auditor) over the same
  card+chunk corpus the consistency sweep already loads. A flag is the minimal surface.
- *Rejected — `/and-write` Phase 5 continuity step:* puts a card-heavy world-detail audit on every
  chapter write; the defect is rare enough and the audit broad enough that on-demand is correct.

### (c) Wire-in point
- **`/and-review consistency`** (`.claude/commands/and-review.md:180`): add a `--world-detail`
  flag. When set, the auditor reviewer additionally cross-references each concrete object/resource
  appearing in the in-scope bones/draft against (i) the location card's economic/class register,
  (ii) condition cards (world-law / scarcity facts), (iii) the persona cards of the characters
  handling the object (does this character's station plausibly possess/access this resource?).
- **No new schema.** Uses existing location / condition / persona cards (`cards/`).
- **Usage convention:** runs at the same cadence as `pipeline` — on demand, and recommended once
  before a book's first chapter and after world-card changes.

### (d) Finding / gate class + disposition
- `WORLD-DETAIL-ANACHRONISM` (object/resource implausible for setting-class) → **SIGNAL** by
  default. Rationale: world-detail plausibility is a *judgment* with legitimate authorial override
  (maybe this smallfolk character *did* scavenge salt, and that's a story point). A HARD would
  over-fire on intentional exceptions. SIGNAL surfaces it for the principal/author to confirm or
  fix. This matches `/and-review consistency`'s general posture (it flags; it is not a per-chapter
  ship gate).
- Promotable to HARD only if a future run shows authors routinely ignoring the SIGNAL (the
  standard SIGNAL→HARD promotion path, not assumed up front).

### (e) Cost: **M**
One flag + one added cross-reference pass inside the existing consistency auditor dispatch. The
"M" (vs "S") reflects that the world-detail cross-reference is genuinely more work than a field
check — the auditor must enumerate concrete objects across the in-scope prose and match each to
card-declared setting register, which is a non-trivial sweep. Still one dispatch (folds into the
consistency auditor fork), still off the per-chapter hot path.

### (f) Dependencies / interactions
- **Location / condition / persona cards** (`cards/`) — read-only inputs; no card schema change.
  Quality of the check depends on those cards declaring an economic/class register; if a location
  card is silent on class economics, the audit degrades to best-effort (note this in the proposal
  as a known limitation — it does not block the build).
- **`/and-review consistency`** existing reviewers (dramatist + auditor) — the new axis is
  auditor-only; dramatist is unaffected.
- **No interaction with the per-chapter chain** (opt-in, off hot path) — does not gate ship,
  consistent with consistency's role.
- **OOS-noted as follow-on by `plan-holes-2026-05-17.md` Hole E item 11.**

---

## 5. Name-novelty enforcement for original characters

### (a) Problem statement
Library persona slugs leak into downstream original-character naming. Observed: *"Mira"* was
used as an original Flea Bottom ward in `taylor-westeros-good-intentions` after appearing as the
library card `mira-stonefield` in projects 02/04/05 (`CLAUDE.md` "Not in scope" §name-novelty).
`CLAUDE.md` documents **three leak vectors**, all confirmed against the command bodies:
1. **`boundary-scope.md`** embeds library slugs in its archetype role menus (the boundary-scope
   fork at `/and-project` Phase 1.7 maps concept-space using library cards by archetype tag).
2. **`prompt-binding.md`** carries those archetype names forward (the binding sheet's archetype
   section, `and-project.md:277-305`, is consumed by every downstream phase).
3. **Naming forks** at `/and-project` 1b (cost-bearer / character naming OQs) and `/and-cast`
   cast composition (`and-cast.md` Phase 2-3 margit menu + screen-writer selection) are **not
   isolated** from `projects/` or library card names — an original character can be christened
   with the name of the library archetype exemplar it was modeled on.

The result: original characters inherit library/archive names, which reads as derivative and can
collide across projects.

### (b) Recommended mechanism
**Two-part: (1) strip library/archive *proper names* from `boundary-scope.md` and
`prompt-binding.md` before downstream consumption — pass archetype *tags*, never card *slugs/names*;
and (2) add a no-prior-name-reuse clause to the two naming forks (`/and-project` 1b naming OQs +
`/and-cast` margit/screen-writer composition), enforced by margit as a name-novelty gate against
a union of `cards/` + `projects/` proper names.**

- *Why both, not one:* vector (1) (strip names at the source artifacts) removes the *suggestion*
  — the downstream forks never see "Mira" as a primed exemplar name. Vector (2) (the novelty gate)
  is the *backstop* — even if a fork independently generates a colliding name, margit catches it.
  The leak has three vectors; a single fix at one vector leaves the other two open. Stripping
  (vectors 1+2 of the doc) is one mechanism; the novelty gate (vector 3) is the other. Together
  they close all three.
- *Why margit owns the gate:* margit is the card warehouse / catalog gatekeeper and already
  validates and indexes all cards — it is the single agent that *knows* every library + archive
  proper name. A name-novelty check is a natural extension of its existing validation remit (it
  already gates `/and-project` Phase 1c and `/and-cast` Phase 5 on exemplar presence).
- *Rejected — name-novelty in the screen-writer fork alone:* the screen-writer doesn't have the
  authoritative name index; margit does. *Rejected — strip-only (no gate):* leaves
  independently-generated collisions uncaught. *Rejected — gate-only (no strip):* leaves the
  forks primed by the leaked name, so the gate fights a current it could have removed.

### (c) Wire-in point
- **Vector 1 — strip at `boundary-scope.md`:** `/and-project` Phase 1.7
  (`and-project.md:213-224`). The boundary-scope fork's archetype role menus must present
  archetype **tags + structural descriptors**, NOT library card slugs/proper names. Add a
  fence to the fork brief: "Reference archetypes by role/tag only; never emit a library or
  archive card slug or character proper name into the menus."
- **Vector 2 — strip at `prompt-binding.md`:** `/and-project` Phase 1.9 write-the-binding-sheet
  step (`and-project.md:277-305`). The archetype section carries tags, not names. Same fence.
- **Vector 3 — novelty gate:** add a margit name-novelty check at (i) `/and-project` 1b naming
  OQ resolution (`and-project.md:376` Step 1b — when an OQ resolves a cost-bearer/character
  proper name) and (ii) `/and-cast` Phase 2-3 (margit candidate menu + screen-writer selection,
  `and-cast.md`). Margit validates each *proposed original-character proper name* against the
  union of proper names in `cards/personas/` + `cards/persona-exemplars/` + `projects/*/`. A
  collision (exact or close-variant, e.g. "Mira" vs "mira-stonefield") is flagged.
- **No new schema.** The name index is computed by margit at check time from existing dirs.

### (d) Finding / gate class + disposition
- `NAME-NOVELTY-COLLISION` (proposed original-character name matches a library/archive proper
  name, exact or close-variant) → **HARD** at the naming fork (margit refuses the name; the fork
  re-picks). Rationale: this is a cheap, unambiguous, mechanical check with a clear correct action
  (pick a different name) and no legitimate override for *original* characters — if a character is
  meant to *be* a library persona, it is provisioned from the card, not named to collide with one.
  HARD is safe because the remediation is trivial (re-pick) and self-contained (no re-cascade).
- Vector 1/2 stripping is a **fork-brief fence**, not a finding class — enforced by the
  NEVER-INLINE / surface-convention discipline already governing those forks; a leaked proper name
  in `boundary-scope.md` / `prompt-binding.md` is a fence violation caught at fork output review.
- **Scope fence:** the gate applies ONLY to *original* characters. Provisioning an actual library
  persona (a deliberate reuse, e.g. a recurring antagonist) is unaffected — that goes through
  `/and-cast --add <slug>` against the card, which is reuse-by-design, not a name collision.

### (e) Cost: **M**
Two fork-brief fences (vectors 1+2 — cheap, additive text) + one margit name-novelty check wired
at two call sites (`/and-project` 1b, `/and-cast` Phase 2-3). The "M" reflects the close-variant
matching (margit must do fuzzy name comparison against a union index across `cards/` + `projects/`,
not just exact-match) and the two-site wiring. No re-cascade, no new schema, no new dispatch
(folds into margit's existing validation calls at those phases).

### (f) Dependencies / interactions
- **Margit** (`staff/margit/`) — extends its existing validation remit; it already runs at
  `/and-project` Phase 1c and `/and-cast` Phase 5. New: a name-novelty check at the naming forks.
- **`/and-project` Phase 1.7 / 1.9 NEVER-INLINE + surface-convention fences** — the strip fences
  ride the existing isolation discipline (`and-project.md:213, 322`); consistent with the
  contamination-vector framing already in those phases.
- **`/and-cast --add <slug>`** — explicitly *out of scope* for the gate (deliberate library reuse);
  the proposal must state this fence clearly so the gate doesn't block legitimate persona reuse.
- **Interaction with the broader `name-novelty` OOS note in `CLAUDE.md`** — this spec implements
  all three candidate fixes the note sketched (strip boundary-scope, no-prior-name clause on
  `/and-cast` + `/and-project` 1b, margit name-novelty ownership), choosing to do all three
  because the three leak vectors are independent.
- **Known limitation to flag in the proposal:** close-variant matching is heuristic (how close is
  "too close"?). Start permissive (exact-match + obvious stem-match like "Mira"/"mira-stonefield")
  and tighten only on observed false-negatives.

---

## Appendix — proposal-readiness summary

| # | Item | Mechanism (1 line) | Primary wire-in | Class | Disp. | Cost |
|---|------|--------------------|-----------------|-------|-------|------|
| 1 | Absolute-length floor | Bones×words estimate at `/and-write` P6 + realized check at `/and-stitch` P8, against new `chapter_word_count_floor` | schema `book_length` + `/and-write` P6 + `/and-stitch` P8 | LENGTH-PROJECTION-SHORT / CHAPTER-BELOW-FLOOR | SIGNAL (P8 → blocking on N=2) | S |
| 2 | Emotional-substance orthogonality | Conditional ≥2-axis-class contract check when a stakes-event is present | `/and-substance chapter` P5 auditor; `state_axes[].class` → required | STAKES-EVENT-EMOTIONALLY-UNDECLARED | HARD | S |
| 3 | Plot-arc-completion | Dramatist verifies setup/complication/resolution beats + stored `what_changed_by_end` line | schema `chapters[]` + `/and-substance chapter` P4/P5 dramatist | ARC-INCOMPLETE / WHAT-CHANGED-MISSING | HARD | S |
| 4 | World-detail consistency | `--world-detail` axis on `/and-review consistency`, auditor cross-refs objects vs setting-class | `/and-review consistency` | WORLD-DETAIL-ANACHRONISM | SIGNAL | M |
| 5 | Name-novelty enforcement | Strip library names from boundary-scope/prompt-binding + margit name-novelty gate at naming forks | `/and-project` P1.7/P1.9 fences + margit gate at P1b/`/and-cast` P2-3 | NAME-NOVELTY-COLLISION | HARD | M |

All five are buildable without a live project. None is subsumed by DEC-0115 / Rule 22, though
items 1 and 2 deliberately reuse its circuit-breaker and contract-check patterns. Recommended
build order if batched: 2 and 3 first (both are small auditor/dramatist extensions at the same
`/and-substance chapter` Phase 5, share a schema-tagging discipline, and close the two
highest-signal user complaints — "no feels" and "what was the point"), then 1 (length), then 5
(name-novelty, two-site), then 4 (world-detail, the broadest sweep).
