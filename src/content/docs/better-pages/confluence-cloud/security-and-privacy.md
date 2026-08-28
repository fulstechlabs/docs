---
title: "Security and Privacy"
description: "Understand Better Pages permissions, stored data, AI boundaries, external content, and sandboxing."
---

Better Pages runs on Atlassian Forge and uses Confluence Cloud APIs. Confluence
continues to enforce the signed-in account's page, space, content, template,
attachment, label, restriction, and administration permissions.

For the customer-facing data notice, read the
[Better Pages Privacy Policy](../privacy-policy/).

## Why the app requests permissions

Better Pages reads accessible content, spaces, users, groups, attachments,
labels, restrictions, templates, and permission information to render macros,
search for destinations, build inventories, and preflight changes. Write scopes
support templates, Smart Designer, Space Manager, attachments, labels,
restrictions, Numbered Headings, archive, and move-to-trash operations.

The app does not use those scopes to reveal content a user cannot access. Tools
that change Confluence show a preview or plan and run as the current account.

## Data stored by Better Pages

Depending on the features used, Forge storage or Forge object storage contains:

- Installation feature controls, revision metadata, external policies, and
  observed external URL inventories.
- Global colors and Brand Kit definitions with verified image and icon assets.
- Local-space colors where authors create them.
- Account-scoped welcome dismissal and alert dismissal state.
- Page-level Numbered Headings settings and operation state.
- Bounded aggregate capability view counters when Usage insights is enabled.

Normal macro configuration is stored with the Confluence page. Template and
Space Manager output is ordinary Confluence content. Uploaded macro imagery can
also be stored as a page attachment or verified Forge-hosted asset, according
to the source the author chooses.

Aggregate usage counters do not contain page IDs, users, queries, or authored
content. Better Pages has no external analytics SDK or support chat widget.

## Marketplace subscription

Better Pages is a paid Marketplace product. An active subscription or
evaluation enables normal features. When Atlassian reports an inactive license,
authoring and app tools show a subscription-required state, backend resolver
operations are rejected, and the Numbered Headings update trigger is skipped.
The App does not delete Confluence content or Forge-hosted data when a trial or
subscription ends.

## AI and external services

AI is off by default. When an administrator enables it and an author explicitly
generates content, Better Pages uses an Atlassian-hosted Forge LLM:

- Interactive Banner sends the submitted goal and prompt. Linked content can
  also send a bounded title and readable excerpt from an accessible Confluence
  page. External web pages are not fetched.
- Smart Designer sends only the selected text and chosen tone.

Licensed stock search uses Wikimedia Commons and its media host. Selected stock
assets retain source, creator, and license attribution.

Compatibility frames and external images load only after both the Better Pages
policy and Atlassian customer-managed egress allow the resource. The external
service may apply its own privacy and logging policy.

## HTML isolation

HTML is sanitised and CSS is scoped to an isolated frame. Optional JavaScript is
off by default. When enabled, it runs only in an opaque-origin nested sandbox
that blocks network requests, form submission, downloads, pop-ups, and host
navigation. Turning JavaScript off again preserves HTML and CSS but stops saved
scripts from running.

## Reader-entered data

Retained local form compatibility performs required-field validation in the
reader's browser. It has no submit destination, and values are not sent to the
Forge backend or stored by Better Pages.
