---
title: "Release Notes"
description: "Verified Better Pages for Confluence Cloud release changes and deployment identifiers."
---

This page records verified public Better Pages releases. **Better Pages Release
13.2** is the current customer-facing release identity. Forge and Marketplace version
numbers are Atlassian-managed deployment identifiers mapped to that release;
use them when checking an installation in Atlassian administration.

## Better Pages Release 13.2 — October 1, 2026

**Release record:** [Release 13.2 source and deployment mapping](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/blob/main/releases/13.2.json).
**Atlassian deployment identifier:** Forge/Marketplace `2.4.0`, Marketplace build `2001030`.
**Repository release:** [release-13.2](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/releases/tag/release-13.2).

### Fixed and hardened

- Resource hub and Composer-generated resource cards now render inside Tabs.
- Older affected Composer content is repaired when displayed, without rewriting
  the page. This does not rebuild tab structure damaged by the earlier save bug.
- The Release 13.1 Tabs persistence and direct Composer publishing fixes remain
  verified, along with independent private **Save draft**.

Production checks used a licensed Fulstech test site: old pages were read
without editing, fresh Resource hub panels survived a cold reload, Tabs retained
both names and a second-tab default, and Composer history recorded V1 → V2.
Scopes, licensing, pricing and permissions are unchanged. See
[Known Limitations](../known-limitations/) for the remaining bounded cases.

## Better Pages Release 13.1 — October 1, 2026

**Release record:** [Historical Release 13.1 record](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/blob/main/releases/13.1.json).
**Atlassian deployment identifier:** Forge/Marketplace `2.3.0`, Marketplace build `2001020`.
**Repository release:** [release-13.1](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/releases/tag/release-13.1).

### Fixed and hardened

- New structured Tabs groups retain names, rich sections and the selected
  default through save, publish and reopen.
- Composer can publish a new private page directly and publish a later edit;
  **Save draft** remains independent.

Production acceptance exposed a separate Resource hub rendering problem inside
Tabs. Release 13.2 fixes that issue; the 13.1 tag and its partial historical
acceptance record are preserved.

## Better Pages Release 13 — September 28, 2026

**Release record:** [Release 13 and its verified source/deployment mapping](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/blob/main/releases/13.json).
**Atlassian deployment identifier:** Forge/Marketplace `2.2.0` ([public Marketplace listing](https://marketplace.atlassian.com/apps/157694075/better-pages-tabs-formatting-macros-for-confluence)).

- **Create a page from an outcome:** [Better Pages Home](../templates-and-home/)
  offers 49 editable starters or a private blank draft, with a path into
  [Composer](../smart-designer/).
- **Build and review sections:** Composer includes 12
  [Section Patterns](../section-patterns/). Preview and arrange the canvas
  before explicitly saving a draft or publishing.
- **Keep an approved look:** Administrators can publish
  [Brand Kits and semantic Brand Styles](../brand-kits-and-colors/) for
  supported components. Applying a style copies its current values into the
  page; it is not a live styling rule.
- **Keep familiar building blocks:** The existing 19
  [Better Pages macros](../macros/) remain available, and written content
  remains editable through Confluence and supported macro configuration.

The release was validated on a licensed development tenant for authoring,
save/reopen, publishing, existing-installation upgrade continuity,
accessibility, and export checks. The production Forge deployment and public
Marketplace version are recorded in the [GitHub Release](https://github.com/fulstechlabs/confluence-cloud-mosaic-forge/releases/tag/v13.0.0).
Its historical Git tag is `v13.0.0`; that tag is technical trace metadata, not
a second Better Pages release name. For a first
page, follow [Getting Started](../getting-started/); for current boundaries,
see [Known Limitations](../known-limitations/).

Older release entries will be added only when their identity and customer
changes can be verified. This page does not imply that Release 13 was the first
Better Pages release.
