---
title: "Troubleshooting and Support"
description: "Resolve common template, field, hierarchy, permission, native Create, and licensing issues."
---

## The app says a subscription is required

Ask a Jira administrator to start or renew the Marketplace evaluation or
subscription. An inactive license keeps existing configuration readable but
blocks create, apply, edit, archive, restore, and other mutations.

## A template does not appear

Check the template status and its project, issue-type, group, and account
availability rules. All configured parts of a rule must match the current user
and Jira context. Ask an administrator to confirm the destination project and
issue type still exist.

If the template was archived, a Jira administrator can restore it from
**Administration → Data management → Archived templates**.

## A template does not appear on a JSM request form

Confirm that the request form contains the **Issue template** field. Then edit
the template and check that one enabled availability rule contains the exact
service project and JSM request type. The request type must use the same Jira
work type as the template root. Required template variables also need defaults.

Portal selectors fail closed. A rule for another request type, a disabled rule,
or a project/work-type mismatch intentionally exposes no template.

## A JSM request was created but no hierarchy appeared

Open the request in Jira and check **Template details**. **No template** is a
valid selection and intentionally creates no app run. For a selected template,
record the request key and run ID, then check whether the run is Pending,
Partial, Failed, or Completed. Correct the reported Jira configuration or
permission problem before retrying unfinished work.

The automatic portal path fills empty supported root fields only. A populated
customer Summary or Description is preserved.

## A field is missing from the editor

Select the project and issue type, then load Jira fields again. Jira returns
only fields available and writable in that context. See
[Templates and supported fields](../templates-and-fields/) and
[Known limitations](../known-limitations/).

## A field is skipped during Create or Apply

Read the preview or result warning. The field may have left the destination
context, an option may no longer exist, or Jira may reject the value for the
current user. Correct the template or destination configuration and retry.

## A variable or Smart Value is blank

Open Preview and check the exact token spelling. The app supports its bounded
token catalog, not Jira Automation expressions. An unknown token or a token
whose context does not yet exist resolves to an empty string.

For example, a new root does not have `{{issue.key}}` before creation and a
child does not have `{{parent.key}}` until its parent has been created. Avoid
custom variable names that duplicate built-in names such as `today` or
`project.key`. See [Variables and Smart Values](../variables-and-smart-values/)
for the token and workflow reference.

## Preview and the final Smart Value do not agree

Do not confirm another run until the template is corrected. Record the
template name and revision, flow, source/root issue key, token, previewed value,
and final value. `currentUser.displayName` should not currently be used in
Apply or child values; collect a readable name as a text variable instead.

## A hierarchy is partial

Open **Template details** on the root issue and review each node outcome. Fix
the reported Jira permission, issue-type, field, or link problem, then retry
the same run. Do not start a new run just to replay completed children.

## Preview says the hierarchy is incompatible

Open the affected work item and review its **Work type** and **Parent**. Jira
allows only a compatible direct parent level; a subtask cannot be standalone.
If the operation targets another project, confirm that project has matching work
types at compatible hierarchy levels. Correct the template or destination, then
run Preview again. The app does not create or update Jira issues while this
preflight error is present.

## An issue link cannot be created

The selected link type may have been renamed, deleted, or made unavailable.
Edit the work item, choose one of Jira's current link types and confirm the
displayed direction. Retry the same partial run so completed issue creation is
not repeated.

## Native Create did not prefill

Confirm that an administrator enabled a rule for the exact project and issue
type. The app fills empty fields only. Group and Sprint are not available to
this app through this integration.

If other UI Modifications apps are configured for the same project, issue type,
and view, check for conflicts on the same field. Jira currently runs up to five
such apps in one context asynchronously; when more than five are configured,
some app changes are ignored.

## A workflow transition did not run the template

Check all three configuration points:

1. The transitioned issue's project and work type have an active app default.
2. The default template has the intended **Workflow integration (Beta)** mode.
3. The Jira transition contains the app's **Create issue template structure**
   post-function and the workflow change was published.

A missing or unavailable default produces no mutation. Invalid hierarchy,
missing variable defaults, or insufficient Jira context fail before child work
is queued. A completed transition run appears in **Template details** with
origin **Workflow**.

## Backup validation fails

Confirm that the document is a complete version 2 app backup. Review every
invalid project, work type, field, hierarchy reference, and default before
restoring. Do not edit stable Jira IDs by guessing. Availability references
that Jira can no longer resolve remain fail-closed after restore.

## Contact support

Submit bugs and feature requests through the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Include:

- Jira site URL and affected issue key.
- App action and template name.
- Run ID when available.
- Expected and actual result.
- Reproduction steps and a screenshot with sensitive information removed.

Never include passwords, tokens, full backup documents, or confidential issue
content unless support specifically confirms a secure need and channel.
