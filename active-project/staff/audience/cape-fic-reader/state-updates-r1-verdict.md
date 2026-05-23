---
reviewer: cape-fic-reader
facet: state-updates
cycle: 1
episode: b01c01
date: 2026-05-23
verdict: revise
---

# Verdict reasoning

The board-tracking is mostly clean — positions, pack, watch-rotation, time-of-day all fire at the right beats and the asymmetry logic (Taylor acquires ward-geometry passively at @9, closes the ledger at @20) is readable. But state:10's inline comment is still doing it wrong: the comment names "watch-rotation geometry" as one of the accumulated items feeding the @20 field flip, while the field value has been safely narrowed to `day-count-complete`. That seam matters. The co-cited narrator:7 covers "the day closed under the count" — which licenses the general ledger-close — but the comment's enumeration of watch-rotation as a specific item in that accumulation is a knowledge-transition leak that the NI text does not register and Taylor should not have cleanly filed without a specific acquisition beat. The patrol-rotation was a single environmental pass (@18-@19); the rubric's POV-restriction says Taylor perceiving it is narrator-interest territory, not a silently accumulated knowledge-field delta that the comment attributes to the @20 close as if it were already banked. Either strip the watch-rotation reference from the comment and limit the accumulation claim to density/corridor/occupation-pattern (what the scene actually walked), or put the acquisition on the @18-@19 watch-pass beat where it belonged. As it stands, the comment is telling me Taylor filed patrol-rotation as a known quantity through diffuse accumulation, and the NI record does not confirm that — that is exactly the "wait, when did she know that" trigger.

The prop:oc-taylor-pack slug is unresolved, which is a lower-stakes issue but matters if this card is going to persist across chapters as an inventory anchor.

# Entry-level callouts

- [state:10] @20 — comment at lines 118-127 enumerates "watch-rotation geometry" as accumulated knowledge feeding the @20 field flip, but narrator:7's ledger-close text does not register patrol-rotation as a specific filed item; the comment contradicts the NI co-citation's register and implies Taylor banked patrol-rotation through passive accumulation with no acquisition beat, which is an unmotivated knowledge transition — the comment needs to limit its enumeration to what the scene's NI record actually logged.
- [state:3/env-entry-3] @7 — prop:oc-taylor-pack slug carried across this entry and through subsequent chapters without verified warehouse card resolution; the target field cannot be confirmed as writing back to a real canonical card.

# Convergence trace

- fault-012 overlap: auditor flagged content-alignment gap between state:10's field mutation and narrator:7's register. The field value was narrowed (repair present), but the inline comment enumeration of watch-rotation geometry is a residual content-alignment seam that the repair did not close. The auditor's criteria (a) said "narrow the field mutation to match what narrator:7 licenses" — the field value narrowed but the comment re-introduces the unauthorized item. Partial repair; the seam is still open at the comment level.
- fault-019 overlap: prop:oc-taylor-pack card-resolution unverified. Auditor flagged this as advisory pending warehouse verification; warehouse check here found no confirmable resolution. The flag holds.
