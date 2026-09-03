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
- Native prefill snapshots literal values and variable defaults when the rule
  is saved. It does not collect run variables or recalculate Smart Values each
  time Jira's Create dialog opens.

## Variables and Smart Values

- Smart Values use the app's documented bounded token set. Jira Automation
  expressions, functions, and arbitrary scripts are not supported.
- Unknown, misspelled, or unavailable context tokens resolve to an empty
  string. Confirm every resolved value in Preview.
- A new root issue has no `issue.key`, `root.key`, or `parent.key` before Jira
  creates it. `parent.key` is available only while child work is executed.
- `currentUser.displayName` is currently safe only for explicit Create root
  values and root comments. Use a required text variable when a readable name
  must remain identical across Apply and child work.
- Smart dates use the run's recorded UTC timestamp. Review results near UTC
  day, month, or year boundaries.

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
