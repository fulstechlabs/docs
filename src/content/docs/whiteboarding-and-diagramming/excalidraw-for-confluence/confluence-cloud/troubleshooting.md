---
title: "Troubleshooting"
description: "Resolve common macro, editor, preview, library, rendering, and license problems in Confluence Cloud."
---

This page applies to the published Forge app, Cloud **3.0.0**. Sites still using
the separate **Open Editor** dialog can follow the [legacy Connect guide](../usage/).
The [Cloud feature reference](../feature-reference/) also explains editor-specific
messages.

## Start with the stage that failed

| Symptom | Start here |
| --- | --- |
| You cannot find the macro | [The diagram macro is not available](#the-diagram-macro-is-not-available) |
| The macro exists but its editor does not open | [The diagram editor does not open](#the-diagram-editor-does-not-open) |
| The editor saved but readers see the old page | [The editor closed but the published page did not change](#the-editor-closed-but-the-published-page-did-not-change) |
| A text-defined diagram shows an error | [A Mermaid, Graphviz, or PlantUML diagram does not render](#a-mermaid-graphviz-or-plantuml-diagram-does-not-render) |
| A published diagram is empty or missing | [A published diagram is blank or missing](#a-published-diagram-is-blank-or-missing) |

## The diagram macro is not available

- Confirm that **Excalidraw, Mermaid, PlantUML - Whiteboard for Confluence** is
  installed on the site and has an active license or trial.
- Edit a page and search for the exact macro name from
  [Choose the right diagram macro](../choose-a-diagram/).
- If you can request apps but cannot install them, ask a Confluence site
  administrator to review the Marketplace app request.

## The diagram editor does not open

1. Keep the Confluence page editor open. Select the existing macro and retry
   **Edit** once. On legacy Connect sites, retry **Open Editor** instead.
2. Reload the page only after copying or exporting any unsaved text or diagram
   content you still need.
3. Check whether a browser extension or organizational browser policy blocks
   embedded app dialogs.
4. If the problem continues, record the macro name, browser, visible error, and
   whether other app macros open on the same page.

Do not delete and reinsert an existing macro merely to clear an editor error;
that can remove the only editable copy attached to the page.

## The editor closed but the published page did not change

The Forge workflow has two save boundaries:

1. **Save** in the diagram editor applies the diagram to the page draft. DrawIO
   uses **Save & Exit**. Wait for a successful return to Confluence.
2. **Publish** or **Update** makes the page draft visible to readers.

Complete both steps and reload the published page. If Save reports that the
macro is not confirmed in the draft, keep the editor open and retry after the
draft is ready. Repeatedly clicking Update does not complete a failed diagram
save. Keep the original macro and contact support if the problem persists.

## A published diagram is blank or missing

- Open Confluence page history and confirm whether an earlier published version
  still shows the expected diagram.
- Edit the current macro only to inspect it. If its source or scene is missing,
  cancel without saving.
- Record the page URL and version before making further changes.

Do not save an empty editor over a diagram you are trying to recover. A page
version or exported editable source is more useful than a screenshot when the
diagram must remain editable.

## A Mermaid, Graphviz, or PlantUML diagram does not render

- Confirm that the source belongs to the selected macro language.
- Use **Show preview** when the editor provides it and fix the first reported
  syntax error.
- Reduce the source to a small known-valid example from the
  [text-defined diagram guide](../text-diagrams/) to separate a syntax problem
  from an app or browser problem.
- For PlantUML code that includes remote files, confirm that your organization
  permits the referenced destination and try a self-contained example.

Keep a copy of the failing source before simplifying it.

## Personal Library items are missing

Personal Library items are browser-local. They can be absent after changing
browsers or profiles, clearing site data, or using private browsing. Import a
previously exported `.excalidrawlib` file. Saving or restoring a Confluence page
does not restore the browser library.

## The app reports an invalid license

Ask a site administrator to check the app subscription under **Manage apps**.
Include the exact error and macro name in a support request; do not include
license keys or billing information in a screenshot.

## Get more help

Follow [Support](../support/) and include the platform, exact macro name,
reproduction steps, expected result, actual result, visible error, and a
sanitized screenshot.
