---
reviewer: worm-canon-pedant
facet: state-updates
episode: b01c01
cycle: 2
date: 2026-05-25
verdict: accept
---

# Verdict summary

Three of my four cycle-1 reject callouts are resolved. The fourth (entry-2, capability_axis) was correctly deleted; I was already on record that the anti-pattern #7 fire was the problem, and the deletion comment in the slice confirms the removal on the exact basis I named. All four Taylor deletes landed correctly. The Wren entry received the field-extension comment it was missing and the value was cleaned to remove the embedded authoring metadata and the inaccurate deterrence charge. The two surviving Taylor entries (deployment-state @12, body-orientation @24), both Oswyn entries, and the revised Wren entry all pass the three axes under V2. No new anti-pattern fires visible in the post-cycle-1 files. Env zero-fire defense is unchanged and still correct.

The auditor's cycle-2 confirm report (facets-cycle2-audit-confirm.md) surfaces a HARD finding (fault-C2C-001) against the dialogue sidecar entries 1 and 2 carrying unresolvable sensory:2 @16 citations. That fault is in the dialogue facet, not in state-updates. It is not within the scope of this state-updates review. The state-updates slice files and the consolidated state-updates.md are clean.

One carry-forward soft observation: the @17 bare-protoline gap documented in cycle-1 (state:5 deleted for missing NI co-citation; re-add contingent on NI author providing @17 entry) remains open as of cycle-2. The gap is not my call to resolve — the NI author route was correctly documented by the fixer. I note it as a matter of record; it does not change my state-updates verdict.

---

# Per-entry readings (post-cycle-1 files)

## taylor-hebert-kl-122ac

Taylor slice now carries 2 entries (down from 6). Both cycle-1 deletes confirmed in file (deletion comment block present with correct basis named for each removal).

**Entry 1 — @12, deployment-state: passive-subsistence-range -> active-crowd-yield-deployment**
Accept. Same basis as cycle-1 — mode-flag, anchor at the deployment bone, field-extension comment present, persistence absolute through handoff_out. No change.

**Entry 2 — @24, body-orientation: facing-the-child -> facing-the-alley-mouth-away-from-stitch-house**
Accept. Same basis as cycle-1 — directional-commitment verb at @24, persistent through chapter close, distinction from posture held, field-extension comment present. Cite-index: state:7 @24 back=Y co=[narrator:8] — narrator co-citation present, POV actor-state cross-facet contract satisfied. Clean.

**Deleted entries (cycle-1):**
- capability_axis @12: deleted. Confirms resolution of my [state-updates:taylor:entry-2] callout. The deletion comment names anti-pattern #7 (pre-empting / ledger-as-state) — correct characterization.
- posture @17: deleted. POV actor-state without NI co-citation — correct. Re-add path documented.
- social_tether_prot_axis @21: deleted. Field not on schema + ledger-as-state — confirms my [state-updates:taylor:entry-4] callout (different framing: I called ledger-as-state; fixer also found anti-pattern #6 invented-field confirmed by state.md check; either basis terminates the entry).
- ward-recognition @26: deleted. Cross-POV authority violation — confirms my [state-updates:taylor:entry-6] callout. Clean.

## oswyn-mudway-flea-bottom-elder

Both entries unchanged from cycle-1. Both accepted in cycle-1. Confirming both hold:

**Entry 1 — @21, location: mudway-alley-hook-district -> lane-mouth-of-rescue-site**
Accept. Unchanged. Position-shift verb, persistence through @26, authority correct (Oswyn fork writing Oswyn state), cite-index state:1 @21 back=Y with full co-list. Clean.

**Entry 2 — @26, relationship_to_taylor: regular-contact-no-awareness-of-function -> categorized-known-unknown-witch-adjacent**
Accept. Unchanged. Field-extension comment present. Chin-lift as somatic expression of a cognitive shift that persists into handoff_out world_state confirmed. Non-POV character; no NI co-citation required. Cite-index state:2 @26 back=Y co=[mem:2, narrator:9]. Clean.

## wren-stitch-maker-flea-bottom-ward

**Entry 1 — @27, relational_anchor_to_taylor: nascent -> observation-traced-chapter-1**
Accept. Cycle-1 soft-flag was the missing field-extension comment and the malformed value containing embedded authoring metadata ("d01") and inaccurate affect charge ("deterrence"). Both fixed: field-extension comment is now present in the slice, documenting the new field, old/new value semantics, and persistence claim. Value changed to "observation-traced-chapter-1" — removes metadata slug, removes inaccurate deterrence charge, anchors the observation to the chapter without inventing an affect. The new value is precise: Wren has directly observed Taylor's intervention and has a face; "nascent" correctly names the prior state. Persistence claim ("Wren has seen Taylor's face") corroborated by handoff_out. Cite-index state:9 @27 back=Y co=[exposition:9, feel:4, narrator:6, vibes:9, vibes:10] — non-POV, NI co-citation not required; the co-list is rich and consistent. My soft-flag is resolved.

## env

Zero-fire defense unchanged. Accept. Same basis as cycle-1.

---

# Entry-level callouts (cycle-2)

None. All four cycle-1 reject entries deleted; Wren entry revised to address both flagged gaps. No new fires or anti-patterns observed in the post-cycle-1 files.

---

# Convergence trace (cycle-2)

| Cycle-1 callout | Fixer action | Resolution |
|---|---|---|
| [state-updates:taylor:entry-2] @12 capability_axis (anti-pattern #7 / ledger-as-state / no cost-registration) | DELETED — fault-SU-001; deletion comment names anti-pattern #7 and confirms handoff_out holds rank-3 record | RESOLVED |
| [state-updates:taylor:entry-4] @21 social_tether_prot_axis (anti-pattern #7 / invented-field / missing NI co-citation) | DELETED — fault-SU-003; fixer confirmed field absent from state.md + ledger-as-state error | RESOLVED |
| [state-updates:taylor:entry-6] @26 ward-recognition (cross-POV authority violation / missing NI co-citation) | DELETED — fault-SU-004; double-filing confirmed (Oswyn categorization canonical in Oswyn slice) | RESOLVED |
| Wren entry soft-flag (missing field-extension comment; malformed value with d01 metadata + inaccurate deterrence charge) | REVISED — fault-SU-005; field-extension comment added; value corrected to observation-traced-chapter-1 | RESOLVED |
| @17 bare-protoline gap / posture NI co-citation absent (noted soft) | DELETED state:5 with re-add path documented for NI author; gap remains open | OPEN — not a state-updates fault; NI author route documented; no state-updates entry needed until NI fires at @17 |
