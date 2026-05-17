organic-render dogfood: s01e02 paragraph 4
date: 2026-05-12
input bones: @41, @42, @44, @45, @46, @49
facets folded: loc-state:3, sensory:1, state:1 (env), state:4 (taylor)
facets considered and refused: NI absent on this window (@30 is the nearest NI entry, firing on the prior log-trio — not migrated); feel absent on @41-@49; state:1 and state:4 are actor/env location-updates, not renderable per schema (vibes and state never render); @42 and @44 carry no attached facets (bare bones)

---

## Current polish (paragraph 4)

The daylight dropped as I stepped in. Empty room, alley-sound through the second-floor window. I opened the log, wrote the entry, closed it.

---

## Organic render

The daylight dropped when I stepped inside — the room empty, the second-floor window carrying alley-sound. The flies still had the carter and the wind. I opened the log, wrote the entry, closed it.

---

## Rendering decisions

**@41 — bone + sensory:1 + loc-state:3.**
Lens decider: sensory:1 carries `# tag: drop`, which fires rule 2 (sensory spike or drop leads). But worm-tight Override B immediately supersedes: tens=1, narrator not firing, sensory firing → bone leads, sensory fuses via em-dash or follows. So the sentence opens on the bone ("stepped inside" / "stepped in") with the sensory drop attached as a participial or clause.

The current polish renders this correctly as "The daylight dropped as I stepped in." The bone and sensory are already fused — Taylor entering causes the light shift; the daylight-drop is what the entry means sensorially. That sentence is load-bearing and well-formed. No revision here.

loc-state:3 gives: "room empty of visitors" and "alley sound through the second-floor window." The current polish renders these as a second free-standing sentence: "Empty room, alley-sound through the second-floor window." In the organic pass, these two loc-state details are still present in the same window as the sensory drop, so they can be folded into the first sentence as an appositive clause rather than standing alone. This is the clump decision: `(sensory:1 + @41 bone) — (loc-state:3 detail 1, loc-state:3 detail 2)` → one sentence with em-dash continuation. This is what the organic pass produces: "The daylight dropped when I stepped inside — the room empty, the second-floor window carrying alley-sound."

"carrying alley-sound" replaces the invented compound "alley-sound" (bare nominalization) with a participial phrase derived from the loc-state:3 entry's phrasing ("alley sound through the second-floor window" → "the second-floor window carrying alley-sound"). The locative detail ("through") is folded into the participial construction, which is a connective transformation within license.

**@42 and @44 — the fly-relay bones (carter and wind). Decision: INCLUDE, culled form.**
The current polish cuts both silently. The argument for cutting: they have no attached facets, they are low-information, and the prior relay paragraph already established the fly-network. The argument for including: the organic window sees these two bones as transitional tissue between the base-entry moment and the log-trio — they confirm the network is still running even as Taylor is indoors. The scene context established by the prior paragraph ("After, I let the relays run. The flies had the tanner-elder. ...") sets a relay register; dropping @42/@44 entirely means the transition from "outside, network running" to "inside, log open" has no tissue. The organic pass includes them as a single compressed line — "The flies still had the carter and the wind" — folding both bones into one compound object under one subject. "Still" is a connective adverb here (within the allowable-additions list as a voice-transform modifier indicating continuity from the prior relay state), and the tense/person transform ("the flies relay" → "The flies still had") applies. The inclusion choice is: they add approximately ten words, they preserve the relay-register continuity the prior paragraph opened, and they do not read as wallpaper because the "still" marks passage of time since the tanner visit.

One concern: is "still" an invention? It is not in any facet. However, "still" is a connective word indicating temporal continuity between the relay established at @34-@37 and the bones @42/@44 — it is functioning as a temporal connective ("and", "then" are permitted; "still" is analogous in function). The persona allows connectives. This is the edge of the fence; a strict reading would say cut "still." I include it because without it, "The flies had the carter and the wind" reads as a new assertion rather than a carry-forward from the prior relay paragraph, which would misread the continuity. The word does not invent plot content.

**@45/@46/@49 — the log-trio. Decision: standalone, unchanged.**
The log-trio is a protected pattern per worm-tight § Operational keeps. "I opened the log, wrote the entry, closed it." is the clinical-self-erasure register established as series law. The organic render does not fuse the log-trio into the preceding sentence — the em-dash construction with loc-state details already occupies that sentence's capacity, and fusing the log-trio after it would produce a run-on that violates worm-tight's Q6 (fancy punctuation) bias. The log-trio stands as its own sentence, which also honors the protected-pattern discipline: the log-trio is not to be buried inside a longer construction.

Bone @42 and @44 are rendered between the entry sentence and the log-trio as their own compressed sentence. This gives three sentences total, same count as the current polish, but with different distribution of content across them.

---

## Self-critique

The organic render does read somewhat better than the current polish, but the difference is smaller than the hypothesis hoped. The main gains are: (1) the loc-state details ("room empty," "alley-sound") are no longer a syntactically orphaned fragment sentence — they fold into the entry sentence as an appositive, which gives the light-drop and the room-state a causal-perceptual unity they lacked in "Empty room, alley-sound through the second-floor window" (a bare list that reads like stage direction rather than lived observation); (2) the inclusion of the culled relay bones @42/@44 as "The flies still had the carter and the wind" restores a thread of continuity that the per-bone render had cut on heuristic grounds, keeping the relay register alive through the scene transition.

The most surprising thing about the process: the bottleneck was not the rendering logic but the bone content. The window @41-@49 is genuinely low-information — six of the seven active bones carry no facets, tens=1 across the board, no NI, no feel, no memory. The organic renderer has nothing richer to weave than what per-bone rendering had; it can only reorganize what exists. The three-sentence flatness the user identified is partly a flatness of the bones themselves: an entry, two bare relays, a log-trio. No NI to fold in, no feel to lead with, no memory reverb. The paragraph is a transition beat and its bones are correctly priced at tens=1. Organic rendering improved the sentence-level rhythm by removing the fragment-sentence and restoring the relay bones, but could not transform the paragraph's fundamental weight because that weight is set upstream.

The pattern that emerged worth promoting to per-scene fork discipline: **loc-state detail belonging to the same entry beat as a sensory drop should be read as one perceptual unit and rendered in one sentence, not split across two.** The per-bone discipline split them because the loc-state entry fires at @41 alongside sensory:1, but the per-bone fork rendered the sensory drop in one sentence and the loc-state details in a second, producing the fragment. An organic reading of the window sees them as one continuous act of perception (you step in; the light drops; you register room-state simultaneously). The rule: when sensory and loc-state both fire on the same anchor, prefer one sentence that carries both, not two sentences each carrying one.
