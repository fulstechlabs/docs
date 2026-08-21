---
title: "Core Macros"
description: "Configure and use Better Pages messages, buttons, progress, tooltips, math, tabs, and clickable content."
---

## Message

Use **Better Pages message** to emphasize information inside the page.

- Choose an inline message or a page alert presentation.
- Choose info, success, warning, error, or neutral appearance where available.
- Inline messages may be dismissible. Page alerts always include a dismiss control.
- Dismissal lasts only until the reader reloads the page; it is not stored.

A page alert is contained inside its Forge macro area. It cannot cover Confluence navigation or other page content. PDF and Word export retain a static panel with the title and message.

## Button

Use **Better Pages button** for one prominent navigation action.

- Enter a label and a [safe destination](../getting-started/#safe-destinations).
- Choose Primary, Standard, or Subtle appearance.
- Optionally add a preset icon or up to four Unicode characters.
- Choose whether the destination opens in a new tab.

An invalid destination produces a disabled button and correction message. Static export keeps the label and icon and creates a link only when the destination is valid.

## Progress

Use **Better Pages progress** for an ordered process, delivery journey, or status sequence. Enter one step per line. Add an optional destination after `|`:

```text
Plan|/wiki/home
Build
Review|https://example.com/review
Notify|mailto:owner@example.com
```

Set the current step to divide the list into completed, current, and upcoming states. Better Pages supports up to 100 steps. If there are no steps, the reader and static export explicitly show that no progress steps are configured.

## Tooltip

Use **Better Pages tooltip** for short supporting text that belongs to one visible trigger.

- Choose top, right, bottom, or left placement.
- Readers can reveal the text with pointer hover, keyboard focus, or click/touch.
- Keep the trigger and its supporting text in the same macro.

Forge isolates each macro surface, so a tooltip cannot target an unrelated element elsewhere on the Confluence page. Empty supporting text produces an explicit configuration message instead of a blank popup.

## Math

Use **Better Pages math** to render a KaTeX equation. Enter the formula without Markdown code fences and choose inline or block display.

```latex
E = mc^2
```

Rendering uses local, non-trusting KaTeX settings. Static export uses accessible equation text rather than promising an identical image render.

## Tabs

Use **Better Pages tabs** to turn one rich Confluence body into navigable sections.

1. Insert the macro and edit its rich-text body.
2. Add level-two or level-three headings.
3. Each heading begins a tab and owns the content until the next heading.
4. Choose horizontal or vertical layout, visual style, compact mode, initial tab, and optional hover hints.

Readers can use Home, End, and orientation-aware arrow keys. On narrow screens, vertical tabs become a horizontally scrollable tab list and use Left/Right navigation. Static export linearizes every section so hidden tabs are not lost.

Supported Confluence content and Forge macros can remain inside a tab section. Third-party Connect macros and nested bodied macros are subject to Confluence platform limitations.

## Clickable content

Use **Better Pages clickable content** when a rich Confluence body should be paired with one destination.

- Edit the body using normal Confluence formatting, panels, tables, and links.
- Configure one safe wrapper destination.
- Safe links already present in the body are exposed as separate actions under **Links in content**.
- **Open destination** activates the wrapper destination.

The app intentionally does not place an invisible click overlay across the rich body because that would block the body's own links. If the wrapper destination is invalid, body content and its safe links remain available while only the wrapper action is disabled. Static export preserves the body and appends a valid destination as a normal link.
