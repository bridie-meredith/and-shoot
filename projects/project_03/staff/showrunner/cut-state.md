# cut-state — 2026-05-05

## Position
pipeline_phase: mid-shoot
active_season: s01
active_episode: s01e06
episode_status: planned

## In-progress files
- episode-plan.md: present — 71 bullets, accepted by audience+dramatist on attempt 1
- episode-plan-log.md: present — attempt 1 verdicts logged
- show.md: present — 12 lines (header + 7 paragraphs; B1–B6 complete; SCENE 2 just opened)
- shoot-log.md: present — bullet 6 of 71 complete (B1 clean, B2 retried, B3 clean, B4 retried, B5 retried, B6 retried)
- wrap-structure-log.md: not present
- wrap-audience-log.md: not present
- staff/auditor/s01e06-wrap-audit.md: not present
- polish/s01e06.md: not present

## Resume instructions
Next: review show.md to find last completed bullet, then either:
  (a) continue: re-run /and-shoot — it will detect show.md has content and stop; delete show.md + shoot-log.md manually to restart from scratch
  (b) abandon and restart: delete active-project/theater/show.md and active-project/theater/shoot-log.md, then re-run /and-shoot

Note on this cut specifically: Phase A (planning) is fully complete and reusable — episode-plan.md, episode-plan-log.md, vibes deltas, studio state, and audience STMs are all in place. To resume the shoot at B7, do NOT delete show.md / shoot-log.md / episode-plan.md. Resume by dispatching coach/impersonator/audience for bullet 7 directly. The skill's "show.md must be header-only" guard would need to be bypassed manually.

## Notes for resume
- SCENE 1 of s01e06 fully shot (B1–B5). SCENE 2 is OPEN — B6 just delivered Taylor at the door of Rowan's writing alcove with the road-clock instrument going information-dark behind two walls of stone.
- B7 is Rowan's first line of the entire show file: "septon-rowan: sets his pen down and does not pick it up." Coach prompt was being prepared and was interrupted by /and-cut.
- POV CONVENTION CONFIRMED THIS SESSION: recipient impersonator writes in their own first-person voice; POV shifts per bullet to whichever actor's bullet it is. See s01e05 archive show.md line 30 for Rowan's first-person voice sample (`"She is." Said it at the cadence the maester had asked it in...`). B7 will be the first POV-shift in s01e06 — Taylor's first-person POV held continuously through B1–B6; B7 shifts to Rowan first-person.
- Rowan tier: absent from card → routes to opus per /and-shoot A3 routing rule.
- Studio state.md and stm.md are current as of B6 (SCENE 2 OPEN — Rowan's writing alcove off the nave; small windowless room; first horizon-grey outside; Rowan on stool at small table; writing case + half-drafted letter on table; Taylor at door interior side, back against inside of door, no movement; passive feed re-indexed to room-only; road-clock outside the perimeter).
- Taylor's actor state.md is **stale** at B5 — B6 update was deferred to next bullet boundary and not yet written. On resume, before B7 dispatch, append a B6 update to taylor-hebert-westeros/state.md noting: position at door of Rowan's writing alcove (not main door); back against inside of room door; no movement; passive feed scope = room-only (Rowan at five paces, mouse at south-corner seam, nave-cold beyond the room walls); road/bird channel acknowledged as outside-the-feed-perimeter; baseline cost (nil); inventory unchanged; psychological note: information-dark on the road-clock is the carry-forward pressure entering scene 2.
- Walk-on card check (A1b) was completed during episode-start phase; no card gaps for SCENE 2 actors (Rowan is established).
- B7 must deliver a board event paired with the pen-set-down (CRITICAL pulp-enthusiast carry-forward demand from B6 close). Strongest angle: the pen going down is Rowan's surrender of his last instrument — the half-drafted motherhouse letter cannot reach in time, mirroring Taylor's road-clock loss in B6. Two characters in a sealed room, both having just lost the channels they held to the outside.
- Hard fence for B7: Rowan does NOT speak (B8 is Taylor's next line); Rowan does NOT look up at Taylor (his registration of her is in the gesture's deliberate non-engagement); pen is still inked (the "pen is dry" detail is reserved for a later studio bullet at episode-plan line 45).

## Audience persona-state at cut
- pulp-enthusiast: strict any-reject-rejects rule still in force. Three retries triggered by this persona this episode (B2, B4, B5, B6 — actually four). Pattern: rejects transit beats and re-descriptions; demands board-worsening per beat. Patience for held-still beats explicitly set to one beat at B6 close — B7 must deliver a clock event before/after the held-still pen-set-down or patience resets to zero.
- dark-fantasy-reader: accepting on every line so far including B6 attempt 2; voice and limit-of-power working; bleak Planetos register clean.
- worm-canon-pedant: accepting on every line so far including B6 attempt 2; passive/active distinction, cost-window logic, fauna-channel mechanics, scope-ends-at-stone-walls all clean.

## Vibe-cloud state
- Episode vibe-cloud derived during A2; active throughout shoot. Both series + season + episode vibes loaded for each impersonator dispatch.
- Active vibe-keys most live at cut: passive-sense-texture, cost-accounting (now expressed as INFORMATION-cost not energy-cost), holding-still / control-as-evidence, the-function-named (anticipated to escalate when Plumm names her function in scenes 4–6), rowan-out-of-instruments (newly-emerged at B6, anticipated to crystallize in B7).

## Pipeline-procedure work also done this session (out-of-band)
- Recovered s01e01 and s01e03 theater archives from git history into theater/s01e01-archive/ and theater/s01e03-archive/.
- Hardened /and-shoot Phase 1 with archive integrity check.
- Added /and-shoot Phase 0: auto skip-wrap of previous shot episode.
- Updated /and-wrap to support bulk modes (--all-shot, range) and resolve source from archive dir or live theater dir per target.
- CLAUDE.md primary pattern updated to reflect shoot-shoot-shoot default.
- Two commits on local main ahead of origin: rebased over remote s01e06 B5 work (cleanly).
- Saved feedback memory: default flow is shoot-shoot-shoot; do not nudge user toward wrap mid-stretch.

Skip-wrap context: s01e05 was marked shot on main but never wrapped. Its theater files were archived into active-project/theater/s01e05-archive/ at the prior session's start to clear the way for s01e06. Polish/s01e05.md was never produced. s01e01 and s01e03 archives also recovered this session — all five completed episodes (s01e01–s01e05) now have intact archive directories awaiting bulk wrap.
