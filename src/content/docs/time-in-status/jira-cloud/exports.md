---
title: "Exports"
description: "Download a page as CSV or prepare a large CSV/XLSX export."
---

Choose the export that matches the result you need.

| You need… | Choose… |
| --- | --- |
| The current report page | **Export this page as CSV** |
| All matching issues | **Export all as CSV** or **Export all as XLSX** |
| Issues behind grouped results | **Contributing issues XLSX** |

## Download a page

1. Run your report and review its scope and completeness.
2. Choose **Export this page as CSV**.
3. When ready, select **Download CSV** and save the file.

## Download a background export

1. Expand **Large and XLSX exports**.
2. Choose **Export all as CSV** or **Export all as XLSX**.
3. Check status and progress in the export list.
4. When ready, choose **Prepare download → Download**.

You can close the tab while the job runs. Return to the list to download it, or choose **Cancel** while it is queued/running.

:::tip[Download within 24 hours]
Background files expire after 24 hours. Save a copy before expiry or create a new export. Files already downloaded stay on your computer.
:::

<details>
<summary>Why can exported numbers differ from the screen?</summary>

Export recalculates results, so its cutoff and open durations can differ. Read the filters, calendar, measurement window and completeness included in the file.
Jira issues can change while pages are collected; all-issues exports are not atomic snapshots.

</details>

<details>
<summary>Partial or failed export?</summary>

Missing values are not zero. Review issue errors before using a partial total.
Background exports collect up to 20,000 issues, subject to page and data-size limits. Interactive all-pages reports collect up to 5,000 issues. A data-size limit can be reached sooner; narrow your project, JQL or measurement window and retry.
See [Support](../support/) for repeated failures.

</details>

Sharing a report configuration does not share your export files. Review downloaded data before passing it on.
