---
title: "User Guide"
description: "Select Jira issues, calculate workflow time, use business calendars, save reports and export CSV or XLSX."
---

## Your first report

1. Open **Apps → Time in Status → Reports** in Jira.
2. Under **Select issues**, choose **Basic** and a project, or **JQL** and enter
   your query. Issue type and current assignee narrow the current issue selection.
3. Select **Time in status** as the metric. Start with **Full history** and
   **24/7 elapsed time** to see elapsed duration across every observed visit.
4. Choose **One search page**, with 25 issues initially, and **Run report**.
5. Read the result's scope, calculation timestamp and completeness before using
   the numbers. Open an issue's history from its report row to inspect visits.

Issues created before installation can be reported from Jira history. The first
request may take longer than later requests because the app has to read history.
There is no bulk historical-import step to start in this version.

If the report offers **Enable cache for [project]**, a Jira administrator can
enable the app-managed workflow field and then rerun. Direct calculation remains
available without a reusable cache. Field configuration can be shared by Jira
projects; read the setup message before applying it. Users do not enter snapshot
data into the field themselves.

## Choose the question you want to answer

| Metric | Meaning |
|---|---|
| Time in status | Sum of all visits to each selected status, including the current open visit up to the calculation cutoff. |
| Status count | Number of observed entrances into a status; initial status at creation is an entrance. |
| Transition count | Number of observed directional changes between statuses. Status selection filters destination statuses. |
| First / latest status entrance | Earliest / latest entrance timestamp for each status. |
| Assignee time | Elapsed ownership time associated with each assignee. This does not measure hours worked or worklogs. |
| Cycle time | Duration in the statuses or status groups you select for the cycle. |
| Lead time | The configured status-set duration or created-to-completion measurement; choose the definition that matches your workflow. |
| Current visit age | Duration of the current status visit; earlier visits to the same status do not increase it. |

Status names are not fixed to a software workflow. Use **Statuses and optional
groups** to select states and define groups such as Waiting or Active work.
Groups belong to the report. Groups can overlap: do not add overlapping group
totals together or add groups to their constituent status totals.

## Working hours and date filters

A Jira administrator can create a calendar under **Calendars** with timezone,
working weekdays, start/end times, breaks and excluded dates. In **Reports**,
select that calendar under **Time calculation**. A calendar existing in settings
does not make a report use business hours automatically.

For example, with Monday–Friday 09:00–18:00 and no breaks or exclusions, an
interval from Friday 17:00 to Monday 10:00 is 65 elapsed hours but two working
hours. Changing the report calendar recalculates the same source intervals.
Overnight shifts are not supported in this release.

Issue selection and measured history are separate. A JQL condition on `created`
chooses issues; **Measure history during** clips the history being measured.
For business time, use the calendar timezone for its schedule; the report's
measurement timezone also explains date-window boundaries and displayed dates.
Read the applied window shown with the result rather than assuming browser time.

## Compare and save

Under **Group results**, group by project, current assignee, issue type or
component. Choose **Total** or **Mean per contributing issue**. Grouping uses
current issue fields; it does not reconstruct historical team membership.

A mean excludes issues with no observed value for that metric. An observed zero
is included. An issue with several components may appear in several component
groups. The Time in Status summary counts each issue once per metric and shows
its own scope. Entrance-date reports stay in issue rows.

Use **Save as new** to name a private report configuration. Select it later and
run it to get current data. **Update saved report** changes that configuration;
**Delete saved report** removes it. Saved views do not freeze the result data.
Last-used inputs are remembered separately in this browser and may disappear
when browser storage is cleared; named saved views are stored by the app.

## Share and schedule a report

Share a saved report configuration when teammates need to use the same settings.
Each viewer calculates results with their own Jira permissions. Sharing settings
does not grant access to issues or to your downloaded files.

To prepare recurring exports, share your saved report and open **Schedule this
report**. Choose weekly or monthly, select the day and local hour, review the
shown timezone, and choose **Create schedule**. Runs use the owner's current
Jira access and are picked up by the hourly scheduler. The resulting XLSX appears
in **Large and XLSX exports** and expires after 24 hours. You can update or delete
the schedule from the same section.

## Export and recover

Run a report and choose its CSV export action. When preparation finishes, use
**Download CSV** and complete the browser's save dialog if shown. Export prepares
a fresh calculation, so the cutoff and open durations may differ from the
previously displayed result. CSV includes raw values and units, filters, calendar,
measurement window, completeness, scope, report type, grouping and aggregation.

**One search page** covers only that page. **All search pages** collects results
in smaller requests within application limits. Jira search membership can change
while collecting pages; this is not an atomic database snapshot.

For a background export, open **Large and XLSX exports** and choose **Export all
as CSV** or **Export all as XLSX**. The job continues if you close the tab. Return
to see its status and progress; when ready, choose **Prepare download**, then
**Download**. You can cancel a queued or running export. Grouped reports also
offer **Contributing issues XLSX** to export the underlying issues.

Background files expire after 24 hours. Download a copy before expiry, or start a
new export afterward. Check completeness before using the file; application
limits still apply to background exports.

| Situation | Action |
|---|---|
| Invalid JQL | Correct the query and run again. |
| Report settings could not load | Use the displayed retry action; saved views are not overwritten by the failure. |
| Selected calendar unavailable | Choose an available calendar or 24/7 explicitly, then run again. |
| Partial result | Read the issue errors. Do not treat missing values as zero or a partial total as complete. Narrow the selection or rerun after resolving the source error. |
| Timeout | Try 10 issues per page or narrow JQL if automatic recovery cannot complete. All-pages mode processes smaller batches but still has limits. |
| Cache unavailable | Use the direct result; ask a Jira administrator to enable the workflow field if the report offers that action. |
| License-required error | Ask the Jira administrator to check the Marketplace trial/subscription. Saved configuration is retained. |

For support, include the error message, approximate time, metric, scope and
calendar configuration. Start with issue counts and a redacted example rather
than exporting a whole customer dataset. Contact the [Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
