# Surface Reconciliation — 2026-08-11

Audit of the live public surfaces against the canonical record. Findings only; no canonical content was changed. Each finding names the conflicting sources so the correction can be made once, in the right file.

Surfaces audited: `tyronenelms.com` (home, about, work, ventures) and `audiojones.com` (home, about, solutions). Records audited: `docs/career-positioning.md`, `docs/professional-brand.md`, `docs/target-roles.md`, `docs/certifications.md`, `docs/achievement-library.md`, `docs/accomplishments.md`, `docs/case-studies.md`, `docs/career-history.md`, `bios/`, `linkedin/`, `resumes/README.md`.

## Summary

The employer-facing surface is in **better** shape than expected. Dates, titles, credentials, and the one published metric all match canon, and `tyronenelms.com/work` labels project maturity more rigorously than most portfolios do. The material problems are in three places: a stale pre-launch TODO that is silently degrading live applications, a metrics conflict on the commercial brand surface, and one direct contradiction between the two sites.

| # | Finding | Severity | Where the fix belongs |
|---|---|---|---|
| 1 | Portfolio URL omitted from every resume and bio — 7 files still say "pending" | **High** | `resumes/README.md`, `docs/professional-brand.md`, +5 |
| 2 | ResponseOS described as pre-alpha on one site, sold as an operating service on the other | **High** | `audiojones.com` or the product record |
| 3 | audiojones.com publishes Tier C metrics the canon bars from public artifacts | **Medium-High** | `docs/achievement-library.md` unlock, or the site |
| 4 | Site target roles omit operations management — 40% of the search allocation | **Medium** | `tyronenelms.com/about` |
| 5 | AJ Digital legal form resolved on the site, still "open question" in canon | **Medium** | `docs/career-history.md`, `docs/professional-brand.md` |
| 6 | LinkedIn Featured gate "site live + URL confirmed" is now met | **Medium** | `linkedin/featured.md` |
| 7 | ARO, Audio Jones, and Eightee20 Society are public but unregistered | **Low-Medium** | `docs/career-history.md`, evidence index |
| 8 | "15+ years" — canon-approved and supportable, absent from the site | **Low** | `tyronenelms.com` |
| 9 | Possible placeholder identity on a live commercial page | **Low** | `audiojones.com/about` |
| 10 | Florida Ramp & Lift named publicly while pipeline gate reads "company approval" | **Low** | `docs/case-studies.md` |

## 1. The portfolio URL is missing from everything you send — High

`tyronenelms.com` is live. Seven files still treat the portfolio URL as unconfirmed:

- `resumes/README.md:21` — "LinkedIn and portfolio URLs are omitted until confirmed"
- `docs/professional-brand.md:11` — "LinkedIn / portfolio URLs: pending confirmation — omit rather than placeholder"
- `docs/professional-brand.md:83` — "Confirm LinkedIn and portfolio URLs, then add them here and to all surfaces in one pass"
- `docs/career-history.md:55` — "Confirm LinkedIn and portfolio URLs"
- `linkedin/about.md:27` — "Add the portfolio URL here once confirmed"
- `bios/short-bio.md:20` — "Add the LinkedIn or portfolio URL as a byline link once confirmed"
- `bios/executive-summary.md:40` — "Add LinkedIn/portfolio URLs when confirmed"

**Consequence:** every resume variant generated from this repository omits the portfolio link. If applications have been going out against these files, they have been going out without the strongest differentiator in the portfolio — a governed, maturity-labeled evidence surface that most applicants for these roles cannot produce. The rule that caused this was correct when written ("omit rather than placeholder", before a site existed); it simply outlived its condition.

This is the single highest-value item in the audit and the cheapest to fix.

## 2. ResponseOS contradiction between the two sites — High

- `tyronenelms.com/work`: ResponseOS — status **"Pre-alpha"**, "Internal pre-alpha revenue-recovery architecture: multi-tenant modelling, tenant isolation, event and audit concepts", explicitly **"No live integrations or customers."**
- `audiojones.com`: ResponseOS presented as a service line — "Revenue Recovery Infrastructure" that handles lead capture, qualification, and recovery of stalled prospects.

One surface says pre-alpha with no customers; the other sells it as operating infrastructure. Both are publicly reachable and both are linked to the same person. A prospective employer or client who reads both sees a contradiction, and the pre-alpha disclosure is the one that makes the sales page look overstated.

This is the most consequential inconsistency found, because it is a genuine factual conflict rather than a framing difference. Resolving it requires deciding which claim is accurate and correcting the other — a decision only you can make.

## 3. audiojones.com metrics versus Tier C — Medium-High

The site publishes, under a "Proof / Metrics" heading:

- "CAC Reduction ↓ 37% — Customer acquisition cost"
- "Pipeline Growth ↑ 28% — Qualified pipeline per quarter"
- "Conversion Rate ↑ 42% — Lead-to-call conversion rate"

**In fairness, these are caveated more carefully than typical marketing.** The section carries "Numbers from in-flight engagements. Names withheld until publication consent," plus "Representative system outcomes. Actual results depend on implementation, offer, market, and operational maturity," and a no-guarantee disclaimer. This is not presented as a guaranteed or averaged result.

The conflict is with this repository's own stricter standard, in three places:

- `docs/accomplishments.md` → Metrics to Verify: "Any revenue, lead generation, response time, cost savings, or efficiency metrics from AJ Digital client work."
- `docs/achievement-library.md` → Tier C: "Any AJ Digital client revenue/lead/response-time metrics", unlock condition **"Client-approved case study"**. Tier C is defined as "Excluded from all public artifacts until evidence exists."
- `docs/case-studies.md` → Publication Gate 1 (client approval) and Gate 4 ("numbers appear only if verified; otherwise the study is qualitative").

The site's own disclaimer — "Names withheld until publication consent" — states that publication consent has not been obtained. That is precisely the Tier C unlock condition, documented as unmet on the surface that publishes the numbers.

Note also that `docs/professional-brand.md` Channel Rules already claims authority over this surface: the "AJ Digital site / proposals" row reads "Case studies only per `case-studies.md` gates." The AJ Digital site was never outside the brand system.

**Two coherent resolutions.** Either treat the commercial brand surface as genuinely outside the career evidence chain and say so explicitly in the Channel Rules — accepting that a stricter standard governs employment materials than marketing — or bring the figures through the Tier C unlock and publish them with evidence. What should not persist is a canonical rule that the surface silently contradicts. Independently of which you choose, these figures stay out of resumes, briefs, and interviews.

## 4. Site target roles omit 40% of the search — Medium

`tyronenelms.com/about` lists target roles: Senior Business Systems Analyst, Business Systems Consultant, Operations Systems Architect, Business Systems Architect, Implementation Manager, Solutions Consultant.

`career-os/strategy/search-strategy.md` allocates **40% of targeting to Business Operations / Operations Manager** — the largest single block — and `docs/target-roles.md` Tier 2 lists Operations Manager, Business Operations Manager, and Project Manager.

No operations-management or program-management title appears on the site. The largest segment of the search is invisible on the primary employer-facing surface. A recruiter screening for an Operations Manager finds an architecture-and-analysis portfolio and no signal that the role is wanted.

Minor related point: the site mixes Tier 1 and Tier 2 titles without distinction (Solutions Consultant is Tier 2 in canon), and uses "Operations Systems Architect" where canon's approved umbrella is "Operations & Business Systems Architect".

## 5. AJ Digital legal form — Medium

- `docs/professional-brand.md:9` — 'Practice / company brand: **AJ Digital** (presentation as company vs. brand vs. practice is an open question in `career-history.md` — until resolved, use "AJ Digital" without a legal-form suffix)'
- `docs/career-positioning.md` Open Questions — still tracks this as unresolved.
- `audiojones.com/about` — "Audio Jones is the operating brand of **AJ Digital LLC**."
- `tyronenelms.com/ventures` — "AJ Digital", no legal form. Compliant with the guardrail.

The question canon records as open has been answered publicly: AJ Digital LLC is the entity, Audio Jones is its operating brand. The canonical record should be updated to match the published reality, and the guardrail retired or narrowed. Right now two live surfaces state different things about the same entity.

## 6. LinkedIn Featured gate is now met — Medium

`linkedin/featured.md` lists under **Gated (do not feature yet)**: "AJ Digital website / landing page — Gate: Site live + URL confirmed."

The gate is met; audiojones.com is live. The item can move to Ready Now.

Worth a decision at the same time: that file's ordering rule puts "AJ Digital site (primary CTA)" first. For a job search, the primary Featured item should almost certainly be `tyronenelms.com`, which does not appear in the table at all. Leading a recruiter-facing Featured shelf with a consulting sales site works against the employment objective — the same audience-separation logic recorded in `docs/public-surfaces.md`.

## 7. Public but unregistered — Low-Medium

Named on live surfaces, absent from the canonical record:

- **ARO — execution runtime.** Featured on `tyronenelms.com` home and `/work`, labeled "Internal system" and "Research hypothesis" with "The market thesis is labelled research, not demand." Honestly labeled; simply has no entry in `career-os/evidence/portfolio-index.md` or this repository. Under the rule added in career-os#8, it cannot be cited in an application until registered.
- **Audio Jones** — "creative and consulting identity — music, media production and the editorial systems", principal role. No entry in `career-history.md` or `experience/`.
- **Eightee20 Society** — "A community and culture venture", founding member. The site itself states "no scale, revenue or programming claims are made here." No canonical entry.

Each is well-labeled publicly. The gap is registration, not overclaiming.

## 8. "15+ years" is approved and absent — Low

Canon asserts "15+ years" in `docs/professional-brand.md` (standard bio block and short pitch), `docs/career-positioning.md`, `docs/achievement-library.md`, and `bios/short-bio.md`. The chronology supports it comfortably — TigerDirect begins February 2008.

`tyronenelms.com` states no years-of-experience figure anywhere. This is a canon-approved, verifiable differentiator the primary employer surface is leaving unused. The only finding in this audit where the site under-claims relative to what the record supports.

## 9. Possible placeholder identity — Low

`audiojones.com/about` appears to reference a person named **"Javi"** with an avatar image, without a title or biography. This may be a testimonial, a collaborator, or leftover template content. Flagged for manual review rather than asserted — an unexplained name on a live commercial About page is worth confirming either way.

## 10. Florida Ramp & Lift naming versus the pipeline gate — Low

`docs/case-studies.md` pipeline row 4 lists "Field-service operations support for an accessibility business — Florida Ramp & Lift — status `idea` — blocking gate: Company approval." `tyronenelms.com/work` publishes a named Florida Ramp & Lift entry described as an "Active engagement."

This is probably compliant rather than a violation: the same file's naming rule permits naming FR&L because it "appears on the published resumes — listing them as candidates discloses nothing new," and the site claims no outcomes ("No scale claims"), satisfying Gate 4. The open question is whether a maturity-labeled project description with no outcomes counts as a "case study" under these gates at all. Worth one sentence in `case-studies.md` recording the decision, so the next reader is not left to infer it.

## Verified consistent — no action

These were checked and matched:

- **Employment chronology.** All seven employers and date ranges on `tyronenelms.com` match `docs/career-history.md`, including the consolidated AHLO entry (2006–2007, 2019–2023). The site uses year-only dating, matching the approved decision to keep fuzzy older dates approximate.
- **Certifications.** The three Google professional certificates and "American Academy — High School Diploma, 2005" match `docs/certifications.md` exactly. The PCMA crisis-prevention credential, marked "needs verification" in canon, is correctly absent from the site.
- **The one published metric.** "over 99% monthly adherence" matches Tier A "99%+ adherence every month (Alorica)" — verified and safe to publish.
- **Default title.** "Operations & Business Systems Architect" matches the canonical umbrella title.
- **Location.** "Miami, Florida" matches `docs/professional-brand.md` ("Miami / Hialeah, Florida"). *Correction to an earlier assumption: the site does not conflict with this repository on location. The divergence is with `career-os`, which plans around Southwest Florida relocation (Fort Myers, Cape Coral). The outlier is the search strategy, not the site.*
- **VPL Flow boundary.** The site's "Specified architecture" label matches the operator-approved boundary recorded in `case-studies.md` on 2026-08-10, which requires stating that no application code or production deployment is claimed.
- **Maturity discipline on `/work`.** All seven projects carry explicit status labels — "Active engagement", "Internal system", "Research hypothesis", "Pre-alpha", "Specified architecture" — with disclaimers including "No scale claims" and "No live integrations or customers." This closely tracks the maturity vocabulary in `career-os/architecture/repository-boundaries.md` and is stronger evidence discipline than the canonical record requires.

## Suggested order of work

1. Resolve the portfolio URL across all seven files in one pass (#1) — highest impact, lowest cost, unblocks every future application.
2. Decide the ResponseOS truth and correct the losing surface (#2) — the only outright factual contradiction.
3. Decide the audiojones.com metrics posture and record it in Channel Rules (#3).
4. Add operations-management titles to the site's target roles (#4).
5. Close the AJ Digital entity question in canon (#5) and update the Featured shelf (#6).
6. Register ARO, Audio Jones, and Eightee20 Society (#7).

Items 1, 5, 6, and 7 are canonical-record edits and can be made in this repository. Items 2, 3, 4, and 8 require changes to sites whose source is not in either repository.
