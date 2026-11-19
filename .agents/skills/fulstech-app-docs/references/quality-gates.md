# Documentation Quality Gates

Apply to changed content and affected links, scaled to the request. A prose
review alone is not proof that a workflow works.

## Content and evidence

- Each page has a clear customer intent, audience, and discoverable applicability.
- Claims, UI names, defaults, permissions, examples, and limits match the target
  release. Security statements have direct evidence rather than inference.
- Steps include prerequisites, entry point, a usable result, and relevant follow-on
  guidance. Terms and shared explanations have canonical sources.
- No unverified claim, internal NEEDS_VERIFICATION marker, fake screenshot,
  placeholder guide, or QA-only feature is published as current customer behavior.
- Last reviewed reflects an actual review, not a cosmetic edit or build date.

## Workflow and presentation

- Walk through the changed procedures with appropriate permissions and safe test
  data when access and scope permit. Check examples against actual output.
  Do not claim live verification when only code/tests were inspected; record the
  untested paths and keep unsupported instructions out of the published result.
- Run the docs repository's required build/lint/link gates. Inspect rendered pages
  for navigation, headings, lists, tables, code blocks, images, alt text/captions,
  and meaningful link labels. Check relevant narrow/wide layouts when changed.
- Ensure internal links, assets, and redirects resolve. A transient fetch failure
  alone is not proof a page is broken; verify or report uncertainty.
- Check that screenshots represent the documented release and contain no private
  data. Inspect reused and newly captured images in the rendered page for readable
  controls, correct workflow state, useful framing, and accurate captions. Replace
  inadequate local assets with fresh captures following the skill's image guidance;
  report any remaining capture gaps. The procedure must remain understandable
  without the screenshot.
- For a whole app, follow the route from product entry to first useful result,
  common tasks, admin/trust information, and troubleshooting/support. Avoid orphan
  pages and excessive fragmentation; do not measure quality by page count.

## Handoff

Report the affected pages and outcomes, evidence/checks run, unresolved gaps, and
whether changes are drafted, committed, or live. Verify the live pages only when
publication is within scope; do not equate a successful build with publication.
Do not silently expand documentation work into product fixes or site redesign.
