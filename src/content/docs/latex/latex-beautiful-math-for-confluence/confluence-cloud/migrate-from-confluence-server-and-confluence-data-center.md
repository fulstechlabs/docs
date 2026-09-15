---
title: "Migration and Forge upgrades"
description: "Understand Data Center migration and the automatic Connect-to-Forge app upgrade."
---

## Existing Confluence Cloud customers

The Cloud app has moved from Atlassian Connect to Forge. Existing Cloud pages do not need a data migration wizard: Forge reads the macro configuration already stored in each page.

The following existing macro formats remain supported:

- MathJax and TeX Live inline and display macros.
- Connect v1 formula content.
- Older Connect v0 body content.
- Existing equation IDs and alignment values.
- Same-page, cross-page, and cross-space references.
- Legacy references that identify a page by title instead of page ID.

The upgrade does not rewrite Confluence pages in the background. A macro is written in the current Forge format only after a user opens it, changes it, and selects **Save**.

## Upgrade to Forge major version 6

Version 6 adds the Equation List feature and the read-only `read:hierarchical-content:confluence` scope used to enumerate child pages. Because the permission set changed, Atlassian requires a site admin to approve this major upgrade.

Until the admin approves it, the existing app version continues to run. The upgrade is not partially applied and existing pages are not modified.

After approval:

1. Existing macros render through Forge using their original macro keys.
2. Existing source and references remain available in the editor.
3. New features such as Formula Library, display names, page and equation pickers, and Equation List become available.
4. No external renderer or customer-run migration service is required.

## Confluence Data Center and Server

Moving content from Confluence Data Center or Server to Cloud is a separate process from the Connect-to-Forge Cloud upgrade. Start with the [Data Center migration guide](../../confluence-data-center-and-confluence-server/migrate-to-confluence-cloud/).

Before a production migration, test a representative space containing inline equations, display equations, TeX Live documents, numbered equations, and cross-page references. Keep a source backup until the Cloud pages and exports have been reviewed.

If migrated content displays an unknown macro or loses configuration, do not manually recreate a large page set. Contact [Fulstech Support](../support/) with the source product version, Cloud site, affected macro type, and one example page URL.
