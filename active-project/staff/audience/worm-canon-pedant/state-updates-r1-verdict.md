---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 1
episode: b01c01
date: 2026-05-23
verdict: revise
---

# Verdict reasoning

Earth-Bet hard-fence scan confirms 0 hits in actual target/old/new field text — the auditor's 0-hit report holds. The "patrol-rotation" string the auditor quotes in fault-012 as the state:10 `<new>` value does not appear on disk; the on-disk value is `flea-bottom-block-level-day-count-complete`, which is clean. However, the auditor-quote discrepancy means fault-012 was adjudicated against a value that does not exist in the file, leaving the substantive cross-facet alignment question at state:10 resolved by a mismatch between what the auditor read and what is on disk — that is not a cleared finding, it is an unresolved one. Separately, `knowledge.ward-geometry` as a field name sits in the double-register zone: "ward" is Westerosi-authentic as a city-district term AND is the PRT cape-program term Taylor carried from Earth-Bet; a displaced Taylor naming her own knowledge-tracking axis "ward-geometry" without the narrative distinguishing which register is active is a lore-leak candidate, not a confirmed hit, but it warrants a documented decision rather than a silent pass.

# Entry-level callouts

- [state:10] @20 — The auditor's fault-012 quotes the `<new>` value of this entry as `flea-bottom-block-level-with-patrol-rotation`, but the on-disk entry reads `flea-bottom-block-level-day-count-complete`. These are not the same field state. The fault-012 finding (NI content-alignment gap: narrator:7's ledger-close register does not license the specific field mutation) was adjudicated against the wrong value. The on-disk value (`day-count-complete`) aligns better with narrator:7 ("the day closed under the count she had been running") than the auditor's quoted value would — which means the content-alignment gap fault-012 identifies may be overstated for the on-disk state. But this also means the auditor's fault-012 criteria ("either narrow the state:10 field mutation or expand narrator:7's text to name the patrol-rotation") is directing a fix against a value that does not exist. The entry cannot be cleared as clean or patched as fault-described until the value discrepancy is resolved: confirm which version is canonical, rebuild the NI alignment check against the actual on-disk value.

- [state:9] @9 — `actor:taylor-hebert-kl-122ac.knowledge.ward-geometry: null -> flea-bottom-block-level-passive`. The field name `ward-geometry` sits in a double-register: in ASOIAF, a "ward" is a city-district (Flea Bottom is a ward of King's Landing — Westerosi-authentic); in Worm, "Ward" is the PRT cape program Taylor explicitly was not part of but spent years adjacent to. A displaced Taylor from post-Khepri arc running Planetos-block discipline would carry both registers simultaneously. The field name is not confirmed as an Earth-Bet leak — Westerosi usage is valid here — but the file contains no documented choice: nothing in the entry or its comment says "ward here = Westerosi city-district, not PRT." The worm-canon-pedant requires either a documented disambiguation comment or a field-name change to something unambiguous (e.g., `knowledge.block-geometry` or `knowledge.quarter-layout`). An unmarked vocabulary collision in a canonical state field that persists into downstream episodes is exactly the kind of thing that produces lore-drift without acknowledgment. Rule: AU variants that name their divergence earn tolerance; unmarked ambiguity does not.

# Convergence trace

- [state:10] auditor overlap: fault-012 (HARD — NI content-alignment gap). My callout adds a layer fault-012 does not: the auditor-quoted `<new>` value does not match the on-disk value, meaning fault-012's specific repair criteria are mis-targeted. The auditor's mechanical scan caught the co-citation content gap; I am flagging that the gap was scanned against a ghost value.
- [state:9] no auditor overlap. The Earth-Bet hard-fence scan returned 0 hits (auditor confirmed, I confirmed); the `ward-geometry` field name is not a hard-fence hit but is a double-register flag the mechanical scan does not catch because the term is valid in both registers. This is exactly the seam between mechanical scan and adversarial reading.
