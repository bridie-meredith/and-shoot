## Summary
total body lines: 33
CORRECT: 2 (lines 8, 17)
faults:
  FAULT-FORM-COPULA: 8 (lines 1, 2, 7, 18, 26, 27, 28, 30)
  FAULT-FORM-NEGATION: 4 (lines 14, 18, 23, 25, 28)
  FAULT-FORM-PERCEPTION: 3 (lines 5, 10, 20)
  FAULT-FORM-MODIFIER: 17 (lines 1, 2, 3, 6, 7, 9, 10, 11, 12, 13, 19, 21, 25, 29, 30, 31, 32)
  FAULT-FORM-INTERIORITY: 4 (lines 2, 14, 28, 33)
  FAULT-FORM-CONJUNCTION: 13 (lines 3, 4, 5, 11, 15, 18, 19, 20, 22, 23, 24, 25, 29)
  FAULT-FORM-NO-VERB: 2 (lines 1, 26)
  FAULT-FORM-MULTI-SUBJECT: 3 (lines 18, 23, 31)
  FAULT-PHYSICAL-ACTOR-ABSENT: 1 (line 16)
file-level: FAIL — 31 of 33 body lines carry at least one fault; only lines 8 and 17 are clean

---

```yaml
audit:
  scope: episode
  target: s01e01
  timestamp: 2026-05-07
  findings:

    - id: fault-001
      type: fault
      what: "line 1 — 'The morning is bright on the sept flagstones' — FAULT-FORM-COPULA (is), FAULT-FORM-MODIFIER (bright; on the sept flagstones), FAULT-FORM-NO-VERB (no concrete physical action)"
      why: State assertion with adjective padding; downstream facet-authoring treats this as a proto-line anchor but there is no physical event to cite — corrupts loc-state and tens facets
      criteria: DELETE or RECAST-AS-HOLD — any environmental state belongs in a loc-state facet, not the proto-line spine; if a physical event is implied (e.g. light falling on flagstones), recast with a named subject performing a concrete act

    - id: fault-002
      type: fault
      what: "line 2 — 'Taylor is tired from the night before' — FAULT-FORM-COPULA (is), FAULT-FORM-INTERIORITY (tired is an internal state), FAULT-FORM-MODIFIER (tired; from the night before)"
      why: Pure interiority line with no physical event; feel/state facets own tiredness — proto-line carrying it contaminates the spine with unfacetable content
      criteria: DELETE — internal state belongs in feel or state-update facet citing the flanking proto-lines; no replacement proto-line needed unless there is a physical expression (e.g. Taylor braces against the doorframe)

    - id: fault-003
      type: fault
      what: "line 3 — 'Mira speaks to the yard loudly that the officer will want the unattached ones first' — FAULT-FORM-MODIFIER (loudly, adverb), embedded content clause ('that the officer will want the unattached ones first' carries dialogue content and a future-tense interiority claim)"
      why: Adverb modifier violates no-modifier rule; embedded dialogue content belongs in Mira's dialogue file, not the proto-line body — facet-authoring will double-count the content
      criteria: RECAST-AS-HOLD — strip to 'Mira speaks to the yard'; dialogue content and volume route to Mira's dialogue file and narrator/feel facets

    - id: fault-004
      type: fault
      what: "line 4 — 'Edric positions himself at the gate post and looks out at the road' — FAULT-FORM-CONJUNCTION (and joining two beats)"
      why: Two distinct physical acts conflated into one proto-line; shape and trim passes will be unable to selectively cut one without cutting both
      criteria: SPLIT-INTO-2 — two proto-lines: (a) Edric moves to the gate post; (b) Edric looks toward the road

    - id: fault-005
      type: fault
      what: "line 5 — 'Taylor reads Mira's tone and notes the warning' — FAULT-FORM-PERCEPTION (reads, notes — both on denied perception-verb list per svo-split-notes), FAULT-FORM-CONJUNCTION (and)"
      why: Both verbs are POV-leak perception verbs; letting these survive into locked proto-lines trains downstream facets to treat perception as physical event — corrupts narrator and feel facets structurally
      criteria: DELETE — both acts are perception events; recast as the physical proto-line that Mira executed (e.g. 'Mira raises her voice') and route Taylor's perception to narrator/feel facets citing that line

    - id: fault-006
      type: fault
      what: "line 6 — 'The census officer enters through the sept gate with his clerk' — FAULT-FORM-MODIFIER (through the sept gate, prepositional padding; with his clerk, prepositional padding adding a second actor)"
      why: Two prepositional phrases pad the SVO spine; 'with his clerk' implies a compound-subject entry that belongs as a separate proto-line for the clerk
      criteria: SPLIT-INTO-2 + trim modifiers — (a) 'the census-officer enters the gate'; (b) 'the clerk enters the gate' — or if entry is one beat, 'the census-officer enters the gate' with clerk entry as its own line; strip both prepositional phrases

    - id: fault-007
      type: fault
      what: "line 7 — 'The clerk is carrying a heavy ledger and an ink case' — FAULT-FORM-COPULA (is, as auxiliary in progressive construction), FAULT-FORM-MODIFIER (heavy, adjective), FAULT-FORM-CONJUNCTION (and)"
      why: Progressive-aspect copula, adjective modifier, and conjunction all violate SVO discipline; downstream state-update facet cannot cleanly record prop inventory from a malformed proto-line
      criteria: RECAST-AS-HOLD + strip modifiers — 'the clerk carries the ledger' (single object, drop heavy and ink case; if ink case is narratively load-bearing, a second proto-line)

    - id: fault-008
      type: fault
      what: "line 9 — 'Taylor moves into the yard with the assembled wards' — FAULT-FORM-MODIFIER (with the assembled wards, prepositional padding; assembled, adjective)"
      why: Prepositional padding obscures the clean location-state change Taylor's move represents; modifier-laden proto-lines bias loc-state facet authoring
      criteria: RECAST-AS-HOLD — strip to 'Taylor moves to the yard'; the assembled wards are context handled by loc-state or narrator facets

    - id: fault-009
      type: fault
      what: "line 10 — 'Taylor counts twelve wards in the line' — FAULT-FORM-PERCEPTION (counts is on the denied perception-verb list per svo-split-notes), FAULT-FORM-MODIFIER (in the line, prepositional padding)"
      why: Perception verb survives into locked proto-lines and trains narrator/feel facets to treat Taylor's counting as a physical event rather than a cognitive one
      criteria: DELETE or RECAST — if the physical event is that twelve people are standing in line, recast as 'twelve wards stand in the line' (environment SVO); Taylor's perception of the count belongs in a narrator/feel facet

    - id: fault-010
      type: fault
      what: "line 11 — 'The officer works through the wards, dictating names and ages and blood-claims to the clerk' — FAULT-FORM-MODIFIER (participial phrase 'dictating names and ages and blood-claims to the clerk' as trailing modifier), FAULT-FORM-CONJUNCTION (and, twice in object list)"
      why: Participial modifier encoding a second beat and conjunctions in the object list; two distinct actions (moving through wards + dictating) cannot be resolved independently by trim or shape passes
      criteria: SPLIT-INTO-2 — (a) 'the officer moves through the ward line'; (b) 'the officer speaks to the clerk' (with dictation content in dialogue file); strip conjunctions from object list

    - id: fault-011
      type: fault
      what: "line 12 — 'The clerk writes carefully into the ledger' — FAULT-FORM-MODIFIER (carefully, adverb; into the ledger, prepositional padding)"
      why: Adverb violates no-modifier rule; prepositional padding is redundant (writing implies the ledger via object); downstream state-update facet receives an imprecise anchor
      criteria: RECAST-AS-HOLD — strip to 'the clerk writes in the ledger' or 'the clerk writes the entry'; remove carefully

    - id: fault-012
      type: fault
      what: "line 13 — 'The officer reaches Taylor at the end of the line' — FAULT-FORM-MODIFIER (at the end of the line, prepositional padding)"
      why: Prepositional phrase is staging context that belongs in loc-state facet, not the proto-line body
      criteria: RECAST-AS-HOLD — strip to 'the officer reaches Taylor'

    - id: fault-013
      type: fault
      what: "line 14 — 'The officer doesn't ask anyone else this question' — FAULT-FORM-NEGATION (doesn't), FAULT-FORM-INTERIORITY (non-event observed by Taylor's POV — no physical event occurs)"
      why: Negation banned; no physical event can be cited by downstream facets — this line is a POV inference, not an observable act
      criteria: DELETE — the absence of a question to others is not a proto-line; Taylor's POV inference belongs in a narrator/feel facet citing the officer's movement proto-lines

    - id: fault-014
      type: fault
      what: "line 15 — 'The officer asks Taylor for her name and age and wardship' — FAULT-FORM-CONJUNCTION (and, twice in object list)"
      why: Conjunctions violate SVO discipline even in object lists unless the verb acts on the set as one physical event; 'and wardship' makes this a compound demand, not a clean set
      criteria: RECAST-AS-HOLD — recast as 'the officer speaks to Taylor'; dialogue content (the specific demands) routes to officer's dialogue file; strip conjunctions

    - id: fault-015
      type: fault
      what: "line 16 — 'Taylor states her name and age and that Septon Osmynd holds her wardship' — FAULT-FORM-CONJUNCTION (and, twice), FAULT-PHYSICAL-ACTOR-ABSENT (Septon Osmynd — the dying septon at this location is Septon Aldric per loc-harrenhal-sept-environs; the name Osmynd does not appear in any active card or memory file)"
      why: Wrong name for the septon means the attestation beat names a non-existent character; if this proto-line survives, downstream dialogue and state-update facets will reference a fabricated actor slug
      criteria: RECAST-AS-HOLD + RENAME-SLUG — recast as 'Taylor speaks to the officer'; strip conjunctions; dialogue content (including correct septon name Aldric) routes to Taylor's dialogue file

    - id: fault-016
      type: fault
      what: "line 18 — 'The sept doors are closed and no one comes out' — FAULT-FORM-COPULA (are), FAULT-FORM-CONJUNCTION (and), FAULT-FORM-MULTI-SUBJECT (the sept doors + no one — two subjects), FAULT-FORM-NEGATION (no one comes out)"
      why: Four simultaneous violations; the line encodes a non-event (nothing happens) — negation and copula both banned; multi-subject and conjunction cannot be resolved without splitting into constituent lines that may themselves be non-events
      criteria: DELETE or RECAST — if the physical event is that the doors remain closed, recast as 'the sept doors hold closed' (single subject, hold-verb, no negation); the absent septon is a narrator/feel facet, not a proto-line

    - id: fault-017
      type: fault
      what: "line 19 — 'Taylor takes out the septon's written letter and presents it' — FAULT-FORM-CONJUNCTION (and joining two beats), FAULT-FORM-MODIFIER (written, adjective modifying letter)"
      why: Two distinct physical acts (retrieval and presentation) joined by and; trim pass cannot cut one independently; adjective modifier violates no-modifier rule
      criteria: SPLIT-INTO-2 + strip modifier — (a) 'Taylor produces the letter'; (b) 'Taylor presents the letter to the officer'

    - id: fault-018
      type: fault
      what: "line 20 — 'The officer reads it and folds it back and hands it to Taylor' — FAULT-FORM-PERCEPTION (reads, on the denied perception-verb list), FAULT-FORM-CONJUNCTION (and, twice — three beats joined)"
      why: Perception verb and two conjunctions; three distinct beats merged; pass 2 cannot legally allow reads to survive; downstream facets will attempt to cite a perception event as a physical proto-line
      criteria: SPLIT-INTO-3 + RECAST perception verb — drop reads or recast (the officer reviews the letter → 'the officer unfolds the letter'); separate fold and hand as individual proto-lines

    - id: fault-019
      type: fault
      what: "line 21 — 'The officer states that without a sworn guardian present the attestation is insufficient' — FAULT-FORM-MODIFIER (without a sworn guardian present, prepositional/participial phrase; sworn, adjective; the entire embedded clause is dialogue content), FAULT-FORM-COPULA (is insufficient in the embedded clause)"
      why: Embedded clause carries dialogue content and contains a copula; proto-line should be dialogue-beat shape 'the officer speaks to Taylor'; modifier-laden embedded clause corrupts SVO spine and biases dialogue-file authoring
      criteria: RECAST-AS-HOLD — strip to 'the officer speaks to Taylor'; dialogue content routes to officer's dialogue file

    - id: fault-020
      type: fault
      what: "line 22 — 'Taylor turns to Mira and asks her to stand as witness' — FAULT-FORM-CONJUNCTION (and joining two beats)"
      why: Two beats (turn + ask) merged; shape pass cannot reorder independently
      criteria: SPLIT-INTO-2 — (a) 'Taylor turns to Mira'; (b) 'Taylor speaks to Mira'

    - id: fault-021
      type: fault
      what: "line 23 — 'Mira looks at the yard stones and says nothing while everyone watches' — FAULT-FORM-CONJUNCTION (and, while), FAULT-FORM-NEGATION (says nothing), FAULT-FORM-MULTI-SUBJECT (Mira + everyone — two subjects)"
      why: Three simultaneous violations; negation and multi-subject are both hard bans; downstream facets receive an anchor with no clean physical event
      criteria: DELETE partial + RECAST — (a) 'Mira looks at the yard stones' (clean SVO, keep); remove 'says nothing while everyone watches' entirely (negation, multi-subject) — crowd behavior routes to loc-state or narrator facet

    - id: fault-022
      type: fault
      what: "line 24 — 'Taylor turns to Edric and asks him to step forward and speak for her' — FAULT-FORM-CONJUNCTION (and, twice)"
      why: Three beats merged by two conjunctions; trim pass cannot address independently
      criteria: SPLIT-INTO-3 — (a) 'Taylor turns to Edric'; (b) 'Taylor speaks to Edric'; remove 'and speak for her' as content belonging in dialogue file

    - id: fault-023
      type: fault
      what: "line 25 — 'Edric does not speak and steps back through the sept door' — FAULT-FORM-NEGATION (does not speak), FAULT-FORM-CONJUNCTION (and), FAULT-FORM-MODIFIER (through the sept door, prepositional padding)"
      why: Negation, conjunction, and modifier; the non-speech act is a non-event; physical event is the retreat — only that survives
      criteria: RECAST-AS-HOLD + strip negation and modifier — 'Edric steps back' or 'Edric retreats through the door'; the non-speech is a feel/narrator facet

    - id: fault-024
      type: fault
      what: "line 26 — 'The yard is silent' — FAULT-FORM-COPULA (is), FAULT-FORM-NO-VERB (no physical action)"
      why: State assertion with no physical event; cannot be cited by any facet as a proto-line anchor — belongs entirely in a loc-state facet
      criteria: DELETE — silence is a loc-state facet entry; no proto-line replacement needed

    - id: fault-025
      type: fault
      what: "line 27 — 'The clerk asks Taylor whether she has been assessed before' — FAULT-FORM-COPULA (has been, in embedded clause)"
      why: Copula in embedded clause; proto-line should be dialogue-beat shape; the embedded question content belongs in clerk's dialogue file
      criteria: RECAST-AS-HOLD — strip to 'the clerk speaks to Taylor'; dialogue content routes to clerk's dialogue file

    - id: fault-026
      type: fault
      what: "line 28 — 'Taylor knows this question was put to no other ward' — FAULT-FORM-INTERIORITY (knows, cognitive internal state), FAULT-FORM-COPULA (was put, passive copula), FAULT-FORM-NEGATION (no other ward)"
      why: Pure interiority line with three co-present violations; nothing observable occurred; facets have no physical event to cite
      criteria: DELETE — this is entirely a narrator/feel facet entry citing the clerk's proto-line (line 27); no proto-line replacement needed

    - id: fault-027
      type: fault
      what: "line 29 — 'The clerk writes Taylor's entry into the ledger and marks a double-stroke notation in the margin' — FAULT-FORM-CONJUNCTION (and joining two beats), FAULT-FORM-MODIFIER (double-stroke, adjective; into the ledger, prepositional; in the margin, prepositional)"
      why: Two distinct physical acts and multiple modifier violations; trim pass cannot separate the write from the notation mark
      criteria: SPLIT-INTO-2 + strip modifiers — (a) 'the clerk writes the entry'; (b) 'the clerk marks the margin'

    - id: fault-028
      type: fault
      what: "line 30 — 'The officer states that Taylor is on the provisional labor-eligibility list pending cognitive assessment by the traveling maester' — FAULT-FORM-COPULA (is in embedded clause), FAULT-FORM-MODIFIER (provisional, adjective; traveling, adjective; pending cognitive assessment by the traveling maester, participial/prepositional phrase), embedded dialogue content"
      why: Copula plus four modifier violations plus embedded dialogue; proto-line shape for a speech act is 'speaks to'; this survives pass 2 as a constraint-relevant beat (impressment outcome) but in completely illegal form
      criteria: RECAST-AS-HOLD — strip to 'the officer speaks to Taylor'; dialogue content (including the list placement and maester assessment notice) routes to officer's dialogue file

    - id: fault-029
      type: fault
      what: "line 31 — 'The officer and clerk exit through the gate with the ledger sealed in the case' — FAULT-FORM-MULTI-SUBJECT (the officer and clerk — two named subjects), FAULT-FORM-MODIFIER (through the gate, prepositional; with the ledger sealed in the case, prepositional; sealed, adjective)"
      why: Multi-subject ban and multiple modifiers; two actors departing is two proto-lines; modifier padding obscures the prop-state change (ledger sealed) which belongs in a state-update facet
      criteria: SPLIT-INTO-2 + strip modifiers — (a) 'the officer exits the gate'; (b) 'the clerk exits the gate'; ledger-sealed state routes to state-update facet

    - id: fault-030
      type: fault
      what: "line 32 — 'Taylor stands alone in the yard holding the letter' — FAULT-FORM-MODIFIER (alone, adjective; in the yard, prepositional padding; holding the letter, participial modifier encoding a second concurrent act)"
      why: Three modifier violations; participial phrase adds a second beat; Taylor's isolation is interiority/feel territory, not a proto-line modifier
      criteria: RECAST-AS-HOLD + strip modifiers — 'Taylor holds the letter' (the hold-verb captures the physical state); or 'Taylor stands in the yard' as a position beat separate from 'Taylor holds the letter'

    - id: fault-031
      type: fault
      what: "line 33 — 'Taylor feels the moment the window closes' — FAULT-FORM-INTERIORITY (feels, internal state verb)"
      why: Pure interiority closing line; no physical event; downstream facets have no proto-line to cite for this beat
      criteria: DELETE — this is a feel/narrator facet entry; no proto-line replacement needed unless there is a physical correlate (e.g. 'the gate swings shut')
```
