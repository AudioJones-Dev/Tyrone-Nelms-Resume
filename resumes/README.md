# Resumes

Resume drafts and role-targeted variants, all derived from the canonical records in [`docs/`](../docs/index.md).

## Status

- [`master-resume.md`](master-resume.md) — **draft, not final.** Contains unresolved `TODO` items that must be cleared before any public export. Excluded from the export pipeline.
- [`ai-operations-consultant.md`](ai-operations-consultant.md) — reviewed; approved for export (content review completed in PR #3).
- [`operations-manager.md`](operations-manager.md) — reviewed; approved for export (PR #3).
- [`project-manager.md`](project-manager.md) — reviewed; approved for export (PR #3).
- [`customer-success.md`](customer-success.md) — reviewed; approved for export (PR #3).
- [`digital-marketing.md`](digital-marketing.md) — reviewed; approved for export (PR #3).
- [`executive-bio-resume.md`](executive-bio-resume.md) — **draft, pending strategic review.** Executive lens (judgment, systems, outcomes), not an ATS variant. Not in the export allowlist until reviewed.

## Variant Conventions

- Public contact (confirmed final): Tyrone.nelms87@gmail.com / 786-280-4470.
- Fuzzy older roles (Alorica, UnitedHealthcare) use year-only / approximate dates.
- The unverified 20% cost reduction and 15% productivity claims are **excluded** from all variants until evidence exists (tracked in `docs/accomplishments.md`).
- The PCMA crisis-prevention credential is excluded from variants until verified (tracked in `docs/certifications.md`).
- LinkedIn and portfolio URLs are omitted until confirmed (tracked in `docs/career-history.md` Open Questions).

## Rules

- Derive content from `docs/career-history.md` (chronology) and `docs/accomplishments.md` (achievements) — never from memory or old resume drafts.
- Keep fuzzy older dates approximate or year-only until verified (UnitedHealthcare and Alorica in particular).
- Do not include unverified metrics (see "Metrics to Verify" in `docs/accomplishments.md`).
- Exports (PDF/DOCX/HTML) are generated only for variants whose content review is recorded as complete above; the export script's allowlist in `scripts/export_resumes.py` must match this list. See [`exports/README.md`](../exports/README.md).
