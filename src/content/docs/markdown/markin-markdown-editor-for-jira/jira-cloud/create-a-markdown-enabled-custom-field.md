---
title: "Configure Markdown fields"
description: "Configure existing Jira fields or the Forge-owned Rich Text Editor Custom Field."
---

## Choose a field

| Field | Behavior |
| --- | --- |
| Jira Description | Enable for selected issue types; Markdown is stored in a Jira document code block |
| Classic Jira multiline text field | Supported when its schema is Jira's standard textarea type |
| **Rich Text Editor Custom Field** | App-owned Forge string field; edited through the app panel |
| Other field types | Arbitrary single-line strings, numbers, selects, and other apps' fields are not supported |

A field named Paragraph is not necessarily compatible: the underlying Jira schema matters. Use the eligible fields shown in the selector. Do not assume every team-managed Paragraph field is supported. The documented validation baseline is company-managed Jira Software; check your project's configuration before rollout.

## Configure an existing field

1. Open **Project settings → Apps → Markdown Fields**.
2. Select a field and click **Add**.
3. Check the issue types that should show it in the panel.
4. Optionally enable **Also highlight Gherkin keywords**.
5. Click **Save** and open an issue of a selected type.

Repeat for each field and project. To disable a mapped field, click **Remove**, then **Save**. This removes its mapping, not the Jira field or stored content.

## Create an app-owned field

A Jira administrator can create a custom field using the app's **Rich Text Editor Custom Field** type.

1. Open Jira administration's custom fields page.
2. Create a field of type **Rich Text Editor Custom Field**.
3. Give it a name such as **Technical notes** and configure its context and applicable screens.
4. Return to **Project settings → Apps → Markdown Fields**. App-owned fields appear separately from the existing-field selector, with a Gherkin option.
5. Save any setting change. Open **Rich Text Custom Fields** on an issue to enter content.

App-owned fields use Jira field context for applicability, not the existing-field issue-type checkboxes.

:::note
The app-owned field is intentionally read-only in Jira's standard editor, including Create and transition forms. Edit it in the app panel after the issue exists.
:::

## Working alongside Jira's editor

Use the app panel consistently for Markdown content. Jira's native editor may show source or a code block instead of the formatted view.

Preserve a copy before enabling a populated Description. Saving through the app updates the field; it does not merge Markdown into an arbitrary existing rich-text document.

Do not delete or recreate fields when upgrading. See [Upgrading from Connect](../upgrading-from-connect/).
