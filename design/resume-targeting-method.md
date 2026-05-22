# Resume-Targeting Method

A repeatable process for honing a candidate's positioning — resumes, next-actions, and a consolidated decision report — by modelling the actual gatekeepers who screen them. Developed and first run on the `resume-targeting` project (Catherine Olver career-pivot analysis, 2026-05). This spec lets the same process be re-run for a different candidate or a different set of opportunities.

**Sibling process specs:** `design/round-trip-method.md`, `design/and-project-process-notes.md`.

---

## 0. What this method is for

A candidate has one resume and a vague sense of several possible career directions. The questions are: *which directions are real, what does each gatekeeper actually screen for, what is the candidate missing, and what should the resume say?*

This method answers all four by (a) mapping the opportunity landscape, (b) building an explicit model of every gatekeeper as a persona card, (c) revising one resume variant per opportunity against those gatekeepers, and (d) deriving short-horizon next-actions plus a *projected* resume that shows what the candidate looks like once those actions are done.

The core idea: **the screener persona is the spec.** A resume is correct when it survives the specific skim of the specific person who will read it — not when it reads well in the abstract.

---

## 1. Inputs

- The candidate's current resume (any format).
- A briefing on the candidate's background, constraints, and the broad space of opportunities they are considering.
- Market/comp context (compensation bands, hiring timelines, role definitions) — researched fresh per run.

---

## 2. Phases

### Phase 1 — Opportunity landscape

Produce one **opportunity report**. It enumerates the candidate's realistic role categories (the first run found eight). For each role: what the work actually is, compensation band, time horizon to land, obligations, pros, cons, and an honest candidate-fit rating. The report also carries:

- a **fit matrix** scoring each role on credentials / skills / network / identity;
- a **cross-cutting weak-spots** section — the gaps that show up across multiple roles;
- a **sequenced next-steps** section (weeks 1-2, weeks 3-6, months 2-3, months 4-6 reassess).

This report is the spine. Every later artifact traces back to a role it defined.

### Phase 2 — Screener persona authoring

For each role, author **2-3 gatekeeper personas**, each modelling one distinct gate or lens on that opportunity (e.g. a first-pass recruiter vs. the hiring manager; a marketplace sourcer vs. the sample-task reviewer; for buyer roles, the analog buyer rather than a hiring manager).

**Author each persona in an isolated fork — no cross-persona visibility.** Independence is the point: two screeners on the same role must not converge by contamination.

Each persona card uses the `class: persona` schema (`schemas/card.schema.md`) adapted for screening, with sections: **Description**, **The Position** (what they fill/buy, comp, how the screen works, what a "yes" means), **Voice** (first-person screening lines — the quotable layer), **Taste** (what jumps to the YES pile), **Pet Peeves** (graded blocker/strong/soft), **The Skim** (first-8-seconds mechanics, scan order, instant rejects), and **Reading `<Candidate>`** (the candidate-specific payload: strengths seen, screen-out risks, what the artifact must surface).

Everything above `Reading <Candidate>` is durable and reusable; only that final section is candidate-specific.

Persona cards are preserved in a screener-persona library (`staff/screener-personas/`) with an INDEX so future runs reuse rather than re-author.

### Phase 3 — Resume variants + review loop

Author **one resume variant per role**, each targeted at that role's personas. Then run a review loop:

1. The role's personas review the variant; a critic produces a per-screener feedback report with an explicit verdict (e.g. `ADVANCE` / `BORDERLINE` / `SCREEN-OUT`).
2. Revise the variant against the feedback.
3. Re-review. Repeat until the personas advance it or the remaining risks are no longer page-level (some risks — e.g. sample-task behaviour — a resume can only *signal* toward, never resolve).

Recurring fixes the loop surfaces: lead with the scarce specialty in the first line; verb discipline (*audited, scored, designed* — not *led, facilitated, taught*); demote prestige that has no operational translation; make availability/positioning explicit; write positioning language legible to the target audience, not the candidate's old one.

Keep every version — current and revised — preservation over overwrite. The first run used `resumes/` (v1), `resumes-v2/` (revised), with `.changelog.md` files per variant.

### Phase 4 — Per-position fork

Run **one fork per role**. Each fork is self-contained and reads only its own role's material (opportunity report section, persona cards, current resume, review). Each fork outputs three files:

1. **persona-analysis.md** — for each persona, the top 6-10 questions that persona asks while screening, and a statement of what they are looking for (the YES bar and the instant-reject triggers). Plus a synthesis of what the role's personas jointly demand.
2. **next-steps.md** — concrete next-actions for the candidate, **each achievable within 1-3 months**, each tied to a specific persona question or screen-out risk it neutralizes, bucketed weeks 1-2 / weeks 3-6 / months 2-3.
3. **projected resume** — the resume rewritten **as if every next-step were already completed**. Hard rule: stay truthful to the 1-3 month horizon — do not invent credentials beyond what the next-steps would plausibly yield (a newsletter with a few hundred subscribers is credible; 10k is not; "can clean a CSV and run a regression" is credible, a quant-research claim is not).

Forks run in parallel; results land in `forks/role-NN-<slug>/`.

### Phase 5 — Master report

Compile everything into one **very detailed master report**: executive summary, candidate profile, opportunity landscape, cross-cutting weak spots, a full per-role section (overview, personas, top questions, verbatim quotes, next-steps, projected resume, key takeaways), a cross-role synthesis table, a unified recommended sequence, and a closing. The master report is the deliverable a human reads to decide.

### Phase 6 — Archival

- Screener personas → screener-persona library (`staff/screener-personas/`), indexed.
- This method spec → `design/`.
- All candidate artifacts (resumes, reviews, personas, forks, reports) → `projects/<candidate>-resume-targeting/` for preservation.

---

## 3. Principles

- **The persona is the spec.** Resume quality is defined by survival of a specific skim, not by abstract polish.
- **Isolation buys independence.** Author personas and run per-role forks in isolated forks so reads do not contaminate.
- **One fork per position.** Each role gets its own analysis lane; never blend roles.
- **Truthful projection.** The projected resume is a 1-3 month forecast, not a fantasy. Every projected claim must be reachable in the horizon.
- **Highest-leverage = shared.** Next-steps that recur across multiple roles (e.g. LLM fluency, one public artifact) are the highest-leverage moves — flag them in the master report.
- **Preservation over overwrite.** Keep current and projected, v1 and v2. Nothing destructive.
- **Honest screen-outs.** If a persona correctly rejects the candidate (a real, unbridgeable gap), the method records it as a correct SCREEN-OUT — it does not engineer the resume to fake past it.

---

## 4. Output layout

```
<project>/
  Catherine_Opportunity_Report.md        — Phase 1
  INDEX.md                               — role → persona map
  personas/                              — Phase 2 (originals)
  resumes/        resumes-v2/             — Phase 3 variants (v1, revised) + .changelog.md
  reviews/        reviews-v2/             — Phase 3 critic feedback per round
  forks/role-NN-<slug>/                   — Phase 4
    persona-analysis.md
    next-steps.md
    Catherine_Resume_NN_<slug>_projected.md
  <Candidate>_Career_Pivot_Master_Report.md  — Phase 5
  staff/                                 — format spec + converters (RESUME_MD_FORMAT.md, md_to_docx.py)
```

On reuse: copy persona cards from `staff/screener-personas/`, re-author only each card's `Reading <Candidate>` section, and re-run Phases 1 and 3-6 for the new candidate.

---

## 5. Re-runnability

The method is re-runnable per role and per phase. Re-running Phase 3 on one variant invalidates that variant's Phase 4 fork outputs; re-running Phase 1 invalidates everything downstream. Treat the opportunity report as the staleness root.
