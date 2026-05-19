---
audit:
  scope: series
  target: pipeline-adaptation — URI-SUBSTANCE-OVERHAUL landing check
  timestamp: 2026-05-19
  auditor-note: >
    This report covers adaptation gaps only — stale references, broken paths,
    and schema mismatches left over after the URI-SUBSTANCE-OVERHAUL (2026-05-17).
    It does not cover the five facet failures in b01c01. Classifications used:
    STRUCTURAL (stale references that should have been deleted or rewritten),
    CONSTRAINT (slug / path pointers that do not resolve),
    METADATA-INCONSISTENCY (frontmatter / schema mismatches),
    DEDUP (concept split across overhauled and un-overhauled surfaces),
    CONTRADICTION (post-overhaul rules contradicting pre-overhaul rules still in place).
    Severity: HARD = a live dispatch reading this surface is misled into pre-overhaul
    behavior; SIGNAL = archival residue that no live dispatch reads.
---

# Pipeline Adaptation Audit — URI-SUBSTANCE-OVERHAUL

---

## STRUCTURAL findings

### STRUCT-001 — HARD
**What:** `schemas/facet.schema.md` § tensometer section (lines 21–68). The section is
fully intact and authoritative-sounding, including "Boundary-carry ID exception
(tensometer only, URI-038)", "Dual provenance (URI-026)", "/and-shoot integration"
block that says "Phase 0 renames `facets/tensometer-<season-slug>e<NN>.md` →
`facets/tensometer.md` for current-episode work."

**Why:** The facet schema is the authoritative format reference for every agent that
authors or reads facet files. The tensometer section teaches agents that tensometer
is a live facet type with an authoring path. Under the overhaul, tensometer is
dropped from R1/R2 fanout. A fresh agent reading this schema before authoring or
reviewing facets concludes tensometer must exist. The section should be marked
DEPRECATED or removed.

**Criteria:** The tensometer section of `schemas/facet.schema.md` must be updated to
reflect that tensometer is dropped from the substance-overhaul chain; it may be
retained as historical reference but must not read as an active authoring target.

---

### STRUCT-002 — HARD
**What:** `schemas/facet.schema.md` § scene-map (lines 278–293). Scene-map is still
described as "Auto-derived at `/and-facets` Phase 4c from `tensometer` + `location-state`
+ `interest-narrator` + proto-lines. Not human-authored." This directly contradicts
the overhaul: scene-map is now emitted by `/and-write` Phase 7 and validated (not
derived) at Phase 4d.

**Why:** Any agent reading this schema to understand scene-map provenance will
believe it is derived at Phase 4c from tensometer. It will look for tensometer as
an input to scene-map derivation. This is wrong in two ways: (1) the derivation
step is gone, (2) tensometer is gone. The schema says "not human-authored" which is
now additionally misleading — it IS authored, by `/and-write` Phase 7.

**Criteria:** The scene-map entry in `schemas/facet.schema.md` must describe scene-map
as upstream-emitted by `/and-write` Phase 7 and validated at `/and-facets` Phase 4d;
tensometer must be removed as a derivation source.

---

### STRUCT-003 — HARD
**What:** `schemas/scene-map.schema.md` — the entire document. The authoring block
names `/and-facets` Phase 4c as the author. The derivation algorithm (step 4 in
particular) says "Read tensometer scene-footer; reconcile canonical labels (A, B, …)
against candidate boundaries. **The tensometer is the labelling authority** — its
named scenes win when candidate boundaries disagree on count." The per-scene
tens-aware fields (`rhythm-shape`, `peak-bones`, `peak-shadow-bones`,
`fusion-eligible-runs`, `protected-patterns`) are derived entirely from tensometer
per-bone entries. The field-derivation algorithm walks tensometer entries explicitly.
The file-structure section names `source: derived from tensometer + location-state
+ interest-narrator + proto-lines` in the required frontmatter.

**Why:** `schemas/scene-map.schema.md` is the schema authority for scene-map files
produced by `/and-write` Phase 7 under the overhaul. If the schema still specifies
tensometer as the scene-labelling authority, any agent authoring a scene-map (now
`/and-write` Phase 7) is directed to reference tensometer entries that do not exist.
The `fusion-eligible-runs` field — which drives stitcher fusion decisions — is defined
entirely in terms of tensometer scalars. The schema cannot guide compliant authoring
of the new scene-map shape.

**Criteria:** `schemas/scene-map.schema.md` must be rewritten to reflect `/and-write`
Phase 7 as the authoring agent, `substance_delta.axis_moves.magnitude` as the
pressure-signal source replacing tensometer, and all per-scene tensometer-derived
fields must be replaced with substance-delta-derived equivalents or removed. The
`fusion-eligible-runs` field definition specifically requires respecification.

---

### STRUCT-004 — HARD
**What:** `.claude/commands/and-facets.md` Phase 5 "Read inputs" block (line ~266):
"All ten facet files at `active-project/theater/facets/` (`tensometer`,
`location-state`, `interest-narrator`, `sensory`, `state-updates`, `memory`,
`feeling`, `metaphor`, `vibes`, `exposition-<slug>`)." Tensometer is listed as one
of ten facet files the auditor must load.

**Why:** The auditor dispatch at Phase 5 is explicitly told to load a tensometer file
that no longer exists. Under the overhaul, the R1 fanout drops tensometer, so no
tensometer file will be present. An auditor fork following this instruction will
either fail to find the file (HARD abort) or silently skip it (contaminating the
audit's completeness assumption). The CURVE-SHAPE audit class reads directly from
tensometer under the current spec; without tensometer, CURVE-SHAPE is undefined in
the command body.

**Criteria:** The Phase 5 read-inputs list must remove tensometer; the CURVE-SHAPE
audit class must be redefined in terms of substance-delta pressure-signal or removed
from the eleven audit classes.

---

### STRUCT-005 — HARD
**What:** `.claude/commands/and-facets.md` Phase 5b audience-gate master summary
template (line ~569): the per-facet aggregate listing explicitly includes
`tensometer: <accept | revise | fail>` as a facet in the audience-gate output table.

**Why:** The master summary template is the canonical output format that the
orchestrator-critic and showrunner read to determine gate status. Listing tensometer
as a gate-required facet means any run that does not produce a tensometer audience
verdict will appear to have an incomplete gate. A run under the overhaul will always
fail this line since tensometer is not authored.

**Criteria:** The Phase 5b per-facet aggregate table in the master summary must
remove the tensometer row; the table should list the nine facets that are actually
authored under the overhaul.

---

### STRUCT-006 — HARD
**What:** `.claude/commands/and-facets.md` Phase 6b master summary (line ~531):
"10 facet files authored (9 in parallel + tens upstream)" — the parenthetical
`+ tens upstream` names tensometer as an upstream input counted in the ten-file total.
Also: the R1 fanout section header says "R1 authors (nine in the parallel block)"
(line ~125) — nine is correct under the overhaul (tensometer dropped), but the
summary counts ten, which contradicts.

**Why:** This is an internal count contradiction in the command body. Line 125 correctly
says nine R1 authors. Line 531's summary template counts ten and attributes the tenth
to "tens upstream." A fresh run following this template will produce a summary claiming
ten facet files when only nine exist.

**Criteria:** Phase 6b summary template must use nine facet files total with no
tensometer parenthetical.

---

### STRUCT-007 — HARD
**What:** `.claude/commands/and-facets.md` Phase 4d validation (line ~253): "Validate
the tens-aware fields (`rhythm-shape`, `peak-bones`, `peak-shadow-bones`,
`fusion-eligible-runs`, `protected-patterns`) are populated per
`schemas/scene-map.schema.md` if the facet was emitted with them. Under the
substance overhaul these fields are derived from the per-bone
`substance_delta.axis_moves.magnitude` (treated as the new pressure-signal) instead
of tensometer entries; `/and-write` Phase 7 computes them at emit time."

**Why:** Phase 4d instructs the orchestrator to validate fields defined by the
pre-overhaul `schemas/scene-map.schema.md` which still specifies those fields in
terms of tensometer scalars (STRUCT-003 above). The validation instruction references
the schema as the authority but the schema is stale. An orchestrator following Phase 4d
will cross-check scene-map tens-aware fields against a schema whose definitions
conflict with the substance-delta-derived values that `/and-write` Phase 7 now emits.
STRUCT-003 must be fixed before Phase 4d validation can be coherent.

**Criteria:** Phase 4d must reference a corrected `schemas/scene-map.schema.md`; this
finding is derivative of STRUCT-003 and resolves when that schema is corrected.

---

### STRUCT-008 — HARD
**What:** `design/shoot-v2/rubric-memory-flags.md` — the entire "Author / reviewer notes"
block (lines ~276–285) instructs the memory-flag author to load "the locked tensometer
file (for inverted-tens-density check)". The §"Licensing-discipline" axis (ACCEPT
signatures) says "**Quiet-beat anchor.** The fire's anchor proto-line is at tens=1 OR
at the trailing edge of a tens=2." The §"Curve-shape rubric / Episode-level shape"
requires "**Inverted tens-density alignment.**" The cross-facet contract section
(lines ~236–251) specifies "**Tensometer (locked, upstream — inverted contract).**
Memory-flags fires concentrate in tens=1 zones and tens=2 trailing edges." The
cross-axis tests include "**The quiet-beat test.** Look up the beat's tensometer
rating." Anti-patterns AP-6 and AP-8 reference peak-fires (tens=3) and
density-on-flat (tens=1).

**Why:** This rubric is the operative instruction set for the memory-flag author and
the mechanic auditor. Every axis in the rubric assumes access to a tensometer file
that no longer exists. An author following this rubric has no substitute for the
quiet-beat-anchor check (tens=1/2/3 classification), which is the rubric's most
consequential gating criterion. Without tensometer, the author falls back on informal
surrogates (pile-up density, dramatic_shape declaration) — which is exactly what the
audience reviewers did in the b01c01 run (cape-fic-reader verdict: "without tensometer
this run, I use pile-up density as the functional marker"). The rubric must name the
substance-delta pressure-signal as the substitute for tens scalars, or the quiet-beat
gate is undefined.

**Criteria:** `design/shoot-v2/rubric-memory-flags.md` must replace all tensometer
references with substance-delta equivalents: `substance_delta.axis_moves.magnitude`
or scene-map `rhythm-shape` + `peak-bones` from the substance-delta-derived scene-map
as the pressure-signal substitute for tens=1/2/3 classification.

---

### STRUCT-009 — HARD
**What:** `design/shoot-v2/rubric-sensory.md` — "Author / reviewer notes" (line ~286):
"Author: studio writer-fork. Loads: [...] locked tensometer file (correlative
observation only — NOT gating)." The §"Cross-facet contract" section names
"**Tensometer (locked, upstream — correlative-not-gating).** Sensory-flags is
independent of tensometer." Anti-pattern #10: "Tens-gating misread. Author treats
high-tens beats as eligible / low-tens as ineligible." The calibration anchors
reference tens values (@24 sound:drop noted as "Tens=3 (correlative observation)";
@13 as "Tens=1 (correlative observation)").

**Why:** The tensometer reference in this rubric is non-gating by design, so the
impact is lower than in the memory rubric. However, the author instructions still
say to load a file that does not exist. The calibration anchors cite tens values
that cannot be verified without tensometer. A fresh author following this rubric
will note the missing file and proceed without it — which is the correct behavior
under the overhaul — but the rubric gives no substitute for the correlative
observation purpose. The scene-map `rhythm-shape` is the natural substitute; it is
not named here.

**Criteria:** `design/shoot-v2/rubric-sensory.md` must remove the tensometer load
instruction from Author notes and replace calibration anchor tens references with
scene-map `rhythm-shape` or `substance_delta` references.

---

### STRUCT-010 — HARD
**What:** `design/shoot-v2/rubric-state-updates.md` line ~8: "The rubric depends on
the locked tensometer file and the locked narrator-interest file for cross-facet
contract. It does NOT depend on [...] the open V3 rubric work for tensometer."
The §"Reality" ACCEPT signatures (line ~66): "Cross-facet honor: tensometer
@64-class beats (irreversible registration) almost always carry a state-update;
narrator-interest fires on actor:POV.knowledge.* shifts." The calibration example
(line ~66) names "@64 STATE-UPDATE NOTE" and "@39 STATE-UPDATE NOTE" as tensometer-
designated beat markers that the state-updates author must cross-reference.

**Why:** State-updates is one of the five facets that failed Phase 5b in b01c01.
The author instruction says to load a tensometer file that does not exist. The
calibration examples reference specific tensometer beat annotations (@39, @64) that
do not exist in a substance-overhaul run. An agent authoring state-updates cannot
perform the cross-facet honor check the rubric requires.

**Criteria:** `design/shoot-v2/rubric-state-updates.md` must replace tensometer
load instruction and @64/@39 tensometer beat references with substance-delta
equivalents (hinge beats per `dramatic_shape`, peak bones per scene-map
`peak-bones` field).

---

### STRUCT-011 — SIGNAL
**What:** `design/shoot-v2/rubric-narrator-interest.md` (first 60 lines read)
does not show tensometer references in those lines. However, the rubric's
structure and the audience reviewer behavior (worm-canon-pedant accepted the NI
file and mentioned foreknowledge-clamp channels) suggest tensometer may appear
in later sections of this rubric. Not confirmed as HARD without a full read;
logged as SIGNAL pending verification.

**Why:** If NI rubric references tensometer for the curve-shape check or the
tens-alignment behavior (NI aligns to peaks, inverse of memory-flags), the same
gap as STRUCT-008 applies.

**Criteria:** Verify remaining sections of `design/shoot-v2/rubric-narrator-interest.md`
for tensometer references; upgrade to HARD if found.

---

### STRUCT-012 — SIGNAL
**What:** `active-project/theater/facets/.r2-decisions.md` is located at
`active-project/theater/` (an output directory), not at `active-project/staff/`
(working memory). The file is 68KB per the audit brief.

**Why:** The `.r2-decisions.md` file is a cross-pipeline contract consumed by the
orchestrator-critic at Phase 6. Its placement in the output directory rather than
the working-memory directory makes it subject to accidental pruning (the command
body at Phase 6a says "`_inflight/` and `_inflight-r2/` may be retained for
forensic review or **pruned**"). A prune operation on the theater/ output directory
would delete the file the orchestrator-critic reads. This is a storage-class error,
not a content error.

**Criteria:** Flag for showrunner: the architectural home for `.r2-decisions.md`
is a decision that may need documentation; if theater/ is treated as purgeable
output and staff/ as durable working memory, the file may be at risk.

---

## CONSTRAINT findings

### CON-001 — HARD
**What:** `active-project/staff/showrunner/memory.md` § series.behaviors (line ~81):
lists `cond-cost-bearer-scene-frequency` as an active behavior constraint. The
actual warehouse file at `active-project/warehouse/cond-cost-bearer-scene-frequency.md`
exists and is correct (resolved to Wren). However, a second file also exists:
`active-project/warehouse/cond-nessa-scene-frequency.md` — a pre-resolution version
naming a different identity (Nessa, age 8) and not marked as superseded in
showrunner memory.

**Why:** The `cond-nessa-scene-frequency.md` file is a prior draft of the cost-bearer
constraint with a different character identity. The `cond-cost-bearer-scene-frequency.md`
card has a `supersedes: cond-nessa-scene-frequency` frontmatter field, but showrunner
memory does not record the supersession. Any pipeline that scans the warehouse for
condition cards governing cost-bearer behavior will find both cards and may apply both.
The two cards describe contradictory cost-bearer identities: Nessa (female, age 8,
original name) vs. Wren (stitch-maker's ward, age 11, resolved identity). An agent
loading both cards cannot determine which is canonical.

**Criteria:** `cond-nessa-scene-frequency.md` must be removed from the active warehouse
or marked as superseded with a pointer to the canonical card; showrunner memory must
record the supersession explicitly.

---

### CON-002 — SIGNAL
**What:** `active-project/warehouse/cond-khepri-residue-122ac.md` slug embeds the
Earth-Bet proper noun "khepri" in its slug. The r2-verify audit logged this as a
NOTE-FOR-NEXT-RUN. The card content itself is correct (does not violate prose fences);
the slug-surface violation is in the file name and the warehouse index, not the prose.

**Why:** The earth-bet-hard-fence scan in the Phase 5 auditor (`and-facets.md`
§CONSTRAINT class) explicitly states: "Slug components matter: a margit-referral
slug embedding `khepri-` or `gold-morning-` is a hard-fence violation even when no
full English phrase is rendered." The card slug `cond-khepri-residue-122ac` embeds
`khepri-`, which the scan would flag as HARD. The card is referenced in
`series.laws` in showrunner memory, so it is in active use. Every agent that loads
this card by slug — including every Phase 5 auditor that scans the warehouse — will
encounter the flagged slug. Per the rubric, the scan hits on slug components; this
is classified as HARD at Phase 5.

**Criteria:** The card must be renamed to a mechanism-descriptive slug (e.g.,
`cond-override-architecture-residue-122ac` or `cond-power-state-122ac`) and all
references in showrunner memory, actor cards, and cross-references must be updated.

---

### CON-003 — HARD
**What:** `.claude/commands/and-facets.md` Phase 6c (line ~590): "Read
`staff/audience/and-facets-orchestrator-critic/card.md`." This path resolves:
the file exists at `/home/user/and-shoot/staff/audience/and-facets-orchestrator-critic/card.md`.
No broken path here. Marking PASS on this specific check.

**Note:** Path resolves correctly. No finding.

---

### CON-004 — HARD
**What:** The audience-gate command body (Phase 5b) instructs the orchestrator to
look for specialist personas by checking for `target-facet: <facet>` in frontmatter
at `staff/audience/<slug>/card.md`. Three sensory specialists exist
(`sensory-disambiguation-pedant`, `sensory-modality-coverage`,
`sensory-old-state-reader`) — confirmed present. No specialists exist for memory,
interest-narrator, location-state, or state-updates.

The five facets that failed Phase 5b in b01c01 (memory, interest-narrator,
location-state, state-updates, sensory) thus ran with:
- sensory: specialists available and should have fired
- memory, interest-narrator, location-state, state-updates: active-project
  audience as fallback (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant)

This is not a CONSTRAINT failure (the command correctly falls back). However,
the sensory specialists may not have fired — the sensory audience verdict files
(`sensory-r1-verdict.md` under any of the three active-audience slugs) do not exist,
suggesting sensory ran without any reviewer dispatches completing. If sensory
specialists exist but no verdict files exist for sensory, the gate is incomplete.

**Why:** If sensory specialists (`sensory-disambiguation-pedant` et al.) were not
dispatched in the b01c01 Phase 5b run, the facet either ran unmanned or the
specialist path was not followed. An incomplete gate means the facet's Phase 5b
result is not a valid ACCEPT or FAIL — it is absent.

**Criteria:** Verify whether sensory received any Phase 5b reviewer dispatches in
the b01c01 run; if no verdict files exist, sensory audience-gate did not complete
and must re-run before Phase 6 can proceed.

---

## METADATA-INCONSISTENCY findings

### META-001 — HARD
**What:** `schemas/facet.schema.md` § scene-map frontmatter spec (lines ~44–50):
the required frontmatter includes `source: derived from tensometer + location-state
+ interest-narrator + proto-lines` and `auto-derived: true`. Any scene-map file
emitted by `/and-write` Phase 7 under the overhaul must use this frontmatter, but
the `source:` value will be factually wrong (tensometer is not a source).

**Why:** The scene-map frontmatter is the metadata the orchestrator-critic and
downstream consumers (stitcher Phase 0.5) read to understand the file's provenance.
If the schema requires a source field naming tensometer, and the actual file is
derived from substance-delta data, the frontmatter will either (a) be wrong if
authored to spec or (b) conflict with the schema if correctly reflecting the actual
sources. Both outcomes are metadata failures.

**Criteria:** Resolves with STRUCT-003 (schema correction); the source field must
reflect actual derivation inputs.

---

### META-002 — SIGNAL
**What:** `staff/audience/INDEX.md` says "19 personas available." The audit brief
says "22 personas." The actual count of persona card directories confirms 19 (5 full
personas + 14 stubs + taste-judge). The INDEX count and the brief's count disagree.

**Why:** This is a minor documentation inconsistency in the INDEX. No live dispatch
reads the INDEX count as an authoritative gate; the discrepancy does not affect
pipeline behavior. However, if the INDEX is used to verify library completeness,
the count is wrong.

**Criteria:** Advisory only. Update INDEX count if the library has been extended
beyond what INDEX records.

---

### META-003 — SIGNAL
**What:** `active-project/audience/cape-fic-reader/card.md` frontmatter retains
`scope: library` (not `scope: project`). The library master at
`staff/audience/cape-fic-reader/card.md` also says `scope: library`. Both the
working copy and the library master have `scope: library`. The same is true for
`dark-fantasy-reader` and `worm-canon-pedant` active copies.

**Why:** If `scope: project` is the intended value for active-project working copies
(to distinguish them from the library originals), all three active copies are
mislabeled. This is a low-stakes inconsistency — no live dispatch gates on the scope
field. However, it means there is no programmatic way to distinguish a library card
from an active project copy using the frontmatter alone.

**Criteria:** Advisory only. Determine whether active-project audience copies should
carry `scope: project`; update if the distinction matters to any downstream consumer.

---

## DEDUP findings

### DEDUP-001 — HARD
**What:** The concept of "pressure signal" — the thing that tells a facet author
whether a given beat is high-charge or low-charge — is now split across two
incompatible surfaces:
1. **Pre-overhaul surface (still operative):** tensometer per-bone scalar (1/2/3)
   as described in `rubric-memory-flags.md`, `rubric-sensory.md`,
   `rubric-state-updates.md`, `schemas/scene-map.schema.md`.
2. **Post-overhaul surface (operative under new chain):** `substance_delta.axis_moves.magnitude`
   in showrunner memory, plus scene-map `rhythm-shape` + `peak-bones` fields as emitted
   by `/and-write` Phase 7.

The `.claude/commands/and-facets.md` mentions the substance-delta substitute in
several Phase 1 author instructions ("per-chapter `substance_delta` from showrunner
memory (pressure-signal substitute)") but the rubrics the authors actually load
(`rubric-memory-flags.md`, etc.) do not describe how to interpret substance-delta
as a pressure-signal substitute.

**Why:** A memory-flag author dispatched under the overhaul reads Phase 1 in the
command body and sees "use substance_delta as pressure-signal substitute." They then
load `rubric-memory-flags.md` and find a fully articulated gating system in terms
of tens=1/2/3. These two surfaces are not bridged — there is no translation table
from substance-delta magnitude to the equivalent of tens=1/2/3. The author must
improvise the bridge, which is what happened in b01c01 (reviewers fell back on
pile-up density as a surrogate).

**Criteria:** A single authoritative translation must be established and placed in
one of: (a) the rubrics themselves (replace tens language with substance-delta language),
(b) a new bridging document that both the command body and the rubrics reference, or
(c) the scene-map schema (so the scene-map's substance-delta-derived `rhythm-shape`
and `peak-bones` fields become the canonical pressure-signal read surface for all
rubrics). Option (c) is highest-leverage because it is already the intended
downstream surface; the rubrics need only cite scene-map fields instead of tensometer
entries.

---

### DEDUP-002 — HARD
**What:** The concept of "quiet-beat" — whether a beat is eligible for a memory-flag
fire — is defined in `rubric-memory-flags.md` as "tens=1 OR trailing edge of tens=2"
and enforced via the quiet-beat cross-axis test ("Look up the beat's tensometer
rating"). The scene-map schema (STRUCT-003) defines `rhythm-shape` values that
directly encode the same concept (`flat-low`, `rising`, `resolving`, etc.). These
two definitions are parallel but unconnected.

**Why:** A downstream memory-flag R2 judge or mechanic auditor following the rubric
has no way to derive quiet-beat classification from the substance-delta-derived
scene-map. They must look up a tensometer file that does not exist. The scene-map
fields are the intended replacement surface but the bridge is not made explicit.

**Criteria:** Resolves with DEDUP-001 and STRUCT-008 together — once rubric-memory-flags
names the scene-map's `rhythm-shape` field as the quiet-beat classification authority,
the duplication is resolved.

---

### DEDUP-003 — SIGNAL
**What:** The auditor's CURVE-SHAPE audit class in Phase 5 of and-facets.md is
defined as checking "tens-rubric § 'Curve-shape rubric (episode-level)'". The
memory-flags rubric has its own curve-shape rubric section that requires "inverted
tens-density alignment" checked against tensometer. The `staff/orchestrator-critic/card.md`
Category B6 also references the shared CURVE-SHAPE class. Three surfaces define
or consume CURVE-SHAPE and all are in terms of tensometer.

**Why:** The CURVE-SHAPE class is the shared reviewer resource referenced in
CLAUDE.md Rule 11 ("The audience persona cards' `Threshold Discipline` body sections
and the auditor class library (`CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND`
definitions in `.claude/commands/and-facets.md`) are the canonical shared surfaces").
CURVE-SHAPE is not yet defined in substance-delta terms anywhere. The class exists
across three surfaces but is nowhere translated.

**Criteria:** The CURVE-SHAPE definition in `.claude/commands/and-facets.md` Phase 5
must be translated to substance-delta terms. The memory-flags rubric's curve-shape
section is a STRUCT-008 concern; this finding tracks the cross-surface duplication.

---

## CONTRADICTION findings

### CONTRA-001 — HARD
**What:** `.claude/commands/and-facets.md` Phase 1 author instructions state for
each facet: "Tens reads are dropped under the substance overhaul; where
pressure-signal is needed, the per-chapter `substance_delta` from showrunner memory
is the substitute." But `rubric-memory-flags.md`, `rubric-sensory.md`, and
`rubric-state-updates.md` — the rubrics each author is also instructed to load —
contain no corresponding statement that tens reads are dropped and no guidance on
using substance_delta as a substitute.

**Why:** This is a direct instruction contradiction. The command body tells authors
to drop tens reads. The rubrics tell authors to load and use the tensometer file.
A conscientious agent following both will find it impossible to satisfy both
instructions simultaneously. The b01c01 run demonstrates the result: audience
reviewers explicitly noted "without tensometer this run" as an improvised
accommodation, not a documented substitute path. The contradiction is the root cause
of the audience callouts citing "inverted tens-density alignment" and "tens=1 quiet
beat" in their verdicts — the reviewers had no substitute rubric to apply.

**Criteria:** The rubrics and the command body must converge on a single description
of what the pressure-signal surface is under the overhaul. Either the rubrics are
updated (resolves STRUCT-008, STRUCT-009, STRUCT-010) or the command body is changed
to name specific rubric sections that provide substance-delta guidance.

---

### CONTRA-002 — HARD
**What:** `schemas/facet.schema.md` § scene-map description says "Auto-derived at
`/and-facets` Phase 4c." `.claude/commands/and-facets.md` Phase 4d says "Under the
substance overhaul, `/and-write` Phase 7 emits the scene-map facet directly from
`chapters[].scenes[]` in showrunner memory. Phase 4d **no longer derives** — it
validates." These two statements are directly contradictory about who authors the
scene-map and when.

**Why:** Any agent reading both the schema and the command body to understand scene-map
provenance receives contradictory answers. The schema wins on authority (schemas/
is the schema authority), which means the schema actively misdirects.

**Criteria:** Resolves with STRUCT-002 (schema must be updated to match command body).

---

### CONTRA-003 — HARD
**What:** `schemas/scene-map.schema.md` § "What this schema does not cover" (lines
~166–169): "**Authored override.** The scene-map is purely derived. Human override
of a scene boundary requires editing the underlying tensometer/loc-state/NI source
and re-running Phase 4c. No direct edits to the scene-map file (any such edit would
be overwritten on next `/and-facets` run)." Under the overhaul, the scene-map is
authored by `/and-write` Phase 7 from substance-delta data; Phase 4c derivation is
gone; `/and-facets` Phase 4d only validates.

**Why:** The override path described in this section is completely wrong under the
overhaul. An agent attempting to correct a scene-map boundary would be directed to
edit tensometer or loc-state and re-run Phase 4c — neither of which is the correct
action. The correct action is to revise `/and-write` output or the substance contract
in showrunner memory.

**Criteria:** Resolves with STRUCT-003 (full schema rewrite).

---

### CONTRA-004 — SIGNAL
**What:** `staff/orchestrator-critic/card.md` Category B6 (line ~117): "Shared-reviewer
accounting: the mechanic-arithmetic auditor invoked at Step 2 cited the class
definitions from `.claude/commands/and-facets-audit.md` (FREQUENCY-BAND / CURVE-SHAPE
/ AP-SCAN tens-subset). No /and-season-specific rubric reimplementation." This
references `/and-facets-audit.md` as the canonical class library location — but
the current command is `.claude/commands/and-facets.md` (the combined command under
the overhaul; the separate `-audit` command was folded into Phase 5 of the unified
command). The path `and-facets-audit.md` may not exist.

**Why:** The orchestrator-critic card was authored in the pre-unified command era
and references the pre-overhaul file path. If `and-facets-audit.md` does not exist
as a separate file, this path is a broken reference that the orchestrator-critic
card asks agents to load.

**Criteria:** Verify whether `.claude/commands/and-facets-audit.md` exists as a
separate file; if not, update `staff/orchestrator-critic/card.md` B6 to reference
the correct file path (`.claude/commands/and-facets.md` Phase 5 audit classes).

---

## Summary of severity counts

```
STRUCTURAL:  HARD=7  SIGNAL=2
CONSTRAINT:  HARD=2  SIGNAL=1  (CON-003 resolved as pass; CON-004 needs verification)
METADATA:    HARD=1  SIGNAL=2
DEDUP:       HARD=2  SIGNAL=1
CONTRADICTION: HARD=3  SIGNAL=1
---
Total HARD:   15 (14 confirmed, 1 pending verification at CON-004)
Total SIGNAL:  7
```
