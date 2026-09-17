---
title: "Create, Apply, and Recreate"
description: "Choose the correct explicit workflow for new work, existing issues, or a one-time copy."
---

The app has three explicit user journeys. Each presents a preview before Jira
is changed.

## Create new work from a template

Use **Use template → Create new** when the process should begin with a new root
issue.

1. Choose a template from the library.
2. Select **Use template**, keep **Create new** selected, and answer its runtime
   inputs.
3. Select **Preview new issue**.
4. Review and adjust the root values.
5. Select the child work needed for this run.
6. Open **Details** on child work to confirm its Jira parent and any additional
   issue-link direction.
7. Select **Create issue**.

Jira receives a normal root issue followed by the selected hierarchy. Parent
work is created before its children. The run keeps an immutable plan, so retry
can skip children and links that already succeeded.

![Preview the selected Jira parent before creating the hierarchy](./assets/hierarchy-preview.jpg)

## Apply a template to an existing issue

Use **Apply template** from an issue when the root already exists but needs
standard fields or follow-up work.

1. Open the issue and choose the app's Apply action.
2. Select an available template.
3. Answer any runtime inputs and select **Preview changes**.
4. Compare **Current** and **Proposed** values. The decision beside each field
   explains whether the app will **Keep**, **Fill**, **Replace**, or **Skip** it.
5. Select only the root fields and child work you want.
6. Include configured comments or attachments only when needed.
7. Select **Apply changes**.

![Selective Apply preview](./assets/apply-preview.png)

The default **Only fill empty fields** rule preserves a populated Jira field. The preview
makes every selected overwrite visible before it happens.

## Recreate live work once

Use **Recreate issue and selected work** when a useful live issue should be
reproduced without adding a governed template to the library.

Choose the destination project and issue type, select the supported root
fields, nested child work, and links, then review the one-time creation plan.
Recreate preserves selected parent relationships and keeps one copy when the
same issue is both a child and linked to the source root. Before Jira is
changed, the app checks that the destination project has compatible hierarchy
levels for the selected work types. The resulting issue is marked
**Recreated once** in its provenance.

## Understand the result

The **Template details** issue panel shows:

- Operation type, template name, and template revision.
- Root and source issue.
- Durable run ID and current status.
- One outcome for each child node.
- The latest actionable error for a partial run.

![Template provenance and run audit](./assets/provenance-panel.png)

Retry is available only for failed or partial work. Completed nodes are not
replayed.
