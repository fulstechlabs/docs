---
title: "Native Jira Create Prefill"
description: "Optionally prefill supported empty fields in Jira's standard Create dialog for an exact project and issue type."
---

Native Create prefill is an optional convenience for teams that want selected
template values in Jira's standard **Create** dialog. It is not required for
the app's explicit Create and Apply workflows.

## How a rule works

An administrator enables prefill for one exact combination of:

- Jira project.
- Issue type.
- Global Issue Create context.

The app then fills supported fields only when both project and issue type
match. Changing context causes app-owned values to be reevaluated.

![URL and cascading select prefilled in Jira Create](./assets/native-create-prefill.png)

## User-value protection

The rule follows two safety principles:

1. Fill an empty field only.
2. Clear a value on context change only while that value is still owned by the
   app.

If a user edits the prefilled value, the app treats it as user-owned and does
not remove it during a later context change.

## Supported fields in native Create

Forge UI Modifications exposes a smaller field set than the app's explicit
workflows. The verified native path supports common system fields plus the
app's URL and cascading-select handling where Jira exposes them.

Group picker and Sprint are not exposed to this Forge integration. They remain
available in explicit Create and Apply.

## Platform boundary

Only one UI Modifications app can operate in a given context. Atlassian may
also change which fields a Jira Create surface exposes. Keep explicit Create
as the dependable cross-context path and verify a new rule in its exact project
and issue type before announcing it to users.

