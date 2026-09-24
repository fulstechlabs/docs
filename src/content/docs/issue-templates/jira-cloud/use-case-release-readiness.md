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

The release owner enters the new values, previews the hierarchy, removes any
unneeded child work, then creates it.

## Also works for

Hotfixes · mobile releases · infrastructure rollouts · customer deployments ·
quarterly upgrades.

[Build the template →](../templates-and-fields/)  
[Add variables →](../variables-and-smart-values/)  
[Run with Create →](../create-apply-recreate/#create-new-work-from-a-template)
