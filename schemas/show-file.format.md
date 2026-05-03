# Show File Format

The show file is the episode manuscript written line by line during shoot. It lives at `active-project/theater/show.md`. It is append-only during shoot. At episode close it is the raw draft passed to wrap.

---

## Format rules

- **Plain text only.** No markdown syntax: no `#` headings, no `*` or `_` for emphasis, no `-` list bullets, no backticks, no link syntax.
- **Single blank line** between scene blocks only. Within a scene, no blank lines between content lines.
- **One line per bullet.** Each bullet from the episode plan produces exactly one line in the show file.
- **No abbreviation.** Write unabbreviated prose. Contractions are fine; shorthand is not.
- **No stage directions.** No `(he turns)` or `[beat]` conventions. Everything is rendered as prose or dialogue.

---

## Annotation format

Annotations appear at the **start of a line**, before any content. Format: `[TYPE:detail]`

The type is always UPPERCASE. The detail follows immediately after the colon, no space.

```
[NEEDS_EDIT:three tries exhausted, audience rejected each] She didn't answer.
[AUDIENCE:flat delivery, no tension in the exchange] He nodded.
[SCENE_START:warehouse confrontation]
[SCENE_END:warehouse confrontation]
[FAULT:fault-003]
```

**Annotation types:**

`[NEEDS_EDIT:reason]` — three-try budget exhausted. The most recent attempt is kept and marked. Showrunner moves to the next bullet without resolving. Editor addresses these in wrap.

`[AUDIENCE:reason]` — audience flag from the wrap-phase entertainment review. Not a rewrite trigger — showrunner decides at wrap whether to patch now or carry to editor.

`[SCENE_START:label]` — dramatist-placed scene boundary marker. Everything inside these markers is episode content. Applied during wrap.

`[SCENE_END:label]` — closes the matching SCENE_START. Content outside scene flags is cut by editor during wrap. The flags themselves are preserved as editor context.

`[FAULT:id]` — auditor fault reference. Links this line to a specific entry in the audit report. Applied by auditor or fixer.

---

## Scene context headers

Showrunner writes plain-text scene context headers between scene blocks. These are not content lines — they orient the editor and auditor. Format:

```
-- scene: <brief label> --
```

Example:
```
-- scene: warehouse confrontation, night --
```

Headers are not annotated or cut. They remain in the show file through wrap and into the final draft as structural anchors.

---

## Deletion during shoot

When audience rejects a line, showrunner deletes the line from the show file before issuing the retry. The show file never accumulates failed attempts. Only successful lines and three-try failures (marked NEEDS_EDIT) persist.

---

## Example show file fragment

```
-- scene: diner, early morning --

The coffee had gone cold. She hadn't touched it since he sat down.
He said he'd been following her for three days. She didn't look surprised.
[NEEDS_EDIT:tone mismatch, impersonator rejected prompt twice] She asked him what he wanted.
He told her. She finally picked up the cup.

-- scene: alley behind diner --

[SCENE_START:alley exit]
Rain. The alley smelled like wet cardboard and something older.
[SCENE_END:alley exit]
```
