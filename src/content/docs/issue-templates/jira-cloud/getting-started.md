---
title: "Getting Started"
description: "Install editable starters and create your first Jira hierarchy from a template."
---

This guide takes you from installation to the first issue hierarchy created
from a reusable template. You do not need to understand Forge or edit JSON.

## Before you begin

You need:

- A Jira Cloud site with the app installed and an active evaluation or
  subscription.
- Permission to create issues in the target project.
- A Jira administrator to install starters. Jira or project administrators can
  manage governed templates for projects they administer.

## Install editable starters

1. In Jira settings, open **Issue Templates & Hierarchy Builder**.
2. Open **Administration → Defaults & integrations**.
3. Select **Install editable starters**.
4. Enter an issue key from the project that should own the starter templates.
5. Select **Install editable starters** in the dialog.

The starter gallery contains normal editable templates for a bug report, user
story, teammate onboarding, and release readiness. They are starting points,
not locked demo content.

## Review a template

Return to **Templates**, open **Release readiness**, select **Details**, and
then select **Edit template**. Review:

- The Jira project and root issue type.
- Root fields owned by the template.
- The child work, each Jira parent, and any separate issue-link relationship.
- Any variables that users answer for each run, plus supported Smart Values
  such as `{{today+7d}}` or `{{project.key}}`.
- Availability rules and default behavior.

Save only when the project, issue type, and fields match your Jira
configuration. See [Templates and supported fields](../templates-and-fields/)
for the complete field list.

## Preview and create

1. Select **Use template** on the template.
2. Keep **Create new** selected and answer any required runtime inputs.
3. Select **Preview new issue**.
4. Review the resolved root fields, especially dates and Jira-context values.
5. Select **Edit** beside a value when it needs a one-run change.
6. Deselect any child work that is not required this time.
7. Open **Details** for child work when you need to confirm its Jira parent or
   issue-link direction.
8. Select **Create issue**.

![Review the fields that will be created before confirming the new issue](./assets/create-preview.png)

The root issue is created first. Parent work is created before its selected
children, using the hierarchy shown in Preview. Child work is then processed
from a durable run plan. If a child fails, completed items are retained and a
retry does not create them again.

Variables are questions answered by the user. Smart Values are bounded values
resolved by the app from the run time or Jira context. They are not the Jira
Automation expression language. See [Variables and Smart Values](../variables-and-smart-values/)
for the exact token list and availability rules.

## Confirm the result

Open the new root issue and check:

- The expected fields and subtasks are visible in Jira.
- **Template details** shows the template name and revision.
- The run status is completed, or each partial result explains what needs
  attention.

Next, learn how to [Apply or Recreate work](../create-apply-recreate/) and how
to [configure availability](../administration/).
