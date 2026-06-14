# Book I — State Ledger & Change-Propagation Instrument (run-02)

> **CANONICAL BOOK-I STRUCTURE (re-fused 2026-06-07, CL-001→004) now lives in
> `book-i-outline.md`** — a clean 11-chapter outline, thread-checked PASS against
> `thread-config-book-i.txt`. *This ledger is retained as the change-history + state/blast-radius
> working memory (the CL log, the GUARDS, the entity registry, the bridge). On any future note: edit
> the ledger, then re-fuse into the outline.*


**Purpose.** The working instrument for *revising* Book I. It tracks character-state and
world-state at every chapter boundary, the causal threads (plant→fire, gift→spend, curdle
rung), and the **blast radius** of each chapter (what downstream beats depend on it). When a
chapter note arrives, this is the surface I edit: slot the change, recompute the downstream
snapshots, flag any thread the change orphans.

**Where this sits (uses existing machinery — does not replace it).** A chapter note is a
*post-convergence principal enrichment* in the sense of `design/convergence-process.md` §Notes:
ratify the addition → write GUARDS (what it must not break) → one integration pass → scoped
re-validation. This ledger is the **state-tracking + blast-radius companion** to that loop; it is
not a new process. Division of labor:
- **Revision loop & criteria** → `design/convergence-process.md` (the six criteria, the
  enrichment-round pattern). Outcomes append to `convergence/convergence-ledger.md`; a full
  re-fuse, when wanted, writes `convergence/round-NN/`.
- **Re-authoring affected chapters** → `screen-writer` agent. **Structural / orphan-thread /
  dramatic-shape re-validation** → `dramatist`. **Taste** → `audience` (taste-judge). **State &
  consistency drift across chapters** → `auditor`. (Same role→agent map as convergence-process.md.)
- **Mechanical thread audit** → `scripts/check-threads.py` (NEW tool) with
  `design/run-02/thread-config.txt`. Mechanizes the convergence criterion *"setups pay off; no
  orphaned threads"* that the dramatist otherwise eyeballs. Run it on the canonical outline
  (closure) after every edit.
- **State home of record (production mode)** → `staff/showrunner/memory.md` + the substance
  signature (`series.substance`, still `~`/to-derive). This ledger is the chapter-granularity
  layer that memory/substance don't yet hold; promote upward when a revision stabilizes.
- **Open cross-chunk watch-items (production mode)** → the parking-lot
  (`schemas/parking-lot.schema.md`). A pending plant with no chosen payoff chapter is a
  parking-lot-shaped item; track it here during design, promote on stabilization.

**Baseline source (pre-change).** `convergence/chapters/round-02/fusion.md` (the converged
10-chapter outline), framed by `design/restructured-books-two-desires.md` (the principal's
**two-desires** re-axis: every book is *acquire resources* vs *be left alone*). Mechanics from
`convergence/round-03/fusion-v2.md` (Cauldron-Belly / poison-path / mithridatism / three Locks).
This ledger reflects the CURRENT canonical state; notes mutate it from here.

---

## Governing state axes (what we track)

**Saerys (the tracked protagonist vector):**
- **RESOURCE** — reagent tier accessible + supply-line reach (the first desire).
- **SOLITUDE** — autonomy / ungovernability: how subtractable her watchers are (the second desire).
- **ARMOR** — grief-armor integrity (transcendence↔attachment); + whether the wound is *visible to the reader* this chapter.
- **CAPABILITY-real** — actual competence on TWO real strands now (GUARD-1 rev-3): (a) mundane poison/mithridatism/logistics and (b) **real, hoarded cultivation** (source-radiance internalized from magical *materials* → body-tempering, growing but deliberately un-spent). The broken-clock TRUE channel.
- **TIER-self** — her *framework-wrong* self-assessment (the broken-clock FALSE channel): she's right the power is real, wrong about what it is — a xianxia model (realms/tribulations) laid over canon blood/fire/death magic. The gap between her model and the real mechanism is the comedy engine.
- **WARMTH** — live rootable bonds open (the reader's investment; the gift accounts).

**World / apparatus (the machine she builds):**
- **APPARATUS** — workshop + procurement network → realm-spanning reagent network (was "sick-house"; CL-004).
- **NOTE** — the master-key lifecycle: *verbal indulgence → standing license → sealed grant → Lock I → (Bk III: orphaned seal)*.
- **DOSE-LOG / FACTOR / BELOW-STAIRS / LEDGER** — the four instruments, with their growth state.
- **POLITICAL CLOCK** — **Jaehaerys I's long peace** (Book I: dormant; Saerys setting-blind throughout). The Dance is the *far-future* series climax (129 AC) reached via her longevity — OPEN; see `timeline-and-family-tree.md` §5.

**Hard fences (never violated by any edit):** setting-blind · **non-combatant by choice + no
external energy spend** (was "never martial" — the power is real and could fight, but she hoards it
absolutely: no fighting, **no healing**, no outward effects on the page: GUARD-1 rev-3) ·
**cultivation is real-but-hoarded + framework-wrong** (GUARD-1 rev-3 — supersedes "real-but-inert"
and the old "clock stays broken") · **materials-only cultivation — never cultivates people / never
demonic** (GUARD-1 rev-3) · idiot-savant boundary · armor cracks exactly once (III.8) · no dragon (she
ate her egg; dragons are fuel, not mounts). See `saerys-targaryen.card.md` §Hard Fences, the run-02
GUARDS below, and `timeline-and-family-tree.md` (era + family tree + magic rules). *Any note that
breaks a fence gets flagged, not silently applied.*

---

## Ratified premise changes (run-02 GUARDS)

*Ratified 2026-06-07 from the I.1 rewrite (CL-001) + the era/cultivation note (CL-002). Recorded per
`convergence-process.md` ("ratify smuggled premises explicitly"); mirrored to
`convergence/convergence-ledger.md`.*

**GUARD-1 (rev-3) — Cultivation is REAL and powerful, hoarded by choice, framework-wrong, and
fuelled by MATERIALS not people** (supersedes rev-2's blood-path; full rules in
`timeline-and-family-tree.md` §3). The magic works. No ambient qi — energy radiates from *sources*,
and the sources are **magical objects + magical substances ONLY**: dragon eggs, weirwood, dragonglass,
Valyrian steel, wildfire and the pyromancers' fire-craft, and assorted reagents. **Living people are
NOT a source — she does not cultivate people. She is NOT a demonic/blood cultivator.** (Her own
blood in I.1 was a one-off sympathetic-resonance catalyst on an object, not a path she walks.)
Mundane matter is inert. She internalizes + refines source-radiance → her body is **tempered**
(durability, slow un-aging, eventually superhuman). She **could** spend it — fight, throw fire, crazy
effects — **but spending sets back the slow internal growth, so she hoards it internal.** **No
external energy application of any kind — including NO magical healing** (a "healing hand" is exactly
the expenditure she refuses); any mending she ever does is *mundane apothecary craft*, not
cultivation. The capacity is real and growing; the restraint is a *choice* → she reads as a
non-combatant and the plot still runs on poison + logistics + paper. **Her actual drive is acquisition:** she is an empirical
materials-hunter, systematically getting and testing things to find what *registers* (radiates) —
indifferent to the common people ("mortals," beneath her notice), forever chasing the next, rarer
reagent. **The broken clock:** she's RIGHT it's real and WRONG about the framework — a past-life
*xianxia* model (dao/realms/tribulations/dantian) over canon **fire/death/old-gods magic**, and she
gains *despite* mis-modeling it (e.g. she ingests poisons hoping they'll register; they don't — but
she builds real mundane immunity and files it as "tempering"). *Must-not-break:* she never fights on
the page; she never cultivates people / is never demonic; **she never spends energy outward — no
healing, no external effects** (hoarding is absolute); cultivation never saves anyone she loves; the
real un-aging makes the ending meta-question LITERAL; she stays blind to the true system.

**GUARD-2 — Inciting inversion re-framed: heal→fuel** (ratified; supersedes pray→desecrate). The
FROZEN opener is now "given a living egg to save her dying life → she taps it for fuel." The
desecration register becomes an experimentation register; the gesture is still "living/sacred thing
→ fuel for the self," carried one inch further — she drains a LIVING beast, not grinds a dead
relic. III.5's frame-rhyme updates to match (one living beast drained → a sky of dead ones).

**GUARD-3 — Curdle R0 stays a LAUGH at the time.** She drains the egg dead, but staged so neither
the infant nor the reader registers a kill: the adults read a failed/dud egg (canon dragonless);
the reader laughs at / marvels at the infant alchemist. The horror is RETROACTIVE — only after III.5
does the reader realize the first thing she ever did was kill a living sacred beast for fuel. The
ladder must start on a laugh so R4 is the betrayal of it.

**GUARD-4 — Era + family tree fixed (CL-002).** Set in **Jaehaerys I's reign** (the long peace,
peak dragon-numbers; Saerys b. ~84 AC). **Jaehaerys = King + father** (the warm cage); **Alicent =
Queen + mother** (AU: stands where canon has Alysanne); **Helaena = Saerys's younger sister**;
**Viserys = a young nephew** (demoted from baseline father-king; OPEN: brother/cousin). The
father-king gift→spend transfers from Viserys to **Jaehaerys** (his 103 AC death). Full tree, canon
date anchors, and the one open fork (series end-date: Dance 129 AC recommended) live in
`timeline-and-family-tree.md`. Saerys stays setting-blind throughout.

---

## Entity registry (canonical, with one-line arc)

### People
| Entity | Book I role | Arc-in-one-line | First / last in Bk I |
|---|---|---|---|
| **Saerys** | protagonist (infant→age 9; b. ~84 AC) | dying reincarnated infant → founds real (blood-)cultivation she hoards → builds the machine → makes herself ungovernable | I.1 → I.11 |
| **Jaehaerys I** | the **King / father** — the warm cage | indulges the miracle child (I.1 aftermath) → seals the grant out of love (I.10) → [Bk II/III: dies 103 AC, mourned; orphans the seal] | I.1 → I.10 |
| **Viserys** | the SI's **nephew** (young, minor warm relation) *(OPEN: brother/cousin)* | "less of a deal at that time" — a fond young kinsman, not yet the future king | ambient (referenced) |
| **The Septa** | central handler / chief watcher | the watcher to subtract; right about everything except *why*; defeated by paper (I.11) | I.1 → I.11 |
| **Helaena** | the warm spot / riddle-twin (Saerys's **younger sister**) | the one who finds Saerys *normal*; bond deepened I.5 → [Bk III: broken] | I.5 |
| **The maester** | lab gatekeeper / first mark | robbed since toddlerhood (I.2, MAESTER-MARK) → out-administered into dependency (I.3); still-room access secured | I.2 → (ongoing) |
| **Alicent** | the **Queen / mother** | **saves the dying infant with an unsanctioned egg (I.1)** → love curdles toward horror as the child returns "wrong" *(default — OPEN: vs. a warm bond the long years spend)* | I.1 → ambient |
| **Otto** | a Hightower at court / Queen's kin | ambient authority Saerys ignores; intelligence source, not antagonist | ambient |
| **Aemond** | foil (offstage-ish) | the *martial* answer to dragonlessness (bonds a great dragon); the warrior road she **declines** (she could fight — chooses to hoard) | referenced I.5 |
| **The laundress's boy** | rootability anchor | dying child she nurses for nothing; proof the armor is armor; lives | I.4 (→ echo I.8) |
| **The pest** (under-septa / rival's man) | first poison victim | moves to expose her; removed by lingering flux; never knows | I.7 |
| **The Braavosi factor** | first remote agent | first bill of exchange; exotic-materials/reagent (incl. poison) import line → [Bk II: the network] | I.3 (→ I.9) |

### Apparatus / props
| Entity | State at Book I close | Cross-book fate |
|---|---|---|
| **The cradle-egg** (living) | drained dead by sympathetic ingestion (I.1) — R0; the hidden origin of her dragonlessness (reads as a dud) | living→dead gesture rhymes (strengthened) to III.5 dead-dragon field |
| **The Cauldron-Belly** (self-label) | principle conceived in infancy (I.1); grandiose label by age 3; retro-frames the eating antics | → III.5 reaches for the black stone |
| **Sympathetic resonance** (cultivation principle) | discovered I.1 — a fragment (+ her blood) stands for the whole | → III.5 (she needn't take the *whole* field, but does) + broken-clock recurrences (I.6/III.5) |
| **Reincarnation-sickness** | the dying-infant origin (I.1); cultivating stabilizes her body | → soft rhyme: I.6 fever / III.3 immunity |
| **The account-book / LEDGER** | unreadable-by-others; now a steering wheel (I.9) | → II.1 owned empire |
| **The NOTE** | sealed grant, fires as Lock I (I.11); kept on person | → III.1 orphaned license → III.10 heist seal |
| **The DOSE-LOG** | mithridatism underway; ~3 yrs of dosing | → II.6 deepened → III.3 failed assassination |
| **The workshop + procurement network** *(was "the sick-house" — CL-004)* | running ~3 yrs; cover = the eccentric scholar-princess; import lines + agents fetching & testing materials | → II.1 realm-spanning *reagent* network |
| **The materials assay / collection** *(new — CL-004)* | her logged survey of what registers (weirwood, wildfire, dragonglass…) vs. what's inert | → the forever-chase; III.5 dragon-corpse feast is the apex |
| **The wildfire-shard** | eaten (I.6); the first genuine ring the *adults witness and fear* (the private founding ring was I.1) | → I.6 is the precedent template for III.5 black-stone reach |

---

## Per-chapter state ledger (I.1 – I.11)

> **Book I is now 11 chapters** (CL-003 inserted I.2 `the-pantry-heist`; old I.2–I.10 shifted +1 to
> I.3–I.11). This diverges from the baseline's 10-ch Book I — final integer numbering is settled at
> re-fuse; the frozen `convergence/` outline keeps the old 10-ch numbering.

> Format per chapter: **Beat** (one line) · **Deltas** (what changed, by entity) ·
> **End-state vector** (Saerys axes + key world flags at chapter close) ·
> **Threads** (PLANT / FIRE / curdle rung / register / DN-T) ·
> **Blast radius** (downstream beats that depend on this chapter — what breaks if it changes).

### I.1 · a-baseline  *(was: the-christening-spoon; alt title: the-frequency)*  `[REWRITTEN · CL-001]`
- **Beat:** A dying reincarnated **infant** — mind/brain incompatibility, seizures. Her mother **Alicent the Queen**, against the withheld blessing of **the King (her father, Jaehaerys)**, slips a **living, warm dragon egg** into the cradle to save her. *Feeling the egg radiate* — and clocking the impossible silver hair / purple eyes around her — Saerys concludes she's in a *magical world* and must cultivate. The air is dead to her sense; she needs a **source** — a **baseline**. She mimics the egg (days; nothing), tries to ingest it whole (can't crack it), then **chips a fragment** with a smuggled hard toy and swallows it — a real flicker, gone in a flash. Insight: **energy is sympathetic** — a chip can stand for the whole. Another chip, **a smear of her own blood** *(her OWN — a one-off sympathetic-resonance catalyst on an object, NOT the demonic/people-harvesting path she never walks; GUARD-1 rev-3)*, *willing the part to be the whole* — and **it takes**: real source-radiance seeds in her body (she calls it a "frequency"; no dantian), and she pulls in more. The egg **goes cold** (drained dead; staged as a failed egg — GUARD-3) and is taken away. The infant lives — serious, and "a bit touched in the head."
- **Deltas:** ARMOR established as **active death-refusal** (a 2nd death, clawed back on-page — the armor is literal from frame one). Cultivation **founded** — real and growing, hoarded internal (GUARD-1 rev-3): the genuine founding ring that makes her believe forever. The **acquisition drive** is born here too (she will spend her life chasing the next source). Cauldron principle **conceived** (body-as-vessel; grandiose label crystallizes by I.5). Dragonlessness **originated** (she consumed her own cradle-hatchling; hidden, reads as a dud). SYMPATHETIC-RESONANCE discovered. Alicent (Queen): life-saving mother-love *(default: curdles toward horror as the saved child returns "wrong" — OPEN)*. Jaehaerys (King/father): indulgence re-homed to the **aftermath** (he dotes on the miracle child who should have died).
- **End-state vector:** age **~infant–1yr** · RESOURCE T0 (the egg, now spent) · SOLITUDE: none (fully watched) · ARMOR: sealed, **death-refusal active** · CAPABILITY-real: **real cultivation seeded** (body-tempering begins; hoarded, never spent) · TIER-self: "Foundation established — the dao is real" *(framework-wrong: it's fire/death/old-gods magic, not a realm-ladder)* · WARMTH: Alicent (open→cooling), Jaehaerys (open, via the miracle) · NOTE: *verbal indulgence (aftermath)* · DOSE-LOG: none.
- **Threads:** PLANT[NOTE] (re-homed to aftermath), PLANT[CAULDRON], PLANT[SYMPATHETIC-RESONANCE] *(new)*, PLANT[REINCARNATION-SICKNESS] *(new)*, PLANT[ACQUISITION-DRIVE seed] *(new — the forever-chase for sources)*, PLANT[GRIEF-REFUSAL seed] *(re-flavored: death-refusal)*, PLANT[GIFT:JAEHAERYS seed] *(miracle-child tenderness; was GIFT:VISERYS)*. Rung **R0** (laugh now / horror retroactive — GUARD-3). Register **SPIKE** held (the infant lecturing itself on sympathetic resonance — keep at full grandiosity so III.8's silence still calibrates; texture is uncanny-funny, not pure zany). DN-1 armed. **Ratifies GUARD-1 rev-3 / 2 / 3 / 4.**
- **Blast radius:** ENORMOUS. Feeds NOTE arc (I.3/I.10/I.11/III.1/III.10), CAULDRON arc (I.5/III.5), GIFT:JAEHAERYS (the father-king spend), ACQUISITION-DRIVE (I.2/I.3/I.5/I.6 → III.5 dragon-feast), the **death-refusal** motif (I.8/III.8 — now *literal*: at III.8 cultivation cannot out-refine Daenys's death). SYMPATHETIC-RESONANCE → III.5 (she needn't take the whole field, but does = curdle) + broken-clock recurrences (I.6/III.5). The drained-living-egg gesture re-rhymes III.5 (living→dead at scale), strengthening the curdle apex. Register here remains the calibration reference for the III.8 break. **HELAENA gift no longer seeded here → first planted I.5** (still fires III.7; optional cradle-witness Helaena beat — OPEN).

### I.2 · the-pantry-heist  *(NEW · CL-003 — toddler bridge chapter)*
- **Beat:** A toddler, barely walking, betrayed by her own baby hands. Her cultivation-sense (sources radiate; the air is dead) snags on the **one thing in the maester's still-room that glows to her** among a wall of inert jars — a genuinely-magical reagent. Her first **heist, in four beats**: **SIGHT** (she clocks the source — *and* that no one in the world guards anything against a two-year-old) → **PLAN** (an immortal mind drawing up an op around toddler assets: the maester's rounds, the cover of clumsiness, the perfect alibi of being underestimated) → **IMPLEMENT** (she toddles in during the gap and takes it — by climbing, toppling, sheer nerve) → **REWARD** (she gets it down and ingests the source). Then the **OH SHIT**: it is far more potent than she gauged — an uncontrolled **breakthrough** tears through a body too small to hold it. It nearly kills her; it nearly flares into the open. She scrambles, genuinely frightened for the first time, to bury it before anyone sees.
- **Deltas:** HEIST-METHOD **founded** (sight→plan→implement→reward — the seed of every later Lock). Maester established as her standing **mark/foil** years before I.3 formalizes him. RESOURCE: first *independent* source acquisition. ARMOR/death-refusal **re-fired** (another brush with death, refused). The "objects radiate → ingest a real source → real gain" mechanic shown live (GUARD-1 rev-2). Breakthroughs shown to have **teeth** — the path is bigger than her control, and it can expose her.
- **End-state vector:** age **~2–3** · RESOURCE T0 (one stolen source, spent) · SOLITUDE: *first taste* (unwatched-because-underestimated — the "ungovernable" engine starts here) · ARMOR: sealed, death-refusal re-fired · CAPABILITY-real: real cultivation **jumped** (a breakthrough, hoarded) · TIER-self: "First true breakthrough — the path is real and steep" *(framework-wrong)* · WARMTH: the maester (an oblivious mark) · NOTE: none yet.
- **Threads:** PLANT[HEIST-METHOD] *(new — sight/plan/implement/reward)*, PLANT[MAESTER-MARK] *(new)*, FIRE[death-refusal re-fire]. Rung **off-ladder** (no living victim — a stolen jar, not a drained life; the curdle ladder stays clean). Register **SPIKE→CHILL** (toddler-heist comedy collapsing into the oh-shit breakthrough — the *private* rehearsal of the I.6 furnace-sect *public* scare). DN-7 (toddler motor-comedy: the immortal mind vs. the traitorous baby hands).
- **Blast radius:** HIGH. HEIST-METHOD → I.11 Lock I (rung 1) → II.10 → III.10 — the three Locks now have a toddler origin. MAESTER-MARK pre-loads I.3 (out-administering a man she has robbed since she could walk lands harder). The "a breakthrough has teeth, and stays secret" beat is the private rehearsal the I.6 public scare escalates. **Bridges the infancy→childhood gap — the structural fix this chapter exists to make.**

### I.3 · the-collector-princess `[KEYSTONE]`  *(was: the-charitable-princess — re-conceived CL-004)*
- **Beat:** Indifferent to the smallfolk (mere "mortals," beneath her notice), she pours her princess-privilege into the only thing that matters: **getting materials**. She founds her **acquisition apparatus** — a private workshop/collection (cover: the eccentric, indulged scholar-princess) and her first **import line** — and brings the maester (her mark since she could walk) to heel as supplier and screen. She begins a systematic **assay**: get a thing, test whether it *registers* (radiates), log it — including dosing herself with poisons (they don't register; she builds real immunity anyway and files it "tempering"). Top of the want-list: **weirwood** and the **pyromancers' fire-craft**.
- **Deltas:** APPARATUS born — a workshop + procurement network (NOT a charity). Maester → dependent supplier/screen. LEDGER born (acquisition account-book only she can read). FACTOR opened (first bill of exchange — to *import exotic materials*). BELOW-STAIRS opened (agents who fetch & test; "the little master"). DOSE-LOG opened (self-assay of poisons → mundane immunity, mis-filed as tempering). ACQUISITION-DRIVE becomes the engine of the book.
- **End-state vector:** age ~6 · RESOURCE T0–1 (local stores + first import line) · SOLITUDE: *low-rising* (the workshop + requisitions launder unsupervised hours) · ARMOR: sealed · CAPABILITY-real: poison-handling begun, immunity rising; real cultivation off acquired materials · TIER-self: "assembling the thousand reagents — tempering against the ten thousand toxins" *(framework-wrong)* · WARMTH: +maester (adversarial-dependent) · NOTE: *standing license* (indulgence formalized) · DOSE-LOG: active.
- **Threads:** PLANT[LEDGER], PLANT[FACTOR], PLANT[BELOW-STAIRS], PLANT[DOSE-LOG]. FIRE[ACQUISITION-DRIVE], FIRE[MAESTER-MARK→dependent], FIRE[NOTE→license]. Rung R0. Register HOLD→SPIKE. DN-2 opens.
- **Blast radius:** LARGE. Keystone — APPARATUS (the procurement network) feeds II.1 (the owned multinational — now a *reagent* empire); DOSE-LOG feeds II.6/III.3; FACTOR feeds I.9/II.1/II.9/III.10; LEDGER feeds I.9. The acquisition framing makes the empire a *side effect of her hunger* — a cleaner "she chose it" for II.1. Targets named here pay out at I.5 (weirwood / materials tour) + I.6 (pyromancers / wildfire). Removing it collapses the empire spine. *Cover (scholar vs. devotional vs. bare privilege) — OPEN, CL-004.*

### I.4 · the-laundress's-boy  `[CHARITY-DEPENDENT — re-home, CL-004 OPEN]`
> **Tension w/ CL-004 + CL-005:** she's now indifferent to the masses + runs no sick-house, AND there is **no healing hand** (energy-spend is forbidden — GUARD-1 rev-3). This beat survives as the *exception that proves she's human* — the ONE child in front of her she can't let die — but (a) it re-homes off the charity-ward context (→ a sick child in her household orbit), and (b) whatever she does for him is **mundane apothecary craft** (nursing, the right tisane, an antidote), NOT cultivation. The load-bearing pieces are the WARM root + the HINGE — now recast as **the craft cuts both ways** (the same still-room knowledge that kept the boy alive will quietly kill → I.7). **KEEP (re-homed, de-magicked).**
- **Beat:** Nurses a dying boy (no cover, no reagent value) three sleepless nights, certain it's karmic hygiene. He lives. She files it as cultivation merit; the reader sees she just couldn't watch a child die.
- **Deltas:** WARMTH +rootability anchor (the 80k root). HINGE established: her **mundane apothecary craft cuts both ways** — the still-room that mends is the still-room that kills (NOT a magical healing hand; GUARD-1 rev-3).
- **End-state vector:** age ~6 · RESOURCE unchanged · SOLITUDE unchanged · ARMOR: sealed but reader sees the human under it · CAPABILITY-real: poison-craft shown as dual-use (mundane medicine, NOT cultivation/energy) · WARMTH: **peak rootability** · DOSE-LOG: active.
- **Threads:** PLANT[WARM], PLANT[HINGE]. Rung **off-ladder** (the warm floor horror is measured against). Register **RECOVER** (lowest-volume scene). DN-3.
- **Blast radius:** MEDIUM-HIGH. The HINGE is the curdle's pivot (fires I.7: same hand now kills). The WARM root keeps Daenys from out-charactering the lead (Bk II). Echoed I.8. Remove it and I.7/I.8 lose their hinge and the reader loses the lead.

### I.5 · tempering-the-cauldron  *(the materials TOUR — CL-004)*
- **Beat:** Her **assay in full swing** — a systematic tour of every material she can get her hands on, each "tempering the cauldron" (the anti-Arya reveal: poison & pills, never a sword). The joke has a TRUE floor (GUARD-1 rev-3): genuinely-magical items **work** (a chip of **weirwood** smuggled from a godswood = a real, *strange* source; dragonglass faintly), mundane ones (dung, a plain pebble) give **nothing** — and she draws the *wrong lesson* from which is which (mis-reads it as "ingredient grade / purity," not "is it actually magical"). The **weirwood** get is a small heist of its own (HEIST-METHOD); old-gods matter behaves *differently* from fire-matter — a clue she misfiles. Helaena bond deepens; riddle-twins as equals.
- **Deltas:** CAULDRON retro-frames all antics. WEIRWOOD acquired + logged (old-gods/green magic registers, behaves oddly). HELAENA bond deepened (toward Bk III spend). No-eat behavior pre-justified (Harwin's future list). The source/non-source split established (real radiance from magical matter; inert mundane matter).
- **End-state vector:** age ~6–7 · RESOURCE T0 broadened · SOLITUDE unchanged · ARMOR sealed · CAPABILITY-real rising (real immunity + faint real cultivation off magical items, still hoarded) · TIER-self "cauldron tempering across antics" *(framework-wrong)* · WARMTH: Helaena **deepened** · 
- **Threads:** PLANT[NO-EAT], PLANT[HELAENA+]. FIRE[CAULDRON]. Rung R0 sustained. Register SPIKE (comic high of early Bk I). DN-5 (Helaena names a swallowed thing as a thing).
- **Blast radius:** MEDIUM. NO-EAT feeds II.2 (Harwin's list). HELAENA+ feeds III.7 spend. CAULDRON feeds III.5. Aemond-foil referenced here (the road-not-taken contrast).

### I.6 · the-furnace-sect  *(the PYROMANCERS — CL-004)*
- **Beat:** The named target lands: she reads the Alchemists' Guild — the **pyromancers** — as "a furnace sect," and goes after their **fire-craft / wildfire**. Something nearly burns; she eats a shard of *real* magic → 3-day "tribulation" fever → surfaces uncannily *changed*. Adults **scared, not charmed** for the first time.
- **Deltas:** WILDFIRE-SHARD eaten — the first genuine ring the *adults witness and fear* (the private founding ring was I.1, the private breakthrough was I.2; per GUARD-1 rev-3 the real strand activates on genuinely-magical materials). Pyromancer contact opened (a guild she'll keep tapping). Household sentiment turns (charmed → wary). The warm cage shows its bars.
- **End-state vector:** age ~7 · RESOURCE T1 (guild contact, wildfire) · SOLITUDE: *threatened* (the turn that triggers the septa's escalation) · ARMOR sealed · CAPABILITY-real: +1 real (a potent source ingested — wildfire is real magic; the gain is real, still hoarded; GUARD-1 rev-3) · TIER-self "realm breakthrough via tribulation" *(framework-wrong — it was a strong source, not a realm)* · 
- **Threads:** PLANT[BLACK-STONE-PRECEDENT] (the "ingest real magic → real wrong effect" template). FIRE[broken-clock-A] (pays out, isn't funny). Rung first **CHILL** (recovers but marked). Register SPIKE→CHILL.
- **Blast radius:** HIGH. The fever-fallout *is the cause* of I.10/I.11 (the septa's move to cloister → the note cashed). The precedent template looms over III.5 (black-stone reach). Remove/alter the wildfire incident and Lock I loses its trigger.

### I.7 · the-impurity-expelled `[FIRST-PEST]`
- **Beat:** A meddler moves to expose the still-room raids; he doesn't die loudly — a lingering flux, slow recovery, posted far from court, **never knows.** Saerys files him "an impurity the cauldron expelled."
- **Deltas:** PEST removed (first poison victim). The cold de-pesting reflex established.
- **End-state vector:** age ~6 (concurrent M3) · RESOURCE unchanged · SOLITUDE: *defended* (a threat to the machine removed) · ARMOR sealed · CAPABILITY-real: **first lethal use** of poison competence · TIER-self "qi-field purified" · WARMTH unchanged.
- **Threads:** PLANT[de-pesting reflex] (rhymes to II.8 Harwin balanced). FIRE[HINGE→R2] (the I.4 craft that kept the boy alive now quietly kills — same still-room, mundane). Rung **R2** (¾ comedy / ¼ chill). DN-6; DN-5 staging (no straight-man; prose shows the flux plainly).
- **Blast radius:** HIGH. R2 is the curdle ladder's load-bearing middle rung — sits between I.8's R1 (ward-child) and II.8's R3 (Harwin). Depends on I.4's HINGE. If removed, the curdle ladder loses a rung and the "same coldness, rising scale" engine skips.

### I.8 · impure-reagents  `[CHARITY-DEPENDENT — re-home "ward", CL-004 OPEN]`
> **Tension w/ CL-004:** "in her own ward" assumed the sick-house. Re-home to a sick child in her household/workshop orbit (e.g., the laundress's-boy echo). The R1 rung + GRIEF-REFUSAL seam are CRITICAL (→ III.8) and survive the re-home unchanged.
- **Beat:** A sick child *in her own ward* dies despite her elixir. She files it "impure reagents" — and the locked POV lets one un-meme-able image slip: *she remembers being the one who died, once* — then buries it.
- **Deltas:** ARMOR: **first visible seam** (the wound shows through to the reader). The literal account-book established as the one place a death is ever *entered*.
- **End-state vector:** age ~7 · RESOURCE unchanged · SOLITUDE unchanged · ARMOR: **cracked-visible-to-reader** (still sealed to her) · CAPABILITY-real unchanged · WARMTH: the I.4 warmth paid against (we see the wound she doesn't).
- **Threads:** PLANT[GRIEF-REFUSAL] (the pre-emptive-refusal mechanic, surfaced once). Rung **R1** (ward-child filed cold — made personal). Register RECOVER-INTO-COLD. DN-2.
- **Blast radius:** CRITICAL for Bk III. GRIEF-REFUSAL is the exact mechanic that fires at III.8 (the blank line). The "account-book = the one place a death is entered" rule *pays the T1 break*. Re-touches I.1 funeral seam. If altered, the III.8 break loses its planted mechanism.

### I.9 · the-fourth-bill `[AGENCY-PATCH]`
- **Beat:** Reconciling books, she notices the loop (factor+maester+below-stairs compounded her bills into 3 unauthorized routes). First read: cosmological. Two pages later — the turn — she sees the machine and **signs a fourth bill she doesn't need, to feed it.** Accident → intent.
- **Deltas:** LEDGER → steering wheel. EMPIRE seed (now partly *chosen*). FACTOR scaled (first bill compounds visibly).
- **End-state vector:** age ~8 · RESOURCE T1, reach *compounding* · SOLITUDE: rising (network extends her without her presence) · ARMOR sealed · CAPABILITY-real: logistics agency now conscious · TIER-self "the spiritual network self-propagates" · LEDGER: **active steering instrument**.
- **Threads:** PLANT[EMPIRE]. FIRE[LEDGER], FIRE[FACTOR→scaled]. Rung R0 (pure engine). Register SPIKE. T3.
- **Blast radius:** HIGH (cross-book). EMPIRE feeds II.1 (discovers she owns a multinational — but post-I.9 the last year was deliberate). The agency-pivot is the thematic patch that makes her an agent, not a leaf on a current. If removed, II.1's "she chose it" reading collapses.

### I.10 · the-sealed-parchment
- **Beat:** The I.6 wildfire fallout matures; the septa prepares to send her to a sept. She talks her doting father into a *sealed* grant — "the princess shall have what she requires for her good works." The warm cage hardens into a tool.
- **Deltas:** NOTE → **sealed grant** (genuine impression). **Jaehaerys (King/father):** the warm-gift chapter (gives the master key *out of love*; was Viserys — CL-002). Saerys: stops being his daughter, becomes his auditor.
- **End-state vector:** age ~8–9 · RESOURCE T1 · SOLITUDE: *near-total* (a sealed instrument that overrules chaperones) · ARMOR sealed · WARMTH: **GIFT:JAEHAERYS** at its final warm form (before the father-king spend) · NOTE: **sealed, on her person**.
- **Threads:** PLANT[ORPHAN-SEAL] (THIS exact seal → III.1 orphaned → III.10 heist), PLANT[GIFT:JAEHAERYS]. FIRE[NOTE→sealed]. Register HOLD. DN-2.
- **Blast radius:** CRITICAL (longest arc in the work). The seal is one prop across three books (I.10→III.1→III.10). The **GIFT:JAEHAERYS** is the warm-before-spend for the father-king's death (the spend chapter re-homes from baseline III.1 to Jaehaerys's 103 AC death — Book II per the pinned timeline; CL-002 downstream item, location TBD). *Residual risk (baseline): weakest of the gift→spend pairs (warmth already half-converted) — now eased by the I.1 miracle-child tenderness.*

### I.11 · paper-wins `[LOCK I · rung 1]`
- **Beat:** Septa holds a true accusation; Saerys produces the sealed parchment; the master key overrules every chaperone below the King. **Paper wins.** Legally ungovernable; thinks she achieved a breakthrough.
- **Deltas:** SOLITUDE → **won at local scale** (legal ungovernability). Septa folded into Lock I (defeated; no standalone saga). The mechanism's audit-rung-1 cleared.
- **End-state vector (BOOK I CLOSE):** age ~9 · RESOURCE T1 (KL-bounded) · SOLITUDE: **ungovernable in the Red Keep** · ARMOR sealed (descent not yet begun — book boundary holds) · CAPABILITY-real: lethal-in-the-unwatched-domain, immunity well underway; real cultivation compounding off acquired materials · TIER-self "breakthrough achieved" · WARMTH: Helaena + Jaehaerys open (gifts banked); maester dependent · NOTE: Lock I fired, kept · APPARATUS: workshop + procurement network mature, compounding.
- **Threads:** FIRE[NOTE→Lock I]. Rung R0 (triumphant farce; T4 boundary holds). Register SPIKE (comic apex + mechanism dress-rehearsal #1). DN-2.
- **Handoff → Book II:** the note can't reach past King's Landing; rarer reagents/poisons need her own supply lines → the roads open. Instrument: the I.3 bill of exchange. Appetite: the cauldron, always wanting a higher grade.
- **Blast radius:** Sets Bk II's opening state (owned-but-undiscovered network, ungovernable-locally, gifts banked). Raises the mechanism to rung-2 (an ocean).

---

## Book I → II/III dependency bridge (what ripples *beyond* Book I)

These Book-I plants/gifts have downstream firings. **Any Book-I edit must check this table** —
if an edit removes or alters the left column, the right column is the orphan list.

| Book-I origin | Fires downstream at | If Book-I origin changes… |
|---|---|---|
| PLANT[NOTE] I.1 *(aftermath)*→I.3→I.10 | III.1 (orphaned seal), III.10 (heist mech #3) | the entire ending heist loses its seal |
| PLANT[HEIST-METHOD] I.2 *(new — sight→plan→implement→reward)* | I.11 (Lock I, rung 1), II.10 (Lock II), III.10 (Lock III) | the three Locks lose their origin / the "she's always run heists" through-line |
| PLANT[MAESTER-MARK] I.2 *(new)* | I.3 (out-administers a man she's robbed for years) | the keystone maester-takeover loses its head-start |
| PLANT[ACQUISITION-DRIVE] I.1→I.2→I.3 *(new — replaces BLOOD-PATH)* | I.5 (weirwood/tour), I.6 (pyromancers), II.1 (reagent multinational), III.5 (dragon-corpse feast) | the engine of the whole book (and the "she chose it" empire) loses its motor |
| PLANT[CAULDRON] I.1 | III.5 (curdle apex / black-stone reach) | the curdle ladder loses its frame-for-frame top |
| PLANT[SYMPATHETIC-RESONANCE] I.1 *(new)* | III.5 (she needn't take the whole field — but does) | the curdle apex loses its "didn't have to" knife |
| PLANT[REINCARNATION-SICKNESS] I.1 *(new)* | soft: I.6 fever / III.3 immunity | the death-refusal origin + immunity rhyme thin |
| PLANT[DOSE-LOG] I.3 | II.6 (deepened), III.3 (failed assassination) | III.3 "she's immune" payoff is unearned |
| PLANT[FACTOR] I.3 | II.1, II.9, III.10 | factor-and-paper engine has no origin |
| PLANT[LEDGER]+EMPIRE I.3/I.9 | II.1 (owns a multinational) | II.1 discovery and "she chose it" both collapse |
| HINGE I.4 + curdle rungs I.7/I.8 | II.8 (R3 Harwin), III.5 (R4 dragons) | the "same coldness rising" engine skips rungs |
| PLANT[GRIEF-REFUSAL] I.1 *(death-refusal, literal)* + I.8 | III.8 (the blank line, T1 — cultivation can't out-refine *this* death) | the one break loses its planted mechanism |
| PLANT[BLACK-STONE-PRECEDENT] I.6 | II.6, III.5 | broken-clock guard for the black-stone reach |
| GIFT:HELAENA I.5 *(was I.1/I.5; I.1 instance dropped)* | III.7 (warm spot out) | her death stops landing as loss |
| GIFT:JAEHAERYS I.1 *(aftermath)* + I.10 *(was GIFT:VISERYS — father role moved to the King)* | the father-king's death (103 AC, mourned) → un-fully-grieved (curdle/armor) | the father-king spend has no warm bank *(stronger: miracle-child tenderness addresses baseline residual-risk #4)* |
| WARM root I.4 | sustains reader investment through Bk II | Daenys out-characters the lead |

**Cross-book invariants (the three rhymes — do not break without re-architecting):**
1. **One method, three Locks** at rising audit-difficulty: septa (I.11) → ocean/clerk (II.10) → Crown+death (III.10).
2. **Curdle ladder, one gesture rising:** R0 **drained living egg** (I.1) → R1 ward-child (I.8) → R2 pest (I.7) → R3 Harwin (II.8) → R4 dragons (III.5). *(R0 strengthened: living→dead, not dead-relic; GUARD-3 keeps it laugh-now / horror-later. III.5 rhyme is now exact: one living beast drained → a sky of them.)*
3. **Gift→spend:** every casualty gets a warm present-tense chapter BEFORE its cold spend. (Bk I banks **Jaehaerys** (father-king) + Helaena (sister).)

---

## Change-propagation protocol (the checklist I run when a note lands)

Notes arrive **messy, fragmentary, and not necessarily cohesive** — that is expected and fine.
Coherence is the ledger's job, not the input's. When you drop ideas, I execute this and report back:

0. **Intake / triage** — parse the dump: sort each fragment to the chapter(s) and entit(ies) it
   touches; separate firm intent from loose musing; surface internal contradictions and gaps
   *back to you as a short list*; and ask only the few questions that genuinely block integration
   (everything else I resolve with a stated default you can override). Nothing is applied at this
   step — triage is a read-back so you can confirm I caught your intent before I propagate.
1. **Slot** — integrate the (triaged, confirmed) note into the target chapter's Beat + Deltas.
2. **Recompute** — update that chapter's end-state vector, then ripple the recomputed state through every later chapter's vector (Book I, and into II/III where the bridge table connects).
3. **Thread audit** — two passes:
   - **Mechanical:** run `python3 scripts/check-threads.py <outline> --config design/run-02/thread-config.txt`.
     Catches orphaned plants, unplanted fires, gift→spend order violations, missing curdle rungs.
     A note that introduces a NEW break makes it FAIL. (If a new token is by-design non-1:1, add it
     to `thread-config.txt` with a reason — never to silence a real orphan.)
   - **Judgment:** the checks the script can't make — does the change break a **gift→spend** warmth
     beat, the **frame-for-frame** curdle rhyme, a **hard fence** (setting-blind / never-martial /
     clock-stays-broken / idiot-savant / one-crack / no-dragon), a **FROZEN beat**, the **three-Locks
     rhyme**, or the register sequence? For anything beyond a local fix, this is the `dramatist`'s
     call (structure/shape) and `audience`'s (taste); `auditor` for state/consistency drift.
4. **Flag** — surface every break with options: *re-plant elsewhere · re-route the payoff · accept
   the break (and what it costs) · escalate (FROZEN/fence touch)*. Fence/FROZEN touches are ratified
   explicitly (convergence-process.md: "ratify smuggled premises") with a written GUARD.
5. **Re-thread** — propose the minimal **required** fixes + a separate **Opportunities** block
   (ripple scope = opportunistic). On your go: write the changes into this ledger, append the
   enrichment-round digest to `convergence/convergence-ledger.md`, and re-run the checker to confirm
   clean. Dispatch `screen-writer` to re-author the affected chapter bodies + `dramatist` for scoped
   re-validation when the change is more than a local touch.

**Conventions:** I do not silently apply a change that breaks a hard fence or a FROZEN beat — I
flag and ask. I keep this ledger as the single source of truth for the revised plot; the
baseline `convergence/` files are preserved untouched as the pre-change record until you ask to
re-fuse them.

**Ripple scope: OPPORTUNISTIC (set 2026-06-06).** On each note I make the minimal consistency
fixes AND propose improvements the change opens up (better placements, tighter rungs, salvaged
warmth), kept in a clearly separated "Opportunities" block so each can be accepted or rejected
independently of the required fixes.

---

## Change log

### CL-001 · I.1 rewrite (2026-06-07)
- **Note:** I.1 re-conceived — dying reincarnated **infant**; **living** egg from **Alicent** (unsanctioned, against the King's withheld blessing); empirical cultivation discovery via **sympathetic resonance** (chip + blood, willing the part to be the whole); egg **drained dead**; survives "touched."
- **Rulings:** Q1 cultivation = **real-but-inert** (a mix of "it works" + "delusion" → **GUARD-1**, supersedes "clock stays broken"). Q2 egg **drained dead** → **GUARD-3** (curdle R0 stays a laugh at the time; horror retroactive). Q3 FROZEN inversion **re-framed** heal→fuel → **GUARD-2** (ratified).
- **Applied to ledger:** I.1 entry rewritten (title → `a-baseline`); fences updated (GUARD-1); GUARDS section added; curdle R0 + III.5 frame-rhyme updated (living→dead); NOTE re-homed to I.1 aftermath; new plants SYMPATHETIC-RESONANCE + REINCARNATION-SICKNESS (bridge rows added); GRIEF-REFUSAL re-flavored as literal death-refusal (seeded I.1 + I.8); GIFT:VISERYS now seeded I.1 aftermath (strengthens baseline residual-risk #4); I.6 distinguished as the first *public/feared* ring; entity registry rows updated (Saerys, Viserys, Alicent split from Otto, cradle-egg, Cauldron, +2 concept rows).
- **OPEN (defaulted, overridable):** Alicent love→horror reversion (vs. a new warm bond the war spends); Helaena cradle-witness beat (currently dropped — gift now first planted I.5); exact infant age + the "traitorous baby fingers" motor-control comedy framing; final title pick (`a-baseline` vs `the-frequency`).
- **Downstream still to propagate when those chapters are touched:** III.5 (sympathetic "didn't have to" + drained-living rhyme), III.8 (death-refusal now literal — stronger), III.3 (immunity = mithridatism + *masked* real durability, GUARD-1), Alicent arc across Book I.
- **Mechanical re-check:** baseline `convergence/` outline is unedited (this revision is staged in the ledger), so closure re-check via `check-threads.py` fires at **re-fuse** (when the new I.1 is written into a 30-ch tokenized doc). New tokens' fires are pre-scheduled in the bridge so re-fuse will PASS.
- **Ratification mirrored to:** `convergence/convergence-ledger.md` (Round 4 — run-02 enrichment).

### CL-002 · era + cultivation ruling (2026-06-07)
- **Note:** (a) move the era to **Jaehaerys I's reign**; **Jaehaerys = King/father**, **Alicent = Queen/mother**, **Viserys** demoted to a young **nephew**. (b) **Cultivation works** — magic/blood/fire/dragon magic is real; no ambient qi but objects/people/substances radiate; internalizing tempers the body; she *could* fight but hoards (spending slows growth); ends up an **unintentional blood-cultivator**.
- **Rulings → GUARDS:** **GUARD-1 rev-2** (real-but-hoarded + framework-wrong + blood-path; supersedes rev-1 "real-but-inert"); **GUARD-4** (era + family tree fixed). "Never martial" fence → "**non-combatant by choice**." New broken clock: right it's real, wrong about the framework (xianxia model over canon blood/fire/death magic).
- **New authority file:** `timeline-and-family-tree.md` — AU-vs-canon dates, the family tree, the magic rules, and the one open fork (series end-date).
- **Pinned:** Saerys b. **~84 AC**; Book I = 84–93 AC (long peace, peak dragons); Jaehaerys d. 103 AC; Dance 129 AC.
- **Applied to ledger:** fences line + axes (CAPABILITY-real two strands / TIER-self framework-wrong / POLITICAL CLOCK = long peace) updated; GUARD-1 rewritten + GUARD-4 added; entity registry (Jaehaerys added as King/father; Viserys→nephew; Alicent→Queen; Otto/Aemond recast; Helaena→sister; Saerys row); I.1 (Jaehaerys + blood-cultivation founding); I.3 (BLOOD-PATH sick-house undertone); I.5 (magical-vs-mundane antic split); I.6 (real source-gain, not inert); bridge rows GIFT:VISERYS→GIFT:JAEHAERYS + new BLOOD-PATH; gift→spend invariant (banks Jaehaerys + Helaena).
- **OPEN (defaulted, overridable):** **series end-date fork** (Dance 129 AC *recommended* vs tighter AU — the one real open call); Viserys relation (nephew default); Alysanne (written out, default); Alicent arc (love→horror default).
- **Downstream to propagate when touched:** III.5 (dragon-blood feast = blood-path apex), III.3 (real tempering + mundane dosing both mask immunity), II.x (Jaehaerys's 103 AC death as the father-king spend), Daenys/Aemond arcs under the new family tree, the blood-magic-secrecy stakes across II/III.
- **Mechanical re-check:** baseline `convergence/` outline unedited; closure re-check deferred to re-fuse (new tokens BLOOD-PATH/SYMPATHETIC-RESONANCE/REINCARNATION-SICKNESS pre-scheduled).
- **Ratification mirrored to:** `convergence/convergence-ledger.md` (Round 5).

### CL-003 · insert I.2 `the-pantry-heist` (toddler bridge) (2026-06-07)
- **Note:** infancy→age-6 was too big a jump ("halfway to adulthood in Westeros"). Insert a **toddler-stage** chapter: a planned-out raid on the maester's pantry, structured **sight → plan → implement → reward**, ending on an **"oh shit"** when she **breaks through** (uncontrolled, nearly fatal/exposing).
- **Applied to ledger:** **renumbered Book I** — old I.2–I.10 shifted +1 to **I.3–I.11** (descending, word-boundary-guarded; II./III. refs verified intact); inserted **I.2 the-pantry-heist**; per-chapter header now I.1–I.11 (+11-ch divergence note); maester registry First → I.2 (MAESTER-MARK); new bridge rows PLANT[HEIST-METHOD] (→ I.11/II.10/III.10 Locks) + PLANT[MAESTER-MARK] (→ I.3); fixed a CL-002 leftover (GIFT:VISERYS → GIFT:JAEHAERYS in the now-I.10 sealed-parchment chapter).
- **What it plants:** HEIST-METHOD (the three Locks now have a toddler origin); the live "objects radiate → ingest source → real breakthrough" mechanic (GUARD-1 rev-2); breakthroughs-have-teeth as the *private* rehearsal of the I.6 furnace-sect *public* scare; the toddler motor-comedy (DN-7) that the I.1 open item ("traitorous baby fingers") now lands in.
- **Off the curdle ladder** (a stolen jar, no living victim) — R0 egg (I.1) stays the ladder's first rung.
- **OPEN (defaulted, overridable):** the stolen item's identity (a genuinely-magical reagent in the maester's stores — pick at draft); exact toddler age (~2–3); how visible the near-exposure gets; chapter title (`the-pantry-heist` vs `the-first-job`).
- **Mechanical re-check:** ledger-internal only (baseline `convergence/` outline keeps 10-ch numbering; final integer numbering settled at re-fuse). New tokens HEIST-METHOD/MAESTER-MARK pre-scheduled in the bridge.
- **Ratification mirrored to:** `convergence/convergence-ledger.md` (Round 6).

### CL-004 · step back from charity + retract the blood-path (2026-06-07)
- **Note:** (a) **step back from charity** — she's indifferent to the masses she can't see ("mortals," beneath her); no charity sick-house as her engine. (b) Her real drive is **acquisition** — chasing other resources; next targets **weirwood** + **pyromancers**, plus a broad **tour of materials** to find what registers. (c) **She is NOT a demonic/blood cultivator — she does not cultivate people** (retracts the CL-002 blood-path).
- **Rulings → GUARDS:** **GUARD-1 rev-3** (supersedes rev-2): cultivation is fuelled by **magical objects + substances ONLY**; people are never a source; *materials-only / never-demonic* added to the hard fences. Her own I.1 blood = a one-off catalyst on an object, firewalled. New broken-clock example: she ingests poisons expecting them to register; they don't → real mundane immunity, mis-filed as tempering.
- **Applied to ledger:** GUARD-1 rewritten rev-3; fences + APPARATUS axis + CAPABILITY-real updated; **I.3 re-conceived** `the-charitable-princess` → `the-collector-princess` (charity sick-house → workshop + procurement network; acquisition keystone; maester from mark → dependent supplier); I.1 (BLOOD-PATH seed → **ACQUISITION-DRIVE** seed; blood-catalyst firewalled); I.5 (weirwood + the materials tour foregrounded); I.6 (pyromancers foregrounded); apparatus/props (sick-house → workshop + materials-assay rows); bridge (BLOOD-PATH row → **ACQUISITION-DRIVE**); Braavosi-factor + I.11 close de-charity'd; timeline §3/§4 magic rules rewritten (materials-only, not demonic); curdle framing corrected (cold instrumentalism + consuming magical *creatures*, never people).
- **FLAGGED, not silently changed:** **I.4 (laundress's-boy)** + **I.8 (ward-child)** are `[CHARITY-DEPENDENT]` — both carry the load-bearing **WARM root + HINGE + GRIEF-REFUSAL** (→ III.8). Recommend KEEP, re-homed off the charity ward to her household/workshop orbit. **Needs a principal call.**
- **OPEN (defaulted, overridable):** the new keystone's **cover** (scholar-princess *default* / devotional-relics / bare princess-privilege); the I.4/I.8 warm-thread re-home (keep-recommended); the I.3 title (`the-collector-princess` vs `the-magpie` / `the-acquisitions`).
- **Curdle ladder:** unaffected — it was never about cultivating people (R0 egg + R4 dragons = magical *creatures*; the pest/Harwin rungs = cold *poison* kills). The retraction actually cleans it up.
- **Mechanical re-check:** ledger-internal (baseline outline untouched; ACQUISITION-DRIVE pre-scheduled in the bridge). 
- **Ratification mirrored to:** `convergence/convergence-ledger.md` (Round 7).

### CL-005 · no healing hand — energy is never spent outward (2026-06-07)
- **Note:** "no healing hand. that would require an external energy application." A magical heal is *expenditure*, which the hoarding rule forbids — so it's a fence breach, not a flavour choice.
- **Ruling:** GUARD-1 rev-3 strengthened — **no external energy application of any kind, including NO magical healing**; hoarding is absolute (no fighting, no healing, no outward effects on the page). Added to the hard fences. Any mending she does is **mundane apothecary craft** (medicine/antidotes/nursing), never cultivation.
- **Applied:** GUARD-1 + fences + timeline §3 updated. **I.4** recast — the warm root survives but the save is **mundane apothecary craft**, not a healing hand; the HINGE recast from "healing-hand = killing-hand" to **"the craft cuts both ways"** (same still-room mends and kills). **I.7** + I.4 deltas/CAPABILITY updated to match. (Token HINGE unchanged → thread graph intact.)
- **Note:** GUARD-2's "heal→fuel" is a *different* sense (the egg given to save the infant, which she taps for fuel) — untouched.
- **Mechanical re-check:** `book-i-outline.md` re-checked → PASS (HINGE I.4→I.7 still closes).
- **Ratification mirrored to:** `convergence/convergence-ledger.md` (Round 8).
