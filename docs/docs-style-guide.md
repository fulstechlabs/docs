# Fulstech Documentation Style Guide

Last reviewed: 2026-09-23

This is the repository-level source of truth for customer-facing documentation
on `docs.fulstech.com`. It consolidates the Fulstech App Documentation
Standard and the current patterns proven in Fulstech's strongest Cloud docs.

The north-star rule is:

> Organize documentation around what the customer is trying to accomplish, not around how the product is implemented.

This guide applies to new documentation and substantial rewrites. Existing
legacy products can be migrated separately; do not force unrelated cleanup into
a product release.

## 1. Source-of-truth order

Verify product claims in this order:

1. Current running product behavior.
2. Current production source and manifest/configuration.
3. Automated tests that define expected behavior.
4. Marketplace listing and deployed app identity.
5. Product requirements and release evidence.
6. Existing Fulstech documentation.
7. Support knowledge.
8. Inference only when unavoidable.

When sources disagree, resolve the conflict before publishing. Never invent
permissions, limits, data handling, migration behavior, UI labels, licensing, or
feature availability.

## 2. Write for customer outcomes

Start from a customer job such as:

- create a repeatable Jira process;
- configure a Confluence macro;
- expose a report;
- migrate a supported configuration;
- diagnose a missing field.

Do not mirror source folders, Forge modules, database tables, or internal class
names unless they are also part of the customer's mental model.

Prefer a small number of strong pages over many thin pages.

## 3. Default information architecture

A mature Cloud app should normally provide:

### Start here

- **Overview**
- **Getting Started**

### Use cases

For flexible products, scenario pages that help customers recognize problems
the product can solve even when they did not begin by searching for a specific
feature.

### Core tasks

Task-oriented pages for the product's recurring customer jobs.

### Administration and governance

Configuration, permissions, defaults, rollout behavior, backup/recovery, and
administrator-only operations.

### Security and privacy

Product-specific data handling and security facts. Keep legal/privacy URLs
stable when they are used by Marketplace.

### Help and updates

- **Frequently Asked Questions**
- **Known Limitations**
- **Troubleshooting and Support**
- **Release Notes**

Small products do not need every page type. Add a page only when it has one
clear user intent.

When one sidebar category grows beyond roughly ten peer pages, group pages by
intent instead of leaving a long flat list. Prefer groups such as **Start
here**, **Build**, **Use**, **Automation**, **Administration**, and **Help**.

## 3.1 Visual-first onboarding

Correct information is not enough if a new customer must read several screens
before knowing what to click.

For Overview and Getting Started pages:

- show the primary action within the first screen of content;
- prefer one short opening paragraph over several orientation paragraphs;
- show a 3–5 step quick-start path before detailed explanation;
- place the first useful screenshot near the first important decision or preview;
- use screenshots to confirm what success looks like, not as decoration;
- move edge cases, architecture, and detailed safety semantics to the relevant
  task, reference, limitation, or troubleshooting page;
- prefer compact tables for workflow choices instead of prose comparisons;
- use progressive disclosure: first help the reader succeed, then help them
  understand the deeper model.

A useful test is: a first-time customer should be able to answer **"What do I
click next?"** within a few seconds of opening the page.

## 4. Overview standard

An Overview should help a customer decide what to do next, not enumerate every
feature.

Recommended order:

1. One-sentence product outcome.
2. A visible **Start here** path or primary CTA.
3. One useful product screenshot when it helps the first decision.
4. **Choose the right workflow** table when the app has multiple entry points.
5. Two to four product promises or safety guarantees.
6. A prominent path to customer use cases when scenarios are a meaningful
   discovery channel.
7. Deeper navigation below the first-success path.

Avoid opening with implementation details, exhaustive field catalogs, or
internal architecture.

## 5. Getting Started standard

Getting Started is for **first useful success**.

Target a 5–10 minute result when practical. Keep the first-run path visually
scannable: a user should be able to follow the headings, numbered actions, and
screenshots without reading every explanatory paragraph.

Use this shape:

```text
# Getting Started

What the user will accomplish.

## Before you begin
Only prerequisites that can block the task.

## Step 1 — ...
## Step 2 — ...
## Step 3 — ...

## Verify the result
Describe exactly what success looks like.

## Next steps
2–5 likely follow-on tasks.
```

Do not turn Getting Started into a complete product manual.

## 6. Task guide standard

One task page should have one primary intent.

Preferred structure:

```text
# <Verb + object or customer goal>

One-sentence outcome.

## Before you begin
## Steps
## Verify the result
## Troubleshooting
## Related tasks
```

Rules:

- Use numbered steps for sequences.
- Use bullets for choices and facts.
- Put prerequisites before the action they block.
- Describe important side effects before the user triggers them.
- Use exact UI labels in **bold**.
- Do not rely on position-only instructions such as "click the button on the
  right".
- Keep troubleshooting close to the task when the failure is specific to that
  task.

## 6.1 Use-case-led discovery

Flexible products often have a discovery problem: a customer may need the
outcome but not know the product category or feature name to search for.

Use-case content should help the reader think:

> "That looks like my situation."

A use-case page is different from a task guide. It starts from the customer's
scenario and demonstrates how the product can fit that scenario, then links to
the canonical configuration/task guides.

Create use-case pages when:

- one product capability can solve several recognizable business processes;
- customers may search for the problem rather than the feature;
- examples can reveal value that is not obvious from the product name;
- the product is flexible enough that a feature catalog undersells its range.

Use customer/search language in page titles where practical, for example:

- Release readiness checklist
- Employee onboarding
- Incident follow-up
- Customer onboarding
- JSM request fulfillment

Recommended structure:

```text
# Use Case: <customer scenario>

One short statement of the recurring problem.

## Situation
What repeats and what changes each time.

## Example Jira/Confluence structure
A concrete example the reader can imagine.

## Recommended approach
Which product workflow fits and why.

## Why this works well
The customer outcomes, not a list of features.

## Variations
Adjacent situations that use the same pattern.

## Build it
Links to the canonical task/configuration guides.
```

Use cases should:

- be concrete enough to inspire adaptation;
- stay within verified product behavior;
- show realistic examples of names, fields, child work, or variables;
- explain tradeoffs when another workflow may fit better;
- link to implementation guides rather than duplicating all setup steps;
- avoid implying that the app provides domain-specific logic it does not have.

A Use Cases hub may also include short "more ideas" examples that do not yet
justify dedicated pages.

For flexible products, place use cases prominently near **Start here**, not only
inside advanced reference navigation. Use cases support discovery; users should
be able to find them before they understand the product's internal vocabulary.

## 7. Choosing between task, concept, reference, FAQ, and troubleshooting

Use a **task guide** when the reader intentionally wants to accomplish
something.

Use a **concept page** only when misunderstanding a concept causes mistakes.

Use a **reference page** for dense lookup information such as supported field
families, syntax, or compatibility.

Use **FAQ** for genuinely frequent questions that can be answered briefly.
Do not use FAQ as a dumping ground for multi-step procedures.

Use **troubleshooting** for observable symptoms. Prefer titles such as
"Template does not appear" over internal root-cause titles such as "Context
resolution problem".

## 8. Troubleshooting standard

For feature-specific problems, place the most likely checks in the feature's
task page. Keep a central Troubleshooting page as an index and support handoff.

A full troubleshooting entry should answer:

- What the user sees.
- Likely causes.
- How to check deterministically.
- How to resolve it.
- What evidence to collect if the issue continues.

Avoid generic advice such as reinstalling or clearing data unless impact and
data preservation are explicitly understood.

## 9. Administration standard

For meaningful settings, explain:

- who can change them;
- where they are configured;
- their scope;
- default behavior;
- effect on existing data;
- effect on future data;
- permission dependencies;
- reversibility;
- rollout considerations;
- limitations.

Clearly distinguish Atlassian permissions from Fulstech app governance.

## 10. Security and data standard

Security and privacy claims must come from the actual app's manifest, source,
storage model, remotes/egress configuration, and verified policies.

Do not copy another Fulstech app's technical declarations simply because the
products look similar.

State clearly when data stays in Atlassian/Forge, when data leaves Atlassian,
what the app stores, and what a backup/export contains.

## 11. Known Limitations standard

Known Limitations should contain intentional product or platform boundaries,
not unresolved bugs disguised as documentation.

Explain the practical effect and the recommended supported path.

Do not advertise a large negative feature list. Document only boundaries that
help customers make or troubleshoot a real decision.

## 12. FAQ standard

A good FAQ answer is short and points to the canonical guide.

Create an FAQ item when:

- customers naturally ask the question;
- the answer is stable;
- the answer is brief;
- a full page would be excessive.

Promote the question to a task/troubleshooting guide when the answer requires
multiple steps or significant prerequisites.

## 13. Release Notes standard

Release Notes are customer-facing change awareness, not a commit log.

For meaningful releases use:

- **New**
- **Improved**
- **Fixed and hardened**

Describe outcomes and changed behavior. Omit refactors that do not affect a
customer or support boundary.

Call out Beta/Preview status and important behavior changes when they affect
rollout decisions.

## 14. Writing style

Use calm, concise, professional English.

- Address the reader as **you** when giving procedures.
- Prefer active voice.
- Keep paragraphs short and focused.
- Use sentence-case headings.
- Use exact current UI labels in **bold**.
- Use `code formatting` for values, keys, syntax, filenames, and tokens.
- Explain Jira/Confluence-specific jargon when a normal administrator may not
  know it.
- Prefer concrete examples over abstract descriptions.
- Avoid hype, competitor comparisons, and unsupported superiority claims.

## 15. Screenshots

Use screenshots when they reduce ambiguity, not as decoration.

Prefer screenshots for:

- a complex editor state;
- a preview/result the user must recognize;
- a configuration surface where labels are difficult to locate;
- a relationship that is easier to see than describe.

Avoid screenshots for a single obvious button or rapidly changing incidental
UI.

Every screenshot should show current product behavior, use safe test data, and
remain readable at the docs layout width.

## 16. Navigation and links

Navigation should reflect customer intent.

- Keep **Overview** and **Getting Started** first.
- Keep legal/security pages stable and discoverable.
- Put **FAQ**, **Known Limitations**, **Troubleshooting**, and **Release Notes**
  together under Help/Updates when the product is large enough.
- Link to one canonical explanation rather than duplicating full sections.
- End task pages with 2–4 strongly relevant related tasks.

## 17. Supportability

A Support section must be more useful than a service-desk link.

Ask for only diagnostics that reduce time to resolution, such as:

- site URL or safe site identifier;
- affected page/issue key;
- feature/action;
- template/report/macro name when relevant;
- run ID or exact error;
- expected and actual behavior;
- minimal reproduction;
- redacted screenshot.

Never ask customers to post passwords, API tokens, cookies, secrets, or
unrelated customer data.

## 18. Quality gate

Before publishing, verify:

### Intent
- The page has one primary user intent.
- The title matches language customers are likely to recognize or search.
- The opening explains why the page matters.

### Accuracy
- UI labels match the current product.
- Permissions and scope are verified.
- Limitations are verified.
- Security/data claims come from the actual app.

### Usability
- Blocking prerequisites appear first.
- Procedures are sequential and testable.
- The expected result is explicit.
- Important side effects are stated before action.
- The likely next step is easy to find.

### Readability
- Paragraphs are short.
- Jargon is necessary and explained.
- Examples are realistic.
- Repeated content links to a canonical source instead of drifting.

### Supportability
- Common symptoms are covered locally or linked.
- Support escalation requests useful diagnostics.
- Sensitive-data warnings exist where needed.

### Maintenance
- Screenshots are necessary and current.
- Beta/Preview/edition applicability is explicit.
- Release-sensitive claims are reviewed during release reconciliation.
- Obsolete pages are redirected or removed deliberately.

## 19. Definition of done

Documentation is ready when a reasonable customer can independently answer:

1. What problem does the app solve?
2. Can I recognize my own situation in one or more documented use cases?
3. Which workflow should I choose?
4. What do I need before I start?
5. How do I reach the first useful result?
6. How do I complete the main recurring tasks?
7. What can an administrator configure?
8. What permissions and data boundaries matter?
9. What limitations affect my rollout?
10. How do I diagnose common failures?
11. What information should I provide to Fulstech Support?
12. What changed in the latest meaningful release?

If a basic product question requires a support ticket, the documentation is
incomplete.

## 20. AI/Codex workflow

When using AI or Codex for docs work:

1. Verify product behavior and source-of-truth evidence.
2. Identify personas, outcomes, and the product mental model.
3. Propose or confirm the information architecture.
4. Map existing pages to keep, rewrite, split, merge, archive, or create.
5. Flag high-risk claims: permissions, security, migration, compatibility,
   limits, pricing, and licensing.
6. Write pages using the page patterns above.
7. Run the repository docs checks and link audit.
8. Review navigation and public URLs after deployment.

Do not mechanically rewrite every legacy page during unrelated product work.
Apply this standard to the product in scope and migrate older products through
their own planned tasks.

## Reference implementations

Use current Fulstech docs as implementation references, not copy sources:

- **Issue Templates & Hierarchy Builder for Jira** demonstrates workflow
  selection, task-oriented automation guides, FAQ, limitations, release notes,
  and recovery-oriented support.
- **Better Pages for Confluence** demonstrates outcome-first Overview,
  first-success Getting Started, nested information architecture, and
  symptom-first troubleshooting.

The standard should remain consistent across Fulstech while allowing each app's
information architecture to match its real customer jobs.
