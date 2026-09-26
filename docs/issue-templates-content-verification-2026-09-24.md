# Issue Templates documentation content verification — 2026-09-24

> Historical audit of the earlier screenshot set. The later live production
> starter test, exact-context screenshots, and placement decisions are recorded
> in [Issue Templates customer screenshot provenance](issue-templates-screenshot-provenance-2026-09-24.md).
> In particular, the unedited Release readiness starter needed its child work
> types mapped to Jira's actual **Sub-task** type on the dev2 test project.

This is an internal verification record for the public documentation under
`src/content/docs/issue-templates/jira-cloud/`.

It is not customer-facing documentation and is intentionally not linked from the
public sidebar.

## Scope

Verified against:

- product repository: `fulstechlabs/issue-templates-for-jira-forge`;
- public production baseline: **4.0.0**, Marketplace build **3002050**;
- release source: `cef1850c52cd1f18f5519a5bad476cecac5d89d7`;
- current product `main` for source-level UI labels and behavioral contracts;
- `docs/product-strategy.md`;
- `docs/implementation-handoff.md`;
- `docs/releases/2026-09-22-production-4.0.0.md`;
- `publication.json`;
- Forge manifest, frontend source, portal access/execution source, workflow
  execution source, Jira API wrapper, storage serialization, and backup
  export/import source.

The audit separately checked:

1. customer-facing text claims;
2. exact UI labels;
3. product/security boundaries;
4. screenshot pixels and visible context;
5. whether each screenshot actually supports the surrounding caption.

A successful Starlight build or link audit was not treated as evidence that an
image was semantically correct.

## Text claims verified

### Core explicit flows

Current frontend source confirms the customer labels and flow used in docs:

- **Use template**
- **Create new**
- **Apply to existing**
- **Preview new issue**
- **Preview changes**
- **Create issue**
- **Apply changes**
- **Install editable starters**
- **Defaults & integrations**

The Forge manifest confirms the issue action/panel labels including:

- **Apply template**
- **Create template from issue**
- **Recreate issue and selected work**
- **Template details**

### Starter templates

Current product source contains four editable starters:

- Clear bug report
- Ready user story
- New teammate onboarding
- Release readiness

The Release readiness starter is:

- root summary: `Release {{version}} readiness`;
- variable: `version`;
- children:
  - Complete QA for `{{version}}`
  - Prepare release notes for `{{version}}`
  - Confirm rollout plan for `{{version}}`

The product acceptance evidence says the starter path completed well under ten
minutes. Public docs therefore use **quick-start / under ten minutes**, not an
unsupported five-minute guarantee.

### JSM portal

Verified in manifest/source and production evidence:

- the app field is **Issue template**;
- authenticated `customer` and `unlicensed` actors are enabled;
- `anonymous` is not enabled;
- portal selection requires exact request-type context and matching template
  project/root work type;
- the selector includes **No template**;
- only a reduced template summary is sent to the portal;
- automatic portal root application forces `only-empty`;
- populated customer root values are preserved;
- required portal variables need defaults;
- comments and attachments are not automatically copied;
- production 4.0.0 smoke passed No-template and matching-template paths.

### Workflow Create

Verified in manifest/source and production evidence:

- Forge post-function: **Create issue template structure**;
- retained modes:
  - `create-structure`
  - `copy-values`
  - `copy-children`
  - `copy-from-epic`
  - `disable`;
- transition identity produces a deterministic run ID;
- invalid hierarchy/configuration is blocked before mutation;
- `copy-children` removes optional additional issue-link behavior;
- Workflow Create remains Beta while the Forge module is Preview;
- production 4.0.0 smoke passed the bounded Workflow Create path.

### Security and user profile storage

Current manifest declares no external Forge remotes or egress domains.

The Jira API wrapper defaults to `api.asUser()`; integration/background paths
opt into `api.asApp()` when required.

Storage serialization uses `stripStoredUserProfileData()`. When an object is
an Atlassian account reference containing `accountId`, persisted JSON strips:

- `displayName`;
- `emailAddress` / `email`;
- `username` / `userKey`;
- `avatarUrls`;
- `timeZone` / `timezone`;
- `locale`.

A one-time persisted-data scrub applies the same serialization to relevant
template, run, audit, and app-config JSON columns.

Public Security documentation was tightened to state this exact contract rather
than making a broader profile-data claim.

### Licensing

Production license evaluation is fail-closed against Atlassian's signed resolver
context.

The customer UI explicitly states that templates remain readable when the
license is inactive and changes require an active trial/subscription. Mutation
resolvers call the license guard.

### Backup and restore

Current export source emits a version-2 document containing:

- templates, including archived templates when requested;
- template values/schema/variables/nodes/comments/attachment references stored
  inside each template;
- availability/permission rules;
- app defaults.

The export does not include:

- Jira issue records;
- attachment file bytes;
- runs or audit history;
- Native Create UI Modification rules.

Restore performs document validation and tenant preflight before writes.
Validation and import require Jira administrator permission; import also
requires an active license.

The current restore UI explicitly warns that Native Create rules are not
restored.

### Intentional boundaries

Known Limitations and FAQ were checked against current product strategy/source,
including:

- Rank / Assets / opaque third-party fields are not generic field support;
- same-tenant backup is not cross-site/DC migration;
- Native Create is optional and more constrained than explicit Create;
- anonymous JSM portal access is unsupported;
- later legitimate Workflow transitions are new executions.

The Customer Onboarding use case now says **migration project preparation**
instead of the ambiguous **migrations**, so it does not imply migration-tool
functionality.

## Screenshot verification

Every image below was opened and visually inspected at readable resolution.

### Existing images retained

| Docs asset | Visible evidence | Verification note |
| --- | --- | --- |
| `product-logo.png` | Product branding | No behavioral claim. |
| `smart-value-authoring.jpg` | Fields & inputs shows `Deliver {{client}}` and relative date `{{today+7d}}` | Correct for variables/Smart Values authoring. Controlled Dev fixture. |
| `hierarchy-preview.jpg` | Create preview shows selected hierarchy and an expanded child with Jira parent | Correct for parent/hierarchy preview. Controlled Dev fixture. |
| `provenance-panel.png` | Template details shows Applied, template revision and completed run audit | Correct only for provenance/completed-run claims. It is **not** a JSM portal screenshot. Controlled Dev fixture. |
| `native-create-prefill.png` | Jira Create contains prefilled URL and cascading-select values | Correct for Native Create verified-field example. |
| `backup-restore.png` | Backup & restore controls and same-site wording | Correct. Controlled Dev fixture. |
| `backup-review.png` | Review restore, affected templates/defaults, zero Jira issues changed, Native Create rules not restored | Correct. Controlled Dev fixture. |

### New/replacement evidence images

These files were copied byte-for-byte from evidence already committed in the
product repository.

| Docs asset | Product-repo evidence source | Visible evidence / allowed claim |
| --- | --- | --- |
| `customer-basics.jpg` | `docs/assets/ui-ux-walkthrough-after-redesign-2026-09/03-basics.jpg` | Customer-shaped Delivery checklist template Basics screen. Use for template identity/context UI, not production-environment claims. |
| `customer-fields-inputs.jpg` | `.../04-fields-inputs.jpg` | Fields & inputs with `{{client}}` and relative date. Use to explain reusable run-specific values. |
| `customer-structure.jpg` | `.../05-structure-editor.jpg` | Delivery root + child in Structure & content, with parent and relationship controls visible. |
| `runtime-inputs.jpg` | `.../08-use-create.jpg` | Use-template runtime input `client=Acme`, Create new selected, Preview new issue button. |
| `apply-preserve.jpg` | `.../11-apply-keep-preview.jpg` | Apply preview explicitly says zero root field values will change and one child will be created. Appropriate for “preserve existing incident details + add follow-up work.” |
| `release-preview.png` | `marketplace/assets/source/create-preview.png` | Release-oriented selected child hierarchy: Complete QA, Prepare release notes, Confirm rollout plan for v1.0. |
| `release-created.png` | `marketplace/assets/source/created-hierarchy.png` | Created `Release v1.0 readiness` root and three selected subtasks. |
| `jsm-template-selection.jpg` | `docs/assets/jsm-next-phase-handoff-2026-09-17/01-customer-template-selection.jpg` | Controlled JSM portal verification showing No template plus one matching template. Dev/E2E fixture; caption must not call it production. |
| `jsm-run-result.jpg` | `docs/assets/jsm-next-phase-handoff-2026-09-17/04-template-run-result.jpg` | Controlled agent-side JSM verification showing matching template Completed and one created child. Dev/E2E fixture; caption must not call it production. |

## Screenshot corrections made

The audit corrected the following semantic mismatches:

1. **Getting Started / Release readiness**
   - Removed generic QA-density Create preview.
   - Replaced with release-specific preview and created hierarchy evidence.

2. **Employee onboarding**
   - Removed generic QA runtime form with `client/input2/input3...`.
   - Replaced with a customer-shaped Fields & inputs example.
   - Caption explicitly explains that it demonstrates the same variable
     mechanism rather than pretending employee-specific values are visible.

3. **Customer onboarding**
   - Replaced QA hierarchy fixture with a Delivery checklist Structure editor.
   - Caption no longer claims an optional issue link that is not visible.

4. **Incident follow-up**
   - Replaced generic custom-field Fill/Keep screenshot with an Apply preview
     that visibly preserves every root field and creates one selected child.

5. **JSM request fulfillment**
   - Removed the Release-readiness Apply provenance screenshot that had been
     incorrectly described as portal-triggered.
   - Added actual controlled JSM portal selector and completed-run evidence.

6. **Templates / variables core guides**
   - Replaced QA-density fixtures where a clearer customer-shaped walkthrough
     image already existed.

## Production-vs-development screenshot caveat

No production-smoke screenshots were attached to the release coordination
issues. Production behavior is verified by the 4.0.0 release receipt and
immutable smoke evidence, but several public-doc UI screenshots necessarily
come from controlled development/E2E verification.

Therefore:

- captions do not call those images production screenshots;
- screenshots are used only for UI/behavior they visibly demonstrate;
- production claims are grounded in the release receipt/source, not inferred
  from a Dev badge screenshot.

## Verification outcome

After the corrections in this audit branch:

- no known screenshot is captioned as a different flow from the one visible;
- high-risk JSM, workflow, security, licensing, and backup claims are grounded
  in current source and/or production 4.0.0 evidence;
- use-case examples remain illustrative custom templates, not claims that the
  app ships domain-specific onboarding/incident/customer-delivery logic;
- the starter-specific Getting Started path matches the actual Release readiness
  starter contract.

Remaining validation before merge:

- Starlight content/config check;
- production docs build;
- built-link/assets audit;
- final diff review.
