---
reviewer: worm-canon-pedant
facet: state-updates
episode: b01c01
cycle: r1
date: 2026-05-19
verdict: revise
---

# Worm Canon Pedant — State-Updates Adversarial Reading

## Persona frame

Keeps a running tally. Reads with the wiki open in the other tab. Adjudicates rather than emotes. When a Taylor-side state entry fires, the question is: does this match how Taylor's capability actually works in source? Does the field track the right thing at the right granularity? Are the costs accounted for? When an entry makes a claim about what Taylor's insect-sense can do — its passive coverage radius, its automatic pattern-read initiation, its discipline under density spikes — this reader checks it against canon mechanics.

Fatigue trigger: if power mechanics exceed established limits without acknowledged reason, or if three errors accumulate in a scene, this reader files a mental report and reads at arm's length. One canonically precise moment can pull them back.

Hot-buttons directly relevant: power mechanics exceeding established limits without acknowledged reason; character knowing information they have no in-world path to knowing; voice register contradicting established personality.

---

## Per-entry adversarial pass

**Env entries [state-updates:1–5]**

Prop states, thermal ambient, occupancy. None of these are Worm-mechanics claims. `ALL ENV ENTRIES: CLEAN`

**[state-updates:6] @3 `actor:coll-net-mender-flea-bottom.block_baseline_new_faces`**
Non-Worm character; field tracks local social physics. `CLEAN`

**[state-updates:7] @2 `actor:taylor-hebert-kl-122ac.social-tether.coll-block-presence: none -> paying-resident-at-corner-room`**
Social status tracking. Not a power-mechanics claim. `CLEAN`

**[state-updates:8] @3 `actor:taylor-hebert-kl-122ac.knowledge.coll-as-vouching-vector: unmapped -> registered-as-block-fixture-with-verbal-contact`**

`coll-as-vouching-vector` — the field name implies Taylor has already assessed Coll as a potential social-license conduit. In Worm canon, Taylor's analytical register is high (she runs tactical calculations continuously) but her social-network modeling is not instantaneous. She takes time to map people's utility. The field name does not violate Worm mechanics directly — Taylor would register Coll's role — but `vouching-vector` as a first-contact field name implies her social-network-analysis mode is already active at @3.

The concern from this reader: is Taylor running social-vector analysis on block contacts at @3 (first verbal exchange) or is she registering presence and deferring the valence assessment? Canon Taylor is strategic but not instantly-categorizing. The field name at @3 is slightly ahead of where Taylor's social processing would realistically be.

`FLAG: [state-updates:8] field name [coll-as-vouching-vector] implies active social-vector analysis at first contact; canon Taylor processes tactically but not instantly-categorizes relationships as vectors; mild over-precision for a first-contact beat`

Convergence-trace: auditor r1/r2 no finding. Cape-fic-reader independently flagged same field-name issue. This reader's angle is Worm-register precision rather than board-coherence.

**[state-updates:9] @5 `actor:taylor-hebert-kl-122ac.work-role.coll-block: outside -> needle-handler-at-coll-block`**
Integration into block labor via tool-handoff. `CLEAN`

**[state-updates:10] @8 `actor:taylor-hebert-kl-122ac.insect-sense-discipline.active-holding: ambient-passive -> threshold-held-against-density-spike`**

This is the first Worm-mechanics check this reader runs seriously. `insect-sense-discipline.active-holding` is a field that tracks Taylor's behavioral management of her passenger's ambient sense output. In Worm source, Taylor's insect sense is passive by default — she receives insect-position data automatically within range, without effort, and she has to actively direct them to do anything different. The question here is: what is `threshold-held-against-density-spike`? Is this Taylor actively suppressing her passive sense (not canon — she doesn't do this; she always passively receives; suppression isn't a documented Taylor behavior), or is this Taylor managing her *processing* of the insect data (more defensible — she's not suppressing sense, she's managing attentional flood)?

The distinction matters. If `active-holding` means Taylor is suppressing her passive insect-sense to avoid overload, that is not how Worm's Taylor works — she doesn't turn off the sense, she manages what she does with it. If `active-holding` means she is managing attentional allocation (not directing bugs, not pattern-reading, just receiving passively without acting), that is canon-consistent.

The entry does not specify which interpretation it carries. `threshold-held-against-density-spike` could mean either. Given that the chapter-stated prohibition is about *pattern-reading* and *deployment* (not about receiving), the `active-holding` field should be framing management of *what Taylor does with* the sense, not whether the sense is on. The current framing is ambiguous.

Additionally, cite-index `state:10 @8 back=N` — the proto-line at @8 does not back-cite this entry.

`FLAG: [state-updates:10] @8 — "active-holding" framing is ambiguous between [suppression of passive sense] (not canon) and [management of attentional allocation / deployment decision] (canon-consistent); clarify field semantics; also back=N issue with @8 anchor proto-line`

Convergence-trace: cite-index `back=N` on state:10. Other reviewers flagged @8 anchor issue. This reader adds the Worm-mechanics interpretation ambiguity.

**[state-updates:11] @12 `actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively`**

Passive density mapping via insect-sense sweep. Canon Taylor gets positional data from her insects automatically — she knows where each bug is within range. `block-density-mapped-passively` correctly encodes this: she's not directing a sweep, she's receiving data from whatever bugs are on the block. The `passively` qualifier is canon-accurate.

Worm-mechanics check: what is Taylor's effective range in canon for passive insect-sense? Within a reasonable urban block (50–100m), Taylor's range is canon-supported; insect density in a city would give her substantial positional data. `CLEAN`

**[state-updates:12] @15 `actor:taylor-hebert-kl-122ac.knowledge.watch-patrol-cadence-hook: unknown -> patrol-pattern-read-passively`**

Canon-mechanics check: Taylor's insect-sense can passively register when a patrol passes through her coverage area (she'd feel the guards' bodies through her bug-sense if they pass within range, and she'd register their movement pattern). `patrol-pattern-read-passively` is canon-consistent as long as the Watch patrol passes through Taylor's insect-sense coverage area at @15. The proto-line establishes "the city-watch passes the hook" — they pass through. Coverage confirmed. `CLEAN`

**[state-updates:13] @18 `actor:taylor-hebert-kl-122ac.work-role.coll-block: needle-handler-at-coll-block -> recurring-needle-handler-coll-block`**

Not a Worm-mechanics issue. Work-role tracking. The `recurring` concern raised by other reviewers (forward-projection without anchor) applies here but this reader has no additional Worm-specific objection. Acknowledged but not primary for this reviewer. `ADVISORY`

**[state-updates:14] @22 `actor:taylor-hebert-kl-122ac.knowledge.wren-presence: unregistered -> face-with-voice-registered`**
First contact registration. `CLEAN`

**[state-updates:15] @24 `actor:taylor-hebert-kl-122ac.insect-sense-discipline.pattern-reading: auto-initiating -> caught-by-rule-not-deployed`**

This is the most Worm-canon-significant entry in the file. `pattern-reading` auto-initiating is a claim about Taylor's insect-sense behavior in this setting: the capability fires automatically before Taylor consciously decides to use it. In Worm canon, Taylor's power is not quite that autonomous — she doesn't run involuntary tactical analysis. Her power gives her insect positional data; the *analysis* of that data into pattern-reading is Taylor's cognitive work, not the shard's autonomous output.

However: this is a post-Gold-Morning Taylor. The chapter's substance contract establishes that Taylor arrived in Westeros after Khepri — after she ran a mass override event. The shard-residue at that scale may have changed how the capability interfaces with her cognition. The `auto-initiating` framing could be read as: pattern-reading has become more reflexive post-Khepri, a side-effect of the massive deployment, so it now fires before Taylor's intentional trigger. That is a plausible AU extension if the text acknowledges it as a departure from prior Taylor behavior.

This reader's question: does the substance contract for this project establish that Taylor's pattern-read is now auto-initiating (a post-Khepri change), or is `auto-initiating` an undeclared deviation from canon mechanics? If the former, this entry is canon-extension properly handled. If the latter, this is a power mechanic exceeding established limits without acknowledged reason — which is this reader's strongest hot-button.

The condition card `cond-khepri-residue-122ac` is listed in the series laws. The existence of that card suggests the project acknowledges Khepri-residue as a declared departure mechanism. If `auto-initiating` is a khepri-residue side-effect tracked under that condition, the extension is acknowledged. If the state-updates file is claiming auto-initiating as Taylor's baseline without citing the residue condition as the mechanism, it is an unmarked canon deviation.

`FLAG: [state-updates:15] @24 — "auto-initiating" pattern-read claims a behavioral change from Worm-canon Taylor (whose pattern-analysis is cognitive, not shard-autonomous); verify that [cond-khepri-residue-122ac] explicitly licenses auto-initiating as a post-Khepri residue effect; if not explicitly licensed, this entry requires a field-extension comment citing the condition card as the mechanism`

Convergence-trace: auditor r1 Earth-Bet fence findings covered vibes:17 (remediated) and vibes:21 (remediated), not this state-updates entry. This finding is new and specific to Worm-mechanics authority.

**[state-updates:16] @25 `actor:taylor-hebert-kl-122ac.relational-anchor-status.wren: stranger -> face-not-node`**

`face-not-node` is Taylor's prohibited-pattern: she refuses to operationalize Wren as a network asset. This is the prohibition operating correctly. Canon Taylor would categorize people in terms of their utility to her network; the prohibition catches that impulse. The field tracks the *refusal* rather than the categorization. Canon-consistent. `CLEAN`

**[state-updates:17] @26 `actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper`**

Not a Worm-mechanics violation in itself. The lag concern (knowledge fires at departure rather than acquisition) is relevant but is covered by other reviewers. This reader notes: Taylor's knowledge acquisition being triggered by Wren's departure is unusual for Taylor's information-processing style — she'd register the social-geometry inference during the conversation, not when the person walks away. `ADVISORY` (covered by other reviewers more specifically).

**[state-updates:18–20] Wren actor entries**
Location and awareness tracking. `CLEAN`

---

## File-level Worm-mechanics scan

The key Worm-mechanics claims in this file are:

1. Taylor's insect-sense operates passively within urban block range — `CANON-CONSISTENT`
2. Taylor can passively register patrol movement within her sense coverage — `CANON-CONSISTENT`
3. Taylor's `active-holding` discipline is a meaningful state that differs from ambient-passive — `AMBIGUOUS` (see entry 10)
4. Taylor's pattern-reading auto-initiates (fires before Taylor's intentional trigger) — `REQUIRES LICENSE VERIFICATION` (see entry 15)

The first two are clean. The third is ambiguous in framing. The fourth is the most significant Worm-mechanics question in the file because it makes a behavioral claim about Taylor's power that departs from source-canon behavior, and the departure needs to be anchored to the declared residue condition.

---

## Verdict

`revise`

**Named revision targets:**

1. `[state-updates:10]` — "active-holding" framing ambiguous between suppression (not canon) and attentional-management (canon-consistent); clarify field semantics; also unresolved @8 anchor (back=N).

2. `[state-updates:15]` — "auto-initiating" pattern-read is a departure from Worm-canon Taylor behavior; requires explicit citation of `cond-khepri-residue-122ac` (or equivalent license) as the mechanism; if the condition card licenses this behavioral change, add a field-extension comment citing it; without that citation, this entry is an unmarked deviation from canon power mechanics.

Advisory (not revision-blocking unless the license check fails):
- `[state-updates:8]` — field name precision; Worm-register concern.
- `[state-updates:17]` — acquisition-vs-departure timing; covered by other reviewers.
