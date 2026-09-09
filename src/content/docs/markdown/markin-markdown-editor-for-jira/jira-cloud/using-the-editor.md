---
title: "Use the editor"
description: "Read, edit, preview, and save Markdown in Jira."
---

Open **Rich Text Custom Fields** on an issue. Each enabled field has its own content area. Click a field or its edit icon to edit; an empty field displays **Click to add content**.

## Preview, save, and cancel

- **Preview:** display your draft without saving.
- **Edit:** return from preview to source.
- **Save:** write the field to Jira and return to the rendered view.
- **Cancel:** discard the draft and restore the previously loaded value.

Save each field separately. Reloading or leaving before saving can lose a draft. Avoid simultaneous edits to the same field: this release has no collaborative draft-merging workflow.

## Suggestions

- **Ctrl + Space:** syntax suggestions.
- **@:** Jira user suggestions.
- **@@:** attachments already on the issue.

Suggestions insert source. They are not an upload tool, and a user reference does not guarantee a Jira mention notification.

## Images and task lists

Markdown images and supported attachment references become links. External images are not loaded automatically. Jira attachment permissions still apply when opening a link.

Change task-list markers from `[ ]` to `[x]` in source and save. Rendered checkboxes are not a separate persisted checklist feature.

## Other Jira surfaces

| Surface | Expected result |
| --- | --- |
| App panel and Preview | Rich Markdown, supported math and diagrams |
| Native app-owned field display | Text representation, not a rich editor |
| Jira Description editor | May show source in a code block |
| Search, lists, notifications, exports | Jira's field representation, not the full app renderer |

There is no app-owned PDF/Word export workflow. Jira exports are separate from the panel view.

## Access and failed saves

Reading requires Jira issue access; saving requires edit permission. Settings require project-administration permission. A valid app trial or subscription is required.

If saving fails, copy the draft before reloading. See [Troubleshooting](../support/).
