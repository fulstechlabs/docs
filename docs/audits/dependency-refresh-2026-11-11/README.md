# Shared docs dependency refresh — 2026-11-11

Owner: [docs issue 54](https://github.com/fulstechlabs/docs/issues/54).
Discovered while preparing [Markdown Forge submission readiness](https://github.com/fulstechlabs/confluence-cloud-markdown-forge/issues/49).
This is docs-platform maintenance, not a new scan result for the Forge plugin.

## Baseline and change

Base main: `b73818fff2bc52f2b8474875a2ae59b1877d74c6`.
A clean install and npm advisory audit reproduced eight affected package entries:
four High and four Moderate, zero Critical. Astro was pinned to 7.2.8.

Astro is now pinned to 7.4.8, within the same major. Its supported dependency
ranges and an ordinary `npm audit fix` resolve the remaining advisory entries.
No forced fix, override, security-rule suppression or dependency downgrade is used.
The upstream minor update also changes Astro compiler/Markdown transitive packages;
the full site build and representative browser checks below cover compatibility.

| Package | Baseline | Candidate |
| --- | --- | --- |
| astro | 7.2.8 | 7.4.8 |
| fast-uri | 3.1.8 | 3.1.9 |
| postcss-selector-parser | 6.1.4 | 6.1.6 |
| smol-toml | 1.7.1 | 1.9.1 |
| source-map-js | 1.2.1 | 1.2.2 |
| undici | 8.11.2 | 8.12.4 |
| vite | 8.2.0 | 8.3.7 |
| zod | 4.4.3 | 4.6.7 |

The dependency guard inventories every installed/locked copy against the assessed
patched minima. Two new behavioral regressions exercise the actual installed Astro
JSX renderer and transition serializer with synthetic closing-tag/CSS-delimiter
payloads and legitimate-content controls. They do not execute attacker code or
claim that this static site accepts such content from a user.

Primary references: [Astro 7.4.8 release](https://github.com/withastro/astro/releases/tag/astro%407.4.8),
[JSX script/style advisory](https://github.com/withastro/astro/security/advisories/GHSA-98hj-9722-w3j8),
[transition CSS advisory](https://github.com/withastro/astro/security/advisories/GHSA-mpr7-6m5w-76rw).
The machine-readable audit summaries and gate exits are retained beside this report.

## Verification

Node 24.22.1; clean `npm ci` from the committed candidate lock.

- `npm run check`: zero errors, warnings or hints.
- `npm run test:publication`: 17 tests pass.
- `DOCS_SITE_URL=https://docs.fulstech.com DOCS_BASE_PATH=/ npm run build`: complete.
- `DOCS_BASE_PATH=/ npm run audit:build`: all local links/assets pass; 15 dependency/security tests pass.
- `npm audit --json` and `npm audit --omit=dev --json`: both zero findings at audit time.
- `git diff --check`: pass.

Local Chrome preview used `127.0.0.1:4322` and the normal 1440px viewport.
Home, Markdown Cloud Usage, Better Pages Getting Started and Issue Templates
Overview rendered; navigation and the Pagefind search interaction worked.
Searching `issue templates` returned 23 results; following its first product title
opened the corresponding overview, with its heading/table/images intact.
This is representative compatibility review, not an exhaustive per-page or mobile pass.

Screenshots show the local docs candidate, not a deployed website or current
plugin behavior:

- [Markdown Usage](markdown-usage-desktop.png): existing Connect-era wording and screenshots are retained. This explicitly does **not** document the Forge editor; product docs need separate release reconciliation.
- [Better Pages Getting Started](better-pages-start-desktop.png): existing guide and layout render.
- [Search results](search-results.png): actual local Pagefind results.
- [Issue Templates Overview](issue-templates-overview-desktop.png): destination after following search. Previously opened navigation groups can remain expanded.

The task-owned preview tab was closed and a fresh inventory showed only the two
unrelated pre-existing tabs. The local preview server was explicitly stopped.

## Residual assessment and publication boundary

Zero npm inventory findings is not a complete-security claim. The existing
`http-cache-semantics` GHSA-ch52 max-stale issue remains observable in the assessed
4.3.0 library with synthetic data. Its characterization and the site-specific
static/no-authenticated-runtime/no-remote-allowlist guards remain unchanged and
pass. This update does not call that issue patched or waive its reassessment if
server routes, authentication, remote images or dependency behavior change.

GitHub's separate default-branch alert inventory may update asynchronously and
must not be relabeled cleared from this local audit. No public deployment,
release promotion, Marketplace operation or Forge app change is performed here.
Any later publication follows reviewed main-to-release promotion and manual
deployment of the exact release SHA. Markdown privacy draft PR 68 remains a
separate unpublished legal/product review gate.
