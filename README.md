# Fulstech documentation

Source for the Fulstech product documentation site.

- Production: <https://docs.fulstech.com>
- Temporary GitHub Pages URL: <https://fulstechlabs.github.io/docs/>
- Legacy GitBook: <https://fulstech.gitbook.io/docs>

## Local development

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

The committed `docs/` tree is a snapshot imported from the legacy GitBook. To
refresh it while the legacy site remains available:

```bash
python scripts/import_gitbook.py
```

The import is deterministic and fails if it cannot map every GitBook image to
the rendered source asset. It also downloads externally hosted content images
into `docs/assets/`, so the published site does not depend on third-party image
hotlinks.

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
