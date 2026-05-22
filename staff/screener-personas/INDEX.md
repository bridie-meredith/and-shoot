# Screener Persona Library

19 personas modelling the gatekeepers who screen a candidate's resume / proposal / pitch for a single coveted slot. Authored for the `resume-targeting` project (Catherine Olver career-pivot analysis, 2026-05). Preserved here for reuse: any future resume-, proposal-, or pitch-targeting effort can draw the relevant subset rather than re-authoring screeners from scratch.

**Provenance.** Originals authored in `resume-targeting/personas/`; this collection is a preservation copy. Each card was authored by an isolated fork (no cross-persona visibility) to keep its read independent. Cards use the `class: persona` schema (`schemas/card.schema.md`) adapted for a screening purpose — see the `## Card structure` section below.

**Reuse note.** Each card's `## Reading Catherine` section is candidate-specific (Catherine Olver). When reusing a card for a different candidate, treat everything above `## Reading Catherine` as the durable, reusable model of the gate; re-author only the `## Reading <Name>` payload for the new candidate.

---

## Personas by screening role

The personas cluster into eight opportunity roles. Each role carries 2-3 personas modelling different gates or lenses on the same opportunity.

### Role 1 — AI training contractor (Mercor / Scale / Surge-class marketplaces)
| Slug | Screener | Lens |
|------|----------|------|
| mercor-talent-ops | Priya Anand — domain sourcing lead, AI-training expert network | Marketplace profile screen |
| lab-domain-reviewer | Ravi Okonkwo — education-domain technical lead, lab/client side | Sample-task quality review (gate after matching) |

### Role 2 — Frontier-lab full-time (evals / human-data / education policy)
| Slug | Screener | Lens |
|------|----------|------|
| frontier-lab-recruiter | Maya Trent — technical recruiter, frontier AI lab | First-pass recruiter screen |
| frontier-lab-evals-manager | Devang Rao — eng & research lead, model behavior / education evals | Evals hiring manager |
| frontier-lab-policy-lead | Naomi Feldman — hiring manager, trust & safety / education policy | Education T&S / policy role family |

### Role 3 — Edtech learning scientist / designer
| Slug | Screener | Lens |
|------|----------|------|
| edtech-learning-science-lead | Hannah Brooks — senior manager, efficacy research | General edtech (quantitative bar) |
| sped-edtech-product-lead | Renée Acosta — director of learning design, SpEd edtech | SpEd-focused edtech subset |
| early-childhood-edtech-curriculum-head | Grace Tan — head of curriculum, early-childhood edtech | Early-childhood edtech subset |

### Role 4 — L&D / instructional design at a SaaS company
| Slug | Screener | Lens |
|------|----------|------|
| saas-talent-recruiter | Tyler Brennan — corporate recruiter, talent acquisition | ATS + first-pass recruiter screen |
| saas-ld-director | Dana Whitfield — director of L&D, mid-stage SaaS | Hiring manager |

### Role 5 — Customer education at an AI company
| Slug | Screener | Lens |
|------|----------|------|
| ai-co-customer-education-lead | Sofia Mendel — head of customer education, K-12 segment | Hiring manager |
| ai-co-gtm-partner | Marcus Hale — VP of go-to-market / customer success | Commercial co-screener (retention lens) |

### Role 6 — Solo consulting to districts
| Slug | Screener | Lens |
|------|----------|------|
| district-sped-director | Renata Okafor — director of special education | Buyer — program / compliance lens |
| superintendent-cabinet | Eleanor Voss — deputy superintendent / chief of staff | Buyer — cabinet / board-politics lens |
| district-principal | Joanne Pruitt — building principal | Buyer — building-level staff-PD lens |

### Role 7 — Ed+AI startup
| Slug | Screener | Lens |
|------|----------|------|
| edai-startup-founder | Devin Park — founder & CEO, early-stage ed+AI startup | Hiring an education lead |
| startup-technical-cofounder | Arjun Mehta — technical co-founder seeking the domain half | Assessing a co-founding partner |

### Role 8 — Productized PD / courses / book
| Slug | Screener | Lens |
|------|----------|------|
| productized-pd-gatekeeper | Camille Duarte — head of instructor partnerships, cohort platform | Platform gatekeeper / acquisitions |
| cohort-pd-buyer | Denise Carver — special-education director | End buyer — will she enroll / pay |

Roles 6 and 8 have no literal hiring manager; those personas screen the analog artifact (consultant one-pagers / proposals, expert pitches / book proposals).

---

## Card structure

Each card uses the `class: persona` schema (`schemas/card.schema.md`), adapted for a screening purpose:

- **Description** — one-line read of the screener.
- **The Position** — what they fill/buy, comp band, how the screen works, what a "yes" means.
- **Voice** — how they sound while screening (mine this for verbatim quotes).
- **Taste** — what makes an artifact jump to the YES / shortlist pile.
- **Pet Peeves** — graded blocker / strong / soft.
- **The Skim** — first-8-seconds mechanics, scan order, instant rejects.
- **Reading `<Candidate>`** — the actionable, candidate-specific payload: strengths seen, screen-out risks, what the artifact must surface. Re-author this section per candidate on reuse.

---

## Method

The end-to-end process that produced and used these personas is documented in `design/resume-targeting-method.md`.
