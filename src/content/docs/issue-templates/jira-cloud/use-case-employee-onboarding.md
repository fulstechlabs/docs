---
title: "Use Case: Employee Onboarding"
description: "Reuse one Jira onboarding process while changing the employee, start date, manager, and team."
---

**Use this when:** every new teammate needs the same coordinated setup.

## Example

```text
Onboard {{employeeName}} — {{team}}
├─ Prepare laptop and equipment
├─ Configure required access
├─ Prepare first-week plan
└─ Schedule onboarding handoff
```

Change each run:

`employeeName` · `startDate` · `manager` · `team`

## Best fit

**Create from a template**

The template author defines those values as runtime inputs, then reuses them in
the root and child fields. A scenario-specific onboarding screenshot will be
used only when the captured UI shows the actual onboarding variables rather than
an unrelated example.

### What this gives the team

- The same setup flow for every new teammate.
- Different employee, team, manager, and start date each run.
- Optional JSM entry when onboarding begins from a service request.

Use **JSM portal templates** instead when onboarding begins from a service
request.

## Also works for

Contractor onboarding · role changes · offboarding · partner onboarding · access
setup.

[Build the template →](../templates-and-fields/)  
[Add variables →](../variables-and-smart-values/)  
[Start from JSM →](../jsm-customer-portal/)
