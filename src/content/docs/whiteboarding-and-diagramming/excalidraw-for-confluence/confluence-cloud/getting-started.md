---
title: "Create your first Excalidraw drawing"
description: "Add, save, and publish an Excalidraw drawing on a Confluence Cloud page."
---

This guide creates a small drawing that readers can see on a Confluence Cloud
page. It applies to the published Forge app, Cloud version **3.0.0**.

## Before you start

- The app must be installed with an active Marketplace license or trial.
- You need permission to edit and publish the target Confluence page.

## Add the drawing

1. Open a Confluence page and select **Edit**.
2. Type `/Excalidraw`, then choose **Excalidraw Diagram**. The diagram editor
   opens directly; there is no separate **Open Editor** step in Forge.
3. Draw two rectangles and label them **Browser** and **Service**. Connect them
   with an arrow to show the direction of a request.
4. Select **Save** and wait for the editor to return to Confluence.
5. Select **Publish** for a new page, or **Update** for an existing page.

You have succeeded when the published page shows the drawing instead of the
macro editor or an empty placeholder.

## Edit the drawing later

1. Edit the Confluence page.
2. Select the drawing and choose **Edit**.
3. Change the **Service** label to **API service**, then select **Save**.
4. Wait for the editor to return to Confluence, then select **Update**.
5. Reload the published page and confirm the label changed while both rectangles
   and their connecting arrow are still present.

Saving the drawing and publishing the page are separate steps. Readers continue
to see the published page until you select **Publish** or **Update**.

## Next steps

- [Choose the right diagram macro](../choose-a-diagram/).
- [Reuse shapes with Personal Library](../forge-preview/#reuse-drawings-with-personal-library).
- [Use the other diagram editors](../forge-preview/).
- [Troubleshoot a diagram](../troubleshooting/).

If your site still shows **Open Editor** and **Save and Close**, use the
[legacy Connect guide](../usage/). If saving reports that the macro has not yet
been confirmed in the page draft, keep the editor open and retry **Save** after
the draft is ready. Do not publish until the diagram editor closes successfully.
