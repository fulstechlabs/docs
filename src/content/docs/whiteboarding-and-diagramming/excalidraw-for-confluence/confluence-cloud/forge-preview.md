---
title: "Forge preview"
description: "Using the Forge preview of Excalidraw, Mermaid, PlantUML and the other diagram macros for Confluence."
---

:::caution[Preview availability]
This guide describes the Forge version currently being validated on test sites. It is not a production rollout announcement. If your editor has an **Open Editor** button followed by a separate macro dialog, use the [current Connect usage guide](../usage/) instead. Do not uninstall the existing app to try this preview.
:::

## Choose a diagram

All seven macros belong to the same Confluence app. Choose the tool that fits the information you want to explain.

| Macro | Best for | How you edit |
| --- | --- | --- |
| Excalidraw Diagram | Sketches, wireframes and informal whiteboards | Draw shapes and edit text on a canvas |
| Mermaid UML Diagram | Diagrams maintained alongside a text description | Edit Mermaid source and review the preview |
| Graphviz Diagram | Relationships, dependencies and directed graphs | Edit DOT source and review the preview |
| PlantUML Diagram | UML and other text-defined diagrams | Edit PlantUML source and review the preview |
| Mind Map | Brainstorming and topic hierarchies | Edit topics and add child branches |
| BPMN Diagram | Business process diagrams | Connect process elements on a canvas |
| DrawIO Diagram (Powered by draw.io) | Structured diagrams using shape libraries | Use the embedded draw.io editor |

On development installations, Confluence may append **(Development)** to a macro's name.

## Open and save a diagram

1. Edit the Confluence page. Insert a diagram macro, or select an existing macro and choose **Edit**.
2. Make your changes in the diagram editor. Review the complete diagram before saving.
3. Choose **Save** in the Forge editor. For DrawIO, choose **Save & Exit**; the label follows the editor's language.
4. Wait for the editor to return to Confluence, then choose **Publish** for a new page or **Update** for an existing page.
5. Reopen the published page to review the result.

**Saving the diagram and publishing the page are separate steps.** Closing a Confluence page editor can leave an unpublished draft. Do not assume that closing a dialog discards changes you already saved into that draft.

To leave a diagram editor without applying its current edits, use **Close**, or **Exit** in DrawIO, before choosing Save.

If Save says that Confluence has not confirmed the macro in the page draft yet, keep the diagram editor open. Your current work stays there so you can retry **Save**. Wait for the editor to close successfully before choosing Publish or Update; repeatedly clicking the page's Update button is not a substitute for a confirmed diagram save.

## Canvas tools

### Excalidraw

Use the shape and text tools to build your drawing. Double-click existing text to edit it. **Undo** and **Redo** let you review changes before saving. Use **Zoom in**, **Zoom out**, and **Reset zoom** to navigate the canvas. **Grid mode** displays a drawing grid; it is not additional diagram content.

Turn on **View mode** to inspect the drawing without editing it; turn it off to use the drawing tools again. **Zen mode** reduces surrounding controls so you can focus on the canvas. These controls change how you work in the editor, not the meaning of the diagram.

**Reset Scene** restores the drawing loaded when you opened the editor. It removes your current unsaved drawing changes; it does not restore an older Confluence page version. To leave without applying edits, choose **Close** instead of Save.

Fonts may finish loading shortly after the editor opens. Wait until the intended font is visible before reviewing the drawing. If a font remains incorrect, report it rather than changing your original text to compensate.

If Save reports that a required font has not loaded, keep the editor open and retry after the font loads. The failed save does not apply the current edits to the macro. Avoid closing or reloading the editor while you have unsaved work.

#### Reuse drawings with Personal Library

The editor's **Personal Library help** link opens this section in another tab. Confluence asks you to confirm the navigation; cancelling or opening help leaves the current drawing in the editor.

1. Select the shapes and text you want to reuse on the canvas.
2. Open **Library** and choose the **+** thumbnail to add the selection.
3. Click a saved item's thumbnail to insert it into the current drawing. Move it to the desired position; it may initially overlap existing content. Use **Undo** if you did not want the insertion.
4. Save the diagram and update the Confluence page to publish the inserted content.

Library items are stored separately in this browser's local storage. Adding an item does not publish or change the page, and closing the diagram editor without Save does not undo the library addition. Do not rely on the library as a backup: clearing browser data can remove it, and it is not a shared team library or cross-browser sync service. Automatic transfer of a library from the old Connect editor has not been verified.

To download a library copy, open the three-dot menu beside **Personal Library**, choose **Save to...**, and finish the browser's Save dialog. The download is an `.excalidrawlib` file, separate from the current page's drawing.

To import a library, use **Open** in that same Personal Library menu and select an `.excalidrawlib` file. Do not use the canvas menu's **Open**, which loads a drawing instead. Import adds library items alongside your existing items; it does not replace the page's drawing. Click an imported thumbnail to insert it, then Save and update the page when you want to publish the result. You do not need to reset your library before importing.

Library export/reimport, adding a new library item, reopening the editor and inserting the imported item have been checked in Chrome on a test site. This does not establish automatic migration of a Connect browser library. Keep your original export as a backup.

If the editor warns that library changes could not be saved in this browser, keep it open and use **Personal Library → Save to...** to download a copy. Saving the diagram does not back up the library. The warning clears after a successful library-storage operation; do not reload to dismiss it while your only copy is still in memory.

### Mind Map

Double-click a topic to rename it. Select a topic and press **Tab** to add a child. Use the branch's **−** and **+** controls to collapse and expand its descendants. Reopen a saved map to continue editing its topics, not just its preview image.

Choose **Close** without Save to leave the stored map unchanged. A changed topic is not published merely because it appears on the editing canvas.

### BPMN

Select an element to open its context controls. For example, **Append EndEvent** adds an end event connected to the selected task.

#### Walk through a process

1. Turn on **Token Simulation**. The diagram switches to its simulation appearance; your modeling colors return when you turn simulation off.
2. Choose **Slow**, **Normal**, or **Fast** using the speed controls at the bottom of the canvas. Slow is useful when explaining the path through a diagram.
3. Trigger the start event. Open **Simulation Log** to follow the process events.
4. While a token is moving, use **Play/Pause Simulation** to pause it. Press the control again to resume. You can select another speed before resuming.
5. For a connected Start → Task → End example, the token reaches the end and displays **Finished**. Use **Reset Simulation** to clear the run and try again; this is different from the editor's **Reset** button.

Simulation is an editing aid, not a workflow engine: it does not execute business actions in Confluence. A successful simulation is not a certification that a complex business process is valid.

#### Save after simulation

Turn simulation off to review the normal diagram appearance. In the current Forge preview, **Save** also turns simulation off automatically before creating the saved preview, so temporary simulation colors are not saved as your diagram's colors. Then select **Update** or **Publish** on the Confluence page to make the changes visible to readers.

If Save reports that Confluence has not confirmed the macro in the draft, keep the editor open and follow [Open and save a diagram](#open-and-save-a-diagram). Do not assume that an error means the page is ready to publish.

To change a task's color, select it, choose **Set Color**, then a swatch. Save the diagram and Update the page to publish the color. To add a standalone task, choose **Create Task** from the left palette and place it on the canvas; adding a task does not automatically connect it to the process. **Reset** restores the model loaded at editor open, discarding current unsaved edits such as label, color or added-task changes.

### DrawIO

The Forge preview uses draw.io's standard editor layout, with shape libraries on the left and formatting on the right. **Save & Exit** and **Exit** are in the top toolbar. Your browser language can change these labels. Saving requires both reusable diagram XML and a preview image; a save error is not confirmation that the page has been updated.

To leave without saving, choose **Exit**. If you changed the diagram, draw.io asks whether to discard those changes. Confirm discarding only when you no longer need the unsaved edits. This is different from **Save & Exit**, which applies the diagram changes to the page draft.

## Text-defined diagrams

Mermaid, Graphviz and PlantUML use different languages. Select the matching macro and keep the source in that language. Review the preview after each change, then save and update the page.

For a small Mermaid flowchart, try:

```text
flowchart LR
  Request --> Review
  Review --> Approved
```

The published diagram is a visual representation. A diagram arrow is not automatically a Confluence navigation link or an executable action.

### Share editable Mermaid source

Expand **Share Mermaid source** in the Mermaid editor:

- **Copy Markdown** copies a fenced `mermaid` code block.
- **Download Markdown** saves the same kind of block in a Markdown file.
- **Download source (.mmd)** saves the exact source, including its configuration and current unsaved edits.

These actions do not save the macro or update the Confluence page. A receiving tool must support Mermaid to display the Markdown as a diagram; otherwise it shows code. This is not an externally hosted image link, a Confluence page share, or a GitHub Gist integration. Use PNG or SVG when the recipient needs an image. If clipboard access fails, use a download instead. You can back up invalid source before fixing its syntax, but finish or cancel any pending configuration/sample decision first.

### Inspect Mermaid in Full view

Choose **Full view** once the preview matches the current source. It opens a larger read-only view inside Confluence. Use zoom and pan to inspect details; **Back to editor** or Escape returns to the same source editor without saving anything. The view displays the rendered snapshot from the moment you opened it, not a separately editable diagram.

Full view is not a standalone browser page or a shareable URL. Its size is controlled by Confluence and your browser window. For edits, return to the editor, change the source, and wait for a fresh preview before opening Full view again.

### Control the Mermaid preview

**Auto preview** is on when you open the editor. After you pause typing, the preview refreshes. **Save** remains disabled until the preview matches the current source, so a previous diagram image is not saved with newly edited source.

For longer editing sessions, turn **Auto preview** off:

1. Edit the source. The previous preview stays visible while you type.
2. Choose **Preview now**, or press **Cmd+Enter** on macOS / **Ctrl+Enter** on Windows or Linux while the source editor has focus.
3. Review the refreshed diagram, then choose **Save** and update the Confluence page.

If the source changes again, refresh the preview again before saving. Turn **Auto preview** back on to resume automatic updates. This preference applies to the current editor session; it is not saved as a page setting.

### Customize a Mermaid diagram

Use **Configuration** to change Mermaid settings without having to write YAML yourself. For example, you can change a theme or whether sequence diagrams repeat their actor boxes at the bottom.

1. Choose **Configuration**. The JSON editor shows the settings already in your source, or `{}` if none are present.
2. Enter a JSON object. For a sequence diagram, try:

   ```json
   {
     "theme": "forest",
     "sequence": {
       "mirrorActors": false
     }
   }
   ```

3. Choose **Apply configuration**. The editor adds or updates `config` in the source's YAML frontmatter. Diagram code stays below that block. Applying settings can reformat the frontmatter, but does not save the macro or publish the page.
4. Review the preview. If Auto preview is off, choose **Preview now**. Then Save and Update the page as usual.

Choose **Cancel configuration** to leave the source unchanged. Invalid JSON is not applied. If you edit Source while Configuration is open, cancel and reopen Configuration before applying settings to the latest source. Enter `{}` to clear the frontmatter's configuration overrides.

Settings travel with the source: Local history restores them together, and image exports use the matching configured preview. There is no separate settings copy to synchronize. Mermaid controls which options may be overridden; platform-controlled options cannot be changed here. Advanced YAML configuration with anchors remains editable directly in Source if the JSON panel cannot safely edit it.

### Download or copy a Mermaid image

Choose **Download SVG** for a vector image, **Download PNG** for a raster image, or **Copy image** to put a PNG on your clipboard. These actions wait for a preview matching the current source and configuration. They do not save the macro or publish the page.

For a PNG, expand **PNG options** and optionally enter **PNG width (pixels)**. Leave it blank to use the diagram's original size. The exporter preserves the aspect ratio and uses a white background. Preview zoom does not change export size. If the requested image exceeds 8192 pixels on either side or 16 megapixels, choose a smaller width or download SVG. Linked external images are rejected by PNG export instead of being silently omitted.

If Chrome opens a **Save** dialog, choose a destination and finish saving there. “PNG prepared” means the file is ready for the browser to save, not that the download is already on disk. For Copy image, paste into an application that accepts images; for example, use **Edit → Paste** in a Confluence page editor. If clipboard access is unavailable or denied, use Download PNG instead.

PNG/SVG downloads and pasting a copied image into Confluence have been checked in Chrome on a test site. This is not a source backup: keep the editable Mermaid source if you need to change the diagram later.

:::caution[Other exports still under validation]
Confluence PDF/Word exports remain under validation. Downloading a library or image does not prove those separate flows are ready for production migration.
:::

### Start with a sample or find syntax help

Choose a **Sample diagram**, then **Load sample**. The available starting points include flowcharts, sequence, class, state and entity relationship diagrams, Gantt, user journey, Git graph, pie, mindmap and quadrant chart. If you already have source, the editor asks before replacing it. Choose **Keep current source** to cancel. Loading a sample changes the editor only; review it before Save and Update.

**Syntax help** opens the official Mermaid documentation for the diagram type detected from your source. Confluence asks you to confirm opening the external documentation page. **Cancel** leaves the source unchanged. The help URL does not include your diagram source. Documentation may describe newer syntax than the app's bundled renderer; check the preview before saving.

### Make room for a larger diagram

Drag the divider between Source and Preview to change their widths. You can also focus the divider and use the arrow keys; **Home** and **End** move to its limits. Double-click it to return to an even split.

Use **−** and **+** above the Mermaid preview to zoom between 25% and 400%; the percentage button resets to 100%. Enable **Pan preview** to drag around an enlarged diagram. For long Gantt charts, zoom in until labels are readable and scroll or pan to review the full chart. These controls affect your editor view, not the source or published diagram size. Collapse Local history when you need more vertical space.

### Recover source with Local history

Local history gives you snapshots you can return to while editing a Mermaid diagram. It is separate from the page's Confluence version history.

1. Open **Local history**, optionally enter a **Snapshot name**, then choose **Save snapshot**.
2. Continue editing. To inspect an older snapshot without changing anything, expand its **View source**.
3. Choose **Restore** on the snapshot you want. Review the confirmation, then choose **Confirm history action**, or cancel to keep editing.
4. The replaced source is kept in a **Before restore** snapshot. Review the restored preview, then choose **Save** and **Update** if you want to publish it.

**Auto history** is optional and off when you open an editor. While enabled in that session, it checks once a minute and keeps up to 30 automatic snapshots, skipping unchanged source. Manual snapshots are not removed by that automatic limit. This is not continuous autosave: source typed after the last snapshot can still be lost if you close the editor or browser.

**Export history** downloads a JSON copy of local source snapshots. **Import history** accepts this Forge app's version-1 source-history export or a JSON history export from the Connect Mermaid editor. It adds snapshots without replacing the current editor source; existing snapshot IDs are skipped. It does not import Confluence page versions or arbitrary Mermaid configuration files. **Delete** and **Clear local history** require confirmation and remove only local snapshots, not the diagram on the page.

:::caution[Local history is not a shared backup]
Snapshots stay in this browser, separated by site, signed-in account, page and macro. They are not synchronized to teammates or other browsers. Browser cleanup, storage limits, restricted browser storage or an app update can make them unavailable. Do not store your only copy of important source here. Forge history import/export and reload have been checked through the tenant editor in Chrome; this does not establish automatic transfer from Connect.
:::

If a history write fails, the editor reports it instead of pretending the snapshot was saved. A restore that cannot preserve the current source stops without replacing it. If history is unavailable because the editor lacks a complete account/site/page/macro identity, you can still use the normal diagram editor; do not remove or recreate the macro to work around the history message.

#### Bring a Connect Mermaid history file

History transfer is manual and separate from upgrading the diagram stored on a page. Before upgrading, keep copies of any browser history you want to retain:

1. In the Connect Mermaid editor, open **History**, select **Saved**, **Timeline** or **Revisions**, and download that tab's JSON history. Repeat for each tab you need. Keep the original files.
2. In the Forge Mermaid editor for the destination macro, open **Local history** and choose **Import history**. Select a downloaded JSON file in the browser's file picker.
3. Check the imported snapshot names. Import leaves the current diagram source and existing snapshots unchanged. Imported Timeline and Revisions entries become manual snapshots, so the automatic 30-snapshot limit does not remove them.
4. Choose **Restore** on a snapshot when you want to use it. Confirm only after reviewing the replacement warning; the current source is backed up as **Before restore**. Check the resulting diagram before **Save** and Confluence **Update**.

The imported snapshot combines diagram code and Mermaid configuration in source frontmatter. Source-level settings take precedence over the old editor's base configuration; frontmatter formatting may change. The original entry is also retained in subsequent **Export history** downloads. Old editor layout, pan/zoom, auto-sync settings and external loader links are not activated. Import does not fetch a GitHub Gist or its revisions.

If a file contains an invalid entry or configuration, the complete import is rejected rather than silently skipping entries. Keep the original file and contact support; do not clear existing history to retry. Reimporting an already imported snapshot ID does not update or duplicate that snapshot.

:::note[Preview validation boundary]
The Connect-format import, restore confirmation, configured preview, export preservation and reload have been checked in Chrome using a test file matching the Connect export format. A file downloaded from an actual Connect editor has not yet completed this validation. This is not an assurance of complete Connect history migration.
:::

## Existing Connect diagrams

The intended upgrade replaces the existing app on the same site and Marketplace listing. Users should not recreate all their pages or remove the existing app.

When supported Connect data is opened in the Forge editor, a legacy-data notice explains that migration has not yet been saved. Review the loaded content before choosing **Save**, then update the page. Opening or viewing a page is not an instruction to overwrite its stored diagram.

If the editor reports that legacy data is unreadable or read-only, leave the original macro in place and contact support. Do not reset the scene, delete the macro, or paste unrelated content over it to clear the message. Keep the page URL and version available for investigation.

:::note[Validation still in progress]
Core same-site upgrade, rendering and edit/save/reopen flows have been checked on controlled Connect-created examples for Excalidraw, Mermaid, Graphviz, PlantUML, Mind Map and BPMN. This does not cover every historical diagram. The current DrawIO Connect-before-upgrade flow remains unverified because the Connect editor did not provide usable creation controls in the test environment. PDF/Word output and additional feature cases are also still being validated. Do not treat this preview as an assurance of production migration readiness.
:::

## Data processing

The Forge version uses Atlassian-hosted app resources and Forge storage, but it is **not currently eligible for Runs on Atlassian**. Some features still use external services:

| Feature | External processing |
| --- | --- |
| Graphviz | Diagram source is encoded into a request to **kroki.io** for rendering |
| PlantUML | Diagram source is encoded into a request to **www.plantuml.com** for rendering |
| DrawIO | Diagram XML is passed to an editor loaded from **embed.diagrams.net** |
| Fonts | The app permits font resources from **esm.sh** |

Encoding a diagram in a URL does not encrypt it. Storing a copy in Forge does not mean that no external service processes the content. Check your organization's data-handling requirements before using externally processed diagram types. This guide does not make a claim about those services' retention policies or regulatory certification.

## Get help

Contact [Fulstech support](https://fulstech.atlassian.net/servicedesk/customer/portals) with the macro type, app version, browser, page version and the steps that failed. Include a screenshot if appropriate. Remove confidential source text and credentials from reports unless your organization has approved sharing them through the support channel.

If a download is blocked by your browser, report the browser error separately from the export result. A completed export job alone does not prove that the file contains the expected diagrams.
