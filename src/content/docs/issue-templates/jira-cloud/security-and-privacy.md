---
title: "Security and Privacy"
description: "Understand app permissions, Forge-hosted storage, authorization, egress, and licensing boundaries."
---

Issue Templates & Hierarchy Builder runs on Atlassian Forge and uses Jira Cloud
APIs. Production version 3.0.0 is eligible for the **Runs on Atlassian**
program. The app declares no external remote, egress domain, or runtime
analytics service.

For the customer-facing privacy notice, read the
[app privacy policy](../privacy-policy/).

## Data stored by the app

Forge SQL stores the app-owned data needed to deliver and support the product:

- Template definitions, revisions, values, and compact field-schema metadata.
- Variables, hierarchy plans, comments, attachment references, and overwrite
  policy.
- Project, issue-type, group, account, and request-context availability rules.
- Defaults, durable runs, child outcomes, relations, and bounded audit events.
- Atlassian account IDs and display names selected for user-field values.

Jira issue provenance is also stored in an app-owned Jira entity property so
the issue panel and JQL functions can explain the relationship.

## Authorization

Most Jira operations run as the signed-in user and remain subject to normal
Jira project, issue, field, and workflow permissions. Where a background
trigger, workflow, queue, or UI Modification must use app authority, the app
validates the trusted context and required Jira permission before accessing or
changing customer data.

Template availability is enforced by the backend. Client-side visibility is
never treated as the permission check.

## Why permissions are requested

- Jira read/write permissions support field discovery, capture, preview,
  issue creation and updates, comments, opted-in attachments, links,
  transitions, and provenance.
- User read permission supports Jira user and group selection.
- Jira Software board and Sprint reads support typed Sprint values.
- Project read permission supports context validation and hierarchy mapping.
- Jira configuration management supports administrator-enabled native Create
  rules.
- App-data permissions support the app-owned provenance entity property.

The manifest is reviewed for minimum scope before each production release.

## External processing and secrets

The app does not send customer data to a Fulstech service or third-party
processor. It does not request Atlassian passwords, personal access tokens, or
customer API secrets. Runtime artwork is bundled with the Forge app.

## Licensing

Production mutations fail closed unless Atlassian reports an active trial or
paid license. Read-only configuration remains available so customers can
understand existing data and obtain support.

