---
title: "Security and Data"
description: "Where Time in Status stores configuration and reusable Jira workflow history."
---

Time in Status runs on Atlassian Forge and calls Jira Cloud APIs. The app has
no external backend, external runtime analytics service or configured external
network destination.

The sections below describe the submitted release. Infrastructure changes being
verified in QA are listed separately under [QA development update](#qa-development-update).

## Data locations

| Location | Purpose |
| --- | --- |
| App-managed Jira custom field | A bounded, replaceable workflow snapshot per issue: source revision, status IDs and visit timestamps, assignee account IDs and ownership timestamps. It contains no saved report totals, copied assignee profile names or email addresses. |
| Forge SQL | Working calendars, private saved report configurations and a singleton cache generation used for validation. Saved JQL may contain references entered by its owner. |
| Your browser | Last-used report inputs. This is separate from named saved reports and does not synchronize across devices. |
| Request memory | Jira responses, current display names and calculated results used for the active request. |
| Downloaded CSV | A user-controlled export of the selected report, including its labels and filters. |

Jira history remains the calculation source. The app reads current display names
from Jira when needed. If a name is unavailable, it shows the unchanged account
ID. A failed profile lookup does not change historical ownership or durations.

The cache is validated against Jira source metadata before reuse and replaced
when necessary. Calendar changes recalculate results from stored source visits;
the cache does not embed one user's timezone or working-hours totals.

## Permissions and events

Reports retrieve Jira data as the signed-in user. The app does not introduce a
separate role-management system. Jira administration permission is required for
calendar administration and workflow-field setup. Saved reports are private to
their owner.

App installation and upgrade initialize storage. A deleted-user event removes
that user's private saved reports; it does not edit Jira issue history. The app
does not run a scheduled report worker or a bulk historical import in this release.

Consult the [Fulstech Privacy Policy](/privacy-policy/),
[Security Policy](/security-policy/) and [support](../support/).

## QA development update

As of September 12, 2026, the following changes are deployed to the development
environment only. They do not change the submitted Marketplace build or the
production app.

### Workflow cache and configuration

The QA report, configuration-save and background-export paths no longer use a
cache-generation token. Workflow snapshots are still checked against the issue
ID, current Jira revision and calculation-engine version. Jira history remains
the source of truth. Calendar and timezone changes recalculate from the same
UTC visits without requiring a separate snapshot for each user.

The legacy generation table remains for inactive upgrade code; active report,
configuration and export flows do not read or write it. Last-used inputs remain
in browser storage. Named saved reports and calendars remain in Forge SQL.

### Background exports and retention

The QA build stores background export job state and report schedules in Forge
SQL. Generated export files are held temporarily in Forge Object Store with a
24-hour TTL. Expired files are handled by Object Store expiry rather than a
recurring application task that lists and deletes files.

An hourly task dispatches due schedules and recovers interrupted export jobs.
A separate daily task expires job state and prunes failed, cancelled and expired
metadata after seven days. Eligible metadata can remain until the next daily
run. Scheduled triggers are filtered to licensed installations. Immediate
best-effort file deletion remains for failed publication, with TTL as fallback.

The browser checks short export jobs frequently and gradually reduces polling
frequency for longer jobs. Lightweight maintenance functions use 128 MB;
the export worker retains 512 MB for CSV and XLSX generation.

### Verification status

A fresh development installation completed all 45 schema setup steps. A
25-issue report successfully rebuilt reusable Jira-field snapshots, and a
second run reused 24 snapshots. Both report runs made zero Forge SQL calls in
the measured report path. Configuration loading and background exports still
use SQL. These checks cover the QA fixture, not every tenant or workload.

The revised idle maintenance schedule is estimated to use about 1,500 SQL
requests per site in a 30-day month, down from 3,600. This is a request-count
estimate, not an invoice or a guarantee of total infrastructure savings.
