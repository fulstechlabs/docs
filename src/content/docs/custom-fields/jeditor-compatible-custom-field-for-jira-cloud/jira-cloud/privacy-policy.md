---
title: "Forge successor privacy notice — draft"
description: "Review draft of JEditor Release 1.1 data handling; not an effective privacy policy."
---

**Review draft, not an effective privacy policy.** This notice describes the
Forge successor, JEditor Release 1.1, which is not yet approved as a Marketplace
successor. Legal review and a separate publication decision are required before
this URL can be used as the app's effective privacy policy.

JEditor edits configured rich Jira issue content and project templates. This
notice does not replace your organization's Jira policies or cover Fulstech's
separate website, billing, or support-business activities.

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
Forge Remote, or product-analytics service. It still makes external browser requests.

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

## Storage location and support

Jira fields/properties follow Jira controls. Forge KVS uses
[Atlassian's hosted-storage data-residency support](https://developer.atlassian.com/platform/forge/data-residency/)
for eligible locations and migrations. JEditor does not promise region pinning
for logs, execution, browser state, or external requests.

Fulstech may receive diagnostics you choose to send to support. Use sanitized
screenshots and the minimum reproducible detail; do not send credentials or
unnecessary customer content. Contact [support@fulstech.com](mailto:support@fulstech.com)
or the [support portal](https://fulstech.atlassian.net/servicedesk/customer/portals)
for questions or data requests. Your Jira administrator controls customer content
and permissions; app support does not promise direct deletion of Atlassian backups.

## Before this draft becomes effective

The policy reviewer must approve the applicable legal entity/contact details,
processor/controller and service-provider/business roles, DPA, provider/transfer
treatment, and support retention. Those commitments are not established by
this technical draft. See also [Security and data](../security-and-data/).
