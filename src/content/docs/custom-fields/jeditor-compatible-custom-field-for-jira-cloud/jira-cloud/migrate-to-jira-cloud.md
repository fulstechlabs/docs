---
title: "Migrate JEditor Content to Jira Cloud"
description: "Move JEditor field values from Jira Data Center or Server into supported Jira Cloud fields."
---

Use this workflow when source issues contain fields created by **JEditor - Rich Text Editor for Jira** on Jira Data Center or Server.

Atlassian's migration tools do not automatically recreate every app-provided custom field type in Jira Cloud. The migration therefore uses a Jira Cloud **Text Field (multi-line)** field as the destination for each migrated JEditor field. The Cloud app then presents that destination field in the **JEditor Fields** panel.

## 1. Prepare the migration

Before importing data:

1. Inventory each source JEditor field, the projects and issue types that use it, and its Jira field ID.
2. Back up the source data and keep the export unchanged until validation is complete.
3. In Jira Cloud, create a separate **Text Field (multi-line)** destination field for each source JEditor field.
4. Record the source-to-destination field mapping.
5. Test the process with a small, representative set of issues before migrating all data.

Include examples with headings, lists, links, tables, code blocks, and any other formatting that matters to your users.

## 2. Move the field values

First migrate the Jira projects and issues with Jira Cloud Migration Assistant. Then follow Atlassian's guidance for [importing additional entities and field values with CSV](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/#Adding-additional-entities-using-CSV-import).

Import each source JEditor value into its mapped Jira Cloud **Text Field (multi-line)** field. Do not import migrated values directly into the app's **JEditor Rich Text** field type.

## 3. Install and configure the Cloud app

1. Install the app from its [Atlassian Marketplace listing](https://marketplace.atlassian.com/apps/1231698/jeditor-compatible-custom-fields-for-jira).
2. For each migrated project, open **Project settings** > **Apps** > **JEditor Fields**.
3. Add each destination field and select the issue types that use it.
4. Select **Save**.

See [Configure JEditor Fields](../create-a-markdown-enabled-custom-field/) for the complete configuration and editing workflow.

## 4. Validate before cutover

For every mapped field and issue type:

1. Open a migrated issue and confirm that the **JEditor Fields** panel appears.
2. Compare the rendered content with the source issue.
3. Edit a copy or test issue, save it, reload the page, and confirm the saved value.
4. Check a representative sample of simple and complex content.
5. Record any unsupported formatting and resolve it before users begin editing production issues.

Keep the source backup and field-mapping record until stakeholders accept the migrated content. Do not delete the source fields or migration files solely because the import completed.

## Upgrade from the earlier Jira Cloud version

The Forge successor keeps the existing Marketplace app identity and Connect app key so Atlassian can deliver it as an upgrade to the earlier Jira Cloud app. Existing mappings and templates use compatible Jira project-property keys. Even so, validate a representative project after the upgrade before rolling it out broadly.

If your site still shows **JEditor-compatible Fields** in project settings, it is using the earlier Connect interface. [Contact Fulstech support](../support/) before changing a production migration configuration.
