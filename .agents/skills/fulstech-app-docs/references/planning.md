# Plan an App Documentation Set

Use before a whole-app rewrite or meaningful restructuring. This is a planning
aid, not a required public page or a reason to pause authorized writing.

## Inventory and coverage

Record the product/platform/release, sources checked, personas, mental model,
main outcomes, first-success workflow, and canonical terminology. Inventory the
existing pages within scope, including navigation, incoming links, screenshots,
legacy/version-specific content, and already useful material.

Use a compact mapping:

| Customer question/task | Current page | Action and destination | Evidence/gap | Priority |
|---|---|---|---|---|
| Relevant intent | Existing URL or missing | Keep, rewrite, split, merge, or propose archive | Verified source or NEEDS_VERIFICATION | P0/P1/P2 |

Prioritize blockers and false claims as P0, missing core-task/first-success
coverage as P1, and secondary depth or polish as P2. Explain priority by customer
impact rather than blindly preserving these labels.

Propose navigation and implementation order. Keep stable URLs where possible;
map moves to redirects and update callers. Do not delete historical content or
archive a product merely because it is old. Preserve supported platform/version
instructions and obtain any required scope decision before destructive cleanup.

## Select depth, not a fixed template

- Small utility: a compact overview, first-success path, usage, relevant settings,
  trust/limits, and troubleshooting/support. Related needs may share a page.
- Standard product: add concepts and task guides, feature reference where useful,
  administration, compatibility, and release information. Add migration/backup
  only for supported capabilities within scope.
- Complex product: split onboarding by genuine personas; organize workflows by
  the product's lifecycle. Add governance, integrations, detailed permissions,
  reference/API, or backup/restore only when the product warrants them.

Make user, administrator, and security/evaluation entry points easy to find when
applicable. Group by product and platform; do not send generic "Getting started"
links to an unrelated app. Reuse the site's existing components and styles.
Propose broader navigation/framework changes separately if outside the request.

End the plan with open verification questions and the pages they affect. Keep
planning notes in the owning repository, not in customer-facing navigation.
