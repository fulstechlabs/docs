# Better Pages Release 13 visual review — 2026-10-01

## Release 13.2 reconciliation — 2026-10-02

Product owner authorized release→update affected docs→safe publish→ChatGPT
public-site review in product #58 and #46. The original accepted visual package
below remains historical evidence; its old Tabs/HTTP400 warnings are superseded
in the current customer pages, not erased from this audit.

Release 13.2 exact source `36b49940322d66bfe7e0c19be7d7d56d662587b5`, annotated
`release-13.2`, Forge/Marketplace 2.4.0, build 2001030 PUBLIC. Production deploy
SUCCESS at 2026-10-01T19:32:20.403Z; authorized licensed FT dev4 Confluence
installation `da649752-2e33-414f-b06f-ced9ff522134`, environment
`a8cf910e-f0fd-4db1-a56f-7dc318bc4f13`, same app ID as below.

Chrome DOM and native Chrome screenshots verified old malformed pages 53379073
and 53641218 without page writes, fresh Resource hub 53673999 direct Composer
V1/V2 with native history, group Save/Update/cold/reopen and independent private
Save draft 53674030. Actual pixels were inspected and curated Drive metadata
verified. Complete checkpoint:
https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/issues/58#issuecomment-5939473127

Two new screenshots in `images/release-13.2/`, with byte-identical public copies:

- `composer-published-guides.jpg`: fresh page 53673999 cold reader at V2;
  title, synthetic V2 marker, Guides/Support, Start guide and Working guide
  visible. This is production on a Fulstech test tenant, not customer data.
  It proves the depicted Guides result; separate Support/history evidence is
  in the checkpoint, not inferred from this screenshot.
- `tabs-support-default.jpg`: same page after group Save plus native Update
  (V3) and cold reload; Support selected, Help center card visible. DOM reopen
  separately confirms both names and second default. No claim of all keyboard,
  export or device tests.

Original 47 selected assets and Getting Started's coherent draft→native Publish
example remain unchanged. Added two selected current-result assets, not a
reconstructed UI. Published captions distinguish original Release 13 DEV
authoring examples from Release 13.2 production-test results.

Known Limitations now preserves two bounded cases: old contaminated tab
structure is not auto-rebuilt; Home's original Continue designing result can
retain stale draft context after Publish (HTTP404). Published reader Smart
Designer loads the current version. No new runtime feature/fix was added.

Shared docs infrastructure #59/#60 implements workflow_dispatch-only exact
release SHA, no automatic push publication. Final build/layout/public receipt
is recorded on product #46/#58 and shared #57; new ChatGPT rendered-site review
must not be claimed until performed.

Internal review package for [product issue #46](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/issues/46).
This file is outside the public Astro content tree. Publication is **not
authorized until this final package is reviewed and accepted on the product
issue**. The app's production release has not been changed by this docs task.

## Runtime identity and capture boundaries

- Canonical product release: **Better Pages Release 13**.
- Production repository marker: annotated tag `v13.0.0`, source
  `225a3e46ac854b2e352b7702d80c068d147bdf16`; Forge/Marketplace version `2.2.0`.
- Capture site: `https://fulstech-dev2.atlassian.net`, licensed custom DEV
  environment `better-pages-license-test`, environment UUID
  `9b29ca2c-7e02-4854-9250-472859cf2769`, app
  `5aa85fa0-711a-4bc1-ac3f-6556b03da50f`.
- Deployed DEV source: `de24f9f2117c37a8995455c6eea221d3490c72b6`. Comparing
  `src/`, `static/`, `manifest.yml`, and `package-lock.json` with the production
  tag produced no differences. This is runtime-code equivalence, not full-commit
  identity, production licensing, migration, or storage-continuity evidence.
- New captures below were taken through Chrome on 1 October 2026. They are
  real UI, not recreated product screens. Direct browser capture clips omit
  unrelated navigation/bylines, never relevant warnings or the depicted
  component's state. No offline overlays or UI reconstruction were used.
- Each selected file's actual pixels were inspected. Blank, clipped-result,
  redundant, and warning-obscuring attempts were excluded. Some configuration
  views intentionally show only the relevant portion of a scrollable form;
  they do not claim to show all settings or a completed Save.
- All fixture text, owners, citations, and status are synthetic. No customer
  data, customer incident, current release readiness, or real academic source
  is depicted.
- All 77 screenshot placements link to byte-identical full-size files in
  `public/assets/better-pages/release-13/`. Inline optimized previews fit narrow
  content widths; readers can open the original for small table/toolbar text.
  These public copies preserve pixels and are not edited or reconstructed UI.

### Fixtures

All fresh fixtures are in the John Brown personal space
`~60f95a15d4b2160068393d49` on the DEV site.

| Key | Page ID / title | What was actually done |
| --- | --- | --- |
| F | `69402626` / Formatting examples — Release 13 | Saved rich macro examples, published/updated through Confluence; reader inspected. Inherits the launch-hub introduction/cards from its parent. |
| R | `69533703` / Research notes — Release 13 | Saved paired note/citation/math examples; published and updated through Confluence. Inherits other parent content; captures show only the claimed technical section. |
| G | `69402677` / Product Launch Hub — guided example | Home private blank draft → Find your way → staged review → Save draft → close/reopen same draft → Confluence Publish. Published Plan card successfully opened T. |
| T | `69402654` / Northstar team — Release 13 | Shipped Team homepage template with prompts replaced; Confluence Publish. Image shows its opening section, not the whole template. |
| O | `69533730` / Welcome to Northstar — Release 13 | Shipped onboarding template with prompts replaced; Confluence Publish. Image shows welcome/checklist section. |
| I | `69795848` / Service recovery — synthetic exercise | Blank draft + Project status section. Composer Publish returned HTTP 400; Save draft then normal Confluence Publish succeeded. Added permanently visible native status/owner/update text and updated. Alert dismissed for page-body capture. |
| D | `69402691` / Northstar documentation — Release 13 | Blank draft + Navigation directory; Save draft then Confluence Publish. Not a screenshot of an entire Knowledge base template. |
| N | `69697541` / Navigation and data — Release 13 | Confluence Publish of rich table, two-slide banner, and four Progress macros. Bar chart saved through reader UI and survived a fresh page opening. |
| L | `68648971` / Product Launch Hub | Existing licensed Release 13 demonstration page; published launch-readiness section inspected. |
| S | Space Manager | Read inventory, filter/column controls and preview plans; Back from copy and hierarchy confirmation. **No operation was executed.** |

## Image-by-image provenance and exact claim

Paths in this table are relative to
`src/content/docs/better-pages/confluence-cloud/images/release-13/`.
Fixture keys above supply tenant, environment, source identity, and page.

| File | Fixture / state | Exact visible claim and limit |
| --- | --- | --- |
| `advanced-cards-config.jpg` | F / macro editor | Three-column, left-aligned Plan/Launch/Support card configuration and order controls; no applied style preset. |
| `advanced-expand-config.jpg` | F / macro editor | Release checklist title, Heading 4 and Elevated card options. |
| `advanced-expand-closed.jpg` | F / published reader | Release checklist collapsed. |
| `advanced-expand-open.jpg` | F / published reader | Same checklist expanded, showing scope/owner/rollback text. |
| `button-group-config.jpg` | F / macro editor | Release resources label, horizontal direction, two stored ordered buttons. |
| `button-group-compatibility.jpg` | F / macro editor | Structured compatibility notice retained; this is not a new open-box group. |
| `button-group-reader.jpg` | F / published reader | Open launch hub followed by Read guide. No claim that both destinations were activated. |
| `html-source-config.jpg` | F / macro editor | Launch update HTML source and its readiness paragraph. |
| `html-css-config.jpg` | F / macro editor | Local stylesheet and All media option. |
| `html-policy-preview.jpg` | F / macro editor | Sanitized live preview and administrator-disabled JavaScript notice. |
| `html-reader.jpg` | F / published reader | Same isolated HTML/CSS card; no JavaScript claim. |
| `pop-up-dialog-config.jpg` | F / macro editor | Launch criteria, Medium width, Left content alignment, Review launch criteria trigger. Lower controls continue below capture. |
| `pop-up-dialog-trigger.jpg` | F / published reader | Actual saved trigger before activation. |
| `pop-up-dialog-open.jpg` | F / opened reader modal | Saved scope, ownership, support, rollback rich body and Close controls; no destination choices. |
| `tooltip-config.jpg` | F / macro editor | Plain-text release-owner definition and information-icon preview; lower explanation continues below capture. |
| `tooltip-focus.jpg` | F / published keyboard-focus state | Saved definition visible on focus. Not touch-device or hover-test evidence. |
| `tabs-group-config.jpg` | F / initial new-group editor, before Save | Add tab and Preparation/default/alignment controls. Only first row is visible; **not** a passing saved two-tab result. See blocking discrepancy below. |
| `footnote-pair-reader.jpg` | R / published reader | Real numbered inline Footnote and populated Review notes entry. |
| `bibtex-pair-reader.jpg` | R / published reader | Real numbered citation and populated Example bibliography; citation is explicitly fictional. Search/sort controls are visible, not exhaustive interaction proof. |
| `latex-builder-config.jpg` | R / macro editor | Mixed prose with `$m$`, `$c$`, and `$$E = mc^2$$`, plus format/library controls. |
| `latex-builder-preview.jpg` | R / live editor preview | Variables and centered equation rendered. This is an authoring preview, not a published page. |
| `latex-reader.jpg` | R / published reader | Inline mass–energy relation with correct surrounding spacing and explanatory Builder prose/display equation. |
| `getting-started-destination.jpg` | G / Home before create | Destination/title and explicit Create blank draft for Composer action. |
| `getting-started-workflows.jpg` | G / Composer | Four workflows, Compose a section, No Brand Kit and administrator-disabled AI notice. |
| `getting-started-review.jpg` | G / staged canvas | Product Launch Hub section, Apply to this page, distinct Save draft/Publish controls. Nothing written by preview alone. |
| `getting-started-draft-saved.jpg` | G / successful Save draft | Actual same-page saved-draft confirmation. |
| `getting-started-reopened.jpg` | G / reopened native editor | Persisted editable heading and three cards. Native configuration labels partially overlap the introductory line; not a clean reader result. |
| `getting-started-reader.jpg` | G / published reader | Heading/introduction and Plan/Launch/Support cards on a light Background. Plan destination separately activated and verified; other links/devices not exhaustively tested. |
| `recipe-team-reader.jpg` | T / published reader | Purpose, audience and fictional maintenance owner/review date. |
| `recipe-onboarding-reader.jpg` | O / published reader | Welcome and first-day checklist with meaningful replaced prompts. |
| `recipe-incident-alert.jpg` | I / published page-load alert | Dismissible synthetic recovery notice, not an inline alert or real incident. |
| `recipe-incident-reader.jpg` | I / published reader after dismissal | Always-visible native status/owner/next update, single current stage, Read exercise notes action. Not a complete Incident template or a four-step Progress journey. |
| `recipe-docs-reader.jpg` | D / published reader | Navigation directory with three useful paths. Not the complete Knowledge base template or proof that every link was activated. |
| `product-launch-reader.jpg` | L / published reader | Actual synthetic launch-readiness section and actions, not current release status. |
| `table-config.jpg` | N / macro configuration | Accessible title and rich source table with three detected synthetic data rows. Charts/styles are configured through reader controls, not this form. |
| `table-reader.jpg` | N / published reader | Three readiness rows, search/filter/sort/column/chart/style controls. Search Launch returned 1 of 3; clearing restored 3 of 3. |
| `table-chart-reader.jpg` | N / persisted reader chart | Bar chart with Workstream axis and Checks values 8, 6, 7; fresh page opening retained chart. No claim all chart types were tested. |
| `banner-reader.jpg` | N / published reader, paused | First of two slides, built-in artwork, direct selectors and previous/next/resume controls. Both actual slides selected; links and touch behavior not exhaustively tested. |
| `progress-reader.jpg` | N / published reader | Four step macros aggregated: Plan/Build complete, Validate current, Launch upcoming. No claim every link was activated. |
| `space-manager-filter-columns.jpg` | S / inventory | Formatting examples filter, six selectable columns, owner-profile lookup warning retained. |
| `space-manager-inventory.jpg` | S / inventory | One of 222 published pages selected, status/date and copy destination controls. Profile unavailable is visible; Parent temporarily hidden from table, then restored. |
| `space-manager-copy-preview.jpg` | S / exact plan before write | One-page Copy plan to John Brown below Product Launch Hub, permission-recheck notice, Back/Confirm. Exited with Back. |
| `space-manager-hierarchy-config.jpg` | S / configuration | John Brown destination, Product Launch Hub parent, Documentation starter, four-page indented outline and overrides. |
| `space-manager-hierarchy-preview.jpg` | S / exact plan before write | Launch handbook with three children; nothing written until confirmation. Back selected, no hierarchy created. |

### Verified existing-image reuse

`clean-home.jpg`, `clean-pattern-library.jpg`, and
`clean-styles-in-composer.jpg` are byte-for-byte copies of existing selected
stills in the product repository's `marketplace/demo-13-video/public/` at
`a599bfb17e79ea5feb16668edc4751a793df9ee4`. They depict licensed DEV Release 13
UI on L, not the new G draft. Home is a common entry point; the pattern image
teaches Find your way selection; the styles image depicts published test-kit
roles. They are not evidence that G used a Brand Kit (it did not).

The retained historical `images/13.0/02-template-choice.jpg` and
`04-private-draft-created.jpg` illustrate a **separate template-created draft**,
not G's blank-draft walkthrough. `14-primary-style.jpg` illustrates the
published synthetic Launch primary action style. Actual pixels were reviewed
and the claims remain those of the existing Release 13 source package.
These captures do not prove a new kit publication in this task.

## Page-by-page visual pass

All 19 macro guides now contain a useful actual configuration or result image.
The 11 previously image-less guides have current captures; paired guides
deliberately share a coherent image rather than duplicate fixtures.

| Guide / prior state | Selected visual decision |
| --- | --- |
| Advanced Expand / none | Configuration + same collapsed/expanded result. |
| Button Group / none | Order/configuration + explicit compatibility-mode notice + actual group. |
| HTML / none | HTML/CSS configuration, policy warning, actual isolated reader. |
| Pop-up Dialog / none | Relevant configuration, trigger, opened saved rich modal. |
| Tooltip / none | Plain-text configuration + keyboard-focus result; no unsupported touch evidence. |
| Footnote / none | Inline marker in realistic sentence + same collected note. |
| Footnote Summary / none | Same populated note pair, caption emphasizing collection. |
| BibTeX Reference / none | Numbered fictional reference + actual bibliography. |
| BibTeX Summary / none | Same populated bibliography, no invented real source. |
| LaTeX Inline / none | Formula in actual prose, not an isolated decorative equation. |
| LaTeX Builder / none | Source + live preview + published mixed prose/equations. |
| Advanced Cards / old | Replace old QA editor and single orange-card reader with current grid configuration and G's coherent three-card outcome. |
| Alert / old | Replace old inline panel with actual page-load alert; caption distinguishes presentation. |
| Background / old | Replace old purple panel with G's rich light section; content remains readable. |
| Button / old | Replace decorative isolated button with I's meaningful status/action context. Configuration image omitted because ordinary appearance settings add little to this short guide. |
| Interactive Banner / old | Replace rough header/chrome crop with actual complete two-slide reader, paused-state caption. Existing written authoring steps remain. |
| Progress Bar / old | Replace rough cropped image with complete four-step reader. |
| Table / old | Replace rough image with source configuration, full table and persisted chart; correct instructions to reader chart/style UI. |
| Tabs / old | Remove legacy reader presented as new-group success. Show initial new-group controls only, pending product decision; do not approve publication yet. |

Other pages:

- **Overview:** Home, staged canvas, finished reader; high-level navigation kept.
- **Getting Started:** one coherent G create/save/reopen/publish path; Home and
  pattern selection reuse are explicitly UI orientation, not same-draft proof.
- **Recipes index:** seven full-content-width previews with short outcome
  captions/links; no tiny screenshot column that would make mobile UI illegible.
- **Seven recipes:** T and O template openings; G product/project navigation
  section; L launch output; I written status/action; D directory section; R
  equations and citations. Captions distinguish section examples from complete
  template outputs.
- **Space Manager:** inventory/filter/columns, exact copy plan, hierarchy
  destination/parent/outline and exact nested preview. No risky operations run.
- **Composer / Section Patterns / Home / Brand Styles:** replace relevant old
  broad views with clean verified views; do not pretend No Brand Kit is a styled
  custom-kit flow or conceal disabled AI.
- **Known Limitations:** normalize product release wording to Release 13.
  Historical Git tag and technical platform identifiers remain unchanged.

## Product discrepancies requiring acceptance decisions

1. **Tabs:** new authoring controls accepted Preparation and Launch. Saving
   rich sections, publishing, and hard-reloading rendered **one Overview tab
   with both bodies**. Reopening the saved macro on 1 October showed the legacy
   single-tab editor with Overview. The initial group image is not saved-state
   acceptance evidence. See [actual reader discrepancy](audits/better-pages-release-13-2026-10-01/tabs-reader-observed.jpg).
   Source inspection suggests `DEFAULT_CONFIG.tabs.tabName` is merged into a
   structured configuration, then `tabsConfigIsStructured` rejects it and the
   reader falls back to legacy grouping. This explanation is an **inference**,
   not a tested fix. No product code was changed. Next decision: authorize a
   separate product correction and recapture, or explicitly accept the limited
   configuration-only docs with a suitable customer limitation.
2. **New private draft / Composer Publish:** direct Publish on I returned
   Confluence HTTP 400. Save draft then normal Confluence editor Publish
   succeeded. The illustrated first-success path uses the latter verified
   route. Do not treat this as a passing direct Composer Publish test. Decide
   whether a product follow-up and customer limitation are required before
   accepting the final docs package.
3. **Owner lookup:** Space Manager reports profile lookup problems, retained in
   the image. It is not evidence that owner resolution succeeded for all pages.
4. **Docs deployment safety:** current `.github/workflows/pages.yml` still has
   an automatic `push` trigger on `main`; it does **not** implement the requested
   release/manual-only publication route. Merging this docs PR would trigger
   deployment even without a manual dispatch. Keep this PR **draft/unmerged**
   until the shared docs-platform deployment policy is corrected and accepted.
   This content task does not silently change the cross-product workflow or
   bootstrap `release`. The owning product issue needs to route/authorize that
   shared infrastructure prerequisite before any merge/promotion/publication.

## Validation and handoff

### Review revision — 1 October 2026

[ChatGPT accepted the visual package](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/issues/46#issuecomment-5927261590)
and requested two explicit customer limitations before publication. The Tabs
guide and Known Limitations now state the observed new-group round-trip
failure and recommend ordinary Confluence headings where separate sections
must remain accessible. Composer and Known Limitations qualify direct Publish
on new private drafts and give the verified Save draft → reopen in Confluence
→ normal Publish route. Getting Started already teaches that accepted route.

The captures above remain unchanged; this revision does not recapture or claim
a product correction. Separate product follow-ups are
[Tabs #48](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/issues/48)
and [Composer #49](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/issues/49).
If a fix ships before docs publication, recapture and adjust/remove the affected
temporary limitation. Shared docs
[#57](https://github.com/fulstechlabs/docs/issues/57) remains a hard publication
prerequisite. PR #58 stays draft/unmerged; no publication is performed.

Revision validation: `npm run check` passed (13 files, zero diagnostics),
`npm run build` passed (175 pages / 215 HTML), `npm run audit:build` passed
(33,514 local href/src references), and `git diff --check` passed. The existing
generated-404 warning is unchanged. Chrome manually reviewed all three changed
customer pages at 1440×659 and 390×844, including both new warning sections and
the four guide/limitation cross-links. Text is readable at both widths; all six
image placements loaded at each width, and document width matched the viewport
without horizontal overflow. No product retest or product fix is claimed.
Temporary viewport was reset and the revision tab was closed; fresh inventory
preserved only the unrelated JEditor issue tab. The local preview server was
stopped after review.

### Original visual package validation

Required local gates: `npm run check`, `npm run build`, `npm run audit:build`,
and `git diff --check` all passed for the final content. Astro check: 13 files,
zero errors/warnings/hints. Build: 175 pages and 215 HTML files. Audit:
**33,508 local href/src references**, including all full-size screenshot links.
The existing generated-404 entry warning remains; build exits successfully.

Chrome review covered 35 routes (19 macro guides, macro catalog, Overview,
Getting Started, eight recipe routes, and five build/design guides) at normal
1440×659 and narrow 390×844 viewports: 70 route checks and 154 image placements.
All images loaded, every screenshot had its full-size link, and no document or
image extended beyond the viewport width. Actual source pixels and representative
rendered desktop/mobile views were manually inspected. Dense inventory/table
text still requires opening the full-size image on a phone; do not claim every
small toolbar label is readable in the inline thumbnail. The Team preview link
opened its real 1520×750 JPEG successfully. No live-product mobile/touch behavior
is certified by this docs-layout check.

Review receipts:
[desktop exact-plan placement](audits/better-pages-release-13-2026-10-01/docs-desktop-preview.jpg),
[mobile recipe placement](audits/better-pages-release-13-2026-10-01/docs-mobile-recipes.jpg).
Temporary viewport overrides were reset; completed task tabs were closed and a
fresh inventory preserved three unrelated user/other-task tabs. The local
preview server was stopped after review.

Dependency audit found
seven pre-existing findings (one moderate, five high, one critical); dependency
upgrades/security remediation are outside this image/content change and were
not hidden or auto-fixed.

Required publication route (not yet implemented by the current workflow):
docs PR → main → promotion PR main→release → merge release → manual dispatch
for exact release SHA → public verification. `origin/release` is currently
absent in docs; establish it from verified production lineage only when that
approved publication work begins, not from this unreviewed branch.
