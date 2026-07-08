# Changelog

## Unreleased

### Added

- Export pipeline: `scripts/export_resumes.py` generates PDF/DOCX/HTML for the five approved resume variants (pandoc for HTML/DOCX, headless Chrome for PDF, LibreOffice Writer fallback); `scripts/resume.css` styles HTML and PDF output; `.github/workflows/export-resumes.yml` regenerates exports on pushes to main and uploads them as build artifacts. Master resume remains excluded via the script's allowlist; artifacts stay out of Git per the existing `.gitignore` rules. `exports/README.md` rewritten with generation instructions.
- LinkedIn OS (`linkedin/`): canonical repository for the entire LinkedIn presence — `headline.md`, `about.md`, `experience.md`, `featured.md`, `recommendations.md` (profile surfaces) and `creator-positioning.md`, `content-pillars.md`, `post-frameworks.md`, `connection-messages.md`, `outreach.md` (growth surfaces), with a `README.md` deployment tracker. The live profile becomes a deployment target of these files.
- Strategic layer above the canonical records: `docs/career-positioning.md`, `docs/professional-brand.md`, `docs/achievement-library.md`, `docs/interview-playbook.md`, `docs/case-studies.md`. Future resumes, LinkedIn copy, bios, proposals, and case studies derive framing from these files and facts from the canonical records.
- Five role-targeted resume variants derived from canonical records: `resumes/ai-operations-consultant.md`, `resumes/operations-manager.md`, `resumes/project-manager.md`, `resumes/customer-success.md`, `resumes/digital-marketing.md`.
- `.gitignore` for OS/editor artifacts and unreleased export binaries.
- `CONTRIBUTING.md` with editing rules and factual-accuracy guardrails.
- `docs/index.md` navigation index linking all major files.
- `resumes/README.md`, `experience/README.md`, and `exports/README.md` folder guides.

### Changed

- `docs/career-history.md` — public contact details confirmed final; recorded decisions to use year-only/approximate dates for fuzzy older roles and to exclude the unverified 20%/15% metrics from resume variants; resolved the date-display open question.
- `resumes/README.md` — variant list updated to reflect created drafts and documents the shared variant conventions (contact, approximate dating, excluded unverified claims).
- README now links to the navigation index and separates planned folders from existing ones.
- Master resume Doctors Diabetics title aligned to the canonical career history (Medical Records Clerk).

### Removed

- `linkedin/profile-draft.md` — fully migrated into the LinkedIn OS (headlines → `linkedin/headline.md`, About → `linkedin/about.md`, featured ideas → `linkedin/featured.md`, guardrails absorbed into `linkedin/README.md` rules).

## v0.1 — Career OS Foundation

Initial repository foundation for Tyrone Nelms Career Operating System.

### Added

- Repository README.
- Canonical career history.
- Professional summary variants.
- Skills ontology.
- Certifications record.
- Accomplishments library.
- Target roles strategy.
- Experience records for AJ Digital, Florida Ramp & Lift, Alorica, UnitedHealthcare, AHLO, TigerDirect, and Miami Spin 360.
- Master resume draft.
- LinkedIn profile draft.
- Experience template.

### Known Gaps

- Several date ranges need reconciliation across older resume versions.
- Public contact details need confirmation before final exports.
- Certificate names and issue dates should be confirmed directly from Coursera.
- Public/private boundaries need review before publishing client-specific case studies.
