---
title: "Data and Privacy"
description: "Where Time in Status 3.0.0 processes and stores report configurations, workflow history and export files."
---

Time in Status uses Jira history to calculate reports and runs on Atlassian Forge. The app has no external backend.

## Data storage

| Location | Purpose |
| --- | --- |
| App-managed Jira custom field | A bounded, replaceable workflow snapshot per issue, including status visits and assignee account IDs/timestamps. |
| Forge SQL | Working calendars, saved report configurations, sharing state, background export job metadata and bounded cache-validation state. Saved JQL can contain references entered by its owner. |
| Forge Object Store | Background CSV/XLSX files for up to 24 hours. |
| Your browser | Last-used report inputs. This is separate from named saved reports and does not synchronize across devices. |
| Request memory | Jira responses, current display names and calculated report results used for the active request. |
| Downloaded files | User-controlled CSV/XLSX copies, including selected report labels and filters. |

Jira history remains the calculation source. Current display names are read from Jira when needed; reusable snapshots do not store assignee profile names or email addresses.

## Jira permissions and sharing

Reports use the signed-in viewer's Jira permissions. The app does not introduce a separate role-management system. Jira administration permission is required for calendar administration and workflow-field setup.

Sharing exposes a saved configuration, including its JQL, but does not grant access to additional issues or to the owner's export files. Shared reports and the **Workflow Time report** dashboard gadget calculate with each viewer's current Jira access.

A background export continues as the Jira account that started it and rechecks that account's access while collecting data. It does not fall back to app-wide access or another user.

## Export lifecycle

Background files expire from Forge Object Store after **24 hours**. A ready job then becomes **expired** and cannot produce a new download link. Failed, cancelled and expired job metadata is retained only for the bounded recent-job window and is pruned after seven days.

Cancelling a job stops further collection. Recovery can redispatch recoverable queued/running work, but permission failures end without publishing a ready file.

Downloaded files are outside the app after you save them. You control their storage, sharing and deletion.

## User and app lifecycle events

Installation and upgrade initialize app storage. A deleted-user event removes that user's saved reports and background export job metadata; it does not edit Jira issue history. Uninstall follows the app's Forge lifecycle cleanup path.

## Policies and support

Read the [Privacy Policy](/privacy-policy/) and [Security Policy](/security-policy/), or [contact support](../support/) with questions about your data.
