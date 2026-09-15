---
title: "Choose the right macro"
description: "Select the correct inline, display, MathJax, TeX Live, reference, or equation-list macro."
---

Start by deciding whether you are creating a formula, linking to one, or listing several equations.

## Everyday equations: use MathJax

Choose **LaTeX Math — inline** or **LaTeX Math — display** for ordinary mathematical notation such as fractions, matrices, calculus, statistics, and physics formulas.

MathJax provides the faster authoring experience:

- synchronized source and visual editors;
- Formula Library;
- Math Actions and matrix tools;
- a virtual keyboard;
- Undo and Redo;
- display alignment and reference metadata.

Use **inline** inside a paragraph. Use **display** when the formula needs its own line, alignment, or more horizontal space.

## Packages, plots, and diagrams: use TeX Live

Choose **Advanced LaTeX — inline** or **Advanced LaTeX — display** when your content needs a full LaTeX document and packages such as:

- `pgfplots` for plots;
- `tikz` for diagrams;
- `chemfig` for chemistry structures.

Advanced macros use a source editor and rendered preview. They do not include Formula Library, the MathJax visual editor, Math Actions, or the virtual keyboard.

## Link to one equation

Choose **LaTeX reference** after the target formula has a **Reference key** and the page containing it has been published. The reference displays the equation number and takes the reader to that formula.

## List several equations

Choose **LaTeX equation list** to build a navigable index from:

- the current page;
- another selected page;
- the selected page and its published child pages.

Only formulas with a Reference key appear in references or equation lists.

## Quick decision table

| Need | Choose |
| --- | --- |
| Short formula in a sentence | **LaTeX Math — inline** |
| Formula on its own line | **LaTeX Math — display** |
| Package-based inline output | **Advanced LaTeX — inline** |
| Plot, chemistry structure, or diagram | **Advanced LaTeX — display** |
| Link to a numbered equation | **LaTeX reference** |
| Index equations across content | **LaTeX equation list** |

