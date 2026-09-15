---
title: "Connect permissions and data"
description: "Understand what the current Confluence Cloud Connect app reads, processes, and stores."
---

This page applies to the Connect app currently available from Atlassian
Marketplace. The separate [Forge preview](../forge-preview/) has a different
runtime, permission model, and storage architecture.

## Confluence access

The Connect descriptor requests the **READ** scope. Confluence sends signed
requests to the app service when it opens an editor or renders a macro. Those
requests can include the macro body or configuration needed to render the
diagram.

The app does not need your Atlassian password or a personal API token. Never put
passwords, access tokens, or other credentials in diagram source.

## Where content is processed or stored

| Content | What happens in the Connect app |
| --- | --- |
| Macro source and editor configuration | Saved with the macro on the Confluence page. The app service receives this data when Confluence asks it to edit or render the macro. |
| Excalidraw scene and preview | The editable scene is saved in macro configuration. The app creates a preview image; current product code supports storing generated image assets in external object storage. |
| Mermaid, Graphviz, and PlantUML source | Saved as macro body text and sent to the app service for rendering. Generated image assets can be cached by the app service. |
| BPMN and DrawIO content | Saved with the macro together with preview data. The DrawIO editor loads from `embed.diagrams.net`. |
| Excalidraw Personal Library | Stored in the current browser's local storage. It is not a shared Confluence library or a page backup. |
| Connect installation and authentication records | Stored by the app service so it can validate requests from installed Confluence sites. |

The Connect source does not establish a customer-facing retention period for
generated assets. If retention, deletion location, or processing region affects
your adoption decision, contact Fulstech support before using the app with
restricted content.

## Access control

Confluence page permissions control who can open a page containing a diagram.
The app's Connect service also validates signed Atlassian requests. Do not use a
diagram as a separate access-control boundary; anyone who can view or edit the
page may be able to view the rendered content.

## Browser-local libraries

Excalidraw library items remain in the browser profile where you added them.
They are not synchronized to teammates or another browser. Export an
`.excalidrawlib` file when you need a portable copy, and do not rely on browser
storage as the only backup.

## Support and privacy requests

For a data-handling, deletion, or security question, use the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
or email [support@fulstech.com](mailto:support@fulstech.com). Include the product
and platform, but do not attach confidential diagram source, credentials, raw
browser archives, or unrelated customer data unless your organization has
approved that disclosure.

For organization-wide terms, see the [Privacy Policy](/privacy-policy/),
[Security Policy](/security-policy/), and [EULA](/end-user-license-agreement/).
