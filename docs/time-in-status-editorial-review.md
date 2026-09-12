# Time in Status customer-documentation review

## Editorial decisions — 2026-09-12

Customer pages explain tasks and results. Internal rollout state, QA evidence,
SQL schemas and infrastructure costs stay outside the published content tree.

References consulted (structure only; no copied text or assets):

- [Timepiece scheduled reports](https://documentation.obss.tech/timepiece-time-in-status-for-jira/cloud/scheduled-reports-and-alarms): task-specific headings, settings next to relevant screenshots, outcome/retrieval instructions. Adopt task-to-result order; avoid reproducing its long sequence of images for our shorter flow.
- [SaaSJet product FAQ](https://help.saasjet.com/tis/time-in-status-general-product-faq): user questions lead to actionable instructions. Adopt question-oriented paths without turning the quickstart into an exhaustive FAQ.
- [Notion help](https://www.notion.com/help): category and task discovery before detailed reference. Adopt a small entry-point set rather than an undifferentiated feature list.

## Content budget

- Overview: navigation and a compact question-to-report mapping; no repeated report screenshot.
- Quickstart: four steps and one result screenshot.
- Analysis: one visible task tab at a time; zero or one relevant image per tab; calculation rules remain expandable.
- Sharing: separate Share, Schedule and Dashboard paths; one image for each visually ambiguous toolbar/form, none for the simple gadget search.
- Exports: distinguish current-scope CSV from all-issues background export; one image shows format, progress and download together.
- Calendar: one focused weekday/time image and one numerical business-time example.
- Administration/privacy/support: short instructions/reference; no decorative images.

Use existing Starlight tabs/steps and native details. Critical scope, permission,
expiry and completeness facts remain alongside the applicable task, not hidden
exclusively in reference sections. Screenshots link to full-size assets with
accessible names and captions. Do not add an image just to meet a count.

## Source and verification evidence

All newly captured images are from the development Jira app on 2026-09-12.
Only crop at capture time; do not replace labels, fabricate figures or imitate
competitor UI. The public captions identify examples. Old snapshots with test
fixture names were replaced with current controls and selected issue results.

Flows observed: create private saved report, share configuration, inspect weekly
schedule controls, stop sharing and delete the temporary saved report; group a
report and open a contributor; create a background XLSX, observe ready (95 issues,
4 pages) and prepare its download link; inspect supported history fields; inspect
calendar controls; run a three-issue report and inspect history.
No recurring schedule was created. No Jira issues were edited. The temporary
export expires through the normal retention flow. The production app was not
deployed. Download-byte integrity is outside this documentation check.

Manual documentation checks and final publish outcome are recorded below after
verification. A successful walkthrough by the author is not an independent
usability study with new customers.

## Verification

- Astro check: 13 files, no diagnostics. Production build and link audit passed;
  21,000 local references across 175 generated HTML files.
- Desktop: task tabs, keyboard tab selection, expandable calculation help and
  loaded schedule imagery checked in preview.
- Mobile: Analysis and Exports checked at 390px. Analysis tab padding reduced
  locally; all four labels fit (last right edge 330px), without page overflow.
- Full-size figure link opened the original 838×109 image in a new Chrome tab.
  The embedded browser did not open the popup, so Chrome verified this behavior.
- All task preview/QA tabs closed; existing user tabs preserved. Viewport reset.
- Publication uses the repository's main-branch GitHub Pages workflow. Deployment
  outcome is verified against the exact pushed commit before task completion.
