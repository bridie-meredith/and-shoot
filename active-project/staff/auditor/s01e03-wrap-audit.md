---
audit:
  scope: episode
  target: s01e03
  timestamp: 2026-05-13
  pipeline-gate: /and-wrap Phase 2
  auditor-version: URI-WRAP-V2
  disposition-authority: URI-WRAP-V2-DISPO (2026-05-13)
---

# /and-wrap Phase 2 Audit — s01e03

## Summary

HARD findings: 0
SIGNAL findings: 1 (CONTINUITY class)

Disposition breakdown (HARD only): N/A — no HARD findings.

Routing implication: zero graph-repair blocks; zero prose-surface blocks; zero acknowledge entries.
Editor pass is UNBLOCKED. The single SIGNAL finding is advisory; editor receives it as a flag.

---

## Class verdicts

| Class | Verdict | Notes |
|---|---|---|
| BONE-COVERAGE | PASS | bones_rendered=155, lost=0; all 155 active bones traced in annotated draft |
| DIALOGUE-VERBATIM | PASS | 12 utterances; all verbatim; attribution-split commas within allowed voice-transform |
| EXPOSITION-VERBATIM | PASS | 5 entries; all match source; clerk-gloss "the clerk's" → "his" is valid in-context pronoun voice-transform |
| NO-INVENTION | PASS | no extra-graph entities; Earth-Bet fence clean |
| CONTINUITY | SIGNAL (find-001) | one pronoun antecedent ambiguity; tense/person/contraction register intact throughout |
| BLOCKING | PASS | perimeter circuit ordering correct; scene-E and scene-K spatial transitions verified |
| SCENE-MAP-RESPECT | PASS | all 11 scene boundaries correctly placed; absence of scene-break markers in stitcher draft is expected pre-editor state |
| EARTH-BET-HARD-FENCE | PASS | no hits on fence list (Khepri, Skitter, Brockton Bay, Coil, Cauldron, Endbringer, shard, capes, parahuman, PRT) |

---

## Findings

```yaml
findings:
  - id: find-001
    class: CONTINUITY
    severity: SIGNAL
    disposition: N/A (SIGNAL; advisory only)
    excerpt: "and the interior had the count of years"
    citation: >
      annotated draft L97 / proto-lines @125 /
      facets [mem:8, narrator:30, exposition:3]
      clean draft line 65: "I faced the Red Keep — the king's castle above the city —
      and the interior had the count of years for what the seat above the city was going to be."
    rationale: >
      "The interior" lacks a syntactically unambiguous antecedent. The most recent noun
      phrase in the sentence is "the city" (via the exposition em-dash fold for "the Red Keep"),
      which could allow a reader to parse "the interior" as referring to the Red Keep's interior
      rather than Taylor's interior state. The displacement-clamp SHAPE pattern (mem:8,
      worm-tight Westerosi-monument clamp) makes the intended reading clear in context, but
      the surface ambiguity is real enough to note.
    recommended-action: >
      Editor may clarify the antecedent with a minimal surface adjustment — for example,
      anchoring "the interior" to the POV body ("my interior" or "the body's interior") — if
      the prose-economy trade-off is acceptable within the bone-faithfulness fence. No
      obligation; this is advisory.
```

---

## Verification notes per class

### BONE-COVERAGE
Verified: render-log Phase 8 STATS bones_rendered=155, bones_cut=0, lost=0. Annotated draft carries 11 scene-trace blocks covering the complete active bone range (1–16, 18–31, 33–48, 50–54, 56–71, 73–94, 96–108, 110–125, 127–134, 136–146, 148–165). All relay-compress fusions, FUSE-into annotations, and per-anchor merges are documented in the annotated draft. No missing bone traces.

### DIALOGUE-VERBATIM
Verified all 12 cast-slug utterances against source dialogue files. Attribution-clause punctuation (period → comma at utterance split point) is consistently within the declared voice-transform-on-attribution-clauses carve-out. Utterance text is verbatim in all 12 cases. The 8 bare-speech walk-on bones (descriptive-noun speakers: the clerk @5, the second clerk @35/@37, the apothecary owner @36/@38, the stall-keeper @80/@82, the messenger @129) are rendered as silent observable action per the bone-faithfulness fence and the dialogue-coverage gate ACCEPT outcome from /and-facets; no quoted content was inserted for these speakers. No unmoored utterances.

### EXPOSITION-VERBATIM
Verified all 5 exposition entries:
- exposition:1 preamble: verbatim match, italic-preamble renders-as honored.
- exposition:2 clerk-gloss: "the clerk's work" → "his work" — pronoun substitution for in-context referent; within voice-transform scope.
- exposition:3 Red Keep em-dash: "the king's castle above the city" — verbatim in em-dash fold.
- exposition:4 overnight scene-bridge: verbatim match.
- exposition:5 maester scene-bridge: verbatim match.

### NO-INVENTION
All named entities verified graph-resident: taylor-hebert-flea-bottom (cast), oc-tanner-elder (cast), oc-broken-maester (cast), oc-tanner-father (cast). Walk-on descriptions (the clerk, the second clerk, the messenger, the keeper, the middleman) all graph-resident via proto-lines. Red Keep referenced via exposition:3 source citation loc-red-keep-outer-ring. No extra-graph character, location, prop, condition, or event introduced. Earth-Bet hard-fence: independent scan of rendered prose — CLEAN. Corroborated by render-log Phase 7 Earth-Bet hard-fence scan: CLEAN.

### CONTINUITY
Tense: first-person past throughout. No mid-paragraph tense shifts detected. Flashback-adjacent constructions ("the way it used to leave before the network went"; "older than any wall I had faced before") are grammatically correct past-perfect or past-habitual, not tense leakage. Contractions: present where expected ("I'd heard," "I'd held," "didn't reopen," "That's," "she's"). Person: first-person POV maintained; third-person descriptions are all insect-relay observations of other characters (graph-consistent POV construction). Displacement-clamp "The body" constructions at L44, L56, L107, L121, L123 are facet-licensed SHAPE patterns (mem:4, mem:8, mem:11, mem:12), not person violations. The single SIGNAL (find-001) is the "the interior" antecedent ambiguity at L97. Possessive register ("The breath held one beat past the close," L74) is annotated as narrator:21 (facet-licensed impersonal article per worm-tight pacing register) — not a fault.

### BLOCKING
Scene-E (dock-side alley): Taylor enters at @56/L45, wasps spread (@57/L46), Taylor speaks (@59/L48), cluster thins (@62/L50), Taylor exits at @64/L52, elder at threshold, coin exchange. Sequence internally consistent. Scene-K perimeter circuit: first alley (@149-@150/L115a) → south alley (@151-@152/L115b) → Fish Gate margin (@153/L115c) → south-wall colony (@155-@156/L117) → junction (@157/L118a) → eastern-quarter approach (@158-@160/L118b) → return to base (@161/L118c, L119). Ordering matches declared spec exactly. No blocking faults.

### SCENE-MAP-RESPECT
Verified all 11 scene boundary placements against scene-map-s01e03.md and annotated draft traces. All boundaries align: each scene opens at the declared first bone and the annotated trace block closes at the declared last bone. The clean draft uses blank-line paragraph breaks at all scene transitions (no formal `---` scene-break markers); this is expected stitcher-output state per URI-WRAP-V2 — the editor pass at Phase 3 is the stage that inserts scene-break markers into polish/<slug>.md. No scenes reordered or merged. Protected patterns intact: log-trio appears at @14-@16, @29-@31, @46-@48, @69-@71, @92-@94, @106-@108, @122-@124, @144-@146, @163-@165 per render-log Phase 6 buildup-preservation log. fauna-relay-spread at @18-@22 (scene-B) and @110-@114 (scene-H) intact.

### EARTH-BET-HARD-FENCE
Scanned all 81 lines of the clean draft for case-insensitive substrings: Khepri, Skitter, Brockton, Coil, Cauldron, Endbringer, shard, capes, parahuman, PRT. Zero hits. Corroborated by render-log Phase 7 independent scan.

---

## Routing summary for editor dispatch

- HARD count: 0
- graph-repair blocks: 0 (editor is NOT blocked)
- prose-surface items for editor: 0 required; find-001 advisory flag passed to editor
- acknowledge entries: 0

Editor receives: PASS-WITH-ONE-ADVISORY. find-001 (SIGNAL, CONTINUITY) is delivered as an advisory flag. Editor may act or decline within allowed-moves contract.
