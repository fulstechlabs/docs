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

Customer-facing documentation should follow [`docs/docs-style-guide.md`](docs/docs-style-guide.md).

## Public publication

Publication follows `docs PR → main → promotion PR main→release → release →
manual deployment → public verification`. No branch push deploys public docs.
Bootstrap a missing `release` only from verified currently published lineage.

After the reviewed promotion is merged, record the full current `release` SHA
and dispatch **Deploy documentation to GitHub Pages** from the `release` branch
with that same SHA as `release_sha`. The workflow fails closed unless the input,
workflow revision, clean checkout and freshly fetched `origin/release` agree.
It checks content, builds and audits links/assets, then rechecks the release tip
before deploying. If the branch advances, review the new promotion and dispatch
again for its exact SHA; do not bypass the guard.

Record promotion PR, deployed full SHA, Actions run, timestamp and verification
of the public custom domain. A successful build alone is not publication proof.
If Actions quota/billing is unavailable, an authorized outside-Actions fallback
must use the same already-promoted SHA and equivalent local check/build/audit,
recording tool versions, artifact and publication evidence. Do not deploy `main`
or replay the deployment automatically when Actions becomes available again.
