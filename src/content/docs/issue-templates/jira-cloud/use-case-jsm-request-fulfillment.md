---
title: "Use Case: JSM Request Fulfillment"
description: "Let an authenticated JSM request start the right internal Jira fulfillment work."
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

![Template details gives agents a visible record of the portal-triggered run](./assets/provenance-panel.png)

*Agents can inspect the template revision, run status, and created child work
after the customer submits the request.*

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
