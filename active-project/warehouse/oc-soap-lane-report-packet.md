---
name: oc-soap-lane-report-packet
class: prop
scope: library
world: planetos
portability: portable
origin: authored
quality: full
references:
  - oc-soap-rendering-lane
  - taylor-hebert-kl-122ac
---

# The Soap-Lane Report Packet — Nighttime-Visitor Intelligence Report, Hook Precinct

## Physical Description

A sealed paper packet, folded and closed at the edge with a wax press — not an elaborate seal, a working-closure wax touch that indicates the packet has not been opened since the contact folded it. The covering cloth is coarse linen, same weight as the general covering-sheet stock used across Taylor's contact network. The packet is small enough to pass hand-to-hand in a single motion at the cross-lane mouth.

Inside (as of b01c11 close): two sheets. The outer sheet is the nighttime-visitor observation record as the soap-lane contact assembled it — entries in a standard Hook-observation format, the precinct pattern for the reporting period. The inner content, added by Taylor at the feed-station (@20): the precinct-pattern sourcing annotation, written in the same column margin, naming the routing path without naming the contact.

After Taylor's seal at @21: the covering cloth has been re-pressed. The wax closure is Taylor's, not the contact's — a distinct working-closure that marks the packet as having passed through the feed-station annotation step. The packet is now route-ready: sealed for Jarvis-channel routing or lateral pass.

## Affordances / Uses

- **Intelligence routing.** The packet carries a complete observation record (nighttime-visitor pattern, Hook precinct, reporting period) plus the precinct-pattern sourcing annotation that makes it actionable for the recipient. It is route-ready for Jarvis-channel onward routing as of b01c11 @21.
- **Sourcing-trace prevention.** The sourcing annotation names the routing path without identifying the soap-lane contact by person. The contact does not appear in any field; the annotation is a routing label, not an attribution. This is the same substrate-split discipline applied to the wool-dyer withhold earlier in the chapter.
- **Persistent inter-chapter prop.** The packet was sealed at b01c11 @21 and NOT dispatched during b01c11 — it remains in Taylor's possession at chapter-close, sitting in the feed-station record rather than the outbound channel. It carries forward into b01c12 as a route-committed but not-yet-dispatched intelligence item.
- **Physical accountability anchor.** As a sealed-and-route-annotated packet, it represents a committed routing decision. Its presence in b01c12 without dispatch would be a visible anomaly in the accounting-in-motion discipline.

## Sensory Hooks

- Coarse linen covering cloth — the slightly rough texture of the covering against fingers, distinct from the smoother packet-sheet stock.
- Weight of two sheets inside a linen wrap — not heavy; the weight of a working document, not a letter.
- The wax closure under thumb: a small raised point of pressed wax at the fold-edge, cool and firm when set. Taylor's closure is identifiable by its flat-press shape (no maker's seal impression).
- The alkaline-faint note the contact's handling may have transferred from the soap-rendering lane — very faint, possibly below detection threshold, but present as a trace on the covering cloth if handled in proximity to the rendering smell.

## Portability

Portable. At chapter-close (b01c11 @27), the packet is at the feed-station — not dispatched, not carried on Taylor's person. It is a staged outbound item in the feed-station's working stack, not yet in the channel.

## Carry State

- **Concealment:** Fold-closed with a working-closure wax press. Not hidden — sits in the outbound work stack. The wax closure signals "route-ready" to any actor familiar with the channel discipline.
- **Weight:** Negligible on-person when carried. Easily carried inside Taylor's pack or held in-hand during routing dispatch.
- **Noise:** Silent. The linen cover absorbs paper-on-paper sound; the packet produces no audible signal when moved.

## Functional State

Tracked in runtime state-updates per chapter. As of b01c11 @21 close:

- `seal_state`: `route-ready` (Taylor's wax press closed; packet annotated and sealed for dispatch)
- `content_state`: `complete` (nighttime-visitor observation record + precinct-pattern sourcing annotation; two sheets)
- `location`: `feed-station outbound stack` (not dispatched as of b01c11 @27)
- `dispatch_state`: `pending` — route committed, channel not yet activated

**b01c12 carry-forward:** The packet must either dispatch via Jarvis-channel (@early) or be held with an explicit accounting reason. A sealed route-ready packet sitting in the outbound stack past the next morning circuit without dispatch would register as an anomaly in Taylor's accounting-in-motion discipline and should generate a bone or state-update noting the hold-reason or the dispatch event.
