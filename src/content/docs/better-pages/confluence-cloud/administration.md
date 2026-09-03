---
title: "Administration"
description: "Configure Better Pages templates, brand assets, feature controls, external content, and diagnostics."
---

Open **Confluence administration → Apps → Better Pages administration**. The
same installation-wide settings are available from **Manage apps → Better
Pages → Configure**. Only a Confluence application administrator can read or
change this page; the Forge backend checks every operation again.

## Recommended first-time setup

1. Review the site feature controls and keep optional AI, local forms, and HTML
   JavaScript disabled until your organization chooses to use them.
2. Create a small shared color palette and, if needed, a
   [Brand Kit](../brand-kits-and-colors/).
3. Synchronize selected Better Pages page starters into Confluence's native
   template catalog.
4. Confirm Numbered Headings, tab share links, welcome guidance, in-app help,
   and aggregate usage insights match your policy.
5. Leave external origins empty unless a compatibility macro has a documented
   business need.

## Site feature controls

| Control | Default | Effect |
| --- | --- | --- |
| AI in macros | Off | Enables explicit Interactive Banner generation and Smart Designer rewriting with an Atlassian-hosted Forge LLM |
| Numbered Headings | On | Allows page editors to apply and remove heading numbering |
| Display Tabs as links | On | Adds shareable, group-scoped tab URLs; tab buttons still work when off |
| Local form capability | Off | Enables browser-local validation for retained compatibility form content; there is no submit destination |
| HTML JavaScript | Off | Shows the JavaScript editor and permits isolated sandbox execution |
| Welcome pop-up | On | Shows dismissible first-use guidance on Better Pages Home |
| In-app help | On | Shows local help without an external chat service |
| Usage insights | On | Stores bounded aggregate capability view counts only |

Select **Save site feature controls** after reviewing the complete set.

## Templates, Brand Kits, and colors

The native template manager can synchronize selected page starters, update
managed copies, or remove them from Confluence's template catalog. Blog and
Delivery journey starters remain in Better Pages Home.

Use Brand Kits for published collections of colors, images, and icons. Use the
global color palette for reusable named colors without assets. See
[Brand Kits and Colors](../brand-kits-and-colors/) for publication behavior.

## External content compatibility policy

Retained compatibility content may contain HTTPS frames or images. Frame rules
accept an exact URL, `*` for one path segment, or `/**` for the remaining path.
Image rules use an exact HTTPS origin. Host wildcards and embedded credentials
are rejected.

An unmatched frame is either **Sandboxed** with scripts and forms disabled or
**Denied**. Adding an origin also requires Atlassian's administrator-owned
customer-managed egress consent. Frame and image approval are separate, even
for the same host, and a configurable group supports up to ten origins.

Observed URLs can be staged for review, but staging never grants access. Review
the final policy and Atlassian consent dialog before saving.

## Usage audit and stored diagnostics

**Macro Usage Audit Report** scans the report's supported Better Pages macro
catalog and produces a CSV with page title, page link, and detected macro
names. Results follow the administrator's Confluence access and do not inspect
another vendor's data. The current scan does not include Button Group, so review
known Button Group pages separately until that family appears in the report.

Administrators can separately clear observed external URL inventories or reset
aggregate usage counters. These actions do not delete pages, macro
configuration, Brand Kits, colors, templates, or approved policy rules.

## Concurrent changes

Settings are revisioned. A stale browser tab cannot overwrite a newer save.
Reload the administration page, review the latest values, and apply the change
again. External egress updates may also be temporarily locked while Atlassian
consent or revocation is in progress.
