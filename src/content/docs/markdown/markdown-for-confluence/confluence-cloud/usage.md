---
title: "Write and edit Markdown"
description: "Create a Markdown macro, preview tables and formulas, save it to Confluence and reopen the source."
---

Create an engineering note with a table and two formulas, then save and reopen
its Markdown source. These steps apply to the **Forge editor**.

## Before you begin

The app needs an active license, and you need permission to edit the page.
For a new page, you also need permission to create and publish it in the space.
Use the [Connect guide](../connect-editor/) if you see the older check-icon editor.

## 1. Insert the macro

1. Create a Confluence page or edit an existing page.
2. Place the cursor where the macro belongs. Type `/` to open the insertion
   menu, then choose **View more** to open **Browse**.
3. Search **Markdown**, select the Markdown macro and select **Insert**.
   On a development installation its name includes **(Development)**; select
   the installation your administrator intends you to use.

The macro opens its Markdown editor. For an existing macro, edit the Confluence
page, select the macro and choose **Edit** from its floating toolbar.

## 2. Write and preview

Paste this example into **Markdown source**:

```markdown
## Engineering notes

Keep the **source** and the formatted result together.

| Quantity | Value |
| --- | --- |
| Mass | 2 kg |
| Acceleration | 3 m/s² |

The force is $F = ma$.

$$
F = 2 \times 3 = 6\,\mathrm{N}
$$
```

[![The engineering-note source and its live preview, including a table and two formulas](/assets/markdown/release-2/editor-preview.png)](/assets/markdown/release-2/editor-preview.png)

*The same example on a Forge development installation. **Up to date** confirms
that the preview has finished; this is still an unsaved macro configuration.
Select the image to open it at full size.*

Use the formatting toolbar for headings, emphasis, lists, quotes, code, tables,
links and images. Select text before applying a format. **Markdown help**
explains syntax; **Keyboard shortcuts** lists the editor's shortcuts.

| Control | Use it to… |
| --- | --- |
| **Side preview** | Show source and formatted output together, or return to source alone |
| **Reader mode** | Review formatted output without the source pane |
| **Focus mode** | Dim source lines outside the current editing line |
| **Scroll sync** | Move the source and preview proportionally together |
| Pane divider | Drag to resize the panes; use arrow keys when the divider has focus |

Use `$...$` for inline mathematics and separate `$$` lines for a displayed
formula. [Compatibility and exports](../compatibility-and-exports/) explains
images, sanitization and output differences.

## 3. Save the macro and publish the page

1. Select **Save and close**. This saves the macro configuration to the Confluence
   draft and closes the macro editor.
2. In Confluence, **Publish** a new page or **Update** an existing page to share
   the change. A new page may show **Publish…** followed by a confirmation.
3. Reload the published page. Check the table, the inline `F = ma`, and the
   displayed `F = 2 × 3 = 6 N`.

![The saved engineering-note macro with Download Markdown, a table and two rendered formulas](/assets/markdown/release-2/published-example.png)

*The same synthetic example after publishing and reloading on the development
site. This is the page result, rather than the editor preview.*

Edit the page and reopen the macro to check that its Markdown source remains
available. Each macro has its own source; edit the intended macro when a page
contains several.

**Keyboard save:** ⌘/Ctrl+Enter and Escape save and close the editor. Escape is
not a discard action while editing source; within a helper dialog it closes
that dialog first.

## Recover unfinished editing

**Draft saved in this browser** means the app has kept a local recovery draft.
If you leave the outer macro editor without saving, reopening that same macro
in the same browser profile and account can show **Recovered your unsaved draft**.
Review it before saving. A successful macro save clears that macro's current
local draft; it does not publish the Confluence page.

Recovery is unavailable when required identity information or browser storage
is unavailable. It is not a cross-device backup and has no fixed expiry.
See [Privacy and data handling](../privacy-policy/) before relying on browser
storage for sensitive content.

## Next steps

- [Download source and check export compatibility](../compatibility-and-exports/).
- [Validate existing content after a Connect update](../migration/).
- [Resolve preview, license or save problems](../support/).
