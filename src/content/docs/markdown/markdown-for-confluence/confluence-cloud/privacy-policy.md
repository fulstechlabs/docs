---
title: "App privacy statement"
description: "How the Forge and legacy Connect editions of Markdown Macro with LaTeX for Confluence Cloud handle content, browser data, images and diagnostics."
---

Fulstech provides **Markdown Macro with LaTeX for Confluence Cloud**. This
statement explains how the Forge edition handles your data. If your site
still runs Connect, see [Legacy Connect edition](#legacy-connect-edition).
The [editor guide](../overview/) helps you identify your edition.

## What both editions use

You choose what to write in a Markdown macro. The source can include personal
or confidential information. The app uses that source and its configuration to
edit and preview the macro, render Markdown and mathematical expressions, and
display the saved content. Saved source belongs to the macro on your
Confluence page. Confluence manages who can view or edit that page and
maintains page drafts and version history. The app receives license or
installation context to determine whether the macro is available.

## Forge edition

The app's editor and renderer are packaged with Forge. Preview runs in the
browser. The macro uses Confluence and Forge for saved content, licensing and
any authorized page reads. The Forge edition uses no Fulstech-operated
application database or external service to render Markdown or formulas.

| Information | How the Forge edition uses it |
| --- | --- |
| Markdown and macro configuration, including supported Connect-authored content | Render and edit the macro, and save the configuration with your Confluence page |
| Page and macro identifiers | Locate the saved macro if a supported Word or history export needs to read the page |
| Account, site, module, macro and available page identifiers | Keep browser recovery drafts separate |
| Unpublished Markdown and a draft timestamp | Recover unfinished editing in the same browser profile |
| Content identifier, export type or response status | Diagnose issues through Atlassian Forge logs |

When a supported export needs a stored page read, the app checks the requesting
user's read permission before using its app permission to read the page. Read
access to Confluence pages and permission information supports this check.
The Forge app's diagnostics use operational identifiers and statuses. Forge
logs are managed by Atlassian.

## Images and external destinations

When a macro contains an external image, your browser or a renderer may request
that image from its host. The host receives the requested URL and normal
request information, which can include an IP address and user agent. The URL
itself can carry information in its path or query. The Forge editor loads
author-selected HTTPS images and applies a no-referrer policy when it renders
them in the live macro. Following an external link is a separate interaction
with its destination.

Choose hosts that meet your organization's needs. An image request can cross
your organization's selected Atlassian data residency boundary. The image
host's privacy terms govern what it does with that request.

## Recovery drafts, retention and deletion

A successful save in the Forge editor clears the current recovery draft for
that macro in your browser. Other drafts can remain until you save them or
clear the browser's site data. Recovery drafts have no fixed expiry set by the
app. Upgrading to Forge leaves browser data from older editor integrations in
place.

Use your organization's Confluence controls to retain or delete saved content,
versions and page drafts. Uninstalling the app leaves saved page content in
Confluence. Copies you download stay wherever you save them and follow your
device and organization controls.

## Legacy Connect edition

Confluence sends the macro body and the request context needed for
authentication and licensing to Fulstech's Connect service on Google Cloud
Run. That service processes the Markdown to produce the rendered macro. The Connect service
uses registration information, including the site identifier and
authentication material, to recognize the installation. Rendered responses
can be cached. The app serves its legacy StackEdit-based editor from the Connect
service. The editor loads the existing Markdown in your browser and saves your
changes back to the macro through Confluence.

The legacy editor may leave data or settings in your browser. Its browser
diagnostics can include the Markdown being edited. Connect service diagnostics
can contain request or processing errors. Use the browser's site-data controls
for the legacy editor origin if you need to clear local data.

## Questions and requests

Contact [support@fulstech.com](mailto:support@fulstech.com) or use the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
if you have a question or need help accessing or deleting information. Provide
the app name, your site and the relevant request. Share only the details
needed to investigate. See the [Fulstech security policy](/security-policy/)
for security reporting.
