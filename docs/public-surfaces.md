# Public Surfaces

Canonical registry of the public web properties that represent Tyrone Nelms professionally.

## Why This File Exists

Resumes, LinkedIn copy, bios, and capability statements are all governed by this repository. The live websites were not — they existed outside the record entirely. That created two problems:

1. **No governed answer to "which link do I send?"** Applications ask for a portfolio URL. Without a registry, that choice was made ad hoc per application.
2. **No claim boundary between audiences.** The employer-facing portfolio and the client-facing consultancy brand make different kinds of claims. Nothing documented which claims were allowed to cross.

Surfaces are **deployment targets**, exactly like `linkedin/` and `site/`. Canonical facts live in `docs/`; surfaces present them. When a surface and a canonical record disagree, the canonical record wins and the surface is corrected — per `CONTRIBUTING.md` ground rule 2.

## Surface Registry

| Surface | Audience | Owner entity | Governed by | Status |
|---|---|---|---|---|
| [tyronenelms.com](https://tyronenelms.com) | Employers, hiring managers, recruiters | Tyrone Nelms (individual) | This repository | `verified` — live |
| [audiojones.com](https://audiojones.com) | Prospective consulting clients | AJ Digital LLC (Audio Jones brand) | Commercial brand; **not** this repository | `verified` — live |
| GitHub Pages portal (`site/`) | Employers; documentation depth | Tyrone Nelms (individual) | This repository | `needs_verification` — deploy status unconfirmed |
| [LinkedIn](https://www.linkedin.com/in/audiojones) | Employers, recruiters, network | Tyrone Nelms (individual) | `linkedin/` in this repository | `verified` — live |
| [GitHub org](https://github.com/AudioJones-Dev) | Technical evaluators | Tyrone Nelms (individual) | Evidence repositories | `verified` — live |

Observations of live site content in this file were recorded 2026-08-11. Re-verify before citing them in an application.

## tyronenelms.com — Primary Employer-Facing Surface

**Positioning:** "Operations & Business Systems Architect." This matches the target positioning in `docs/target-roles.md` and Career OS, so the surface and the search strategy are aligned.

**Structure observed:** navigation across Work, About, Ventures, Résumé, and Contact. Capabilities are grouped as business analysis, process and systems design, systems implementation, and AI-enabled workflows. Three case studies are featured: Florida Ramp & Lift FieldOps, Career OS, and ARO (execution runtime). Contact is direct email (`tyrone@tyronenelms.com`) plus LinkedIn and GitHub.

**This is the default portfolio link for employment applications.** It is the only surface whose audience, positioning, and claim discipline all match an employment context.

**Claim rule:** anything asserted here must be derivable from `docs/` canonical records at the maturity level the evidence supports. It is an individual professional surface, not a commercial one — it should not carry AJ Digital client-performance metrics.

## audiojones.com — Commercial Brand Surface

**Entity:** an operating brand of AJ Digital LLC, serving founder-led businesses. Positioning is built around a signal/noise thesis, with service lines including ResponseOS, Founder Intelligence Systems, an AI readiness diagnostic, and an ROI calculator.

**This surface is evidence that AJ Digital exists and operates as a real consultancy with defined service lines.** That is genuinely useful — it substantiates the consulting entity referenced in `experience/aj-digital.md`. It is legitimate to reference for that purpose.

### Metric Boundary — Required Reading

audiojones.com publishes engagement-performance figures (CAC reduction, pipeline growth, and conversion-rate improvements are stated on the site as of 2026-08-11).

**Those figures must not enter resumes, application briefs, cover letters, LinkedIn copy, or interview claims sourced from this repository.**

This is not a judgment that the figures are wrong. It is that they are **client-facing marketing claims whose underlying measurement is not documented in this repository's evidence chain.** `CONTRIBUTING.md` ground rule 1 forbids unverified metrics in the professional record, and Career OS's evidence rules forbid publishing unverified percentages, revenue effects, or cost savings. A number being published on a site you own does not convert it into verified evidence — the verification has to exist.

To lift any of these figures into employment-facing material, first land the measurement basis in `docs/accomplishments.md` with its source, method, time window, and scope. Until then the figure stays on the marketing site only.

### Audience Separation

Do not send audiojones.com as the portfolio link for an employment application. It sells consulting services. To a hiring manager evaluating a full-time candidate, a consultancy sales page reads as a competing commitment rather than as evidence of capability. Reference the entity through `tyronenelms.com`'s Ventures section instead, which frames it as background rather than as an active pitch.

## GitHub Pages Portal (`site/`)

The `site/` folder deploys to GitHub Pages and carries no `CNAME`, so it does **not** serve `tyronenelms.com` — the two are independent properties. Per `site/README.md` the deploy workflow is manual-dispatch and requires Pages to be enabled in repository settings; whether a successful deploy has occurred is unconfirmed.

**Overlap warning:** the portal and tyronenelms.com address the same audience with the same positioning. Two employer-facing surfaces that can drift apart is a maintenance liability. Until that is resolved, treat tyronenelms.com as primary and the portal as documentation depth for technical evaluators who want to read the underlying record. Resolving the overlap — retire, redirect, or formally differentiate — is an open decision, not something to settle silently.

## Open Verification Items

- `needs_verification` — **ARO (execution runtime)** is featured as a case study on tyronenelms.com but has no entry in this repository or in Career OS's evidence index. Either add it as a governed evidence source with a maturity label, or reconcile the site.
- `needs_verification` — **Location claim.** tyronenelms.com states a Miami base. Career OS plans around Southwest Florida relocation flexibility (Fort Myers, Cape Coral). Both can be true simultaneously, but the surface and the search strategy should state the same thing to a recruiter who reads both.
- `needs_verification` — GitHub Pages portal deploy status and the surface-overlap decision above.

## Maintenance Rules

1. A new public surface is added to this registry in the same change that launches it.
2. Surfaces present canonical facts; they do not originate them. New facts land in `docs/` first.
3. Claims do not cross the employer/client audience boundary without an explicit entry in this file permitting it.
4. When a surface is edited outside this repository, record the observation date here — this file records what is live, and stale observations are worse than none.
