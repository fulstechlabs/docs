---
title: "Extended Formatting"
description: "Use Better Pages callouts, navigation, search, tables, references, external content, and other formatting components."
---

Insert **Better Pages extended formatting**, then choose one capability from the configuration panel.

## Formatting and labels

| Capability | How it works |
| --- | --- |
| Lozenge/status label | Shows a colored status with optional icon, arrow, width, supporting text, tooltip, and safe destination. Invalid destinations remain static. |
| Trademark/service/copyright mark | Adds a compact visible mark to a configured label. |
| Safe style/highlight/alignment | Applies bounded styling inside the app-owned macro surface. It does not inject arbitrary CSS into Confluence. |
| Privacy policy/mark | Displays an app-owned privacy notice for the macro output. |
| Rounded callout/flag | Shows emphasized text using a configured appearance. |
| Fancy bullets | Renders one configured item per line as a styled unordered list. |
| Preformatted block | Preserves whitespace in a local preformatted text block. |
| Safe paragraph/div/span | Renders bounded text and styling; it does not execute arbitrary HTML, CSS, or JavaScript. |
| Hidden comment | Keeps configured text out of reader and static-export output. |

## Actions and interaction

### Button group and horizontal navigation

Enter one item per line as `label|destination`. Every item is validated separately, so one invalid destination cannot affect its siblings. The accessible group label describes the collection to assistive technology.

### Local dialog

The trigger opens a dialog contained inside the macro frame. Escape closes it and focus returns to the trigger. The dialog cannot cover or control unrelated Confluence UI outside its Forge surface.

### Rollover card

Configure front text, revealed text, and an optional destination. Hover, keyboard focus, or click/touch reveals the second side. A valid destination adds **Open destination**; an unsafe destination produces a correction without navigation.

## Search and structured data

### Confluence search box

Configure initial text and select current space, up to 20 explicit spaces, or all spaces available to the reader. You can limit results by modified date, group them by space or content type, hide the button for Enter-only use, and assign one alphanumeric access key.

Search is limited to pages and blog posts and runs as the current reader. It cannot expose content the reader may not view. Reader-entered queries are session-only and are not stored by Better Pages.

### Confluence result table

Displays permission-scoped search results in a Title/Type table. Readers may change the query for their session. Static export retains the configured query but does not freeze dynamic result rows into the file.

### Structured table and lists

For a table, enter one row per line and separate cells with `|`. The first row becomes the header. Ordered and unordered lists accept one item per line. Empty data produces an explicit state instead of an empty element.

## References

### BibTeX bibliography

Paste bounded `@article` or `@book` entries. Better Pages parses them locally, keeps at most 50 entries in input order, and displays the entry key as the citation ID. Invalid input produces **No valid BibTeX entries.**

### Local footnotes

Enter one `label|note` pair per line. The macro owns both the markers and note list, giving repeated visible labels unique local anchors. It does not collect footnotes from unrelated Confluence content outside the macro.

## External content

### Allowlisted external frame

Enter an HTTPS URL, accessible frame title, optional description, dimensions, language, direction, and fullscreen choice. Rendering requires both:

1. A matching Better Pages frame rule configured by a Confluence administrator.
2. Atlassian customer-managed egress approval for that origin and resource type.

The destination can still refuse embedding through its own Content Security Policy or `X-Frame-Options`. Static export retains the title, description, and URL instead of embedding live content.

### Allowlisted image

Enter an HTTPS image URL and meaningful alternative text/caption. The administrator must approve the exact origin for the image resource type. Frame permission for the same host does not grant image permission. Denied images show an explicit reason rather than a broken image.

## Local form

Enter one required field name per line. A Confluence administrator must enable local forms before readers can interact with them. **Validate** uses browser-local required-field validation only:

- There is no submit destination.
- Values are not transmitted or persisted.
- Reloading clears all values and validation state.
- Static export lists the required fields and states the local-only boundary.
