---
title: "Get started"
description: "Install, configure a field, and save your first Markdown note."
---

## Before you begin

Ask a Jira administrator to install the Cloud app from [Marketplace](https://marketplace.atlassian.com/apps/1214558/markdown-rich-text-editor-for-jira-with-latex-mermaid-uml?showOnlyPublic=true) and activate a trial or subscription. Settings require permission to administer the project; saving content requires permission to edit the issue.

Use a test issue with an empty field. Do not replace an existing team's Description just to try the editor.

## 1. Configure one field

Open **Project settings → Apps → Markdown Fields**.

1. Under **Select fields to show as Markdown**, choose **Description** or an eligible multiline field.
2. Click **Add**.
3. Select issue types, such as Task.
4. Click **Save**.

This configures an existing field; it does not create one. For a dedicated field, see [Field configuration](../create-a-markdown-enabled-custom-field/).

## 2. Open the issue panel

Open an issue of a selected type. Find **Rich Text Custom Fields** in the issue's Apps or actions menu, depending on your Jira layout. The panel lists fields enabled for that issue.

## 3. Write and preview

Click **Click to add content** or the field's edit icon. Paste:

```markdown
## Release checklist

- [x] Requirements agreed
- [ ] Review implementation

| Owner | Responsibility |
| --- | --- |
| Product | Acceptance criteria |
| Engineering | Implementation |
```

Click **Preview**. Preview does not save. Click **Edit** to return, then **Save**.

## 4. Confirm persistence

Reload the issue and reopen the panel. Your content should still be present. Change task-list items in the Markdown source and save; do not rely on clicking a rendered checkbox to persist changes.

Next: [Using the editor](../using-the-editor/) or [Syntax examples](../markdown-syntax/).
