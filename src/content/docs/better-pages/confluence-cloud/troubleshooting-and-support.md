---
title: "Troubleshooting and Support"
description: "Resolve common Better Pages configuration, navigation, search, external content, and permission issues."
---

## A macro is missing from the editor

Confirm that Better Pages is installed and enabled under **Manage apps**. Reload the editor, open **Insert more content**, and search for `Better Pages`. If an older test page contains a retired pre-release macro identifier, remove that macro and insert the current Better Pages macro again.

## A button or destination is disabled

Use a relative Confluence path beginning with `/`, an `https://` URL, or a strict `mailto:` address. Remove spaces, embedded credentials, protocol-relative syntax, and unsupported schemes such as `file:` or `javascript:`.

## Tabs show no sections

Edit the body of **Better Pages tabs** and add level-two or level-three headings. Each heading starts a section. Content before the first supported heading is not a tab.

## Search returns no results

- Confirm the reader can access the expected pages.
- For explicit-space mode, verify the configured space keys.
- Remove or widen the modified-after date.
- Try a shorter search phrase.

Better Pages search intentionally does not fall back from an invalid explicit-space configuration to an all-site search.

## An external frame is denied or blank

Ask a Confluence administrator to check both the Better Pages frame policy and Atlassian customer-managed egress approval. A frame can still be blank when the destination blocks embedding with Content Security Policy or `X-Frame-Options`; Better Pages cannot override the destination's policy.

## An external image is denied

The exact HTTPS origin must be approved specifically for images. Existing frame permission for the same origin is not sufficient. Also confirm the final image URL does not redirect to a different, unapproved origin.

## A local form is disabled

A Confluence administrator must enable **Local form capability** in **Better Pages administration**. This setting applies to the whole installation.

## An administrator save reports a conflict

Another administrator saved a newer settings revision or a customer-managed egress change is still in progress. Reload the administration page, review the latest state, and save again.

## PDF or Word looks different from the page

Exports are intentionally static. Tabs, dialogs, tooltips, forms, search results, and external content cannot preserve live browser interaction. See [Security and Privacy](../security-and-privacy/#static-export) for the export contract.

## Contact support

Submit bugs and feature requests through the [Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals). Include:

- Confluence site and page URL.
- Better Pages macro name.
- Expected and actual behavior.
- Reproduction steps.
- A screenshot with sensitive information removed.

Do not include passwords, access tokens, private form values, or confidential page content that support does not need.
