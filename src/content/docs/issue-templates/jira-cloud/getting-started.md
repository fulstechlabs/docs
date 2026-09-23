---
title: "Getting Started"
description: "Create your first useful Jira hierarchy from an editable starter template in a few minutes."
---

This guide takes you from an installed app to one completed Jira hierarchy. The
goal is a useful first result, not a tour of every feature.

## Before you begin

You need:

- A Jira Cloud site with the app installed and an active evaluation or
  subscription.
- Permission to create issues in the target project.
- A Jira administrator for the one-time starter installation.

## Step 1 — Install the editable starters

1. In Jira settings, open **Issue Templates & Hierarchy Builder**.
2. Open **Administration → Defaults & integrations**.
3. Select **Install editable starters**.
4. Enter an issue key from the project that should own the starters.
5. Confirm **Install editable starters**.

The starter gallery contains normal editable templates for a bug report, user
story, teammate onboarding, and release readiness. They are starting points, not
locked demo content.

## Step 2 — Open Release readiness

1. Return to **Templates**.
2. Find **Release readiness**.
3. Select **Use template**.
4. Keep **Create new** selected.

You can edit the starter later. For the first run, use it as-is so you can verify
the complete flow quickly.

## Step 3 — Preview the new work

1. Answer any required runtime inputs.
2. Select **Preview new issue**.
3. Review the root fields.
4. Confirm the selected child work.
5. Open **Details** on a child when you want to check its Jira parent or
   additional issue-link direction.

Preview is the decision point. Jira has not been changed yet.

## Step 4 — Create the hierarchy

Select **Create issue**.

The root issue is created first. Parent work is created before its selected
children. The run keeps an immutable plan, so retry can skip nodes and links
that already succeeded.

## Verify the result

Open the new root issue and confirm:

- The expected root fields are present.
- The selected child work exists with the expected Jira parent hierarchy.
- **Template details** shows the template name and revision.
- The run is **Completed**, or a partial result explains what needs attention.

You have now completed the core product journey.

## Next steps

Choose the next task that matches your goal:

- [Edit a template and supported fields](../templates-and-fields/).
- [Apply a template to an existing issue](../create-apply-recreate/#apply-a-template-to-an-existing-issue).
- [Add variables and Smart Values](../variables-and-smart-values/).
- [Configure template availability and defaults](../administration/).
- [Offer templates on a JSM customer request](../jsm-customer-portal/).
- [Run a template after a workflow transition](../workflow-create/).

If something does not match the preview, start with
[Troubleshooting and Support](../troubleshooting-and-support/).
