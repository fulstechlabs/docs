# Docs dependency security — JEditor submission prerequisite

Relates to [JEditor194](https://github.com/fulstechlabs/jira-cloud-jeditor-forge/issues/194)
and its [independent reassignment](https://github.com/fulstechlabs/jira-cloud-jeditor-forge/issues/194#issuecomment-5969891046).
Baseline docs main: `10eacf5ae164ac2cc2ddc8c58905186f542ff652`.
Assessment date:2026-10-03. This is internal platform evidence, not public legal
documentation, a customer release, or security certification.

## Outcome and smallest safe scope

Update only direct Astro7.1.6→**7.2.8**, the first release fixing both its AVIF
and base-path advisories. Keep Starlight0.41.6, check0.9.6, TypeScript5.9.3,
content, sidebar, redirects, theme, Astro config, workflows and release route.
Refresh only named vulnerable transitive packages within compatible ranges.
The lock necessarily includes Astro's compiler/Markdown/helper/font dependency
closure and Sharp native binaries/libvips, plus SVGO's selector dependencies;
these are not new product features or a blanket latest/force update.

Seven baseline package findings are removed, including the critical AVIF
finding. **npm audit remains exit1 with5high affected package nodes**, all
propagation of the single unpatched http-cache-semantics advisory. This is
neither zero findings nor five independent new vulnerabilities. Audit initially
reported8nodes(1critical/7high); an intermediate Astro-only refresh reported10high,
then the targeted transitive refresh reduced it to5high. No intermediate result
is hidden or misrepresented as final success.

Do not run npm audit fix --force: its current suggestion downgrades Astro to
2.10.9/Starlight0.8.1 to remove the cache dependency, which would be a breaking
and unrelated platform rollback. Current Astro7.3.5 still depends on the same
unpatched cache library and is not a solution to that residual finding.
No override, scanner exclusion, allowlist, audit suppression or vendor patch.

## All eight baseline affected packages

| Package / baseline | Final lock | Finding and disposition |
| --- | --- | --- |
| Astro7.1.6 |7.2.8| [AVIF RCE](https://github.com/advisories/GHSA-26w7-cxv4-gfx2) (<7.2.8) and [base path boundary](https://github.com/advisories/GHSA-376h-93r7-7g6f) (≤7.2.3) patched; cache advisory remains transitive. |
| Sharp0.35.3 |0.35.5| [libheif vulnerabilities](https://github.com/advisories/GHSA-rgj7-g3m4-5g8c), patched ≥0.35.4; platform binaries/libvips advanced consistently. |
| devalue5.9.0 |5.9.4| [malformed-input DoS](https://github.com/advisories/GHSA-9rgm-9g3h-6x36), [shared memory](https://github.com/advisories/GHSA-j22f-vq7h-c4qm), [sparse-array CPU](https://github.com/advisories/GHSA-hx4r-w6wj-j8fg), [string expansion](https://github.com/advisories/GHSA-mcm9-63f2-9j32), [eager allocation](https://github.com/advisories/GHSA-wf3x-273g-mvxv), [async rejection](https://github.com/advisories/GHSA-x5rw-q4pp-hg5g), [key coercion](https://github.com/advisories/GHSA-4q55-j62x-fr9h); all baseline ranges end before5.9.3. |
| fast-uri3.1.5 |3.1.8| [IDN](https://github.com/advisories/GHSA-5jgf-p345-68v8), [IPv6](https://github.com/advisories/GHSA-f65p-4m7j-42xc), [decoding](https://github.com/advisories/GHSA-fph4-wmhf-6fwf), [scheme](https://github.com/advisories/GHSA-jqff-g426-hqxp), [port](https://github.com/advisories/GHSA-qw65-cvwx-89v3), [host case](https://github.com/advisories/GHSA-hrr3-gc8f-f4qj); all patched by3.1.8. Dev language-server→AJV dependency, not a new public proxy. |
| js-yaml4.3.1 |4.3.2| [merge CPU amplification](https://github.com/advisories/GHSA-2883-xcg3-v3hh), patched ≥4.3.2; all locked instances verified. |
| nanoid3.3.17 |3.3.19| [zero-size custom generator loop](https://github.com/advisories/GHSA-2v37-7h3g-55p8), patched ≥3.3.18; PostCSS transitive. |
| SVGO4.0.2 |4.1.0| [namespace/control-character links](https://github.com/advisories/GHSA-w27v-7q3p-w38r), [foreignObject sanitization](https://github.com/advisories/GHSA-4vpr-x523-8j87), patched ≥4.1.0. |
| http-cache-semantics4.2.0 |4.2.0| [CVE-2026-93748 / max-stale shared-cache disclosure](https://github.com/advisories/GHSA-ch52-4w7c-c8xp). **No published patched version**, retained openly with the scoped reachability evidence below; reviewer acceptance required. |

Baseline/final full audit JSON and registry dependency inventories are preserved
outside the repository in `/tmp/jeditor-194-followup-evidence/`.
Final propagated nodes: http-cache-semantics, Astro, @astrojs/mdx,
astro-expressive-code, @astrojs/starlight. Only the first has an underlying
remaining advisory; the others report its dependency propagation.

## Actual reachability, not “static therefore safe”

### AVIF / Sharp

Current config uses Astro's default Sharp service. `GuideFigure.astro` uses
actual `astro:assets` Image with repository-imported PNGs; Markdown images also
optimize during build. This is a **reachable native decoder in build/dev**, not
an absent dependency. No authored `.avif` asset was found, but extensions alone
are not a security boundary. A malicious contributor/build input could reach
the decoder: it is patched, not waived as static-only or currently unused.

The new executable guard creates a benign2×2AVIF and sends it through the actual
patched Astro Sharp transform, asserting a valid2×2PNG result. No malicious
payload, exploit, untrusted download or live customer input is used. This smoke
is functional execution, not independent exploit-resistance certification.

### Unpatched cache library

Inspected installed Astro `dist/assets/build/remote.js` and redirect helper:

- The only Astro JS import of http-cache-semantics is the build-time remote
  image helper. It constructs policies to calculate `storable/timeToLive`.
  It does **not** use shared-client cache lookup/revalidation methods such as
  `satisfiesWithoutRevalidation` or `responseHeaders`.
- `loadRemoteImage` creates a fresh anonymous Request from the source URL.
  Conditional refresh sends only If-None-Match/If-Modified-Since, with no
  incoming user Cookie/Authorization/max-stale. Output contains image bytes,
  expiry and validators, not retained response Set-Cookie/session credentials.
- The effective resolved project config is static, no adapter; app source has
  no pages/server routes, middleware, actions, live loaders, session/cookie
  access or fetch customization. Remote image domains/patterns are empty;
  unsafe SVG processing is false. Current dev/preview defaults are localhost,
  not all-interface/public service; temporary smoke explicitly uses127.0.0.1.
- The reviewed Pages workflow uploads **dist only** to GitHub Pages, not
  node_modules or a Node server. Built artifact has static HTML/assets, no
  server/worker/image endpoint or HTML references to on-demand `_image`.
  Repository content and public imported assets, not per-user authenticated
  responses, are its build inputs.

Together this bounds the advisory's **cross-user session-cache/max-stale attack
path** for the current static publication architecture. It does not patch the
library or prove every possible Astro/dev/SSR usage safe. Any public dev server,
SSR adapter, authenticated remote assets/cache, live routes/session handling,
new image allowlist or upstream cache-method change invalidates this assessment
and requires re-review. No publication approval is inferred here.

## Regression and validation

`npm run audit:build` now runs the existing link audit **and**9new security
tests, so both existing validation and manual pre-publication workflows invoke
the bounded-model guard without a workflow change. Tests inspect effective
Astro config and installed/locked patched versions; execute actual upstream
remote load/revalidation/redirect/cookie handling with synthetic fetch; exercise
actual patched Sharp; inspect application source and built artifact. They fail
closed on the bounded assumptions above and do not suppress npm audit.

Initial local validation: Node24.14.1; locked install;17publication guards and
9security casesPASS/0fail/0skip; Astrocheck0errors/0warnings/0hints;175-pagebuild
with398imageoptimizations;33518href/srcreferences across215HTMLfiles PASS.
This branch excludes the3new JEditor pages in content PR62;175/215 is expected,
not a silent removal from its178/218 content build.

Rendered smoke on the built local site: Time in Status GuideFigure's WebP loads
(naturalWidth880) at1280desktop and390mobile, document width equals viewport;
JEditor overview at390 and actual Next navigation→legacy create-field page at
1280 render normally. Three nearby legacy images loaded; four offscreen lazy
images were not yet requested, **not** claimed all-image visual acceptance.
No product/content copy was changed here. Temporary viewport reset, owned tab40
closed and fresh IAB/MCP inventories empty; three user Chrome tabs preserved.
Preview daemon stopped/status verified before final coding/build checks.

Full exact **committed** head gate is required again before push/PR; final
source identity and results are recorded in the PR/issue handoff, not guessed
in this report. Public deployment remains independently review-gated. Keep
accepted-content PR62 open until this platform change integrates normally;
then update its base/head and repeat its complete checks/publication review.
Privacy stays a non-effective legal draft; historical Forge issuer receipts,
Sharing, exact Marketplace target and submission remain separate unresolved gates.

Read-only missing-path/glob searches were corrected without state changes.
Native Mac remained locked, but IAB rendering/inventory worked. No hidden test
failure, destructive install, public deploy, auth weakening or broad platform
rollback. The earlier full app security gate is separate from this docs gate.
