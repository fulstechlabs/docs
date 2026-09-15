---
title: "Usage"
description: "A complete guide to equations, formula templates, references, and equation lists."
---

## Insert an equation

1. Edit a Confluence page.
2. Type `/latex` or select **Insert → View more** and search for `latex`.
3. Choose the macro that matches the content:
   - **LaTeX Math — inline** for a formula inside a sentence.
   - **LaTeX Math — display** for a separate, optionally numbered equation.
   - **Advanced LaTeX — inline** or **Advanced LaTeX — display** for TeX Live packages.
4. Enter the formula and review the preview.
5. Select **Save**, then publish the Confluence page.

## Edit with source and visual modes

The MathJax editor provides two synchronized ways to work:

- **Source** is best when you already know LaTeX commands.
- **Visual** is best when you want to build or inspect the formula interactively.

Changing either editor updates the other. The rendered preview remains visible so you can confirm the result before saving.

The toolbar provides familiar **Undo**, **Redo**, and block alignment actions. Undo and Redo include changes made through typing, the visual editor, Formula Library, Math Actions, and the virtual keyboard.

## Use Formula Library

Open **Formula Library** from the editor toolbar to browse common formulas and reusable structures.

1. Search by a formula name, category, or LaTeX command.
2. Select a result to preview its source.
3. Insert it at the current cursor position.
4. Replace the example values with your own.

Inserting a template does not replace the surrounding source.

## Use Math Actions and the virtual keyboard

Use **Math Actions** for frequently used editing commands. Open the keyboard button for numbers, operators, relations, Greek letters, and common structures.

The keyboard is docked to the editor so it remains separate from the configuration fields. Closing the keyboard restores the full editor area without covering **Save** or **Cancel**.

## Align a display equation

Display macros support left, center, and right alignment. Select the corresponding toolbar icon while editing. Inline macros follow the surrounding sentence and therefore do not show alignment controls.

## Number an equation

Provide a **Reference ID** when an equation should receive a number.

- The Reference ID is the stable technical identifier used by links.
- **Display name** is an optional reader-friendly title.
- Leaving Display name empty does not prevent numbering.

Reference IDs should be unique within a page. If duplicates exist, the first matching equation is the link target.

## Link to an equation

1. Insert the **LaTeX reference** macro.
2. Choose **This page** or **Another page**.
3. For another page, search for and select the page. The app stores its immutable page ID, so renaming or moving the page does not break a new reference.
4. Select an equation from the equations found on that page.
5. Save and publish.

The published reference shows the equation number. Selecting it opens the correct page when needed and scrolls the matching equation into view.

Existing references created by older versions remain supported, including title-only and `SPACE:Page title` values.

## Create an Equation List

The **LaTeX equation list** macro creates a linked index from numbered equations.

1. Insert **LaTeX equation list**.
2. Choose whether to include only the current page or the current page and its child pages.
3. Save and publish.

The list is generated from published content and reflects the current equation order and display names. Each item links to its equation. Users only see equations from pages they are allowed to view.

Including child pages requires the `read:hierarchical-content:confluence` permission. See [Permissions and data handling](../permissions-and-data/) for details.

## Render advanced TeX Live content

Use an Advanced LaTeX macro when the source requires a document preamble or packages such as TikZ, PGFPlots, `mhchem`, or `chemfig`.

```latex
\documentclass{article}
\pagestyle{empty}
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}
\addplot3[surf] {exp(-x^2-y^2)*x};
\end{axis}
\end{tikzpicture}
\end{document}
```

Use `\pagestyle{empty}` to prevent page headers, footers, and page numbers from appearing in the rendered image.

TeX Live requires more processing than MathJax. Repeated page views and exports reuse Atlassian-hosted cached artifacts when available.

## Export and mobile viewing

Formulas, equation numbers, references, and Equation Lists are included in Confluence PDF and Word exports. Wide formulas are constrained to the document width, while inline formulas keep their natural size.

Published formulas can also be viewed in Atlassian's Confluence mobile apps.

## If a formula does not render

- Confirm that the source is valid LaTeX.
- Use MathJax for ordinary formulas and TeX Live only for package-dependent content.
- Include a complete document preamble for Advanced LaTeX.
- Check that a referenced equation has a unique Reference ID and that the page is published.
- If the problem continues, see [Support](../support/).
