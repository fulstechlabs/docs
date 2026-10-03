---
title: "Forge successor security and data"
description: "Architecture, permissions, recovery, external requests, and limitations of JEditor Release 1.1."
---

This technical review page describes **JEditor Release 1.1 on Forge**, not the
legacy Connect app. The successor is not yet approved or available on Marketplace.
It is not a security certification or a claim that final submission checks are complete.

## Where your data goes

Issue values remain in Jira. Project mappings/templates use Jira project
properties. Native fields use Jira app-field storage plus an issue-property
compatibility mirror. Atlassian-hosted Forge KVS stages accepted native saves
for recovery; this can temporarily include rich content and personal data.
There is no Fulstech-hosted product backend, Forge Remote, product-analytics
service, or automatic external log exporter in this release.

See the [draft privacy notice](../privacy-policy/) for data categories,
retention boundaries, external providers, and privacy contacts. It is not yet
an effective legal policy.

## Permissions and access

Interactive operations validate trusted Forge project/issue context before
checking Jira permissions. Resolvers then call Jira as the app. Configuration
and templates require project administration; issue reading requires browse
permission, and new saves require edit permission. Recovery can complete an
already accepted save during a later read or scheduled app-context maintenance;
the reading caller does not supply a new recovery value.

| Scope | Purpose |
| --- | --- |
| `read:jira-work` | Read configured values, fields, edit metadata, issue types, and properties |
| `read:permission:jira` | Check Jira issue/project permissions |
| `write:issue:jira` | Save Description and supported multiline fields |
| `write:issue.property:jira` | Maintain native-field compatibility mirrors |
| `write:project.property:jira` | Save mappings and templates |
| `write:app-data:jira` | Save app-owned native field values |
| `storage:app` | Stage and complete interrupted saves in Forge KVS |

These are mixed classic/granular scopes, not seven granular scopes. Jira fields
and properties are not a secret vault. The app does not ask users for passwords
or external-service credentials.

## Content and external requests

Read-only rich HTML is sanitized before insertion into the page. Stored-content
and trusted-target checks provide additional controls; tested paths are not an
exhaustive XSS guarantee.

CKEditor assets come from `cdn.ckeditor.com`; MathJax from `cdnjs.cloudflare.com`.
Image references can contact customer-selected external hosts. Public HTTPS
authoring restrictions and image-loading checks do not certify every provider's
TLS negotiation, redirects, or DNS behavior. No-referrer does not hide IP
addresses or requested URLs. This architecture does not claim **Runs on Atlassian**.

**CKEditor 4.22.1 is end-of-life.** It is not claimed current, vendor-supported,
or vulnerability-free. npm audits cover locked npm packages, not CDN-delivered
libraries. Recorded compatibility risk and maintenance commitments are not remediation.

## Recovery, logs, and residency

Native recovery journals are deleted after canonical/mirror convergence. Daily
maintenance retries stale intent; 24 hours is not a hard payload TTL. The app
can retain accepted content while an interrupted write cannot safely finish.

Forge logs can contain operational identifiers and Jira error text, including
customer data in failed responses. This release does not guarantee universal
personal-data redaction. Send only sanitized diagnostics to support.

Jira follows its platform controls; Forge KVS follows eligible
[hosted-storage residency](https://developer.atlassian.com/platform/forge/data-residency/).
This is not a pinning guarantee for logs, compute, browser state, or external
traffic. Atlassian certifications are not certifications of JEditor or Fulstech.

## Report a security concern

Contact [support@fulstech.com](mailto:support@fulstech.com) with the product,
affected version, and minimum reproducible detail. Do not post credentials or
exploit data publicly. Review the [Fulstech security policy](/security-policy/)
alongside these release-specific limits; it is not evidence of app certification.

This page does not assert Bug Bounty enrollment, a published CAIQ, a completed
Marketplace security review, or customer-managed encryption keys.
