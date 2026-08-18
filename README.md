# Fulstech documentation

Source for the Fulstech product documentation site.

- Production: <https://docs.fulstech.com>
- Legacy GitBook: <https://fulstech.gitbook.io/docs>

## Local development

```bash
npm install
npm run dev
```

To verify the root path used by the production custom domain:

```bash
DOCS_SITE_URL=https://docs.fulstech.com DOCS_BASE_PATH=/ npm run build
DOCS_BASE_PATH=/ npm run audit:build
```

The site is built with [Astro Starlight](https://starlight.astro.build/) and
uses Starlight's default Pagefind search. Production output is generated in
`dist/`.

The committed `src/content/docs/` tree contains authored documentation,
not a one-to-one copy of GitBook routes or UI. The current public GitBook
inventory contains 76 authored pages and 36 navigation-only category, product,
and platform nodes. Starlight renders those nodes as native sidebar groups,
while static redirects preserve their former URLs.

To refresh authored content while the legacy site remains available:

```bash
python scripts/import_gitbook.py
```

The import is deterministic and follows the reviewed content model: it retains
authored text, headings, links, code, images, callout content, and tab labels;
it excludes GitBook-generated navigation pages and UI. It also keeps content
images local, adds Starlight frontmatter, regenerates `src/sidebar.json`, and
updates `src/redirects.json`.

## Migration audit

Compare the committed authored-content inventory with GitBook and verify that
navigation-only source routes remain classified separately:

```bash
python scripts/audit_migration.py
```

Also verify all rendered GitBook and GitHub Pages routes, headings, images, and
code blocks:

```bash
python scripts/audit_migration.py \
  --live-base https://docs.fulstech.com/ \
  --output migration-audit.json
```

The public audit covers the complete published inventory exposed by the
GitBook sitemap, Markdown index, and every chunk of the paginated
`llms-full.txt` export. Hidden or unpublished GitBook content must be
inventoried separately through Git Sync or the authenticated GitBook API.
The audit also fails if a visible content image remains externally hosted.
