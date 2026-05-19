---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 1
episode: b01c01
date: 2026-05-19
verdict: revise
---

# Verdict reasoning

The environment and prop entries are clean — no Worm-mechanics claims, no violations. The non-Taylor actor entries are clean. The Taylor-side entries have two problems that require adjudication, not advisory treatment. Entry 10 (`insect-sense-discipline.active-holding: ambient-passive -> threshold-held-against-density-spike`) uses "active-holding" in a way that is ambiguous between suppression of the passive sense (not canon — Taylor does not turn off her insects) and management of attentional allocation (canon-consistent). The ambiguity matters because the field will be written to canonical state and downstream chapters will read it; if it is read as "suppression," future authors will have a power-mechanics error baked into the record. Entry 15 (`insect-sense-discipline.pattern-reading: auto-initiating -> caught-by-rule-not-deployed`) makes a stronger claim: that pattern-reading fires before Taylor's intentional trigger, autonomously. In source, Taylor's pattern analysis is cognitive work, not shard-autonomous output. The `auto-initiating` framing is a departure from canon behavior, and the file does not anchor it to the declared residue condition (`cond-khepri-residue-122ac`). An AU departure from canon mechanics that names its mechanism earns tolerance; this one does not name it in the state-updates entry.

# Entry-level callouts

- [state:10] @8 `actor:taylor-hebert-kl-122ac.insect-sense-discipline.active-holding: ambient-passive -> threshold-held-against-density-spike` — "active-holding" is ambiguous between [suppression of passive sense] (not how Taylor's power works in source — she does not turn off insect reception) and [management of attentional allocation / deployment decision] (canon-consistent). The field as written will sit in canonical state and downstream authors will inherit it. If they read "active-holding" as suppression, they have a power-mechanics error from the start. The field semantics need to be explicit. Also: cite-index records `back=N` — the @8 proto-line does not cite this entry — so the anchor itself is unverified.

- [state:15] @24 `actor:taylor-hebert-kl-122ac.insect-sense-discipline.pattern-reading: auto-initiating -> caught-by-rule-not-deployed` — "auto-initiating" is a behavioral claim that pattern-reading fires before Taylor's conscious trigger. In Worm canon, Taylor's insect-sense delivers positional data automatically; the *pattern analysis* of that data is Taylor's cognitive work, not an autonomous shard process. The `auto-initiating` framing departs from that. If this is a post-Khepri residue effect — the shard's behavior altered by the scale of the Gold Morning override — it needs to say so. The warehouse condition `cond-khepri-residue-122ac` exists precisely to license departures of this kind, but this entry does not cite it. An unmarked deviation from canon power mechanics is this reviewer's strong flag. Either add a field-extension comment citing `cond-khepri-residue-122ac` as the mechanism for auto-initiation, or revise the framing to something that stays within source behavior.

# Convergence trace

- [state:10] @8: Cite-index `back=N` noted in the r1 audit data (state:10 appears with `back=N` in the index). The mechanical auditor did not flag the `back=N` on this entry in the CONSTRAINT pass; it was not enumerated in r2-verify. Cape-fic-reader and dark-fantasy-reader both independently flagged the @8 anchor issue. This reviewer's additional finding (active-holding ambiguity as a Worm-mechanics concern) has no auditor convergence — the mechanical audit did not reach this semantic question.
- [state:15] @24: The r1 auditor's Earth-Bet fence scan covered vibes:17 (remediated via `khepri-residue` renaming). The auditor did not scan state-updates field semantics for canon-mechanics consistency — the audit is structure and cross-facet, not Worm-canon accuracy. No auditor convergence. The condition card `cond-khepri-residue-122ac` is referenced in the exposition source field (r2-verify NOTE-FOR-NEXT-RUN on warehouse slug), but that reference is to the exposition facet's source field, not to this state entry's canonical field-semantics. No convergence.
