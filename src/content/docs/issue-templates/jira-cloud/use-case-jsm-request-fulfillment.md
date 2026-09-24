---
title: "Use Case: JSM Request Fulfillment"
description: "Let an authenticated JSM customer choose a template that starts the right internal Jira fulfillment work."
---

**Use this when:** customers submit a simple request, but agents need repeatable
internal follow-up work.

## Example

```text
Customer request:
Provision test environment for Project Atlas

Internal follow-up:
├─ Validate request details
├─ Prepare environment
├─ Perform configuration
└─ Verify fulfillment
```

## Best fit

**JSM Customer Portal Templates**

![A controlled JSM portal verification showing No template plus the matching request-type template](./assets/jsm-template-selection.jpg)

*The screenshot shows the selector behavior on the customer portal. Production
4.0.0 separately verified the matching-template path with an authenticated
portal-only customer. Anonymous portal access is not supported.*

![Agents can see the completed template run and created child work on the Jira request](./assets/jsm-run-result.jpg)

*This controlled verification fixture shows the matching template completed and created one child work item.*

### What this gives the team

- A simple customer-facing request experience.
- Consistent internal follow-up work behind the request.
- A supportable run record for agents without exposing internal template data to
  the customer.

The customer sees **No template** plus matching choices for the exact request
type. Their populated Summary and Description stay unchanged.

## Good for

Provisioning · access/setup requests · onboarding requests · standard operational
changes · internal service fulfillment.

[Configure the JSM flow →](../jsm-customer-portal/)  
[Build the reusable template →](../templates-and-fields/)
