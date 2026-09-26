# Issue Templates customer screenshot provenance — 2026-09-24

Internal review record for the public Issue Templates pages. The images below
show the **production Forge installation of version 4.0.0 (Marketplace build
3002050) on the dev2 test site**. They are real Jira/portal interactions with
test fixtures, not mockups or a customer production tenant.

The first five images were captured for
[product issue #22](https://github.com/fulstechlabs/issue-templates-for-jira-forge/issues/22).
The remaining selected images come from
[product PR #21](https://github.com/fulstechlabs/issue-templates-for-jira-forge/pull/21),
commit `d528c1767400b77e5e8ede32ede9ce74389681aa`. Public images are faithful
crops or copies of those sources. The screenshot capture and selection did not
alter app code, production deployment, Marketplace listing, or pricing.

| Public docs asset under `assets/customer-use-cases/` | Fixture and version | Exact claim shown | Caveat |
| --- | --- | --- | --- |
| `getting-started-release-runtime.png` | Source-defined Release readiness starter, revision 2, production 4.0.0, ITHBE2E | Create new asks for required `version=v2.5` and offers Preview new issue. | The three child work types/parents were mapped to this Jira project's actual **Sub-task** type for this 4.0.0 capture; the image does not prove newer automatic resolution. |
| `getting-started-release-preview.png` | Same starter and run | Proposed root values resolve `v2.5`; all three named subtasks are selected; Create issue is available. | This is a preview before mutation. |
| `getting-started-release-result.png` | ITHBE2E-1084 with 1085–1087 | Create run reached Completed and lists three created child keys. | The result dialog shows keys, while the Jira screenshot shows their summaries. |
| `getting-started-release-jira.png` | ITHBE2E-1084 with 1085–1087 | Jira root has the resolved description and three actual subtasks. | Left-side crop excludes unrelated account/field details. |
| `getting-started-release-details.png` | ITHBE2E-1084 / Release readiness revision 2 | Template details shows Created origin, Completed status, and all three child outcomes. | Panel crop omits the issue title; pair with the Jira screenshot. |
| `employee-variables.png` | Employee onboarding fixture, production 4.0.0 | Fields & inputs defines `employeeName`, `team`, and `startDate`. | Does not show `manager` or child hierarchy from the expanded example. |
| `employee-runtime-inputs.png` | Same employee fixture | Create new asks for the three inputs before preview. | That fixture creates only a root issue. The photographed date is browser-localized. |
| `customer-structure.png` | Customer rollout fixture | Structure shows root, three children, and selected child Work type, Parent, and Relationship controls. | Saved but not run; it does not show the five-child illustrative example or customer variable. |
| `incident-kept-fields-child.png` | ITHBE2E-1082 / Incident follow-up | A second Apply preview shows Description Keep with matching Current/Proposed values and one selected child. | This is a **second preview after an earlier completed Apply**. No second Apply was submitted; it is not evidence of a second completed child. |
| `jsm-portal-selection.png` | Authenticated portal-only customer, JSME2E matching request type | Production Issue template selector offers No template and a friendly matching template, without an internal template ID. | Focused selector crop; the dev2 site also has an unrelated development installation. |
| `jsm-agent-run-result.png` | JSME2E-135 / Service request checklist | Agent view shows Portal origin, Completed, and one created child JSME2E-136. | It is an agent-side result, not a customer-facing portal result. |

## Capture-era starter behavior and next-release reconciliation

The installed Release readiness starter was recreated from the source-defined
template: one `version` input, the source Summary/Description, and the three
source child summaries. A previous disposable fixture had the same name, so it
was renamed **Release planning example** before installing the true starter.

In production 4.0.0, an unedited starter failed Create preview in ITHBE2E:
its children specified work type name `Subtask`, while Jira exposes
`Sub-task`. The app reported “Jira hierarchy metadata is unavailable for
Subtask” and disabled Create. For the screenshots above, each child's Work
type was changed to **Sub-task** and Parent to **Root issue** in the editable
starter before a successful Completed run. These images prove the pictured
input, preview, result, and Jira issue; they do **not** prove automatic
work-type selection.

The upcoming consolidated product candidate on `main` resolves
[product issues #23](https://github.com/fulstechlabs/issue-templates-for-jira-forge/issues/23)
and [#25](https://github.com/fulstechlabs/issue-templates-for-jira-forge/issues/25)
through merged [PR #24](https://github.com/fulstechlabs/issue-templates-for-jira-forge/pull/24).
When a project has exactly one compatible Jira subtask work type, installation
binds the starter children to its canonical ID/name; live preflight also
resolves older generic starters. When several compatible types exist without a
valid explicit choice, Preview fails closed and asks the user to choose the
intended type in **Structure**. A valid stored type ID remains authoritative.
The customer guidance in this PR describes that candidate behavior, while the
screenshots retain their production-4.0.0 provenance. This docs PR remains
unmerged until the consolidated app release and docs publication are sequenced.

## Deliberate exclusions

- PR #21 images 01–04 show a different disposable Release readiness fixture;
  they are not used as proof of the installed starter.
- PR #21 portal submission image 10 exposes the test customer's display name.
  No public crop from that image can show the complete submitted request and
  safely omit the name, so no submitted-request screenshot is published.
- PR #21 image 09b contains the dev2 dual-install context; image 12 names an
  internal workflow smoke fixture. Both remain internal evidence. The Workflow
  Create public guide stays textual until a clean customer-facing fixture exists.
- The existing `docs/issue-templates-content-verification-2026-09-24.md` is a
  historical record of the earlier screenshot set. This record supersedes its
  screenshot-placement decisions for the pages changed in issue #22.

## Review gate

For each changed public page, compare the rendered image with its immediately
adjacent text and caption. Verify fixture, variable set, child count, flow,
preview versus completed state, app version, privacy, and visible labels. A
successful build or valid image path alone does not establish that alignment.
