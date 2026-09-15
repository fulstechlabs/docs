---
title: "Permissions and data handling"
description: "Learn what the Forge app reads, stores, processes, and sends outside Atlassian."
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

## Processing and egress

- MathJax SVG is produced in a Forge function.
- Advanced TeX Live PNG is produced in an app-owned Forge Container.
- Object Store and KVS are Atlassian Forge services partitioned by installation and environment.
- Formula source and derived output are not sent to Fulstech infrastructure, a public CDN, or a third-party renderer.
- The app does not provide customer-configured egress.

The deployed Forge version is eligible for Atlassian's **Runs on Atlassian** program. Eligibility is a platform status, not a separate security certification.

## Why the app requests Confluence scopes

| Scope group | Why it is needed |
| --- | --- |
| Page/content read scopes | Read formulas, macro configuration, published page metadata, and export context. |
| Space and content-details read scopes | Search and resolve pages in the user's accessible Confluence context, including legacy-compatible routes. |
| `read:hierarchical-content:confluence` | Enumerate descendants only when an equation list includes child pages. |
| `storage:app` | Use Forge Object Store and KVS for derived artifacts and reference indexes. |

The hierarchical-content scope is read-only. Adding it caused a Forge major upgrade because existing site administrators must review the new permission.

For organization-wide legal terms, see the [Privacy Policy](/privacy-policy/), [Security Policy](/security-policy/), and [EULA](/end-user-license-agreement/).

