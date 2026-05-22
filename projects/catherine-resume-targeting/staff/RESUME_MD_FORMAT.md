# Resume markdown format

Structured markdown consumed by `staff/md_to_docx.py` to produce a one-page
`.docx` in Catherine's house style. The name line ("Catherine Olver, EdD") is
fixed by the converter — do not include it.

```
TAGLINE: one-line positioning tagline (sits under the name, centered)
CONTACT: Algona, WA  •  253.335.9805  •  CEOlverThompson@alaska.edu  •  LinkedIn: linkedin.com/in/catherineolver

# SECTION HEADER
Body paragraph text (used for the PROFILE block).

# STRENGTHS HEADER
- bullet line
- bullet line

# SELECTED EXPERIENCE
## Role Title — Organization | Location  •  Dates
- bullet line
- bullet line
```

Rules:
- `TAGLINE:` / `CONTACT:` — header block. One each.
- `# ` — section header, rendered bold uppercase.
- `## ` — role/entry line. Text before the first ` — ` is bolded (the title);
  the rest is the organization; everything after ` | ` is location/dates in
  smaller type. Keep the ` — `, ` | `, and `  •  ` separators.
- `- ` — bullet.
- Any other non-blank line — body paragraph.
- Keep it to one page: roughly 45-52 content lines total.
