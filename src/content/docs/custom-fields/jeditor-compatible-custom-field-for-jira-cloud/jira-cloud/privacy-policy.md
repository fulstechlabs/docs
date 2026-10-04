---
title: "Forge successor privacy policy"
description: "How JEditor Release 1.1 on Forge processes, stores, and retains data."
---

**Effective date:** October 4, 2026

This policy explains how **Fulstech, Inc.** processes information through
**JEditor Release 1.1 on Forge**. It describes the Forge successor, not the
legacy Connect app. The Forge successor is not yet approved or available on
Marketplace; this policy does not announce a Marketplace release.

JEditor edits configured rich Jira issue content and project templates. This
policy does not replace your organization's Jira policies or cover Fulstech's
separate website or billing activities.

## Data used by the app

| Data | Purpose and location |
| --- | --- |
| Rich field content, including links, image references, tables, and equations | Display/edit in your browser; underlying values in Jira |
| Project, field, and issue-type identifiers; mappings and template content | Configuration and reuse in Jira project properties |
| Native app-field values and compatibility mirror | Jira app-field storage and issue properties |
| Accepted native-save content, issue/field identifiers, timestamps, confirmation digest | Interrupted-save recovery in Atlassian-hosted Forge KVS |
| Operational identifiers and errors | Forge logs; error text can contain customer data |
| Requested asset/image URLs and browser network metadata | External providers that receive those browser requests |

You control content entered into issues and templates; it may contain personal
or sensitive information. Do not enter passwords, API tokens, or unnecessary
sensitive content. This release has no Fulstech-hosted product backend,
Forge Remote, product-analytics service, advertising, or AI processing.
Fulstech does not sell data collected through this app. The app still makes
external browser requests.

## Save recovery and retention

Before a native-field write, the app stages the accepted intent in Forge KVS.
After matching Jira readback, it can remove the rich payload while retaining
confirmation metadata until mirror repair completes. Completion deletes the journal.

Daily maintenance retries stale records after a 24-hour active period.
**24 hours is not a deletion deadline.** Unavailable or inconsistent Jira
readback can require retaining accepted content until recovery safely completes.
There is no customer-selectable recovery-journal retention setting.

Your organization manages Jira fields and properties. Uninstalling the app is
not represented as erasing Jira values or all configuration. Forge installation
storage retention and recovery follow [Atlassian's hosted-storage lifecycle](https://developer.atlassian.com/platform/forge/storage-reference/hosted-storage-data-lifecycle/).
Those platform processes are not an app promise to erase every log or backup.

## External assets and images

The browser loads CKEditor from `cdn.ckeditor.com` and MathJax from
`cdnjs.cloudflare.com`. The app does not intentionally upload issue/template
content to these asset CDNs. Providers receive network metadata and requested
resource URLs under their own policies.

Referenced images are loaded from the selected host, not uploaded to Fulstech
storage by this feature. A URL's path or query can disclose sensitive information.
Use trusted HTTPS image providers. No-referrer reduces referrer disclosure;
it does not hide your IP address or the requested URL.

External destinations have their own processing, logging, and retention
practices. Their requests are not covered by your Atlassian data-residency
choice, and they may process network information outside your selected
Atlassian region or outside the EEA. Use destinations whose policies and
transfer conditions meet your organization's requirements. This policy does
not claim that Fulstech has a DPA or approved transfer mechanism with those
providers.

## Storage location

Jira fields/properties follow Jira controls. Forge KVS uses
[Atlassian's hosted-storage data-residency support](https://developer.atlassian.com/platform/forge/data-residency/)
for eligible locations and migrations. JEditor does not promise region pinning
for logs, execution, browser state, or external requests.

## Customer Data Processing Agreement

Fulstech does not currently provide a separate customer Data Processing
Agreement (DPA) for this app. This statement does not remove obligations under
applicable data-protection laws. Atlassian's Forge developer DPA is not a
Fulstech-to-customer DPA.

## Support and privacy requests

For support or privacy requests, contact
[support@fulstech.com](mailto:support@fulstech.com) or the
[Fulstech support portal](https://fulstech.atlassian.net/servicedesk/customer/portals).
Provide only the minimum information necessary and do not include passwords,
API tokens, or unnecessary customer content. Your Jira administrator controls
customer content and permissions; app support does not promise direct deletion
of Atlassian backups.

See [Security and data](../security-and-data/) for release-specific permissions,
logging, external requests, and security limitations. Material changes to this
policy will be published at this URL with an updated effective date.
