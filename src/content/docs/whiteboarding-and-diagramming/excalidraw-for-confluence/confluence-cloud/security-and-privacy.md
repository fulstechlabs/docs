---
title: "Security and privacy"
description: "Understand Forge storage, authorization, permissions, external processing, and local browser data."
---

**Excalidraw, Mermaid, PlantUML - Whiteboard for Confluence** runs on Atlassian
Forge and uses Confluence Cloud APIs. It is not eligible for the **Runs on
Atlassian** program because Graphviz and PlantUML use declared external
renderers and other optional resources load from declared external domains.

For the customer-facing privacy notice, read the
[App privacy policy](../privacy-policy/).

## Data stored by the App

Atlassian Forge hosted storage contains app-owned diagram source,
configuration, preview images and bounded storage metadata. Large payloads can
be compressed and divided into installation-scoped records. Compatible source
or preview data can also remain in the Confluence macro body so existing pages
continue to render through supported upgrades.

Excalidraw Personal Library items and Mermaid local-history snapshots are
stored only in the current browser. They are not shared Forge storage, team
history or a substitute for Confluence page versions. Use the editor's export
tools when you need a portable backup.

The App has no Forge Remote and no Fulstech-owned customer-content server.

## Authorization

Before a resolver reads or changes Confluence content using app authority, it
derives the page from trusted Forge context and checks whether the invoking user
can read or update that page. Payload page identifiers cannot redirect an
operation to a different page. Diagram type, identifier and storage shape are
validated before stored content is used.

The browser UI is not treated as the authorization boundary. Confluence page
permissions and backend checks remain authoritative.

## Why permissions are requested

- `read:page:confluence` reads the current or draft page structure needed to
  open supported legacy macros and produce Confluence exports.
- `write:page:confluence` updates the draft page structure when the first save
  of a supported Connect text diagram adopts it into the Forge format.
- `read:content.permission:confluence` verifies that the invoking user may read
  or update the page before privileged app operations.
- `storage:app` stores app-owned diagram source, configuration, previews and
  chunk metadata within the Forge installation.

## External processing

| Destination | When it is used | Information sent |
| --- | --- | --- |
| `kroki.io` | Render Graphviz | Compressed/encoded diagram source in the HTTPS request URL and normal network metadata |
| `www.plantuml.com` | Render PlantUML | Compressed/encoded diagram source in the HTTPS request URL and normal network metadata |
| `embed.diagrams.net` | Load the DrawIO editor | Normal network metadata; editable XML is exchanged client-side with the embedded editor |
| `api.github.com`, `gist.githubusercontent.com` | Explicit Mermaid public-Gist import | Selected public Gist/revision request and normal network metadata; no current diagram upload |
| `esm.sh` | Load declared font resources | Normal resource-request metadata; no diagram source is intentionally included |

All destinations are allowlisted in the Forge manifest. The App does not send
Atlassian credentials, personal access tokens or customer API secrets to them.
Read [Data processing](../forge-preview/#data-processing) before using an
external renderer with confidential content.

## Security practices and support

The release uses Forge isolation and hosted storage, trusted context,
Confluence permission checks, bounded input and storage validation, declared
egress, dependency audits, secret scanning and Atlassian's Forge Marketplace
security scanner. No system can be guaranteed completely secure.

Contact [support@fulstech.com](mailto:support@fulstech.com) or the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
for security and privacy questions. Label suspected security issues as
security-sensitive and do not include confidential diagram source unless your
organization has approved sharing it through the support channel.
