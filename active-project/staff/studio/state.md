STATE:
  episode: s01e01
  current_scene: jack
  current_location: reach-minor-lordship-hall

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

    narrow-sea-merchant-cog:
      description: A trading cog three days from Driftmark, heading north. Grey morning, moderate swell. Captain, young maester Pylos, three sailors. Deck of salt and old timber smell.
      time_of_day: grey morning (scene 3)
      light: overcast
      atmosphere: routine voyage, transitioning to alarm
      active_characters: [maester-pylos, ship-captain, three-sailors]
      props: [brass looking-glass, journal, ink and vellum, rope]

    stormlands-coastal-cliffs-cave:
      description: The large cave two-thirds down the cliff face. Smells of salt and something scorched. Cave mouth framing a view of the Narrow Sea. Late afternoon light going orange-grey. Crawler visible as iridescent-black shape against the darker interior.
      time_of_day: late afternoon / dusk
      light: orange-grey, fading
      atmosphere: stillness, observation
      active_characters: [crawler]
      props: []

  scene_transitions:
    scene_1_jack: reach-minor-lordship-hall — bullets 1-13
    scene_2_dennis: stormlands-market-town-square — bullets 14-23 (by episode-plan line count offset)
    scene_3_crawler: narrow-sea-merchant-cog + stormlands-coastal-cliffs-cave — final bullets

  world_flags: []
  state_changes_this_episode:
    - scene_1_jack: opened; hall setup recorded
    - bullet_3: lord-left-hand-tell, steward-quill-pause recorded
    - bullet_5: arrangement closed; lord orders "find out who told him"; steward writing; Jack exits
    - scene_2_dennis: opened; market square established
    - bullet_8: cart horse spooks, boy pinned against well coping; crowd turns
    - bullet_9-10: clockblocker glove off, cart frozen; boy freed; glove back on
    - bullet_11: sell-sword, market women, septon, mother all observing; cart at impossible angle
    - bullet_13: cart releases; septon names event to mother with old word; story starts
    - scene_3_crawler: opened; cave mouth, merchant cog at distance
    - bullet_16: crawler perceived by ship crew; four figures oriented toward cliff
    - bullet_17: ship adjusting west; withdrawal pattern; maester going below for writing materials
    - bullet_18: ship bearing away; maester report in progress; Crawler returns to cave interior

  episode_end_state:
    jack-slash: cover intact on exit; thread pulled; lordship investigation initiated against Jack
    clockblocker: exposed publicly; old word spoken; rumor in motion; at doorway three streets from square
    crawler: sighted; report in transit to King's Landing; unaware of significance; in cave
