---
title: "Release notes"
description: "Customer-visible changes in LaTeX for Confluence Cloud."
---

## Forge 6.0.0 — September 15, 2026

Marketplace status: Public. Source release: 7.18.0.

### Formula authoring

- Added synchronized source and visual editing for MathJax formulas.
- Added Formula Library with 44 ready-made formulas and 11 reusable structures.
- Added Math Actions, a matrix picker, and a docked virtual keyboard with Numeric, Symbols, Alphabetic, and Greek layouts.
- Added shared Undo and Redo across source, visual, library, Math Actions, and keyboard input.
- Moved display alignment to clear left, center, and right toolbar actions.

### References and equation lists

- Separated optional **Display label** from the technical **Reference key**.
- Added guided same-page and cross-page equation pickers.
- Saved selected page IDs so cross-page references tolerate page title changes and moves.
- Added **LaTeX equation list** with optional descendant pages and reader-friendly names.
- Improved published reference focus, navigation, duplicate-key handling, and content-sized layout.

### Rendering and exports

- Moved formula processing to Atlassian-hosted Forge functions and a Forge Container, with no Fulstech remote renderer.
- Added Forge Object Store caching for derived SVG and PNG output and KVS caching for derived reference indexes.
- Improved inline/display sizing and PDF/Word export layout.
- Kept existing supported Connect-format formulas and reference configurations compatible with the Forge app.

### Administrator action

This release adds the read-only `read:hierarchical-content:confluence` scope for equation lists that include child pages. Atlassian therefore presents it as a major Forge upgrade. Existing sites must have an administrator approve the new permission before they move from the previous major version.
