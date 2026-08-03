# Migrate to Jira Cloud

> **info**
>
JEditor custom fields only Jira Data Center or Jira Server must be created by the [JEditor - Rich Text Editor For Jira](https://marketplace.atlassian.com/apps/1210768/jeditor-rich-text-editor-for-jira?tab=overview) plugin.

According to [this Atlassian's article](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/#Adding-additional-entities-using-CSV-import), custom fields created by add-ons are not migrated by default.

However, the migration is still possible by the following steps:

## **Migrate the custom fields' data**

After migrate all data from Jira Data Center or Jira Server to Jira Cloud using Jira Cloud Migration Assistant, follow the instructions in [this Atlassian's article](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/#Adding-additional-entities-using-CSV-import) to migrate JEditor fields to the Jira Cloud instance. Since Jira Cloud does not allow add-ons to add new custom field types, the Jira Cloud instance's custom fields to receive JEditor content must be of the type "Text Field (multi-line)".

## Install the Jira Cloud app

Please see the instructions [here](overview.md).

## Configure the Jira Cloud app to render the new custom fields as JEditor

Please see the instructions [here](create-a-markdown-enabled-custom-field.md).
