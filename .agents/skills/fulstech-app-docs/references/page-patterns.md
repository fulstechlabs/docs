# Page Patterns

Choose the reader's intent, not a mandatory form. These are content prompts;
omit irrelevant sections and avoid empty scaffolding.

## Overview

Explain the outcome, who benefits, the simple mental model, platform, and a few
real use cases. Route new users to first success, admins to configuration, and
evaluators to data handling. Link key capabilities and important limitations.
Keep it a useful entry point, not an exhaustive manual or a sales landing page.

## Getting Started and task guides

State the useful result, prerequisites and permissions, where to start, numbered
actions with exact UI labels, and how to recognize and interpret success. Use a
coherent Jira/Confluence example rather than disconnected placeholder values.
Offer the next likely task. Keep advanced setup out of onboarding unless required.

## Concepts and feature reference

A concept explains what something means, why/when it matters, how it affects the
result, and a simple example. A task explains how to achieve a result. Link them
instead of repeating long conceptual introductions in every procedure.

Feature reference explains supported options, defaults, interactions, example
input/output, and limits. Use tables for genuine comparisons or field mappings,
not to replace a readable workflow. Link to a task that demonstrates the feature.

## Administration and permissions

Explain who can configure, where the controls are, and whether settings apply to
the site, space, project, or user. Cover verified defaults, effects on existing
data and other users, and recovery/audit options only if supported. Distinguish
permission to configure from permission to use or view results. Use a permission
matrix when several roles/actions would otherwise be ambiguous.

## Security and data

For active Cloud apps, provide a discoverable product-specific explanation of:
hosting/runtime; accessed and processed data; storage locations; egress and
external services; scopes and their purpose; retention, deletion and uninstall;
data residency; analytics/telemetry; and support diagnostics. Link applicable
approved policies. A global privacy link alone does not explain product behavior.

Verify each applicable statement against the target release and authoritative
policy/platform evidence. Do not infer "no storage" from stateless compute or
"no egress" from using Forge. Do not infer compliance, certification, residency,
or a trust badge from architecture. Resolve contradictions with declarations;
do not silently rewrite legal commitments as part of a docs update.

## Compatibility, limitations, migration and backup

State what is supported, unsupported, or not yet verified distinctly. Include
platform, version, project types, fields, export formats, or limits only as relevant.
Separate materially different Cloud/DC or legacy/current workflows.

For supported migration/backup, explain source and target versions, what moves
and does not, prerequisites, ordering, validation, failure/recovery behavior, and
whether the source remains intact. Never imply migration parity from similarly
named features. Do not create a migration guide for a backlog-only capability.

## Troubleshooting and support

Title entries with the symptom the customer sees. Explain likely causes as
hypotheses, how to distinguish them, safe remedies, and when to contact support.
Place contextual troubleshooting close to the related task; promote recurring
questions to guides instead of growing a miscellaneous FAQ.

Give a verified support link and the minimum useful diagnostic details: product,
platform/version, relevant project type, reproduction steps, expected/actual
result, error text, and a sanitized screenshot when useful. Warn against sending
passwords, tokens, unnecessary customer data, or raw HAR/logs containing secrets.
Do not require intrusive diagnostics for every issue or promise an unverified SLA.

## Release notes

Describe the customer-visible change, affected version/platform, required action,
and known limitations. Distinguish released changes from plans. Link to updated
guides rather than repeating implementation history or claiming exhaustive QA.
