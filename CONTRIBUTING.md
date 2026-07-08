# Contributing to the Career OS

This repository is the canonical source of truth for Tyrone Nelms' professional record. Every change should protect the accuracy of that record.

## Ground Rules

1. **Never fabricate.** No invented dates, titles, metrics, certifications, or outcomes. If a fact is not verified, mark it with `TODO` or a status label instead of guessing.
2. **Canonical files win.** When files disagree, `docs/career-history.md` is the authority for chronology. Fix the downstream file, not the canonical one — unless the canonical file is the one that is wrong, in which case correct it with a source note.
3. **Preserve uncertainty markers.** Do not remove `TODO` items, `needs_verification` labels, or "approximate" date qualifiers unless the underlying fact has actually been verified. Fuzzy older dates stay approximate or year-only.
4. **Respect public/private boundaries.** Client-specific details for AJ Digital and Florida Ramp & Lift stay out of public-facing copy unless explicitly approved.
5. **Source records vs. polished copy.** `experience/*.md` files are internal source records — keep source notes and reconciliation history there. Public polish belongs in `resumes/` and `linkedin/`.

## File Roles

| File / Folder | Role |
|---|---|
| `docs/career-history.md` | Canonical chronology — authority for dates, employers, titles |
| `docs/accomplishments.md` | Achievement library — reusable, evidence-based accomplishments |
| `docs/skills.md` | Skills ontology grouped by domain |
| `docs/certifications.md` | Credentials record with verification links |
| `docs/target-roles.md` | Target role strategy and positioning guardrails |
| `experience/*.md` | Role-level source records (not public copy) |
| `resumes/*.md` | Resume drafts and variants derived from `docs/` |
| `linkedin/*.md` | LinkedIn profile copy drafts |
| `templates/*.md` | Reusable content templates |
| `exports/` | Generated PDF/DOCX/HTML outputs (none yet) |

## Workflow

- Add new roles using `templates/experience-template.md`.
- When a fact is verified, resolve its `TODO` in the same commit that updates the content, and note the source.
- Update `CHANGELOG.md` for milestone-level changes.
- Use conventional commit messages, e.g. `docs: reconcile alorica end date`.

## Status Labels

- `verified` — appears in uploaded resumes or the current professional record.
- `needs_verification` — conflicts between sources or awaiting date/title confirmation.
- `current_context` — supported by recent working context; review before public release.
- `private_context` — internal only; do not publish.
