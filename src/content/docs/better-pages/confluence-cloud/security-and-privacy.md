---
title: "Security and Privacy"
description: "Understand Better Pages permissions, stored data, external content controls, and export behavior."
---

Better Pages is implemented on Atlassian Forge and uses public Forge bridge and Confluence Cloud APIs.

## Confluence permissions

The app requests permission to:

- Read Confluence content summaries and user context needed by app features.
- Read spaces and search Confluence for permission-scoped search and usage reporting.
- Create Confluence pages and blog posts from templates as the current user.
- Use Forge app storage for installation settings and aggregate diagnostics.

Confluence continues to enforce the signed-in user's page and space permissions. Better Pages does not use app search to reveal content that the current reader cannot access.

## Data stored by Better Pages

Forge storage contains installation-scoped:

- Revisioned external frame and image policies.
- Local-form enabled/disabled state.
- Observed external frame and image URLs.
- Aggregate extended-capability view counters.

Aggregate counters do not include page IDs, users, search queries, or authored macro content. Normal macro configuration is part of the Confluence page. Template output is created directly as ordinary Confluence content.

Reader-entered search queries and local-form values are not persisted by Better Pages. Local-form values are not transmitted to the Forge backend.

## External content

External frames and images are disabled unless their destination passes both the Better Pages administrator policy and Atlassian customer-managed egress controls. Frame and image permissions are separate. Better Pages accepts HTTPS destinations only and rejects credentials in URLs.

When allowed, the reader's browser loads the external frame or image. That external service may have its own privacy policy and logging. Administrators should approve only destinations their organization trusts.

Better Pages does not proxy arbitrary URLs and does not run author-supplied HTML, CSS, or JavaScript.

## Static export

Interactive behavior cannot run in PDF or Word. Better Pages therefore exports bounded static representations:

- Safe destinations remain links.
- Tabs become sequential sections.
- Dialogs, rollover cards, and tooltips retain their important text.
- Search configuration is retained without freezing permission-sensitive results.
- Hidden content remains excluded.
- External content is represented by its approved text and URL rather than fetched into the file.
