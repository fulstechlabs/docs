---
title: "Troubleshooting and Support"
description: "Resolve common template, field, hierarchy, permission, native Create, and licensing issues."
---

## The app says a subscription is required

Ask a Jira administrator to start or renew the Marketplace evaluation or
subscription. An inactive license keeps existing configuration readable but
blocks create, apply, edit, archive, restore, and other mutations.

## A template does not appear

Check the template status and its project, issue-type, group, and account
availability rules. All configured parts of a rule must match the current user
and Jira context. Ask an administrator to confirm the destination project and
issue type still exist.

## A field is missing from the editor

Select the project and issue type, then load Jira fields again. Jira returns
only fields available and writable in that context. See
[Templates and supported fields](../templates-and-fields/) and
[Known limitations](../known-limitations/).

## A field is skipped during Create or Apply

Read the preview or result warning. The field may have left the destination
context, an option may no longer exist, or Jira may reject the value for the
current user. Correct the template or destination configuration and retry.

## A hierarchy is partial

Open **Template details** on the root issue and review each node outcome. Fix
the reported Jira permission, issue-type, field, or link problem, then retry
the same run. Do not start a new run just to replay completed children.

## Native Create did not prefill

Confirm that an administrator enabled a rule for the exact project and issue
type. The app fills empty fields only. Group and Sprint are not available in
this integration. Another UI Modifications app in the same context can also
prevent the rule from running.

## Backup validation fails

Confirm that the document is a complete version 2 app backup. Review every
invalid project, issue type, field, option, user, group, and default before
restoring. Do not edit stable Jira IDs by guessing.

## Contact support

Submit bugs and feature requests through the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Include:

- Jira site URL and affected issue key.
- App action and template name.
- Run ID when available.
- Expected and actual result.
- Reproduction steps and a screenshot with sensitive information removed.

Never include passwords, tokens, full backup documents, or confidential issue
content unless support specifically confirms a secure need and channel.

