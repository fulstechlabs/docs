# Issue Templates documentation release-gate audit — 2026-09-27

Internal evidence for [product issue #36](https://github.com/fulstechlabs/issue-templates-for-jira-forge/issues/36). The public site at docs commit `137fdb58073efb8fbaa4f4669ff56ee320ae2332` was already deployed from [docs PR #46](https://github.com/fulstechlabs/docs/pull/46) before this follow-up. Marketplace production remained app 4.0.0, build 3002050; product source for the upcoming consolidated release was certified at `96e1c12c8680eb3ebd9cb6edf5d5432a2ad6ef22`. This audit changes docs assets and prose only.

## Seven screenshot repairs

All published replacements are crops or direct captures of real Jira/Forge UI. No product text inside an image was edited. The first three live captures below were made in the **production Forge installation on the dev2 test tenant**, not the separate Dev installation. Their editor/preview states were left without saving or creating Jira work.

| Public asset | Source, fixture and workflow state | What the image proves; limits |
| --- | --- | --- |
| `customer-basics.jpg` | Fresh 4.0.0 capture, Customer rollout, ITHBE2E / Task, **Edit template → Basics**. | Name, description, category, project and issue-type controls are visible. The screenshot does not prove a save. |
| `hierarchy-preview.jpg` | Fresh 4.0.0 capture, manually mapped Release readiness starter with `version=v2.5`, **Review new issue** with the third child's Details open. | Three selected subtasks and `Jira parent: root issue; no additional issue link` are visible. It is a preview, not a completed Create; this installed starter was manually mapped under 4.0.0. |
| `native-create-settings.png` | Fresh 4.0.0 capture, Customer rollout with a transient unsaved Sprint field, **Review & settings → Edit settings**. | Both default and native Create controls plus the full Forge UI Modifications warning for Sprint are visible. Neither control was enabled or saved in this capture. |
| `smart-value-authoring.jpg` | Exact crop of the prior real dev2 Jira capture introduced in docs commit `b0ef2e9` (3.6 documentation pass); source installation/build is not independently recorded. Fields & inputs had `{{client}}` in Summary and `{{today+7d}}` in Due date. | Demonstrates the authoring controls and example. It is not evidence of a completed run or of the current date. Current visible labels and relative-date behavior were checked against product source `b6f9afc`. |
| `runtime-inputs.jpg` | Removed. Its customer-facing role now reuses `customer-use-cases/employee-runtime-inputs.png`, captured in 4.0.0 for Employee onboarding. | Three inputs before Preview; the fixture creates a root issue only. Adjacent prose and alt text now name the same employee fixture. |
| `backup-restore.png` | Exact crop of prior real dev2 Jira capture introduced in docs commit `b0ef2e9`; source installation/build is not independently recorded. | Shows Backup & restore, Download backup file, Choose File, disabled Validate file before selection, Create backup and Validate backup. The crop excludes unrelated fixture rows and app navigation; current labels were cross-checked with product source `b6f9afc`. |
| `backup-review.png` | Exact crop of the same legacy dev2 capture, **Review restore** modal for a test backup. | Shows no changes yet, 45 affected templates, two default changes, zero Jira issues, native Create warning and confirmation. These counts belong only to the test backup; current modal labels were checked against product source `b6f9afc`. No restore was performed during this audit. |

The older uncropped captures exposed Dev badges, unrelated installed apps or QA fixture names. The new frames omit that clutter without hiding a relevant disabled state or warning. The three fresh screenshots are of production 4.0.0 running on a **test tenant**; they are not customer-tenant or next-release evidence.

## Team-managed Jira Software receipt

The public Known Limitations sentence is supported by a concrete tenant record, not a manifest inference. Product repository commit [`b6f9afc`](https://github.com/fulstechlabs/issue-templates-for-jira-forge/commit/b6f9afc415f301788378003d366db6c8c3f9abd4) identifies `SCRUM` as a **team-managed Jira Software project** in `docs/implementation-handoff.md` (team-managed regression and `SCRUM-80` through `SCRUM-89`). Its `docs/evidence-report.md`, `docs/product-walkthrough.md` and `app/evidence/implementation-20260829/` record explicit native hierarchy `SCRUM-63 → SCRUM-64`, starter Create `SCRUM-68 → SCRUM-69/70/71`, selective Apply `SCRUM-76 → SCRUM-77`, and Recreate `SCRUM-76 → SCRUM-78 → SCRUM-79`. The public sentence remains concise; these are the immutable review references.

## Release-state reconciliation

- Starter installation calls `assertTemplateAdmin(projectKey)`. The production `v4.0.0` tag (`cef1850c52cd1f18f5519a5bad476cecac5d89d7`) and product source `b6f9afc` both accept Jira `ADMINISTER` **or** project `ADMINISTER_PROJECTS`; Getting Started now names both. Backup and diagnostics still require Jira `ADMINISTER`.
- Public Getting Started, FAQ and hierarchy troubleshooting now distinguish production 4.0.0 manual mapping from the upcoming sole-compatible-subtask resolution. The production Release readiness screenshot pack retains its documented manual-mapping provenance.
- Release Notes has an unnumbered **Upcoming release** section for exactly two post-4.0.0 changes: starter type resolution and bounded Jira error details. It does not imply Marketplace promotion or invent a version/date.
- The earlier [screenshot provenance](issue-templates-screenshot-provenance-2026-09-24.md) now records the actual docs PR #46 merge/publication order, while preserving its capture-era facts.

## Public-page content audit

All 22 pages under `src/content/docs/issue-templates/jira-cloud/` were reviewed against `docs/docs-style-guide.md`. Intent and navigation remain as accepted; no rewrite or product scope change was warranted.

| Page | Release-gate result |
| --- | --- |
| `overview` | Primary path, workflow choice and outcome visual retained. |
| `getting-started` | Starter permissions and 4.0.0/upcoming distinction corrected; preview and completed-result claims stay separate. |
| `use-cases` | Scenario navigation and Release readiness preview claim retained. |
| `use-case-release-readiness` | Expanded example remains distinguished from the photographed one-input, three-child starter. |
| `use-case-employee-onboarding` | Three-input fixture and illustrative larger hierarchy remain distinguished. |
| `use-case-customer-onboarding` | Structure image shows three children; prose does not claim a completed run. |
| `use-case-incident-follow-up` | Second Apply preview is not presented as a second submitted Apply. |
| `use-case-jsm-request-fulfillment` | Portal selection and agent-side completion remain separate claims. |
| `templates-and-fields` | Basics image replaced; supported field families, hierarchy and 20-node limits retained. |
| `variables-and-smart-values` | Dev/QA screenshots removed; runtime image/prose now name the same employee fixture. |
| `create-apply-recreate` | Hierarchy preview recaptured; preview-before-write and same-run recovery retained. |
| `native-create-prefill` | Both controls and full Sprint warning shown; five-UIM-app platform boundary retained. |
| `jsm-customer-portal` | Authenticated portal-only actor and exact request-type boundary retained; anonymous remains excluded. |
| `workflow-create` | Beta/Forge Preview boundary retained. |
| `administration` | Project-template governance and Jira-admin-only backup/diagnostics remain distinct. |
| `backup-and-restore` | Controls and review-modal crops repaired; version 2 and same-tenant limits retained. |
| `security-and-privacy` | Forge storage, authorization, egress and licensing statements left unchanged after source check. |
| `privacy-policy` | Legal/privacy URL and product data categories preserved. |
| `faq` | Current vs upcoming starter behavior corrected; short answers still link to canonical guides. |
| `known-limitations` | Team-managed evidence traced to immutable receipt; field, hierarchy and platform limits retained. |
| `troubleshooting-and-support` | Current-version hierarchy symptom corrected; support diagnostics and secret warning retained. |
| `release-notes` | Upcoming section added without fabricated version or promotion claim. |

## Referenced-image audit

The starting deployed pages referenced **18 distinct product screenshots**, plus the logo. Seven legacy screenshot roles above were the only Dev/QA/debug failures. One is now served by an already accepted employee capture, leaving **17 distinct product screenshots plus the logo** in this PR. All remaining image files were opened at readable resolution and checked against adjacent fixture, child count, Create/Apply/portal state, permission and release claims:

| Retained screenshot set | Alignment result |
| --- | --- |
| `customer-use-cases/getting-started-release-{runtime,preview,result,jira,details}.png` | One Release readiness input, three mapped children; preview, completed run and Jira issue remain distinct 4.0.0 evidence. |
| `customer-use-cases/employee-{variables,runtime-inputs}.png` | Three variables and three runtime answers; pictured fixture is root-only. |
| `customer-use-cases/customer-structure.png` | Three child controls, not the larger illustrative example or a completed run. |
| `customer-use-cases/incident-kept-fields-child.png` | Second Apply preview with Keep decision; no second submission claim. |
| `customer-use-cases/jsm-{portal-selection,agent-run-result}.png` | Authenticated customer selector and agent-side Portal-origin result correctly separated. |
| The six replaced/cropped files in the table above | Current visible labels checked; state and crop limitations recorded per file. |

The product logo is a brand asset rather than an interaction screenshot and was checked for a valid reference. The `runtime-inputs.jpg` debug fixture is no longer referenced or retained. No screenshot is used to claim automatic starter resolution in production 4.0.0.

## Verification

- `npm run check`: passed, 0 errors, warnings or hints.
- `npm run build`: passed, 164 pages built.
- `npm run audit:build`: passed, 29,444 local `href`/`src` references checked across 204 HTML files.
- `git diff --check`: passed.
- The nine affected public pages (`getting-started`, `templates-and-fields`, `create-apply-recreate`, `variables-and-smart-values`, `native-create-prefill`, `backup-and-restore`, `faq`, `release-notes`, `troubleshooting-and-support`) were rendered and inspected at **390px** and **1280px**. Document scroll width equalled viewport width at both sizes for every page. A normal scroll loaded the lower lazy images in Getting Started (5/5) and Create/Apply/Recreate (3/3); no image path was missing in the built-site audit.
- The browser review tab was closed and the temporary viewport reset. Preview server was stopped. Unrelated user tabs were left open.

CI and PR review are additional gates. Site publication and app promotion are separate later actions.

## 28 September 2026 follow-up

The 4.1.0 Forge production deployment and Marketplace build 3002060 are now
public. The earlier 4.0.0 release-state statements above remain the historical
state of this audit. The 4.1.0 docs update changes only release wording and
starter guidance; the screenshots retain their 4.0.0 capture provenance.
