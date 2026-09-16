# Fulstech documentation

Source for the Fulstech product documentation site.

- Production: <https://docs.fulstech.com>

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

The committed `src/content/docs/` tree is the canonical documentation source.
Navigation is maintained in `src/sidebar.json`, and redirects are maintained in
`src/redirects.json`.
