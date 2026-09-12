---
title: "Security and Data"
description: "Where Time in Status stores configuration and reusable Jira workflow history."
---

Time in Status runs on Atlassian Forge and calls Jira Cloud APIs. The app has
no external backend, external runtime analytics service or configured external
network destination.

## Data locations

| Location | Purpose |
| --- | --- |
| App-managed Jira custom field | A bounded, replaceable workflow snapshot per issue: source revision, status IDs and visit timestamps, assignee account IDs and ownership timestamps. It contains no saved report totals, copied assignee profile names or email addresses. |
| Forge SQL | Working calendars, saved report configurations, schedules and background export job information. Saved JQL may contain references entered by its owner. |
| Your browser | Last-used report inputs. This is separate from named saved reports and does not synchronize across devices. |
| Request memory | Jira responses, current display names and calculated results used for the active request. |
| Forge Object Store | Temporary background export files, which expire after 24 hours. |
| Downloaded CSV/XLSX | A user-controlled export of the selected report, including its labels and filters. |

Jira history remains the calculation source. The app reads current display names
from Jira when needed. If a name is unavailable, it shows the unchanged account
ID. A failed profile lookup does not change historical ownership or durations.

The cache is validated against Jira source metadata before reuse and replaced
when necessary. Calendar changes recalculate results from stored source visits;
the cache does not embed one user's timezone or working-hours totals.

## Permissions and events

Reports retrieve Jira data as the signed-in user. The app does not introduce a
separate role-management system. Jira administration permission is required for
calendar administration and workflow-field setup. Saved reports are private unless the owner shares their configuration. Shared
reports are calculated separately using each viewer's Jira access.

App installation and upgrade initialize storage. A deleted-user event removes
that user's owned saved reports, schedules and export job records; it does not
edit Jira issue history. Scheduled reports use the owner's current Jira access.
Historical issues can be calculated on demand without a bulk import.

Consult the [Fulstech Privacy Policy](/privacy-policy/),
[Security Policy](/security-policy/) and [support](../support/).
