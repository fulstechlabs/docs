---
title: "Release notes"
description: "What's new in LaTeX Math for Confluence version 7.18.0."
---

## Version 7.18.0 — September 15, 2026

Marketplace version: Forge 6.0.0. Status: Public.

### Formula authoring

- Added a searchable Formula Library with 44 formulas and 11 reusable structures.
- Added synchronized source and visual editing.
- Added Math Actions and a docked virtual keyboard.
- Added unified Undo and Redo across typing, templates, visual edits, actions, and keyboard input.
- Replaced ambiguous toolbar glyphs with recognizable Atlassian-style icons.
- Added clear left, center, and right alignment controls for display equations.

### Equations and references

- Added an optional reader-friendly Display name separate from the stable Reference ID.
- Added a page picker that stores immutable Confluence page IDs.
- Added an equation picker for same-page and cross-page references.
- Added linked navigation that opens and scrolls to the selected equation.
- Added the **LaTeX equation list** macro for the current page or its child pages.
- Kept legacy Connect title-only and cross-space reference values compatible.

### Rendering and exports

- Added light and dark theme-aware MathJax output while preserving explicit formula colors.
- Kept editor previews session-only to reduce storage operations.
- Added content-addressed Forge Object Store caching for page views and exports.
- Kept MathJax in Forge functions and TeX Live in an Atlassian-hosted Forge Container.
- Improved sizing and alignment parity between the Confluence page, PDF, and Word exports.

### Upgrade note

This release adds the read-only `read:hierarchical-content:confluence` scope for Equation List child-page traversal. Atlassian therefore treats it as a major Forge upgrade. Existing customers remain on their working version until a site admin accepts the new permission.

See [Migration and Forge upgrades](../migrate-from-confluence-server-and-confluence-data-center/) and [Permissions and data handling](../permissions-and-data/) for details.
