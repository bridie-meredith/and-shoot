# b01c10 — Phase 1 bone draft (screen-writer)

Chapter: b01c10 — THE CLIMAX (Otto formalizes the arrangement + the courier's detention)
POV narrator: taylor-hebert-kl-122ac
dramatic_shape: climax
goal: Show the audience the formalization and the detention in the same chapter so the structure is clear — Otto naming the arrangement and Taylor's feed confirming its operational consequence are the same event.

Cast slugs resolved (from cast/actor_baselines + prior bones):
- protagonist / narrator: taylor-hebert-kl-122ac
- antagonist (relayed-speaker, never on-stage): otto-hightower
- courier-conduit (channel-resident, off-channel here): jarvis-coin-kl-courier
- detained figure (established c08/c09): corwick

Register-resident props/objects (established c08/c09 bones — reused, no new coinage):
- the courier-coin   (the relay medium named in the s01 [mechanism:] tag — Otto's words arrive in Taylor's hand via the coin)
- the jarvis-packet / the jarvis-seal   (the relayed written message-object + its seal; c08 lines 11-12)
- the-feed-station   (Taylor's coverage-review station; c08/c09)
- the insect-feed    (the coverage stream; c08/c09)
- the feed-record / the observation-entry / the ledger   (the accounting record; c09 lines 19/26/36)
- the stylus, the seal   (accounting/sealing implements; c08 line 16, c09 line 37)

GROUNDING-QUOTA NOTE (PASS-CHUNK-VOICE-RISK, Signal B carried): every scene below carries ≥1 explicit
grounding bone (flagged [GROUND]). The two central events (s02 breach, s03 detention) are authored as
CONCRETE actor-verb-object events, not process-abstraction, per EVENT-NOT-CONCRETE risk.

DIALOGUE-ANCHOR NOTE (URI-WRITE-DIALOGUE-COBONDED): s01 + s02 carry the channel-relayed exchange.
Otto and Taylor NEVER meet — the speech-act is the relayed text arriving/departing via the courier-coin.
Dialogue-anchor bones use canonical speech form `<speaker> speaks to <listener>`; the coin is the medium,
rendered as the relayed words, not face-to-face. Flagged [DIALOGUE-ANCHOR] for Phase 1.5 + Phase 7 co-emit.

==============================================================================================
SCENE s01 — THE NAMING (Jarvis-mediated formalization)
scene_conflict.stakes_axis: position-prot-rise
substance_delta.axes_in_motion target:
  position-prot-rise   +1.0  (cl-d07a)
  social_tether-prot-rise +1.0 (cl03b)
  social_tether-antag  +1.5  (cl-antag-d10)
axes_held: relational_anchor_status, political_register-prot, social_tether-prot-collapse,
           moral_framework, moral_legibility_to_self
==============================================================================================

b01c10s01n01  taylor-hebert-kl-122ac takes the-feed-station
  shape: chatter
  axis_moves: []   axes_held: []
  cost_ledger_anchor: cl-d07a   (setup transition into the relay scene; anchored per chatter rule)
  [GROUND] — place-situated open: Taylor at the physical coverage station.

b01c10s01n02  the courier-coin reaches taylor-hebert-kl-122ac's hand
  shape: chatter
  axis_moves: []   axes_held: []
  cost_ledger_anchor: cl-d07a   (the relay medium arrives; pure setup of the channel object)
  [GROUND] — the coin in Taylor's hand; the relay made physical.

b01c10s01n03  taylor-hebert-kl-122ac breaks the jarvis-seal
  shape: chatter
  axis_moves: []   axes_held: []
  cost_ledger_anchor: cl-d07a   (opening the relayed message-object; physical transition to the utterance)
  [GROUND] — the seal broken; the message-as-object handled.

b01c10s01n04  otto-hightower speaks to taylor-hebert-kl-122ac   [DIALOGUE-ANCHOR — relayed via courier-coin]
  shape: moving
  axis_moves: [{axis: position-prot-rise, direction: up, magnitude: 1}]
  cost_ledger_anchor: cl-d07a
  note: Otto names the arrangement an ongoing FUNCTION — the load-bearing utterance. The naming
        forecloses informal-deniability; position made legible/standing. Communication-class axis carried
        by position-prot-rise via the relayed administrative naming. [event: Otto names the arrangement an ongoing function]

b01c10s01n05  otto-hightower speaks to taylor-hebert-kl-122ac   [DIALOGUE-ANCHOR — relayed via courier-coin]
  shape: moving
  axis_moves: [{axis: social_tether-antag, direction: up, magnitude: 2}]
  cost_ledger_anchor: cl-antag-d10
  note: Otto sets Sera's protection as the STANDING consideration — leverage converted from contingent to
        structural. The relayed second clause naming the consideration. (magnitude 2 toward the +1.5 target;
        sum-roll lands within tolerance — see roll check.)

b01c10s01n06  taylor-hebert-kl-122ac turns the courier-coin
  shape: held
  axis_moves: []
  axes_held: [{axis: moral_framework, rationale: "the breach is enacted in s02; here Taylor receives the frame without breaching — SVO enacts the discipline of registering-and-not-yet-acting"},
              {axis: moral_legibility_to_self, rationale: "suppressed-recognition crack opens in s03 at the detention, not here; the physical handling holds the legibility static"}]
  cost_ledger_anchor: cl-d07a
  [GROUND] — Taylor working the coin in her fingers; the deniability-foreclosure registered as an object-act, not a realization.

b01c10s01n07  taylor-hebert-kl-122ac speaks to otto-hightower   [DIALOGUE-ANCHOR — relayed back via courier-coin]
  shape: moving
  axis_moves: [{axis: social_tether-prot-rise, direction: up, magnitude: 1}]
  cost_ledger_anchor: cl03b
  note: Taylor's relayed confirmation — not refusal. The tether goes load-bearing: confirming the standing
        function binds her into the apparatus. Communication-class axis carried by social_tether-prot-rise.
        [image: the tether going load-bearing]. Render as operational confirmation, NOT moral concession.

b01c10s01n08  taylor-hebert-kl-122ac seals the jarvis-packet
  shape: held
  axis_moves: []
  axes_held: [{axis: relational_anchor_status, rationale: "Wren not in the channel; the formal arrangement runs outside the Wren relationship; anchor holds at 3.5 — SVO is Taylor finishing the formal exchange with no Wren-account touched"},
              {axis: political_register-prot, rationale: "the naming received as operational fact; resentment-processing deferred to c11; the sealing enacts filing-without-grieving"}]
  cost_ledger_anchor: cl03b
  [GROUND] — the packet sealed; the channel going quiet with the function named.

b01c10s01n09  the courier-coin settles in taylor-hebert-kl-122ac's palm
  shape: held
  axis_moves: []
  axes_held: [{axis: social_tether-prot-collapse, rationale: "non-extractable confirmation is in progress across the chapter but not advanced in this scene; the coin-at-rest holds the collapse axis static"}]
  cost_ledger_anchor: cl-d07a
  [GROUND] — close on the coin in hand, the deniability gone. [image: arrangement as a named standing position]

--- s01 SUM-ROLL CHECK ---
  position-prot-rise:      +1 (n04)                target +1.0  → EXACT
  social_tether-antag:     +2 (n05)                target +1.5  → +0.5 over, WITHIN ±1 ✓
  social_tether-prot-rise: +1 (n07)                target +1.0  → EXACT
  Held axes covered by ≥1 bone: moral_framework (n06), moral_legibility_to_self (n06),
    relational_anchor_status (n08), political_register-prot (n08), social_tether-prot-collapse (n09) ✓
  Bone count: 9 (within 5-15) ✓

--- s01 EVENT-MAP ---
  [mechanism: Jarvis coin-courier channel — Otto's words relayed via courier-coin to Taylor's hand, responses back]
      → n02 (coin reaches hand), n03 (break seal), n04/n05 (Otto relayed), n07 (Taylor relayed), n08 (seal back). COVERED.
  [force: Otto — the relayed words, the apparatus naming the instrument by its use]
      → n04, n05. COVERED.
  [force: Taylor — reading the relayed text for the pattern under it, finding the pattern is now her]
      → n06 (turns the coin — the registration enacted as object-handling). COVERED.
  [event: Otto names the arrangement an ongoing function]   (CONCRETE — load-bearing utterance)
      → n04. COVERED (dialogue-anchor; "function" register carried in Phase 1.5).
  [image: the arrangement as a named standing position rather than a contingent favor]
      → n09 (coin settling — close image). COVERED (image; rendered in facets/stitch).
  [mechanism: Sera's protection is the standing consideration — the weight that makes refusal not a real option]
      → n05 (Otto sets the standing consideration). COVERED.
  [image: the tether going load-bearing]
      → n07 (Taylor's confirmation binds the tether). COVERED (image).

==============================================================================================
SCENE s02 — THE DESCRIPTION (Otto requests the courier; Taylor provides it) — THE BREACH
scene_conflict.stakes_axis: moral_framework
substance_delta.axes_in_motion target:
  moral_framework        -1.0  (cl03a)
  position-world         +0.5  (cl-world-d04)
  political_register-world +0.5 (cl-world-d07)
axes_held: relational_anchor_status, political_register-prot, social_tether-prot-collapse,
           moral_legibility_to_self, position-prot-rise, social_tether-prot-rise, social_tether-antag
==============================================================================================

b01c10s02n01  the courier-coin reaches taylor-hebert-kl-122ac's hand
  shape: chatter
  axis_moves: []   axes_held: []
  cost_ledger_anchor: cl03a   (second relayed message arrives hard on the first; setup of the request)
  [GROUND] — the coin again in hand; same channel, same one-remove.

b01c10s02n02  otto-hightower speaks to taylor-hebert-kl-122ac   [DIALOGUE-ANCHOR — relayed via courier-coin]
  shape: moving
  axis_moves: [{axis: position-world, direction: up, magnitude: 1}]
  cost_ledger_anchor: cl-world-d04
  note: Otto requests the courier BY DESCRIPTION — a face, a route, a pattern up the hill. The apparatus
        already half-knows; the request is the Green channel reaching into the lower-city layer.
        Communication-class carried by position-world (consolidation request). [event: Otto requests the courier by description]
        (magnitude 1 toward +0.5 target — see roll; the world-axis half-increments split s02/s04.)

b01c10s02n03  taylor-hebert-kl-122ac faces the jarvis-packet
  shape: held
  axis_moves: []
  axes_held: [{axis: moral_legibility_to_self, rationale: "recognition SUPPRESSED at the breach itself; the crack opens in s03; here Taylor recognizes the figure operationally without self-accounting — SVO is the still recognition, no conclusion drawn"}]
  cost_ledger_anchor: cl03a
  note: Taylor recognizes the figure instantly — the Corwick courier-face withheld in c09 beat 2 — but
        registers it as the operational match, not a moral event. [image: the withheld observation asked for by description]
  [GROUND] — Taylor over the physical packet, the described figure resolving against her body-map.

b01c10s02n04  taylor-hebert-kl-122ac marks corwick
  shape: held
  axis_moves: []
  axes_held: [{axis: relational_anchor_status, rationale: "Wren not present; the breach runs outside the Wren relationship; anchor holds at 3.5 — the marked figure is Corwick, not Wren"},
              {axis: position-prot-rise, rationale: "peaked structurally at s01; this scene operates inside that frame without moving it; the marking-act enacts the position being used, not raised"}]
  cost_ledger_anchor: cl03a
  [GROUND] — the body-map figure (Corwick) physically marked/located against the coverage; the withheld observation surfacing as a concrete locatable person.

b01c10s02n05  taylor-hebert-kl-122ac speaks to otto-hightower   [DIALOGUE-ANCHOR — relayed back via courier-coin]
  shape: moving
  axis_moves: [{axis: moral_framework, direction: down, magnitude: 1}]
  cost_ledger_anchor: cl03a
  note: THE BREACH ENACTED — Taylor provides the courier identity, route, and pattern, relayed back as a
        clean report. systematic-override-rationalized threshold crosses HERE. Info requested, info given —
        ENACTED, not narrated as realization. moral_framework 0 → -1. Communication-class breach carried by
        moral_framework via the relayed delivery. [event: Taylor provides the courier identity and pattern]
        [VOICE-RISK: render as competence-AS-catastrophe — the smoothness IS the cost.]

b01c10s02n06  taylor-hebert-kl-122ac seals the jarvis-packet
  shape: held
  axis_moves: []
  axes_held: [{axis: political_register-prot, rationale: "no resentment processing; deferred to c11; the provision filed as a report not grieved — SVO is the sealing, the report finished without affect"},
              {axis: social_tether-prot-rise, rationale: "tether went load-bearing at s01; holds through the breach — the sealing enacts the standing function operating, not deepening"},
              {axis: social_tether-antag, rationale: "Otto's leverage made structural at s01; the breach is the leverage being USED, not increased; the sealed delivery is the leverage producing its output"}]
  cost_ledger_anchor: cl03a
  [GROUND] — the packet sealed, the pattern given, the channel quiet. Close on the report delivered.

b01c10s02n07  taylor-hebert-kl-122ac closes the observation-entry
  shape: moving
  axis_moves: [{axis: political_register-world, direction: up, magnitude: 1}]
  cost_ledger_anchor: cl-world-d07
  note: The war's apparatus now operates on Taylor's intelligence; the Green succession register advances as
        the apparatus completes its lower-city logistics picture. [image: the Green channel hardening]
        (magnitude 1 toward +0.5 target — world-axis split s02/s04; see roll.)

b01c10s02n08  the courier-coin settles in taylor-hebert-kl-122ac's palm
  shape: held
  axis_moves: []
  axes_held: [{axis: social_tether-prot-collapse, rationale: "non-extractable confirmation in progress; not advanced in this scene; the coin at rest holds the collapse axis static"}]
  cost_ledger_anchor: cl-world-d07
  [GROUND] — close: the coin at rest, the breach a finished transaction.

--- s02 SUM-ROLL CHECK ---
  moral_framework:          -1 (n05)               target -1.0  → EXACT
  position-world:           +1 (n02)               target +0.5  → +0.5 over, WITHIN ±1 ✓
  political_register-world: +1 (n07)               target +0.5  → +0.5 over, WITHIN ±1 ✓
  Held axes covered by ≥1 bone: moral_legibility_to_self (n03), relational_anchor_status (n04),
    position-prot-rise (n04), political_register-prot (n06), social_tether-prot-rise (n06),
    social_tether-antag (n06), social_tether-prot-collapse (n08) ✓
  Bone count: 8 (within 5-15) ✓
  NOTE on world-axis sizing: bone min magnitude is 1 (bone:{delta_per_axis: 1-3}); the scene's +0.5 targets
    are met by a single +1 bone each, within ±1 tolerance. The s02 +1 / s04 +1 pair sums to the chapter's
    declared +1.0 position-world and +1.0 political_register-world (first-half/tail split per contract).

--- s02 EVENT-MAP ---
  [event: Otto requests the courier by description]   (CONCRETE)
      → n02. COVERED (dialogue-anchor).
  [mechanism: Otto's apparatus already knows the courier exists independent of Taylor's feed — asks BY DESCRIPTION]
      → n02 (the by-description request itself encodes the apparatus's prior partial knowledge). COVERED.
  [image: the withheld observation asked for by description — the thing Taylor chose not to put in the feed, now requested]
      → n03 (Taylor faces the packet, recognizing the withheld figure). COVERED (image).
  [event: Taylor provides the courier identity and pattern]   (CONCRETE — THE BREACH; EVENT-NOT-CONCRETE guarded)
      → n05 (relayed delivery) + n04 (marking corwick as the locatable person being handed over). COVERED.
  [force: Taylor — the instrument doing exactly what it is good at]
      → n05, n06 (clean delivery + sealing). COVERED.
  [force: Otto — the apparatus that already half-knew, completing its picture from Taylor's feed]
      → n02, n07 (request + the entry closing into the apparatus's picture). COVERED.
  [mechanism: the rationalization is operational, not stated — provision framed as completing a report]
      → n07 (closing the observation-entry — the act that frames it as a completed report). COVERED.
  [image: the Green channel hardening — the Hightower apparatus's grip on the lower-city layer settling]
      → n07. COVERED (image).

==============================================================================================
SCENE s03 — THE DETENTION (two days later; learned through the feed) — d10 / Dance-pressure pulse 1
scene_conflict.stakes_axis: moral_legibility_to_self
substance_delta.axes_in_motion target:
  moral_legibility_to_self +0.5  (null anchor — legibility-crack, not a ledger-gain)
axes_held: moral_framework, position-prot-rise, social_tether-antag, relational_anchor_status,
           political_register-prot, social_tether-prot-collapse, position-world, political_register-world
==============================================================================================

b01c10s03n01  taylor-hebert-kl-122ac takes the-feed-station
  shape: held
  axis_moves: []
  axes_held: [{axis: moral_framework, rationale: "breach crossed at s02 (-1.0); the detention is the breach's consequence, not a further breach; holds at -1 — ordinary coverage-review enacts the framework static"}]
  cost_ledger_anchor: null   (HELD bone — no chatter-anchor requirement)
  [GROUND] — open on ordinary coverage-review; the station, the routine, two days after the report.

b01c10s03n02  the insect-feed threads the courier-route
  shape: held
  axis_moves: []
  axes_held: [{axis: position-prot-rise, rationale: "peaked at s01; the feed running its routine confirms the position's functional reality but does not raise it"}]
  cost_ledger_anchor: null
  [GROUND] — the feed running as it always runs; the coverage stream over the route.

b01c10s03n03  the wrong bodies ring corwick
  shape: held
  axis_moves: []
  axes_held: [{axis: relational_anchor_status, rationale: "Wren not present; anchor holds at 3.5; the figure in the feed is Corwick, the Black-faction logistics figure, outside the formal ledger and this consequence"}]
  cost_ledger_anchor: null
  [GROUND] — CONCRETE perceived-event grounding: the wrong bodies in the wrong configuration around the figure; the detention's shape arriving in the feed before it is named. [mechanism: read off the count, not told]

b01c10s03n04  the route closes around corwick
  shape: held
  axis_moves: []
  axes_held: [{axis: social_tether-antag, rationale: "Otto's leverage made structural at s01; the detention is the leverage producing a result, not increasing"},
              {axis: position-world, rationale: "solidified at s02; the detention is its operational confirmation; tail increment at s04, not here"},
              {axis: political_register-world, rationale: "advanced at s02; the detention is the register's operational confirmation; tail increment at s04, not here"}]
  cost_ledger_anchor: null
  [GROUND] — CONCRETE central event: the route closing, the figure intercepted and held — the detention enacted as a perceived feed-event (the wrong bodies, the closing route), not a data abstraction. [event: the courier (Corwick) is detained]

b01c10s03n05  taylor-hebert-kl-122ac marks the detention
  shape: moving
  axis_moves: [{axis: moral_legibility_to_self, direction: up, magnitude: 1}]
  cost_ledger_anchor: null
  note: Taylor registers the connection (her report → two days → this detention); the registration is
        SUPPRESSED — she marks the timing the way she marks any pattern, then does not follow it to its
        conclusion about herself. +0.5 = the crack DEEPENING, not the recognition opening. moral_legibility
        5 → 5.5. (magnitude 1 toward +0.5 — see roll; bone-min is 1.) [image: the war's first operational
        consequence of Taylor's intelligence arriving as a pattern in her own coverage]
        [HARD: NOT a recognition/realization scene — the conclusion about herself is NOT drawn.]

b01c10s03n06  taylor-hebert-kl-122ac closes the observation-entry
  shape: held
  axis_moves: []
  axes_held: [{axis: political_register-prot, rationale: "the detention produces resentment material but processing is deferred to c11; this scene holds it — the closing-act files it without grieving"},
              {axis: social_tether-prot-collapse, rationale: "non-extractable confirmation in progress; the detention contributes but the collapse is not completed here; the routine close holds it static"}]
  cost_ledger_anchor: null
  [GROUND] — close on the detention confirmed in the feed, the connection registered-and-held-down; the pattern seen, the conclusion not drawn, the legibility crack one fracture wider.

--- s03 SUM-ROLL CHECK ---
  moral_legibility_to_self: +1 (n05)               target +0.5  → +0.5 over, WITHIN ±1 ✓ (bone-min 1)
  Held axes covered by ≥1 bone: moral_framework (n01), position-prot-rise (n02),
    relational_anchor_status (n03), social_tether-antag (n04), position-world (n04),
    political_register-world (n04), political_register-prot (n06), social_tether-prot-collapse (n06) ✓
  Bone count: 6 (within 5-15) ✓
  Grounding: n03, n04 carry the two CONCRETE central-event perceived beats (wrong bodies / route closing) ✓

--- s03 EVENT-MAP ---
  [mechanism: how Taylor learns of the detention through the insect-feed — read off the count, not told;
              wrong bodies in wrong configuration; feed delivers the shape before she names it]
      → n02 (feed threads route), n03 (wrong bodies ring corwick). COVERED.
  [event: the courier (Corwick) is detained]   (CONCRETE)
      → n04 (route closes around corwick). COVERED.
  [image: the detention read off the count — war's first operational consequence arriving as a pattern in her own coverage]
      → n03, n04. COVERED (image).
  [force: Taylor — the instrument receiving the result of its own accuracy, no action to take, no consent to give]
      → n05 (marks the detention — receiving, not acting). COVERED.
  [force: the war's logic — the Dance moving through Taylor's network without her; the abstract conflict made operational and local]
      → n04 (route closing = the war's logic enacted through the feed) + n05 (the connection registered). COVERED.
  [image: the war's logic having moved through Taylor's network without her consent — the thing she built now a vector the war runs through]
      → n05, n06. COVERED (image).
  [mechanism: the suppression is operational — notes the timing, does not follow it to a conclusion about herself]
      → n05 (the suppressed marking) + n06 (the routine close enacting the not-drawn conclusion). COVERED.

==============================================================================================
SCENE s04 — THE LEDGER CLOSE (the first closed entry with a name) — thesis-image as physical act
scene_conflict.stakes_axis: position-world
substance_delta.axes_in_motion target:
  position-world         +0.5  (cl-world-d04)
  political_register-world +0.5 (cl-world-d07)
axes_held: moral_framework, moral_legibility_to_self, position-prot-rise, social_tether-prot-rise,
           social_tether-antag, relational_anchor_status, political_register-prot,
           social_tether-prot-collapse
==============================================================================================

b01c10s04n01  taylor-hebert-kl-122ac takes the-feed-station
  shape: chatter
  axis_moves: []   axes_held: []
  cost_ledger_anchor: cl-world-d04   (setup transition into the accounting close)
  [GROUND] — open on Taylor at the accounting: the ledger, the count, the operational record she keeps.

b01c10s04n02  taylor-hebert-kl-122ac lifts the stylus
  shape: held
  axis_moves: []
  axes_held: [{axis: moral_legibility_to_self, rationale: "crack deepened at s03 (+0.5, suppressed); the ledger close enacts the thesis physically without opening the recognition further; holds at 5.5 — the deliberate accounting-act holds the legibility static"},
              {axis: moral_framework, rationale: "breach crossed at s02 (-1.0); the ledger close is the quiet aftermath, not a further breach; holds at -1"}]
  cost_ledger_anchor: cl-world-d04
  [GROUND] — the stylus lifted to the record; the competent accounting hand. [force: Taylor — running the accounting, doing the thing she is good at]

b01c10s04n03  taylor-hebert-kl-122ac closes corwick's ledger-entry
  shape: moving
  axis_moves: [{axis: position-world, direction: up, magnitude: 1}]
  cost_ledger_anchor: cl-world-d04
  note: THE THESIS-IMAGE AS PHYSICAL ACT — the figure body-mapped for months becomes the first entry in
        Taylor's accounting that is both closed AND named. The Black-faction logistics thread foreclosed =
        one node off the board; the Green channel's grip settling. accuracy-as-catastrophe ENACTED, not
        stated: her competence at keeping the count is what made the detention possible, shown by her
        competently closing the entry. [event: Taylor closes the courier's ledger entry]
        [image: the ledger's first closed entry with a name; the face becoming the ledger's cost]
        (magnitude 1 toward +0.5 — world-axis tail half; pairs with s02 n02 for chapter +1.0.)
  [GROUND] — CONCRETE central act: the named entry physically resolved/closed in the record.

b01c10s04n04  taylor-hebert-kl-122ac names corwick in the ledger
  shape: held
  axis_moves: []
  axes_held: [{axis: relational_anchor_status, rationale: "Wren outside the formal ledger; anchor holds at 3.5; the closed named entry is a Black-faction figure (Corwick), not Wren — the named-line discipline that pointedly is NOT Wren"},
              {axis: position-prot-rise, rationale: "peaked at s01 (4.5); the close confirms the functional peak, does not raise it"},
              {axis: social_tether-prot-rise, rationale: "load-bearing as of s01; holds through the close"}]
  cost_ledger_anchor: cl-world-d04
  [GROUND] — the name written to the line — the first time the accounting's price has a specific human shape (a gait, a route, a face she could have described and did). [image: the face becoming the ledger's cost]

b01c10s04n05  taylor-hebert-kl-122ac closes the observation-entry
  shape: moving
  axis_moves: [{axis: political_register-world, direction: up, magnitude: 1}]
  cost_ledger_anchor: cl-world-d07
  note: World-tail — the detention's operational confirmation closing into the war's register; the
        Black-faction logistics thread foreclosed, Dragonstone-adjacent consequences pending at remove.
        [image: the Black-faction logistics thread foreclosed — one node the war's apparatus has taken off the board]
        (magnitude 1 toward +0.5 — pairs with s02 n07 for chapter political_register-world +1.0.)

b01c10s04n06  taylor-hebert-kl-122ac sets the stylus down
  shape: held
  axis_moves: []
  axes_held: [{axis: political_register-prot, rationale: "resentment processing deferred to c11; the close holds it — the stylus set down ends the act without affect surfacing"},
              {axis: social_tether-antag, rationale: "structural as of s01; holds through the close"},
              {axis: social_tether-prot-collapse, rationale: "non-extractable confirmation in progress; not completed here; the act-end holds the collapse static"}]
  cost_ledger_anchor: cl-world-d07
  [GROUND] — close the chapter quiet: the stylus down, the entry closed, the count accurate and complete, the cost of that accuracy sitting in the record with a face. [mechanism: the thesis enacted, not stated]

--- s04 SUM-ROLL CHECK ---
  position-world:           +1 (n03)               target +0.5  → +0.5 over, WITHIN ±1 ✓
  political_register-world: +1 (n05)               target +0.5  → +0.5 over, WITHIN ±1 ✓
  Held axes covered by ≥1 bone: moral_framework (n02), moral_legibility_to_self (n02),
    relational_anchor_status (n04), position-prot-rise (n04), social_tether-prot-rise (n04),
    political_register-prot (n06), social_tether-antag (n06), social_tether-prot-collapse (n06) ✓
  Bone count: 6 (within 5-15) ✓

--- s04 EVENT-MAP ---
  [force: Taylor — running the accounting, doing the thing she is good at: an observation resolved, a pattern completed, an entry finished]
      → n02 (lifts stylus), n03 (closes the entry). COVERED.
  [force: the closed entry — the figure who was a recurring body-map now a finished line; the war's logic putting a name and face to what the accounting cost]
      → n03, n04. COVERED.
  [event: Taylor closes the courier's ledger entry]   (CONCRETE)
      → n03. COVERED.
  [image: the ledger's first closed entry with a name — the body-map figure becoming a finished line, closed because of what she did, with a face to it]
      → n03, n04. COVERED (image).
  [mechanism: the thesis enacted, not stated — accuracy IS the catastrophe; competence at keeping the count made the detention possible]
      → n03 (competent close) + n06 (the quiet end-act). COVERED.
  [image: the face becoming the ledger's cost — the first time the accounting's price has a specific human shape; a gait, a route, a face she could have described and did]
      → n04. COVERED (image).
  [image: the Black-faction logistics thread foreclosed — Dragonstone-adjacent consequences pending at remove, one node off the board]
      → n05. COVERED (image).

==============================================================================================
CHAPTER ROLL-UP (vs chapter substance_delta; chapter_class climax)
==============================================================================================
  position-prot-rise:        s01 +1.0                                  → chapter +1.0  (target +1.0 EXACT)
  social_tether-prot-rise:   s01 +1.0                                  → chapter +1.0  (target +1.0 EXACT)
  social_tether-antag:       s01 +2.0 (bone) ~ +1.5 contract           → chapter ~+1.5 (target +1.5; WITHIN ±1)
  moral_framework:           s02 -1.0                                  → chapter -1.0  (target -1.0 EXACT)
  moral_legibility_to_self:  s03 +1.0 (bone) ~ +0.5 contract           → chapter ~+0.5 (target +0.5; WITHIN ±1)
  position-world:            s02 +1 + s04 +1 = +2 (bone) ~ +1.0 contract → chapter ~+1.0 (target +1.0; split halves)
  political_register-world:  s02 +1 + s04 +1 = +2 (bone) ~ +1.0 contract → chapter ~+1.0 (target +1.0; split halves)

  All scene axes_held have ≥1 holding bone. All chatter bones carry a cost_ledger_anchor.
  Bone counts per scene: s01=9, s02=8, s03=6, s04=6 — all within 5-15.

  WORLD-AXIS SIZING FLAG (for orchestrator / Phase 6): bone-floor magnitude is 1 (bone:{delta_per_axis:1-3}),
  so the four +0.5 world-axis scene targets are each met by a single +1 bone. Per-scene this reads +0.5 over
  (WITHIN ±1). The s02/s04 PAIR sums to the chapter's declared +1.0 on each world axis exactly. If Phase 6
  prefers tighter per-scene fidelity, the alternative is to NOT move the world axes at s02 (hold them) and
  carry the full chapter +1.0 split as +1/+1 across s04 only — but that contradicts the contract's explicit
  "first at s02 / tail at s04" split. Recommend keeping the split as authored; flagging for disposition.

==============================================================================================
DIALOGUE-ANCHOR BONE MANIFEST (for Phase 1.5 dialogue authoring + Phase 7 co-emit)
==============================================================================================
  All relay-mediated; speakers never co-present; medium = courier-coin (rendered as relayed words, not face-to-face).
  s01n04  otto-hightower → taylor-hebert-kl-122ac   (Otto names the arrangement an ongoing FUNCTION; load-bearing "function" register)
  s01n05  otto-hightower → taylor-hebert-kl-122ac   (Otto sets Sera's protection as the standing consideration)
  s01n07  taylor-hebert-kl-122ac → otto-hightower   (Taylor's relayed confirmation — not refusal; operational, not concession)
  s02n02  otto-hightower → taylor-hebert-kl-122ac   (Otto requests the courier BY DESCRIPTION — face, route, pattern)
  s02n05  taylor-hebert-kl-122ac → otto-hightower   (THE BREACH — Taylor provides identity, route, pattern; competence-AS-catastrophe)

  Behavior-card resolution + objective/Earth-Bet-fence enforcement is Phase 1.5's job. Flagged here only.

==============================================================================================
CONSTRAINT PRE-CHECK (screen-writer, before handoff)
==============================================================================================
  - Earth-Bet fence: no banned proper nouns; register-resident (insect-feed, coverage, count, jarvis-channel,
    courier-coin, ledger, observation-entry). PASS.
  - moral_framework breach ENACTED at s02 (Taylor provides the info via relay), NOT narrated as realization
    (s02n05 is the relayed delivery act; the recognition is explicitly suppressed). PASS.
  - moral_legibility SUPPRESSED at s03 (s03n05 marks-and-suppresses; HARD note attached: conclusion-about-self
    NOT drawn). PASS.
  - s04 no thesis-naming (thesis enacted as the physical ledger-close; HARD note: Taylor does NOT name the thesis). PASS.
  - SVO cleanliness: each bone is one subject / one concrete physical verb / object; no copula/negation/
    conjunction/interiority/perception-verb in the draft SVO. (Full SVO craft is Phase 2.) Note: "marks" at
    s02n04/s03n05/s04 — flagged for Phase 2 perception-verb check (FAULT-FORM-PERCEPTION risk: "marks" reads
    as a physical inscribe/mark act here, not a perceive-and-note; Phase 2 to confirm or recast to "writes"/
    "strikes" / route to a state facet). Likewise s02n03 "faces the jarvis-packet" is the licensed transitive
    face-form. CLEAN-PENDING-PHASE-2.
  - Grounding quota: ≥1 [GROUND] bone per scene (s01: 6, s02: 5, s03: 6, s04: 6). Central events s02 (breach)
    + s03 (detention) authored as concrete actor-verb-object. PASS (quota exceeded per voice-risk carry).
