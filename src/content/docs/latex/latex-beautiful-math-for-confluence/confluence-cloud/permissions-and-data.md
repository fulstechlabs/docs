---
title: "Security, privacy, and data handling"
description: "Learn what the Forge app reads, stores, processes, retains, and sends outside Atlassian."
---

LaTeX for Confluence Cloud runs on Atlassian Forge. It has no Fulstech-hosted rendering endpoint and no external runtime egress for formula processing.

## What the app accesses

The app reads the Confluence page content and metadata needed to:

- render the current formula and its configuration;
- number formulas and resolve a Reference key;
- search for a selected reference page;
- list equations from a page;
- enumerate child pages when **Include child pages** is enabled;
- build PDF and Word export output.

Reference and equation-list reads run as the current user. Confluence therefore enforces that person's existing page permissions before the app returns equation information.

## Where data is stored

The source formula and macro configuration remain in the Confluence page.

The app also stores rebuildable derived data within Forge:

| Data | Forge service | Purpose | Retention |
| --- | --- | --- | --- |
| Rendered SVG or PNG artifact | Object Store | Reuse unchanged output for page view and export | Up to 90 days |
| Page/revision identity and hashed Reference-key-to-number index | Key-Value Store | Resolve current published equation numbering efficiently | 30-day logical TTL |

The reference index does not store formula source, rendered images, page titles, or raw Reference keys. Hashing minimizes data but does not make derived customer data anonymous.

Editor preview sessions avoid persistent artifact storage until the saved/published and export paths need durable reuse. Temporary TeX Live files are created for one request inside the Forge Container and removed when that request ends.

Forge Object Store is currently an Atlassian Preview capability. Atlassian describes Preview features as supported for production use while still under active development and potentially subject to shorter deprecation windows. See [Forge storage](https://developer.atlassian.com/platform/forge/storage-reference/).

## Processing and egress

- MathJax SVG is produced in a Forge function.
- Advanced TeX Live PNG is produced in an app-owned Forge Container.
- Object Store and KVS are Atlassian Forge services partitioned by installation and environment.
- Formula source and derived output are not sent to Fulstech infrastructure, a public CDN, or a third-party renderer.
- The app does not provide customer-configured egress.

The deployed Forge version is eligible for Atlassian's **Runs on Atlassian** program. Eligibility is a platform status, not a separate security certification.

Forge Container services are currently an Atlassian Preview capability. They run on Atlassian infrastructure and are fully supported, but remain under active development. See [Managing containerised services](https://developer.atlassian.com/platform/forge/containers-reference/managing-service/).

## Analytics and operational diagnostics

The app does not send product-usage analytics to Fulstech or a third-party analytics service. Operational logging is handled through Forge. The app records bounded failure categories and response status where needed for diagnosis; it is designed not to log formula source or page content.

If you contact support, Fulstech receives the information you choose to submit. Remove confidential formulas, credentials, cookies, and unrelated customer data before sharing a screenshot or error report.

## Data residency

The Object Store and KVS entries described above use Forge hosted storage. Atlassian partitions this storage by app installation and manages its residency together with the host Atlassian app where supported. Runtime placement is managed by Atlassian. See [Forge data residency](https://developer.atlassian.com/platform/forge/data-residency/) for current realms and migration behavior.

The app does not copy formula data to a Fulstech database or an external rendering service, so there is no separate Fulstech processing region to select.

## Retention, uninstall, and recovery

- Formula source and macro configuration follow the customer's Confluence page retention, version, trash, and deletion controls.
- Rebuildable render artifacts expire after up to 90 days. Derived reference-index entries use a 30-day logical TTL and can be rebuilt from current published content.
- Uninstalling the app does not delete the Confluence pages or their saved macro configuration. The macros may not render or be editable while the app is unavailable.
- Atlassian currently retains Forge hosted storage for 28 days after uninstall. Reinstalling does not automatically restore the previous installation's data. A recovery request requires customer consent and must be submitted within Atlassian's documented window. See [Forge storage recovery](https://developer.atlassian.com/platform/forge/storage-reference/).
- After Atlassian removes the hosted data, Fulstech does not retain another copy. The derived cache can be rebuilt from Confluence after a supported recovery or reinstall path.

## Why the app requests Confluence scopes

| Scope | Why it is needed |
| --- | --- |
| `read:confluence-content.all` | Read legacy-compatible Confluence content routes used by existing macros. |
| `read:page:confluence` | Read pages selected for formula numbering, references, equation lists, and export. |
| `read:hierarchical-content:confluence` | Enumerate descendants only when an equation list includes child pages. |
| `read:space:confluence` | Resolve the spaces that contain accessible source pages. |
| `read:content:confluence` | Read current Confluence content used by compatibility and export paths. |
| `read:content-details:confluence` | Read content metadata needed to identify and resolve pages. |
| `read:space-details:confluence` | Read space metadata used by page search and legacy-compatible routes. |
| `read:blogpost:confluence` | Preserve content lookup compatibility where Confluence returns blog posts. |
| `storage:app` | Use Forge Object Store and KVS for derived artifacts and reference indexes. |

The hierarchical-content scope is read-only. Adding it caused a Forge major upgrade because existing site administrators must review the new permission.

For organization-wide legal terms, see the [Privacy Policy](/privacy-policy/), [Security Policy](/security-policy/), and [EULA](/end-user-license-agreement/). For an access, correction, deletion, or recovery request that cannot be completed in Confluence, use the [Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
