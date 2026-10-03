---
title: "Migrate to Jira Cloud"
---

This guide concerns **Server/Data Center → Jira Cloud**, using the legacy
Connect app and Jira text fields. It is not a Connect → Forge upgrade procedure.
The [Forge successor guide](../forge-successor/#plan-a-connect-to-forge-upgrade)
describes the separate, not-yet-public successor boundary.

> **info**
>
JEditor custom fields only Jira Data Center or Jira Server must be created by the [JEditor - Rich Text Editor For Jira](https://marketplace.atlassian.com/apps/1210768/jeditor-rich-text-editor-for-jira?tab=overview) plugin.

According to [this Atlassian's article](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/#Adding-additional-entities-using-CSV-import), custom fields created by add-ons are not migrated by default.

However, the migration is still possible by the following steps:

## **Migrate the custom fields' data**

After migrating your Jira data with Jira Cloud Migration Assistant, follow
[Atlassian's guidance](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/#Adding-additional-entities-using-CSV-import)
for additional entities. For this legacy workflow, use **Text Field (multi-line)**
as the destination for JEditor content. First validate a representative sample,
including tables, images, and equations, before a wider import. Keep your source
export until you have checked the destination values and rendering.

## Install the Jira Cloud app

Please see the instructions [here](../overview/).

## Configure the Jira Cloud app to render the new custom fields as JEditor

Please see the instructions [here](../create-a-markdown-enabled-custom-field/).
