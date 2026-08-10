# Resumes

Resume drafts and role-targeted variants, all derived from the canonical records in [`docs/`](../docs/index.md).

## Status

- [`master-resume.md`](master-resume.md) — second-pass source copy prepared; excluded from the export pipeline pending final human review.
- [`ai-operations-consultant.md`](ai-operations-consultant.md) — legacy path containing the AI & Business Systems Architect variant; second-pass source copy prepared.
- [`operations-manager.md`](operations-manager.md) — reviewed; approved for export (PR #3).
- [`project-manager.md`](project-manager.md) — reviewed; approved for export (PR #3).
- [`customer-success.md`](customer-success.md) — reviewed; approved for export (PR #3).
- [`digital-marketing.md`](digital-marketing.md) — reviewed; approved for export (PR #3).
- [`executive-bio-resume.md`](executive-bio-resume.md) — executive lens aligned to Operations & Business Systems Architect; not in the export allowlist until human review.

## Variant Conventions

- Public contact (confirmed final): Tyrone.nelms87@gmail.com / 786-280-4470.
- Approved public chronology: AHLO 2006–2007 and 2019–2023; TigerDirect 2008–2011; Alorica 2015; UnitedHealthcare 2016–2018.
- The unverified 20% cost reduction and 15% productivity claims are **excluded** from all variants until evidence exists (tracked in `docs/accomplishments.md`).
- The PCMA crisis-prevention credential is excluded from variants until verified (tracked in `docs/certifications.md`).
- LinkedIn and portfolio URLs are omitted until confirmed (tracked in `docs/career-history.md` Open Questions).

## Rules

- Derive content from `docs/career-history.md` (chronology) and `docs/accomplishments.md` (achievements) — never from memory or old resume drafts.
- Use the approved chronology exactly; retain conflicting source variants only in the internal experience records.
- Preserve actual employer titles. Use Operations & Business Systems Architect as the umbrella positioning title, not as a retroactive title for unrelated employment.
- Describe VPL Flow only as specified operations-system architecture; do not imply application code, deployment, production use, customer adoption, or measured outcomes.
- Refer to private evidence as “private repository—walkthrough available”; never publish a private repository URL.
- Do not include unverified metrics (see "Metrics to Verify" in `docs/accomplishments.md`).
- Exports (PDF/DOCX/HTML) are generated only for variants whose content review is recorded as complete above; the export script's allowlist in `scripts/export_resumes.py` must match this list. See [`exports/README.md`](../exports/README.md).
