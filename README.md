# Tyrone Nelms Professional Operating System

Canonical source of truth for Tyrone Nelms' professional experience, accomplishments, certifications, resumes, LinkedIn profile, portfolio material, and executive positioning.

## Purpose

This repository is designed to maintain one verified professional record and generate targeted career artifacts from it.

Outputs may include:

- Master resume
- AI Operations Consultant resume
- Operations Manager resume
- Project Manager resume
- Customer Success resume
- Digital Marketing resume
- LinkedIn profile sections
- Professional bios
- Portfolio case studies
- Consulting capability statements

## Operating Principles

- Maintain one canonical source of truth.
- Separate verified facts from positioning language.
- Do not fabricate dates, titles, metrics, certifications, or outcomes.
- Mark uncertain items with `TODO` until verified.
- Prefer evidence-based accomplishments over generic responsibility statements.
- Keep resumes ATS-friendly and readable.
- Preserve public/private boundaries for client-sensitive work.

## Navigation

Start at [`docs/index.md`](docs/index.md) for a full index of all records, drafts, and templates. Editing rules live in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository Status

The Professional OS is under active construction. The canonical knowledge base, strategic positioning layer, resume variants, LinkedIn OS, executive/capability layer, and export pipeline exist; publication surfaces (portfolio, GitHub Pages) are still ahead.

Naming note: this repository began as the "Career OS" (see CHANGELOG v0.1). It was renamed to Professional Operating System because its scope outgrew resumes — it now generates resumes, LinkedIn copy, bios, capability statements, and exports from one evidence-governed record. Historical release titles in the changelog keep the original name.

## Core Folders

- `docs/` — canonical career records, skills, certifications, accomplishments, and target roles.
- `experience/` — role-level experience files by employer or project.
- `resumes/` — generated or hand-curated resume variants.
- `linkedin/` — LinkedIn headline, about section, and experience copy.
- `bios/` — short, founder, consultant, speaker, and media bios plus the executive summary.
- `capability-statements/` — AJ Digital service-line capability statements.
- `site/` — curated GitHub Pages portal (deployment target; see `site/README.md`).
- `templates/` — reusable content templates.
- `exports/` — generated PDF, DOCX, and HTML outputs (via `scripts/export_resumes.py`).

Planned folders, to be added when their first content lands:

- `portfolio/` — public-facing case studies and project summaries.
- `evidence/` — supporting proof points, links, and source notes.
