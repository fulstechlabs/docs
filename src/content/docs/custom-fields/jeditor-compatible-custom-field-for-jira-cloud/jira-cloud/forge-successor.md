---
title: "Use the Forge successor"
description: "Configure and evaluate JEditor Release 1.1 without confusing it with the legacy Connect app."
---

Use **JEditor Fields** to view and edit rich issue content and reuse templates.
This guide describes **JEditor Release 1.1 on Forge** for an explicitly enabled
evaluation. It is not an installation announcement: the successor is **not yet
approved or available on Marketplace**.

## Before you begin

- Confirm with your administrator that the Forge successor is installed in the
  evaluation site. A Forge deployment alone does not install it in your Jira site.
- You need project-administration permission to configure fields and templates.
  Users need the applicable Jira browse/edit permissions to read/save issue content.
- Use a disposable issue and non-sensitive content for evaluation. Do not
  uninstall the existing app or replace customer fields to follow this guide.

## Configure a field and reach a first result

1. Open the project's **Project settings → JEditor Fields**.
2. Select a supported field, such as **Description** or an existing multiline
   text field, and select the issue types where it should appear.
3. Select **Save**. Open an issue of one of those types and open **JEditor Fields**.
4. Select **Edit** beneath the configured field. Enter a short heading and a
   two-row table, then select **Save**.
5. Reload the issue and check the rich result in **JEditor Fields**. Confirm
   your other field values are unchanged.

Configuration is per project and issue type. If the field does not appear,
check the mapping, the issue type, field availability, and your Jira permissions.
Use the JEditor panel to preserve rich content; the ordinary Jira editor is not
the same rich-editing surface.

## Choose the field path

| Field path | Rich editing | Other Jira surfaces |
| --- | --- | --- |
| Description or supported multiline text field | JEditor Fields panel | Underlying Jira field; rich formatting is not guaranteed in every surface |
| App-owned **JEditor Rich Text** field | JEditor Fields panel | Read-only native field with a text/Markdown representation; not a second rich editor |

A Jira administrator manages field contexts and screens for an app-owned field.
Do not convert an existing imported text field into a different field type as
an assumed migration step. Validate search, API, export, and notification
behavior for your chosen field rather than assuming rich-editor parity there.

## Reuse project templates

In **Project settings → JEditor Fields**, manage templates for the relevant
field and select **Save templates**. Templates contain reusable rich content
and belong to that project/field, not a global secret store. Open the configured
issue panel to use them; verify the saved template after reloading settings.

## Recognize a pending native-field save

**Saved; sync pending** or **Saved; sync required** means the native value and
its compatibility mirror have not yet fully converged. The app keeps accepted
content in a recovery journal and retries completion on a later load; daily
maintenance also retries stale records. This is not a promise of deletion after
24 hours. Avoid uninstalling the app or clearing fields to resolve this message.
If it persists, contact [support](../support/) with sanitized diagnostics.

## Plan a Connect-to-Forge upgrade

The successor preserves the existing app identity and Connect-compatible
project mappings/templates. Bounded test-site migration has been verified,
but that is not a guarantee for every customer configuration or a public
upgrade instruction. Wait for the approved Marketplace version and its rollout
guidance before changing a customer installation.

For a planned pilot, record representative field values and templates before
the upgrade, then compare configured issue types, rich rendering, edit/save/reload,
and relevant Jira text/search/API results afterward. Keep Server/Data Center
imports separate from this Cloud app upgrade; see [Migrate to Jira Cloud](../migrate-to-jira-cloud/).

## Important limits

CKEditor 4.22.1 is end-of-life and not claimed vendor-supported or
vulnerability-free. Editor assets and external HTTPS images make browser
requests outside Atlassian. Read [Security and data](../security-and-data/)
before evaluating sensitive-content use.
