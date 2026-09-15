---
title: "Troubleshooting"
description: "Resolve common formula, preview, reference, equation-list, permission, and license problems."
---

## A formula does not render

Check which engine the macro uses:

- For **LaTeX Math**, review the highlighted source error and simplify unsupported commands. Use a ready-made Formula Library entry to confirm the editor is working.
- For **Advanced LaTeX**, include `\documentclass`, `\begin{document}`, and `\end{document}`. Select **Preview** and correct the reported TeX error.
- If the content requires `tikz`, `pgfplots`, or `chemfig`, use an Advanced LaTeX macro rather than a MathJax macro.

## An Advanced LaTeX preview is still starting

On development or staging environments, the TeX Live container can scale to zero and needs time to start for an uncached formula. The editor retries a bounded startup response. Wait for the preview state to change before resubmitting.

If the message persists, copy the visible error text and contact support. Do not send confidential page content unless it is required and sanitized.

## A reference cannot find its equation

1. Open the target formula and confirm it has a non-empty **Reference key**.
2. Publish the target page; draft-only formulas are not available to the picker.
3. Reopen **LaTeX reference** and choose the equation from the picker.
4. For a legacy configuration that cannot be selected, use **Advanced: enter a legacy key** and enter the exact saved key.

Changing a Reference key does not rewrite existing reference macros. Update those sources explicitly.

## A reference does not navigate in the editor

This is expected. Editor-mode references are previews. Publish the page and select the reference in the published view.

## An equation list is empty or outdated

- Confirm that formulas have Reference keys and their pages are published.
- Confirm the selected source page is correct.
- Enable **Include child pages** if the equations are on descendants.
- Select **Refresh equations** after publishing source changes, or reload the page.
- Confirm the current reader can view the source pages.

Equation lists do not reconstruct historical page versions.

## The app reports “License required”

The paid Cloud app requires an active Atlassian Marketplace license or trial. Ask a site administrator to check the app subscription in **Manage apps**. Rendering, configuration, reference lookup, equation lists, and export are unavailable while the Marketplace license is inactive.

## Content looks different in Dark appearance

MathJax output follows Confluence appearance unless the formula specifies an explicit color. Advanced TeX Live output is a PNG and keeps its authored canvas and colors. Choose formula colors that remain readable on the intended background.

## Get more help

Follow [Support](../support/) and include the exact macro name, platform, reproduction steps, expected result, actual result, visible error text, and a sanitized screenshot.

