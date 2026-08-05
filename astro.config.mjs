import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sidebar from './src/sidebar.json';

const site = process.env.DOCS_SITE_URL || 'https://docs.fulstech.com';
const base = process.env.DOCS_BASE_PATH || '/';

export default defineConfig({
  site,
  base,
  integrations: [
    starlight({
      title: 'Fulstech Docs',
      description: 'Documentation for Fulstech Jira and Confluence apps',
      favicon: '/favicon.svg',
      customCss: ['./src/styles/custom.css'],
      expressiveCode: {
        shiki: {
          langs: [
            { name: 'plant-uml', scopeName: 'source.plantuml', patterns: [] },
            { name: 'dot', scopeName: 'source.dot', patterns: [] },
          ],
        },
      },
      editLink: {
        baseUrl: 'https://github.com/fulstechlabs/docs/edit/main/',
      },
      lastUpdated: true,
      social: [
        {
          icon: 'github',
          label: 'Fulstech on GitHub',
          href: 'https://github.com/fulstechlabs',
        },
      ],
      components: {
        Header: './src/components/Header.astro',
        MarkdownContent: './src/components/MarkdownContent.astro',
        PageTitle: './src/components/PageTitle.astro',
      },
      sidebar,
    }),
  ],
});
