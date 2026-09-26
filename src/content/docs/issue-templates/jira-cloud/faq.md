---
title: "Frequently Asked Questions"
description: "Quick answers about Create, Apply, Recreate, JSM portal templates, Workflow Create, recovery, licensing, and product boundaries."
---

## Which workflow should I use: Create, Apply, or Recreate?

Use **Create** to start new governed work from a saved template. Use **Apply** to
standardize an existing issue or add selected follow-up work. Use **Recreate**
when you want to copy useful live Jira work once without saving it as a governed
template.

See [Create, Apply, and Recreate](../create-apply-recreate/) for the complete
decision guide.

## Is Native Jira Create Prefill the same as Create from a template?

No. Native Create Prefill is an optional convenience inside Jira's standard
Create dialog for one exact project and issue type. It cannot collect run-time
template inputs the way the app's explicit Create flow can.

Use [explicit Create](../create-apply-recreate/) when users need variables,
fresh Smart Values, hierarchy selection, or a full preview.

## Can a JSM portal-only customer use a template without a Jira or JSM product license?

Yes. Authenticated portal customers without a Jira/JSM product license are
supported when the administrator configures the exact service project and JSM
request type.

Anonymous portal submission is not supported.

## Does a portal template overwrite what the customer typed?

Populated customer root fields are preserved. The automatic JSM path fills
supported empty root values only.

Template comments and attachments are not copied automatically.

## Can a JSM portal template ask the customer for template variables?

Not after the request is submitted. Every required variable must have a usable
default before the template can be offered on the portal.

See [JSM Customer Portal Templates](../jsm-customer-portal/).

## Is Workflow Create production-ready?

Workflow Create is available but remains **Beta** because Atlassian's Forge
workflow post-function module is still Preview.

Use the explicit Create and Apply journeys when you need an interactive,
preview-before-write workflow.

## Will Workflow Create run twice if Forge delivers the same transition more than once?

Duplicate delivery of the same transition execution reuses one deterministic
run. A separate legitimate transition later is a new execution and can start a
new run.

See [Workflow Create](../workflow-create/) for the repeat-transition behavior.

## Can Retry create duplicate child issues?

A retry resumes the same durable run and skips nodes that already completed.
Use **Template details** to retry a Partial or Failed run after correcting the
underlying Jira problem.

Do not start a second Create or Apply solely to replay unfinished children.

## Can I use the same template across different Jira projects?

Explicit Create, Apply, and Recreate can work across projects when the
destination contains compatible work types, fields, and hierarchy levels. The
app validates the selected destination before mutation.

JSM portal availability is intentionally stricter and requires an exact service
project, request type, and root work type.

## Do I need to configure the starter's subtask work type?

Usually no. If the target project has one compatible subtask work type, the app
resolves it for the built-in starters. If Jira offers several, choose the
intended child **Work type** in **Structure** when Preview asks. See
[Getting Started](../getting-started/) for the first-run flow.

## Does the app support Jira Assets, Rank, or opaque third-party fields?

Not through the generic field adapter. Rank, Assets/Object fields, and opaque
Marketplace-app-owned field formats remain outside the documented generic
support boundary.

See [Known Limitations](../known-limitations/).

## Does backup and restore migrate templates to another Jira site?

No. Backup and restore is designed for same-tenant app configuration safety. It
does not automatically remap projects, work types, fields, users, options, or
attachments between Jira sites.

See [Backup and Restore](../backup-and-restore/).

## What happens when the Marketplace evaluation or subscription ends?

Existing templates and app configuration remain readable. Mutating operations
such as Create, Apply, Edit, Archive, Recreate, and Restore require an active
evaluation or subscription.

Ending the subscription does not silently delete app configuration.

## Where should I start when something does not work?

Start with [Troubleshooting and Support](../troubleshooting-and-support/). For a
partial hierarchy, open **Template details** first because it shows the run ID,
node outcomes, and latest actionable error.

If you contact Fulstech Support, include the affected Jira issue key, app action,
template name, run ID when available, expected result, actual result, and a
redacted screenshot.
