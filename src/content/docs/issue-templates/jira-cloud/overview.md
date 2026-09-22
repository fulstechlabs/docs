---
title: "Issue Templates & Hierarchy Builder for Jira"
description: "Create consistent Jira issues, subtasks, and reusable hierarchies with clear previews and recoverable results."
---

![Issue Templates & Hierarchy Builder for Jira](./assets/product-logo.png)

Issue Templates & Hierarchy Builder turns repeatable Jira work into a reusable
process. Build a template from scratch or capture a proven issue, ask users for
the values that change each time, preview the result, and create or apply the
work without silently changing unrelated fields.

The app is designed for Jira Cloud teams that repeat release checklists,
onboarding, QA, incident follow-up, operational reviews, and other structured
work.

## What can you do?

| If you want to… | Start with… |
| --- | --- |
| Build a reusable issue and subtask structure | [Templates and supported fields](../templates-and-fields/) |
| Create new Jira work from a template | [Create, Apply, and Recreate](../create-apply-recreate/) |
| Add a standard process to an existing issue | [Selective Apply](../create-apply-recreate/#apply-a-template-to-an-existing-issue) |
| Reproduce selected live work once | [Recreate](../create-apply-recreate/#recreate-live-work-once) |
| Ask for run-specific values or derive dates and Jira context | [Variables and Smart Values](../variables-and-smart-values/) |
| Control who can use each template | [Administration](../administration/) |
| Offer a governed template on a JSM customer request form | [JSM customer portal templates](../jsm-customer-portal/) |
| Run a template after a Jira workflow transition | [Workflow Create](../workflow-create/) |
| Prefill Jira's standard Create dialog | [Native Create prefill](../native-create-prefill/) |
| Protect app configuration | [Backup and restore](../backup-and-restore/) |

## The predictable workflow

1. An administrator or project lead prepares the reusable process once.
2. A user chooses a template and answers any run-specific questions.
3. The app shows the exact root fields and child work before changing Jira.
4. Jira receives normal issues with the reviewed parent hierarchy and selected
   issue links.
5. The **Template details** panel records what happened and supports safe
   recovery when a hierarchy finishes only partially.

The explicit **Use template** and **Apply template** journeys are the dependable
product paths. Optional native Create prefill is available for exact project
and issue-type combinations configured by a Jira administrator.

Administrators can also expose a template on an authenticated Jira Service
Management request form or run an app default from a Jira workflow transition.
Workflow Create is Beta while Atlassian's Forge workflow post-function module
remains Preview.

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
template ID or a ready-to-use `createdFromTemplate("…")` JQL query for issues
created from that template.

## Create your first hierarchy

1. Ask a Jira administrator to open **Administration → Defaults & integrations**
   and select **Install editable starters**.
2. In the template library, find **Release readiness** and select **Use template**.
3. Keep **Create new** selected, answer any runtime inputs, and select
   **Preview new issue**.
4. Review the fields and child hierarchy, then select **Create issue**.

Continue with [Getting started](../getting-started/) for the complete walkthrough.
See [Release notes](../release-notes/) for the latest customer-visible changes.
