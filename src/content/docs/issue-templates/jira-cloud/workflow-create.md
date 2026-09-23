---
title: "Workflow Create"
description: "Run an app default after a Jira workflow transition with explicit, recoverable behavior."
---

Workflow Create is an automatic channel for Jira administrators. A Jira
transition decides when the app runs, the active app default chooses the
template, and the template's **Workflow integration (Beta)** setting chooses the
result.

Workflow Create is Beta because Atlassian's Forge workflow post-function module
remains Preview. The explicit [Create and Apply](../create-apply-recreate/)
journeys remain the dependable paths for interactive work.

## Before you begin

Use a test workflow and project first. You need:

- A matching active app default for the transitioned issue's project and work
  type.
- A template with the intended **Workflow integration (Beta)** mode.
- Defaults for every required template variable.
- Permission to edit and publish the target Jira workflow.

## Prepare the app default

1. Open the template and select **Details → Edit template**.
2. In **Review & settings**, select **Edit settings**.
3. Enable **Use as the app default for this project and issue type**.
4. Under **Workflow integration (Beta)**, choose the transition behavior.
5. Confirm every required variable has a usable default.
6. Save the template.

Missing, archived, disabled, or unavailable defaults produce no Jira mutation.

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

The post-function needs no separate app form. Its description points to the app
default and the template's workflow setting.

## Verify the result

Run the configured transition on a test issue, then open **Template details**.

Confirm:

- Origin is **Workflow**.
- The expected mode was applied.
- Created child work matches the configured hierarchy.
- The run reaches **Completed**, or an actionable Partial/Failed result is shown.

One Jira transition execution maps to one deterministic app run. Retried or
duplicate event delivery reuses that run. A later legitimate matching transition
is a new execution and starts another run.

## Failure and recovery behavior

Before queueing child work, the app validates the Jira context, default,
required variable defaults, and hierarchy compatibility. Missing transition
identity or invalid configuration fails closed. Partial hierarchy recovery
reuses the same run and skips completed nodes.

## Troubleshooting

### The transition succeeds but the app does nothing

Check all three configuration points:

1. The transitioned issue's project and work type have an active app default.
2. The default template has a Workflow integration mode other than
   **Perform no workflow action**.
3. The transition contains **Create issue template structure** and the workflow
   change is published.

### The workflow run is Partial or Failed

Open **Template details** and fix the reported Jira permission, hierarchy,
field, or link problem. Retry the same recoverable run instead of triggering a
new transition solely to replay completed work.

### A later transition creates another hierarchy

That is expected for a new legitimate transition execution. Duplicate delivery
of the same transition reuses its deterministic run, but a separate later
transition is a new run.

For more symptoms, see
[Troubleshooting and Support](../troubleshooting-and-support/).

## Related tasks

- [Configure app defaults](../administration/).
- [Build the template hierarchy](../templates-and-fields/).
- [Use explicit Create or Apply](../create-apply-recreate/).
- [Review Workflow Create boundaries](../known-limitations/).
