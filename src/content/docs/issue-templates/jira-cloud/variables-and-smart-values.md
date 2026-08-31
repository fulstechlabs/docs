---
title: "Variables and Smart Values"
description: "Collect typed values for each run and resolve safe Jira, user, and date context."
---

Variables keep a reusable process stable while allowing names, owners, dates,
and choices to change for each run.

## Variable types

Template authors can define:

- Text input.
- A choice from an authored list.
- A Jira user.
- A date.

A variable can have a default and can be required. Required values are checked
before the preview and before any Jira mutation.

## Insert a variable

Use the variable token shown by the editor, such as `{{version}}`, in a
compatible root or child value.

Example:

```text
Prepare release notes for {{version}}
```

At run time, the app collects the answer with a typed control and shows the
resolved result in the preview.

![Typed teammate and date inputs](./assets/variables.png)

## Bounded smart values

The app supports a deterministic set of values rather than arbitrary scripts:

- Current user identity and display name.
- Current date and time.
- Relative dates such as today plus seven days or one month.
- Current issue, source issue, root issue, parent issue, project, and issue-type
  context where that value exists.

Date resolution uses one recorded run time so a root and its children do not
receive different dates because processing crossed midnight.

## Validation behavior

- A missing required answer blocks preview and mutation.
- An invalid date or choice produces an inline message.
- User values are selected through Jira controls; users do not type account
  IDs.
- A token with no available context resolves predictably instead of running
  arbitrary code.

