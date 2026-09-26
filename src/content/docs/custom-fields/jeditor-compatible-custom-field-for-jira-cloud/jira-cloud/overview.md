---
title: "JEditor-compatible Custom Fields for Jira Cloud"
description: "Use rich-text fields in Jira Cloud and preserve JEditor content during a Data Center or Server migration."
---

JEditor-compatible Custom Fields for Jira Cloud provides a rich-text editing experience for Jira issue content. It is designed for teams migrating content from **JEditor - Rich Text Editor for Jira** on Jira Data Center or Server, and for teams that need a JEditor rich-text field in Jira Cloud.

The app supports two field paths:

- **Migrated fields:** Jira **Description** and **Text Field (multi-line)** fields that receive JEditor content migrated from Data Center or Server.
- **New fields:** fields created with the app's **JEditor Rich Text** custom field type.

Project administrators choose which fields and issue types use JEditor. Users view and edit the configured content in the **JEditor Fields** panel on an issue. Templates can provide reusable HTML content for each configured field.

The issue panel is the canonical rich-text view and edit surface. The native Jira presentation of a field can be a plain-text or search-oriented fallback and must not be used as a replacement for the JEditor Fields panel.

## Before you begin

These instructions apply to the Forge version of the app. If your project settings still show **JEditor-compatible Fields** instead of **JEditor Fields**, your site is using the earlier Connect version. Contact [Fulstech support](../support/) before changing an established migration workflow.

You need:

- permission to administer the Jira project to configure fields, issue types, and templates;
- permission to browse and edit the relevant issues to use the issue panel; and
- a Jira field that follows one of the supported field paths above.

Install or manage the app from its [Atlassian Marketplace listing](https://marketplace.atlassian.com/apps/1231698/jeditor-compatible-custom-fields-for-jira).

## Next steps

- [Configure fields, issue types, and templates](../create-a-markdown-enabled-custom-field/)
- [Migrate JEditor content from Jira Data Center or Server](../migrate-to-jira-cloud/)
- [Get support](../support/)

:::note[Product relationship]
Fulstech does not develop the original JEditor - Rich Text Editor for Jira Data Center or Server app. Fulstech develops this Jira Cloud app to provide a compatible migration and editing path.
:::
