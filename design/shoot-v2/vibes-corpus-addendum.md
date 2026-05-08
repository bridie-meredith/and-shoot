# Vibes-Updates Corpus Addendum

Applies to: `design/shoot-v2/vibes-corpus.md` (locked 2026-05-07)
Authored: Phase 4 (RF-001 resolution)

---

## What the corpus assumes

The `vibes-corpus.md` reference fires (16 entries; 16 × `+`) were authored under the assumption that s01e01 is the project's first episode and no vibe-clouds exist at facet-authoring time. Under this assumption:

- All five s01e01 event-keywords (`the-machinery-arrives`, `the-letter`, `the-naming`, `the-septon-as-absence`, `the-yard-as-witness`) are absent from all target vibe-sets at episode open.
- Every corpus fire is a fresh `+` add.
- No `++` operations appear because there is nothing yet to extend.
- Calibration anchors C1–C4 are satisfied by fresh `+` fires.

This is the clean-slate scenario. The corpus is internally consistent and correct for that scenario.

---

## What this project actually has

This project (taylor-hebert-westeros / s01) pre-seeds vibe-clouds at world-build / project-activation time. At episode-facet-authoring time:

- `active-project/actors/taylor-hebert-westeros/vibes.md` carries all five s01e01 event-keywords with full token-bundles.
- `active-project/actors/mira-stonefield/vibes.md` carries `the-machinery-arrives` and `the-yard-as-witness`.
- `active-project/actors/edric-cray/vibes.md` carries `the-machinery-arrives` and `the-yard-as-witness`.
- `active-project/actors/census-officer/vibes.md` carries `the-machinery-arrives`.
- `active-project/staff/studio/vibes.md` EPISODE_1_VIBES section carries all five s01e01 event-keywords.

The clean-slate assumption is false. Gate 2 applies to all these pre-loaded targets. The 16 × `+` corpus format is not valid as the Phase 2 target for this project.

---

## Effective Phase 2 target for pre-seeded projects

For a project with world-build pre-seeding, the effective Phase 2 task is the `++`-and-fresh-add subset:

**`++` operations:** Extend pre-loaded keywords with genuinely non-duplicate tokens licensed by on-screen s01e01 beats. Required when on-screen beats add tokens not covered by the pre-loaded bundle. Optional (skip) when the pre-loaded bundle already covers the event's full qualitative-consequence range.

**Fresh `+` operations:** Add new keywords to targets whose vibe-sets do not yet carry the keyword. In this project: `actor:septon-dying-protector` (no s01e01 event-keywords pre-loaded), `loc:harrenhal-sept-environs` (empty vibe-set — no card VIBES section), and any other entity targets with genuinely empty vibe-sets.

**Skips (legitimate):** Episode-scope keywords already fully covered by the EPISODE_1_VIBES pre-load, with no genuinely non-duplicate tokens from on-screen beats. Skipping is correct rubric behavior, not a fault.

---

## Corpus calibration anchors — re-evaluation for pre-seeded projects

| Anchor | Corpus form | Pre-seeded form |
|---|---|---|
| C1 — `actor:taylor +the-machinery-arrives` | Fresh `+` | Satisfied by pre-load; episode-facet contributes `++` extension only |
| C2 — `actor:septon +the-septon-as-absence` | Fresh `+` | Remains fresh `+` — septon vibe-set does not carry this keyword at activation |
| C3 — `actor:mira +the-yard-as-witness` | Fresh `+` | Satisfied by pre-load; episode-facet contributes `++` extension only |
| C4 — `episode +the-naming` | Fresh `+` | Satisfied by EPISODE_1_VIBES pre-load; episode-facet contributes `++` only if non-duplicate tokens exist |

The calibration anchors remain valid as CHECKS — the question is whether the target carries the keyword (pre-load or facet-fire, either satisfies the anchor). The specific operation (`+` vs `++`) depends on the pre-seeded state.

---

## Expected yield for pre-seeded projects (revised)

Clean-slate expected yield: ~16–20 entries (16 × `+`).

Pre-seeded expected yield: ~9–14 entries (mix of fresh `+` on empty targets, `++` extensions on pre-loaded targets, deletions where pre-load covers range).

The reduction in entry count relative to the corpus is correct behavior in a pre-seeded project. A pre-seeded Phase 2 file with 9–12 entries that correctly identifies empty targets for `+` fires and correctly extends pre-loaded targets with non-duplicate `++` tokens is a higher-quality output than a 16-entry file with AP5 faults on all pre-loaded targets.

---

## For future episodes

From s01e02 onward, the vibe-cloud files carry the results of s01e01 facet authoring. Episode-scope targets in `studio/vibes.md` will be populated from prior EPISODE_N_VIBES sections. The pre-seeded scenario is the normal state for all subsequent episodes: every episode begins with a populated cloud, and the facet author uses `++`-or-skip for pre-loaded keywords and fresh `+` for new keywords introduced by that episode's events.

The clean-slate corpus scenario applies only to hypothetical project-activation-time authoring where no world-build pre-seeding has occurred. In practice, any project using the world-build pipeline described in the showrunner memory schema will encounter pre-seeded clouds at the first episode.

---

## Status

Addendum authored Phase 4. Addendum is a supplement to the locked corpus, not a replacement. The corpus remains the gold-standard reference for the clean-slate scenario and for the structural logic of fan-out coherence, calibration anchors, and anti-pattern refusals. This addendum narrows the scope of applicability and restates the effective Phase 2 target for pre-seeded projects.
