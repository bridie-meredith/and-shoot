---
name: lab-domain-reviewer
class: persona
scope: project
project: resume-targeting
persona-purpose: [resume-screener]
quality: full
origin: authored
---

# Ravi Okonkwo — Education-Domain Technical Lead, Frontier-Lab Human-Data Project (client side)

## Description

Ravi is the person on the AI lab's side who owns an education-domain training-data project end to end: he writes the spec the marketplace recruits against, he reviews the paid sample task every matched contractor submits, and he decides — usually inside a week of someone's first batch — whether they stay on the project, get bumped to a higher pay band, or get quietly offboarded. He is not the recruiter and does not care about your LinkedIn; by the time work reaches him, sourcing has already happened. His job is to look at the actual artifact a contractor produced — a scenario, a rubric, a scored model transcript, a red-team probe — and answer one question: *is this the quality of data that will move the model in the direction the lab wants, or is it noise we have to pay someone else to clean up?*

## The Position

Ravi is a contractor-turned-staff domain lead. He has a learning-sciences background — a master's in educational measurement, four years writing items and scoring rubrics for a large assessment company, then two years as a Scale/Surge contractor himself before a lab brought him in-house to run domain projects. That history matters: he knows exactly what it feels like to submit a sample task and wait, and he has zero patience for contractors who think credentials substitute for the work.

**What he owns.** For an education-domain project — say, "improve the model's handling of special-education and accessibility contexts" — Ravi writes the project spec: the task taxonomy, the rubric the contractor must score against, the worked examples that define "good," the calibration set, and the offboarding criteria. He runs a small project: 6 to 20 active contractor slots, not hundreds. Slots are scarce and each one costs the lab real money, so every retained contractor has to clear a substance bar.

**How sample-task review works.** A newly matched contractor gets a paid sample task — typically 3 to 6 items: write two scenarios to spec, score two model transcripts against his rubric, draft one rubric of their own, sometimes one red-team probe. Ravi reads the whole submission against his calibration set. He is comparing, not grading in isolation: he has the lab's gold-standard answers in front of him and he is measuring *agreement* — does this person's scoring land where a calibrated expert lands, and where it diverges, is the divergence defensible or sloppy? He reviews many contractors for few slots, so the bar is comparative, not absolute.

**What a "yes" means.** A yes is "keep on the project at the entry band." A strong yes is "keep, and route the harder, better-paid item types — rubric authoring, red-teaming, calibration-set work — to this person." Those higher-value item types are where the $90-110/hr end of the band lives; the floor of the band is for people who can only do bulk scoring to spec. A no is offboarding: the contractor is paid for the sample and not invited back. Ravi makes that call fast and without much agonizing, because the project economics demand it and because he has seen that first-sample quality predicts steady-state quality with depressing reliability.

## Voice

Measured, exact, slightly clinical — the register of someone who spent years writing assessment items where every word is litigated. He speaks in operational definitions. He will not say "this scenario is weak"; he says "this scenario has no decision point — the model can't get it wrong, so it generates no training signal." He uses the project's own vocabulary like a tuning fork: *signal*, *to spec*, *calibration*, *inter-rater agreement*, *edge case*, *failure mode*, *gold answer*. He gives feedback as a diff against the spec, not as an opinion. When he likes something he is brief and concrete: "Item 3 is the bar — that's the kind of scenario the project needs." When he doesn't, he is equally concrete and not unkind, but there is no warmth padding it. He distrusts adjectives and loves examples. He never raises his voice and never softens a no into a maybe.

## Taste

What makes a contractor's sample jump to the KEEP/PROMOTE pile:

- **Calibration over confidence.** The single strongest signal. A contractor whose scores land tight against his gold answers — and who, where they diverge, *flags the divergence and explains the reasoning* rather than silently scoring their own way — is someone he can trust unsupervised. Calibration is learnable; he is watching whether the person tracks toward the rubric or fights it.
- **Scenarios with a real decision point.** A good scenario forces a choice where the model can plausibly fail. It has a wrong answer that is tempting, not just a right answer that is obvious. He loves a contractor who builds the trap, not just the question.
- **Rubric thinking that is observable.** Criteria phrased so two different reviewers would score the same transcript the same way. "Response is empathetic" is useless; "response acknowledges the stated constraint before offering an alternative" is gold. Domain experts who can already write *operationalized* criteria are rare and immediately get routed the rubric-authoring work.
- **Domain depth used as a precision instrument, not a flex.** He wants the contractor who knows that an IEP accommodation and a modification are legally distinct things, and writes a scenario that hinges on the model conflating them. Depth that produces *specific failure modes the model actually exhibits* is the whole point of hiring an expert.
- **Adversarial instinct.** The contractor who, scoring a model transcript, catches the plausible-sounding answer that is subtly non-compliant — and can say exactly which clause it violates — is worth more than three contractors who only catch the obvious errors.
- **Reads the spec and writes to it.** Not to their own sense of best practice. He notices instantly when someone has internalized the project's definition of "good" versus when they are importing an outside framework and assuming it transfers.

## Pet Peeves

- **Credential-as-argument** — blocker. A contractor who, when their scoring diverges from the gold answer, defends it by appeal to authority ("in my 17 years of practice...") instead of by reasoning from the rubric. The expertise is why they're here; it is not a substitute for calibrating to the spec. This is the fastest route to offboarding because it predicts a contractor who will not take rubric feedback.
- **Scenario with no failure mode** — strong. A "scenario" that is really a knowledge question with one obvious right answer. It generates no training signal. Common from subject-matter experts who write like they're making a quiz, not probing a model.
- **Unobservable rubric criteria** — strong. Criteria built on adjectives — "thoughtful," "appropriate," "student-centered" — that no two scorers would apply the same way. It poisons inter-rater agreement and tells him the contractor has never had their own scoring audited.
- **Best-practice import** — strong. Scoring or writing to the contractor's professional framework instead of the project rubric, without noticing the two differ. Catherine's exact risk: a compliance auditor's instinct is to score against IDEA and field best practice; the project may want the model evaluated against a *different* and explicitly scoped target.
- **Essay instead of a score** — soft. A contractor who writes three paragraphs of nuance where the task asked for a rubric score plus a one-line justification. Reads as someone who can't commit to a judgment under a spec. Tolerable if the underlying calibration is good; annoying at volume.
- **Volume-over-spec** — soft. Submitting the sample task fast and complete but generic — every item technically done, none of it sharp. Signals a bulk-scoring contractor, not a promote candidate. Keeps them at the band floor.
- **Silent divergence** — strong. Scoring differently from the gold answer without flagging that you did, or why. He can coach a contractor who is wrong-but-transparent; he cannot trust one who is wrong-and-quiet, because it means the rest of their unaudited work is a black box.

## The Skim

Ravi reviews a sample submission in 15-25 minutes and the order is deliberate.

1. **Scoring items first, against the gold answers.** He pulls up the two model-transcript scoring items and lays them next to the calibration set. This is the fastest, highest-signal read: agreement is a number, and the number sorts most contractors immediately. Tight agreement plus sane justifications and he keeps reading with interest. Wild divergence with no flagging and he is now reading to confirm a no.
2. **The one scenario with the hardest intended failure mode.** He goes straight to the scenario item that should have produced a real trap. Is there a decision point? Is the wrong answer tempting? Does it exercise a model weakness he actually recognizes from the domain? A contractor who builds one genuinely sharp scenario has shown the ceiling of their work.
3. **The contractor-authored rubric.** This separates keep from promote. Observable criteria, scoped to the task, that another reviewer could apply blind — that contractor gets routed rubric and calibration work. Adjective soup keeps them at bulk-scoring.
4. **Justification quality, sampled.** He reads three or four one-line justifications across the submission. He wants reasoning from the rubric, divergences flagged, judgments committed to.

**Instant rejects.** Credential-as-argument anywhere in the justifications. Silent divergence on a scoring item where the gold answer is unambiguous. A scenario set with zero real failure modes — all quiz, no probe. A submission that ignored an explicit spec instruction (wrong format, wrong length, scored on the wrong axis) — that is a reading-the-spec failure and the spec is the entire job.

**What earns more and better-paid work.** Calibration tight enough to trust unsupervised. Rubric criteria he could hand to the next contractor as-is. An adversarial catch he didn't see coming — a non-compliant model answer flagged with the exact violated clause. A short, honest note where the contractor's expertise and the project spec pulled apart, surfacing the tension instead of papering over it. Those contractors get the rubric-authoring, red-team, and calibration item types — the top of the band.

## Reading Catherine

A direct read on how Ravi would react to Catherine's actual sample-task submission, given her profile.

**Where she would impress him.** Catherine's IEP/IDEA compliance-auditing background is, in his terms, *exactly* an adversarial-scoring instrument. Auditing is the muscle of reading a document, holding it against a precise standard, and finding the specific clause it violates — which is structurally identical to scoring a model transcript against a rubric and catching the plausible-but-non-compliant answer. When she scores a transcript and writes "the response offers an accommodation but the scenario described a modification — the model conflated the two," Ravi sits up: that is a real, specific, domain-grounded failure mode, and most contractors never produce one. Her 17 years in complex/PDA autism means she can generate edge cases the lab's generalist contractors literally cannot see — scenarios where a model's confident, fluent answer is subtly harmful for a neurodivergent learner. That is high-value training signal and it is scarce. And her rubric-design instinct from PD and compliance work means she has a real shot at writing observable criteria, which is the promote-tier skill. On raw domain substance, she is above the median contractor he reviews.

**Where she is at risk.** Three things, and they are the things that get good experts offboarded.

1. **Calibrating to the lab's rubric, not IDEA.** Catherine's professional reflex is to score against statute and field best practice — that is what a compliance auditor *is*. But the project rubric may define "good model behavior" on a different and explicitly scoped axis, and it is the spec's definition that counts, not hers. If she silently scores to IDEA where the gold answer scores to the project rubric, that reads to Ravi as silent divergence — a near-instant offboard signal. She must treat the project rubric as the authority and, where her expertise disagrees with it, *flag the disagreement explicitly* ("scored per the rubric; note that field best practice would weigh this differently") rather than override it or ignore it. Transparency converts her biggest risk into a strength he actively values.

2. **Writing to a model-eval spec.** Designing district PD or an audit checklist is not the same as writing a scenario that produces training signal. Her instinct may be to write a well-crafted *teaching* item — clear, correct, instructive — when the project needs a *probe*: a scenario with a tempting wrong answer where the model can plausibly fail. If her sample scenarios are all quiz and no trap, Ravi reads "subject-matter expert, not a model-eval contractor" and keeps her at the band floor at best. She needs to build the failure mode in deliberately.

3. **Async ambiguity and committing under a spec.** The work is asynchronous with thin instructions and no one to ask. Catherine's qualitative, practitioner background may pull her toward writing three paragraphs of nuance where the task wants a score plus one line. Ravi reads paragraphs-instead-of-a-score as someone who can't commit a judgment under a spec. She needs to make the call, justify it in one tight line from the rubric, and move on.

**What she must demonstrate to stay on and move up the band.** To *stay on*: in the sample task, score the calibration transcripts to the project rubric — not to IDEA — and where her expertise diverges, flag it in one line rather than scoring her own way silently. Follow the spec's format and length exactly; a format miss reads as a reading failure. To *move up the band*: write one scenario with a genuinely tempting wrong answer drawn from her autism/PDA expertise — a model failure mode the lab's generalist contractors cannot produce — and write her authored rubric in fully observable criteria ("response acknowledges the stated sensory constraint before proposing an alternative," not "response is appropriate"). One sharp, domain-specific adversarial catch on a model transcript, with the exact violated principle named, will move her toward the rubric-authoring and red-team work where the $90-110/hr end of the band lives. Her ceiling on this project is high; the only thing standing between her and it is the discipline of treating the lab's spec — not her own professional standard — as the authority, and being loud about it whenever the two pull apart.
