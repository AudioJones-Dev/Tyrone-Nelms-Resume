# Case Studies

Registry and pipeline for public-facing case studies. No case study is published — or drafted with specifics — until its evidence and approval gates are met.

Framing derives from [`career-positioning.md`](career-positioning.md). Facts must come from documented client work, not memory.

## Publication Gates

A case study may be published only when ALL of the following hold:

1. **Client approval** — explicit, written permission for the client to be named, or the study is fully anonymized in a way the client has approved.
2. **Evidence** — every stated outcome traces to a document, screenshot, analytics export, or client statement on file (future `evidence/` folder).
3. **Boundary review** — no confidential process, pricing, or client-internal detail, per the public/private rules in [`CONTRIBUTING.md`](../CONTRIBUTING.md).
4. **Metric discipline** — numbers appear only if verified; otherwise the study is qualitative.

## Candidate Pipeline

Status values: `idea` → `evidence-gathering` → `client-approval` → `drafting` → `published`.

| # | Candidate | Source engagement | Status | Blocking gate |
|---|---|---|---|---|
| 1 | AI-enabled operations system for a founder-led service business | AJ Digital client work | idea | Client selection + approval + evidence |
| 2 | Workflow/project-management consolidation (ClickUp/Asana) for a client team | AJ Digital client work | idea | Client selection + approval + evidence |
| 3 | Content and ad management supporting brand visibility and conversions | AJ Digital client work | idea | Analytics evidence + client approval |
| 4 | Field-service operations support for an accessibility business | Florida Ramp & Lift | idea | Company approval; public scope review flagged in `experience/florida-ramp-lift.md` |
| 5 | Event production operations (photo booth / media delivery at scale) | Miami Spin 360 | idea | Company approval |

None of the above has named clients, dates, or outcomes on file yet. Do not draft specifics until a row reaches `drafting`.

## Case Study Template

Use this structure when a candidate reaches `drafting`:

```markdown
# [Client type] — [Outcome-oriented title]

- Status: drafting | published
- Client: [named with approval | anonymized profile]
- Engagement: [service line, period]
- Approval: [link/reference to written approval]
- Evidence: [links/references to evidence files]

## Context
## Problem
## Approach
## What was built or changed
## Results
(verified numbers only; otherwise qualitative outcomes)
## What this demonstrates
(tie back to positioning pillars in career-positioning.md)
```

## Anonymization Rules

- Anonymized clients are described by type, size band, and industry only ("a Florida-based home-services company").
- Never combine anonymized details specific enough to identify the client.
- Anonymization does not lower the evidence bar — outcomes still require documentation.

## TODO

- Create the `evidence/` folder structure when the first candidate enters `evidence-gathering`.
- Draft a one-paragraph client-approval request template.
- Decide publication surface (GitHub Pages portfolio vs. AJ Digital site) — affects tone and depth.
