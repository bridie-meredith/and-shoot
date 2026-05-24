---
name: oc-taylor-pack
class: prop
scope: library
world: planetos
portability: portable
origin: authored
quality: full
---

# Taylor's Carried Pack

## Physical Description

A worn canvas satchel, mid-weight, closed with a simple flap and a leather toggle. Shaped by use — the flap sits flat from repeated folding, the strap has stretched to the length of Taylor's arm. Undyed, the color of whatever city it has been set down in too many times. Flea Bottom dirt has worked into the seams.

## Affordances / Uses

- **Currency storage.** The pack is where Taylor keeps her copper-star reserve: the transaction float that pays for building-keeper access, market purchases, and low-denomination exchange.
- **Tool storage.** Carries the working-corner toolkit: an awl, a length of waxed thread, a folding knife with a cracked handle, and a small bone needle-case (pre-loaded needles, Flea Bottom quality).
- **Mending supply.** A rolled bundle of patch-cloth and a spare spool of coarse thread. Functional, not decorative.
- **Chapter-to-chapter inventory anchor.** The pack is the single persistent prop tracking Taylor's material position across scenes. Its contents reflect the chapter's resource state; depletion or addition of items is recorded as pack-state changes in state-updates.

## Sensory Hooks

- Canvas: the muffled thud of the pack setting down on stone.
- The strap creak when lifted from ground to shoulder.
- Copper smell from the coin pocket when the flap opens.
- Weight that reads as loaded-not-heavy — a working-day load, not a journey load.

## Portability

Portable. Carried on Taylor's person or set down at the working corner during stationary beats. Pack position is tracked in state-updates (carried vs. set-at-working-corner vs. stored).

## Carry State

- **Concealment:** none — the satchel is visible, worn across one shoulder or set at foot level; not hidden.
- **Weight:** mid-weight when loaded (tools + coin + patch-cloth). Taylor carries it without posture change; the weight is habitual.
- **Noise:** low — the canvas doesn't rattle; the coin pocket is cloth-padded. Boot-step-adjacent movement produces minimal sound signature.

## Functional State

Tracked in runtime state-updates per chapter. Active states:
- `position`: `carried` | `set-at-working-corner` | `stored-off-scene`
- `coin-reserve`: tracked in showrunner memory (currency-state axis) when depletion events occur
- `tool-integrity`: `intact` until a specific loss or damage event fires

Starting state (b01c01 @7): `position: set-at-working-corner` (Taylor drops the pack at the start of the scene-B working sequence; it remains there through @20).
