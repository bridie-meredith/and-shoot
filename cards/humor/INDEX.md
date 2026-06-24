# Humor Hall Index

All humor cards. Maintained by margit — update on every card store, quality change, or new authoring.

Humor cards are a **cross-project library resource class** (not story-facing). Each card catalogues one comedic *mechanism* — the structural engine of a kind of joke — with a bank of faceted exemplars spread across eras, cultures, classes, and teller-types. The dialogue-writer fork consults a humor card the way it consults a behavior card: as raw material to draw on, not a persona to embody. Humor cards are consulted, never cast.

**Future integration (not yet wired):** the dialogue-writer fork will pull a humor card by facet combination — e.g. `gallows-humor / setting:england-18thc / teller:condemned-prisoner` — to retrieve the right mechanism for a given anchor. The `## Dialogue-generation hooks` section in each card is the contract that integration will read. Until the wiring lands, human dialogue-writers and the fork consult these cards manually.

Schema: `schemas/humor-card.schema.md`.

---

## by_family

### incongruity
*Humor from violated expectation — collision of frames, logic past breaking, the impossible treated as mundane.*

- [absurdist-surreal](absurdist-surreal.card.md) — violated expectation: logic extended past breaking, deadpan impossible, non-sequitur, bureaucratic recursion; full
- [understatement](understatement.card.md) — incongruity of scale downward: the disaster named with a word calibrated for something orders of magnitude smaller; full
- [hyperbole-exaggeration](hyperbole-exaggeration.card.md) — incongruity of scale upward: inflating a real thing to absurd magnitude so the inflation itself is the joke; full

### superiority
*Humor from a target made smaller — including when the target is the self.*

- [irony-sarcasm](irony-sarcasm.card.md) — saying the opposite of what is meant; the gap between stated and intended meaning is the joke; sarcasm assigns the gap's edge to a person; full
- [self-deprecation](self-deprecation.card.md) — making yourself the target: disarming, bonding, or deflecting by absorbing mock-humiliation on your own terms; full

### relief
*Humor that discharges tension — laughing at what cannot be escaped.*

- [gallows-humor](gallows-humor.card.md) — laughing in the face of death / suffering / doom; tension discharged through comic acknowledgment of what cannot be escaped; full

### wordplay
*Humor from the language itself.*

- [wordplay-pun](wordplay-pun.card.md) — exploiting the slippage between sound, spelling, and meaning: puns, double-entendre, homophone exploit, idiom-literalization; full

### observational
*Humor from recognition of the shared ordinary.*

- [observational](observational.card.md) — naming the thing everyone experiences but no one has said aloud; the "it's funny because it's true" move; full

### character
*Humor that lives in how a person is — deadpan, the quick mind, the straight man.*

- [deadpan-dry-wit](deadpan-dry-wit.card.md) — comic content delivered with flat, affectless presentation; the gap between content weight and delivery register is the joke; full
- [wit-repartee-banter](wit-repartee-banter.card.md) — fast, intelligent back-and-forth; wit (the single well-made remark), repartee (the swift reply), banter (the sustained exchange and topper chain); full

---

## by_facet_keyword

A lookup aid for retrieval by tag, setting, teller-type, or deployment context. Pull the column that matches what you know; it names the card(s) to consult.

### by theme / subject matter

| keyword | cards |
|---|---|
| dark / death / doom | gallows-humor, irony-sarcasm, understatement, absurdist-surreal |
| coping / survival | gallows-humor, self-deprecation, absurdist-surreal |
| suffering / loss | gallows-humor, understatement, hyperbole-exaggeration |
| power / authority | irony-sarcasm, observational, absurdist-surreal, self-deprecation, wit-repartee-banter |
| class / social hierarchy | observational, self-deprecation, irony-sarcasm, wit-repartee-banter |
| language / words | wordplay-pun, wit-repartee-banter, irony-sarcasm |
| institutions / bureaucracy | absurdist-surreal, understatement, irony-sarcasm, observational |
| war / soldiers / military | gallows-humor, deadpan-dry-wit, understatement, hyperbole-exaggeration, wit-repartee-banter |
| grief / mourning | gallows-humor, understatement |
| boasting / self-promotion | hyperbole-exaggeration, self-deprecation (inverse), wit-repartee-banter |
| recognition / "it's true" | observational, self-deprecation, wit-repartee-banter |

### by era / setting

| setting keyword | cards |
|---|---|
| ancient world (Rome, Greece, China) | gallows-humor, self-deprecation, deadpan-dry-wit, wordplay-pun, observational, irony-sarcasm, understatement, hyperbole-exaggeration, wit-repartee-banter, absurdist-surreal |
| medieval (Europe, tavern, court) | gallows-humor, wordplay-pun, observational, irony-sarcasm, understatement, hyperbole-exaggeration, wit-repartee-banter |
| 17th–19th century (England, drawing-room, club) | self-deprecation, deadpan-dry-wit, wordplay-pun, irony-sarcasm, understatement, wit-repartee-banter |
| WW1 / WW2 / 20th century | gallows-humor, deadpan-dry-wit, understatement, observational, absurdist-surreal |
| secondary world / fantasy court | all 10 cards have secondary-world exemplars |
| westeros (planetos) | gallows-humor, self-deprecation, deadpan-dry-wit, wordplay-pun, observational, irony-sarcasm, understatement, hyperbole-exaggeration, wit-repartee-banter |
| modern / office / corporate | absurdist-surreal, observational, hyperbole-exaggeration, irony-sarcasm |
| folk / frontier / oral tradition | hyperbole-exaggeration, observational, wordplay-pun |

### by teller type

| teller type | cards |
|---|---|
| condemned / prisoner | gallows-humor, wordplay-pun |
| soldier / veteran / garrison | gallows-humor, deadpan-dry-wit, understatement, hyperbole-exaggeration, wit-repartee-banter |
| smallfolk / working-class | gallows-humor, self-deprecation, observational, wordplay-pun, hyperbole-exaggeration, irony-sarcasm |
| courtier / noble | self-deprecation, deadpan-dry-wit, irony-sarcasm, wit-repartee-banter |
| administrator / bureaucrat | absurdist-surreal, deadpan-dry-wit, understatement |
| philosopher / scholar | self-deprecation, wit-repartee-banter, wordplay-pun, absurdist-surreal |
| servant / steward | observational, understatement, absurdist-surreal |
| monarch / high authority | self-deprecation, irony-sarcasm, wit-repartee-banter |
| terminal patient / grieving | gallows-humor |

### by delivery mode

| delivery | cards |
|---|---|
| spoken-aside | all 10 |
| retort / topper | irony-sarcasm, wit-repartee-banter, understatement, gallows-humor |
| written / dispatch / letter | irony-sarcasm, understatement, deadpan-dry-wit, absurdist-surreal |
| interior / private | observational, self-deprecation, absurdist-surreal, hyperbole-exaggeration |
| performed / storytelling | hyperbole-exaggeration, wit-repartee-banter, wordplay-pun |
| two-speaker exchange | wit-repartee-banter (primary), irony-sarcasm (several exemplars) |

### by register / tone

| register | cards |
|---|---|
| bleak / dark | gallows-humor, deadpan-dry-wit, absurdist-surreal, understatement |
| dry / arid | deadpan-dry-wit, understatement, irony-sarcasm, observational |
| warm / bonding | self-deprecation, observational, wit-repartee-banter (warm end) |
| light / playful | wordplay-pun, hyperbole-exaggeration, wit-repartee-banter (warm end) |
| sharp / cutting | irony-sarcasm, wit-repartee-banter (cold end), deadpan-dry-wit |

### by project-world tag

| world | relevant cards (by exemplar coverage) |
|---|---|
| planetos / westeros (hotd, got) | gallows-humor (northerns, smallfolk), self-deprecation (noble courtly), deadpan-dry-wit (northerns), wordplay-pun (smallfolk oral), observational (smallfolk), irony-sarcasm, understatement (northerns, military), hyperbole-exaggeration (smallfolk tavern) |
| earth-bet (worm) | all mechanisms portable; no setting-specific exemplars yet |

---

## Composition

**Mechanism (humor card) + voice (behavior card) = a comedic line.**

A dialogue-writer fork loads a speaker's **behavior card** for voice — how this person sounds, their register, their fences. It pulls a **humor card** for the comedic move — the structural engine to use. The two cards compose at authoring time.

Example: a character with `westeros-northern` behavior card + `gallows-humor` mechanism card yields a dry Northern joke about impending death. The behavior card constrains vocabulary and cadence; the humor card supplies the setup → turn → payoff structure.

Cross-reference: `cards/dialects/comedy-register.card.md` — the shared tonal overlay card for comedy-register projects (e.g. and-experiment). That card describes *how a cast or project sounds when being funny*; these humor cards describe *what kind of funny*. The two layers are independent and compose.

**Mechanism × mechanism composition** is also supported — several pairs are noted in card-level `Pairs with` sections:
- `gallows-humor` + `deadpan-dry-wit` — the natural pair for bleak-comedy delivery.
- `understatement` + `irony-sarcasm` — share the gap-engine; often co-present.
- `hyperbole-exaggeration` + `wit-repartee-banter` — escalation chains in banter.
- `wordplay-pun` + `observational` — overlap at the recognition/double-meaning intersection.

---

## Pending / candidates

Mechanisms not yet authored that would round out the hall. Ordered roughly by priority for a general-purpose library.

### High value (close gaps in current coverage)

- **satire** — humor that attacks institutions, systems, or types through exaggeration and critique; distinct from observational (which notices) and irony (which inverts); needs its own card with political/social exemplars. Related to absurdist-surreal and hyperbole but with a target.
- **callback / running-gag** — humor from pattern and repetition within a narrative; the first instance sets up; each return escalates. Structural, not a single-line mechanism. Requires exemplars built across scene boundaries. Currently unaddressed.
- **mock-heroic / bathos** — applying elevated epic register to trivial subjects (or trivial register to epic subjects); closely related to understatement and hyperbole but with a specific register-collision engine. Deserves separation.
- **parody** — humor that mimics the style of a known genre or work for comic effect; requires genre-recognition; the closest mechanism in the current hall is absurdist-surreal (frame-violation) but parody's engine is specifically imitation. Secondary-world court parody of formal heraldry, chronicle, or epic verse is relevant to the pipeline.

### Medium value (enriches teller/delivery range)

- **bawdy / ribald** — humor from sexual innuendo, bodily functions, and taboo; the relief engine in its most direct form; tavern, soldier, and common-register staple. Currently the only relief-family card is gallows-humor. Smallfolk and medieval-setting coverage would benefit.
- **malapropism / verbal-confusion** — a speaker using the wrong word with comic effect; character-based; requires low-literacy or overly-formal teller archetypes; would pair with wordplay-pun. Narrower scope than wordplay; reasonable standalone.
- **situational / wordless humor** — humor that lives entirely in staging: a well-timed entrance, a prop discovered, a look exchanged. Not dialogue-driven; would be a prop/staging card rather than a dialogue card. Closest current card is deadpan-dry-wit (the oblivious variant), but purely physical comedy needs its own entry.
- **comic misunderstanding** — humor from two speakers talking at cross-purposes; both sincere, each missing the other's meaning. Structural rather than linguistic; dialogue-pair mechanism. Composes with wordplay-pun and wit-repartee-banter.

### Lower priority / specialist

- **anachronism-joke / fish-out-of-water** — humor from a character's vocabulary, assumption, or object being out of place in the setting. Highly useful for AU fic and portal-fantasy but narrow scope.
- **deadpan-fool / holy-fool** — the character who states an uncomfortable truth without register because they are not aware it is uncomfortable; related to deadpan-dry-wit (genuinely-oblivious axis) but deserves a standalone card as a character type with its own fences.
- **anti-joke** — sets up a joke structure then refuses the comedic payoff; humor from the refusal. Niche; requires sophisticated audience.
- **ironic-echo / dramatic-irony-humor** — the reader/audience knows something the character doesn't, and the character's sincere line is funny for that reason; narrative-level, not character-level; outside the scope of dialogue-writer consultation but relevant to dramatist and stitch phases.
