---
title: "Troubleshooting and Support"
description: "Resolve report, sharing, dashboard and background export problems in Time in Status 3.0.0."
---

Contact the [Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
for help or feature requests.

| Situation | Next step |
| --- | --- |
| Setup not complete | Use **Refresh setup status**; a Jira administrator can choose **Request setup (Jira admin)**. See [Setup](../administration/). |
| Invalid JQL | Correct the syntax and run again. Basic project filtering is also available. |
| First report is slow | Reading issue history can take longer than using a valid workflow cache. Keep the report tab open while interactive batches run. |
| Timeout after retry | Choose 10 issues per page or narrow the JQL. Avoid repeatedly starting the same large request. |
| Partial result | Read the issue errors. Missing values are not zero and partial totals are not complete totals. |
| Shared report unavailable | Ask its owner whether sharing was stopped or the saved configuration was deleted. Jira access can also affect the calculated result. |
| Dashboard gadget is unavailable | Confirm the saved report still exists. Share its configuration if other dashboard viewers need to use it, then verify the viewer can access the selected Jira issues. |
| Background export stays queued | Leave the job available for recovery and refresh the export list later. If it does not progress, include its created time and status in a support request. |
| Background export failed | Read the bounded error message. Verify Jira access, report settings and the selected calendar, then start a new export. |
| Background export expired | Create a new export; background files expire after 24 hours. |
| Cancelled export is still listed | The status records the cancelled job. Start a new export if needed; cancelled/expired metadata is pruned from the recent-job window later. |
| Calendar unavailable or changed | Select an available calendar, or explicitly choose 24/7, and start a new report/export. |
| Workflow cache unavailable | Direct Jira history calculation remains available. A Jira administrator can review the **Workflow field** screen. |
| License required | Ask a Jira administrator to check the trial or subscription. |
| Saved inputs disappeared | Last-used inputs live in browser storage. Use named saved reports for reusable configuration. |

Interactive all-pages collection is bounded to 5,000 selected issues; background exports are bounded to 20,000 selected issues. Page and result-size limits can require narrower filters. Jira search membership can change during traversal, so a report or export is not an atomic database snapshot.

Include the approximate time, exact error message, metric, issue count, scope, calendar and export status with a support request. Start with a redacted example or sanitized screenshot. Do not send passwords, tokens or unnecessary customer data.

See the [User Guide](../getting-started/), [Exports](../exports/) and
[Fulstech Service Level Agreement](/service-level-agreement-sla/).
