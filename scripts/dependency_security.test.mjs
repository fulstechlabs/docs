import assert from 'node:assert/strict';
import { readFile, readdir, stat } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import test from 'node:test';

// These tests bound one UNPATCHED upstream cache advisory for this static site.
// They do not mark npm audit clean or approve an SSR/authenticated deployment.
const require = createRequire(import.meta.url);
const root = dirname(dirname(fileURLToPath(import.meta.url)));
const astroRoot = dirname(require.resolve('astro/package.json'));
const { resolveConfig } = await import(pathToFileURL(join(astroRoot, 'dist/core/config/config.js')));
const { loadRemoteImage, revalidateRemoteImage } = await import(
  pathToFileURL(join(astroRoot, 'dist/assets/build/remote.js'))
);
const { astroConfig: config } = await resolveConfig({ root }, 'build');
const lock = JSON.parse(await readFile(join(root, 'package-lock.json'), 'utf8'));
const semver = require('semver');
const CachePolicy = require('http-cache-semantics');
const imageUrl = 'https://assets.example.test/public.png';

async function files(directory) {
  const result = [];
  for (const item of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, item.name);
    if (item.isDirectory()) result.push(...await files(path));
    else result.push(path);
  }
  return result;
}

test('all seven patchable baseline package findings have patched installed/locked versions', () => {
  for (const [name, minimum] of Object.entries({
    astro: '7.2.8', sharp: '0.35.4', devalue: '5.9.3', 'fast-uri': '3.1.8',
    'js-yaml': '4.3.2', nanoid: '3.3.18', svgo: '4.1.0',
  })) {
    const entries = Object.entries(lock.packages).filter(([path]) =>
      path === `node_modules/${name}` || path.endsWith(`/node_modules/${name}`));
    assert.ok(entries.length > 0, `${name} must remain inventoried`);
    for (const [path, entry] of entries) {
      assert.ok(semver.gte(entry.version, minimum), `${path} ${entry.version} < ${minimum}`);
      assert.equal(require(join(root, path, 'package.json')).version, entry.version);
    }
  }
});

test('installed and locked cache library includes the 4.3.0 Vary/header fix, not a max-stale fix', () => {
  const entries = Object.entries(lock.packages).filter(([path]) =>
    path === 'node_modules/http-cache-semantics' || path.endsWith('/node_modules/http-cache-semantics'));
  assert.ok(entries.length > 0, 'cache dependency must remain inventoried');
  for (const [path, entry] of entries) {
    assert.ok(semver.gte(entry.version, '4.3.0'), `${path} lacks CVE-2026-93750 fix`);
    assert.equal(require(join(root, path, 'package.json')).version, entry.version);
  }
});

test('actual cache rejects Vary wildcards with whitespace or additional fields', () => {
  for (const vary of ['*', '* ', ' *', ' * ', '*,', '*, weather', 'weather, *']) {
    const policy = new CachePolicy(
      { headers: { weather: 'ok' } },
      { headers: { 'cache-control': 'max-age=5', vary } },
    );
    assert.equal(policy.satisfiesWithoutRevalidation({ headers: { weather: 'ok' } }), false,
      `Vary ${JSON.stringify(vary)} must never match`);
  }
});

test('actual Vary matching ignores inherited values while preserving own-header positive controls', () => {
  // Published 4.3.0 follows the later upstream simplification: absent on both
  // sides may match, but an inherited value cannot impersonate an own header.
  for (const name of ['constructor', '__proto__', 'weather']) {
    const own = { [name]: 'nice' };
    const inherited = Object.create(own);
    const response = { headers: { 'cache-control': 'max-age=5', vary: name } };
    const ownPolicy = new CachePolicy({ headers: own }, response);
    assert.equal(ownPolicy.satisfiesWithoutRevalidation({ headers: { [name]: 'nice' } }), true);
    assert.equal(ownPolicy.satisfiesWithoutRevalidation({ headers: { [name]: 'bad' } }), false);
    assert.equal(ownPolicy.satisfiesWithoutRevalidation({ headers: inherited }), false);
    const inheritedPolicy = new CachePolicy({ headers: inherited }, response);
    assert.equal(inheritedPolicy.satisfiesWithoutRevalidation({ headers: own }), false);
    assert.equal(inheritedPolicy.satisfiesWithoutRevalidation({ headers: {} }), true);
  }
});

test('GHSA-ch52 remains unpatched in assessed cache source; bounded Astro guards are still required', () => {
  // Characterize the residual flaw with only local synthetic data. This is NOT
  // desired application behavior or a waiver. If upstream fixes it, fail here
  // so the disposition is reassessed rather than silently claiming remediation.
  const url = 'https://cache.example.test/synthetic';
  const policy = new CachePolicy({ url, headers: {} }, {
    status: 200,
    headers: { 'cache-control': 'max-age=60', 'set-cookie': 'synthetic=not-a-credential' },
  });
  policy.now = () => policy._responseTime + 1000;
  assert.equal(policy.maxAge(), 0, 'shared response with cookie has security-zeroed freshness');
  assert.equal(policy.stale(), true);
  const result = policy.evaluateRequest({ url, headers: { 'cache-control': 'max-stale=999999' } });
  assert.equal(result.revalidation, undefined,
    'upstream behavior changed; independently reassess GHSA-ch52 disposition');
  assert.equal(result.response?.headers['set-cookie'], 'synthetic=not-a-credential',
    'upstream behavior changed; do not carry the old unpatched assessment forward');
});

test('effective production config stays static, without adapter or authenticated runtime', () => {
  assert.equal(config.output, 'static');
  assert.equal(config.adapter, undefined);
  assert.equal(config.server.host, false, 'dev/preview must not bind all interfaces by default');
  assert.deepEqual(config.server.allowedHosts, []);
  assert.equal(config.security.checkOrigin, true);
});

test('effective image boundary has no remote allowlist or unsafe SVG processing', () => {
  assert.deepEqual(config.image.domains, []);
  assert.deepEqual(config.image.remotePatterns, []);
  assert.equal(config.image.dangerouslyProcessSVG, false);
  assert.equal(config.image.service.entrypoint, 'astro/assets/services/sharp');
});

test('patched actual Sharp service can decode a benign generated AVIF during the static build', async () => {
  const sharp = require('sharp');
  const { default: service } = await import(pathToFileURL(join(astroRoot, 'dist/assets/services/sharp.js')));
  const avif = await sharp({ create: { width: 2, height: 2, channels: 3, background: '#3377aa' } }).avif().toBuffer();
  const result = await service.transform(avif, { src: 'memory.avif', width: 2, height: 2, format: 'png' }, config.image);
  assert.equal(result.format, 'png');
  const metadata = await sharp(result.data).metadata();
  assert.equal(metadata.width, 2);
  assert.equal(metadata.height, 2);
});

test('application source has no server routes, middleware, actions or live loaders', async () => {
  for (const name of ['pages', 'actions', 'middleware.ts', 'middleware.js']) {
    await assert.rejects(stat(join(root, 'src', name)), { code: 'ENOENT' });
  }
  const appFiles = (await files(join(root, 'src'))).filter(path => /\.(astro|ts|js|mjs|mdx)$/.test(path));
  for (const path of appFiles) {
    const source = await readFile(path, 'utf8');
    assert.doesNotMatch(source, /defineLiveCollection|liveLoader|Astro\.(request|cookies|session)|\bfetch\s*\(/,
      `${path} changed the bounded no-user-session/no-live-fetch model; reassess cache reachability`);
  }
});

test('actual Astro remote load makes a fresh anonymous request, not a client max-stale request', async () => {
  const cacheSource = await readFile(join(astroRoot, 'dist/assets/build/remote.js'), 'utf8');
  assert.doesNotMatch(cacheSource, /satisfiesWithoutRevalidation|responseHeaders|revalidationHeaders|max-stale/,
    'upstream cache use expanded beyond build-time TTL calculation; reassess advisory reachability');
  let calls = 0;
  const result = await loadRemoteImage(imageUrl, async (request, options) => {
    calls++;
    assert.equal(request.url, imageUrl);
    assert.equal(request.method, 'GET');
    assert.deepEqual([...request.headers], []);
    assert.equal(options.redirect, 'manual');
    return new Response('public-image', { headers: { 'cache-control': 'public,max-age=60' } });
  }, config.image);
  assert.equal(calls, 1);
  assert.equal(result.data.toString(), 'public-image');
});

test('actual revalidation accepts only validators, not supplied cookies/auth/cache-control', async () => {
  let calls = 0;
  const result = await revalidateRemoteImage(imageUrl, {
    etag: '"public-image"', lastModified: 'Wed, 01 Oct 2025 00:00:00 GMT',
    headers: { cookie: 'synthetic', authorization: 'synthetic', 'cache-control': 'max-stale=999999999' },
  }, async (request) => {
    calls++;
    assert.deepEqual([...request.headers.keys()], ['if-modified-since', 'if-none-match']);
    assert.equal(request.headers.get('if-none-match'), '"public-image"');
    return new Response(null, { status: 304, headers: { 'cache-control': 'public,max-age=60' } });
  }, config.image);
  assert.equal(calls, 1);
  assert.equal(result.data, null);
});

test('actual build helper does not retain response cookies and rejects unapproved redirects', async () => {
  const result = await loadRemoteImage(imageUrl, async () => new Response('public-image', {
    headers: { 'set-cookie': 'synthetic=not-a-credential', 'cache-control': 'private,no-store' },
  }), config.image);
  assert.deepEqual(Object.keys(result).sort(), ['data', 'etag', 'expires', 'lastModified']);
  assert.ok(result.expires <= Date.now());
  let calls = 0;
  await assert.rejects(loadRemoteImage(imageUrl, async () => {
    calls++;
    return new Response(null, { status: 302, headers: { location: 'https://other.example.test/image.png' } });
  }, config.image), /not an allowed remote location/);
  assert.equal(calls, 1);
});

test('deployable artifact contains static HTML/assets, not a server or dynamic image endpoint', async () => {
  const output = join(root, 'dist');
  const artifact = await files(output);
  assert.ok(artifact.some(path => path.endsWith('/index.html')), 'run build before this artifact gate');
  assert.ok(!artifact.some(path => /\/(server|_image|_worker\.js)(\/|$)/.test(path)));
  for (const path of artifact.filter(path => path.endsWith('.html'))) {
    assert.doesNotMatch(await readFile(path, 'utf8'), /(?:src|srcset)=["'][^"']*\/_image\?/,
      `${path} references an on-demand image endpoint`);
  }
});
