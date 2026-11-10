---
title: "Move from the Connect editor"
description: "Check existing Markdown macros before and after a same-site Connect-to-Forge update."
---

Validate existing Markdown macros when your Confluence Cloud site updates from
the Connect app to the Forge edition. This procedure covers the existing app
on the same site; it does not describe a Data Center or cross-site migration.

## Before the update

A Confluence administrator must manage the app update. Keep the existing app
installation and existing pages in place. Do not uninstall the app or recreate
macros as a migration step.

1. Choose representative pages: ordinary Markdown, tables, inline and block
   mathematics, images, and pages with more than one macro.
2. Record the visible result and keep a copy of each macro's source. If the old
   editor has no source-download action, open it and copy the source to a local
   text file without changing the page.
3. Include a page with restrictions. Record which test users should be able to
   read and edit it; app installation does not override Confluence permissions.
4. Retain the page's normal version history and your organization's backups.

## Apply the update

When the Forge update is available for the site, have an administrator apply
it to the **existing app installation** through Atlassian's update flow.
Review the permissions shown there. The Forge app requests permission to read
pages and check content access when saved source is needed for export/history.

The updated app can read supported legacy macro body content. Its first Forge
save stores the current source in the macro's Forge configuration. You do not
need to paste the source into a replacement macro to start using the editor.

The Forge editor is bundled with the app and has **Save and close**, side
preview and Markdown help. Independent StackEdit settings, browser caches or
cloud-account integrations are not moved into this editor. Historical
browser data is not automatically erased.

## Check the existing macros

1. Reload each selected page before editing. Compare headings, tables, formulas,
   links and images with the saved baseline.
2. Edit the page and open the **existing** macro. Check that its source matches
   the copy you kept. If source is blank or wrong, stop before saving.
3. For a correct macro, make a small reversible edit, select **Save and close**,
   then **Update** the Confluence page.
4. Reload, reopen that macro and compare the saved source again. On pages with
   several macros, check each independently.
5. Check search, history and required exports for your content. Open the actual
   downloaded files and inspect formulas and layout; a completed export job
   alone does not establish a usable file.
6. Verify access with the intended ordinary and restricted users.

## If something differs

Preserve the page and your source copy. Avoid saving an unexpectedly empty
editor, uninstalling the app, or repeatedly replacing the macro. Reopening
browser drafts can also affect what you see; check whether the recovery notice
is present.

Contact [support](../support/) with the app edition, site, affected page/macro,
expected result, a minimal safe source sample and a redacted screenshot.
There is no app-provided one-click Forge-to-Connect rollback. Confluence page
history can help inspect earlier content, but it is not a promise that reverting
a page restores the previous app runtime or every editor integration.

See [Write and edit Markdown](../usage/) for the new workflow and
[Compatibility and exports](../compatibility-and-exports/) for validation limits.
