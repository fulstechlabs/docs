import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

export function assertPublicationSource({ selectedSha, runRef, runSha, eventName, headSha, releaseSha, dirty }) {
  if (eventName !== 'workflow_dispatch') throw new Error('Publication requires a manual workflow_dispatch.');
  if (runRef !== 'refs/heads/release') throw new Error('Dispatch the workflow from release, never main or another ref.');
  if (!/^[a-f0-9]{40}$/.test(selectedSha ?? '')) throw new Error('Select one full, lowercase Git commit SHA.');
  if ([runSha, headSha, releaseSha].some(sha => sha !== selectedSha)) {
    throw new Error('Selected SHA, workflow SHA, checkout HEAD and current origin/release must all match.');
  }
  if (dirty) throw new Error('Publication source must be clean.');
  return selectedSha;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const git = (...args) => execFileSync('git', args, { encoding: 'utf8' }).trim();
    git('fetch', 'origin', 'release');
    const sha = assertPublicationSource({
      selectedSha: process.env.DOCS_RELEASE_SHA,
      runRef: process.env.DOCS_RUN_REF,
      runSha: process.env.DOCS_RUN_SHA,
      eventName: process.env.DOCS_EVENT_NAME,
      headSha: git('rev-parse', 'HEAD'),
      releaseSha: git('rev-parse', 'origin/release'),
      dirty: git('status', '--porcelain').length > 0,
    });
    console.log(`Verified exact documentation publication source: ${sha}`);
    if (process.env.GITHUB_STEP_SUMMARY) {
      const { appendFileSync } = await import('node:fs');
      appendFileSync(process.env.GITHUB_STEP_SUMMARY, `Documentation publication source: \`${sha}\` (current release tip).\n`);
    }
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
