## chapter-01 pass-2 repairs — 2026-05-07

chapter-01 | fault-001 | RECAST-PHYSICAL: removed prepositional padding | `septon-dying-protector breathes in the cottage below` → `septon-dying-protector breathes`
chapter-01 | fault-002 | RECAST-PHYSICAL: removed prepositional padding | `the ravens call in the bell tower` → `the ravens call`
chapter-01 | fault-003 | RECAST-PHYSICAL: removed adverb modifier | `the sept candles gutter low` → `the sept candles gutter`
chapter-01 | fault-004 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros lights a candle at the altar` → `taylor-hebert-westeros lights a candle`
chapter-01 | fault-005 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros opens a book at the altar table` → `taylor-hebert-westeros opens a book`
chapter-01 | fault-006 | RECAST-PHYSICAL: removed prepositional padding | `a village woman knocks at the cottage door` → `a village woman knocks`
chapter-01 | fault-007 | RECAST-PHYSICAL: removed prepositional padding | `septon-dying-protector stirs on the bed` → `septon-dying-protector stirs`
chapter-01 | fault-008 | RECAST-PHYSICAL: removed prepositional padding | `the village woman sets the broth pot on the table` → `the village woman sets the broth pot`
chapter-01 | fault-009 | RECAST-PHYSICAL: removed prepositional padding | `the ravens flush from the bell tower` → `the ravens flush`
chapter-01 | fault-010 | RECAST-PHYSICAL: removed directional padding | `three riders crest the road from the north` → `three riders crest the road`
chapter-01 | fault-011 | RECAST-PHYSICAL: removed prepositional padding | `the riders stop at the sept yard gate` → `the riders stop`
chapter-01 | fault-012 | RECAST-PHYSICAL: transitive recast preserving destination weight | `taylor-hebert-westeros steps back` → `taylor-hebert-westeros retreats`
chapter-01 | fault-013 | RECAST-PHYSICAL: removed prepositional padding (also covered by fault-048 slug rename) | `oc-castellan-harrenhal's officer knocks at the cottage door` → `census-officer knocks`
chapter-01 | fault-014 | RECAST-PHYSICAL: removed prepositional padding (also fault-048) | `oc-castellan-harrenhal's officer makes a notation on the scroll` → `census-officer makes a notation`
chapter-01 | fault-015 | RECAST-PHYSICAL: removed adverb, collapsed to intransitive | `septon-dying-protector falls back` → `septon-dying-protector falls`
chapter-01 | fault-016 | RECAST-PHYSICAL: removed adjective modifier (also fault-048) | `oc-castellan-harrenhal's officer produces a writing quill` → `census-officer produces a quill`
chapter-01 | fault-017 | ABSORBED: line 89 blanked; beat absorbed by fault-040 resolution (quill-drop is downstream of release on line 88) | `the quill drops to the floor` → [blanked; ID 89 preserved as gap]
chapter-01 | fault-018 | RECAST-PHYSICAL: removed adverb (also fault-048) | `oc-castellan-harrenhal's officer marks the scroll again` → `census-officer marks the scroll`
chapter-01 | fault-019 | RECAST-PHYSICAL: removed adjective modifier | `a man-at-arms produces a second scroll` → `a man-at-arms produces a scroll`
chapter-01 | fault-020 | RECAST-PHYSICAL: removed prepositional+adjective padding (also fault-048) | `oc-castellan-harrenhal's officer makes a notation on the second scroll` → `census-officer makes a notation`
chapter-01 | fault-021 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros holds the feet in the yard` → `taylor-hebert-westeros holds the feet`
chapter-01 | fault-022 | RECAST-PHYSICAL: removed adverb+prepositional padding | `the riders turn north on the Harrenhal road` → `the riders turn`
chapter-01 | fault-023 | RECAST-PHYSICAL: removed prepositional padding | `the ravens resettle in the bell tower` → `the ravens resettle`
chapter-01 | fault-024 | RECAST-PHYSICAL: removed directional padding | `taylor-hebert-westeros turns from the window` → `taylor-hebert-westeros turns`
chapter-01 | fault-025 | RECAST-PHYSICAL: removed adjective modifier | `taylor-hebert-westeros takes the septon's writing materials` → `taylor-hebert-westeros takes the septon's materials`
chapter-01 | fault-026 | RECAST-PHYSICAL: substituted verb to avoid adverb | `taylor-hebert-westeros sets the book down` → `taylor-hebert-westeros places the book`
chapter-01 | fault-027 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros kneels at the altar` → `taylor-hebert-westeros kneels`
chapter-01 | fault-028 | DELETE: perception verb, no clean physical recast; line 8 blanked | `taylor-hebert-westeros scans the Harrenhal road` → [deleted; route to narrator/feel facet citing line 7]
chapter-01 | fault-029 | DELETE: perception verb per audit recommendation; line 16 blanked | `taylor-hebert-westeros reads the page` → [deleted; route to narrator/feel facet citing line 15]
chapter-01 | fault-030 | RECAST-PHYSICAL: perception verb recast as physical orientation, modifier dropped | `the village woman glances toward the Harrenhal road` → `the village woman turns`
chapter-01 | fault-031 | DELETE: perception verb, repeat instance; line 33 blanked | `taylor-hebert-westeros scans the Harrenhal road` → [deleted; route to narrator/feel facet citing line 32]
chapter-01 | fault-032 | RECAST-PHYSICAL: perception verb recast as physical orientation (also fault-048) | `oc-castellan-harrenhal's officer looks at taylor-hebert-westeros` → `census-officer turns toward taylor-hebert-westeros`
chapter-01 | fault-033 | RECAST-PHYSICAL: perception verb recast as physical orientation per audit alternative (also fault-048) | `oc-castellan-harrenhal's officer scans the outbuildings` → `census-officer turns toward the outbuildings`
chapter-01 | fault-034 | DELETE: perception verb; line 62 blanked; blank ID preserved as structural gap (also fault-048) | `oc-castellan-harrenhal's officer sees septon-dying-protector on the bed` → [deleted; septon bed-location to state-update facet]
chapter-01 | fault-035 | RECAST-PHYSICAL: idiomatic perception act replaced with physical body-orientation | `taylor-hebert-westeros meets the officer's eyes` → `taylor-hebert-westeros raises her eyes`
chapter-01 | fault-036 | DELETE: perception verb, third instance; line 120 blanked | `taylor-hebert-westeros scans the Harrenhal road` → [deleted; route to narrator/feel facet citing line 119]
chapter-01 | fault-037 | RECAST-PHYSICAL: stative flank recast as discrete positioning act; "beside" modifier retained as minimum viable form — flag for auditor re-review | `two men-at-arms flank a mounted official` → `two men-at-arms take position beside the official`
chapter-01 | fault-038 | DELETE: stative environment-observation, redundant with line 47; line 36 blanked | `a packaged scroll protrudes from the official's saddlebag` → [deleted; route to location-state facet]
chapter-01 | fault-039 | RECAST-PHYSICAL: stative flank recast as motion act (also fault-048) | `the men-at-arms flank the yard entrance` → `the men-at-arms cross to the yard entrance`
chapter-01 | fault-040 | RECAST-PHYSICAL: stative-result verb replaced; actor restored as subject; line 89 blanked as now-redundant downstream | `septon-dying-protector's hand fails` → `septon-dying-protector releases the quill`; line 89 blanked
chapter-01 | fault-041 | DELETE: stative/perceptual gradual-change verb; line 121 blanked | `the riders diminish on the northern road` → [deleted; route to narrator/feel facet]
chapter-01 | fault-042 | RECAST-PHYSICAL: unlicensed abstract-object hold replaced with licensed body-part hold | `taylor-hebert-westeros holds the position` → `taylor-hebert-westeros holds the spine`
chapter-01 | fault-043 | SPLIT-INTO-N: intent verb split into two observable beats | `septon-dying-protector attempts to rise` → line 71: `septon-dying-protector rises`; line 72: `septon-dying-protector falls`
chapter-01 | fault-044 | RECAST-PHYSICAL: perception-noun object replaced with physical body-part object | `taylor-hebert-westeros drops her gaze` → `taylor-hebert-westeros lowers her eyes`
chapter-01 | fault-045 | RECAST-PHYSICAL: intent verb replaced with observable physical act | `septon-dying-protector attempts a signature` → `septon-dying-protector marks the scroll`
chapter-01 | fault-046 | DELETE: copula-equivalent stative construction; line 9 blanked | `the road shows empty` → [deleted; route to narrator/feel or location-state facet]
chapter-01 | fault-047 | RECAST-PHYSICAL: invalid location-listener replaced with physical call-out act | `oc-castellan-harrenhal's officer speaks to the yard` → `census-officer calls out`
chapter-01 | fault-048 | RENAME-SLUG: global replace throughout file | `oc-castellan-harrenhal's officer` → `census-officer` (all subject lines)

---

## fault-001 — RESOLVED
fault: line 58 "a girl appears the mill hamlet road edge" — existential verb, no actor action
scope: line
change: recast to "oc-girl-from-hamlet rounds the mill hamlet road edge" — physical movement verb, named actor
criteria met: yes

## fault-002 — RESOLVED
fault: line 31 "the headache starts" — state-onset verb, no actor action
scope: line
change: recast to "taylor-hebert-westeros presses the temples" — physical action marks onset
criteria met: yes

## fault-003 — RESOLVED
fault: line 52 "the nosebleed starts" — state-onset verb, no actor action
scope: line
change: recast to "blood marks the lip" — physical event, active verb
criteria met: yes

## fault-004 — RESOLVED
fault: protagonist named "Taylor" throughout ch02 instead of slug "taylor-hebert-westeros"
scope: line (global replace)
change: replace_all Taylor → taylor-hebert-westeros across chapter-02.md
criteria met: yes

---

chapter-03 | structural-narrator-escalation | full re-author with fauna-feed framing
