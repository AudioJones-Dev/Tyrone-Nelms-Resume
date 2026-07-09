# Site (GitHub Pages Surface)

This folder is the **curated public portal** — a deployment target, not the repository itself. The site's navigation intentionally surfaces only reviewed public artifacts, even though the public repository remains browsable on GitHub.

## Rules

- Pages quote only **approved deploy wording** from reviewed artifacts (bios, capability statements, resume variants) and link to sources for depth — never restate facts independently (drift risk).
- No private intelligence content, no client specifics, no Tier C metrics, no case studies until the gates in `docs/case-studies.md` clear.
- No committed PDFs — the download center will link to workflow artifacts in a later iteration.
- Edit site pages only to reflect changes already merged in the underlying artifacts.

## Enabling GitHub Pages (owner action required)

The deploy workflow (`.github/workflows/deploy-site.yml`) is **manual-dispatch only** and will fail until Pages is enabled:

1. Repository **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Run the "Deploy site" workflow from the Actions tab (workflow_dispatch).
3. After the first successful deploy, optionally switch the workflow trigger to `push` on `main` for `site/**` so the portal auto-updates.

The workflow builds this folder with Jekyll (`jekyll-theme-primer`), so the Markdown files here render as styled pages; relative `.md` links are converted automatically by the github-pages Jekyll plugins.
