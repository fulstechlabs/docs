---
title: "Use Case: Customer Onboarding and Implementation"
description: "Create a repeatable Jira delivery plan for each new customer while changing the customer, owner, target date, and rollout details."
---

Customer onboarding often contains the same delivery stages even when the
customer, owner, configuration, and timeline are different.

A reusable hierarchy gives the delivery team a standard starting point without
turning every customer implementation into a cloned Jira project.

## Situation

A services, SaaS, or implementation team may repeat work such as:

- kickoff and requirements confirmation;
- environment or configuration setup;
- data or integration validation;
- training and handoff;
- go-live verification.

The customer name, target date, delivery owner, and rollout scope change each
time.

## Example Jira structure

**Root**

`Customer rollout — {{customer}}`

**Child work**

- Confirm onboarding requirements
- Configure customer environment
- Validate integration or data
- Prepare user handoff
- Verify go-live

Useful variables might include:

- `customer`
- `targetDate`
- `deliveryOwner`
- `environment`

## Recommended approach

Use **Create** to start a new customer rollout from a governed template.

When a live customer rollout already contains a useful one-off structure that
you do not want to govern as a reusable template, use **Recreate** to reproduce
selected live work once.

## Why this works well

- Delivery teams start from the same process without creating a whole Jira
  project template.
- Variables make the same template useful across customers.
- The user can preview and remove work that does not apply to a smaller rollout.
- Cross-project creation can be validated before Jira is changed when the
  destination supports the required work types and hierarchy.
- Provenance makes it easier to see which template revision started a rollout.

## Variations

The same pattern can support:

- professional-services engagements;
- partner enablement;
- new-site rollout;
- migration preparation;
- customer environment provisioning;
- recurring managed-service onboarding.

## Build it

See [Create, Apply, and Recreate](../create-apply-recreate/) to choose between a
governed template and a one-time Recreate flow.

Then use [Templates and Supported Fields](../templates-and-fields/) to model the
delivery hierarchy.
