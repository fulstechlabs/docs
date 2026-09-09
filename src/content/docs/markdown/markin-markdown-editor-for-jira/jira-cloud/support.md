---
title: "Troubleshooting and support"
description: "Resolve missing fields, save failures, rendering questions, and access issues."
---

## A field is missing

Check eligibility, the project mapping, and issue-type selection. Save settings after changes. For app-owned fields, check Jira field context and screens.

The panel is **Rich Text Custom Fields**; settings are **Markdown Fields**. Not every Paragraph schema is supported. See [Field configuration](../create-a-markdown-enabled-custom-field/).

## I cannot type in Jira's native field

App-owned fields are intentionally read-only in the native editor. Use the app panel on an existing issue. A missing input on Create is expected.

## Preview looks right but changes disappear

Preview is not Save. Return to **Edit**, click **Save**, and verify after reload. Save each field separately. Preserve the draft before leaving if a save fails.

## Access is denied or settings do not load

Check the app trial/subscription, issue access, edit permission, and project-administration permission. Complete any Jira app-access prompt through the authorized user or administrator, then reload.

Do not reinstall or uninstall a production app as the first troubleshooting step.

## Images show as links

This is intentional in Forge 3.6.0. External images are not fetched automatically. Attachment links still require Jira access.

## A formula or diagram shows source

Use the delimiters in the [syntax reference](../markdown-syntax/). Keep math outside code blocks. Diagrams need the supported container syntax, not only a fence labeled mermaid.

Try a minimal example in Preview, then save and reload. Native field, search, and list views do not run the full panel renderer.

## Content looks different after upgrading

Stop editing, preserve the source, and follow the [upgrade checklist](../upgrading-from-connect/). Do not clear mappings or recreate fields to work around missing content.

## Contact Fulstech

[Open a support request](https://fulstech.atlassian.net/servicedesk/customer/portals) or email [support@fulstech.com](mailto:support@fulstech.com).

Include the app version, project and field types, steps to reproduce, expected and actual results, and a redacted screenshot or minimal Markdown sample.

Never send passwords, API tokens, cookies, or confidential issue content. Review logs before attaching them.
