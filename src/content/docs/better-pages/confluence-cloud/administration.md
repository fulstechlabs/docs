---
title: "Administration"
description: "Configure Better Pages external content, local forms, diagnostics, and usage reporting."
---

Open **Confluence administration → Apps → Better Pages administration**. The same installation-scoped settings are available from **Manage apps → Better Pages → Configure**.

Only a Confluence application administrator can use this page. Every settings mutation is also authorized by the Forge backend; displaying the page alone is not treated as authorization.

## External frame policy

Choose the behavior for an HTTPS frame URL that does not match an approved rule:

- **Sandboxed**: renders with an empty iframe sandbox, which disables scripts and forms.
- **Denied**: prevents rendering.

Add an exact HTTPS URL, use `*` for one path segment, or use `/**` for the remainder of a path. Host wildcards and embedded credentials are rejected.

New origins require an Atlassian-owned customer-managed egress consent dialog. Review that dialog before approval. Rejecting consent leaves the Better Pages policy unchanged. The configurable egress group supports at most ten unique origins; several frame path rules may share one origin.

## External image policy

Add an exact HTTPS origin such as `https://images.example.com`. Image and frame permissions are independent even when they use the same origin.

Observed frame and image URLs appear in separate inventories. Staging an observed URL does not immediately grant access: review the staged policy, select **Review and save changes**, then review Atlassian's consent dialog.

## Local forms

Local forms are disabled for the installation by default. Select **Enabled** and save the local-form setting to expose configured fields on published form macros. Disabling the feature again replaces every form with an administrator-disabled message.

Better Pages forms validate only in the reader's browser. The app does not receive or store entered values.

## Concurrent changes

Settings are revisioned. If another administrator saves first, a stale browser tab cannot overwrite the newer value. Reload, review the current policy, and try again. External-policy changes also use a short lease while Atlassian egress consent or revocation is in progress.

## Macro Usage Audit Report

Select **Start scan** to find Confluence pages that contain the eight current Better Pages macro module keys. Results are grouped by page and include navigation back to the content. **Download report** exports page title, page link, and macro families as CSV.

The report scans Better Pages macros only. It does not inspect comments or data owned by another app.

## Stored diagnostic data

Administrators can separately:

- Clear observed frame and image URL inventories.
- Reset aggregate extended-capability view counters.

Each action requires confirmation. These controls do not delete macro configuration, Confluence pages, approved URL rules, or local-form configuration.
