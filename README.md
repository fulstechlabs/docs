# Fulstech documentation

Source for the Fulstech product documentation site.

- Production: <https://docs.fulstech.com>
- Temporary GitHub Pages URL: <https://fulstechlabs.github.io/docs/>
- Legacy GitBook: <https://fulstech.gitbook.io/docs>

## Local development

```bash
npm install
npm run dev
```

To verify the same `/docs` base path used by GitHub Pages:

```bash
DOCS_SITE_URL=https://fulstechlabs.github.io DOCS_BASE_PATH=/docs npm run build
DOCS_BASE_PATH=/docs npm run audit:build
```

The site is built with [Astro Starlight](https://starlight.astro.build/) and
uses Starlight's default Pagefind search. Production output is generated in
`dist/`.

The committed `src/content/docs/` tree is a snapshot imported from the legacy
GitBook. To refresh it while the legacy site remains available:

```bash
python scripts/import_gitbook.py
```

The import is deterministic and fails if it cannot map every GitBook image to
the rendered source asset. It also downloads externally hosted content images
into `src/content/docs/assets/`, adds Starlight frontmatter, and regenerates
`src/sidebar.json`, so the published site does not depend on third-party image
hotlinks or a manually maintained navigation inventory.

## Migration audit

Compare the committed source with every Markdown page and asset reference
published by GitBook:

```bash
python scripts/audit_migration.py
```

Also verify all rendered GitBook and GitHub Pages routes, headings, images, and
code blocks:

```bash
python scripts/audit_migration.py \
  --live-base https://fulstechlabs.github.io/docs/ \
  --output migration-audit.json
```

The public audit covers the complete published inventory exposed by the
GitBook sitemap, Markdown index, and every chunk of the paginated
`llms-full.txt` export. Hidden or unpublished GitBook content must be
inventoried separately through Git Sync or the authenticated GitBook API.
The audit also fails if a visible content image remains externally hosted.
