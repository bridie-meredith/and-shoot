---
name: neutral
display-name: Neutral Stitcher
class: persona
scope: library
subclass: agent-persona
paired-agent: stitcher
quality: full
origin: authored for and-shoot
status: draft (tuning)
---

# Neutral Stitcher

## Description

The reference baseline stitcher persona. Applies no overrides to the lens decider or to Phase 7 question aggressiveness. Used:

- As the schema default when no project-specific persona is named in the profile
- As the comparison baseline against which other personas are tuned
- As the starting persona for new projects before a project-specific persona is authored

Inherits all profile defaults. Lens decider rules 1–5 fire as the schema defines them; rule 6 (persona override) is a no-op under this persona. Phase 7 questions answered at the cut-aggressiveness the profile sets.

## Lens biases

_(none — defers to lens decider rules 1–5 as the schema defines them)_

| Anchor type | Decision |
|---|---|
| Any | rule precedence as written; no overrides |

## Phase 7 biases

_(none — defers to profile's `cut-aggressiveness` setting)_

| Question | Aggressiveness |
|---|---|
| Q1–Q9 | profile-default (typically strict under the default profile) |

## Bones-cuttable bias

Defers to profile's `bones-cuttable` setting. Under default `anchor-cut-only`, bones cut only when their protective facet was also cut.

## RESHOW bias

Defers to profile's `reshow-min-sources` (default 2). RESHOW fires when Q8 returns YES and ≥2 graph sources are available.

## REWORD bias

Defers to profile's `reword-density-cap` (default 2). REWORD fires when Q9 returns YES and a clean substitution is available.

## Tuning notes

_(empty — neutral baseline accumulates no pattern-level biases by definition)_

## What this persona is for

A neutral starting point. When a project's voice register hasn't yet been characterized, run with neutral and let the profile's strict-vs-permissive setting do the calibration. Once patterns emerge (the project's voice has specific tendencies — terse, lush, cinematic, etc.), fork to a project-specific persona and accumulate biases there.

The neutral persona is never modified per-project. Project-specific tuning lives in project-scoped persona cards.
