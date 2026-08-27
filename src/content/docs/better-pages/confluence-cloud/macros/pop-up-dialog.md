---
title: "Pop-up Dialog"
description: "Open focused rich Confluence content in an accessible modal dialog."
---

Use **Better Pages Pop-up Dialog** for supporting content that should stay out of
the initial reading flow but needs more space than a tooltip.

## Add a dialog

1. Insert **Better Pages Pop-up Dialog**.
2. Enter the dialog title and trigger text.
3. Choose small, medium, large, or extra-large width.
4. Set trigger and content alignment.
5. Optionally add up to 12 labelled destination choices.
6. Save, add rich content to the macro body, and publish.

## Reader interaction

The trigger opens a modal hosted by Confluence. Readers can close it with the
Close action, Escape, or the overlay. Focus is contained while the dialog is
open and returns to the trigger afterward.

Each optional choice accepts a Confluence page or supported safe destination
and may open in a new tab.

## Example

Use `Review launch criteria` as the trigger. Put the checklist in the body and
add choices for `Open readiness page` and `Contact release owner`.

## Good practice

- Use a dialog for a focused task, not a replacement for a long child page.
- Make the trigger and title describe the content clearly.
- Keep the primary reading path available without opening the dialog.
- Test touch, keyboard, Escape, overlay close, and focus return after publishing.
