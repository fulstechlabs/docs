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

## Canvas tools

### Excalidraw

Use the shape and text tools to build your drawing. Double-click existing text to edit it. **Undo** and **Redo** let you review changes before saving. Use **Zoom in**, **Zoom out**, and **Reset zoom** to navigate the canvas. **Grid mode** displays a drawing grid; it is not additional diagram content.

Fonts may finish loading shortly after the editor opens. Wait until the intended font is visible before reviewing the drawing. If a font remains incorrect, report it rather than changing your original text to compensate.

If Save reports that a required font has not loaded, keep the editor open and retry after the font loads. The failed save does not apply the current edits to the macro. Avoid closing or reloading the editor while you have unsaved work.

#### Reuse drawings with Personal Library

1. Select the shapes and text you want to reuse on the canvas.
2. Open **Library** and choose the **+** thumbnail to add the selection.
3. Click a saved item's thumbnail to insert it into the current drawing. Move it to the desired position; it may initially overlap existing content. Use **Undo** if you did not want the insertion.
4. Save the diagram and update the Confluence page to publish the inserted content.

Library items are stored separately in this browser's local storage. Adding an item does not publish or change the page, and closing the diagram editor without Save does not undo the library addition. Do not rely on the library as a backup: clearing browser data can remove it, and it is not a shared team library or cross-browser sync service. Automatic transfer of a library from the old Connect editor has not been verified.

### Mind Map

Double-click a topic to rename it. Select a topic and press **Tab** to add a child. Use the branch's **−** and **+** controls to collapse and expand its descendants. Reopen a saved map to continue editing its topics, not just its preview image.

### BPMN

Select an element to open its context controls. For example, **Append EndEvent** adds an end event connected to the selected task. **Token Simulation** lets you explore a process; trigger a start event and open the simulation log to follow execution. Simulation is an editing aid, not a workflow engine that executes business actions in Confluence. Turn simulation off before reviewing and saving the diagram.

### DrawIO

The Forge preview uses draw.io's standard editor layout, with shape libraries on the left and formatting on the right. **Save & Exit** and **Exit** are in the top toolbar. Your browser language can change these labels. Saving requires both reusable diagram XML and a preview image; a save error is not confirmation that the page has been updated.

## Text-defined diagrams

Mermaid, Graphviz and PlantUML use different languages. Select the matching macro and keep the source in that language. Review the preview after each change, then save and update the page.

For a small Mermaid flowchart, try:

```text
flowchart LR
  Request --> Review
  Review --> Approved
```

The published diagram is a visual representation. A diagram arrow is not automatically a Confluence navigation link or an executable action.

### Control the Mermaid preview

**Auto preview** is on when you open the editor. After you pause typing, the preview refreshes. **Save** remains disabled until the preview matches the current source, so a previous diagram image is not saved with newly edited source.

For longer editing sessions, turn **Auto preview** off:

1. Edit the source. The previous preview stays visible while you type.
2. Choose **Preview now**, or press **Cmd+Enter** on macOS / **Ctrl+Enter** on Windows or Linux while the source editor has focus.
3. Review the refreshed diagram, then choose **Save** and update the Confluence page.

If the source changes again, refresh the preview again before saving. Turn **Auto preview** back on to resume automatic updates. This preference applies to the current editor session; it is not saved as a page setting.

### Download a Mermaid SVG

The preview editor includes **Download SVG** for the current Mermaid diagram. Like Save, this action waits for a preview matching the current source. It does not save the macro or publish the page.

:::caution[Download validation]
SVG file generation has passed local browser tests, but successful file delivery from the Forge editor on a Confluence test site is still being verified. Personal Library file export/import and Confluence PDF/Word exports also remain under validation. Do not rely on these flows for backups or production migration yet.
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
