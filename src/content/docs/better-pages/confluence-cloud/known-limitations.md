---
title: "Known Limitations"
description: "Current Better Pages Release 13 boundaries to consider before creating or maintaining Confluence Cloud pages."
---

These are customer-relevant boundaries of Better Pages Release 13 for Confluence
Cloud, not a list of every Confluence limitation. For a failed workflow, use
[Troubleshooting and Support](../troubleshooting-and-support/).

## Migration and platform

Better Pages does not automatically read or convert another vendor's private
Data Center app data or macros. Plan a manual content review for a Data Center
migration rather than expecting the Cloud app to transform those pages. The
Release 13 existing-installation upgrade check concerns this Better Pages Cloud app,
not third-party Data Center conversion. See the [Overview](../overview/#availability-and-migration)
and [FAQ](../faq/).

## Composer and published content

- Composer can preview the *current Confluence editor draft* from its
  in-editor launcher, but cannot apply a page-level change over that unsaved
  editor work. Save or close the editor, then open Composer from the published
  page's Better Pages byline for a reviewed write. See
  [Composer](../smart-designer/#save-draft-close-reopen-or-publish).
- Composer's native-block editing covers supported headings, paragraphs,
  lists, quotes, code, panels, dividers, and simple tables. Existing macros,
  complex tables, and media are protected rather than silently rewritten.
  Edit those in their appropriate Confluence or macro editor. See
  [Composer](../smart-designer/#choose-an-authoring-path).
- A published Brand Style is a snapshot. Editing or unpublishing its preset
  does not restyle pages already saved with it. Reapply the current published
  choice when updating a page. See
  [Brand Kits and Brand Styles](../brand-kits-and-colors/#for-authors-choose-a-published-look).

## Page and space operations

- A **Delivery journey** creates published linked pages after confirmation;
  it is not the private single-page draft used by other page templates. Check
  the space and hierarchy before creating it. See
  [Templates and Better Pages Home](../templates-and-home/#other-template-outcomes).
- Space Manager operations run with your Confluence permissions and may stop
  after some items succeed if permission or page state changes. Review the
  completed-operation list and refresh before retrying; do not rerun a full
  selection blindly. See [Space Manager](../space-manager/#preview-and-run-page-actions)
  and [Troubleshooting](../troubleshooting-and-support/#space-manager-stopped-partway).
- In the current **Tabs** group editor, deleting a tab also deletes its owned
  rich-content section. Review that section before confirming the edit. See
  [Tabs](../macros/tabs/#add-a-tab-group).

If one of these boundaries changes, the linked feature guide is the detailed
procedure; this page is a quick evaluation checklist.
