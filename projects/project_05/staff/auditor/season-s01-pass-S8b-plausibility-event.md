# Audit Report — Season s01 Pass S8b: Event-in-World Plausibility
# schema: schemas/audit-report.schema.md
# auditor: season-s01-pass-S8b-plausibility-event
# target: active-project/theater/proto-lines/s01.bones.md + active-project/staff/screen-writer/s01-content-beats-draft.md
# date: 2026-05-11
# pass: Phase 3 Sweep A — S8b Event-in-World Plausibility

---

## Scope Statement

This audit checks whether each of the 26 content beats, as rendered in the bones, is plausible as an *event that would actually occur* given the active condition cards, series laws, lore, and location constraints. S8b is distinct from S8a (character plausibility): a character can behave plausibly in executing an implausible event. The question here is whether the world mechanics permit the event to occur at all.

Condition cards loaded:
- cond-shard-behavioral-weight
- cond-no-parahuman-infrastructure
- cond-smallfolk-political-physics
- cond-feudal-hierarchy-law
- cond-westerosi-customary-authority-125ac
- cond-fauna-control-rules-125ac-addendum
- cond-reincarnation-mechanics-125ac
- cond-crownlands-superstition-frame-125ac
- cond-clinical-self-erasure
- cond-series-tone-constraints-125ac

S8a report: does not exist at audit time. Split-verdict adjudication under URI-016 cannot be applied; no S8a report to cross-reference. Noted.

---

## Five Specifically-Tasked Plausibility Questions

### Q1 — Hightower apparatus opening intelligence files on Crownlands smallfolk in 125 AC pre-Dance: plausible given cond-feudal-hierarchy-law + cond-westerosi-customary-authority-125ac?

**PLAUSIBLE.**

Supporting warrant:
- cond-westerosi-customary-authority-125ac explicitly states the Hand of the King's administrative apparatus manages "special inquiries" and that "Otto Hightower's intelligence-architect function means his apparatus is more actively interested in unusual persons than a passive administrative apparatus would be."
- The card further specifies: "A Taylor who shows up in Gold Cloak records gets faster attention from the Hand's level than she would under a less intelligence-minded Hand." This implies the apparatus is actively tracking unusual persons below Gold Cloak formal detention level.
- The three-tier escalation in beats 5 / 18 / 20 / 25 maps correctly to the authority architecture: (a) lord's-man quarterly pass creating an informal note (village-claim arc); (b) low-tier Hightower clerk building a population register of non-native Flea Bottom residents (beat 18); (c) second clerk conducting a behavioral-profile inquiry at the apothecary (beat 20); (d) senior operative sending a formal written-account request through the tanner-elder (beat 25). Each step is within the apparatus's described function.
- cond-feudal-hierarchy-law establishes that the lord's administrative record-keeping is routine: "Early stages invoke the lord's administrative record-keeping and monitoring authority." The Hand's apparatus is the Crown-direct equivalent in KL.
- The beats correctly do not have Taylor formally detained, charged, or processed — the apparatus is operating at the observation and registration level, which is explicitly within its authority pre-Dance.

No violation. The events fit the described institutional mechanics.

---

### Q2 — Range-expansion mechanics: within cond-shard-behavioral-weight + cond-no-parahuman-infrastructure constraints?

**PLAUSIBLE.**

Supporting warrant:
- cond-fauna-control-rules-125ac-addendum establishes: story-open range 300m; organic ceiling ~1.5km by late s2; range expansion is "organic and legible to the audience" through use; expansion is a "threshold-event, not continuous" at the first expansion, then "incremental" at beat 19.
- The beat-by-beat expansion: beat 2 (300m established), beat 11 (~330m, threshold event, overnight network operation), beat 14 (~400m, sustained autumn relay), beat 19 (~500m, incremental through early winter), beat 24 (~600m, sustained overnight Fish Gate operation). This is a five-step progression across 26 beats, with each expansion preceded by a described operational trigger. This is consistent with the addendum's "organic through use" rule.
- The addendum explicitly states "Range expansion is not a quiet background process. It is a visible power-progression with associated behavioral cost." The beats include physiological cost notation (headache, onset, duration) at each step. Consistent.
- cond-no-parahuman-infrastructure prohibits the Shard buffering that would make the cost curve disappear. The cost curve is present and logged at each expansion. No violation.
- cond-shard-behavioral-weight governs judgment-distortion, not power parameters. It does not constrain range expansion mechanics. No interaction issue.

No violation. Range expansion as structured is mechanically permissible.

---

### Q3 — Insect-network coordination at Flea Bottom scale: within cond-fauna-control-rules + 125ac-addendum constraints?

**PLAUSIBLE with one FLAG (see fault-001).**

Supporting warrant:
- The species in the bones: flies (beats 26, 96, 107, 119, 137, 143, 187, 214, 219, 238, 240, 266, 338, 371, 384, 438, 461, 462, 471); beetles (beats 27, 96, 106, 112, 130, 160, 211, 239, 267, 287, 296–298, 310, 346, 350, 366, 370, 384, 403, 412, 416, 417, 440, 444, 484); wasps (beats 29, 97, 121, 190, 215, 216, 247, 255, 267, 319, 345, 384, 439, 502); spiders (beats 108, 122, 212, 217, 257, 319, 347, 441). These are all plausible urban Flea Bottom insects and arachnids — no exotic or implausible species.
- The coordination tasks performed (perimeter relay, positional data on persons, acoustic relay of conversation, visitor detection) are consistent with the base card's described capabilities: insect-level perception (breath, body temperature, proximity, physical state), partial acoustic access through beetle colonies.
- The spatial claims are consistent with location cards: loc-flea-bottom-base establishes ~250m to the apothecary, within the 300m story-open radius. The market-side junction, Fish Gate margin, and south-wall colony are within the described operational radius.

**FLAG — fault-001 (below):** Beats 108/122 deploy spiders in ceiling corners of the apothecary's upper room for relay. The loc-eastern-quarter-apothecary card lists "Spider presence in ceiling corners (consistent)" as an established through-wall observation point. This is consistent. However, beat 108 ("the spiders spread the ceiling corners") and beat 122 ("the spiders relay the room") appear in the bones without prior establishment that Taylor controls the ceiling-corner spiders versus passively uses spiders already present. The distinction matters because cond-fauna-control-rules-125ac-addendum specifies range parameters: "spreading" implies active command deployment rather than passive use of existing populations. This is a fine-grained execution flag, not a structural violation, but it warrants checking at line-level to ensure "spread" does not imply deploying from outside the apothecary (which would require her to be within 300m — she is — but the acoustic-access-through-wall distinction should be maintained).

Classified: FLAG (execution-level; not a structural implausibility).

---

### Q4 — Customary wage-claim mechanism: accurate to cond-westerosi-customary-authority-125ac?

**PLAUSIBLE.**

Supporting warrant:
- cond-feudal-hierarchy-law establishes that informal custom carries weight even without legal title: "certain practices have customary protection even without legal backing." The card also specifies "unlawful collective action" as a concern but does not prohibit individual customary claims.
- cond-westerosi-customary-authority-125ac and cond-feudal-hierarchy-law together establish the customary framework. A daughter's wage obligation to her family under Crownlands customary practice (beat 13) is consistent with a society where a smallfolk woman's legal visibility runs through her family and where informal credit/obligation mechanisms govern economic life (cond-smallfolk-political-physics: "Extended in kind, tracked in obligation-memory rather than ledgers").
- The beat does not claim formal legal enforcement mechanism — it claims customary practice: "the family has a claim on the girl's labor under Crownlands customary practice." The claim formalizes (beat 23) when it reaches the lord's-man record, which is explicitly within the lord's administrative record-keeping authority.
- The mechanism of "a daughter working in the city owes a portion of her wages to the family that raised her" is consistent with the period and setting — it reflects the customary dependency relationship the cards describe, where a smallfolk woman's economic activity is tied to household and kin claims.
- The lord's-man recording the claim (beat 23) is plausible: the lord's administrative apparatus records customary obligations as part of its rent and labor management function. This does not require a formal legal proceeding.

No violation. The customary wage-claim mechanism is consistent with the world's legal and social physics.

---

### Q5 — Lord's-man / reeve / quarterly-pass: Crownlands administrative reality?

**PLAUSIBLE.**

Supporting warrant:
- loc-tanner-village card explicitly establishes: "Lord's man arrives quarterly for rent collection. Village events reach the lord's record." This is a direct authorization from the location card.
- cond-feudal-hierarchy-law establishes the lord's tax collection right ("the annual and seasonal extraction") and the lord's administrative apparatus function ("administrative record-keeping").
- The reeve as membrane between informal network and official apparatus is established in cond-smallfolk-political-physics: "The local reeve sits at the membrane between the informal network and the official apparatus." The reeve transmitting background village gossip to the lord's man on a quarterly pass (beat 5) is a direct expression of this described function.
- The lord's-man in Flea Bottom (beats 71–77, 232–244) is a KL-adjacent enforcement agent: this role is consistent with cond-westerosi-customary-authority-125ac's description of the lord's administrative apparatus operating through the Crown-direct chain. The bones' depiction of the lord's-man entering the village, speaking to the reeve, opening a record book, writing an entry, and exiting (bones 71–77) is a minimal and accurate depiction of quarterly administrative contact.

No violation. The lord's-man / reeve / quarterly-pass mechanism is directly supported by the location card and condition cards.

---

## Beat-by-Beat Verdicts

**Beat 1** — Taylor wakes, tanner-father runs behavioral-tell audit at morning meal, "Tya who came back wrong" category closes.
PLAUSIBLE. Consistent with cond-crownlands-superstition-frame-125ac (Stranger-leavings frame, behavioral-wrong register). Community response to the returned-wrong body is accurate to the described superstition frame. The father's behavioral-tell audit (salt, dogs, door-angle) is plausible domestic observation by someone looking for evidence of what category to assign.

**Beat 2** — Taylor inventories 300m insect range from yard; shard runs local-only.
PLAUSIBLE. 300m is the defined story-open range per cond-fauna-control-rules-125ac-addendum. Local-only, no network, no multiplier — consistent with cond-no-parahuman-infrastructure (no Shard buffering). Walking a perimeter within her range from a single position is within defined capability.

**Beat 3** — Tanner-mother's three-note private song; Taylor does not finish it; mother's foreclosure completes.
PLAUSIBLE. Consistent with cond-crownlands-superstition-frame-125ac ("Tya's personal memories are absent, not suppressed"). Taylor has no episodic memory of Tya's relationships. Failing to complete a song known only to Tya is expected behavior, not a flaw in the event. The mother running her own identity-test via a private reference is a plausible action for someone who suspects the body is not the person she knew.

**Beat 4** — Tanner-father reorders labor distribution, withdrawing Taylor to functional-slot-at-edge.
PLAUSIBLE. Consistent with cond-smallfolk-political-physics (collective compliance as armor; household authority distribution). The father's covert structural withdrawal — routing rather than declaration — is accurate to how small-community authority operates under the conditions described. No event here requires special institutional mechanics.

**Beat 5** — "Tya who came back wrong" category reaches lord's-man on quarterly pass; reeve mentions it as background; lord's man records "tanner's daughter, fever-return, behavior irregular."
PLAUSIBLE. Supported by Q5 analysis above. Reeve function (cond-smallfolk-political-physics), lord's-man quarterly pass (loc-tanner-village), and administrative record-keeping (cond-feudal-hierarchy-law) all authorize this event. The informal channel — reeve mentions as background — is the correct transmission mechanism.

**Beat 6** — Taylor chooses KL; tanner-elder places her in Flea Bottom labor web as "reliable and strange" via trade-reference; she maps 300m radius in 48 hours and identifies the apothecary.
PLAUSIBLE. The elder's trade-reference routing is consistent with cond-smallfolk-political-physics (informal credit network, whisper chain as organizing substrate). The 300m radius covering the apothecary at ~250m is consistent with loc-flea-bottom-base (geometry confirmed). Mapping in 48 hours is within range capability — no expansion required, just systematic perimeter walk.

**Beat 7** — 300m sphere catalogs block, junction, Fish Gate margin, apothecary upper room at 250m, broken maester's working pattern via south-wall beetle colony.
PLAUSIBLE. Consistent with loc-flea-bottom-base (lists the through-wall observation points at the apothecary including "Beetle colony in gap between south wall's inner plaster and outer stone"). Range geometry consistent. The catalog-as-primary-action is within cond-fauna-control-rules operational scope.

**Beat 8** — Dock-runner moves cargo through shifted Watch pattern; Taylor observes but does not warn; runner recalibrates; runner approaches via elder for Watch-pattern information; first transactional exchange.
PLAUSIBLE. The Watch patrol shift as observable-by-insect-network is plausible: street-level patrol movements are within range. Taylor's non-intervention is consistent with cond-shard-behavioral-weight (direct-action preference, but also self-concealment logic). The runner's approach via the elder is consistent with cond-smallfolk-political-physics (information travels through whisper chain and labor-web nodes; elder is the membrane). The transactional exchange structure is accurate to the informal credit economy described.

**Beat 9** — Tanner-family first KL visit; father observes the half-second strategic-scan; family leaves with a new problem they cannot name.
PLAUSIBLE. The family visiting for trade is a plausible Crownlands smallfolk activity (market-side junction). The father's observation of an unfamiliar behavioral tell is consistent with his established role as behavioral-tell auditor (beat 1). The family not having a frame for "strategic scan" is consistent with cond-crownlands-superstition-frame-125ac (they have categories for body-wrong, not for tactical cognition). The event as a whole is a plausible domestic encounter.

**Beat 10** — Taylor maps whisper chain architecture; begins routing anonymous weather-pattern and Watch-movement data through the chain; chain accepts; she reads as "odd but functional."
PLAUSIBLE. cond-smallfolk-political-physics describes the whisper chain as emergent and resistant to disruption. Routing anonymous information through it is plausible if the information is useful and untraceable to a specific source. The "odd but functional" register is consistent with cond-crownlands-superstition-frame-125ac (Stranger-leavings frame has not reached Flea Bottom; the city's "touched" category is crowded with other candidates; urban tolerance for strangeness is higher). The community accepting useful anonymous information without demanding attribution is consistent with how the informal credit economy manages useful information.

**Beat 11** — Range expands ~30m during sustained overnight network operation; marks new edges; logs physiological cost (headache, four-hour onset, six-hour duration).
PLAUSIBLE. First range expansion event. cond-fauna-control-rules-125ac-addendum: "threshold-event, not continuous." Overnight sustained operation as trigger is consistent with the addendum's description of high-density operation as the expansion mechanism. 30m expansion from 300m to ~330m is a plausible small-threshold event. Physiological cost logging is required by the addendum ("prose must register range expansion as it happens... through operational notes in her internal register"). Consistent.

**Beat 12** — Flea Bottom family evicted from two-room dwelling; lord's-man enforcement action; Taylor's network covers the event; she observes but does not intervene; logs with children's ages and rent debt.
PLAUSIBLE. Eviction enforcement by lord's-man for unpaid rent is within the lord's administrative authority (cond-feudal-hierarchy-law: tax collection rights, low justice, "the right to conscript smallfolk labor for the lord's projects"). The neighbors watching from doorways without intervening is consistent with cond-smallfolk-political-physics (learned invisibility; cost of being visible to power; collective compliance as armor). Taylor's network covering the alley-level event is within 300m range. The log entry including children's ages and rent debt is consistent with the s1 clinical-self-erasure register (cond-clinical-self-erasure: "s01 register: full clinical, full notation. Subject behavioral changes, day by day, with named individuals and specific descriptions").

**Beat 13** — Tanner-family second visit; father states customary wage-claim; Taylor makes partial payment; transactional surface formalizes.
PLAUSIBLE. Supported by Q4 analysis above. The father's statement of the claim in accurate legal terms (amount, mechanism, no raised voice) is consistent with cond-smallfolk-political-physics (the posture of non-threat; operating through the mechanisms available). Taylor's partial payment is plausible — it is within her means to make some payment. The formalization without closure is consistent with the described customary-claim mechanics.

**Beat 14** — Range crosses 400m during sustained autumn relay operation; log entry clinical; expanded radius includes additional labor-web traffic and broader eastern-quarter approach.
PLAUSIBLE. Second range expansion. The seasonal trigger (autumn peak insect density) is mechanically plausible — the addendum does not specify a seasonal constraint on expansion, but higher ambient insect density providing more operational substrate for sustained relay is consistent with the fauna-control mechanics. The expansion from ~330m to ~400m across several weeks of autumn operation is consistent with the "organic through use" description. The clinical log entry (new perimeter, date, ambient conditions, headache duration) is consistent with s1 notation register.

**Beat 15** — Broken maester's side-alley door used at unusual pre-light hour; heavy-tread visitor; 40-minute low-register conversation; Taylor cannot identify visitor; records as anomaly.
PLAUSIBLE. Side-alley door visits at unusual hours are a plausible occurrence for a chain-stripped maester who might have contacts he receives discreetly. The acoustic capture limitation ("register too low for clear acoustic capture through the beetle colony") is mechanically consistent with the through-wall acoustic access described in loc-eastern-quarter-apothecary ("partial audio of speech near south/window walls"). Low-register speech at 40 minutes at distance through the beetle colony plausibly fails to provide full acoustic capture. Taylor's inability to identify the visitor is plausible — she knows the footfall but not the person.

**Beat 16** — Taylor determines maester is chain-stripped, keeping systematic record in upper room; records as "subject: chain-stripped maester, upper room apothecary, eastern quarter, consistent high-density notation activity."
PLAUSIBLE. The method of inference (acoustic fragments accumulated across weeks, spoken phrases, rhythm of decades-organized information) is within the established acoustic observation capability. That a chain-stripped maester would keep systematic records is plausible Westerosi behavior — stripped of chain but retaining scholarly habits. The information Taylor can extract (fact of chain-stripping via acoustic fragments, systematic notation recognized by rhythm) is within the described observation capability. She cannot read the record — consistent with physical constraints of through-wall insect observation (no visual-field access; partial audio only).

**Beat 17** — Tanner-family third visit; mother alone; Taylor declines the cold-months question; mother reports she has stopped the vigil candle; leaves without staying for the meal.
PLAUSIBLE. An unannounced family visit is plausible for smallfolk with trade connections to KL. The mother's report about the vigil candle is consistent with cond-crownlands-superstition-frame-125ac ("vigil candle" is consistent with Faith-of-the-Seven practice for the recent dead; a family stopping the vigil is a practical decision about grief management, consistent with the Stranger-leavings frame's logic that "waiting for Tya was not the same as waiting for what came back"). The mother's register — practical statement, not confession — is consistent with the political-physics-of-non-threat posture and the described grief texture.

**Beat 18** — Hightower intelligence clerk maps Flea Bottom labor web on routine population-register pass; speaks to tanner-elder; records "trade-referenced from the Crownlands, reliable, strange, no known affiliations"; Taylor's network covers the exchange.
PLAUSIBLE. Supported by Q1 analysis above. The low-tier operative conducting a population-register pass is within the described function of the Hand's administrative apparatus (cond-westerosi-customary-authority-125ac: "census-adjacent records when conducted, special inquiries"). The elder accurately describing Taylor as "reliable, strange, no known affiliations" is consistent with the elder's own assessment (he placed her as "reliable and strange" in beat 6). The clerk recording what the elder says without evaluating it is plausible procedural behavior. Taylor's network covering the junction exchange is within range.

**Beat 19** — Range crosses 500m through early winter incremental expansion; broken maester's full vertical inside radius; log specific.
PLAUSIBLE. Third range expansion. Incremental rather than threshold-event is consistent with the addendum's description of the second expansion type ("incremental, not threshold-event, a gradual extension through the weeks of early winter as the shard's local-reseed stabilizes further"). 500m from ~400m is a plausible incremental gain. The expanded radius covering the ground-floor apothecary is consistent with geometry (loc-eastern-quarter-apothecary: ~250m from base; 500m radius covers both floors with margin). Log specificity consistent with s1 notation register.

**Beat 20** — Second Hightower clerk asks apothecary owner about unusual recent residents; describes behavioral profile matching Taylor; owner names her; clerk records and leaves; Taylor's network covers the exchange.
PLAUSIBLE. Supported by Q1 analysis. A second clerk operating via the eastern-quarter adjacent streets (not Flea Bottom junction) is consistent with the apparatus conducting a geographic spread of its population mapping. The apothecary owner being asked about unusual residents is plausible — the apothecary is a known business where community members interact. The owner naming Taylor is plausible — Taylor's access to the building (proximity to the side-alley door, her network's presence in the building) may make her a known presence to the owner, and a behavioral profile ("Crownlands-origin woman, unskilled labor entry, trade-referenced, unusual behavioral register") matches well enough to trigger recognition. Taylor's network covering the exchange through insects in the doorframe is within 500m range and consistent with loc-eastern-quarter-apothecary's observation points.

**Beat 21** — Elder receives task requiring Fish Gate Watch-pattern knowledge and invisible information-handoff; Taylor accepts; burns portion of dock-side insect cluster to route through controlled coverage; cluster needs weeks to reseed.
PLAUSIBLE. The task type (Watch-pattern knowledge, invisible hand-off) is plausible within the Flea Bottom labor web's described function. The elder routing a task to Taylor as a functional node is consistent with beat 10's establishment that she is now embedded in the chain. The operational cost — burning through the dock-side cluster to route through controlled coverage — is consistent with cond-fauna-control-rules mechanics. Insect populations require time to reseed after depletion; this is consistent with the biological realism the cards maintain. The network position upgrade from "placed by the elder" to "routed to by the network" is a plausible consequence of having demonstrated a capability the network needed.

**Beat 22** — Broken maester walks to eastern-quarter market stall selling dried beetles and preserved specimens; speaks to stall-keeper about insect coordination anomalies in Flea Bottom-adjacent alleys; buys nothing; returns; pen-scratch continues six hours past usual stopping point.
PLAUSIBLE. A chain-stripped maester maintaining scholarly interests and walking to a specimen stall is plausible behavior. The stall-keeper having noticed insect coordination anomalies is plausible given Taylor's network operations: the insects in the Flea Bottom-adjacent alleys have been behaving with unusual coordination since beat 2, and a specimen dealer who tracks insect behavior for commercial reasons would be a plausible early noticer. The maester's response (extended work session after the conversation) is consistent with a scholarly figure receiving potentially significant observation data. The stall-keeper mentioning the anomaly is plausible — it is an interesting commercial observation, not a dangerous disclosure.

**Beat 23** — Tanner-father appears at junction alone; states wage claim is on customary record with lord's man; elder routes to Taylor; village-claim now external record she cannot access or modify.
PLAUSIBLE. Supported by Q4 and Q5 analyses. The father registering the claim with the lord's man is a plausible step: having established the claim (beat 13), he formalizes it through the administrative apparatus available to him. The lord's man receiving and recording such a claim is within the administrative record-keeping authority. The father traveling to KL specifically to deliver this message (rather than doing so on the quarterly pass) is plausible if the quarterly pass has already occurred and he does not want to wait another quarter. The elder routing the information to Taylor is consistent with his function as a membrane between the labor web and those Taylor's activities concern.

**Beat 24** — Range reaches ~600m in late winter via sustained overnight Fish Gate margin operation; log records expansion, headache duration, new geography; Red Keep still 400m beyond ceiling; math is in the log.
PLAUSIBLE. Fourth range expansion. Sustained overnight operation as trigger is consistent with the prior expansion pattern. 600m from ~500m is a plausible incremental gain. The addendum establishes the ceiling at ~1.5km by late s2; 600m in s1's late winter is consistent with the progression toward that ceiling. The specific detail that the Red Keep's outermost approach is "still four hundred meters beyond her current ceiling" is consistent with the location cards: loc-red-keep-outer-ring states "Not available until late s2 / early s3 range expansion" and "Taylor's range at ceiling covers outer ring at degraded precision." At 600m in s1, she cannot reach it. The 400m gap is consistent with the location's described accessibility threshold.

**Beat 25** — Senior Hightower operative in Red Keep outer ring sends messenger to elder requesting written account of Crownlands girl's behavior and affiliations; elder delivers via middleman three days later; Taylor's network observes messenger and elder's response but cannot observe what is written or where it goes.
PLAUSIBLE. The escalation to a senior operative is consistent with Q1 analysis — the prior two clerk contacts (beats 18 and 20) have fed information up the apparatus chain, producing sufficient interest for a more senior contact. The contact mechanism (messenger to a community figure rather than direct approach to Taylor) is consistent with how the Hand's apparatus would handle a subject who has no formal status — using the known community node (elder) rather than direct contact that would either produce a watch-house record or warn the subject. The elder delivering a written account via middleman is plausible — a community-elder figure who operates as a membrane between the labor web and the larger world would have access to informal couriers. Taylor's network observing the messenger-and-elder interaction but not the content of the written account is consistent with her observation capability: she can detect persons in range and their movements, but cannot read a document the elder writes in a room she is not observing in detail.

One sub-question: Is the Red Keep outer-ring operative sending a messenger to Flea Bottom plausible at this stage (pre-Dance, before the apparatus has a clear profile of Taylor)? Yes — the two prior clerk contacts have produced a consistent pattern (Crownlands-origin, trade-referenced, "reliable and strange," no known affiliations but with a behavioral profile worth tracking). A senior operative in an intelligence apparatus that is actively building a population register of unusual persons in KL would plausibly escalate to a formal written-account request when field reports produce a consistent-but-incomplete picture. The timing (both arcs converging near season end) is a story choice, not an event impossibility — the two apparatuses operating independently and closing around her at similar times is described as coincidence within the story world, and it is plausible as coincidence. Two separate administrative cycles (quarterly passes, routine population-register pass, seasonal follow-up) converging within a week of each other is within normal variance.

**Beat 26** — Taylor walks full Flea Bottom perimeter; writes two log entries side by side; explicitly notes the two apparatuses have no knowledge of each other; log does not speculate; architecture has changed.
PLAUSIBLE. The perimeter walk is within her range and established operational pattern. Writing two log entries that record the two-arc convergence is consistent with s1 clinical notation register. Her analysis that the two apparatuses are on different institutional tracks and not cross-referencing is accurate to the described institutional architecture: the lord's-man who holds the village customary-wage-claim record is a local Crownlands administrative functionary; the Hightower apparatus operates through the Hand's office. These are distinct bureaucratic structures. Her log not speculating beyond what the data shows is consistent with cond-clinical-self-erasure s1 register ("she records what the data shows").

---

## Summary of Findings

### Faults

None structural.

### Flags

| id | type | beat | what | why |
|----|------|------|------|-----|
| fault-001 | flag | 7, 105–122, 209–225, 344–359, 438–453 | Bones use "the spiders spread the ceiling corners" and "the spiders relay the room" in recurring network expansion beats. The loc-eastern-quarter-apothecary card lists ceiling-corner spider presence as an established passive observation point, but "spread" implies active deployment command. This is ambiguous at bone level — it could mean Taylor directs the existing population or actively deploys new spiders into the room from outside. If the latter, the mechanism requires clarifying at line level: Taylor's acoustic access to the upper room is through the south-wall beetle colony, not through spiders she commands from outside the wall at 250m. Spider deployment from Taylor's position into the closed upper room would require insects to navigate building entry points not established in the location card. | At line level, if "spread" is written as active interior deployment through the building, it may overstate the precision of Taylor's acoustic access beyond what the beetle-colony observation point warrants. Fixer must not be dispatched — this is an execution-level flag for screen-writer awareness at the facet-writing stage, not a bones-level structural problem. |

### No Split-Verdict Adjudication Required

S8a does not exist at audit time. URI-016 split-verdict protocol cannot be applied. If S8a is subsequently filed and any beat receives PLAUSIBLE-CHARACTER against this report's PLAUSIBLE verdicts, no split exists. If S8a returns PLAUSIBLE-CHARACTER on any beat this report has found PLAUSIBLE-EVENT, the verdicts are consistent. If S8a is filed and returns a differing verdict on any beat, URI-016 adjudication applies at that time.

---

## File-Level Verdict

**PLAUSIBLE**

All 26 content beats are plausible in-world events given the active condition cards, series laws, lore, and location constraints. The five specifically-tasked plausibility questions (Hightower apparatus intelligence filing; range-expansion mechanics; insect-network coordination at Flea Bottom scale; customary wage-claim mechanism; lord's-man / reeve / quarterly-pass) all return PLAUSIBLE. One execution-level FLAG (fault-001) is raised on spider deployment semantics in the bones — this is not a structural implausibility and does not affect the file-level verdict.

No escalation required.
