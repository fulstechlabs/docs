---
title: "Data and Privacy"
description: "Where Time in Status stores configuration and reusable Jira workflow history."
---

Time in Status uses Jira history to calculate reports and runs on Atlassian Forge. The app has no external backend.

## Data storage

| Location | Purpose |
| --- | --- |
| App-managed Jira custom field | A bounded, replaceable workflow snapshot per issue, including status visits and assignee account IDs/timestamps. |
| Forge SQL | Working calendars, private saved report configurations and bounded cache-validation state. Saved JQL may contain references entered by its owner. |
| Your browser | Last-used report inputs. This is separate from named saved reports and does not synchronize across devices. |
| Request memory | Jira responses, current display names and calculated report results used for the active request. |
| Downloaded CSV | A user-controlled export of the selected report, including its labels and filters. |

Jira history remains the calculation source. Current display names are read from Jira when needed; reusable snapshots do not store assignee profile names or email addresses.

## Jira permissions

Reports use the signed-in viewer's Jira permissions. The app does not introduce a separate role-management system.
Jira administration permission is required for calendar administration and workflow-field setup.
Saved reports are private to their owner.

## User and lifecycle events

Installation and upgrade initialize app storage. A deleted-user event removes that user's private saved reports; it does not edit Jira issue history.

Downloaded CSV files are outside the app after you save them. You control their storage, sharing and deletion.

## Policies and support

Read the [Privacy Policy](/privacy-policy/) and [Security Policy](/security-policy/), or [contact support](../support/) with questions about your data.
