---
title: "Use Case: Incident Follow-up"
description: "Apply a standard post-incident Jira process without overwriting the incident information already entered."
---

**Use this when:** the incident already exists, but follow-up work repeats.

## Example

```text
INC-123 — Checkout outage
├─ Complete root-cause analysis
├─ Review alerting gaps
├─ Define corrective actions
└─ Prepare incident retrospective
```

## Best fit

**Apply to the existing incident**

![Compare the current incident with the proposed template values before applying](./assets/apply-preview.png)

*Apply shows Current vs Proposed so the incident details can stay untouched while
the follow-up work is added.*

### What this gives the team

- The existing incident remains the source of truth.
- Standard follow-up work is added only after review.
- Partial child creation can resume from the same run.

Preview **Current** vs **Proposed**, keep the real incident details, and add only
the follow-up work you need.

## Also works for

Security events · failed deployments · customer escalations · defect reviews ·
operational exceptions.

[Build the follow-up template →](../templates-and-fields/)  
[Use Apply →](../create-apply-recreate/#apply-a-template-to-an-existing-issue)
