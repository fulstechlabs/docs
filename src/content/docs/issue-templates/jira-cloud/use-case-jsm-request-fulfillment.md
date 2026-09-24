---
title: "Use Case: JSM Request Fulfillment"
description: "Let authenticated JSM customers choose a governed request template and automatically create the standard follow-up work after submission."
---

A Jira Service Management request form can collect the customer's need, while a
template can define the repeatable Jira work that happens after the request is
created.

This is useful when different request variants need different follow-up work but
the customer should not have to understand the internal Jira process.

## Situation

A service team receives recurring requests such as:

- environment or access setup;
- onboarding or provisioning;
- operational change requests;
- standard service fulfillment;
- internal enablement requests.

The customer's Summary and Description should remain exactly what they entered,
while the internal follow-up work should be consistent.

## Example flow

**Customer request**

`Provision test environment for Project Atlas`

The customer chooses a matching template on the request form.

**Follow-up Jira work**

- Validate request details
- Prepare environment
- Perform configuration
- Verify fulfillment

Required template variables use configured defaults because a portal run cannot
pause after submission to ask another template question.

## Recommended approach

Use [JSM Customer Portal Templates](../jsm-customer-portal/).

Configure an availability rule for the exact:

- service project;
- JSM request type;
- root Jira work type.

Then add the app's **Issue template** field to that request form.

## What the customer experiences

The portal selector shows:

- **No template**; and
- only matching templates for the exact request context.

A portal-only authenticated customer does not need a Jira/JSM product license
to use the supported selector. Anonymous submission is not supported.

## What happens after submission

- Customer-entered populated root values are preserved.
- Supported empty root values can be filled from the template.
- Required variable defaults are resolved automatically.
- The hierarchy is queued after the request exists.
- Template comments and attachments are not copied automatically.
- **Template details** records the run for agents/support.

## Why this works well

The customer interacts with a simple request form while the service team gets a
repeatable internal Jira process.

The template library also stays governed independently from the JSM request
form, so the same reusable process can still be used in other supported Jira
contexts where its availability rules allow it.

## Build it

Start with the full
[JSM Customer Portal Templates](../jsm-customer-portal/) configuration guide.

If the process should instead start from a Jira workflow transition, see
[Workflow Create](../workflow-create/).
