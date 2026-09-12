---
title: "Time in Status for Jira"
description: "Measure status duration, cycle time, lead time and elapsed ownership using your team's Jira workflow."
---

See where Jira work spends its time. Time in Status measures workflow history
using your own statuses, optional status groups and working calendars.

## What you can measure

- Duration across repeated visits to each status, including the current visit.
- Status entrances, directional transitions, and first or latest entrance dates.
- Cycle time using the statuses you select, and configurable lead time.
- Current status age to find work that may be waiting too long.
- Assignee ownership duration. This is elapsed time, not logged effort.

Select issues using a project and basic filters or JQL with autocomplete.
Compare issue rows or group by project, current assignee, issue type or component.
Save report configurations, share them with teammates, and export CSV or XLSX.

Start with the [user guide](../getting-started/). Jira administrators can configure
working calendars and enable the app-managed workflow field where needed.
Historical issues are calculated from Jira history on demand; this version does
not require a bulk import before the first report.

## Current scope

This release focuses on workflow time. It does not provide timesheets, billing,
or arbitrary formulas. Grouping uses current
issue fields rather than reconstructing historical team membership.

See [security and data](../security-and-data/) and
[troubleshooting and support](../support/) for operational details.

## Explore reports

| If you want to… | Start with… |
| --- | --- |
| Calculate your first workflow-time report | [User Guide](../getting-started/) |
| Investigate bottlenecks, trends and aging work | [Report Analysis](../report-analysis/) |
| Share settings or prepare recurring reports | [Sharing and Schedules](../sharing-and-schedules/) |
| Download CSV, XLSX or contributing issues | [Exports](../exports/) |
