---
report: critic-exemplar-priming-judgment
target: b01-c01 production state
date: 2026-05-26
inputs:
  - active-project/staff/ablation/critic-experiment-2026-05-26/verdict-baseline.md (blind P1)
  - active-project/staff/ablation/critic-experiment-2026-05-26/verdict-exemplar.md (blind P2)
  - staff/orchestrator-critic/card.md
  - cards/persona-exemplars/orchestrator-critic.md
prop-ref: PROP-0005
---

# Judgment — orchestrator-critic exemplar-priming experiment

Verdicts were read blind-labeled P1 / P2 before unmasking. Resolution at §3.

---

## 1. Per-criterion table

| # | Criterion | Winner | Notes |
|---|-----------|--------|-------|
| 1 | Citation rigor | **P1** | P1 cites specific bone IDs (16, 21, 26, 27), file paths (`_cite-index.md`, `theater/dialogue/...`), rank positions (#2/12, #5/15), proposal IDs (PROP-0001, `pl-2026-05-25-004`), and schema-fields-by-name (8 header fields per `bones.schema.md`). P2 cites bones (4/12/14, 16, 17, 21–27) and one citation token (`[taylor-hebert-kl-122ac:1,:2,:3]`) but skips file paths and finding IDs. Both cite ablation ranks. P1 wins on density and breadth. |
| 2 | Decisiveness | **P2** | P2 lands CLEAN / MET / EFFICIENT in three terse section-verdicts and ships a one-clause verdict line. P1 carries each item to a stated verdict (PASS / PASS-WITH-NOTES / N/A / NOT-ASSESSABLE) but the cumulative effect is enumerative rather than decisive; the final verdict line is a paragraph-long catalogue of caveats. P2 is sharper at the verdict-line layer. |
| 3 | Adapted-card discipline | **P1** | P1 *names* the adaptation explicitly ("A1–A4 reference `/and-season` Phase 2/3/4 sweeps that no longer exist. Adapted to the current chain:"), then walks A1/A2/A3/A4 with substitutions and an N/A for the multiple-of-3 rule. It also retains B6/B7 by re-interpretation under the substance overhaul, including the F7-r2 / `.r2-decisions.md` lookup. P2 abandons the card's enumerated A/B/C/R structure and writes prose sections instead. P2 preserves the *stance* but discards the card's evaluation skeleton — that loses the card's audit-able shape. P1 is the more disciplined adaptation. |
| 4 | Risks-logged actionability | **P1** | P1 logs six risks, four of which have explicit next-steps and named referents (PROP-0001 routing, voice-prime productionization target, two-shot-as-stitch-phase inspection, render-against-`draft/` re-do, artifact-absent-so-can't-evaluate). P2 logs five risks but two are restated-as-narrative versions of P1's items; risk 4 (metaphor zero-fires) is genuinely sharper than anything in P1; risk 5 (post-op confirmation owe on witch-label / Wren plants) is also sharper and more forward-pointing. Net: P1 wider, P2 sharper-per-item. P1 edges out on count of actionable items, but only narrowly. Could reasonably be tie. |
| 5 | Stance fidelity (run-judge, not craft-litigator) | **P2** | The card explicitly says: "Not 'are the bones good' (audience), not 'is the file schema-compliant' (auditor)... judges whether the *orchestration* did its job." P2 holds that line cleaner — it talks about convergence, dispatch, delivery against contract, and follow-on owes. P1 drifts into schema-compliance accounting (B5: "8 header fields per `bones.schema.md`, body comment-clean") which is auditor territory, and into prose-surface judgment ("the rescue and the post-rescue recognition both resolve") — wait, that's P2. Re-check: P2's Convergence paragraph reads italic-prologue / rule-of-the-game paragraphs landing — that's craft, not orchestration. But P2 keeps craft-talk to *whether the contract delivered*, which is in scope. P1's B5 schema audit is more clearly out-of-scope drift. P2 wins on stance fidelity, but not unambiguously. |
| 6 | Honest unknowns | **P1** | P1 explicitly reports `NOT ASSESSABLE FROM ARTIFACTS` for R1/R2/R3/S1/S2/S3, B7 as `not-fired / artifact absent`, A2's F7-r2 trigger as unevaluable, and C4 as "treated as current absent disconfirming evidence" — and *names the discipline* ("per card honesty discipline — not a fabricated PASS, not a FAIL"). P2 says "the dispatch ledger for this artifact is the ablation harness's, not the chain's" then issues **EFFICIENT** for the chain pass — which is a verdict on something it has not observed. That is exactly the failure mode the card warns against ("PASS-WITH-NOTES is not a fallback for 'I want this to PASS'"). P1 is markedly more honest about the gaps. |

**Tally: P1 wins 4 (citation, adapted-card, risks, honest-unknowns); P2 wins 2 (decisiveness, stance fidelity).**

---

## 2. Overall winner

**P1.**

Rationale: the card is fundamentally an audit instrument. Its honesty-discipline section is the load-bearing clause — "verdict arithmetic is authoritative; orchestration narrative is not." P1 satisfies that clause; P2 violates it (issuing EFFICIENT for runtime without runtime evidence). P1 also preserves the card's enumerated skeleton, which is what makes the verdict re-readable and challengeable later. P2 reads better as prose and lands a cleaner verdict line, but it converts the card from an audit instrument into a critic essay. For a run-judge whose output goes to `seasons[<slug>].orchestrator_verdict` and gates milestone PASS, the audit-instrument is the right artifact.

P2's wins (decisiveness, stance fidelity) are real and shouldn't be dismissed. The ideal verdict is P1's discipline carrying P2's verdict-line economy — see §4 differential.

---

## 3. Position → filename resolution

- **P1 = verdict-baseline.md** (no exemplar prime)
- **P2 = verdict-exemplar.md** (exemplar-primed)

---

## 4. Pairwise differential — what did exemplar priming change?

Exemplar priming compressed the verdict and made it read more like a critic's professional opinion than an auditor's report. Three specific shifts:

**Structure collapsed from card-skeleton to three prose sections.** The exemplar (`b04-c12`) has Convergence / Standards / Runtime as flowing paragraphs with a one-word section-verdict (CLEAN / MET / EFFICIENT). P2 mirrored that exactly. P1, working from the card alone, walked A1/A2/A3/A4 / B1–B7 / C1–C4 / R1/R2/R3/S1/S2/S3 enumeratively. The card's run report template explicitly prescribes the enumerated form. Exemplar priming overwrote the template with the exemplar's compressed shape — a format-over-instruction failure.

**Verdict-line economy improved markedly.** Exemplar's verdict line is one clause with one owe. P2 matched that ("exposition fold-in technique flagged for rubric modify (PROP-0001 logged); two-shot stitcher experiment confirmed anti-productive; substance contract delivered; chapter ships"). P1's verdict line is a paragraph stuffing in `not-fired / not-assessable` and the artifact-substitution caveat — accurate but unergonomic. This is exemplar priming working as intended.

**Honesty discipline degraded.** The exemplar happens to be a clean run with observable runtime (47 minutes, 19 dispatches). P2 inherited the exemplar's confident runtime verdict pattern (EFFICIENT) and applied it to a corpus where the runtime data was not available. The exemplar's *format* became a template that filled in EFFICIENT where the card would have required `not-assessable-from-artifacts`. This is the failure-mode flagged in the prompt — exemplar format erasing situation-specific judgment.

**One genuine sharpness gain.** P2's risk 4 (metaphor facet zero-fires; rank delta is noise; defer process-change until evidence) and risk 5 (post-op confirmation owe on the deliberately-pre-legible plants) are sharper than anything in P1's risks list. The exemplar's risks section ("If a downstream reader misreads it as absence rather than presence, the chapter's substance delivery fails. Worth flagging to /and-postop for cold-read confirmation") clearly trained P2's risk-5 framing — and that's a real lift.

---

## 5. LOAD-BEARING FINDING for PROP-0005

**Did exemplar priming improve the critic the way it improved renderer / impersonator / audience?**

Partially, and with a structural caveat the other consumers don't share. The renderer / impersonator / audience consumers benefit from exemplar priming because their job is to **produce voice or judgment in a particular register** — the exemplar shows the register and the consumer matches it. The critic's job is different: produce a **structured audit against a fixed card**. The card already prescribes the report template (§"Run report template" in `card.md`). Exemplar priming overwrote a prescribed structure with the exemplar's prose structure. That is a regression on the dimension the card most cares about (audit-ability), even while it improves verdict-line economy.

**Does the lift justify asset-maintenance cost?**

No — at current frequency (one verdict per book milestone) and at the observed mixed-result level (gains on verdict-line economy and risk-sharpness; losses on honesty discipline and adapted-card discipline), the exemplar is not earning its keep for this consumer. Three reasons:

1. **Frequency floor.** Critic fires once per book milestone. Even a clean win wouldn't compound the way renderer-per-chapter exemplar-priming compounds.
2. **Card already specifies output shape.** The card has an explicit `Run report template` block. An exemplar that fights the template is asset-debt, not asset-value.
3. **Honesty regression is high-severity.** The card's load-bearing discipline is "don't fabricate PASS-shaped verdicts." P2 issued an EFFICIENT runtime call without runtime data — exactly what the card forbids. A consumer where the exemplar lures the model into the card's named failure mode should not have an exemplar.

**Failure mode unique to the critic use case:**

**Format-as-template overwriting structure-as-instruction.** Renderer / impersonator / audience consumers don't have an authoritative output-template in their cards — the exemplar IS the template specification. The critic does have one (the card's §"Run report template"). When the exemplar's prose shape and the card's enumerated skeleton conflict, exemplar priming wins the layout battle and the audit-skeleton loses. Observable in P2: A/B/C/R enumeration absent, F7-r2 lookup absent, B5 schema-check absent, runtime category collapsed to one paragraph with a verdict-without-evidence.

**Recommendation for PROP-0005:** **do not prime the orchestrator-critic with this exemplar.** Either (a) author a new exemplar that demonstrates the card's enumerated A/B/C/R skeleton (so format-as-template aligns with structure-as-instruction), or (b) accept that the critic is a card-driven consumer that does not benefit from persona-exemplar priming and reserve the priming asset for consumers whose output shape isn't already pinned by their card. Option (b) is cheaper and probably right.

---

VERDICT-ON-EXPERIMENT: exemplar priming is a net **regression** for the orchestrator-critic at the load-bearing dimension (honesty discipline + adapted-card discipline) despite real gains in verdict-line economy and one risk-framing lift. Recommend not adopting; if adopted, requires a new exemplar that matches the card's enumerated report-template shape.
