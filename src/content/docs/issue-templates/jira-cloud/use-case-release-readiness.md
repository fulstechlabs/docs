---
title: "Use Case: Release Readiness Checklist"
description: "Reuse the same Jira release checklist while changing the version, date, owner, and environment."
---

**Use this when:** every release needs nearly the same preparation work.

## Example you can build

```text
Release {{version}} readiness
├─ Validate release candidate
├─ Prepare release notes
├─ Confirm deployment readiness
└─ Verify production
```

For this expanded template, change each run:

`version` · `releaseDate` · `releaseOwner` · `environment`

## Best fit

**Create from a template**

The installed **Release readiness** starter is smaller than the example above:
it asks only for `version` and creates **Complete QA**, **Prepare release notes**,
and **Confirm rollout plan** as subtasks. You can edit it to add dates, owners,
environments, or more work.

![The installed Release readiness starter asks for one version value](./assets/customer-use-cases/getting-started-release-runtime.png)

![The starter preview shows the resolved root values and three selected subtasks](./assets/customer-use-cases/getting-started-release-preview.png)

*The screenshots show the installed starter, not the expanded four-child
example above. Nothing is created at the preview step.*

### What this gives the team

- One governed release process instead of copied checklists.
- New version/date/owner values for each run.
- Recoverable child creation if Jira completes only part of the hierarchy.

For an expanded template, the release owner enters its configured values,
previews the hierarchy, removes any unneeded child work, then creates it.

![A completed run of the installed starter created the root and three children](./assets/customer-use-cases/getting-started-release-result.png)

## Also works for

Hotfixes · mobile releases · infrastructure rollouts · customer deployments ·
quarterly upgrades.

[Build the template →](../templates-and-fields/)  
[Add variables →](../variables-and-smart-values/)  
[Run with Create →](../create-apply-recreate/#create-new-work-from-a-template)
