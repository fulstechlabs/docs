---
title: "Use Case: Release Readiness Checklist"
description: "Reuse the same Jira release checklist while changing the version, date, owner, and environment."
---

**Use this when:** every release needs nearly the same preparation work.

## Example

```text
Release {{version}} readiness
├─ Validate release candidate
├─ Prepare release notes
├─ Confirm deployment readiness
└─ Verify production
```

Change each run:

`version` · `releaseDate` · `releaseOwner` · `environment`

## Best fit

**Create from a template**

![Preview selected Release readiness child work before creating Jira issues](./assets/release-preview.png)

*This view shows the selected child work before Jira is changed. The same
Preview also contains the root values above this section.*

### What this gives the team

- One governed release process instead of copied checklists.
- New version/date/owner values for each run.
- Recoverable child creation if Jira completes only part of the hierarchy.

The release owner enters the new values, previews the hierarchy, removes any
unneeded child work, then creates it.

![A verified Release readiness run created the root issue and selected subtasks](./assets/release-created.png)

## Also works for

Hotfixes · mobile releases · infrastructure rollouts · customer deployments ·
quarterly upgrades.

[Build the template →](../templates-and-fields/)  
[Add variables →](../variables-and-smart-values/)  
[Run with Create →](../create-apply-recreate/#create-new-work-from-a-template)
