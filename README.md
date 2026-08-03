# Fulstech documentation

Source for the Fulstech product documentation site.

- Production: <https://docs.fulstech.io>
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
the rendered source asset.
