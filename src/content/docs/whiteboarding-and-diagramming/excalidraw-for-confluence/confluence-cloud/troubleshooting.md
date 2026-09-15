---
title: "Troubleshooting"
description: "Resolve common macro, editor, preview, library, rendering, and license problems in Confluence Cloud."
---

This page starts with the current Marketplace Connect app. If your macro opens
directly into a full-page Forge editor, use the troubleshooting guidance inside
the [Forge preview guide](../forge-preview/).

## The diagram macro is not available

- Confirm that **Excalidraw, Mermaid, PlantUML - Whiteboard for Confluence** is
  installed on the site and has an active license or trial.
- Edit a page and search for the exact macro name from
  [Choose the right diagram macro](../choose-a-diagram/).
- If you can request apps but cannot install them, ask a Confluence site
  administrator to review the Marketplace app request.

## Open Editor does not open the canvas

1. Keep the Confluence page editor open and retry **Open Editor** once.
2. Reload the page only after copying or exporting any unsaved text or diagram
   content you still need.
3. Check whether a browser extension or organizational browser policy blocks
   embedded app dialogs.
4. If the problem continues, record the macro name, browser, visible error, and
   whether other app macros open on the same page.

Do not delete and reinsert an existing macro merely to clear an editor error;
that can remove the only editable copy attached to the page.

## The editor closed but the published page did not change

The Connect workflow has three save boundaries:

1. **Save and Close** (or the equivalent action in the embedded editor) returns
   the changed diagram to the macro dialog.
2. **Insert** for a new macro, or **Save** for an existing macro, applies it to
   the Confluence page draft.
3. **Publish** or **Update** makes the page draft visible to readers.

Complete all three steps and then reload the published page. If the preview in
the macro dialog never changed, keep the original macro and contact support.

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
  [Connect usage guide](../usage/) to separate a syntax problem from an app or
  browser problem.
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
