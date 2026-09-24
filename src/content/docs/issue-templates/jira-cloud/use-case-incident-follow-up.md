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

![A read-only second Apply preview shows Keep decisions and one selected follow-up subtask](./assets/customer-use-cases/incident-kept-fields-child.png)

*This is a second, read-only preview after an earlier Apply run. The root fields
show **Keep** and one follow-up child is selected; **Apply changes** was not
selected a second time. The four-item outline above is a possible expanded
incident process, not the photographed fixture.*

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
