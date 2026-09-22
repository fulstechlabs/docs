---
title: "Workflow Create"
description: "Run an app default after a Jira workflow transition with explicit, recoverable behavior."
---

Workflow Create is an automatic channel for Jira administrators. A Jira
transition decides when the app runs, the active app default chooses the
template, and the template's **Workflow integration (Beta)** setting chooses
the result.

Workflow Create is Beta because Atlassian's Forge workflow post-function module
remains Preview. The explicit [Create and Apply](../create-apply-recreate/)
journeys remain the dependable paths for interactive work.

## Prepare the app default

1. Open the template and select **Details → Edit template**.
2. In **Review & settings**, select **Edit settings**.
3. Enable **Use as the app default for this project and issue type**.
4. Under **Workflow integration (Beta)**, choose the transition behavior.
5. Confirm every required variable has a usable default.
6. Save the template.

The default must match the transitioned issue's project and work type. Missing,
archived, disabled, or unavailable defaults produce no Jira mutation.

## Choose a mode

| Mode in the template editor | Result after the transition |
| --- | --- |
| **Create complete configured hierarchy** | Keeps the transitioned issue as the root and creates the complete validated hierarchy, including configured descendants and links. |
| **Fill empty values on transitioned issue** | Fills supported blank root fields only and creates no child work. Populated values are preserved. |
| **Create direct Jira children only** | Creates only work whose Jira parent is the transitioned issue. Descendants, standalone work, and additional issue links are omitted. |
| **Create hierarchy under transitioned Epic-level issue** | Creates the complete validated hierarchy only when the transitioned issue is an Epic-level work type. |
| **Perform no workflow action** | Leaves the issue and shared template unchanged. Use this to keep a post-function installed without running template work. |

All automatic modes exclude template comments and attachments.

## Add the Jira post-function

1. Open Jira workflow administration and edit the workflow used by the target
   project and work type.
2. Select the transition that should start the app.
3. Add the **Create issue template structure** post-function.
4. Publish the workflow change according to your Jira workflow process.

The post-function needs no separate app form. Its description points to the
app default and the template's workflow setting.

## Understand repeat and failure behavior

One Jira transition execution maps to one deterministic app run. Retried or
duplicate event delivery reuses that run. A later legitimate matching
transition is a new execution and starts another run; hierarchy modes can
therefore create the configured work again.

Before queueing child work, the app validates the Jira context, default,
required variable defaults, and hierarchy compatibility. Missing transition
identity or invalid configuration fails closed. Partial hierarchy recovery
reuses the run and skips completed nodes.

Open **Template details** on the transitioned issue. A workflow run shows origin
**Workflow**, its status, created child work, and any actionable recovery
message.

## Roll out safely

Use a test workflow and project first. Verify no-default behavior, the chosen
mode, the resulting Template details record, and a second legitimate transition
before adding the post-function to a shared production workflow.
