---
title: "Administration"
description: "Control template availability, defaults, licensing, diagnostics, and recovery tools."
---

Jira administrators can open the app's administration page from Jira settings.
Project administrators can manage governed templates for projects where Jira
grants the required permission. The backend checks permissions again for every
read or mutation; hiding a button is not the authorization boundary.

## Availability rules

A template can be limited by:

- Jira project.
- Issue type.
- Jira group.
- Individual Atlassian account.
- Enabled or disabled rule state.

All configured parts of a rule must match. A deleted or invisible project,
group, or account does not broaden access.

## App defaults

An app default helps users find the relevant template in the explicit app
journey. It does not automatically change Jira's standard Create dialog.

Native Create prefill is a separate administrator-controlled rule. See
[Native Create prefill](../native-create-prefill/) before enabling it.

## Licensing behavior

Issue Templates & Hierarchy Builder is a paid Marketplace app. With an active
evaluation or subscription, create and administration actions are available.
When Atlassian reports an inactive license:

- Existing templates and configuration remain readable.
- Create, Edit, Duplicate, Archive, Apply, Recreate, and other mutations are
  disabled.
- Backend mutation resolvers reject direct calls as well.

Ending a trial or subscription does not silently delete app data.

## Diagnostics and support lookup

Administrator diagnostics show bounded counts and schema status. The run
lookup accepts a known root issue key and returns a human-readable run summary;
it does not expose raw SQL rows.

Use [Backup and restore](../backup-and-restore/) before significant
configuration work. For a support case, include the site URL, affected issue
key, run ID, expected result, and a screenshot with unrelated information
removed.

