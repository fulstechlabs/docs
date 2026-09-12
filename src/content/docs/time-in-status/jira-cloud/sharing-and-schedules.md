---
title: "Sharing and Schedules"
description: "Reuse report settings with teammates and prepare recurring exports."
---

Share a saved configuration so teammates can run the same report with their
own Jira access. Schedule recurring XLSX exports when you need regular results.

## Share a report

1. Configure a report and choose **Save as new**.
2. Give it a name that explains its purpose.
3. With that saved report selected, choose **Share configuration**.
4. Copy the **Share link** and send it to your teammates.

Each viewer runs the configuration using their own Jira permissions. Sharing a
report does not grant access to additional issues. Review the JQL and settings
before sharing, since they are part of the shared configuration.

Choose **Stop sharing** to disable existing links. A recipient can save a private
copy of a shared configuration; that copy is separate from the owner's report.

## Use a dashboard report

Add the Time in Status gadget to a Jira dashboard and choose a saved report in
its configuration. Share the report configuration if other dashboard viewers
need to use it. Each viewer sees results calculated with their own Jira access.

## Schedule an export

1. Select a saved report and share its configuration.
2. Expand **Schedule this report**.
3. Choose **Weekly** or **Monthly**, then select the day and local hour.
4. Review the displayed timezone and choose **Create schedule**.
5. Check the next-run and last-run information in the same section.

Scheduled reports use the owner's current Jira permissions. Runs are picked up
by the hourly scheduler, so the selected time is not an exact-minute guarantee.
The XLSX file appears in **Large and XLSX exports** and expires after 24 hours.

Use **Update schedule** to change the timing or **Delete schedule** to stop
recurring exports. Scheduled processing requires an active app license.

See [Exports](../exports/) for downloading files and checking their completeness.
