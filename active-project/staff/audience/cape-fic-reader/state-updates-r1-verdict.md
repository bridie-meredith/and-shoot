---
reviewer: cape-fic-reader
facet: state-updates
episode: b01c01
cycle: 1
date: 2026-05-25
verdict: revise
---

# Verdict reasoning

The operational state picture is tracking the right things — Taylor's deployment flip,
the capability increment, Oswyn's location and categorization, Wren's relational
anchor — and those are the beats I actually want recorded. But entry 8 is doing
something that makes me stop: it writes a field on Taylor's actor-state (`ward-recognition`)
that is Oswyn's cognitive act, not Taylor's, and the framing ("the ward's category for
Taylor") is unstable — is this Taylor knowing she's been categorized, or is it the
categorization itself? A cape-fic reader who is tracking who-knows-what-when cannot
have fuzzy entries on exactly the question of who-knows-what-when. Entry 6 also fires
at @21 on a bone that is Oswyn's move, not Taylor's, and the justification ("Taylor
enters Oswyn's awareness layer and the tether-account opens") is a registration framing,
not a canonical-state-change framing — which means this reader can't confidently say
what actually changed on Taylor's record at that beat.

---

# Per-entry readings (group by character file + env)

## taylor-hebert-kl-122ac

**Entry 3 (@12 — deployment-state: passive-subsistence-range -> active-crowd-yield-deployment)**
ACCEPT. This is the cleanest entry in the file. The insects propagate at @12 — field flips,
persists, handoff_out confirms it. I know exactly what changed. This is the kind of state
record I can track forward.

**Entry 4 (@12 — capability_axis: 2 -> 3)**
ACCEPT with a raised eyebrow. A stat increment anchored to a canonical axis-move at the
same bone as entry 3 — licit, and the substance_delta citation is load-bearing here.
The field-extension is documented. The only friction: two field-changes on the same
actor at the same anchor bone means I'm reading this chapter as a single moment of
double-upgrade, which is exactly what the bones show. Fine. The double-fire is
warranted.

**Entry 5 (@17 — posture: in-the-gap -> hands-up-mouth-shut-witness-facing)**
ACCEPT. Posture-as-state works here because the comment names the multi-beat persistence
and its load-bearing function explicitly: @17-@22, resolves at @24. The witness-
categorization beats listed (@19, @20, @21) confirm the state is load-bearing across
multiple bones. This passes the persistence test and the strip test — remove the entry
and the witness-reads at @19-@21 lose their canonical foundation.

**Entry 6 (@21 — social_tether_prot_axis: 1 -> 2)**
FLAG. The axis increment is claimed here ("Taylor enters Oswyn's awareness layer and
the tether-account opens"), but the anchor bone is @21 — "oswyn-mudway-flea-bottom-elder
takes the lane-mouth." That is Oswyn's action beat. The justification reads as
registration framing ("Taylor enters Oswyn's awareness layer") rather than naming what
Taylor's own tracked field actually changed at @21. A cape-fic reader tracking operational
state wants to know: what is the field state BEFORE @21, what is it AFTER, and why does
it flip at this bone rather than at @26 (Oswyn's chin-lift) or @27 (Wren faces Taylor)?
The comment claims the tether-account "opens" here, but the anchor is Oswyn's move not
Taylor's. If the substance contract says the social_tether axis increments at this bone,
I need the entry to say "because X happened to Taylor's state at this beat" — not "because
Oswyn moved." Entry is poorly defended; it passes form but not the strip test from my
perspective.

**Entry 7 (@24 — body-orientation: facing-the-child -> facing-the-alley-mouth-away-from-stitch-house)**
ACCEPT. Clean. The bone name is "taylor-hebert-kl-122ac faces the alley-mouth" — the
body-orientation field flips on the exact beat where the verb says it flips. The comment
names the persistence ("through chapter close") and the load-bearing function (the
not-looking is enacted as a direction-toward). This is exactly what I want in a
state-update.

**Entry 8 (@26 — ward-recognition: invisible-foreign-woman -> categorized-by-oswyn-as-something-other)**
FLAG. The field name is `ward-recognition` and the comment says "the ward's category for
Taylor." But the field is being written on `actor:taylor-hebert-kl-122ac` — not on
`actor:oswyn-mudway-flea-bottom-elder`. So: is this Taylor's knowledge of her own
categorization, or is it Oswyn's categorization act? If it is Taylor's knowledge of
being categorized, then (a) this is a POV-actor knowledge field-extension and (b) it
needs narrator-interest co-citation on @26 to satisfy the cross-facet contract. The
cite-index shows @26 carries [mem:2] [state:2] [state:8] — `state:8` is this entry,
and `mem:2` is the only co-citation candidate. There is no `narrator:*` co-citation
at @26. If this is a POV-actor knowledge shift ("Taylor now knows she has been
categorized"), the missing narrator-interest co-citation is a breach. If this is meant
to track the ward's social-category-for-Taylor (Oswyn's view), then it should not be
on Taylor's actor record at all — it should be on Oswyn's. The field sits in an
authority gap and the name does not resolve it. A cape-fic reader who is tracking
who-knows-what-when cannot let this stand: the entry is ambiguous on the exact axis
(Taylor's knowledge vs. Oswyn's categorization) that makes the scene's information
asymmetry interesting.

## oswyn-mudway-flea-bottom-elder

**Entry 1 (@21 — location: mudway-alley-hook-district -> lane-mouth-of-rescue-site)**
ACCEPT. Bone name: "oswyn-mudway-flea-bottom-elder takes the lane-mouth." Location
flips on the beat the verb names. Clean. Persistent — Oswyn stays at the lane-mouth
through @26 at minimum. No ambiguity.

**Entry 2 (@26 — relationship_to_taylor: regular-contact-no-awareness-of-function -> categorized-known-unknown-witch-adjacent)**
ACCEPT with a note. The field-extension is documented and the anchor bone ("oswyn-mudway-flea-bottom-elder
lifts the chin") is the right somatic tell for the categorization-completing act. Persistence
past the chapter is confirmed in the handoff_out comment. The `witch-adjacent` value is
exactly the kind of faction-legible categorization that makes a cape-fic reader pay attention.
What I want to cross-check: entry 8 on Taylor's slice is also firing at @26 about this same
act of categorization. Two entries on two actors, same beat, same categorization event —
Oswyn's entry 2 is the categorization act; Taylor's entry 8 is Taylor's recognition of being
categorized. That's coherent in principle, but entry 8's authority gap (described above)
means the pair is not cleanly resolved.

## wren-stitch-maker-flea-bottom-ward

**Entry 9 (@27 — relational_anchor_to_taylor: nascent -> observation-traced-d01-deterrence)**
ACCEPT with a note. Wren's single entry at the chapter's final bone. The value
`observation-traced-d01-deterrence` is information-rich (Wren has observed Taylor;
the deterrence tag implies Wren read the crowd-yield as a threat-adjacent signal, not
just curiosity). As a cape-fic reader I want this field to track forward into subsequent
chapters — this is the kind of relational-state entry that pays off when Wren shows up
again and the relationship has a documented foundation. The field-extension is sparse on
documentation compared to Taylor's entries, but the persistence claim is implicit in
`relational_anchor` (it names an anchor, not a transient registration). Acceptable.

## env

**Zero entries — carve-out defended.**
ACCEPT. The carve-out rationale is correct by the rubric: static exterior environment,
no prop cards, no tracked prop exchanges, no door states, no time-of-day shift. The
tallow smoke is ambient-continuous (not a state flip from a prior canonical value),
crowd-dynamics are transient and revert. The fish-cart non-entry is the right call —
no prop card, no oc-* warehouse presence, refuse and flag is the conservative ruling.
SEAM-001 and SEAM-002 are flagged appropriately. A zero-fire env pass on a chapter
this sparse is not a coverage failure.

---

# Entry-level callouts (revise/fail only)

**[state-updates:6] @21 actor:taylor-hebert-kl-122ac.social_tether_prot_axis: 1 -> 2**
— The entry fires on Oswyn's action bone. The comment reads as registration ("Taylor
enters Oswyn's awareness layer") not as a named field mutation on Taylor. Strip the
entry: would Taylor's `social_tether_prot_axis` still be 2 at @22 without this entry?
The substance contract claims yes, but the bone rationale points to Oswyn moving, not
to a canonical Taylor-state change at this beat. Either (a) rename the justification to
specify what Taylor's field actually did at @21 (not what Oswyn did) or (b) move the
fire to the beat where Taylor's own state demonstrably changes — candidates are @26
(Oswyn's chin-lift completes the categorization) or @27 (Wren's registration closes
the social circuit). If the substance contract anchors the axis-move at b01c01s03n04
and that maps to @21, surface that mapping explicitly so I can verify it — right now
it's asserted, not shown.

**[state-updates:8] @26 actor:taylor-hebert-kl-122ac.ward-recognition: invisible-foreign-woman -> categorized-by-oswyn-as-something-other**
— The field name is ambiguous: `ward-recognition` on Taylor's record could mean (a)
the ward's recognition of Taylor (Oswyn's cognitive state — wrong actor) or (b)
Taylor's recognition of her own status in the ward (Taylor's knowledge — correct actor,
but requires narrator-interest co-citation). The cite-index at @26 shows no `narrator:*`
co-citation, only [mem:2] [state:2] [state:8]. If this is a POV-actor knowledge shift,
the narrator-interest co-citation breach must be resolved. If this is meant to encode
Oswyn's view of Taylor, the field belongs on Oswyn's record (already covered by entry 2
in a different form) or must be renamed to unambiguously mark it as Taylor's knowledge
field (e.g., `actor:taylor-hebert-kl-122ac.knowledge.ward-status-as-seen-by-oswyn`).
As written the entry conflates the two sides of the information asymmetry at exactly
the beat where that asymmetry is the story.

---

# Convergence trace

**[state-updates:6] @21 (registration-as-state concern)**
— Overlaps with rubric anti-pattern #1 (Registration-as-state): the comment frames
the entry as Taylor entering Oswyn's awareness ("the tether-account opens") which
reads as a perception/registration beat, not a canonical field mutation on Taylor.
The auditor's facets-final-audit-r2 did not flag this entry directly (audit was
CLEAN on state-updates), but the rubric's § Reality REJECT signature "Registration-as-state
— the proto-line is a perception beat but no field on any target changes" applies:
@21 is Oswyn's action bone; Taylor's awareness of being entered into Oswyn's field is
narrator-interest territory. Whether the substance contract requires the axis-increment
to fire here is a separate question — but the entry needs to name what Taylor's field
does, not what Oswyn's move means for the relationship.

**[state-updates:8] @26 (POV-actor knowledge field, missing narrator-interest co-citation)**
— Cross-facet contract: rubric § "POV-character actor-state must have narrator-interest
co-citation." The cite-index at @26 shows [mem:2] [state:2] [state:8] — no `narrator:*`
entry. The auditor's R2 report flagged no state-updates entries directly, but the cross-
facet contract check (§ "Cross-facet test" — "actor:<POV-character>.* entries paired
with narrator-interest co-citation on the same beat") would catch this if the entry is
classified as a POV-actor knowledge shift. The R2 report is CLEAN on state-updates,
suggesting either the auditor treated this as a non-POV-knowledge field (social
recognition status, not knowledge.*) or the cross-facet check was not applied to this
entry. Either way, the authority gap and co-citation gap are real and unresolved.
