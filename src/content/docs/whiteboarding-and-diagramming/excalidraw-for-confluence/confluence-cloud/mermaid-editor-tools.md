---
title: "Use Mermaid editor tools"
description: "Preview, configure, export, share, and recover Mermaid source in Confluence Cloud."
---

Use these tools after you can create and publish a basic Mermaid diagram. This
guide applies to the published Forge app, Cloud version **3.0.0**. Start with
[Create diagrams from text](../text-diagrams/) if you have not yet published a
Mermaid diagram.

## Keep the preview in sync with source

**Auto preview** is on when you open the editor. After you pause typing, the
preview refreshes. **Save** remains disabled until the preview matches the
current source.

For a longer editing session:

1. Turn off **Auto preview**.
2. Edit the source. The previous preview stays visible while you type.
3. Choose **Preview now**, or press **Cmd+Enter** on macOS or **Ctrl+Enter** on
   Windows or Linux while the source editor has focus.
4. Review the refreshed diagram, then choose **Save** and update the Confluence
   page.

If the source changes again, refresh the preview again before saving. The Auto
preview preference applies only to the current editor session.

## Configure a Mermaid diagram

Use **Configuration** to change Mermaid settings without writing YAML directly.
For example, you can change the theme and sequence-diagram actor layout.

1. Choose **Configuration**. The JSON editor shows the settings already in the
   source, or `{}` when none are present.
2. Enter a JSON object. For a sequence diagram, try:

   ```json
   {
     "theme": "forest",
     "sequence": {
       "mirrorActors": false
     }
   }
   ```

3. Choose **Apply configuration**. The editor adds or updates `config` in the
   source's YAML frontmatter.
4. Review the preview. If Auto preview is off, choose **Preview now**.
5. Save the diagram and update the Confluence page.

Choose **Cancel configuration** to leave the source unchanged. Invalid JSON is
not applied. Enter `{}` to clear configuration overrides. Settings travel with
the source and are restored with Local history snapshots.

## Inspect a larger preview

Choose **Full view** after the preview matches the current source. Use zoom and
pan to inspect details. Choose **Back to editor**, or press Escape, to return to
the same source editor without saving.

Full view is read-only. It is not a standalone browser page or a shareable URL.

Drag the divider between Source and Preview to change their widths. You can
also focus the divider and use the arrow keys; **Home** and **End** move it to
its limits. Double-click the divider to return to an even split.

Use **−** and **+** above the preview to zoom between 25% and 400%. Select the
percentage to reset to 100%. Enable **Pan preview** to drag around an enlarged
diagram.

## Share editable Mermaid source

Expand **Share Mermaid source**:

- **Copy Markdown** copies a fenced `mermaid` code block.
- **Download Markdown** downloads the same kind of block in a Markdown file.
- **Download source (.mmd)** downloads the exact source, including its current
  configuration and unsaved edits.

These actions do not save the macro or update the Confluence page. The receiving
tool must support Mermaid to render the Markdown as a diagram. Use PNG or SVG
when the recipient needs an image instead of editable source.

## Download or copy an image

- Choose **Download SVG** for a vector image.
- Choose **Download PNG** for a raster image.
- Choose **Copy image** to place a PNG on the clipboard.

These actions wait for a preview that matches the current source and
configuration. They do not save the macro or publish the page.

For PNG, expand **PNG options** and optionally enter **PNG width (pixels)**.
Leave it blank to use the diagram's original size. The exporter preserves the
aspect ratio and uses a white background. Preview zoom does not change export
size.

If a requested image exceeds 8192 pixels on either side or 16 megapixels,
choose a smaller width or download SVG. If clipboard access is unavailable,
use Download PNG instead.

:::note[Confluence PDF and Word]
Confluence PDF and Word exports use the diagram snapshot saved with the macro.
Save the diagram and publish the page before exporting. Browser image downloads
do not update the Confluence page.
:::

## Start with a sample or open syntax help

Choose a **Sample diagram**, then **Load sample**. If the editor already contains
source, it asks before replacing it. Choose **Keep current source** to cancel.
Loading a sample changes the editor only; review it before Save and Update.

**Syntax help** opens the official Mermaid documentation for the diagram type
detected from the source. External documentation may describe newer syntax than
the app's bundled renderer, so check the preview before saving.

## Recover source with Local history

1. Open **Local history**.
2. Optionally enter a **Snapshot name**, then choose **Save snapshot**.
3. Continue editing. Expand **View source** to inspect an older snapshot without
   changing the current source.
4. Choose **Restore** on the snapshot you want, review the confirmation, then
   choose **Confirm history action**.
5. Review the restored preview, then choose **Save** and **Update** when you want
   to publish it.

The editor keeps the replaced source in a **Before restore** snapshot.
**Auto history** is optional and applies to the current editor session. While
enabled, it checks once a minute and keeps up to 30 changed automatic snapshots.
Manual snapshots are not removed by that automatic limit.

**Export history** downloads a JSON copy of local snapshots. **Import history**
adds snapshots from this Forge app's version-1 export or a JSON history export
from the Connect Mermaid editor. It does not replace the current source.
Existing snapshot IDs are skipped.

:::caution[Local history is not a shared backup]
Snapshots stay in this browser and are not synchronized to teammates or other
browsers. Browser cleanup, storage limits, or restricted browser storage can
make them unavailable. Keep an exported copy of important source.
:::

### Bring a Connect Mermaid history file

1. In the Connect Mermaid editor, open **History**, select **Saved**,
   **Timeline**, or **Revisions**, and download the JSON history you need.
2. In the Forge Mermaid editor, open **Local history** and choose
   **Import history**.
3. Select the downloaded JSON file and check the imported snapshot names.
4. Choose **Restore** on a snapshot, confirm the replacement, then review the
   resulting diagram before **Save** and Confluence **Update**.

Import leaves the current source and existing snapshots unchanged. Keep the
original files. If an entry is invalid, the complete import is rejected rather
than silently skipping it.

## Next steps

- [Upgrade existing diagrams from Connect](../upgrade-from-connect/).
- [Resolve a diagram that does not render](../troubleshooting/#a-mermaid-graphviz-or-plantuml-diagram-does-not-render).
- [Contact support](../support/).
