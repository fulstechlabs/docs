---
title: "Help and troubleshooting"
description: "Resolve Markdown editor, preview, license, draft and export problems in Confluence Cloud."
---

These checks apply to the **Forge edition**. If you still use the check-icon
editor, see the [Connect editor guide](../connect-editor/) and tell support
which editor you have.

## The macro says an active license is required

Ask your Confluence administrator to check the app's evaluation or subscription
in Atlassian's app management. An inactive license blocks rendering, source
download and editing. Do not uninstall the app as a license troubleshooting step.
Your page content and the billing entitlement are different things.

## I saved the macro but readers see the old content

**Save and close** updates the macro in the Confluence draft. You still need to
**Publish** or **Update** the page. Reload the reader view after that action.
On a page with several macros, reopen the intended macro and check its source.

## The editor shows a recovered draft

A local recovery draft can be newer than the published source. Review the
**Recovered your unsaved draft** notice and the source before saving. Recovery
is scoped to the account and macro in the current browser profile; another
profile or device may not contain it.

If the recovered text is unwanted, replace it with the source you intend to
save and select **Save and close**, then publish/update only when ready.
Do not clear all browser site data as a first diagnostic step; it can remove
unfinished work. See [data handling](../privacy-policy/) for storage boundaries.

## Preview, math or an image differs from what I expected

Wait for **Up to date** in the preview. Check the formula delimiters and start
with a minimal expression such as `$F=ma$`. Unsupported TeX or unsafe HTML/URLs
can behave differently from another editor. For images, check that the URL uses
HTTPS and that the host allows access for the reader.

Compare the same source in the preview and published macro. If an old Connect
macro opens blank after an update, stop before saving and follow the
[migration checks](../migration/).

## The editor cannot save

Keep a copy of your source before retrying. Check page-edit permission and the
app license. The error message can report that a browser draft was retained
when storage was available; do not assume it exists on another device.
Escape in the source editor is a save-and-close shortcut, not a discard command.

## A download or export is incomplete

For Markdown source, use **Download Markdown** on the intended rendered macro.
For PDF/Word, inspect the actual downloaded file and record the viewer used.
A whole-page Markdown conversion can omit macro content. The current Forge
candidate's native PDF/Word layout gate remains open; see
[Compatibility and exports](../compatibility-and-exports/).

## Contact Fulstech

Use the [Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
or email [support@fulstech.com](mailto:support@fulstech.com).
Include:

- App name, Forge/Connect editor, site and affected page or macro.
- Steps, expected result, actual result and exact error message.
- Export type and document viewer, when relevant.
- A minimal safe source sample and a redacted screenshot when they explain the issue.

Do not send passwords, API tokens, cookies, raw session logs or unnecessary
customer content. Ask support for a suitable evidence-sharing method if the
problem requires confidential material.
