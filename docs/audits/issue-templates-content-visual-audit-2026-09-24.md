# Issue Templates content and screenshot audit — 2026-09-24

## Scope

This audit verifies the public Issue Templates Jira Cloud documentation against:

- product repository `fulstechlabs/issue-templates-for-jira-forge` at `96dbe0d41dc3ac1790f1f31f1d66ee9a2bbc52f2`;
- production release 4.0.0 / Marketplace build 3002050;
- production release receipt and `publication.json`;
- current public-doc source baseline `fulstechlabs/docs` at `284c01778592e8c8cbab72d74f125d8f99d14fd6`;
- the actual pixels of every screenshot referenced by the reviewed Issue Templates pages.

The audit distinguishes **what a screenshot proves** from broader behavior proved
by source, tests, or production evidence.

## Text verification

| Public claim area | Verification source | Result |
| --- | --- | --- |
| Explicit Create / Apply labels and preview flow | `app/src/frontend/main.jsx` | Pass — current labels include Use template, Create new, Preview new issue, Create issue, Preview changes, Apply changes. |
| Create / Apply preserve-before-write contract | product strategy, implementation handoff, production smoke | Pass. |
| 20 related-item Capture/Recreate traversal limit | `app/src/index.js`, `app/src/hierarchy.js` | Pass. |
| Variable types and token syntax | `app/src/logic.js` | Pass — text/select/user/date variables; bounded token interpolation; unknown/unavailable tokens resolve to empty string. |
| Relative date/time syntax | `app/src/logic.js` | Pass — today/now with h/d/w/m/y offsets using one UTC base time. |
| Backup format/version and same-tenant scope | `app/src/index.js`, backup UI, release evidence | Pass — version 2; templates/defaults plus embedded template configuration; native Create rules are not restored. |
| JSM exact context filtering | `app/src/templateAccess.js` | Pass — service project/request type/root work type are revalidated and fail closed. |
| JSM automatic root-field safety | `app/src/portalExecution.js` | Pass — automatic portal execution forces only-empty behavior. |
| Portal-only customer support | manifest + 4.0.0 production smoke | Pass — `customer` and `unlicensed` enabled; `anonymous` excluded. |
| Portal-safe template payload | `app/src/portalExecution.js` | Pass — only selection-safe summary data is returned to the portal. |
| Template details supportability | `app/src/runSummary.js` + issue panel | Pass — run status, root/source, node outcomes and errors are exposed subject to access checks. |
| Workflow Create modes and deterministic run identity | `app/src/workflowExecution.js`, manifest, production smoke | Pass. |
| Workflow Create Beta disclosure | manifest / Atlassian Forge module status checked during PR #42 | Pass. |
| Native Create empty-only/user-owned-value safety | `app/static/ui-modifications/index.js` | Pass. |
| Native Create Group/Sprint boundary and multi-UIM wording | PR #42 platform revalidation | Pass. |

## Screenshot verification

| Asset | What the pixels prove | Status / usage rule |
| --- | --- | --- |
| `release-preview.png` | Release-oriented child hierarchy can be selected and edited before Create. | Pass. It does **not** show the root fields in the crop; captions must not say that the image itself proves root values. |
| `release-created.png` | Release v1.0 root exists with three created subtasks. | Pass. |
| `customer-basics.jpg` | Basics editor exposes name, description, category and Jira context. | Pass. |
| `customer-structure.jpg` | Structure editor exposes reusable child work plus separate Parent and Relationship controls. | Pass. |
| `customer-fields-inputs.jpg` | Fields & inputs supports variable insertion and relative-date authoring. | Pass as a delivery example. Do not present it as an employee-onboarding-specific screenshot. |
| `hierarchy-preview.jpg` | Create preview shows selected nodes, a selected parent and no additional link for the expanded child. | Pass. |
| `apply-preserve.jpg` | Apply can leave root fields unchanged while selected child work remains actionable. | Pass. |
| `provenance-panel.png` | Template details shows an Applied template, revision and completed run audit. | Pass for generic provenance/Apply. Do not use it as proof of a Create-origin or portal-origin run. |
| `native-create-settings.png` | App default and native Create prefill settings are separate controls. | Pass. |
| `backup-restore.png` | Backup/download/file-validation controls exist and describe same-site restore. | Pass. |
| `backup-review.png` | Restore review shows affected templates/defaults, zero Jira issue changes, Native Create warning and explicit confirmation. | Pass. |
| `smart-value-authoring.jpg` | Fields & inputs can insert a variable and use a relative-date token. | Pass. |
| `runtime-inputs.jpg` | Use template collects a required runtime input before Preview. | Pass as a generic delivery example. |
| `jsm-template-selection.jpg` | A controlled JSM request-form verification shows No template plus one friendly matching template. | Do not use on the authenticated-customer procedure: the screenshot contains "Raise this request on behalf of" and is the wrong actor context. Keep it only as historical evidence until replaced by the fresh portal-only capture from product issue #20. |
| `jsm-run-result.jpg` | Jira agent view shows Template details, Completed status and one created child for the controlled JSM fixture. | Pass. |

## Corrections from this audit

- Release-readiness caption now describes only the child-work evidence visible in
  `release-preview.png`; root-field review is described as part of the same
  Preview rather than as something visible in that crop.
- Release use case now also shows `release-created.png` so the result is
  visually grounded.
- The employee-onboarding page no longer uses the customer-delivery
  `customer-fields-inputs.jpg` screenshot as if it were onboarding-specific.
  The text keeps the verified variables behavior without pretending the image is
  scenario-specific.
- The old JSM selector screenshot is removed from the authenticated-customer
  public flow because it is an agent/on-behalf-of context. Portal-only support
  remains a production-evidence claim until issue #20 supplies a matching
  customer-context screenshot.

## Fresh production screenshot follow-up

Product issue `fulstechlabs/issue-templates-for-jira-forge#20` requests a
scenario-specific production screenshot set from the controlled dev2 tenant.

The requested captures cover:

- Release readiness runtime input / preview / result / Template details;
- Employee onboarding variables and runtime inputs;
- Customer onboarding structure;
- Incident Apply preservation;
- genuine portal-only JSM selector/submission/run result;
- optional Workflow-origin Template details.

When that issue hands back, replace older controlled development screenshots
only after verifying the new pixels and their evidence README. Do not replace an
accurate current image merely because a newer image looks cleaner.

## Audit outcome

The public text is within the verified 4.0.0/source contract after the corrections
above. Current screenshots are usable only under the evidence boundaries listed
in this document. The remaining quality improvement is scenario-specific
production capture, not a known product-claim defect.
