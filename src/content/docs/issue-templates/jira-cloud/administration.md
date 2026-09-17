---
title: "Administration"
description: "Control template availability, defaults, licensing, diagnostics, and recovery tools."
---

Jira administrators can open **Issue Templates & Hierarchy Builder** from Jira
settings and select **Administration**.
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

To preview the matching default for an issue:

1. Open **Administration → Defaults & integrations**.
2. Select **Apply project default**.
3. Enter the Jira issue key and select **Preview project default**.
4. Review the proposed changes before selecting **Apply changes**.

Native Create prefill is a separate administrator-controlled rule. See
[Native Create prefill](../native-create-prefill/) before enabling it.

## Archive and restore templates

Archiving removes a template from the active library. It also clears that
template's app default and native Create rule. Existing Jira issues and their
**Template details** remain unchanged.

A Jira administrator can restore an archived template from
**Administration → Data management → Archived templates**. Restoring returns
the template to the library; it does not automatically recreate a previous
default or native Create rule.

## Backup and restore

**Data management** also contains same-site configuration backup and restore.
Only Jira administrators can perform these operations. See
[Backup and restore](../backup-and-restore/) for the contents and restore
safety checks.

## Licensing behavior

Issue Templates & Hierarchy Builder is a paid Marketplace app. With an active
evaluation or subscription, create and administration actions are available.
When Atlassian reports an inactive license:

- Existing templates and configuration remain readable.
- Create, Edit, Duplicate, Archive, Apply, Recreate, and other mutations are
  disabled.
- Backend mutation resolvers reject direct calls as well.

Ending a trial or subscription does not silently delete app data.

## Advanced diagnostics and recovery

Select **Show diagnostics** under **Administration → Advanced** to see storage
status, inspect native Create rules, run reconciliation, or find the latest app
run for a known root issue key. A failed or partial run can expose
**Retry failed nodes** after the underlying Jira problem is corrected.

The support lookup returns a human-readable run summary and does not expose raw
SQL rows.

For a support case, include the site URL, affected issue key, run ID, expected
result, and a screenshot with unrelated information removed.
