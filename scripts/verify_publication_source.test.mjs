import test from 'node:test';
import assert from 'node:assert/strict';
import { assertPublicationSource } from './verify_publication_source.mjs';

const sha = 'b802b078fd7541e0b9fb005c6e89a33ad931610b';
const valid = { selectedSha: sha, runRef: 'refs/heads/release', runSha: sha, eventName: 'workflow_dispatch', headSha: sha, releaseSha: sha, dirty: false };
test('accepts a clean exact current release manual dispatch', () => assert.equal(assertPublicationSource(valid), sha));
for (const runRef of ['refs/heads/main', 'refs/heads/codex/task', 'refs/tags/docs-snapshot']) {
  test(`rejects dispatch from ${runRef}`, () => assert.throws(() => assertPublicationSource({ ...valid, runRef })));
}
for (const eventName of ['push', 'pull_request', 'schedule']) {
  test(`rejects automatic ${eventName} publication`, () => assert.throws(() => assertPublicationSource({ ...valid, eventName })));
}
for (const selectedSha of [undefined, '', 'b802b07', 'release', sha.toUpperCase(), `${sha}\nextra`]) {
  test(`rejects invalid selected SHA ${JSON.stringify(selectedSha)}`, () => assert.throws(() => assertPublicationSource({ ...valid, selectedSha })));
}
for (const field of ['runSha', 'headSha', 'releaseSha']) {
  test(`rejects mismatched ${field}, including an advanced release tip`, () => assert.throws(() => assertPublicationSource({ ...valid, [field]: 'a'.repeat(40) })));
}
test('rejects dirty publication source', () => assert.throws(() => assertPublicationSource({ ...valid, dirty: true })));
