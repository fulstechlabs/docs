---
title: "Export and compatibility"
description: "Understand PDF, Word, mobile, page history, and legacy Connect-format behavior."
---

## PDF and Word export

Use Confluence's standard page actions to export a page to PDF or Word. The app supplies export-specific formula output so inline and display equations keep their placement, size, alignment, and equation numbers.

PDF and Word exports contain static equation labels. Reference links and equation-list navigation are interactive on the published Confluence page, not in the exported document.

Word output is generated as a higher-density PNG at the same logical display size. This avoids enlarging inline formulas while improving raster clarity. TeX Live formulas that are already PNG remain PNG.

## Mobile viewing

Published MathJax and Advanced LaTeX formulas render in Atlassian's Confluence mobile experience. Editing remains a Confluence page-editor workflow.

## Light and Dark appearance

Ordinary MathJax SVG output follows Confluence appearance while preserving colors explicitly written in the formula. PDF and Word use a paper-oriented presentation rather than the reader's current Dark appearance.

Advanced TeX Live PNG output keeps its image colors and canvas in both appearances.

## Page history

Historical page versions can render formula images. Historical equation numbering, reference navigation, and Equation List reconstruction are not supported; open the current published page to use those features.

## Existing Connect-format macros

The Forge app preserves the macro keys and reads legacy Connect configuration formats. Existing supported formulas and references continue to render after the Marketplace app upgrades from Connect to Forge. Opening an existing macro in Forge normalizes its configuration when you save it; you do not need to recreate the formula.

This compatibility does not migrate content from Confluence Data Center or Server. See [Cloud upgrades and Connect compatibility](../migrate-from-confluence-server-and-confluence-data-center/) for the distinction.

