---
title: "Issue Templates & Hierarchy Builder for Jira"
description: "Standardize recurring Jira work with reusable templates, previewed changes, multi-level hierarchies, and recoverable automation."
---

![Issue Templates & Hierarchy Builder for Jira](./assets/product-logo.png)

Issue Templates & Hierarchy Builder turns repeatable Jira work into a reusable
process. Build a template from scratch or capture proven Jira work, preview what
will change, and create or apply the result without silently replacing unrelated
user data.

The app is designed for Jira Cloud teams that repeat release checklists,
onboarding, QA, incident follow-up, operational reviews, and other structured
work.

## Choose the right workflow

| If you want to… | Use |
| --- | --- |
| Start new Jira work from a governed process | [Create from a template](../create-apply-recreate/#create-new-work-from-a-template) |
| Standardize an issue that already exists | [Apply a template](../create-apply-recreate/#apply-a-template-to-an-existing-issue) |
| Copy useful live work once without saving a governed template | [Recreate](../create-apply-recreate/#recreate-live-work-once) |
| Prefill Jira's standard Create dialog | [Native Jira Create prefill](../native-create-prefill/) |
| Let an authenticated JSM customer choose a template on a request form | [JSM customer portal templates](../jsm-customer-portal/) |
| Run template behavior after a Jira workflow transition | [Workflow Create](../workflow-create/) |

If you are unsure, start with explicit **Create** or **Apply**. They are the
dependable interactive paths because the user can review the result before Jira
is changed.

## What you can rely on

### Preview before changing Jira

Create, Apply, and Recreate show the fields and selected hierarchy before the
final action. Cross-project hierarchy is validated before mutation.

### Preserve user-entered data

Selective Apply makes Keep, Fill, Replace, and Skip decisions visible. Automatic
JSM and Workflow paths use a conservative empty-only root-field policy and do
not silently copy template comments or attachments.

### Recover partial hierarchy work safely

The **Template details** panel records the template revision, run status, child
outcomes, and actionable failures. Retrying a partial run reuses completed
checkpoints instead of creating the same child work again.

## Common use cases

- **Release readiness:** create a root issue with repeatable validation,
  documentation, and rollout tasks.
- **Onboarding:** ask for the person, date, or environment that changes each
  time and create the standard follow-up hierarchy.
- **Bug and QA process:** capture proven Jira work, standardize supported fields,
  and reproduce selected child work.
- **JSM operations:** let authenticated portal customers choose a governed
  request-type template while preserving the values they entered.

## Build and govern templates

Template authors can:

- Create a template from scratch or capture an existing issue.
- Add typed Jira-native fields, variables, and bounded Smart Values.
- Model multi-level Jira parent hierarchy separately from optional issue links.
- Control availability by project, group, person, and JSM request type.
- Configure app defaults, optional native Create prefill, and Workflow Create.
- Back up and validate same-tenant app configuration.

See [Templates and supported fields](../templates-and-fields/) and
[Administration](../administration/) for the complete authoring and governance
model.

## Where the app appears

- **Apps → Issue Templates & Hierarchy Builder** opens the complete template
  library.
- **Project → Templates & Hierarchies** opens the library in a project context.
- Jira administration contains governance, native Create rules, diagnostics,
  and backup/restore.
- A configured JSM request form can show the **Issue template** field to
  authenticated portal customers.
- A configured Jira workflow post-function can run the matching app default
  after a transition.
- An issue's actions menu contains Apply, Capture, and Recreate journeys.
- The **Template details** issue panel shows provenance and run outcomes.

Template authors can also open **Details** in the library to copy the stable
template ID or a ready-to-use `createdFromTemplate("…")` JQL query.

## Create your first useful result

The fastest first success is to install the editable starters and create the
**Release readiness** hierarchy.

Continue with [Getting Started](../getting-started/). After that, use the
[FAQ](../faq/) for common product decisions or [Release Notes](../release-notes/)
for the latest customer-visible changes.
