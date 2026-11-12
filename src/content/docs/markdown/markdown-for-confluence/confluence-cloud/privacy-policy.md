---
title: "Privacy and data handling"
description: "How the Forge edition of Markdown Macro with LaTeX for Confluence Cloud handles content, browser drafts, images, exports and diagnostics."
---

This notice describes **Markdown Macro with LaTeX for Confluence Cloud, Forge
edition**. It does not describe the older Connect runtime or other Fulstech
apps. Fulstech provides the app. Contact
[support@fulstech.com](mailto:support@fulstech.com) with questions about this
notice or your information.

## Content and information used

You choose what to write in a Markdown macro. That content may include personal
or confidential information. The app uses it to show formatted content and
mathematical expressions, provide an editing preview, and save the configuration
you submit to Confluence.

| Information | Purpose and location |
| --- | --- |
| Markdown and macro configuration, including supported legacy macro content | Render and edit the macro; saved with your Confluence page |
| Page and macro identifiers | Select the correct saved macro when a page read is needed for export or history |
| Account, site, module, macro and available page identifiers | Keep recovery drafts separate in your browser |
| Unpublished Markdown and a draft timestamp | Recover unfinished editing from browser local storage |
| App license status | Determine whether the macro can be used |
| Bounded operational details, such as content identifier, export type and response status | Diagnose a failed page read using Atlassian Forge logs |

The app does not ask you to enter an Atlassian password, personal access token
or API token. Information you choose to send to support is a separate
interaction; include only what is needed to explain the problem.

## Confluence, Forge and the editor

Saved Markdown belongs to the macro configuration on your Confluence page.
Confluence manages page access, drafts and version history. **Save and close**
saves the macro configuration; publishing or updating the page is a separate
Confluence action.

The editor is packaged with the app's Forge Custom UI resources. Preview and
published content use rendering libraries packaged with Forge. The current
integration does not open the external StackEdit editor or pass your macro
source to that service. There is no Fulstech-operated application database or
external formula-rendering service for this edition.

When an export needs to read the stored page, the app checks the invoking
user's read permission before using its app permission for that read. The app
requests Confluence permissions to read the page and check access to content.
Installing the app does not grant a user access to restricted pages.

## Images and external destinations

An author can include an HTTPS image URL in Markdown. The reader's browser can
request that image from the selected host; Confluence's export renderer may
also load it. HTTP images are shown as links instead of being loaded as mixed
content.

An image host receives the requested URL and normal request information, which
can include an IP address and user agent. The URL itself may contain information
in its path or query. The live macro applies a no-referrer policy to its image
elements; this does not conceal the requested URL or all network metadata.

Choose image hosts suitable for your organization's requirements. Fulstech does
not control an author-selected host's processing locations, retention, deletion
or privacy terms. Following an external link is also a separate interaction
with its destination.

## Recovery drafts and browser data

The app stores an unpublished recovery draft in browser local storage. Its key
separates the current account, site, module and macro, and includes the page
identifier when available. If required identity information is missing, local
draft recovery is unavailable. Old drafts without an account association are
not automatically restored.

A successful macro configuration save clears that macro's current draft for
the account. Other drafts can remain until a later successful save or browser
site-data cleanup. The app does not provide a fixed draft expiry period.
Browser local storage is not an encrypted vault supplied by the app: someone
with access to your browser profile or device may be able to inspect it.

Data or settings left by older editor integrations or independent StackEdit
use are not automatically removed by this edition. Use the appropriate
browser site-data controls for those locations when cleanup is needed.

## Retention, deletion and downloads

Saved macro configuration, page drafts and history follow your organization's
Confluence administration and content lifecycle. Use Confluence's content
controls to change or remove saved content. Removing a macro, deleting a page
or uninstalling the app does not automatically erase all page history or
browser-local data.

Files you download remain where you save them and in any copies you make. Use
your device and organization controls to retain or delete those copies. The app
does not manage their lifetime after download.

For an information request you cannot complete through Confluence or browser
controls, contact [support@fulstech.com](mailto:support@fulstech.com) or the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Include the app name, relevant site and the request. Do not send passwords,
tokens or unnecessary page content.

## Diagnostics and platform services

The app's diagnostic statements use bounded operational details rather than
intentionally logging full Markdown, credentials or raw Confluence responses.
There is no app-configured external logging destination. Atlassian manages
Forge logging; this notice does not promise a fixed retention period for
platform logs.

Atlassian services and SDKs, and customer-selected image hosts, can operate
their own diagnostic systems. Removing an external editor is not a guarantee
that every platform or SDK makes no network requests or processes no telemetry.

## Locations and security limits

Saved content remains with Confluence; recovery drafts remain in the browser
profile where they were created. External image requests can cross an
organization's selected Atlassian residency boundary. This app does not offer
a region selector or a pinning guarantee for all of those flows.

The app uses permission checks, trusted licensing, HTML sanitization and URL
filtering. These controls do not establish a compliance certification or a
promise of complete security. Report suspected privacy or security problems to
[support@fulstech.com](mailto:support@fulstech.com).
