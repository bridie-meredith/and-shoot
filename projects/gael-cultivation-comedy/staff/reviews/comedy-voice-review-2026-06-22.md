# Comedy Voice Review — *gael-cultivation-comedy*

**Date:** 2026-06-22
**Reviewer:** main session (read-only audit; no story development)
**Scope:** the voice channel of the comedy — the nine `persona-exemplars/` (the live Tier-1 voice
primers, Rule 16) read against the comedy architecture in `intake/spine.md`, the foil design in
`intake/character-reactions.md`, the cast in `actors/`, and the canon-of-record in
`intake/CHARACTER-LAYER-INDEX.md`.
**Status of this project:** frozen provenance archive — migrated to `and-write` on 2026-06-14
(`MIGRATED-TO-AND-WRITE.md`). This is an **advisory** review; the live exemplars now live in
`and-write → projects/gael-cultivation-comedy/persona-exemplars/`. Fixes should be applied **there**,
not here. This report is the punch-list to carry across.

---

## Verdict

**The voice *design* is strong; the voice *roster* is not wired to the live cast.**

The two lead exemplars (Gael, Wylla) are excellent — distinct, on-spec, Rule-22-compliant, well-fenced —
and the craft across the whole standby set is genuinely high (each register is sharply differentiated).
But **only 2 of the 9 exemplars bind to a live cast slug.** The other seven are either stale pre-rename /
span-B artifacts or unbound register-references, and **all nine — including an explicitly superseded one —
are flagged `dispatch-status: active`**, so the status field carries no signal. Meanwhile the cast members
who power the funniest *recurring* comedy — the three antagonist faces and the interlude narrator — have
**no exemplar at all.**

Net: not production-blocking for the leads, but the supporting/antagonist voice layer is under-specified
and the exemplar directory is mislabeled. Address F1–F3 before live chapter production in `and-write`.

---

## What's working (keep)

- **Gael (`gael-targaryen.md`) — PASS, exemplary.** Breezy, deflecting, monomaniacal; concrete-action-first;
  grimdark deflected *through the lens* (the man to the black cells is "a him problem"); the trope-dodge +
  self-audit construction is right there in 225 words. The fences carry the **Rule-22 HARD** note and the
  `supersedes: saerys-targaryen-exemplar` link. This is the model the rest should match.
- **Wylla (`wylla-maid.md`) — PASS.** Plain-warm smallfolk Common Tongue + half-understood convert lingo
  ("I wrote *in balance* at the bottom and underlined it"), deadpan-on-the-impossible, and the
  dramatic-irony of devotion-to-a-sect-with-no-future. Cleanly distinct from Gael; the deuteragonist
  channel is voiced.
- **Register differentiation is a real strength.** Across the standby set the registers do not blur:
  mechanism-first counter-thesis (Daenys), flat anthropological witness (Nymeria), riddle-naturalist
  (Helaena), bone-dry incident-log (Harwin), precision-under-alarm report (the septa), indulgent-paternal
  "spirited-child filter" (Viserys). Whoever authored these can clearly hit a target; the problem below is
  *aim*, not *craft*.

---

## Findings (classified)

### F1 — Exemplar roster ↔ live cast drift *(HARD; production-readiness)*
Live cast (`CHARACTER-LAYER-INDEX.md`): leads **gael · wylla**; antagonist faces **jaehaerys · otto ·
septon-barth**; narrator **alicent**; foils **maester-lorren · septa-aldith · hobb · daemon**; plus
`the-factor` + three chambermaids in `actors/`.

Exemplars present: gael ✓, wylla ✓, **saerys-targaryen, saerys-septa, viserys-i-targaryen,
helaena-targaryen-122ac, daenys-velaryon, nymeria-summer-isles, ser-harwin-the-patient** — **7 of 9 bind
to no live cast slug.** Of the ten live cards, **eight have no exemplar** (everyone but Gael and Wylla).
Because Tier-1 resolution keys on the persona slug (Rule 16), the slug mismatch *prevents auto-misfire* —
but it also means the considerable register work in the standby files is **stranded under dead slugs**
while the live personas resolve to *absent*. The voice exists; it just isn't wired to the cast.

### F2 — `saerys-septa.md` and `saerys-targaryen.md` are stale, mislabeled active *(HARD)*
Both reference tombstoned personas (`saerys-targaryen → gael`, `saerys-septa → septa-aldith`, per the
index). `saerys-targaryen.md` at least carries `superseded_by: gael-targaryen-exemplar` — yet **still says
`dispatch-status: active`.** `saerys-septa.md` carries **no** superseded marker at all and is `active`,
even though its persona-ref is retired. The septa's register work (precision-under-alarm, the correct
report that won't land — a genuinely good fit for **septa-aldith**) is stranded under the dead `saerys-`
slug. **Fix:** retire both (`dispatch-status: superseded` + `superseded_by`), and re-home the septa
register to a new `septa-aldith.md` if that voice is still wanted.

### F3 — `viserys-i-targaryen.md` is a span-B artifact with reassigned DNA, mislabeled active *(HARD)*
The index lists `Viserys-father` among the stale `saerys-*`/span-B tombstones, and
`character-reactions.md` is explicit: the `viserys-i` card's **warm-cage / "spirited-child filter" DNA was
split and reassigned to Alicent**, with a standing reconciliation fence *not* to carry it forward as-is.
The current father is **Jaehaerys — the cold/institutional face**, not a warm indulgent paternal. The
exemplar sits in the directory `dispatch-status: active` with no superseded marker. The slug mismatch
again prevents auto-misfire, but the warm-paternal register belongs on **Alicent**, not on any father
slug. **Fix:** retire it; fold its usable warmth into an Alicent exemplar (see F6).

### F4 — Helaena / Daenys / Nymeria / Harwin are unbound register-references *(SOFT)*
None appear in `character-profiles.md`/`character-reactions.md` as bound to a live role; Helaena's role is
an explicit **open/parked slot**. These read as library-grade register-reference cards, not project
exemplars — but they're `dispatch-status: active` in a *project-bound* directory, which overstates their
status. **Fix:** either bind each to a live slug (e.g. evaluate the bone-dry-list Harwin register for
`maester-lorren`; the mechanism-first Daenys or flat-witness Nymeria for `the-factor`) **or** demote to
`dispatch-status: reference` / move to the library so they don't masquerade as live cast voices.

### F5 — Rule-22 ledger-register: cumulative-texture watch *(SOFT)*
Rule 22 / DEC-0115 retires the ledger/accounting/apparatus register **as the narrator's prose mode**. The
POV layer is clean: the retired ledger voice (`saerys-targaryen.md`) is correctly superseded by Gael's
concrete-action-first exemplar, and Gael's own voice note reinforces "the bestiary is a *prop we cut to
for the joke,* not the prose voice." **But** the reverse-angle format concentrates *documentary* channels
(the maester's Citadel letters as Greek chorus, the septa's reports, Harwin's incident-log), and three
standby exemplars are themselves list/report registers. Each is individually licensed as character/channel
— the ban is on narration, not on a clerk speaking like a clerk — yet the *cumulative* chapter texture
could drift back toward ledger-feel if documentary channels stack. **Recommendation:** have the
`/and-stitch` Phase 9 naive-follow / cold-read explicitly watch documentary-channel *density* per chapter,
not just the POV line.

### F6 — The marquee recurring comedy has no voice exemplar *(NOTE; high-value)*
The two funniest *every-chapter* engines — **Alicent's "what the hell"** (interlude narrator; the warm,
hopelessly-wrong maternal read) and **the three antagonist faces "breaking"** (Jaehaerys's control-plays
dissolving; Otto's scheme that won't close; Barth's theory one fact short) — have **no exemplar**. The
index itself lists "exemplars for the three antagonist faces (impersonator-Tier-1 eligible)" as pending
option 2. For voice fidelity on the beats the reader will laugh at most, these should be authored before
live production. Alicent is the natural home for the reclaimed `viserys-i` warm-cage DNA (F3); Barth is
cleanly seated (Hand 82–98 AC) and the easiest face to voice first.

---

## Recommended actions (prioritized; apply in `and-write`)

1. **Hygiene pass on `dispatch-status` (F2/F3).** Set `saerys-targaryen`, `saerys-septa`, `viserys-i` →
   `superseded`/`retired` with `superseded_by`. The field currently says `active` on all nine — make it
   mean something.
2. **Author the four missing load-bearing voices (F6 + F1):** `alicent-hightower` (absorbing the
   reclaimed warm-cage DNA), `septon-barth`, `jaehaerys-i-targaryen`, `otto-hightower`. These four carry
   the antagonist/narrator comedy.
3. **Resolve the standby set (F4):** bind Harwin/Daenys/Nymeria to live foils (`maester-lorren`,
   `the-factor`) where the register fits, or demote to library/reference. Re-home the septa register to
   `septa-aldith`.
4. **Wire the Rule-22 texture watch (F5)** into the stitch cold-read for documentary-channel density.

## Not changed
No story content, cards, or exemplars were modified — this project is the frozen pre-migration archive.
This report is advisory provenance to carry into `and-write`, where the live voice work continues.
