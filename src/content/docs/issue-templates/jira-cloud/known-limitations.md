---
title: "Known Limitations"
description: "Understand verified Jira contexts and intentional product boundaries before rollout."
---

These boundaries describe the current supported product. They prevent the app
from guessing Jira or third-party payloads that cannot be validated safely.

## Field boundaries

- Rank is not authored or copied as a generic field.
- Jira Assets/Object fields are not supported by the generic adapter.
- Opaque fields owned by another Marketplace app, including proprietary
  checklist formats, require a separately verified integration.
- A supported field that is not available in the destination project and issue
  type is warned and skipped.
- Jira subtasks inherit Sprint from their parent because Jira rejects direct
  Sprint writes to a subtask.

## Native Create boundaries

- Group picker and Sprint are not exposed by Forge UI Modifications and remain
  blank in native Create.
- Only one UI Modifications app can operate in a context.
- Native prefill is verified for exact company-managed Jira Software project
  and issue-type rules. Use explicit Create for the guaranteed path.

## Jira product contexts

- The release has end-to-end tenant evidence on a company-managed Jira
  Software project.
- Team-managed projects have not completed separate tenant certification.
- Jira Service Management customer-portal templates are not a launch claim.
- Workflow-driven creation is Beta while the relevant Forge module remains
  Preview.

## Data movement

- JSON backup/restore protects same-tenant app configuration.
- It does not migrate another vendor's Data Center data.
- It does not automatically remap projects, issue types, fields, options,
  users, or attachments between Jira sites.

