---
title: "Export and compatibility"
description: "Understand PDF, Word, page history, viewing, and legacy Connect-format behavior."
---

## PDF and Word export

Use Confluence's standard page actions to export a page to PDF or Word. The app supplies export-specific formula output so inline and display equations keep their placement, size, alignment, and equation numbers.

PDF and Word exports contain static equation labels. Reference links and equation-list navigation are interactive on the published Confluence page, not in the exported document.

Confluence—not the app—creates the Word file. The app supplies a higher-density PNG at the same logical display size. This avoids enlarging inline formulas while improving raster clarity. TeX Live formulas that are already PNG remain PNG.

## Viewing outside the desktop editor

Published formulas use Confluence macro views. Editing and macro configuration are supported through the Confluence page editor. A dedicated mobile editing workflow has not been verified for this release.

## Light and Dark appearance

Ordinary MathJax SVG output follows Confluence appearance while preserving colors explicitly written in the formula. PDF and Word use a paper-oriented presentation rather than the reader's current Dark appearance.

Advanced TeX Live PNG output keeps its image colors and canvas in both appearances.

## Page history

Historical page versions can render formula images. Historical equation numbering, reference navigation, and Equation List reconstruction are not supported; open the current published page to use those features.

## Existing Connect-format macros

The Forge app preserves the macro keys and reads legacy Connect configuration formats. Existing supported formulas and references continue to render after the Marketplace app upgrades from Connect to Forge. Opening an existing macro in Forge normalizes its configuration when you save it; you do not need to recreate the formula.

This compatibility does not migrate content from Confluence Data Center or Server. See [Cloud upgrades and Connect compatibility](../migrate-from-confluence-server-and-confluence-data-center/) for the distinction.
