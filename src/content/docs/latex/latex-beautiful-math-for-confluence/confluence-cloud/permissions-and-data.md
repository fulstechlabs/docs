---
title: "Permissions and data handling"
description: "Why LaTeX Math requests Confluence permissions and how Forge processes content."
---

LaTeX Math for Confluence uses Atlassian permissions only for the features that read pages, spaces, equation metadata, and app-owned cached render artifacts.

## Permission added in version 6

`read:hierarchical-content:confluence` allows the Equation List macro to enumerate child pages when **Include child pages** is enabled.

This permission:

- Is read-only.
- Does not allow the app to edit, move, or delete a page.
- Does not bypass Confluence permissions.
- Returns only content available to the current viewer.

Adding this scope caused Atlassian Forge to create major version 6 and require site-admin consent for the upgrade.

## Other access

The app uses Confluence read scopes to load published pages, page details, spaces, and equation configuration needed for rendering and references. `storage:app` stores app-owned render artifacts and reference indexes inside Atlassian Forge.

## Where processing happens

- MathJax equations are rendered by Forge functions.
- Advanced TeX Live equations are rendered in an Atlassian-hosted Forge Container.
- Rendered view and export artifacts may be cached in Forge Object Store for up to 90 days.
- Editor previews are session-only and are not written to Object Store.
- The current app declares no external remote and no external egress destination.

Removing an equation or changing its source naturally creates a different render result. Cached artifacts are addressed by their content and cannot replace a different formula.

## Runs on Atlassian

Forge reported Production version 6.0.0 as eligible for the Runs on Atlassian program. Processing and app-owned storage for this version remain on Atlassian-hosted Forge services.
