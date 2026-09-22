---
title: "Release Notes"
description: "Customer-visible changes in Issue Templates & Hierarchy Builder for Jira Cloud."
---

## 4.0.0 — 22 September 2026

### New

- **JSM customer portal templates.** Administrators can offer templates for an
  exact service project and request type to authenticated portal customers.
  The selector supports **No template**, preserves customer input, resolves
  configured defaults, and records recoverable hierarchy execution.
- **Workflow Create (Beta).** A Jira workflow post-function can run the active
  app default in one of five explicit modes. Deterministic runs prevent
  duplicate provider delivery from creating duplicate work.

### Improved

- Hierarchy authoring now keeps Jira parent structure separate from optional
  issue links and validates compatible levels before mutation.
- Create, Apply, Recreate, and Capture support deeper selected hierarchy with
  safer cross-project work-type mapping.
- Current and Proposed comparisons, issue search, run status, and same-run
  recovery are clearer across the app.
- Empty Jira collection values are normalized consistently during authoring,
  preview, capture, and Jira writes.

### Fixed and hardened

- Authenticated JSM portal-only customers can load the template selector; the
  app still excludes anonymous portal access.
- Concurrent first-use SQL initialization elects one schema leader and safely
  recovers after an interrupted lease.
- Portal lifecycle processing rejects stale and out-of-order selections, while
  retries reuse completed root and child checkpoints.
- Automatic portal and workflow paths fill empty root values only and never
  copy comments or attachments silently.

Workflow Create remains Beta while Atlassian's Forge workflow post-function
module is Preview. See [Known limitations](../known-limitations/) for current
platform boundaries.
