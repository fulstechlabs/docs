---
title: "Security and privacy"
description: "Data handling and permissions for Jira Markdown Forge 3.6.0."
---

This technical summary covers **Forge Cloud 3.6.0**, not the older Connect runtime or other Fulstech apps. It supplements the [Fulstech privacy policy](/privacy-policy/) and [security policy](/security-policy/).

## Processing and storage

Markdown, math, and diagrams render in packaged Forge Custom UI in the browser. Forge functions read and write Jira data. This release has no Forge Remote, external renderer, or declared external network permissions.

Content is stored in Jira fields. Project properties hold mappings and settings; Jira issue properties also hold a mirror of app-owned field values. There is no separate Fulstech database, Forge KVS, or Forge Object Store.

Images become links rather than being fetched automatically. Opening external links is a separate user action. Information you choose to send to support is separate from normal app rendering.

## Access controls

The app checks caller permissions before privileged issue reads and saves. Settings require project-administration permission. Installation does not grant users access to restricted issues.

| Permission | Purpose |
| --- | --- |
| Read Jira work | Load issues, fields, issue types, and properties |
| Write Jira work | Save supported fields and the issue-property mirror |
| Read Jira users | User-picker suggestions |
| Read Jira permissions | Caller permission checks |
| Manage Jira projects | Project field mappings and settings |

Raw HTML input is disabled and unsafe link schemes are rejected. Arbitrary HTML and scripts are not supported content.

## Logging and data lifecycle

App audit events use operation, outcome, and status metadata rather than intentionally logging Markdown bodies or credentials. Atlassian platform logging is separate. Review diagnostic output before sharing it.

Data follows its Jira storage lifecycle, not an app cache-expiry period. Removing a mapping does not delete a field. Arrange required backups and data handling with your Jira administrator before uninstalling or deleting fields.

## Procurement questions

The listing displays **Runs on Atlassian**. This is not itself GDPR certification, a guarantee of a particular residency region, or a bug-bounty claim. [Contact support](../support/) for product-specific security questions.
