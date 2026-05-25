---
reviewer: worm-canon-pedant
facet: state-updates
episode: b01c01
cycle: 1
date: 2026-05-25
verdict: revise
---

# Verdict reasoning

Two entries write canonical-axis stat increments directly into state-updates fields —
`capability_axis: 2 -> 3` at @12 and `social_tether_prot_axis: 1 -> 2` at @21 — and
the Worm-specific concern is stark: in canon, Taylor's shard capability does not increment
as a discrete integer at a single observed beat; it is an asymptotic pressure that
surfaces through accumulated cost and feedback loops, not a ledger-click. Treating it as
a +1 stat posted to a canonical field at the moment of insect-propagation is a power-
mechanic legibility failure — it makes the shard look like a level-up system, which it is
not. Additionally, entry [state:8] at @26 fires on `actor:taylor-hebert-kl-122ac.ward-
recognition` — a field that tracks how the ward categorizes Taylor — but authority for
that field should belong to the Oswyn fork (it is a shift in Oswyn's perception-and-
categorization of Taylor, authored from Taylor's perspective in violation of the cross-POV
authority rule). Two findings: one power-mechanic mis-representation, one authority
violation. The file is revise, not fail, because the env zero-fire defense is clean and
the location/posture entries are form-correct.

---

# Per-entry readings (group by character file + env)

## taylor-hebert-kl-122ac

**Entry 1 — @12, deployment-state: passive-subsistence-range -> active-crowd-yield-deployment**
Accept on reality and authority. The insects propagate at @12; that is the bone. Deployment
posture shifts from suppressed to active and the field-extension comment names the persistence
anchor (handoff_out confirms deployment active at close). The field is a legitimate tracked-
state aspect — on/off posture of the insect-network. From a Worm-mechanics standpoint, this
is the right kind of field: a mode-flag, not a magnitude claim. The frugality check holds;
@12 is the first bone where the deployment actually fires (bones 4, 9, 11 are crowd-pressure
buildup without explicit deployment). The cross-facet co-citation with narrator:4 at @12 is
present. No complaint here.

**Entry 2 — @12, capability_axis: 2 -> 3**
Reject. This is the power-mechanic flag. The entry posts a canonical-axis integer increment
— `capability_axis: 2 -> 3` — at the beat where the insects propagate. The rubric's reality
axis asks: does a tracked field on a real card change at this beat and is the change persistent?
The answer here requires that a shard capability axis is a discrete integer that ticks up at
observable action-beats. That is not how Taylor's power works in Worm source. Khepri-Taylor's
capability is a surface of shard investment and feedback: it does not snap from 2 to 3 at the
moment she pushes bugs into a crowd gap. The substance contract may declare capability+1.0
across the chapter — that is a chapter-level delta accounting device — but mapping it directly
to a canonical field that increments at @12 treats the shard like a JRPG stat bar. This is
a power-mechanics-exceed-established-limits flag (persona hot-button 1): the field implies
a quantized, real-time incrementing model of shard ability that Worm does not support without
acknowledged divergence. The entry also conflates substance_delta bookkeeping (chapter aggregate)
with mid-beat canonical state (what the field value is at @12). If the chapter ends with
capability rank 3, that is a handoff_out fact, not a @12 bone-anchored state-update. The
proposed state-update fires too early and misrepresents the mechanism.

**Entry 3 — @17, posture: in-the-gap -> hands-up-mouth-shut-witness-facing**
Accept with a soft note. The posture is load-bearing across @17–@22 (the chunk that produces
the witch-label) and it resolves at @24 (body-orientation fires). Persistence is defended.
The field-extension note is present. The cross-facet picture is consistent: @17 is a bare
proto-line (no co-citations), which is unusual for a posture fire on the POV character — the
rubric says POV actor-state shifts require narrator-interest co-citation, but I see no
narrator:* entry at @17 in the cite-index. The cite-index lists state:5 back=Y @17 as a
lonely entry (no co-location, no inbound license). The rubric cross-facet contract: "every
`actor:taylor.*` entry must have a narrator-interest entry on the same beat." @17 does not.
This is a cross-facet contract gap. Not a power-mechanics flag from my lens, but it is a
structural flag the auditor should have caught harder. Noting it; it reinforces the revise
verdict without adding a new grounds category (the auditor's flag-list would cover this under
the cross-facet signal findings I am not re-enumerating).

**Entry 4 — @21, social_tether_prot_axis: 1 -> 2**
Reject. Same class of failure as entry 2. `social_tether_prot_axis` is a substance-contract
axis tracking Taylor's protection-tether count in the social ledger; incrementing it as a
canonical integer at @21 (Oswyn takes the lane-mouth) again treats a narrative cost-tracking
device as a discrete real-time counter that ticks at observable beats. The comment acknowledges
this is the cl01b anchor bone — which confirms this is chapter-substance bookkeeping, not a
moment-of-bone state-flip. The tether-axis value does not snap from 1 to 2 when Oswyn steps
to the lane-mouth; the tether is a retrospective assessment of what the chapter delivers,
not a real-time field mutation. Writing it as a canonical state-update at @21 is power-
tradeoff legibility failure: the cost-tracking mechanism is being rendered as if it is a
live in-world event that the canonical state file should hold mid-chapter. In Worm terms, this
is the equivalent of writing `actor:taylor.shard-investment: low -> medium` at the moment
she first makes eye contact with Tattletale — it confuses the narrative accounting layer with
the canonical-state layer.

**Entry 5 — @24, body-orientation: facing-the-child -> facing-the-alley-mouth-away-from-stitch-house**
Accept. The field-extension is a direction-of-attention field, cleanly distinct from posture.
The bone text ("taylor-hebert-kl-122ac faces the alley-mouth") is a persistent re-orientation
named explicitly in the bone rationale. Narrator-interest co-citation at @24 is present
(narrator:8 via cite-index). The POV actor-state cross-facet contract is satisfied. The
not-looking-at-the-stitch-house is a tracked-state aspect (it governs what Taylor does and
does not register for the rest of the chapter). Clean.

**Entry 6 — @26, ward-recognition: invisible-foreign-woman -> categorized-by-oswyn-as-something-other**
Reject. Authority violation. The field `ward-recognition` is glossed as "the ward's category
for Taylor" in the comment — which is actually Oswyn's categorization of Taylor, not a state
that Taylor's fork has authority to write. The field name obscures the violation: it sounds
like it belongs on Taylor's schema ("how the ward recognizes her"), but the comment confirms
it tracks what Oswyn has categorized Taylor as ("the ward's category for Taylor," "Oswyn's
chin-lift is the categorization-completing body-tell"). The shift being recorded — Oswyn
completing a mental categorization of Taylor — is a field on Oswyn's social-awareness state,
not Taylor's. This is cross-POV authoring (anti-pattern #2): Taylor's fork is writing a
state-update for a shift in Oswyn's cognitive/social state and attaching it to Taylor's actor
slug to slip past the authority rule. Compare: `actor:oswyn.relationship_to_taylor` entry at
@26 (in the Oswyn slice) correctly fires on Oswyn's own slug for the same beat. Firing again
on `actor:taylor.ward-recognition` for the same moment, authored by the Taylor fork, is
double-covering Oswyn's categorization from the wrong authority. Even if `ward-recognition`
were Taylor's own tracked field (e.g., "Taylor's knowledge of how the ward categorizes her"),
the update would require narrator-interest co-citation at @26, and the cite-index shows
state:8 co-cited with mem:2 and state:2 — no narrator entry at @26 at all. POV actor-state
co-citation is missing AND the authority is wrong. Two-axis failure.

## oswyn-mudway-flea-bottom-elder

**Entry 1 — @21, location: mudway-alley-hook-district -> lane-mouth-of-rescue-site**
Accept. Oswyn takes the lane-mouth at @21. The position shift is real, the persistence is
clear (she is at the lane-mouth through @26 where the chin-lift fires). The Oswyn fork writes
the Oswyn actor-state — no authority problem. @21 is a peak-bone (cite-index lists it as the
highest co-citation node in the chapter). The rubric expects state-update co-citation at
peak-bones-class beats; this fires correctly. Form is clean.

**Entry 2 — @26, relationship_to_taylor: regular-contact-no-awareness-of-function -> categorized-known-unknown-witch-adjacent**
Accept with narrow note. The field is on Oswyn's schema (or is a legitimate field-extension
on her state.md under the rubric's extension protocol). The chin-lift at @26 is the somatic
expression of a cognitive shift that persists through chapter close (handoff_out world_state
named). Authority is correct — Oswyn fork writes Oswyn actor-state. The field-extension
comment is present. The value `categorized-known-unknown-witch-adjacent` is slightly thick
but is a compound that names a real semantic: known (recognizes her), unknown (does not know
her function), witch-adjacent (the social label beginning to attach). This is the kind of
precision that earns tolerance from my reading. The cross-facet picture: @26 co-cites mem:2
and state:2 — no narrator entry, but the non-POV rule applies here. Oswyn is not the POV
character; no narrator-interest co-citation required. Clean.

## wren-stitch-maker-flea-bottom-ward

**Entry 1 — @27, relational_anchor_to_taylor: nascent -> observation-traced-d01-deterrence**
Borderline accept. The field tracks where Wren's awareness of Taylor is anchored. At @27
("wren-stitch-maker-flea-bottom-ward faces taylor-hebert-kl-122ac") there is a turn — Wren
faces Taylor, which is the first explicit acknowledgment in the bones that Wren has a
directional relationship to Taylor. The value `observation-traced-d01-deterrence` is opaque:
"d01-deterrence" reads as an internal project shorthand (a deterrence relationship coded to
day-01?) rather than a plain state description. If that label is not defined anywhere on
Wren's card or state schema, it is an invented-value entry that fails the authority test
through value-space extension without documentation. The field-extension comment is absent
from this entry (compare the Taylor and Oswyn entries, which all carry `# field-extension:`
comments). The schema requires field-extensions to be documented. This is a soft flag: the
field is plausibly a tracked-state aspect (Wren's relational awareness of Taylor is load-
bearing for downstream chapters), but the value-label is undocumented and the extension
comment is missing. Not a fatal reject from my primary lens (no power-mechanic misrep, no
canon-continuity break), but the missing extension documentation is a form failure the
auditor should have flagged as a hard requirement. Noting as a soft concern.

## env

Accept. The zero-fire defense is well-constructed and internally consistent. The chapter is
exterior Flea Bottom, no tracked prop exchanges, no door state, no time-of-day shift,
crowd-dynamics transient. The rubric explicitly prohibits inflating fires to hit density band;
the defense cites the relevant section. SEAM-001 (fish-cart) and SEAM-002 (time_of_day
baseline) are correctly flagged as seams rather than entries — the conservative ruling under
the field-extension protocol is taken. No attack from my lens here.

---

# Entry-level callouts (revise/fail only)

**[state-updates:entry-2] @12 actor:taylor-hebert-kl-122ac.capability_axis: 2 -> 3**
Power-mechanic legibility failure. Shard capability does not quantize to an integer that
ticks at an observable action-beat in Worm source. This maps substance-contract bookkeeping
(chapter-aggregate Δ) onto a canonical field as if it is a real-time mid-bone increment.
Fires too early (chapter-end fact posted at mid-chapter bone) and misrepresents the
mechanism. Remove or defer to handoff_out as a baseline-initialization fact, not a bone-
anchored state-update.
Convergence: no direct auditor flag found on this specific entry in r2 audit. Signal
findings (flag-001 to flag-021) not re-enumerated in r2 — potential seam in auditor's
signal-finding coverage.

**[state-updates:entry-4] @21 actor:taylor-hebert-kl-122ac.social_tether_prot_axis: 1 -> 2**
Same class. Substance-contract axis increment posted as a bone-anchored canonical state-
update mid-chapter. The axis does not flip at Oswyn's lane-mouth step; it is the chapter's
retrospective accounting of what the Oswyn encounter costs and delivers. Remove or defer to
handoff_out / showrunner-canonical baseline update post-chapter-close.
Convergence: same gap as entry-2 — not explicitly flagged in r2 HARD findings.

**[state-updates:entry-6] @26 actor:taylor-hebert-kl-122ac.ward-recognition: invisible-foreign-woman -> categorized-by-oswyn-as-something-other**
Authority violation. Field glossed as "the ward's category for Taylor" is Oswyn's cognitive
state, not Taylor's. Cross-POV authoring by the Taylor fork. Additionally, @26 carries no
narrator-interest entry (cite-index: state:8 co=[mem:2, state:2] — no narrator co-citation),
so the POV actor-state cross-facet contract is broken even if the authority issue were
resolved. Two-axis failure: authority (wrong author) + cross-facet (missing narrator co-
citation). Delete entry. If Taylor's knowledge of Oswyn's categorization needs to be tracked,
it should be authored as `actor:taylor.knowledge.oswyn-categorization-of-taylor` by the
Taylor fork with narrator-interest co-citation — and that narrator-interest entry must exist
first.
Convergence: auditor r2 CLEAN status covers faults 001-005 only; this authority/cross-facet
violation on entry-6 appears to be outside the r2 fault scope (signal findings not
re-enumerated). Potential coverage gap.

---

# Convergence trace

| Callout | Auditor r2 finding | Overlap |
|---|---|---|
| entry-2 capability_axis stat-increment | Not explicitly in r2 HARD list (fault-001 to fault-005 cover cite-ID corrections and token form) | No direct convergence — gap |
| entry-4 social_tether_prot_axis stat-increment | Not explicitly in r2 HARD list | No direct convergence — gap |
| entry-6 ward-recognition authority + cross-facet | Not in r2 HARD list; signal findings (flag-001 to flag-021) not re-enumerated in r2 | Possible overlap with prior-round signal findings — unverifiable |
| entry-3 @17 narrator co-citation absence | cite-index "lonely entries" list names state:5 @17; auditor's signal findings may include this — not confirmed from r2 text alone | Soft overlap with lonely-entry classification |
| Wren entry missing field-extension comment | Not in r2 verified scope | No convergence — gap |
