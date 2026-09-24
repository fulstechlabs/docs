---
title: "Use Case: Employee Onboarding"
description: "Coordinate repeatable employee onboarding tasks in Jira while changing the employee, start date, manager, and team for each run."
---

Onboarding usually crosses several people or teams, but the checklist is mostly
the same for every new employee.

A reusable Jira hierarchy can turn that checklist into a visible, repeatable
process without recreating the tasks manually.

## Situation

For every new teammate, the organization may need work such as:

- prepare equipment;
- request or confirm system access;
- prepare first-week material;
- assign an onboarding buddy;
- complete team-specific setup.

The employee, manager, team, location, and start date change each time.

## Example Jira structure

**Root**

`Onboard {{employeeName}} — {{team}}`

**Child work**

- Prepare laptop and equipment
- Configure required access
- Prepare first-week plan
- Schedule onboarding handoff

Useful variables might include:

- `employeeName`
- `startDate`
- `manager`
- `team`

## Recommended approach

Use **Create** when HR, IT, or an operations owner starts the onboarding
process explicitly.

The user enters the employee-specific values, previews the work, and creates the
selected hierarchy.

If onboarding begins from a Jira Service Management request, the same idea can
also use [JSM Customer Portal Templates](../jsm-customer-portal/) when the
request type and template are configured for that exact context.

## Why this works well

- One template expresses the standard onboarding process.
- Variables keep personal/run-specific values out of the reusable definition.
- Optional child work can be deselected for contractors or team-specific cases.
- The Jira hierarchy makes ownership visible across teams.
- The result remains normal Jira work after creation.

## Variations

The same model can support:

- contractor onboarding;
- role changes;
- employee offboarding;
- access-review follow-up;
- partner or vendor onboarding.

Use separate templates when the underlying process is meaningfully different
instead of creating one template with excessive conditional complexity.

## Build it

Start with [Templates and Supported Fields](../templates-and-fields/) and
[Variables and Smart Values](../variables-and-smart-values/).

If users will start the process from JSM, continue with
[JSM Customer Portal Templates](../jsm-customer-portal/).
