---
title: "Troubleshooting and Support"
description: "Resolve common Better Pages authoring, interaction, permission, image, and administration issues."
---

## A macro is missing from the editor

Confirm that Better Pages is installed and enabled under **Manage apps**. Reload
the Confluence editor, open **Insert elements**, and search for `Better Pages`.
The current catalog contains 19 authoring macros.

## A Button, Card, Banner, or Progress step does not open

Edit the component and verify the destination. Supported values are a selected
Confluence page, an `https://` address, a relative path beginning with `/`, an
anchor beginning with `#`, or a valid `mailto:` address. Credentials,
protocol-relative URLs, `javascript:`, and local-file schemes are rejected.

## Tabs do not form one group

Each Tabs macro represents one tab. Put the Tabs macro blocks directly next to
one another. A normal block between them separates the groups. Give each tab a
unique name and select only one default tab.

## Footnotes or references are missing from a summary

Publish the page before checking the final order. A summary collects compatible
items above it, stopping at the previous summary in the same page scope. Move
the summary after the items it should collect.

## An image is blank

Open the macro editor and reselect the source. For uploads, confirm the file
type and size; for page attachments, verify the reader can access the page; for
Brand Kit assets, confirm the kit is published. A stock result may become
unavailable at its source and can be selected again.

## Interactive controls look correct but do not respond

Test the published page, not only the Confluence editor placeholder. Reload the
page, then try pointer and keyboard interaction. Confirm the app is enabled and
that no browser content blocker is removing Atlassian Forge frames.

## Smart Designer will not save

Open Smart Designer from the published page's byline. The editor launcher is a
safe preview because Forge cannot replace the surrounding unsaved editor draft.
If the source page changed, reload the source, rebuild the staged canvas, and
apply it again.

## Space Manager stopped partway

Review the completed-operation list and refresh the inventory. Confluence
permissions and page state are checked immediately before each operation, so a
batch can stop after earlier items succeeded. Do not rerun the full selection
until you identify which pages already changed.

## An administrator setting reports a conflict

Another administrator saved a newer revision, or Atlassian egress consent is in
progress. Reload, review the current state, and save again.

## Contact support

Submit bugs and feature requests through the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Include the site and page URL, Better Pages feature, expected and actual result,
reproduction steps, and a screenshot with sensitive information removed. Never
include passwords, tokens, or confidential content that is not required.
