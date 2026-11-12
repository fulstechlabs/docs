---
title: "Compatibility and exports"
description: "Understand Markdown rendering, image handling and Confluence exports."
---

Use this reference to choose how to keep source or share rendered content from
the **Forge edition**.

## Rendering

| Content | Behavior |
| --- | --- |
| Headings, emphasis, lists, tables and fenced code | Rendered from Markdown; syntax highlighting applies to supported code languages |
| Task lists | Rendered as checkbox glyphs, not editable Confluence tasks |
| Inline and displayed LaTeX | Rendered with MathJax; use `$...$` or separate `$$` lines |
| HTTPS images | Loaded from the author-selected host, subject to that host and the reader's access |
| HTTP images | Shown as links instead of loading mixed content |
| Raw HTML | Sanitized; scripts, event handlers and unsafe URLs are removed |
| Empty source | Produces a blank macro result |

The editor preview and published macro use the same renderer. This is not a
complete LaTeX document engine or a guarantee that every TeX package, command,
HTML attribute or Markdown extension works. Check the expressions your team
uses. Source line endings may be normalized by Confluence's persistence path;
do not treat the macro as a byte-preserving archive for every line-ending format.

External images may not load for every reader or exporter. Use hosts approved
by your organization; [Privacy and data handling](../privacy-policy/) explains
the resulting external requests.

## Keep a copy of the Markdown source

Open the macro editor and copy the source to a local text file. This preserves
the Markdown and LaTeX you see in the editor. Confluence's **Export to Markdown**
action converts the page and can omit the contents of the macro.

## PDF, Word and page history

Use Confluence's page export controls for a rendered document. PDF delegates to
Confluence's native macro rendering. Word and page history use a structured
representation of the Markdown; an authorized saved-page read may be needed
when Confluence does not supply the macro configuration directly.

:::caution[Forge release validation]
Fresh native PDF and Word artifact/layout acceptance for this Forge candidate
is still pending. Do not treat the implementation or an export-job completion
message as proof that the current release's files preserve the required layout.
:::

Open the actual exported file before distributing it. Check tables, long code,
formulas, images and page breaks. A source `.md` file and a rendered PDF/Word file
serve different purposes; neither establishes the other's layout quality.

Confluence's Word export can use a `.doc` extension for an MHTML archive.
Compatibility with other document viewers varies; a viewer that opens the
file may still omit embedded formula images or change layout. Keep a source
copy and report an unusable export through [support](../support/), including
the export type and viewer name.

App licensing and Confluence content permissions still apply. A successful
export on an administrator account does not demonstrate access for every user.
