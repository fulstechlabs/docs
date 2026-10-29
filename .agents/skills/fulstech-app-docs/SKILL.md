---
name: fulstech-app-docs
description: Write or improve customer-facing documentation for a Fulstech app, grounded in verified product behavior and customer tasks. Use for product overviews, onboarding, guides, administration, trust, and troubleshooting docs; not internal engineering reports, Marketplace copy, or docs-site redesign.
---

# Fulstech App Docs

Produce documentation that lets customers understand the app, reach a first
useful result, complete daily tasks, resolve problems, and evaluate adoption.
Organize around customer problem → outcome → workflow → feature, not code or
the settings menu. Consistency means shared thinking and writing standards,
not identical page counts or headings across products.

## Scope and product understanding

1. Identify the app, audience, platform, documented release, owning product
   repository, and docs source using
   [workspace discovery](../../../../../../../../../.agents/skills/workspace-skill-discovery/SKILL.md).
   For Fulstech,
   use the canonical docs.fulstech.com source; do not revive GitBook links.
2. Establish the user's requested output: plan, sample pages, a bounded update,
   or a complete app documentation set. Do not turn a single-page edit into a
   portfolio audit or redesign the site framework. Follow requested review
   checkpoints; a draft request does not authorize publication.
3. Identify actual personas, their main questions, the app's mental model,
   core workflows, and a visible definition of first success. Explain where
   the app appears in Jira/Confluence and what it changes. Do not assume the
   reader knows the plugin just because they know Jira or Confluence.
4. Before a whole-app rewrite or restructuring, read
   [planning.md](references/planning.md) and prepare a concise inventory and
   coverage plan. For a small edit, do this only for the affected workflow.

## Ground claims in the documented release

- Prefer observed behavior of the target release, deployed code/configuration,
  relevant tests, manifest/Marketplace metadata, then requirements/release notes,
  existing docs and support knowledge. Treat inference as a question, not a fact.
  Evidence must match its claim: manifest permissions do not prove actual data
  retention; a successful happy path does not prove universal compatibility.
- Reconcile contradictory evidence rather than blindly choosing the first source.
  A running bug is not automatically intended behavior. Keep QA/unreleased
  capabilities separate from customer docs for a published release.
- Record uncertain claims internally as NEEDS_VERIFICATION with the source or
  check needed. Never publish that placeholder or invent missing capabilities,
  defaults, permissions, limits, security facts, or an unsupported workaround.
  Continue verified sections and report the affected gaps to the user.
- Competitor docs may inspire organization, not establish our app's features,
  security, pricing, or compatibility. Prior research is a lead, not current proof.
- Docs work does not authorize changing app behavior to make a guide true,
  accepting agreements, or altering legal declarations. Flag such gaps separately.

## Author for the customer's task

Read [page-patterns.md](references/page-patterns.md) for the page types being
written. Apply only useful sections; remove irrelevant headings.

- One page has one primary customer intent. Separate independently searchable
  tasks and concepts, but keep a short necessary explanation beside a procedure.
  Do not fragment every field or CRUD action into a tiny page.
- Put prerequisites and role requirements before steps. Give the exact entry
  point, actions, meaningful example input, expected result, and useful next task.
  Getting Started ends with a result the reader can use and interpret, not merely
  installation or opening the app. Do not promise a completion time without basis.
- Use clear English by default for Fulstech customer docs, matching the existing
  site's language unless requested otherwise. Address the reader as "you", use
  active voice and short paragraphs, and use exact visible UI labels.
- Keep canonical product/feature terminology consistent. Follow the documented
  UI/version rather than hardcoding a supposedly universal Jira vocabulary.
- Prefer task/search wording such as "Limit a template to selected projects"
  over "Context configuration". Explain jargon once; avoid keyword stuffing,
  promotional filler, and unsupported superlatives.
- Explain concepts and limits once in a canonical location and link from guides.
  Include decision-critical limits where they affect a task, not only in an FAQ.
- Use screenshots where location, choice, or visual results are hard to explain.
  Inspect existing local screenshots and illustrations visually before reusing
  them: check the documented platform/release, workflow state, legibility,
  framing, and relevance to the reader's task. File presence alone is not enough.
  If local assets are missing, outdated, unclear, or show the wrong step/result,
  proactively capture fresh screenshots from the actual app in an authorized
  environment as part of the docs work. Do not limit the guide to available
  local images or ask the user to supply images when safe capture is available.
  Prefer an appropriate test environment and coherent sample data. Do not deploy,
  change production data, or broaden access merely to obtain a screenshot.
  If capture is blocked, report the exact missing visual and access prerequisite;
  continue useful text rather than substituting misleading imagery.
  Capture the actual applicable UI with safe sample data, crop to useful context,
  and add descriptive alt text and captions. Text must remain usable without the
  image. Never present mockups or competitor screenshots as our app's behavior.
  Label conceptual diagrams as illustrations, not screenshots. Store selected
  documentation assets in the owning docs repository using its conventions;
  keep disposable captures outside the tracked docs and record enough provenance
  to identify the source environment, release, and depicted workflow state.
  For browser work, follow
  [browser cleanup](../../../../../../../../../.agents/skills/browser-task-cleanup/SKILL.md).
- Make platform/version applicability discoverable. Record Last reviewed only
  after an actual content check, using existing metadata conventions; a build
  timestamp does not demonstrate content freshness.

## Verify and deliver

Read [quality-gates.md](references/quality-gates.md) before handing off edited
docs. Report precisely what was written, verified, not verified, and published
or only committed. Follow the owning repo's delivery rules and
[repository delivery](../../../../../../../../../.agents/skills/repository-change-delivery/SKILL.md).

For a complete app set, a new customer should be able to answer: What does it do?
Does it fit my need? How do I start? What permissions do I need? How do I complete
the main tasks? What explains unexpected results? How is data handled? What are
the limits? Where can I get help? Judge coverage and time to first useful result,
not page count; do not invent usage or support-deflection metrics.
