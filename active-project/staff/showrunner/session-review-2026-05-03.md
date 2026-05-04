# Session Review Notes — 2026-05-03
# and-project output quality review + partial s01e01 shoot

## What was done
- Verified and-project (taylor-hebert-westeros) landed correctly
- Ran /and-shoot s01e01 as a diagnostic test — halted after 3 bullets
- Identified 6 systemic issues and applied fixes where possible

## Fixes applied this session

### 1. Passive-sense vibe gap (FIXED)
Taylor's vibes lacked a key encoding how the passive sense appears in prose.
Impersonators wrote "through the three beetles" (active directed) instead of ambient awareness.
Fix: added `passive-sense-texture` key to active-project/actors/taylor-hebert/vibes.md.
Future: and-project.md updated — power-mechanics vibe key requirement added to step 1c.

### 2. Walk-on NPC card gap (FIXED in command)
Census officer had on-stage lines but no card. Created manually during shoot setup.
Fix: and-shoot.md now has step A1b — walk-on card check before shoot begins.
Census-officer card lives at active-project/actors/census-officer/ — not yet in library.

### 3. Inventory carry-forward (FIXED in command)
No explicit rule enforcing item/wound persistence across bullets.
Fix: and-shoot.md updated with "Inventory carry-forward is absolute" rule.

### 4. Actor dir naming (FIXED in command)
taylor-hebert dir vs taylor-hebert-westeros card name mismatch caused coach path failures.
Fix: and-project.md now requires actor dirs named by card.name field (variant slug, not base slug).
Current active-project still has the mismatch — not worth fixing mid-shoot.

### 5. Duplicate condition cards (FIXED)
cond-reincarnation-rules and cond-reincarnation-mechanics both in library.
margit tombstoned cond-reincarnation-rules → cond-reincarnation-mechanics.
Content from rules card merged into mechanics card before tombstone.

### 6. Coach tuning harness (CREATED)
staff/coach/tuning/harness-pulp-enthusiast.md — three failure patterns documented with what worked.

## Open issue: pulp-enthusiast vs. slow-open structure

NOT fixed. Requires product decision.

Pattern: pulp-enthusiast rejects every line in a setup/sickroom scene (pre-inciting-incident).
All three rejection reasons ("slice-of-life filler", "offscreen threat", "interior inventory") fire on legitimate dramatic setup.
Two paths:
  A. Recalibrate pulp-enthusiast card — add exception for legitimate pre-inciting-incident setup scenes.
  B. Restructure episode plans so Scene 1 opens with an active attempt, not atmospheric setup.

Current s01e01 episode plan starts with 6 sickroom bullets before any external action. That structure
will produce NEEDS_EDIT on ~4 of those 6 bullets under the current pulp-enthusiast card.

## Shoot state at session end
- s01e01 status: planned (not marked shot — shoot was halted early)
- show.md has 3 bullets written (b1 clean, b2+b3 NEEDS_EDIT)
- Episode plan accepted, all A-phase setup complete
- Ready to resume shoot OR restart with improvements applied

## Recommended next session order
1. Decide: fix pulp-enthusiast card vs. restructure e01 episode plan
2. If restructuring: have screen-writer rewrite Scene 1 with earlier action entry
3. Resume shoot from bullet 4 OR restart s01e01 clean
