# Continuity Audit — /and-write b01c09 Phase 5
# auditor: fork, 2026-05-31
# target: active-project/staff/showrunner/b01c09-bones-draft-2026-05-31.md
# schema: schemas/audit-report.schema.md

---

## Verdict

FINDINGS-PRESENT — 1 fault, 1 flag. Not CONTINUITY-OK.

---

## Findings

---

### fault-001

**id:** fault-001
**type:** fault
**axis:** FAULT-REFERENCE

**what:**
Bones b01c09s02n09, b01c09s02n04, and b01c09s02n05 use "corwick" as the SVO subject slug:

- n09: `"the insect-feed returns corwick"`
- n04: `"corwick faces the second man"`
- n05: `"corwick squares the shoulders"`

"corwick" is a bare first-name token. It does not resolve against the cast roster. The series actor_baselines section registers eleven actors; none carries the slug "corwick" or any compound form. The character was named in b01c08s03 through Oswyn's dialogue but was never formally registered as a cast actor with a project-canonical slug.

**why:**
The project's established slug convention requires compound kebab-case actor identifiers (taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward, oswyn-mudway-flea-bottom-elder, jarvis-coin-kl-courier). At /and-write b01c04 Phase 2, "actor-slug abbreviations" were a HARD fault resolved by inline fix ("wren-stitch-house → wren-stitch-maker-flea-bottom-ward"; "oswyn-mudway → oswyn-mudway-flea-bottom-elder"). The same class of deficiency applies here. An unresolved slug propagates into Phase 7 bones emit, breaks the dialogue-citation anchor pattern (no registered slug = no dialogue citation can resolve), and will fail Phase 2 SVO audit.

**criteria:**
Assign a canonical compound slug for the courier character consistent with project naming convention (slug format: `<given-name>-<role-descriptor>-<location-context>`; example: `corwick-kl-courier`). Register the slug with margit (cast card + warehouse INDEX entry). Update the three SVO lines in the bones draft to use the canonical slug. The slug must also match any future dialogue citations.

---

### flag-001

**id:** flag-001
**type:** flag

**what:**
Bones b01c09s02n01, b01c09s02n02, and b01c09s02n03 reference specific physical locations for the first time as scene-entered set pieces:

- n01: `"taylor-hebert-kl-122ac enters the dragonpit-margin lane"` — the Dragonpit-margin lane as a physically traversed location
- n02: `"the supply cart marks the lower-gate road"` — lower-gate road
- n03: `"the stone-post marks the lower gate side-exit"` — lower-gate side-exit, stone-post

The b01c09 chapter entry in memory.md does not include a `write_margit_referrals_open` block (contrast b01c07 which carried `oc-sept-corner.card.md` as an explicit forward-notice). Warehouse card existence for these locations cannot be confirmed from available files.

**why:**
At /and-write b01c04 Phase 5, three novel physical locations first touched at the bones layer were FAULT-REFERENCE findings (oc-cooper-yard-eel-alley, oc-pig-tallow-lane, oc-ropers-court); margit had to author cards before the audit could clear. The dragonpit-margin lane and lower-gate side-exit are different in kind from those three (they are Westerosi canon KL geography, not invented-for-this-project locations), so they may be covered by the warehouse's cond-kl-geography-122ac location cards rather than requiring new oc-* cards. Warehouse state cannot be confirmed from the bones draft and memory alone. If cards are absent, Phase 2 audit will surface FAULT-REFERENCE on these locations.

This is classified as a flag rather than a fault because: (a) the /and-substance chapter Phase 5 auditor returned "0 HARD" with no location-card deficiencies flagged (weaker signal than direct warehouse verification, but on record); (b) the locations are canonical Westerosi geography; (c) the Dragonpit and its gates are referenced as background in earlier chapters without new margit cards being required.

**action:** Verify warehouse card coverage for dragonpit-margin-lane and lower-gate-side-exit before Phase 2 /and-write audit. If no cards exist, dispatch margit to author location cards before proceeding.

---

## Axes checked with no findings

**FAULT-REACHABILITY:** No fault.

Chapter goal: "Show that Taylor is now surveilling Wren as routine coverage — and not calling it that — and advance the courier-face so the d10 accounting has a body with a history."

- Goal leg 1 (surveillance-without-naming): s01 bones deliver Wren's daily pattern in the internal map (n02, n03, n04-moving, n05), deliverable receiving geometry-not-pattern (n07), substrate split enacted without naming (n06). relational_anchor_status +0.5 at n04 (cl-d08). DELIVERED.
- Goal leg 2 (courier-face advance): s02 bones deliver the courier at the Dragonpit lower gate (n09, n04, n05), posture-class filed (n06-moving, cl-d05), Black-faction contact inferred, observation withheld from Jarvis (n07, n08). political_register-prot +0.5 at n06. DELIVERED.
- Chapter close / thesis-image: s03 delivers two-substrates-one-station-surface with all axes held. DELIVERED.

Handoff_out claims versus bones output:
- "Wren anchor rank 3.5" — bones deliver relational_anchor_status from 3 (handoff_in) +0.5 (s01n04) = 3.5. CONSISTENT.
- "courier observed at Dragonpit, withheld from Jarvis" — s02 n07+n08 deliver this. CONSISTENT.
- "political_register-prot resentment deepening / rank 3.5" — bones deliver from 3 (handoff_in) +0.5 (s02n06) = 3.5. CONSISTENT.
- "capability rank 5 / moral_framework rank 0" — no capability or moral_framework moves. Held axes rationales reference these ranks correctly. CONSISTENT.

**FAULT-STATE:** No fault.

Scene sequence (s01 ward circuit south of Hook → s02 dragonpit-margin evening circuit → s03 feed-station accounting close) is a coherent single-day operational sequence. No actor appears in two places simultaneously. No prop is referenced after deletion. Axis tracking across scenes is internally consistent: relational_anchor_status opens at 3, moves at s01n04 to 3.5, held at 3.5 through s02 and s03 (scene contracts match). political_register-prot opens at 3, held through s01, moves at s02n06 to 3.5, held at 3.5 through s03 (scene contracts match).

**FAULT-POV:** No fault.

Non-Taylor SVO subjects throughout the draft (the insect-feed, the stitch-shop door, the supply cart, the stone-post, the ward-coverage notes, the internal map, the feed-record, the seal, corwick) conform to the established feed-POV-by-object idiom confirmed in c02. No bone smuggles interiority or perception into Taylor via the SVO line itself. The axes_held rationales contain Taylor's accounting logic, but those are in the rationale fields, not in the SVO prose. The "the internal map files wren's route" (s03n05) and "the feed-record closes the courier entry" (s03n06) treat internal architectural structures as physical objects performing observable acts — consistent with the project idiom, not a POV leak.

**FAULT-HANDOFF-IN-MISMATCH:** No fault.

All handoff_in terms honored by opening bones:
- "Wren anchor rank 3, daily pattern beginning to be legible" — s01 opens with the pattern already accumulated, moving to 3.5. No contradiction.
- "courier named (beat 1 complete)" — the bones treat corwick as a known figure from c08 (the courier appears, is not introduced fresh). No contradiction.
- "Oswyn watcher-network inside coverage" — not contradicted; background architecture, not referenced directly.
- "Taylor: capability rank 5 / moral_framework rank 0 / political_register-prot rank 3" — s01 axes_held rationales reference rank 5, rank 0, rank 3 correctly. No contradiction.
- "KL 122 AC coverage expanding" — s01 treats the Wren-lanes coverage as already expanded (boundary moved three weeks ago). No contradiction.

**Plan quality signal and audience protocol:** Not applicable to this gate (Phase 5 continuity; no audience rejections in bones draft; no REVISE-due-to-exhaustion condition on the chapter plan record).

---

## Scope note

fault-001 is episode-scope: fixable by assigning a compound slug and updating three SVO lines. Margit dispatch required for slug registration. flag-001 is episode-scope: fixable by warehouse card verification before Phase 2 audit.
