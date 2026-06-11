# Agents Improvement-Loop Ledger

Round-robin registry. Each entry: agent tuned, the one change, next agent in rotation.
Survey scope: `.claude/agents/*.md` + `staff/*/card.md`.

---

## Round-robin order (alphabetical by file name, first pass)

1. admin
2. audience
3. auditor
4. coach
5. dramatist
6. editor
7. fixer
8. impersonator
9. margit
10. renderer-minimal
11. screen-writer  ← **TUNED 2026-06-11**
12. showrunner
13. studio

---

## Log

### 2026-06-11 — screen-writer

**Agent:** `.claude/agents/screen-writer.md`
**Finding:** `description` field used legacy pipeline vocabulary throughout. Said "Works at series, season, and episode levels" (wrong: current pipeline is series/book/chapter). Said "Receives a chunk statement and constraints from showrunner" (wrong: command bodies are the dispatchers). Said "At episode level, the plan is the show file script" (wrong: episode level is archived; chapter level output is scene chunks with substance metadata).
**Change:** Updated `description` field to replace season/episode with book/chapter, corrected dispatcher from "showrunner" to "dispatching command body", replaced "show file script" claim with accurate chapter-level output description.
**Why this one:** The description field is the highest-visibility contract surface — read by dispatching command bodies and by the agent itself. Stale vocabulary here can cause the agent to misunderstand or resist its actual task scope.

**Next in rotation:** showrunner (`.claude/agents/showrunner.md`) — body contains a large legacy "Episode shoot — line-by-line loop" section and planning patterns in series/season/episode vocabulary; the "Role boundary" disclaimer covers the orchestration patterns but does not update the vocabulary; the body's shoot-loop section uses imperative voice directed at showrunner and is not clearly flagged as archived.
