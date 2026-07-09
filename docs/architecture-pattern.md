# The Professional Operating System Pattern

A reference architecture for evidence-based professional knowledge management: treating a professional identity as a governed, version-controlled knowledge system rather than a collection of disconnected documents.

This document is deliberately generic. It contains no facts about any individual and could be lifted into a template repository or product doctrine unchanged. This repository is one implementation of the pattern.

## The Problem It Solves

Professional artifacts — resumes, profiles, bios, proposals — are conventionally maintained as independent documents. They drift: dates disagree between the resume and the profile, a claim gets embellished in one place and not another, an old metric survives in a forgotten file, and nobody can say which version is true. The pattern replaces document maintenance with **system maintenance**: one governed record, many generated surfaces.

## Layer Model

Information flows in one direction. Every layer may read from the layers above it; no layer may introduce facts.

```text
1. CANONICAL FACTS        what is true
        │
2. STRATEGIC FRAMING      how the truth is presented
        │
3. DERIVED ARTIFACTS      the documents themselves
        │
4. DEPLOYMENT TARGETS     where the documents live
```

### 1. Canonical facts layer

The single source of truth: chronology (employers, titles, dates), skills, credentials, accomplishments, and per-engagement source records. Properties:

- Every entry carries a **verification status** (verified / needs-verification / current-context), not just content.
- Uncertainty is recorded, never resolved by guessing — fuzzy dates stay marked approximate; conflicting sources are preserved side by side with notes.
- Resolved decisions (e.g., "use year-only dates for role X") are logged in the canonical layer so downstream artifacts stop re-deciding them.

### 2. Strategic framing layer

Positioning doctrine that governs *presentation* without adding facts: the career narrative, positioning pillars, audience framing, voice and tone rules, a title system, an achievement library tiered by evidence, and interview/story preparation. Properties:

- Framing files cite canonical sources for every factual reference.
- A **derivation map** states explicitly which artifact draws framing from which file — drift becomes a detectable rule violation instead of an accident.

### 3. Derived artifact layer

The generated surfaces: resume variants per target role, profile copy, bios per context, capability statements per service line. Properties:

- Artifacts are **assembled, not authored** — new claims enter through the canonical layer or not at all.
- Each artifact declares its review status; unreviewed artifacts are structurally blocked from export (see governance gates).
- Variants differ by emphasis and selection, never by contradiction.

### 4. Deployment targets

External surfaces — a live profile, a website, a sent PDF — are **deployments of repository files**, not independently edited copies. Edits happen in the repository first, then get applied outward. A deployment-status table records what is live versus drafted, making profile drift visible.

## Evidence Tiers

Every claim is classified by evidence strength, and the tier controls where it may appear:

| Tier | Definition | Permitted use |
|---|---|---|
| A | Verified and specific (named recognition, documented scope) | Anywhere, including exports |
| B | Verified but qualitative | Anywhere, phrased qualitatively |
| C | Asserted somewhere but unverified (typically metrics) | Nowhere public, until evidence exists |

Two operating rules make the tiers real: a claim's tier can only be *raised* by documented evidence, never by repetition or plausibility; and a third party repeating a Tier C claim (a recommender, an old document) does not verify it for first-party use.

## Governance Gates

Gates are conditions, written down in advance, that block an action until met — enforced structurally where possible (allowlists in code), procedurally otherwise:

- **Export gate:** artifacts export only after recorded content review; the export tool carries an explicit allowlist that must match the recorded statuses.
- **Publication gate (case studies / client work):** written approval + documented evidence + confidentiality boundary review + metric discipline, all before drafting specifics.
- **Claim gate:** Tier C content is excluded from every public surface, and the exclusion itself is documented so it reads as discipline, not omission.
- **Decision gate:** open questions (an unchosen title, an unconfirmed URL) are tracked in one place and surfaces omit the item rather than shipping placeholders.

## Export Pipeline

Derived artifacts become deliverables mechanically: plain-text sources (Markdown) converted to distribution formats (PDF/DOCX/HTML) by a repeatable script, run locally and in CI. Doctrine:

- Generated binaries stay out of version control; CI publishes them as build artifacts.
- The pipeline enforces the export gate (allowlist), validates its own output (a converter that exits cleanly on failure is assumed guilty), and names outputs by variant and date.
- Styling lives in the pipeline; content questions belong to the sources.

## Public/Private Boundary Rules

Decide visibility **before** content exists, not after:

- If the repository is public, internal notes are public — pipeline entries, TODOs, and open questions are all externally visible. Anything identifying a third party clears its gates before it is written down at all.
- Names already public in the canonical record may appear elsewhere in the repository; identities of clients and counterparties may not, until approved.
- High-churn environmental intelligence (companies researched, contacts, negotiations) belongs in a **separate private layer**, never in the public identity system. The identity system describes the subject; the intelligence layer describes the environment. They have different change rates, different audiences, and different visibility — separating them keeps the identity system stable and publishable.

## Review Workflow

Every change lands through the same loop:

1. **Branch per intent** — one branch per coherent change (content pass, build tooling, terminology), never mixed.
2. **Draft PR** with an explicit account of what changed, what was deliberately excluded, and which gates were checked.
3. **Owner strategic review** — accuracy, positioning, scope. The owner is the only party who can accept a factual claim.
4. **Automated review** — mechanical and consistency findings; internal-inconsistency catches (a file violating its own stated rule) are treated as real defects.
5. **Merge** only after strategic sign-off, with review findings either applied or explicitly declined with reasons on the record.

The changelog records every addition and decision; release history is never rewritten, including superseded project names.

## Anti-Patterns

- **Editing a deployment.** Fixing the live profile or an exported PDF directly. The correction evaporates on the next generation; the drift returns.
- **Confidence inflation.** "Supported X" becoming "Led X" between drafts. If the canonical record didn't change, the verb doesn't either.
- **Placeholder shipping.** Publishing a surface with `TODO` markers or guessed values because it was "mostly done." Omit the item; track the question.
- **Metric laundering.** An unverified number gaining credibility by appearing in many places, or being cited back from a document that originally copied it.
- **History rewriting.** Renaming or editing past changelog entries to match current framing.
- **Precision theater.** Inventing exact dates for genuinely fuzzy history. False precision is a worse look than honest approximation.
- **One mega-document.** Collapsing layers into a single "master" file — it destroys the ability to review facts and framing separately.
- **Gate erosion.** Adding "just this once" exceptions to export or publication gates. Gates only work if the exceptional path is also written down.

## Minimal Implementation Checklist

A new implementation needs, in order: (1) a canonical chronology with verification statuses; (2) written contribution rules (no fabrication, canonical precedence, uncertainty markers); (3) a positioning/framing document; (4) one derived artifact assembled from the above; (5) an export gate; (6) a changelog. Everything else — variant sets, deployment surfaces, pipelines, intelligence layers — is additive.
