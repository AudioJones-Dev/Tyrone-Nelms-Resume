# Exports

Generated PDF, DOCX, and HTML outputs for the approved resume variants.

## Status

- **Exportable now:** the five reviewed variants in [`resumes/`](../resumes/README.md) — ai-operations-consultant, operations-manager, project-manager, customer-success, digital-marketing (approved in the resume-variants content review).
- **Still blocked:** `master-resume.md` — its "Resume TODO Before Public Use" items must be resolved first. The export script enforces this via its approved-variants allowlist.

## How to Generate

### Locally

```bash
python3 scripts/export_resumes.py                      # all variants, all formats
python3 scripts/export_resumes.py --only project-manager
python3 scripts/export_resumes.py --formats pdf
python3 scripts/export_resumes.py --stamp 2026-07      # override the date stamp
```

Dependencies:

- **pandoc** — `apt install pandoc`, or `pip install pypandoc-binary` (the script auto-detects either).
- **PDF engine** — Chrome/Chromium (auto-detected, preferred) or LibreOffice with Writer. Override with `RESUME_PDF_ENGINE=/path/to/browser`.

Pipeline: Markdown → HTML (pandoc + `scripts/resume.css`) and Markdown → DOCX (pandoc); PDF is printed from the styled HTML by headless Chrome, so PDF and HTML always match.

### Continuous (GitHub Actions)

[`export-resumes.yml`](../.github/workflows/export-resumes.yml) regenerates all formats on every push to `main` that touches `resumes/` or `scripts/`, and on manual dispatch. Outputs are uploaded as a build artifact (`resume-exports-<sha>`, 90-day retention) — download from the workflow run page. Nothing is committed to the repository.

## Rules

- Exports are generated from the Markdown sources in `resumes/` — **never edit an export directly**; edit the source and regenerate.
- Binary artifacts (`.pdf`, `.docx`, `.html`) are gitignored. Commit a specific export deliberately with `git add -f` only when it is approved as a release deliverable.
- Naming is automated: `<variant>-<YYYY-MM>.<ext>`.
- Styling lives in `scripts/resume.css` (screen + print rules). Content questions belong in the resume sources, not the stylesheet.
