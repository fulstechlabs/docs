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

![Fields and inputs can reuse a run-specific value inside Jira fields](./assets/customer-fields-inputs.jpg)

*This verified delivery example shows the same input mechanism. An onboarding
template can use it for values such as employee name, team, manager, and start date.*

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
