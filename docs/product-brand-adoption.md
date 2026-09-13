# Documentation product identities

Approved on-site adoption: 2026-09-13. Reusable sources remain in
`fulstechlabs/brand` at revision `42f4c9b`. Exact source paths, source revision,
copy paths and SHA-256 hashes are recorded in
`public/assets/app-icons/v1/provenance.json`. Time in Status keeps its existing
versioned asset URL for the Forge dashboard thumbnail.

`src/product-icons.json` maps product routes to bundled public assets. More
specific Cloud/Data Center entries precede shared product prefixes. Both page
headings and the home directory use `src/product-icons.ts`, independent of
editable sidebar labels. Add new approved identities here rather than
hard-coding another product into a component.

The audit covered all built documentation routes: 128 product pages now have
matching icons (119 newly covered, 9 existing Time in Status pages retained).
The home directory includes 16 products with known identities, including the
previously omitted Better Pages, Time in Status, Issue Templates and JEditor.
Better font for Jira Server remains text-only: it is archived and no verified
identity exists in the brand catalog. Company/legal pages keep company identity.
Category illustrations and historical feature screenshots are not app logos.

Original asset bytes and aspect ratios are preserved. Neutral white icon
surfaces keep black line art readable in dark mode; decorative images use
empty alt text beside their existing title/link text.

Verification: Astro check (14 files, zero errors/warnings), 137-page build and
21,148 local references across 175 HTML files passed. Every mapped rendered
page was checked against its expected asset. Desktop home and Better Pages
heading, dark home, 390px directory and Issue Templates heading were visually
verified. The mobile document width remained 390px. Preview server stopped and
task-owned browser tabs closed after verification.
