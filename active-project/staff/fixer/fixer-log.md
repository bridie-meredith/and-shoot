# Fixer Log — 1d constraint-consistency check
session: 2026-05-09

---

## fault-001 — RESOLVED
fault: actor card cost curve diverges from warehouse cond-fauna-control-rules (10/20/30 vs 3/10/20 breakpoints)
scope: card
change: No edit required. cards/personas/taylor-hebert-jaehaerys.card.md already carries the correct child-body numbers (3–10 min headache, 10–20 nosebleed, 20+ blackout) in both the ambient_vs_directed NOTE (Stats block) and the Action Costs section. These match the warehouse card exactly. The provisioned copy in active-project/actors/ is a stub pointing to the library card and does not independently state the cost curve. Criterion met as-is.
criteria met: yes

---

## fault-002 — RESOLVED
fault: library cond-fauna-control-rules scoped to wrong project (taylor-hebert-westeros) with dead cross-references
scope: card
change: No edit required. cards/conditions/cond-fauna-control-rules.card.md already carries scope: library with no project field. Interaction Notes reference cond-westerosi-customary-authority-jaehaerys (correct 84 AC slug) and do not contain cond-impressment-census-120ac or the generic cond-westerosi-customary-authority. Criterion met as-is.
criteria met: yes

---

## fault-003 — RESOLVED
fault: library cond-no-parahuman-infrastructure and warehouse copy have inverted scope values; library body references 120 AC and taylor-hebert-westeros
scope: card
change: No edit required. cards/conditions/cond-no-parahuman-infrastructure.card.md already carries scope: library with no project field; title reads "Hard World-Law (Planetos)" with no taylor-hebert-westeros or 120 AC reference. active-project/warehouse/cond-no-parahuman-infrastructure.card.md already carries scope: project and project: taylor-hebert-jaehaerys. Criterion met as-is.
criteria met: yes

---

## fault-004 — RESOLVED
fault: both copies of condition-swarm-in-foreign-ecology contain dead cross-references (condition-language-barrier, condition-war-of-five-kings-riverlands); warehouse copy lacks project-scope metadata
scope: card
change: Library card (cards/conditions/condition-swarm-in-foreign-ecology.card.md) — confirmed no dead references present; Interaction Notes section already clean (scene-level use only). Warehouse copy (active-project/warehouse/condition-swarm-in-foreign-ecology.card.md) — two edits applied directly: (1) frontmatter updated from scope: library / no project field to scope: project / project: taylor-hebert-jaehaerys / overrides: condition-swarm-in-foreign-ecology; (2) dead Interaction Notes entries for condition-language-barrier and condition-war-of-five-kings-riverlands removed and replaced with a single era-correct entry referencing cond-westerosi-superstition-frame.
files changed: active-project/warehouse/condition-swarm-in-foreign-ecology.card.md
criteria met: yes

---

## fault-005 — RESOLVED
fault: Stage 4 age annotation in cond-suppression-policy-progression reads "Taylor age ~21" for 98–101 AC; correct is ~14–17
scope: card
change: No edit required. active-project/warehouse/cond-suppression-policy-progression.card.md Stage 4 header already reads "Taylor age ~14–17". cards/conditions/cond-suppression-policy-progression.card.md Stage 4 header carries no age annotation (not ~21). Neither copy contains the erroneous ~21 annotation. Criterion met as-is.
criteria met: yes
