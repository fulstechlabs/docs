---
title: "Overview"
description: "Create, edit, number, reference, and export LaTeX equations in Confluence Cloud."
---

LaTeX Math for Confluence brings a visual formula editor, MathJax, and TeX Live to Confluence Cloud. Use it for quick inline notation, numbered display equations, chemistry, plots, and reusable equation references.

[Install LaTeX Math for Confluence from Atlassian Marketplace](https://marketplace.atlassian.com/apps/1216800/latex-beautiful-math-for-confluence?hosting=cloud&tab=installation).

> Using Confluence Data Center or Server? See the [Data Center and Server documentation](../../confluence-data-center-and-confluence-server/overview/).

## What you can do

- Write LaTeX source or build a formula visually with synchronized editors.
- Search and insert from a library of common formulas and structures.
- Use a docked math keyboard for symbols, Greek letters, fractions, roots, sums, and integrals.
- Add a stable reference ID and a reader-friendly display name to an equation.
- Link to numbered equations on the same page, another page, or another space.
- Generate an Equation List for the current page or its child pages.
- Render advanced TeX Live documents with packages such as TikZ, PGFPlots, and chemistry packages.
- Preserve formulas and references in Confluence PDF and Word exports.

## Choose the right macro

| Need | Macro | Renderer |
| --- | --- | --- |
| Formula inside a sentence | **LaTeX Math — inline** | MathJax |
| Numbered or aligned display equation | **LaTeX Math — display** | MathJax |
| Advanced package output inside a sentence | **Advanced LaTeX — inline** | TeX Live |
| TikZ, plots, chemistry, or full documents | **Advanced LaTeX — display** | TeX Live |
| Link to a numbered equation | **LaTeX reference** | Forge |
| Build a linked equation index | **LaTeX equation list** | Forge |

MathJax is the recommended choice for most equations because it previews quickly. Choose TeX Live only when the formula depends on a LaTeX package or document preamble.

## Start here

1. Open a Confluence page and select **Edit**.
2. Type `/latex` and choose an inline or display macro.
3. Enter a formula, or open **Formula Library** to insert a template.
4. Review the rendered preview and select **Save**.
5. Publish the page.

Continue with the [complete usage guide](../usage/), learn about [permissions and data handling](../permissions-and-data/), or review [version 7.18.0](../release-notes/).

## Cloud architecture

The current Cloud app runs on Atlassian-hosted Forge infrastructure. MathJax is rendered in Forge functions, while advanced TeX Live rendering uses an Atlassian-hosted Forge Container. The app has no external remote or egress destination.
