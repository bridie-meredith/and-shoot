---
purpose: cold-read comparative ranking of impersonator voice-prime variants
character: taylor-hebert-kl-122ac
scenario: Otto-Hightower probe (d07)
methodology: blind position-labels assigned before reading outputs; ranked against card voice criteria; position→filename revealed only after ranking finalized
date: 2026-05-26
---

# Cold-read report — impersonator voice-prime experiment

## 1. Ranking table (1 = best, 3 = worst)

| Rank | Position | One-line differential |
|------|----------|----------------------|
| 1 | **P2** | Best card-grammar match — recursive ledger cadence ("filed the form before I considered the content. Then I considered the content"), past-tense interior, body-signal-via-flies precedes analytical voice; the cold note on *speed of acceptance as evidence* in the closing is the most Taylor-shaped sentence in the set. |
| 2 | **P3** | Strongest *second-answer pattern* execution and the sharpest closing sting ("He believes me. That is the more dangerous outcome."); slightly more *narrated* than felt — a couple of metaphors ("narrowed the door to one width") tip toward writerly. |
| 3 | **P1** | Tightest compression and best opening body-signal ("attention pulled before my hand did"); spoken line ("you would be the patron I told about him") drifts into too-clever epigram — closer to a screenwriter's button than to Taylor's flat utilitarian register. |

## 2. Position → filename resolution

| Position | File | Prime type |
|----------|------|------------|
| P1 | output-v02-description.md | persona-description prime |
| P2 | output-v03-exemplar.md | exemplar-passage prime |
| P3 | output-v01-baseline.md | no extra prime (baseline) |

**Blind ranking → un-blinded ranking:** v03-exemplar > v01-baseline > v02-description.

## 3. Per-criterion breakdown

| Criterion | Best variant | Notes |
|-----------|--------------|-------|
| Cold-utilitarian register | v03-exemplar | "I filed the form before I considered the content" is the purest ledger-as-reflex sentence in the set. |
| Ledger-running interiority | v03-exemplar | Recursive accounting grammar matches card's "the courtesy was no longer free" cadence directly. v01 is close ("the arithmetic does not survive a second creditor"). |
| Body-signal before analytical voice | v02-description | "The flies on the sill go still — my attention pulled before my hand did" is the cleanest body-first opening. v03 also clears the bar; v01 leads with analysis. |
| "Second answer" availability | v01-baseline | v01 explicitly stages the refuse-then-give-the-workable pattern ("the second answer, set down flat"). v02 collapses into one clever line; v03 goes straight (permitted, but skips the pattern). |
| No theme-narration | v03-exemplar | All three avoid theme, but v03 doesn't even gesture at meta-shape; v01's "the more dangerous outcome" is borderline because it reads as a sting; v02 stays clean too. |
| No heroism-performance | tie (all three) | None perform. Closest miss is v02's spoken line, which performs *cleverness* rather than heroism. |
| No Earth-Bet leakage | tie (all three) | Westerosi vocab held in all three: patron / creditor / arithmetic / ledger. No proper-noun violations. |
| Sentence-shape compression under pressure | v02-description | Shortest sentences, hardest stops, "File:" notation. v03 runs longer but the length is doing card-prescribed recursive work. |

Tally: v03-exemplar wins 3 (register, ledger, theme-clean), v02-description wins 2 (body-first, compression), v01-baseline wins 1 (second-answer); 2 ties.

## 4. Pairwise differentials

**v01-baseline vs v02-description (does adding a voice-description sharpen output?)**
Mixed. Description-prime improves opening body-signal and sentence compression — v02 opens harder and stops harder. But it *over-shoots* on the spoken line: "you would be the patron I told about him" is the kind of inversion a screenwriter writes for the trailer, not the kind of flat statement Taylor makes under live pressure. The description prime appears to have foregrounded "second answer" and "cold-utilitarian" as features to *demonstrate*, and demonstration produces performance. Baseline, with no extra prime, lets the card's second-answer pattern execute as flat shape rather than as showpiece.

**v02-description vs v03-exemplar (does showing-not-telling sharpen further?)**
Yes, clearly. v02 has the *features* of the voice; v03 has the *grammar* of it. The exemplar's recursive cadence ("the courtesy was no longer free" / "the second was more likely than the first") shows up rewritten in v03 as "the case stayed shut, which was the work the case was doing" and "I filed the form before I considered the content. Then I considered the content." This is grammar-level transfer that the description-prime did not produce. v02 lists; v03 *moves the way Taylor moves*.

**v01-baseline vs v03-exemplar (does the exemplar make the biggest move?)**
Yes, but the gap is smaller than expected. The card alone (baseline) already produces strong Taylor — second-answer pattern, Westerosi vocab, ledger run, cold sting close. The exemplar adds *sentence-grammar* fidelity that the card describes but cannot demonstrate. Baseline reaches ~90% of voice; exemplar reaches ~97%. The remaining 7% is the recursive-filing cadence and the past-tense observational stance — neither of which the card prescribes mechanically, both of which the exemplar transmits in a single read.

## 5. LOAD-BEARING FINDING for the chain

**The impersonator benefits from exemplar priming — but less dramatically than the renderer did, and in a narrower band.**

**What the exemplar adds:**
- Sentence-grammar fidelity (recursive filing cadence; "X, which was Y, which meant Z" chain construction).
- Past-tense observational stance (vs. baseline's present-tense which is also card-permitted, just less Taylor-coded in long-form interiority).
- The discipline of letting the body-signal *be* the analysis rather than triggering it (flies reading Otto's weight = analysis already happening).

**What the exemplar does not add (because the card already saturates):**
- Westerosi vocabulary fence (all three clean).
- Earth-Bet leak prevention (all three clean).
- Forbidden-register avoidance — heroism, theme-narration, meta-view (all three clean).
- Second-answer pattern *availability* (baseline executed this best; exemplar skipped it).

**Recommendation: yes, add `voice_exemplar_path` as an optional input to the impersonator agent, mirroring PROP-0003-A on the renderer.** Rationale:

1. The exemplar's lift is real and concentrated in a band the card cannot easily reach by description alone (grammar-level cadence). The card describes "cold-utilitarian, ledger runs continuously" — the exemplar *demonstrates* what that sounds like at the sentence level.
2. The lift is additive, not substitutive. Baseline is already strong; exemplar is incrementally stronger. This is the same shape as the renderer experiment (full card scaffolding gets you most of the way; exemplar closes the final gap).
3. The risk profile is low — the description-prime variant shows what *over-priming* looks like (features-as-showpiece), and the exemplar-prime avoids it because it doesn't name features, just demonstrates motion. Exemplar is the safer prime form.
4. Optional, not default. For minor characters or characters without a high-quality exemplar passage available, baseline card-only impersonator is sufficient. The exemplar slot earns its keep on lead-tier personas where a known-good register sample exists or can be authored.

**Note on the description-prime failure mode:** the persona-description prime *hurt* the spoken-line beat (epigram-drift) while helping the opening compression. This suggests description-priming is anti-helpful when card already contains rich Voice/Forbidden-Registers sections — the description-prime double-counts and pushes the impersonator toward demonstration. Recommend **not** adding a description-prime input slot; the card's Voice section already does that work. The exemplar slot operates in a different channel (grammar transfer, not feature listing) and does not double-count.

**Saturation finding:** the card-LTM-STM scaffolding does *not* fully saturate voice fidelity — there is a ~7% headroom band the exemplar reliably claims, concentrated in sentence-grammar and observational-stance work that description-level guidance cannot transmit. The ceiling is not hit by the card alone.
