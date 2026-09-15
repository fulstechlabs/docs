---
title: "Cloud upgrades and Connect compatibility"
description: "Understand the Forge major upgrade, existing Connect macros, and Data Center migration boundary."
---

## Upgrading the Cloud app from Connect to Forge

LaTeX for Confluence keeps the same Marketplace identity and compatible macro keys when the Cloud app moves from Connect to Forge. Site administrators upgrade the existing app; users do not install a second product or run a content migration job.

Existing supported Connect-format formula and reference configurations continue to render. When a user opens and saves a legacy macro in the Forge editor, the app preserves its formula, placement, alignment, and Reference key while writing the current configuration format.

The app does not rewrite every page in the background. Untouched macro data remains in Confluence and is interpreted when the page renders or the macro is edited.

## Why an administrator may see an approval request

Forge Production 6.0.0 adds the read-only `read:hierarchical-content:confluence` scope. It allows **LaTeX equation list** to enumerate published descendants when **Include child pages** is enabled.

Atlassian classifies a permission change as a major Forge upgrade. Existing sites remain on their current working version until a site administrator reviews and accepts the new permission. New installations receive the current version during installation.

After approval, verify a page with an existing formula, a reference, and—if used—an equation list. No manual conversion should be required.

## Confluence Data Center and Server are different migrations

Connect-to-Forge compatibility applies to Confluence Cloud content already using this Marketplace app. Moving content from Confluence Data Center or Server to Cloud is a separate Atlassian migration workflow.

See [Migrate to Confluence Cloud](../../confluence-data-center-and-confluence-server/migrate-to-confluence-cloud/) for the supported Data Center/Server instructions. Keep the source site and a backup until you have verified representative formulas on Cloud.

If migrated content displays an unknown macro or loses configuration, do not recreate it immediately. Record the source platform/app version, affected macro name, page migration method, and a sanitized screenshot, then [contact support](../support/).
