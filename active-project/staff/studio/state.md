STATE:
  episode: s01e01
  current_scene: crawler
  current_location: stormlands-coastal-cliffs-cave

  locations:
    reach-minor-lordship-hall:
      description: Great hall of a minor Reach lordship. Long table, remains of a meal, arrow-slit windows letting in late afternoon light. Lord Edwyn Fossoway-minor at the head. Two men-at-arms by the door. Steward with quill and ledger. Dogs under the table. Tallow candles. Jack seated across from the lord in the traveling merchant's role.
      time_of_day: late afternoon
      light: amber through arrow-slits; tallow candles on the table
      atmosphere: warm, formal, watchful
      active_characters: [jack-slash, lord-edwyn, lord-steward, two-men-at-arms]
      props: [wine cup, ledger, quill, candles, tallow, dogs under table]

    stormlands-market-town-square:
      description: A market square in a Stormlands market town. Livestock market in progress. Bread stall, goat pen, water trough, well. Farrier's queue. Two dogs fighting over a scrap. A sell-sword watching the crowd. Dennis at the square's edge.
      time_of_day: midday
      light: overcast, grey-white
      atmosphere: busy, indifferent, becoming watchful
      active_characters: [clockblocker, bread-woman, cart-boy, boy-mother, septon, sell-sword]
      props: [bread stall, cart horse and cart, water trough, well, goat pen]
      scene_status: CLOSED (scene 2 complete, bullet 25)

    narrow-sea-merchant-cog:
      description: A trading cog heading west (withdrawal course), grey morning, moderate swell. Salt and old timber. Deck: ordinary crew activity, no looking-glass raised. Below decks: maester Pylos at a plank table, parchment flat, quill inked, lamp lit, first line of a report to the Citadel (copy to the Hand's office, King's Landing) being written.
      time_of_day: grey morning (scene 3, episode close)
      light: overcast (deck); lamp-lit (below decks)
      atmosphere: routine withdrawal; below decks — documentation, the record opening
      active_characters: [maester-pylos (below decks), ship-captain, three-sailors (deck)]
      props: [brass looking-glass (below decks, not in use), parchment, inked quill, lamp, plank table]
      scene_status: CLOSED (scene 3, bullet 33 — episode end)

    stormlands-coastal-cliffs-cave:
      description: Large cave two-thirds down the Stormlands cliff face. Salt smell layered with something scorched — heat residue, not recent fire. Cave mouth opens onto a broad view of the Narrow Sea: grey, flat, morning light coming in diffuse with no hard shadows. Interior darker than mouth; crawler visible as iridescent-black shape settled back from the opening. From inside, the cog is a small dark shape a quarter-mile east — sail distinguishable, mast line clear, working east at steady pace.
      time_of_day: morning
      light: diffuse, grey-white, flat — no direct sun
      atmosphere: stillness, observation, the-observer-observed (reversal complete — cog crew now oriented on cliff)
      active_characters: [crawler]
      props: []
      scene_status: OPEN (scene 3, bullet 28)

  scene_transitions:
    scene_1_jack: reach-minor-lordship-hall — bullets 1-13
    scene_2_dennis: stormlands-market-town-square — bullets 14-23 (by episode-plan line count offset)
    scene_3_crawler: narrow-sea-merchant-cog + stormlands-coastal-cliffs-cave — final bullets

  world_flags: []
  state_changes_this_episode:
    - scene_1_bullet_1: hall opened; tallow candles lit and burned down by a third; late-afternoon amber through two arrow-slits; two men-at-arms by the door; dogs under the table, one with chin on Jack's boot; Lord Edwyn at hall's head; steward standing left with ledger open and quill active; Jack seated across from lord
    - scene_1_bullet_3: Lord Edwyn nods; taps table twice with two left-hand fingers (tell registered); glances to steward; steward's quill status: active but slowing
    - scene_1_bullet_5: steward's quill lifted off ledger; quill did not return to page; ledger still open; steward posture: alert, still
    - scene_1_bullet_6: Lord Edwyn paused, then smiled; arrangement verbally confirmed; wine ordered; wine cup en route to Jack
    - scene_1_bullet_8: Lord Edwyn angled body toward steward; spoke one word, volume below table-carry threshold; steward received the word
    - scene_1_bullet_9: steward set quill down; closed ledger; exited through side passage; steward no longer in hall; ledger closed and on table
    - scene_1_bullet_11: men-at-arms near door shifted weight; neither stepped aside; held position until Lord Edwyn raised hand; path to door then clear
    - scene_1_bullet_13: hall main doors closed behind Jack; steward absent from table; Lord Edwyn remains at hall's head; hall interior now contains lord, steward's closed ledger, two men-at-arms, dogs; Jack is outside in courtyard
    - scene_2_bullet_14: scene opened; stormlands-market-town-square established; midday overcast; livestock pens east wall; bread stall center square; water trough beside well coping; sell-sword at well post; clockblocker present at square
    - scene_2_bullet_16: cart horse shied at dog through pen-gap; hooves lost purchase on wet stone; cart lurched sideways; boy pinned between cart wheel and well coping; crowd turning
    - scene_2_bullet_18: cart frozen mid-motion — wheel mid-skid, horse foreleg lifted, harness chains suspended without tension; freeze state active
    - scene_2_bullet_19: boy dropped clear of wheel to ground; boy not moving; freeze state still active
    - scene_2_bullet_21: cart still frozen; wheel locked mid-arc, horse foreleg suspended, harness chains hanging; market square ambient noise dropped; crowd witnesses frozen cart
    - scene_2_bullet_22: freeze released (timer expiry, not clockblocker action); horse lurched forward; harness dropped; wheel struck well coping at full weight; cart motion resumed
    - scene_2_bullet_23: sell-sword straightened from well post; watching clockblocker; did not move toward him
    - scene_2_bullet_24: septon crossed to boy's mother; spoke one word at close range — old word, pre-Andal root, outside Seven's liturgy; word spoken, not recorded in square's common tongue
    - scene_2_bullet_25: boy's mother oriented on clockblocker; looked at septon; returned gaze to clockblocker and held it; gaze did not break at scene close
    - scene_3_bullet_26: scene 3 opened; stormlands-coastal-cliffs-cave established; morning, diffuse light; salt-and-scorched smell; cave mouth frames Narrow Sea; trading cog a quarter-mile east, sail and mast visible, working east; crawler settled in cave interior, oriented on cog
    - bullet_16: crawler perceived by ship crew; four figures oriented toward cliff
    - bullet_17: ship adjusting west; withdrawal pattern; maester going below for writing materials
    - bullet_18: ship bearing away; maester report in progress; Crawler returns to cave interior
    - scene_3_bullet_28: maester Pylos at the cog's rail; brass looking-glass raised and trained on cliff face; two sailors reoriented toward cliff, following the line of the glass; observer-observed reversal complete — cog crew no longer incidentally aware, now actively looking at cave mouth as specific point of interest; looking-glass glinting in grey light (brass catching diffuse morning grey — visible from cliff as a small bright point); Crawler is now the object of directed observation
    - scene_3_bullet_30: one sailor raised arm and pointed toward cave mouth — gesture instinctive, immediately withdrawn (hand pulled back); helmsman adjusted bearing two points west, no spoken order; cog now on withdrawal course from cliff; sail angle shifted relative to sky as heading changed — readable from cliff as the sail's presented face rotating; cog is moving away
    - bullet_32: maester Pylos left the deck and went below; looking-glass not raised again after last use; deck now empty of the glass; cog continues west at routine sailing pace; deck returns to ordinary crew activity without the glass; no further observation of cliff
    - bullet_33: below decks, maester Pylos has parchment flat on a plank table, quill inked; first line of a report being written; report addressed to the Citadel; copy notation to Hand's office in King's Landing; the record is open and in progress; lamp or equivalent light source in use (below-decks, no natural light)

  episode_end_state:
    jack-slash: cover intact on exit; thread pulled; lordship investigation initiated against Jack
    clockblocker: exposed publicly; old word spoken; rumor in motion; at doorway three streets from square
    crawler: sighted; report in transit to King's Landing; unaware of significance; in cave
