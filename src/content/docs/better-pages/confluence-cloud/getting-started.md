---
title: "Getting Started"
description: "Install Better Pages, open its home page, and add your first Confluence macro."
---

## Requirements

- Confluence Cloud.
- A Confluence administrator to install or upgrade the app.
- Page edit permission to add macros.
- Space create permission when using a Better Pages template.

During private availability, install Better Pages with the Atlassian installation link supplied for your environment. After installation, confirm that **Better Pages home** appears under **Apps → Your apps**.

## Add your first macro

1. Edit a Confluence page.
2. Select **Insert more content** or type `/`.
3. Search for `Better Pages`.
4. Select the macro that matches your need.
5. Configure it and save the macro.
6. Publish or update the page.
7. Reload the published page and test its reader interaction.

Better Pages currently exposes these editor entries:

- **Better Pages message**
- **Better Pages button**
- **Better Pages progress**
- **Better Pages tooltip**
- **Better Pages math**
- **Better Pages tabs**
- **Better Pages clickable content**
- **Better Pages extended formatting**

## Use a template

Open **Apps → Better Pages home**, select a destination space, enter a unique title, and choose a template. Select **Preview template** to review the content type and generated structure. Nothing is created until you select **Create in Confluence**.

Created pages and blog posts are ordinary Confluence content. You can open, edit, move, copy, or delete them using normal Confluence controls. A delivery journey creates one parent page and a linked child page for each configured stage. If a later child cannot be created, Better Pages keeps the items that were created successfully and shows them in the result.

Available templates:

- Project brief
- Weekly update blog post
- Research brief
- Financial review
- Software requirements
- Space landing page
- Delivery journey

## Safe destinations

Buttons, progress steps, status labels, navigation items, rollover cards, and clickable content accept:

- Relative Confluence paths beginning with `/`, such as `/wiki/home`.
- `https://` URLs without embedded credentials.
- Strict `mailto:` addresses.

Unsafe or unsupported destinations such as `javascript:`, `file:`, protocol-relative URLs, or malformed email links do not become active navigation actions.
