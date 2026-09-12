---
title: "Exports"
description: "Download report results as CSV or XLSX, including large background exports."
---

Export report results for further analysis or to keep a local copy. Use a page
CSV for a small result, or a background export for all matching issues and XLSX.

## Export the current page

1. Run your report and review its scope and completeness.
2. Choose **Export this page as CSV**.
3. When preparation finishes, choose **Download CSV**.
4. Save the file using your browser's download controls.

The export recalculates results. Its cutoff and open durations may therefore
differ from the result previously displayed. Filters, calendar, measurement
window and completeness information help identify what the file covers.

## Export all matching issues

1. Configure the report you want to export.
2. Expand **Large and XLSX exports**.
3. Choose **Export all as CSV** or **Export all as XLSX**.
4. Review the job's status and progress in the export list.
5. When ready, choose **Prepare download**, then **Download**.

The job continues after you close the tab. Return to the export list to check
its progress. Choose **Cancel** to stop a queued or running job.

For a grouped report, **Contributing issues XLSX** exports the underlying issues
so you can investigate the measurements behind grouped results.

## Keep a copy before expiry

Background export files expire after 24 hours. Download the file before expiry,
or create a new export afterward. Files already saved to your computer remain
under your control.

Sharing a report configuration does not share the owner's export files. Review
a downloaded file before distributing it, since it contains data available to
the person who generated it.

## Check the result

- Read completeness information before treating a total as complete.
- Missing values are not zero. Resolve issue errors or narrow the selection
  before rerunning a partial report.
- Large exports still have application limits. Narrow the project, JQL or
  measurement window if a job cannot complete.
- Jira issues can change while pages are collected. An all-issues export is not
  an atomic snapshot of Jira.

See [Troubleshooting and Support](../support/) if an export repeatedly fails.
