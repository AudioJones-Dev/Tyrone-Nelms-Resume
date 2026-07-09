---
title: Architecture
---

# How This System Works

This site is the public surface of a **Professional Operating System**: a version-controlled repository that treats a professional identity as a governed knowledge system rather than a collection of disconnected documents. The full pattern is documented, deliberately free of any personal facts, in [`docs/architecture-pattern.md`](https://github.com/AudioJones-Dev/Tyrone-Nelms-Resume/blob/main/docs/architecture-pattern.md) — this page is the short version.

## The Layer Model

```text
1. CANONICAL FACTS        what is true
        │
2. STRATEGIC FRAMING      how the truth is presented
        │
3. DERIVED ARTIFACTS      resumes, bios, statements, profiles
        │
4. DEPLOYMENT TARGETS     this site, LinkedIn, sent PDFs
```

Information flows one direction: downstream layers read from upstream layers, and no layer may introduce facts. Resumes are assembled, not authored. This site is layer 4 — nothing here is a source of truth.

## Evidence Tiers

Every claim is classified: **Tier A** (verified and specific), **Tier B** (verified, qualitative), **Tier C** (asserted somewhere, unverified). Tier C claims appear nowhere public — including this site — until evidence exists. A claim's tier rises only on documented evidence, never on repetition.

## Governance Gates

Exports require recorded content review (enforced by an allowlist in the export script). Case studies require client approval, documented evidence, and confidentiality review *before drafting*. Open questions produce omissions, not placeholders.

## Why Bother?

Because the alternative is drift: dates that disagree between resume and profile, claims that inflate a little with each retelling, an old metric surviving in a forgotten file. A governed system makes consistency structural — and it demonstrates, rather than asserts, how I approach documentation, evidence, and AI-assisted work for clients.

The pattern is generic and reusable. If you want to build one for yourself, start with the [blueprint](https://github.com/AudioJones-Dev/Tyrone-Nelms-Resume/blob/main/docs/architecture-pattern.md).
