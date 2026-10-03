---
title: "Configure JEditor Fields"
description: "Map Jira fields to issue types, edit rich text from the issue panel, and create reusable templates."
---

A project administrator configures which supported fields appear in the **JEditor Fields** panel for each issue type.

## Choose a field path

Use one of these field paths before configuring the project:

| Goal | Field to use |
| --- | --- |
| Receive content migrated from Jira Data Center or Server | **Description** or a Jira **Text Field (multi-line)** field |
| Create a new app-owned field in Jira Cloud | A custom field created with the **JEditor Rich Text** field type |

For a migration, do not import the old JEditor value directly into a new **JEditor Rich Text** field. Import it into a Jira **Text Field (multi-line)** field first, then map that field as described below.

## Map a field to issue types

1. In the Jira project, open **Project settings**.
2. Under **Apps**, select **JEditor Fields**.
3. In **Select a Jira field**, choose a supported field and select **Add field**.
4. Under that field, select every issue type that should show it in the JEditor panel.
5. Select **Save** and wait for the **Saved** status.

Repeat these steps for each field that needs the rich-text experience. Use **Remove field** to remove a mapping; this removes the field from the app configuration, not from Jira.

## Edit a configured field

1. Open an issue whose type is mapped to the field.
2. Find and open the **JEditor Fields** panel.
3. Under the field name, select **Edit**.
4. Add or format the content in the editor.
5. Select **Save** and wait for the **Saved** status.
6. Reload the issue and confirm that the content is still present in the JEditor Fields panel.

:::caution
Use the **JEditor Fields** panel to edit mapped rich-text content. The **JEditor Rich Text** field type is read-only in Jira's native field surfaces, and migrated multi-line fields can display their stored source differently outside the panel.
:::

## Create and use templates

Templates are configured per project and per field.

1. Go to **Project settings** > **Apps** > **JEditor Fields**.
2. Find the configured field and select **Templates**.
3. Select **Add template**.
4. Enter a title, optional description, and the HTML content to insert.
5. Select **Save templates** and wait for the **Saved** status.

To use a template, edit the field from the issue panel, select a template, and select **Insert template**. Review the inserted content before saving the field.

## If the panel or field is missing

Check that:

- the field was added and the current issue type was selected before saving;
- the issue belongs to the project where the mapping was configured;
- you have permission to browse and edit the issue; and
- the field is **Description**, **Text Field (multi-line)**, or **JEditor Rich Text**.

If the configuration still does not appear, collect the project key, issue key, field name, issue type, and app version, then [contact Fulstech support](../support/).
