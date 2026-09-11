---
title: "App privacy policy"
description: "How Excalidraw, Mermaid, PlantUML - Whiteboard for Confluence processes, stores, shares, retains, and deletes data."
---

**Effective date:** September 11, 2026

This policy explains how Fulstech processes information when a customer
installs and uses **Excalidraw, Mermaid, PlantUML - Whiteboard for Confluence**
(the **App**). It applies to the Forge Cloud app and supplements the customer's
agreements with Fulstech and Atlassian.

## Information the App processes

| Information | Purpose | Location or recipient |
| --- | --- | --- |
| Diagram source, editor configuration, preview images and storage metadata | Create, edit, display, copy and export diagrams | Atlassian Forge hosted storage and the customer's Confluence site |
| Current page content, draft content, page identifiers and macro identifiers | Preserve supported Connect macros, enforce page access and produce Confluence exports | Processed through Atlassian APIs; not copied to a Fulstech-owned database |
| Excalidraw Personal Library items and Mermaid source-history snapshots | Let the current user reuse or recover editor content | The user's browser local storage |
| Graphviz diagram source | Generate the requested SVG preview | Sent over HTTPS, compressed and encoded in the request URL, to `kroki.io` |
| PlantUML diagram source | Generate the requested SVG preview | Sent over HTTPS, compressed and encoded in the request URL, to `www.plantuml.com` |
| A public GitHub Gist identifier and revision selected by the user | Import Mermaid source after an explicit user action | Requested by the user's browser from `api.github.com` and, when needed, `gist.githubusercontent.com` |
| Normal browser and network information, such as IP address and user agent | Load declared editor, font and rendering resources | The applicable external destination |

The App does not request Atlassian passwords, personal access tokens or API
tokens. It has no Fulstech-owned application server, customer-content database,
advertising tracker or runtime analytics SDK.

Do not put passwords, tokens or other secrets in diagram source. Diagram source
can also contain personal or confidential information entered by an author.

## External diagram services

Graphviz and PlantUML previews use public rendering services. Encoding source
in a URL is not encryption. The renderer must receive and decode the source to
produce the image, and normal network metadata is also visible to the service.
Fulstech does not use those services to retain a separate customer diagram
library.

The App loads the DrawIO editor from `embed.diagrams.net`. In the embed mode
used by the App, editable XML is exchanged client-side between the Forge UI and
the embedded editor. The provider states that this diagram data is not sent
back to or sourced from its application server. Loading the editor can still
disclose normal browser and network information to the destination.

Mermaid Gist import is optional and runs only after the user supplies and loads
a public Gist. It reads the selected source into the editor; it does not upload
the current page's diagram to GitHub. Font resources are loaded from `esm.sh`;
the App does not intentionally include diagram source in those font requests.

The external services have their own privacy, security, availability and
logging practices. See the [Forge app guide](../forge-preview/#data-processing)
before using an externally processed diagram type with restricted content.

## Permissions and access

The App checks the current user's Confluence page permissions before reading or
updating page content with app authority. Forge storage is isolated by
installation. Stored diagram identifiers and trusted Confluence context are
validated before app-owned diagram data is returned or changed.

The App requests only the Confluence and Forge scopes described in
[Security and privacy](../security-and-privacy/#why-permissions-are-requested).

## Data residency and international processing

Persistent Forge hosted storage follows Atlassian's data residency support and
the customer's selected Atlassian realm. Atlassian documents the current
locations and behavior in its [Forge data residency documentation](https://developer.atlassian.com/platform/forge/data-residency/).

Requests to public Graphviz, PlantUML, DrawIO, GitHub or font services are not
covered by the customer's Atlassian data residency choice. Those destinations
may process network information—and, for Graphviz and PlantUML, diagram
source—outside the customer's selected Atlassian region or outside the EEA.
Customers should use those features only when the destination and transfer
conditions meet their own requirements.

## Retention and deletion

- Confluence page content and macro parameters follow the customer's
  Confluence retention, version, trash and deletion controls.
- App-owned diagram records remain in Forge hosted storage while the App is
  installed unless they are replaced or removed through a supported App flow.
- Atlassian currently retains Forge hosted storage for up to 28 days after
  uninstall for possible recovery. Recovery is not automatic and is subject to
  Atlassian's documented process and customer consent.
- Personal Library items and local source history remain in the browser until
  the user clears them, clears browser data, or the browser removes them. They
  are not synchronized to Fulstech.
- Fulstech does not retain another customer-content copy after Atlassian removes
  the hosted App data. Files downloaded by a user remain wherever that user
  saved them.
- Third-party destinations control their own transient processing and network
  log retention. The PlantUML public server states that it does not store
  diagrams, although it may temporarily enable HTTP traces. Do not treat that
  statement as an Atlassian or Fulstech retention guarantee.

## Requests, changes and contact

For an authorised access, correction, deletion or recovery request that cannot
be completed in Confluence or the App, contact
[support@fulstech.com](mailto:support@fulstech.com) or use the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Fulstech may need the site, page and installation identifiers and will verify
the requester's authority.

Fulstech will update the effective date and publish material changes at this
URL. Report a suspected security or privacy issue to the same support address
and label it security-sensitive.
