---
title: "Upgrading from Connect"
description: "Check existing content and understand the Cloud Forge successor."
---

Forge 3.6.0 is the approved successor on the existing Marketplace listing. Publication does not mean every Connect installation has upgraded. A Jira administrator should check the installed version and any update or permission prompts in app management.

## Existing content and settings

Markdown values remain in Jira fields. Forge retains the legacy project-setting keys to read existing mappings. There is no customer-operated JSON export/import wizard.

Do not delete or recreate fields, clear settings, or uninstall the existing app as an upgrade step without a support plan.

## What changes?

- The issue panel is **Rich Text Custom Fields**; project settings remain **Markdown Fields**.
- The Forge-owned **Rich Text Editor Custom Field** type is available for new fields.
- Images and attachment references display as links.
- Legacy AI Copilot is not included.
- Native field and search/list views do not run the full rich renderer.

Upgrading does not automatically convert existing fields into the app-owned type.

## Rollout checklist

Preserve representative content and record project mappings before rollout.

1. Confirm the installed version and complete the applicable Jira app-update flow.
2. Compare a pre-existing issue's Description and each mapped custom field.
3. Check issue-type mappings and Gherkin settings.
4. Compare formulas, diagrams, tables, and attachment links with the source.
5. Edit a test record through the panel, save, reload, and verify the value.
6. Check the Jira search and export surfaces your team relies on separately.

Published status is not a blanket guarantee for every historical configuration. If content is missing or changes unexpectedly, stop editing the affected field and [contact support](../support/) with sanitized reproduction steps.

This is a Cloud Connect-to-Forge update guide, not a Data Center data migration guide.
