# Changelog

## Unreleased

### Added

- Public portal (`site/`): curated GitHub Pages surface — index, profile, resumes, bios, capability statements, LinkedIn, and architecture pages, each quoting only approved deploy wording and linking to sources. Deploy workflow (`.github/workflows/deploy-site.yml`) builds `site/` with Jekyll and publishes via the Pages Actions path; manual-dispatch only until Pages is enabled in repository settings (owner action — see `site/README.md`). No PDFs committed; no Tier C metrics; no client specifics; no case studies pending gates.
- `docs/architecture-pattern.md` — the Professional Operating System pattern as a reusable, fully generic reference architecture (layer model, evidence tiers, governance gates, export doctrine, public/private boundary rules, review workflow, anti-patterns, minimal implementation checklist). Zero subject-specific facts; written to be liftable into a template repository unchanged.
- Executive & Capability Layer: `bios/` (short, founder, consultant, speaker, media bios and one-page executive summary — each with purpose, audience, approved wording, open questions, and maintenance rules) and `capability-statements/` (AI operations, operations systems, project management, digital transformation — each with approach, competencies, engagement model, and deliberate exclusions). `resumes/executive-bio-resume.md` added as an executive-lens resume (judgment/systems/outcomes framing; draft, excluded from the export allowlist pending review). All facts from canonical records; framing from the strategic layer; no Tier C metrics.
- Export pipeline: `scripts/export_resumes.py` generates PDF/DOCX/HTML for the five approved resume variants (pandoc for HTML/DOCX, headless Chrome for PDF, LibreOffice Writer fallback); `scripts/resume.css` styles HTML and PDF output; `.github/workflows/export-resumes.yml` regenerates exports on pushes to main and uploads them as build artifacts. Master resume remains excluded via the script's allowlist; artifacts stay out of Git per the existing `.gitignore` rules. `exports/README.md` rewritten with generation instructions.
- LinkedIn OS (`linkedin/`): canonical repository for the entire LinkedIn presence — `headline.md`, `about.md`, `experience.md`, `featured.md`, `recommendations.md` (profile surfaces) and `creator-positioning.md`, `content-pillars.md`, `post-frameworks.md`, `connection-messages.md`, `outreach.md` (growth surfaces), with a `README.md` deployment tracker. The live profile becomes a deployment target of these files.
- Strategic layer above the canonical records: `docs/career-positioning.md`, `docs/professional-brand.md`, `docs/achievement-library.md`, `docs/interview-playbook.md`, `docs/case-studies.md`. Future resumes, LinkedIn copy, bios, proposals, and case studies derive framing from these files and facts from the canonical records.
- Five role-targeted resume variants derived from canonical records: `resumes/ai-operations-consultant.md`, `resumes/operations-manager.md`, `resumes/project-manager.md`, `resumes/customer-success.md`, `resumes/digital-marketing.md`.
- `.gitignore` for OS/editor artifacts and unreleased export binaries.
- `CONTRIBUTING.md` with editing rules and factual-accuracy guardrails.
- `docs/index.md` navigation index linking all major files.
- `resumes/README.md`, `experience/README.md`, and `exports/README.md` folder guides.

### Changed

- Repository framing renamed from "Career OS" to **Professional Operating System (Professional OS)** across README, docs index, CONTRIBUTING, and LinkedIn OS references — the scope outgrew resumes (resume variants, LinkedIn OS, bios, capability statements, export pipeline all derive from one evidence-governed record). No facts or artifacts changed; the historical "v0.1 — Career OS Foundation" release title below is intentionally preserved.
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
