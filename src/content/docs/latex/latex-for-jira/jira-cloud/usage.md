---
title: "Usage (without browser extension)"
---

## Notice

> **It is recommended to use this Jira app with browser extension, since the combination provides the flexibility to write LaTeX in everwhere: Summary, Description, Comment, custom fields, etc. Please see the instructions here** [**https://docs.fulstech.com/latex/latex-for-jira/jira-cloud/usage-with-browser-extension/**](../usage-with-browser-extension/)**.**

## Overview

After installing and starting the trial period, the app will add a custom field name **LaTeX text** to the Jira instance.

The first step is to add the custom field **LaTeX text** to issue types and projects.

## For classic Jira projects

### Associate the LaTeX custom field to issue screens

Navigate to the **Custom fields** page.

![LaTeX for Jira](../../../assets/external-7e926d1490e4a36b.png)

![LaTeX for Jira](../../../assets/external-bfd05a7f64382c75.png)

Search for the custom field **LaTeX text** and add it to screens.

![LaTeX for Jira](../../../assets/external-4578362930201747.png)

![LaTeX for Jira](../../../assets/external-5e987019a4893c3d.png)

![LaTeX for Jira](../../../assets/external-fbb4b8de05d114fb.png)

### Add the **LaTeX** panel to the issue screen

On an issue view, click on the “three dots” icon and select **LaTeX**.

![LaTeX for Jira](../../../assets/external-5c4fd8126a9a7c6c.png)

## For Next-gen Jira projects

Click on **Project settings** on the left sidebar.

![LaTeX for Jira](../../../assets/external-99523016357c1eee.png)

On the **Project settings** page, click on **Apps** on the left sidebar.

![LaTeX for Jira](../../../assets/external-f475cc2761077474.png)

Click on **App fields** on the left sidebar and enable **LaTeX for Jira Cloud.**

![LaTeX for Jira](../../../assets/external-9edea863ac195939.png)

Go back to the **Project settings** page, click on **Issue types** on the left sidebar.

![LaTeX for Jira](../../../assets/external-a14893461410b900.png)

Drag the **LaTeX text** field from the right sidebar and drop it into the **Description fields** area.

![LaTeX for Jira](../../../assets/external-75edc2820fe16390.png)

![LaTeX for Jira](../../../assets/external-38167e93e6f3f532.png)

## Add LaTeX formulas to an issue

Click on the **Edit** button.

![LaTeX for Jira](../../../assets/external-a6a7931ffa877c47.png)

**Please do not edit the custom field itself. Whenever you want to add or modify the formulas, please use the app’s Edit button.**

The LaTeX content is wrapped around by **{latex}…{latex}**.

Sample content:

```
{latex}
ax^2 + bx + c = 0
{latex}

{latex}
x = \frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}}
{latex}
```

![LaTeX for Jira](../../../assets/external-881ddc36d48fe2a6.png)

After that, click **Save**.

![LaTeX for Jira](../../../assets/external-9edb2d771155714f.png)
