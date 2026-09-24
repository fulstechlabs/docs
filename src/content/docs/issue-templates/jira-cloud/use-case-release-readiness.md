---
title: "Use Case: Release Readiness Checklist"
description: "Turn a repeatable software release checklist into one reusable Jira template with variables, child work, preview, and recovery."
---

A release may be different every time, but the readiness work is often almost
identical.

Instead of copying an old release issue and cleaning it up manually, create one
governed template and supply only the values that change.

## Situation

A team releases regularly and wants every release to cover the same preparation:

- QA sign-off;
- documentation and release notes;
- deployment preparation;
- stakeholder or operational handoff;
- post-release verification.

The release version, owner, target date, and environment change each time.

## Example Jira structure

**Root**

`Release {{version}} readiness`

**Child work**

- Validate release candidate
- Prepare release notes
- Confirm deployment readiness
- Verify production after release

Useful variables might include:

- `version`
- `releaseDate`
- `releaseOwner`

You can also use bounded Smart Values for relative dates or Jira context where
the documented token is available.

## Recommended approach

Use **Create** from a saved template.

1. Define the root fields and readiness child work once.
2. Add variables for the values that change per release.
3. Select **Use template** for each new release.
4. Enter the version/date/owner.
5. Preview the complete hierarchy.
6. Create only the child work needed for that release.

The preview lets the release owner remove an irrelevant step without changing
the reusable template.

## Why this works well

- The checklist is governed once instead of copied from memory.
- Run-specific values stay outside the template definition.
- Child work is visible before creation.
- **Template details** records which template revision created the work.
- A partial hierarchy can retry without recreating completed children.

## Variations

The same pattern can represent:

- hotfix readiness;
- mobile app releases;
- infrastructure rollout;
- customer-specific deployments;
- quarterly platform upgrades.

The process does not need to be "software release" specifically. It only needs a
repeatable root + follow-up work structure.

## Build it

Start with [Templates and Supported Fields](../templates-and-fields/) and
[Variables and Smart Values](../variables-and-smart-values/).

For the execution flow, see
[Create new work from a template](../create-apply-recreate/#create-new-work-from-a-template).
