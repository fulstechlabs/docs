---
title: "Sharing and Schedules"
description: "Share report settings and schedule recurring XLSX exports."
---

Save a useful report once, then reuse it with teammates or run it on a schedule.

## Share a report

1. Configure your report and choose **Save as new**.
2. With the saved report selected, choose **Share configuration**.
3. Copy the **Share link** and send it to your teammates.

:::note[Each viewer uses their own Jira access]
Sharing settings does not grant access to additional issues. Review the saved JQL before sharing; it is part of the shared configuration.
:::

Choose **Stop sharing** to disable existing links. Recipients can save their own private copy.

## Schedule an XLSX

1. Select a saved report and share its configuration.
2. Open **Schedule this report**.
3. Choose **Weekly** or **Monthly**, a day and local hour.
4. Review the timezone and select **Create schedule**.

| After setup | Where to look |
| --- | --- |
| Next run and last result | **Schedule this report** |
| Change or stop the schedule | **Update schedule** / **Delete schedule** |
| Download the XLSX | **Large and XLSX exports** |

Runs use the owner's current Jira permissions and require an active app license.
The hourly scheduler picks up due runs; execution is not guaranteed at an exact minute.
**Download files within 24 hours.** See [Exports](../exports/).

## Add a dashboard report

In your Jira dashboard, choose **Add gadget** and find **Workflow Time report**. Add it, select a saved report in the gadget configuration, then choose **Save gadget**.
Share the configuration if other dashboard viewers need it. Each viewer sees results based on their own Jira access.

The gadget shows a bounded report page of up to 25 issues. Open the full report to analyze a larger selection.
