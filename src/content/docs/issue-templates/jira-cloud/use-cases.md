---
title: "Explore Use Cases"
description: "See practical ways teams use reusable Jira issue templates and hierarchies for releases, onboarding, incidents, service requests, and recurring delivery."
---

Issue Templates & Hierarchy Builder is useful anywhere a team repeatedly creates
the same **kind of Jira work** but the people, dates, customer, version, or scope
change each time.

You do not need to start by choosing a feature. Start with a recurring process
your team already recognizes.

## Which situation looks familiar?

| Your recurring work | A useful starting pattern |
| --- | --- |
| Every release needs the same readiness work | [Release readiness checklist](../use-case-release-readiness/) |
| Every new employee needs the same coordinated setup | [Employee onboarding](../use-case-employee-onboarding/) |
| Every customer rollout follows a repeatable delivery plan | [Customer onboarding and implementation](../use-case-customer-onboarding/) |
| Every incident needs structured follow-up after the urgent response | [Incident follow-up](../use-case-incident-follow-up/) |
| A JSM request should create standard fulfillment work | [JSM request fulfillment](../use-case-jsm-request-fulfillment/) |

These are examples, not fixed template types. The app stores normal Jira work,
so you can adapt the same model to your own process.

## The pattern behind all of them

A reusable process usually has three parts:

1. **What stays the same** — the standard fields, child work, hierarchy, and
   optional links.
2. **What changes each time** — a customer, employee, release version, date,
   owner, environment, or other run-specific input.
3. **How the process starts** — a user creates it explicitly, applies it to
   existing work, a JSM customer selects it, or a workflow transition triggers
   it.

The app lets you capture those three parts without turning the process into a
large Jira Automation rule.

## More ideas to adapt

Once you recognize the pattern, the same approach can fit many other recurring
jobs:

- change rollout and deployment checklists;
- recurring access or configuration reviews;
- vendor or partner onboarding;
- campaign or launch coordination;
- monthly operational checklists;
- environment provisioning follow-up;
- QA or regression work packages;
- audit-readiness task sets;
- support escalation follow-up;
- office, store, or site opening checklists.

A good candidate is any process where someone says:

> "We create almost the same Jira issues every time, but a few values and
> people are different."

## Start from your own process

If you already have a good Jira issue and child structure, you can
[Capture it into a template](../templates-and-fields/#capture-an-existing-issue).

If you are designing a new process, start with
[Templates and Supported Fields](../templates-and-fields/).

If you are not sure which execution path fits the use case, see
[Create, Apply, and Recreate](../create-apply-recreate/).
