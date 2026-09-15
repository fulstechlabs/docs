---
title: "LaTeX for Confluence Cloud"
description: "Create, edit, number, reference, and export mathematical formulas in Confluence Cloud."
---

LaTeX for Confluence adds editable mathematical notation to ordinary Confluence pages. Use it for a formula inside a sentence, a numbered display equation, a TeX Live plot or chemistry diagram, or an index that links readers to equations across pages.

The Cloud app runs on Atlassian Forge. Formula processing and derived render storage stay within Atlassian-hosted Forge services; the app does not send formulas to a Fulstech server or another external rendering service.

If you use Confluence Data Center or Server, see the [Data Center and Server guide](../../confluence-data-center-and-confluence-server/overview/).

## What you can do

- Write everyday equations with synchronized **LaTeX source** and **Visual editor** surfaces.
- Start from 44 ready-made formulas or 11 reusable structures in **Formula Library**.
- Insert symbols and structures with **Math Actions** and the docked virtual keyboard.
- Place formulas inline or on their own line and align display formulas left, center, or right.
- Give equations stable reference keys and reader-friendly display labels.
- Link to equations on the same page or another page without copying a technical key.
- Build an equation list from one page and, optionally, its child pages.
- Render advanced packages such as `pgfplots`, `tikz`, and `chemfig` with TeX Live.
- Keep formulas in Confluence PDF and Word exports.

## How the app fits into Confluence

While editing a Confluence page, type `/LaTeX` and choose one of the six app macros:

| Macro | Use it for |
| --- | --- |
| **LaTeX Math — inline** | A MathJax equation within a sentence. |
| **LaTeX Math — display** | A MathJax equation on its own line, with optional alignment and numbering. |
| **Advanced LaTeX — inline** | TeX Live content with packages, placed inline. |
| **Advanced LaTeX — display** | TeX Live content with packages, plots, or diagrams on its own line. |
| **LaTeX reference** | A numbered link to a referenceable equation on this page or another page. |
| **LaTeX equation list** | A navigable list of referenceable equations from a page and optionally its descendants. |

MathJax is the best default for most equations. Choose an Advanced LaTeX macro only when you need a full LaTeX document or packages that MathJax does not provide.

References and equation lists use the current published version of pages the reader can access. They do not reconstruct historical numbering or navigation from an older page version.

## Start here

Follow [Create your first equation](../getting-started/) to add `E=mc^2` to a page and publish a result. Then use the [guide index](../usage/) to find the next task.

Administrators and evaluators can review [security, privacy, and data handling](../permissions-and-data/). Existing customers moving from the Connect version should read [Cloud upgrades and Connect compatibility](../migrate-from-confluence-server-and-confluence-data-center/).

## Platform and licensing

This guide applies to the paid Confluence Cloud app. An active Atlassian Marketplace license is required for customer use. Install or start a trial from [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1216800/latex-beautiful-math-for-confluence?hosting=cloud&tab=installation).
