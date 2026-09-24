---
title: "Use Case: Incident Follow-up"
description: "Apply a repeatable post-incident Jira process to an existing incident without overwriting the incident information your team already entered."
---

The urgent incident response may be unique, but the follow-up work after an
incident is often predictable.

Instead of asking the incident owner to remember every post-incident task, apply
a reusable process to the Jira issue that already contains the incident facts.

## Situation

After an incident is stabilized, the team may consistently need to:

- document root-cause analysis;
- identify corrective actions;
- review monitoring or detection gaps;
- prepare a retrospective;
- track longer-term follow-up work.

The incident Summary, Description, severity, and timeline already exist and
should not be silently replaced.

## Example result

**Existing root**

`INC-123 — Checkout outage`

**Follow-up work**

- Complete root-cause analysis
- Review alerting gaps
- Define corrective actions
- Prepare incident retrospective

## Recommended approach

Use **Apply** on the existing incident issue.

1. Select the post-incident template.
2. Preview **Current** and **Proposed** values.
3. Keep the incident values that already contain the real event details.
4. Select the follow-up child work.
5. Apply the reviewed changes.

The default empty-only behavior helps preserve populated fields, while the
preview still gives the user an explicit decision for supported values.

## Why this works well

- The original incident remains the root work item.
- Existing customer/team-entered content can be preserved.
- The follow-up checklist is reusable across incidents.
- Only relevant follow-up child work needs to be selected.
- Partial hierarchy work can resume from the same run after a Jira-side problem
  is corrected.

## Variations

The same Apply pattern works when the root issue already exists and you want to
attach a standard process, for example:

- security-event follow-up;
- failed deployment review;
- customer escalation follow-up;
- quality escape or defect review;
- operational exception handling.

## Build it

Create the reusable follow-up definition with
[Templates and Supported Fields](../templates-and-fields/).

Then follow [Apply a template to an existing issue](../create-apply-recreate/#apply-a-template-to-an-existing-issue).
