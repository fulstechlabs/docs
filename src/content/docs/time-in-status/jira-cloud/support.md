---
title: "Troubleshooting and Support"
description: "Resolve report errors, unavailable calendars and workflow-field setup problems."
---

Contact the [Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
for help or feature requests.

| Situation | Next step |
| --- | --- |
| Setup not complete | Use **Refresh setup status**; a Jira administrator can choose **Request setup (Jira admin)**. See [Setup](../administration/). |
| Shared report unavailable | Ask its owner whether sharing was stopped or the configuration was deleted. Jira access can also affect results. |
| Export expired | Create a new export; background files expire after 24 hours. |
| Invalid JQL | Correct the syntax and run again. Basic project filtering is also available. |
| First report is slow | Reading issue history can take longer than using a valid workflow cache. Keep the report tab open while batches run. |
| Timeout after retry | Choose 10 issues per page or narrow the JQL. Avoid repeatedly starting the same large request. |
| Partial result | Read the issue errors. Missing values are not zero and partial totals are not complete totals. |
| Calendar unavailable | Select an available calendar or explicitly choose 24/7. |
| Workflow cache unavailable | Direct history calculation remains available. A Jira administrator can review the Workflow field screen. |
| License required | Ask a Jira administrator to check the trial or subscription. |
| Saved inputs disappeared | Last-used inputs live in browser storage. Use named private saved reports for reusable configuration. |

All-pages collection is bounded to 5,000 selected issues and a bounded result
size. Large selections may need narrower filters. Jira search membership can
change during traversal; a report is not an atomic database snapshot.

Include the approximate time, error message, metric, issue count, scope and
calendar settings with a support request. Start with a redacted example rather
than uploading an entire customer dataset.

See the [user guide](../getting-started/) and
[Fulstech Service Level Agreement](/service-level-agreement-sla/).
