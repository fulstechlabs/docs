---
title: "Better Pages Privacy Policy"
description: "How Better Pages for Confluence Cloud processes, stores, shares, retains, and deletes data."
---

**Effective date:** August 28, 2026

This policy explains how Fulstech processes information when a customer
installs and uses Better Pages for Confluence Cloud (the **App**). It applies to
Better Pages and supplements the customer's agreement with Fulstech and
Atlassian.

## What the App processes

| Information | Purpose | Location or recipient |
| --- | --- | --- |
| Macro configuration, created pages, templates and page attachments | Render and manage the content selected by an author | Customer-controlled Confluence content |
| Site controls, external-content policy, observed external URLs and revision/operation state | Apply administrator choices safely and prevent stale concurrent changes | Atlassian Forge hosted storage |
| Brand Kits, colours, verified uploaded assets and selected stock-image copies | Reuse approved visual resources | Atlassian Forge hosted storage and object storage |
| Account-scoped welcome and alert dismissal state | Remember a signed-in user's dismissal choice | Atlassian Forge hosted storage; welcome state uses a SHA-256-derived account key |
| Page-level Numbered Headings state | Reapply the author's numbering configuration after a page update | Atlassian Forge hosted storage |
| Bounded aggregate capability counters | Show relative feature usage when Usage insights is enabled | Atlassian Forge hosted storage; no page ID, user ID, query or macro body is included |
| Permission-scoped page, space, user, group, attachment, label and restriction results | Populate searches, previews, inventories and plans | Returned to the signed-in browser session; these result rows are not copied to an external Fulstech database |
| Interactive Banner goal/prompt and optional bounded same-site page excerpt | Generate a reviewable draft after an administrator enables AI | Atlassian-hosted Forge LLM; inputs are not copied into App storage |
| Smart Designer selected text and tone | Generate a reviewable rewrite after an administrator enables AI | Atlassian-hosted Forge LLM; unselected page content is not sent |
| An author-entered stock-image search phrase | Search public images after an explicit action | `commons.wikimedia.org` over HTTPS |
| Selected public image bytes and attribution metadata | Copy the chosen image into an Atlassian-hosted App asset or Confluence attachment | Fetched from `upload.wikimedia.org`; stored in Atlassian services |

The App does not request Atlassian passwords, personal access tokens or API
tokens. It has no Fulstech-owned application server, customer database,
advertising tracker, analytics SDK or support-chat widget.

## AI choices

AI features are off by default. A Confluence administrator must enable them,
and an author must explicitly request each generation. Better Pages uses the
Atlassian-hosted Forge LLM, not a Fulstech or independently selected AI service.
Generated output remains a draft until the author chooses to use it.

## External frames, images, and Wikimedia

Compatibility frames and external images load only when both Atlassian's
installation-level customer-managed egress permission and the narrower Better
Pages site policy permit the destination. The reader's browser—not a Fulstech
proxy—requests that resource. The destination may receive normal browser and
network information, including IP address, user agent, referrer behavior, and
destination cookies. Its own privacy and security terms apply.

Stock-image search is different: after an author submits a search, the App sends
the bounded phrase to Wikimedia Commons and downloads only a supported,
freely-licensed image the author selects. Better Pages retains source, creator
and licence attribution with the selected asset.

Administrators should approve only destinations their organization trusts.
Destination CSP, `X-Frame-Options`, authentication, availability and browser
controls remain authoritative. The App never forwards Atlassian credentials.

## Permissions and access

Confluence reads and user-initiated writes run as the signed-in user and remain
subject to that user's Confluence permissions. Site-setting and diagnostic-data
changes also require a backend check that the current user has Confluence's
application-level administer operation. A UI display condition is not treated
as authorization by itself.

## Data residency and international transfers

Confluence content and persistent Forge hosted storage follow Atlassian's data
residency controls for Forge. Atlassian publishes the current supported realms
and behavior in its [Forge data residency documentation](https://developer.atlassian.com/platform/forge/data-residency/).

An explicit Wikimedia search or customer-approved external frame/image may
cross the customer's selected Atlassian residency boundary. Wikimedia and each
customer-selected destination determine their own processing locations. A
customer should enable those features only when they fit its privacy and
transfer requirements.

## Retention and deletion

- Macro settings, pages and attachments follow the customer's Confluence
  retention, permissions, trash and deletion controls.
- Administrators can clear the App's observed external-URL inventories and
  reset aggregate usage counters from Better Pages administration.
- Site policy, Brand Kits, colours, assets, dismissal state and operation state
  remain while the App is installed unless removed through an available App or
  Confluence control.
- Atlassian currently retains Forge hosted storage for up to 28 days after
  uninstall. It is not automatically restored. Atlassian's recovery process
  requires customer consent and a qualifying request within its documented
  recovery window.
- Better Pages does not keep another copy after Atlassian removes the hosted
  data. A downloaded report remains wherever the administrator saved it.

For an authorised access, correction, deletion or recovery request that cannot
be completed in Better Pages or Confluence, contact
[support@fulstech.com](mailto:support@fulstech.com) or use the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Fulstech may need the site and installation identifiers and will verify the
requester's authority.

## Security

Better Pages uses Forge isolation and hosted storage, Confluence permission
checks, bounded input, URL and file validation, HTML sanitisation, sandboxed
optional JavaScript, explicit administrator controls and dependency scanning.
No system can be guaranteed completely secure. Report a suspected security or
privacy issue to `support@fulstech.com` and label it security-sensitive.

## Changes and contact

Fulstech will update the effective date and publish material changes at this
URL. Questions can be sent to
[support@fulstech.com](mailto:support@fulstech.com) or the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
