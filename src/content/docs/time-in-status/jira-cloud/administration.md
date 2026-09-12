---
title: "Setup and Administration"
description: "Prepare the app and enable reusable workflow history for your projects."
---

Jira administrators manage working calendars and the workflow field. Report viewers use their existing Jira permissions.

## Open the app

After installation, open **Apps → Time in Status → Reports**. The app also has a project page and a **Time in Status** issue panel.

If **Preparing Time in Status** appears, allow setup to finish. Use **Refresh setup status** to check progress. A Jira administrator can select **Request setup (Jira admin)** if another attempt is needed. Reports open when setup completes.

## Enable the workflow field

The app can reuse workflow history to speed up later reports. Direct calculation remains available without it.

1. Open **Workflow field** in the app.
2. Select the **Project**.
3. Review the configuration message.
4. Select **Enable workflow field for project**.
5. Return to Reports and run again to verify availability.

:::note[Shared field configurations]
Enabling applies to all issue types in the project. Jira may also apply it to projects sharing the same field configuration.
:::

The **Fulstech Workflow History** field is managed automatically. Users do not create or edit its snapshot values.
If Jira has not applied the change yet, use **Refresh settings** and rerun the report after a short wait.

## Manage working calendars

Follow [Working Calendars](../working-calendars/) to create or edit a schedule.
Deleting a calendar requires saved reports that use it to select another calendar. The default calendar cannot be deleted.

## Inspect one issue

Open the **Time in Status** panel on a Jira issue to see its status visits and recorded transitions. Use **Refresh history** to retrieve changes.
For history using a report's selected calendar and period, run the report and choose **View history** on its issue row.
