# actor_baselines draft — /and-substance series add actor_baselines (Step 4d)
# Generated: 2026-05-24
# Cells: 11 actors × 12 axes = 132
# User: edit YAML in place. When ready, type `accept` to persist to series.substance.actor_baselines[].

actor_baselines:

  # === taylor-hebert-kl-122ac (protagonist; 12 axes) ===
  # All 9 protagonist-perspective axes: moves, lifted-from-state-axes.
  # social_tether-antag, position-world, political_register-world: not-applicable — she is object or instrument, not carrier.

  - actor: taylor-hebert-kl-122ac
    axis: moral_framework
    applicability: moves
    start_rank: 2
    end_rank: 8
    source: lifted-from-state-axes
    notes: "prohibition collapse; matches state_axes[].{start_rank,end_rank}; monotonic"

  - actor: taylor-hebert-kl-122ac
    axis: capability
    applicability: moves
    start_rank: 2
    end_rank: 8
    source: lifted-from-state-axes
    notes: "insect-network deployment scale rises; matches state_axes[].{start_rank,end_rank}; monotonic"

  - actor: taylor-hebert-kl-122ac
    axis: position-prot-rise
    applicability: moves
    start_rank: 1
    end_rank: 7
    source: lifted-from-state-axes
    notes: "rise phase only; peaks ~7 at d07; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: position-prot-collapse
    applicability: moves
    start_rank: 7
    end_rank: 1
    source: lifted-from-state-axes
    notes: "collapse phase only; starts from d10 peak; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: relational_anchor_status
    applicability: moves
    start_rank: 1
    end_rank: 9
    source: lifted-from-state-axes
    notes: "un-priced anchor pressure rises; HIGH=WORST; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: moral_legibility_to_self
    applicability: moves
    start_rank: 4
    end_rank: 8
    source: lifted-from-state-axes
    notes: "non-linear net-positive; recognition-too-late; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: political_register-prot
    applicability: moves
    start_rank: 1
    end_rank: 9
    source: lifted-from-state-axes
    notes: "contempt-accumulation; monotonic; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: social_tether-prot-rise
    applicability: moves
    start_rank: 1
    end_rank: 8
    source: lifted-from-state-axes
    notes: "rise phase only; peaks ~8 at d07; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: social_tether-prot-collapse
    applicability: moves
    start_rank: 8
    end_rank: 1
    source: lifted-from-state-axes
    notes: "collapse phase only; starts from d10 peak; matches state_axes[].{start_rank,end_rank}"

  - actor: taylor-hebert-kl-122ac
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage OVER Taylor; Taylor is the object the leverage is measured against, not a carrier of the position"

  - actor: taylor-hebert-kl-122ac
    axis: position-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "Taylor is the instrument of Green-faction consolidation, not a position-holder in the faction; axis tracks institutional consolidation, not the instrument's standing"

  - actor: taylor-hebert-kl-122ac
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position secured; Taylor is the mechanism, not a faction member or position-occupant"


  # === otto-hightower (antagonist; 12 axes) ===
  # Primary carriers: social_tether-antag (lifted), position-world (lifted), political_register-world (lifted).
  # Taylor's interior axes (moral_framework, capability, relational_anchor_status, moral_legibility_to_self,
  # political_register-prot): not-applicable — Taylor's interior accounting; Otto is proximate cause, not carrier.
  # Taylor's position/tether axes: not-applicable — track Taylor's standing, not Otto's.

  - actor: otto-hightower
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior anti-instrumentalization accounting; Otto is the proximate cause of each breach but does not carry the position"

  - actor: otto-hightower
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment scope; Otto's own intelligence capability is off-axis and off-arc in this framework"

  - actor: otto-hightower
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Otto is the position-architect but does not occupy the position on this axis"

  - actor: otto-hightower
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Otto removes Taylor at d14 but does not himself lose position — he is the agent of collapse, not the carrier"

  - actor: otto-hightower
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor pressure; Otto is the structural threat enabling the cost but not a carrier of the relational position"

  - actor: otto-hightower
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior self-accounting; Otto has no self-accounting gap in this framework — his misread of Taylor is the gap but it is not this axis"

  - actor: otto-hightower
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward Westerosi elite; Otto IS the elite architecture Taylor is developing contempt toward; he does not carry the register-toward position"

  - actor: otto-hightower
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's relational and institutional tether in KL; Otto is the architect of that tether but does not occupy a position on the tether axis itself"

  - actor: otto-hightower
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Otto dissolves the arrangement at d14 but does not himself lose tether — agent of collapse, not carrier"

  - actor: otto-hightower
    axis: social_tether-antag
    applicability: moves
    start_rank: 1
    end_rank: 9
    source: lifted-from-state-axes
    notes: "primary carrier; Otto's leverage over Taylor rises monotonically as network embeds; matches state_axes[].{start_rank,end_rank}"

  - actor: otto-hightower
    axis: position-world
    applicability: moves
    start_rank: 5
    end_rank: 9
    source: lifted-from-state-axes
    notes: "consolidation architect; his operational moves ARE the Green-faction institutional rise; matches state_axes[].{start_rank,end_rank}"

  - actor: otto-hightower
    axis: political_register-world
    applicability: moves
    start_rank: 5
    end_rank: 9
    source: lifted-from-state-axes
    notes: "Green-faction succession position secured through his intelligence architecture; primary driver of world-axis rise; matches state_axes[].{start_rank,end_rank}"


  # === wren-stitch-maker-flea-bottom-ward (cost-bearer; 12 axes) ===
  # Primary carrier: relational_anchor_status (lifted; HIGH=WORST — the axis IS the cost-bearer's vulnerability).
  # All other axes: not-applicable with role-specific rationale.

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior anti-instrumentalization accounting; Wren is the subject of the omission, not a carrier of the framework position"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Wren has no capability arc in this framework"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Wren has no court position and no standing arc — she is a Flea Bottom ward throughout"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Wren's d14 death is a consequence of the collapse, not an instance of it on this axis"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: relational_anchor_status
    applicability: moves
    start_rank: 1
    end_rank: 9
    source: lifted-from-state-axes
    notes: "primary carrier; axis IS the cost-bearer's vulnerability trajectory; HIGH=WORST; her exclusion from the ledger is structurally causal to her death; matches state_axes[].{start_rank,end_rank}"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting accuracy; Wren is the subject of Taylor's accounting gap, not a self-accounting carrier"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward Westerosi elite; Wren is smallfolk with no court-register arc and no investment in the succession axis"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's KL institutional tether; Wren is entirely Flea Bottom-local and is not a component of Taylor's court-adjacent tether architecture"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Wren's death is a cost paid at collapse, not an axis position she carries"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor; Wren is the latent lever Otto identifies at d11, not a carrier of the leverage position"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: position-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction institutional consolidation; Wren is a Flea Bottom ward with no participation in the faction machinery"

  - actor: wren-stitch-maker-flea-bottom-ward
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position; Wren has no participation in the succession machinery"


  # === sera-hightower-kl-122ac (protect-target; 12 axes) ===
  # No axis fully parallel to Wren's relational_anchor_status — Sera is the priced-and-protected target, not the un-priced anchor.
  # position-world / political_register-world: static — she is a beneficiary, not an agent.
  # All protagonist-interior, Otto-leverage, and Taylor-tether axes: not-applicable.

  - actor: sera-hightower-kl-122ac
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior anti-instrumentalization accounting; Sera is the object of the protection arrangement, not an accounting carrier"

  - actor: sera-hightower-kl-122ac
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Sera has no capability arc in this framework"

  - actor: sera-hightower-kl-122ac
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Sera's court position is held by Otto's architecture, not a parallel arc on this axis"

  - actor: sera-hightower-kl-122ac
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Sera's position is sustained (the protection succeeds as stated); her arc does not collapse on this axis"

  - actor: sera-hightower-kl-122ac
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor; Sera is the priced-and-protected target — opposite role on the same machinery; the un-priced anchor is Wren"

  - actor: sera-hightower-kl-122ac
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Sera has no self-accounting arc visible in this project — she does not know Taylor exists"

  - actor: sera-hightower-kl-122ac
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward the elite; Sera IS a court-tier ward — she does not carry a register-toward-elite position"

  - actor: sera-hightower-kl-122ac
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's KL tether; Sera's court placement is what the tether is built to protect, not a parallel tether position"

  - actor: sera-hightower-kl-122ac
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Sera's position is sustained through d14; she is not a tether-collapse carrier"

  - actor: sera-hightower-kl-122ac
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor; Sera's legitimacy question IS the lever, but she is the object of the lever, not a leverage-position carrier"

  - actor: sera-hightower-kl-122ac
    axis: position-world
    applicability: static
    start_rank: 6
    end_rank: 6
    source: inferred-from-role-card
    notes: "court-tier ward in Alicent's household; her position is held by Otto's architecture throughout and does not independently move; beneficiary of consolidation, not its agent; static at mid-high rank reflecting protected court standing"

  - actor: sera-hightower-kl-122ac
    axis: political_register-world
    applicability: static
    start_rank: 6
    end_rank: 6
    source: inferred-from-role-card
    notes: "her legitimacy question is the lever Taylor is protecting against; her succession-adjacent standing is held steady by the protection (that is the arrangement's purpose); static rather than moves — she is a beneficiary, not a faction agent"


  # === aemond-targaryen-122ac (world-embodiment:opposite-number; 12 axes) ===
  # Walk-on at d10-d14; Otto-directed; axis-movement-per-appearance hard fence.
  # position-world: static (IS elite; Vhagar-armed enforcement; position not a rise-trajectory for him).
  # Most axes: not-applicable with "IS elite" / "instrument-not-carrier" rationale.

  - actor: aemond-targaryen-122ac
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior accounting; Aemond is the embodied consequence of Otto's proposals, not a carrier of the anti-instrumentalization framework"

  - actor: aemond-targaryen-122ac
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Aemond's capability (Vhagar bond) is not this axis"

  - actor: aemond-targaryen-122ac
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Aemond's court position is birthright, not a rise trajectory on this axis"

  - actor: aemond-targaryen-122ac
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Aemond does not lose position at d14 — he is the agent of Taylor's collapse, not a collapse carrier"

  - actor: aemond-targaryen-122ac
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor; Aemond has no un-priced relational anchor function in this framework"

  - actor: aemond-targaryen-122ac
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Aemond is 12 and Otto-directed; he does not carry a moral self-accounting arc in this project"

  - actor: aemond-targaryen-122ac
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance TOWARD the Westerosi elite; Aemond IS elite (Targaryen prince, Vhagar rider) — he does not carry a register-toward-elite position"

  - actor: aemond-targaryen-122ac
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's relational tether in KL; Aemond's dynastic institutional ties are birthright, not a tether-rise arc on this axis"

  - actor: aemond-targaryen-122ac
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Aemond does not lose tether at d14 — he is the instrument of Taylor's severance"

  - actor: aemond-targaryen-122ac
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor specifically; Aemond is a coercive instrument within Otto's apparatus, not a leverage-over-Taylor carrier in his own right"

  - actor: aemond-targaryen-122ac
    axis: position-world
    applicability: static
    start_rank: 8
    end_rank: 8
    source: inferred-from-role-card
    notes: "axis tracks Green-faction institutional consolidation; Aemond IS the Green faction's coercive enforcement instrument — already at high institutional rank (Vhagar, Targaryen prince); his position does not rise on this axis because he starts already at the coercive ceiling; static at 8"

  - actor: aemond-targaryen-122ac
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position secured; Aemond IS the Green faction's coercive arm — he does not carry a register-toward-Green position; the axis tracks the institutional achievement, not the instrument embodying it"


  # === alicent-hightower-122ac (world-embodiment:green-faction-institution; 12 axes) ===
  # Primary carriers: position-world and political_register-world (lifted from state_axes).
  # IS elite — political_register-prot not-applicable.
  # All protagonist-interior and Taylor-tether axes: not-applicable.

  - actor: alicent-hightower-122ac
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior anti-instrumentalization accounting; Alicent's own moral framework is the Faith-register but is not this axis"

  - actor: alicent-hightower-122ac
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Alicent has no capability arc in this framework"

  - actor: alicent-hightower-122ac
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Alicent's court position is Queen Consort, birthright-adjacent — not a rise arc on this axis"

  - actor: alicent-hightower-122ac
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Alicent does not collapse at d14 — the Green faction's consolidation holds through the project end"

  - actor: alicent-hightower-122ac
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced relational anchor; Alicent has no function in this framework's anchor machinery"

  - actor: alicent-hightower-122ac
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Alicent is observable through compound eyes only; her self-accounting is off-axis"

  - actor: alicent-hightower-122ac
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance TOWARD the Westerosi elite; Alicent IS the institutional face of the Westerosi elite — she does not carry a register-toward position"

  - actor: alicent-hightower-122ac
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's KL tether; Alicent's household IS the institution Taylor is tethering to, not a parallel tether-position carrier"

  - actor: alicent-hightower-122ac
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Alicent does not lose tether — the apparatus she heads survives Taylor's expulsion"

  - actor: alicent-hightower-122ac
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor specifically; Alicent is the household-anchor of the Green faction architecture but not a leverage-over-Taylor carrier"

  - actor: alicent-hightower-122ac
    axis: position-world
    applicability: moves
    start_rank: 5
    end_rank: 9
    source: lifted-from-state-axes
    notes: "primary carrier alongside Otto; the consolidation is performed in her name and through her household; matches state_axes[].{start_rank,end_rank}"

  - actor: alicent-hightower-122ac
    axis: political_register-world
    applicability: moves
    start_rank: 5
    end_rank: 9
    source: lifted-from-state-axes
    notes: "primary carrier; institutional Green-faction face; the succession position Taylor despises is Alicent's position made concrete; matches state_axes[].{start_rank,end_rank}"


  # === criston-cole-122ac (world-embodiment:faction-violence-instrument; 12 axes) ===
  # Observable as operational aftermath only; not a position-holder on any axis.
  # All axes: not-applicable — enforcement arm, not a position-carrier.

  - actor: criston-cole-122ac
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "operational-output observable only; his moral framework is fully subsumed into institutional identity and is not an arc in this project"

  - actor: criston-cole-122ac
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Criston's enforcement capability is not this axis"

  - actor: criston-cole-122ac
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Criston is the enforcement arm of the institution, not a court-position-rise carrier"

  - actor: criston-cole-122ac
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Criston enacts the Green faction's enforcement at d14 but does not himself collapse"

  - actor: criston-cole-122ac
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor; Criston has no relational-anchor function; cast_roster note flags him as relational_anchor_status indirect but this refers to his operations threatening Wren's street-safety, not a position he carries"

  - actor: criston-cole-122ac
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Criston's self-accounting has been fully converted to institutional identity; he carries no moral-legibility arc visible in this project"

  - actor: criston-cole-122ac
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance TOWARD the elite; Criston IS the enforcement arm of the elite institution; he does not carry a register-toward position"

  - actor: criston-cole-122ac
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's KL tether; Criston's Kingsguard institutional position is not a tether-rise arc"

  - actor: criston-cole-122ac
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Criston executes enforcement at d14 but does not lose his own tether"

  - actor: criston-cole-122ac
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor; Criston is three tiers below Otto in practice and is not a leverage-position carrier"

  - actor: criston-cole-122ac
    axis: position-world
    applicability: static
    start_rank: 8
    end_rank: 8
    source: inferred-from-role-card
    notes: "Kingsguard Lord Commander; he enacts Green-faction consolidation as operational output but does not himself rise in position-world terms; his standing is stable at a high enforcement rank throughout the project; static"

  - actor: criston-cole-122ac
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position secured; Criston is the enforcement instrument that makes consolidation operative, not a succession-position carrier; he enacts, he does not hold"


  # === rhaenyra-targaryen-122ac (world-embodiment:black-faction-claimant; 12 axes) ===
  # position-world and political_register-world: moves INVERSE — as Green rises, Rhaenyra's claimant position is foreclosed.
  # She is not on the Green-faction axis; she is the axis's opposing claimant.
  # JUDGMENT CALL: using moves with inverted direction (high → low) to represent foreclosure rather than not-applicable,
  # because her active succession agenda makes her foreclosure a live on-page irony, not mere background.
  # All protagonist-interior and Taylor-tether axes: not-applicable.

  - actor: rhaenyra-targaryen-122ac
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior accounting; Rhaenyra does not know Taylor exists and carries no position on this axis"

  - actor: rhaenyra-targaryen-122ac
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Rhaenyra has no capability arc in this framework"

  - actor: rhaenyra-targaryen-122ac
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Rhaenyra's position is at Dragonstone — a distinct standing arc not tracked on this axis"

  - actor: rhaenyra-targaryen-122ac
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Rhaenyra's claimant foreclosure is tracked under position-world (inverted) — not this axis"

  - actor: rhaenyra-targaryen-122ac
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor; Rhaenyra has no function in the anchor machinery"

  - actor: rhaenyra-targaryen-122ac
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Rhaenyra has no self-accounting arc visible to Taylor's project scope"

  - actor: rhaenyra-targaryen-122ac
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward the elite; Rhaenyra IS the claimant — she does not carry a register-toward-elite position"

  - actor: rhaenyra-targaryen-122ac
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's KL tether; Rhaenyra is at Dragonstone with no KL-tether arc on this axis"

  - actor: rhaenyra-targaryen-122ac
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Rhaenyra's faction position erodes through a distinct mechanism not captured here"

  - actor: rhaenyra-targaryen-122ac
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor; Rhaenyra has no function in the Otto–Taylor leverage machinery"

  - actor: rhaenyra-targaryen-122ac
    axis: position-world
    applicability: moves
    start_rank: 7
    end_rank: 2
    source: inferred-from-role-card
    notes: "INVERTED CARRIER: axis tracks Green-faction consolidation rising (5→9); Rhaenyra's claimant position is the inverse — live claim at story-open (rank 7: heir named, Viserys holding the question), foreclosed to near-structural-loss by d14 (rank 2: Green apparatus locked, Dragonstone position isolated); road-not-taken irony requires her foreclosure to be tracked, not left as background"

  - actor: rhaenyra-targaryen-122ac
    axis: political_register-world
    applicability: moves
    start_rank: 7
    end_rank: 2
    source: inferred-from-role-card
    notes: "INVERTED CARRIER: axis tracks Green succession position secured (5→9); Rhaenyra's succession register is the opposing pole — viable claim at story-open, foreclosed through d14 as Green apparatus locks the council; her active Dragonstone agenda makes this a live irony, not passive background"


  # === oswyn-mudway-flea-bottom-elder (supporting:Flea-Bottom-ward-network-anchor; 12 axes) ===
  # No axis primary carrier. Acts 1-2 tapering presence.
  # social_tether-prot-rise: static (substrate Taylor builds on, not himself an arc).
  # All other axes: not-applicable.

  - actor: oswyn-mudway-flea-bottom-elder
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior accounting; Oswyn is a ward-network substrate who does not know he is inside a coverage architecture; no position on this axis"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Oswyn's ward-knowledge is ground-layer substrate, not this axis"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Oswyn has no court position and no standing arc — fixture of Flea Bottom only"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Oswyn does not collapse — he is a Flea Bottom fixture throughout"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor (Wren); Oswyn is a ground-layer contact, not the un-priced relational anchor"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Oswyn has no moral-legibility arc — he does not know he is inside the architecture"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward the elite; Oswyn has no court register — his world is ward-scale, not succession-scale"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: social_tether-prot-rise
    applicability: static
    start_rank: 3
    end_rank: 3
    source: inferred-from-role-card
    notes: "ward-network anchor that constitutes the ground layer of Taylor's social tether; his own standing does not rise — he is stable-fixture throughout; static at 3 (ground-level embedded; not patron-adjacent); his position is the substrate, Taylor's tether moves on top of it"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Oswyn remains in Flea Bottom and does not experience the tether collapse — the collapse is Taylor's, not his"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor; Oswyn is entirely outside the patron-lever machinery"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: position-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction institutional consolidation; Oswyn has no participation in the faction machinery — ward-network substrate at Flea Bottom scale"

  - actor: oswyn-mudway-flea-bottom-elder
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position; Oswyn has no succession-scale awareness or function"


  # === jarvis-coin-kl-courier (supporting:Otto-courier-adjacent; 12 axes) ===
  # Structural vector for social_tether-antag and social_tether-prot-rise; moral_framework made material.
  # No axis he independently carries as position-holder — he is the transactional conduit.
  # All axes: not-applicable with vector/conduit rationale.

  - actor: jarvis-coin-kl-courier
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior accounting; Jarvis is the moral_framework-made-material vector — the exchange is the accounting event, not a position he carries"

  - actor: jarvis-coin-kl-courier
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Jarvis is the delivery conduit, not a capability carrier"

  - actor: jarvis-coin-kl-courier
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Jarvis is a courier-tier operative with no court position"

  - actor: jarvis-coin-kl-courier
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Jarvis recedes from the narrative before d14 and does not carry a collapse position"

  - actor: jarvis-coin-kl-courier
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor; Jarvis is a transactional contact with no relational-anchor function"

  - actor: jarvis-coin-kl-courier
    axis: moral_legibility_to_self
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's self-accounting; Jarvis has no moral-legibility arc — transactional flat-affect throughout"

  - actor: jarvis-coin-kl-courier
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward the elite; Jarvis is lower-city origin with no court-register investment"

  - actor: jarvis-coin-kl-courier
    axis: social_tether-prot-rise
    applicability: static
    start_rank: 2
    end_rank: 2
    source: inferred-from-role-card
    notes: "structural vector through which Taylor's social tether passes upward toward Otto; Jarvis's own position is flat-transactional throughout acts 1-2; static at 2 — present in the tether architecture without himself being a tether carrier; recedes to absent by act 3"

  - actor: jarvis-coin-kl-courier
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Jarvis is receding/absent in act 3 — not a tether-collapse carrier"

  - actor: jarvis-coin-kl-courier
    axis: social_tether-antag
    applicability: static
    start_rank: 2
    end_rank: 2
    source: inferred-from-role-card
    notes: "structural vector through which Otto's leverage over Taylor transmits at the exchange layer; Jarvis's own position in the leverage machinery is flat — he is the conduit, not the leverage-holder; static at 2; recedes to absent by act 3"

  - actor: jarvis-coin-kl-courier
    axis: position-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction institutional consolidation; Jarvis is three tiers below the faction intelligence structure and has no participation in the consolidation machinery"

  - actor: jarvis-coin-kl-courier
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position; Jarvis does not know the Green faction exists as a faction; no position on this axis"


  # === septon-halvard-flea-bottom (supporting:naive-idealist-foil; 12 axes) ===
  # moral_legibility_to_self mirror: static — his own moral legibility is stable by design (the contrast with Taylor).
  # All other axes: not-applicable.

  - actor: septon-halvard-flea-bottom
    axis: moral_framework
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis is Taylor's interior accounting; Halvard has his own moral framework (principled-slower Faith register) but it is not the anti-instrumentalization arc tracked by this axis"

  - actor: septon-halvard-flea-bottom
    axis: capability
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's insect-network deployment; Halvard has no capability arc in this framework"

  - actor: septon-halvard-flea-bottom
    axis: position-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's court-position rise; Halvard has no court position — minor precinct septon only"

  - actor: septon-halvard-flea-bottom
    axis: position-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's position collapse; Halvard does not collapse — he is still present at d14 in the precinct"

  - actor: septon-halvard-flea-bottom
    axis: relational_anchor_status
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's un-priced anchor (Wren); Halvard has no un-priced-anchor function"

  - actor: septon-halvard-flea-bottom
    axis: moral_legibility_to_self
    applicability: static
    start_rank: 7
    end_rank: 7
    source: inferred-from-role-card
    notes: "the moral-legibility mirror; his OWN legibility to himself is stable by design — principled-slower, names wrong acts without suppressing recognition; static at 7 (honest self-accounting, not full 9 because he acknowledges the cost of his slower method and its death-toll); the contrast with Taylor's non-linear rise is the load-bearing structural juxtaposition"

  - actor: septon-halvard-flea-bottom
    axis: political_register-prot
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's stance toward the elite; Halvard has no succession-register investment — his scale is Flea Bottom precinct, not court"

  - actor: septon-halvard-flea-bottom
    axis: social_tether-prot-rise
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's KL tether; Halvard's presence is Flea Bottom precinct — not a component of Taylor's court-adjacent tether architecture"

  - actor: septon-halvard-flea-bottom
    axis: social_tether-prot-collapse
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Taylor's tether collapse; Halvard is still present at d14 — he does not experience the tether collapse"

  - actor: septon-halvard-flea-bottom
    axis: social_tether-antag
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Otto's leverage over Taylor; Halvard has no participation in the patron-leverage machinery"

  - actor: septon-halvard-flea-bottom
    axis: position-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction institutional consolidation; Halvard is a minor precinct septon with no participation in the faction machinery"

  - actor: septon-halvard-flea-bottom
    axis: political_register-world
    applicability: not-applicable
    start_rank: null
    end_rank: null
    source: inferred-from-role-card
    notes: "axis tracks Green-faction succession position; Halvard does not calculate the succession — his scale is the sick and dying in the Hook"
