---
name: oc-magistrate-hall
class: location
scope: library
world: planetos
origin: authored
quality: full
references:
  - cond-kl-geography-122ac
  - cond-kl-social-physics-122ac
  - cond-kl-court-state-122ac
  - loc-flea-bottom
---

# The Magistrate's Hall — Rented Back Room, Chandler's House, Hook-Ward-Network Fringe

## Geography

Not a court chamber. A rented back room in a chandler's house at the fringe where the Hook's lane network meets the broader ward connections — a transitional address, belonging to neither district fully. In 122 AC, the room is rented by the hour for court-adjacent proceedings: minor-debt disputes, ward-level ordinance violations, the low-tier administrative functions that the Crown's formal apparatus cannot be bothered to seat closer to the Red Keep. The chandler who owns the house benefits from the regular rent and the implied respectability of hosting official-adjacent proceedings; the proceeding-runners benefit from a room with a table and a door.

The room's court status is pretext-adjacent: proceedings here have the form of judicial process (a presiding figure, a written record, an accused presented before a verdict-giver) without the formal standing of a Crown court. Verdicts issued here are enforceable under ward-elder authority or faction household pressure, not under crown seal. The distinction is invisible to anyone who cannot read the difference, which is most of the ward.

In 122 AC: the room is in regular use by the Green-faction ward apparatus for the lower-tier administrative processing of Black-sympathizer-adjacent ward residents. The proceedings are faster and cheaper than formal courts, and the verdicts are final at ward-network level.

## Layout

**Back room (main chamber):** The room is larger than the chandler's standard workspace — it was adapted for the purpose, or the chandler's house is larger than typical. A long table runs along the room's primary axis; the presiding figure sits at the far end with the ward's relevant document stack and the charge ledger. The accused stands or sits at the near end; the gap between them is the proceeding's entire physical geography. A clerk's position at the table's side holds the record-ledger and document stack.

**Clerk's position (table-side):** Where the Green-faction clerk sits during proceedings. This is the position from which documents enter the proceeding — the list-output, the evidence packet, the pre-prepared charge. The clerk handles documents and does not speak unless asked; the clerk's role is to set papers at the table's edge at the correct moment.

**Door (single, to front-of-house corridor):** The room has one door. It is the only entrance and exit for the proceeding's participants. The accused enters here; no party exits during a proceeding without marking the end of the formal portion.

**Ceiling-corner (observer geometry):** The room's ceiling is low by court standards — the chandler's back room was not built for ceremony. A corner above the door end of the table is the highest accessible point in the room; it is the natural observation position for an insect-feed anchor held at ceiling-level. From there, the full table length is visible, including the clerk's document stack and the magistrate's writing position.

## Sensory Vocabulary

**Smell:** Tallow from the chandler's trade is the base note — not fresh rendering (that is in the workroom) but the ambient accumulation of wax dust and wick-smoke in the house walls, older than the current occupant's tenure. The back room adds a document smell: paper and dust and the slightly sharp note of ink used regularly in small quantities. If the door is open to the corridor, the tallow note strengthens briefly.

**Sound:** During proceedings: the scratch of the magistrate's quill — the pre-inscribed procedural form being completed as the accused speaks, so that the writing occurs simultaneously with the formal verbal portion and does not wait for it. The accused's voice is the only other sound of consequence; the clerk does not speak, and the magistrate asks questions whose answers the form already contains. Outside the room, the chandler's house is a working building: dull thumps, the occasional creak of the front shop floor, sound that enters at low register through the door.

**Light:** The back room's light is ambient and flat — the chandler's house does not receive direct light in this room at any time of day. Candles on the table supplement on grey days. The effect is that the room is always slightly underlit relative to outdoor expectation: faces at the table are visible but not strongly characterized by light.

**Texture:** The table is plain wood — serviceable, not a court piece. Long use has smoothed the section in front of the magistrate's position. The chair at the magistrate's end is the room's only substantial piece of furniture; the accused's end may have a stool or nothing.

## Fixed Props

- `oc-d06-document` (present during b01c13 s02; set by the clerk at the table edge before the proceeding opens — runtime state, not permanently fixed here)
- `oc-procedural-form` (present during active proceedings — the magistrate's document; runtime state)

## Exits

- **Single door (to front-of-house corridor, chandler's house):** Only exit. Opens toward the chandler's front-of-house. The corridor connects to the chandler's shop entrance, which opens onto the Hook-fringe lane. There is no rear exit from the back room.

## Hazards

- **Verdict-before-speech:** The magistrate writes before the accused finishes speaking. Anyone observing who can read the timing understands that the proceeding's outcome was determined before the accused entered the room. The accused typically cannot read this timing, which is the procedural's working mechanism.
- **Document-order primacy:** The document the Green-faction clerk sets at the table edge (the list-output, the intelligence report) is the operative input for the verdict, not the accused's presentation. The form of the proceeding — accusation, evidence, response — exists to create a record; it is not the decision pathway.
- **Single-exit geometry:** One door in and out. The accused cannot leave without the proceeding's formal conclusion, which is the magistrate's verbal release. Anyone arriving at the door during a proceeding has an audience with everyone in the room simultaneously.
- **Rented-room legitimacy gap:** The room's status as court-pretext is not visible in its furniture or procedure. A ward resident brought here for the first time has no way to distinguish this proceeding from a formal Crown court unless they know the address and the tenant.

## Ambient Interruption Hooks

- Chandler's shop noise breaking through the door at an inopportune moment — a delivered load, a customer argument, sound that enters the proceeding and creates a pause in the magistrate's writing
- A second proceeding waiting in the front corridor — muffled presence behind the door, audible to the accused
- The candle on the table burning low during an extended proceeding — the room darkening incrementally
- The clerk setting a document at the wrong moment — timing error in the apparatus choreography, visible to an observer who knows the sequence
- Rain beginning outside — the chandler's house has a thin roof; rain on the tiles changes the ambient sound register of the back room

## VIBES

green-faction-apparatus, pretext-proceeding, verdict-before-speech, list-operative, chandler-house, hook-ward-fringe, document-primacy
