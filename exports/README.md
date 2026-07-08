# Exports

Generated PDF, DOCX, and HTML outputs will live here.

## Status

**No exports yet.** Final exports are blocked until:

1. Content review of the canonical records in `docs/` is complete.
2. All `TODO` items in `resumes/master-resume.md` under "Resume TODO Before Public Use" are resolved.
3. Unverified metrics and fuzzy dates are either verified or explicitly approved as approximate.

## Rules

- Exports are generated from the Markdown drafts in `resumes/` and `linkedin/` — never edited directly.
- Binary export artifacts (`.pdf`, `.docx`, `.html`) are gitignored by default; commit a specific export deliberately with `git add -f` when it is approved for release.
- Name exports with the variant and date, e.g. `master-resume-2026-07.pdf`.
