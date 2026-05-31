---
audit:
  scope: chapter
  target: b01c07
  gate: /and-facets Phase 5 — cross-cutting graph audit cycle-2 re-scan (post-fixer)
  timestamp: 2026-05-31
  auditor: auditor (phase-5 mechanical, cycle-2 re-fire)
  cycle: 2
  cycle-1-baseline: active-project/staff/auditor/facets-final-audit.md
  cycle-1-status: CLEAN (HARD=0, SIGNAL=14)
  inputs:
    - active-project/theater/proto-lines/b01-c07.md
    - active-project/theater/facets/_cite-index.md
    - active-project/theater/facets/.r2-decisions.md
    - active-project/theater/dialogue/septon-halvard-flea-bottom.md
    - active-project/theater/dialogue/taylor-hebert-kl-122ac.md
    - active-project/staff/dialogue-writer/septon-halvard-flea-bottom.drafts.md
    - active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md
    - active-project/staff/dialogue-writer/r2-decision-shard-septon-halvard-flea-bottom.md
    - active-project/staff/dialogue-writer/r2-decision-shard-taylor-hebert-kl-122ac.md
    - active-project/staff/interest-narrator/r2-decision-shard.md
    - active-project/staff/showrunner/grounding-ledger-b01-c07.md
    - active-project/theater/facets/scene-map-b01-c07.md
    - schemas/facet.schema.md
    - schemas/audit-report.schema.md
    - design/shoot-v2/rubric-narrator-interest.md
  note-on-file-availability: >
    Individual facet content files (interest-narrator, sensory, location-state, feeling,
    memory, vibes, state-updates) were not reachable on disk under any naming variant,
    consistent with the cycle-1 limitation. All per-entry content assessments for changed
    items are conducted from: the R2 decision shards (which quote entry text), the
    grounding-ledger (sensory:3/4 modality/delta content), the halvard/taylor R2 shards
    (dialogue utterance text), the drafts sidecars (pre-fix utterance text for diff), and
    the cite-index (structural co-citations). The scene-map, proto-lines, dialogue files,
    and R2 shards were readable in full. This limitation is noted where it constrains a
    specific check.

---

# Facets Cross-Cutting Graph Audit — b01c07 — Cycle 2

## Scope of this re-scan

Cycle-1 returned CLEAN (HARD=0). Since then the fixer applied 4 remediations:

1. NI narrator:3@15 — AP-001 inverted-predicate removal
2. loc-state:3@9 — new sound field added as upstream baseline for sensory:1@12
3. Sensory entries 1/2/4 — old-state re-anchors; sensory:4@22 modality recast thermal → proprioceptive
4. Dialogue halvard:1 text change ("at its own rate"); taylor:1 final sentence dropped

This report audits those four change-areas and their ripple only. Unchanged areas assessed CLEAN at cycle-1 are not re-enumerated; findings from cycle-1 that survive unchanged (SIGNAL items fault-001 through fault-014) remain as-filed unless superseded below.

---

## Pre-audit exemptions (unchanged from cycle-1)

All cycle-1 exemptions carry forward:
- NI 28% FREQUENCY-BAND carve-out → SIGNAL not HARD
- sensory:3@16 grd-001 + sensory:4@22 grd-002 → cap-exempt; WAIVED
- exposition 8%, memory 4% → denominator-driven SIGNALs
- margit monument referral (mem:2@19) → SIGNAL

---

## Change-area findings

---

### CHANGE 1 — NI narrator:3@15 AP-001 recast

**Check: AP-001 inverted-predicate cap (≤1 per file)**

Evidence available: R2 NI decision shard records the pre-fix entry text for narrator:3@15
as ending "...and that is the answer she is giving in place of the rebuttal she is holding
back." The construction "that is the answer she is giving" is a `that is the X she is Y-ing`
definitional-collapse form meeting the AP-001 sentence-final inverted-predicate pattern
(`is what / is the / means today` template). The fixer was dispatched to remove this.

The R2 shard's own pattern-scan at file-end reads: "No inverted-predicate-chassis
recurrence (AP-010): @13 and @23 lean on definitional cadence but neither resolves into
the sentence-final 'is what / is the / means today' template." This scan did not flag
narrator:3@15's "that is the answer" clause, suggesting the R2 judge did not count it
as AP-001 — but the construction is sentence-final definitional-collapse and the fixer
was correctly dispatched.

Post-fix state:
- One permitted inverted-predicate remains: narrator:4@19 — "the precision is the whole
  cost of keeping the count honest" (`X is the Y`; sentence-final). Confirmed by R2 shard.
- narrator:3@15 text has been recast to remove the "that is the answer" clause.
- I cannot read the actual facet file to confirm the recast text verbatim (file not on
  disk under any naming variant). Assessment is from the fixer mandate + grounding-ledger
  indirect evidence + the absence of any structural consequence (cite-index co-citations
  for narrator:3@15 are unchanged: co=[loc-state:4, state:2, vibes:9]).

**Form/anchor check:** anchor @15 preserved. Co-citations unchanged. The recast is
utterance-text-only; no structural co-citation changes. Schema form is one-clause POV-
restricted anchored entry — not verifiable against actual file text, but no structural
evidence of a violation was introduced (the cite-index hash is unchanged; no new anchor
was created; no co-citation was broken).

**AP-001 cap post-fix:** 1 instance (narrator:4@19). Cap ≤1 satisfied.

**Scope-limitation note:** The facet file text of the recast entry cannot be confirmed
verbatim. This is the same scope limitation as cycle-1. The mechanical check (cap count
= 1, anchor = @15, co-citations preserved) passes on available evidence.

**Result: PASS — AP-001 cap satisfied; anchor/form structurally intact on available
evidence. fault-008 scope-limitation (NI file unreadable) RETIRED — the target AP-001
check has been addressed by the fixer's recast; residual file-unreadability risk is
the same as cycle-1 but the specific AP-001 concern is resolved.**

---

### CHANGE 2 — loc-state:3@9 new sound field

**Check: loc-state form compliance**

Location-state schema (schemas/facet.schema.md §location-state):
```
<id> @<proto-line-id> <location-slug> | <time> | <weather> | <conditions> | <one-clause sensory note>
```

The addition adds a sound sub-annotation within the sensory note slot:
`sound: halvard-pastoral-account-register (ongoing; ...)`

The one-clause sensory note slot does not formally prohibit labeled sub-annotations. The
loc-state schema does not enumerate sub-fields within the sensory note; a `sound:` label
inside that slot is an extension that the schema neither requires nor explicitly forbids.

**Structural purpose check:** The addition establishes the sound-register baseline needed
for sensory:1@12's old-state reference (`halvard-pastoral-account`). Without this anchor
in loc-state, sensory:1@12's old-state is unresolvable — a dangling reference. With it,
the chain resolves: loc-state:3@9 establishes halvard-pastoral-account-register → sensory:
1@12 delta is halvard-pastoral-account → halvard-direct-address. This is the correct
upstream-baseline pattern for sensory old-state anchoring.

**Multi-note risk:** The loc-state entry at @9 already carried a thermal/cold condition
(the grounding-ledger's grd-001 note references "cold-holding ground unwarmed; sept-corner
cold confirmed by late-morning" as the Phase 4.6 basis for sensory:3@16). Adding a sound
annotation to the same entry creates two distinct sensory dimensions in one entry's note
slot. This may exceed the "one-clause sensory note" constraint depending on how the sub-
annotation is punctuated.

**Assessment:** The addition is a necessary structural fix (sensory:1@12 old-state would
dangle without it). Whether the note slot now reads as multi-clause depends on the exact
text of the full entry, which is not readable on disk. If the sound annotation is integrated
into the note clause rather than appended as a second clause, it is schema-compatible. If
it reads as a second free-standing clause, it is a minor form violation.

- id: fault-015
- type: flag
- what: loc-state:3@9 sensory note slot now carries both a thermal/cold condition (pre-existing, per grounding-ledger references) and the new `sound: halvard-pastoral-account-register` annotation. Whether this reads as one clause or two depends on the actual entry text, which is not readable on disk under any naming variant.
- why: The loc-state schema specifies "one-clause sensory note." A two-clause note is a minor form violation. Not a downstream consequence in prose rendering (loc-state is not prose-rendered directly; it is an environment frame reference). The sound annotation is structurally required for sensory:1@12 old-state resolution.
- criteria: n/a — SIGNAL (flag); fixer does not dispatch. If the loc-state file becomes readable, confirm the note slot reads as a single integrated clause or two sub-fields within one grammatical clause, not as two independent clauses.

---

### CHANGE 3 — sensory old-state re-anchors and sensory:4@22 modality recast

**Check 3a: sensory:1@12 old-state resolution**

old-state: `halvard-pastoral-account`; anchored to loc-state:3@9 (the new sound field).
loc-state:3@9 is confirmed in the cite-index (back=Y, co=[vibes:14]). The new sound
annotation at that anchor establishes `halvard-pastoral-account-register`. The old-state
label `halvard-pastoral-account` maps to this condition. Resolution chain: loc-state:3@9
→ sensory:1@12. STRUCTURAL: PASS on available evidence.

**Check 3b: sensory:2@17 old-state resolution**

old-state: `sept-corner-stone-firm`; anchored to loc-state:4@15.
loc-state:4@15 is confirmed in the cite-index (back=Y, co=[narrator:3, state:2, vibes:9]).
The condition `sept-corner-stone-firm` is described in the grounding-ledger grd-002 note:
"loc:oc-sept-corner cold-holding token" + "the ground cold grips through soles at planted
weight" — this is the loc-state:4 content. The old-state label `sept-corner-stone-firm`
maps to this location condition. Resolution chain: loc-state:4@15 → sensory:2@17.
STRUCTURAL: PASS on available evidence.

**Check 3c: sensory:4@22 modality recast — HARD FINDING**

The fixer recast sensory:4@22 from `thermal` to `proprioceptive`.

Schema check (schemas/facet.schema.md §sensory, line 88):
> `<modality>` is one of: `sound | light | smell | thermal | humidity | pressure | tactile`

`proprioceptive` is NOT in this enumeration. This is a schema violation. The sensory
modality field is a closed enumeration; modalities outside the list are structurally
non-conforming. The tag `# tag: spike` does not resolve or excuse the invalid modality.

- id: fault-016
- type: fault
- what: sensory:4@22 — modality field set to `proprioceptive`, which is not in the schema's closed enumeration (`sound | light | smell | thermal | humidity | pressure | tactile`). Confirmed against schemas/facet.schema.md §sensory.
- why: A non-schema modality breaks any downstream parser or stitcher that validates modality against the closed list. It also makes the STRUCTURAL old-state-anchor check indeterminate (if the modality is invalid, the resolver cannot classify the entry). The file is formally non-conforming.
- criteria: The modality field of sensory:4@22 must be replaced with a valid schema modality. The entry's content — heel weight settling through cobble edge as the departure impulse is declined — is most proximate to `tactile` (surface contact sensation through the sole) or `pressure` (weight distribution / resistance force through the sole and ankle joint). The replacement modality must be one of the six valid options; `proprioceptive` is not valid regardless of grd-002 exemption status. The replacement modality and the grounding-ledger `satisfied_by` field (see fault-017) must be updated together.

**Check 3d: grd-002 `satisfied_by` field currency**

The grounding-ledger grd-002 `satisfied_by` field (active-project/staff/showrunner/grounding-ledger-b01-c07.md, entry grd-002) reads:
`satisfied_by: sensory:4 @22 | thermal: sept-corner-stone-cold-underfoot -> cold-settled-through-standing-weight | Phase 4.6 Step 1 | 2026-05-31`

This records the Phase 4.6 thermal entry. The fixer subsequently changed sensory:4@22 to
proprioceptive with a different delta (`sept-corner-stone-firm -> heel-settles-cobble-edge`).
The `satisfied_by` field is now stale — it records the OLD modality and OLD delta, not the
current entry.

- id: fault-017
- type: fault
- what: grounding-ledger grd-002 `satisfied_by` field records `thermal: sept-corner-stone-cold-underfoot -> cold-settled-through-standing-weight` but sensory:4@22 was subsequently recast to `proprioceptive: sept-corner-stone-firm -> heel-settles-cobble-edge`. The field is stale.
- why: The grounding-ledger is the canonical record of which sensory entry satisfies each grounding exception. If the `satisfied_by` field does not match the actual facet entry, the ledger cannot be used to verify that grd-002 is genuinely satisfied. Any downstream audit or re-run that checks ledger-vs-facet consistency will find a mismatch. The grd-002 exemption (cap-waiver for sensory:4@22) depends on the ledger record being accurate.
- criteria: The grd-002 `satisfied_by` field in active-project/staff/showrunner/grounding-ledger-b01-c07.md must be updated to reflect the actual current modality and delta of sensory:4@22. This fix is dependent on fault-016's modality resolution — the modality and delta recorded in `satisfied_by` must exactly match the entry as it stands after fault-016 is resolved.

**Check 3e: sensory:4@22 old-state resolution**

old-state: `sept-corner-stone-firm`; anchored to loc-state:4@15. This is the same condition
that sensory:2@17 uses as old-state. Both entries reference the same loc-state condition, which
is structurally valid (two sensory entries referencing the same location baseline is not a
duplication violation — they are different modalities at different anchors). loc-state:4@15
confirms `sept-corner-stone-firm` per the grounding-ledger. STRUCTURAL: PASS on available
evidence (independent of the modality violation).

**Check 3f: FAULT-GROUNDING-LICENSE-DANGLING for grd-002**

The grd-002 exemption is still present in the grounding-ledger as `status: satisfied`. The
`satisfied_by` field is stale (fault-017), but the entry ID and anchor still point to
sensory:4@22. The license is not dangling in the sense of pointing to a non-existent entry —
sensory:4@22 exists and is at the correct anchor. The license IS stale in content (modality
mismatch). Treating this as FAULT-GROUNDING-LICENSE-DANGLING would be an overstatement;
it is better classified as fault-017 (ledger stale). The license resolves to a real entry
at the right anchor; the description of that entry is outdated.

**grd-002 license status: NOT DANGLING. Ledger stale — captured under fault-017.**

---

### CHANGE 4 — Dialogue modifications

**Check 4a: halvard:1 "at its own rate"**

Current theater/dialogue file: "It grows crooked at its own rate."
Prior text (from halvard drafts sidecar Draft A): "It grows crooked at the rate it was
always going to grow."

Anchor: @b01c07s02n04 = flat12. Unchanged. Bone cite at proto-line 12 confirmed
(`[septon-halvard-flea-bottom:1]` at bone 12 in the bones file). STRUCTURAL: PASS.

Earth-Bet fence: clean. No Worm proper nouns introduced or affected.

Behavior-card compliance: "It grows crooked at its own rate" is plain-Anglo, no theological
jargon, no strategy supplied to Taylor, no forbidden cadence. The actor overlay "plain
language; no theological jargon" is honored. Q1 (affirmative card demonstration) and Q2
(no card violation) both continue to pass — the simplified phrasing is, if anything, more
idiomatic to the plain accounting register than the original.

AP-SCAN (chassis check): no em-dash+semicolon spine. The em-dash in the entry ("The slow
way costs him more now — he'd go hungry a while, refusing") is unchanged. No deposition
cadence. PASS.

fault-009 (TASTE-FLAG — aphorism-strain at halvard:1): The aphorism-strain concern was
specifically about the elaborated "at the rate it was always going to grow" form, which
the R2 adversarial shard identified as the one place the register strains toward aphorism.
"At its own rate" is simpler, more idiomatic, and less aphorism-shaped. The TASTE-FLAG
risk REDUCES with this change. fault-009 as filed at cycle-1 is now WEAKER; it is
retained as SIGNAL for Phase 5b awareness but with reduced adversarial force.

Halvard drafts sidecar currency: the sidecar (active-project/staff/dialogue-writer/
septon-halvard-flea-bottom.drafts.md) records Draft A with the OLD utterance text. The
halvard R2 shard also records the old text in its adversarial discussion. Neither sidecar
nor R2 shard was updated to reflect "at its own rate." This is a record-currency issue.

- id: fault-018
- type: flag
- what: Halvard drafts sidecar and halvard R2 decision shard both contain the pre-fix utterance text ("at the rate it was always going to grow") while the canonical theater/dialogue file now reads "at its own rate." The sidecar's chosen-mark Draft A and the R2 shard's Stage 2 adversarial discussion quote text that no longer matches the shipped entry.
- why: If a downstream audit or re-run reads the sidecar/R2 shard for halvard:1 utterance verification, the quoted text will not match the canonical file. The halvard R2 shard's facet-license citations (sensory:1@12 + vibes:2/12) remain valid — they are not utterance-text-dependent. The aphorism-strain adversarial defense is now obsolete (the changed text is less aphoristic). Non-blocking; informational only.
- criteria: n/a (SIGNAL — no fixer dispatch; informational for showrunner or the next re-run's sidecar refresh)

**Check 4b: taylor:1 final sentence dropped**

Current theater/dialogue file: entry :1 ends at "She's the first name in the count."
Prior text (from taylor R2 shard + taylor drafts sidecar): also included "She's why I'm
in Flea Bottom at all."

Anchor: @b01c07s03n02 = flat19. Unchanged. Bone cite `[taylor-hebert-kl-122ac:1]` at
proto-line 19 confirmed in both bones file and cite-index. STRUCTURAL: PASS.

Earth-Bet fence: clean. Unchanged.

WATCH-1 concrete landing: The critical check per the chapter goal is that the named death
lands with full specificity: name + family + age + street + district + season + failure-
mechanism + ledger-position. Current entry retains: "The Cobb girl — Wenna, six years old,
Pig-Tallow Lane in the Hook. The fever season, two years back, before there was anyone here
who could route the maester-call in time. By the time someone was found to carry it, it was
a burial, not a call. The slower way kept its principles intact for the eleven days it took
her to die. She's the first name in the count." All WATCH-1 elements are present. The
dropped sentence carried motivational context ("She's why I'm in Flea Bottom at all"), not
any element of the named death's specificity. WATCH-1 PASS.

Behavior-card compliance: fault-011 TASTE-FLAG identified "She's why I'm in Flea Bottom
at all" as the suasion-edge risk (near-thesis-statement-of-motive, approaching self-
justification-to-the-room, which the card forbids). Dropping this sentence removes the
flagged construction. The remaining "She's the first name in the count" is a closing
ledger-register statement — within card. fault-011 is RETIRED: the suasion-edge is gone.

Taylor R2 shard currency: the R2 shard for taylor records the full old utterance including
"She's why I'm in Flea Bottom at all" and defends its KEEP. The shard also carries the
Stage-2 adversarial-counter defense ("The card's closing-clause-twist IS a signature...").
With the sentence dropped, the R2 shard's Stage-2 defense is obsolete but the KEEP verdict
is stronger without the sentence than with it. No new violation is introduced.

Taylor drafts sidecar: carries the old utterance text. fault-014 at cycle-1 flagged the
taylor sidecar for the facet-licenses field not being updated in the chosen-mark block.
The sidecar's quoted utterance text is now also stale (in addition to the facet-licenses
field). This extends fault-014 but does not escalate it.

- id: fault-019
- type: flag
- what: Taylor drafts sidecar and taylor R2 decision shard both carry the pre-fix utterance text including "She's why I'm in Flea Bottom at all." The canonical theater/dialogue file ends at "She's the first name in the count." fault-014 (cycle-1 SIGNAL; sidecar chosen-mark facet-licenses field not updated) is now extended: both the facet-licenses field and the utterance text in the sidecar are stale.
- why: Same downstream traceability risk as fault-018. The R2 shard's KEEP verdict and the WATCH-1 concrete check are both stronger with the sentence dropped; no adverse consequence from the text change. The sidecar is now doubly stale. Non-blocking.
- criteria: n/a (SIGNAL — extends fault-014; no separate fixer dispatch warranted beyond the existing fault-014 sidecar-update action item; the utterance text should be updated at the same time as the facet-licenses field)

**Check 4c: dialogue-coverage still intact**

Bones @12, @19, @21 all carry dialogue citations in the bones file. The dialogue files
contain :1 at halvard (@b01c07s02n04 = flat12), :1 at taylor (@b01c07s03n02 = flat19),
:2 at halvard (@b01c07s03n04 = flat21). All three anchors resolve. No citation was removed
or added by the fixer. STRUCTURAL PASS.

---

## New findings summary

| id | type | area | class |
|---|---|---|---|
| fault-015 | flag | loc-state:3@9 note-slot form | STRUCTURAL (soft) |
| fault-016 | fault | sensory:4@22 modality `proprioceptive` not in schema enumeration | STRUCTURAL — HARD |
| fault-017 | fault | grounding-ledger grd-002 `satisfied_by` field stale | STRUCTURAL — HARD |
| fault-018 | flag | halvard sidecar/R2 shard utterance text stale | RECORD CURRENCY |
| fault-019 | flag | taylor sidecar utterance text stale (extends fault-014) | RECORD CURRENCY |

**Retired findings from cycle-1:**
- fault-008 (NI AP-001 scope-limitation) — RETIRED. AP-001 check addressed by fixer recast; cap count = 1 (narrator:4@19 only); specific concern resolved.
- fault-011 (taylor:1 suasion-edge TASTE-FLAG) — RETIRED. Flagged sentence removed; risk eliminated.

---

## Cycle-2 audit status

**HARD count: 2** (fault-016 + fault-017)

**HARD classes:** STRUCTURAL — invalid schema modality (sensory:4@22); STRUCTURAL — grounding-ledger record stale (grd-002 satisfied_by mismatch)

**HARD findings are coupled:** fault-016 (modality fix) and fault-017 (ledger update) must be resolved together. They are both localized to sensory:4@22 + the grd-002 `satisfied_by` field. Fixer resolution: (1) replace `proprioceptive` with a valid schema modality in sensory:4@22 — best candidates are `tactile` (surface sensation through sole) or `pressure` (weight/force through sole and joint); (2) update grounding-ledger grd-002 `satisfied_by` to reflect the corrected modality and delta.

**Other findings:** fault-015 (SIGNAL — loc-state note-slot form question; non-blocking), fault-018 (SIGNAL — halvard sidecar text stale; non-blocking), fault-019 (SIGNAL extending fault-014 — taylor sidecar text stale; non-blocking).

**Change-area confirmations:**
- NI narrator:3@15 AP-001 recast: MECHANICALLY SOUND (cap = 1; anchor preserved; structural citations unchanged). Scope-limitation on file text verbatim confirmed same as cycle-1.
- loc-state:3@9 new sound field: SOUND for upstream-baseline purpose; soft form question flagged (fault-015, non-blocking).
- sensory:1@12 old-state resolution: RESOLVES to loc-state:3@9. PASS.
- sensory:2@17 old-state resolution: RESOLVES to loc-state:4@15. PASS.
- sensory:4@22 old-state resolution: RESOLVES to loc-state:4@15. PASS on the old-state anchor. Modality INVALID (fault-016 HARD).
- grd-002 license: NOT DANGLING. Stale content — fault-017 HARD.
- halvard:1 "at its own rate": structurally clean; card-compliant; fault-009 TASTE-FLAG weakened.
- taylor:1 final sentence dropped: WATCH-1 concrete intact; fault-011 retired; card compliance improved.
- Dialogue anchor coverage: unchanged and intact at @12/@19/@21.

---

## Phase 5b cycle-2 routing

**Phase 5b cycle-2: BLOCKED.**

HARD count = 2. Fault-016 (invalid sensory modality) and fault-017 (grounding-ledger stale) must be resolved before Phase 5b cycle-2 aggregation can stand. Both are localized fixer-scope fixes (change one modality field; update one ledger field). Neither requires episode-plan revision or upstream re-authoring.

**Fixer dispatch: required for fault-016 + fault-017 (coupled; resolve together).**

After fixer resolves fault-016 + fault-017, a cycle-3 mechanical re-check of sensory:4@22
modality validity + grd-002 `satisfied_by` field match is required before Phase 5b fires.
All other findings are SIGNAL and do not block.
