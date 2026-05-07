verdict: CONTINUITY-OK

audit:
  scope: episode
  target: s01e01
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: flag
      what: line 25 ("the sept doors") vs. line 40 ("the sept door") and location card loc-harrenhal-sept-environs ("Entry from the west through the worn door" — singular)
      why: reference inconsistency between lines; non-load-bearing but creates an editorial continuity note; editor may want to normalize
      criteria: n/a (flag — no fixer dispatch required)

reachability: PASS — chunk-end state (Taylor named, listed, double-stroke flagged, window closed) is fully reachable from chunk-start through surviving beats; goal delivered at lines 45–46; change delivered at line 46.
state: PASS — letter chain clean (lines 27–31, 55); ledger chain clean (lines 11–46); no actor in impossible location; all time-skips (IDs 7, 16, 26, 49, 54) are compatible with surrounding location-state.
reference: PASS — all five cast slugs resolve to episode-plan actors; all location references resolve to loc-harrenhal-sept-environs (active warehouse); collective noun "the wards" consistent throughout; "the sept doors" (line 25) flagged above as singular/plural mismatch.
pov: PASS — no perception-verb leak onto narrator; all non-POV lines show observable action only; environment-as-subject idiom ("the yard holds") does not constitute a leak.
laws: PASS — no law violations introduced or re-introduced; no fauna-control use present; no parahuman infrastructure; no Gold Morning reference.
