---
title: "Upgrade existing diagrams from Connect"
description: "Review and preserve existing diagrams when moving from the Connect editor to the Forge app."
---

The Forge upgrade replaces the existing Cloud app on the same Confluence site
and Marketplace listing. Keep existing macros in place. Do not uninstall the
app, delete macros, or recreate pages as an upgrade step.

This guide applies to the published Forge app, Cloud version **3.0.0**. If your
site still shows a separate **Open Editor** step, use the
[legacy Connect guide](../usage/) until the Forge upgrade is available.

## Know what you are preserving

The diagram on a Confluence page, reusable library items, and source-history
snapshots are separate. Successfully opening one does not prove that the others
have transferred.

| Your content | What to do |
| --- | --- |
| A diagram saved on a Confluence page | Keep its existing macro. Review it in Forge before the first Save, then publish and reopen it using the checklist below. |
| Excalidraw Personal Library | Export an `.excalidrawlib` backup from the old editor while it is available. Follow [Reuse shapes with Personal Library](../canvas-diagrams/#reuse-shapes-with-personal-library). |
| Mermaid history in the Connect editor | Download the history files you need before upgrading. Follow [Bring a Connect Mermaid history file](../mermaid-editor-tools/#bring-a-connect-mermaid-history-file). |
| Current unsaved edits | Finish the intended save or keep an editable export before leaving the editor. A screenshot preserves appearance, not editable diagram data. |

Keep the original library and history exports after importing them. Do not
clear browser data or reset a library as a migration step.

## Check the first edited diagram

Start with a page whose expected diagram you know before editing a larger set of
pages.

1. Record the page URL and published version. Review the existing diagram's
   text, connections, colors, and embedded images.
2. Open the existing macro in Forge. Check that its editable content matches the
   published page.
3. If content is missing, unexpected, or read-only, choose **Close** without
   Save and keep the original macro in place.
4. When the content is correct, make a small identifiable edit.
5. Choose **Save** once and wait for the editor to return to Confluence.
6. Choose **Update** or **Publish**, then reload the published page.
7. Check the complete diagram, not only the changed item. Reopen the macro and
   confirm that the edit remains editable.

If you test a copied page or duplicated macro, change only the copy and check
the original separately. A copy that looks correct before editing does not prove
that both diagrams remain independent after saving.

## Respond to a legacy-data message

When supported Connect data opens in the Forge editor, a legacy-data notice can
explain that migration has not yet been saved. Review the loaded content before
choosing **Save**, then update the Confluence page.

Opening or viewing a page does not overwrite its stored diagram. If the editor
reports unreadable or read-only legacy data, choose **Close**, leave the original
macro in place, and contact support. Do not reset the scene or delete and reinsert
the macro to clear the message.

A missing preview is not proof of an empty diagram. For an unreadable Mind Map,
**Save** remains disabled even when no preview image is available. Keep the
original page for investigation.

Confluence can create an unpublished draft when you open an older macro's
configuration. That does not mean the published diagram has been migrated.
Review the page draft separately.

:::note[Verified upgrade coverage]
Same-site render, edit, save, and reopen flows were checked on controlled
Connect-created examples for Excalidraw, Mermaid, Graphviz, PlantUML, Mind Map,
and BPMN. Historical diagrams can vary. DrawIO compatibility is implemented and
regression-tested, but a genuine Connect-authored editable DrawIO baseline was
not available in the test environment.
:::

## If a check fails

Keep the original macro, page URL and version, and any exported editable source.
Do not repeatedly save missing content or replace the macro. Contact
[Fulstech support](../support/) with the macro type, app version, browser,
expected result, actual result, and the failed checklist step.

## Next steps

- [Create and edit canvas diagrams](../canvas-diagrams/).
- [Create diagrams from text](../text-diagrams/).
- [Use Mermaid editor tools](../mermaid-editor-tools/).
