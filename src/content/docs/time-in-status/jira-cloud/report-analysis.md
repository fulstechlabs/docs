---
title: "Report Analysis"
description: "Compare workflow bottlenecks, trends and aging work."
---

Use report analysis to find where work waits, compare delivery over time, and
inspect the issues behind a total. Open **Apps → Time in Status → Reports**.

## Start with a question

1. Under **Start with a question**, choose the question you want to investigate.
2. Select **Use this question**.
3. Choose your project or JQL and review the suggested report settings.
4. Select your statuses and calendar, then **Run report**.

The question sets starting options. Adjust them to match your team's workflow.

## Compare repeated visits

For **Time in status**, use **Repeated status visits** to choose the total,
first, latest or average observed visit. For example, two visits of two hours
and six hours give a total of eight hours and an average of four hours.

The rule is applied to each issue and status before issues are grouped. Status
groups combine the resulting member-status values.

## Compare groups and inspect contributors

1. Expand **Group results**.
2. Choose **First dimension**, such as project or current assignee.
3. Optionally choose **Second dimension** to compare combinations.
4. Choose total, mean or median per contributing issue and run the report.
5. Select a grouped value to inspect the issues contributing to it.

A missing measurement is excluded from mean and median; an observed zero is
included. Grouping uses current Jira fields. An issue with several components
can appear in more than one component group.

Use **View history** on an issue row to inspect its workflow visits. This helps
explain repeated statuses and the durations shown in the report.

## Compare trends

Choose **Status time by period** to see how much time occurred in each week or
month. A visit spanning two periods contributes time to both periods.

Choose **Delivery trend** to compare completed issues by week or month. Configure
the completion statuses to match your workflow. Issues are placed in the period
when they entered their current completion block. Reopened issues are excluded
until they are completed again.

Review the measurement window and calendar before comparing periods. A period
that is still in progress may have less recorded time or fewer completed issues.

## Find aging work

1. Select **Open work aging**.
2. Configure cycle and completion statuses for your workflow.
3. Set **Minimum cycle age (hours)** to focus on older work.
4. Run the report and inspect cycle age alongside current-status age.

Cycle age starts at the first configured cycle status in the current delivery
episode. Current-status age measures only the current visit. Age is measured up
to now, independently of the selected history period. One-page reports rank
issues within that page; all-pages reports rank the collected issues.

## Explore ownership and field history

**Assignee by status** breaks elapsed ownership down by workflow status. It can
help explain handoffs and waiting while an issue belonged to someone. These
values are not logged effort or an individual productivity score.

Select **Jira field duration** or **Jira field value count**, then choose a
supported field offered by the app. Duration measures how long each value was
held; count measures entrances into each value. For example, a supported Client
field can show time associated with each client value as that field changes.
Only history available from Jira can be measured.
