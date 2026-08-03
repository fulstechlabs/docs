# Usage (without browser extension)

## Notice

> **It is recommended to use this Jira app with browser extension, since the combination provides the flexibility to write LaTeX in everwhere: Summary, Description, Comment, custom fields, etc. Please see the instructions here** [**https://fulstech.gitbook.io/docs/latex-for-jira/jira-cloud/usage-with-browser-extension**](usage-with-browser-extension.md)**.**

## Overview

After installing and starting the trial period, the app will add a custom field name **LaTeX text** to the Jira instance.

The first step is to add the custom field **LaTeX text** to issue types and projects.

## For classic Jira projects

### Associate the LaTeX custom field to issue screens

Navigate to the **Custom fields** page.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/07/image.png?w=1024)

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/07/image-1.png?w=1024)

Search for the custom field **LaTeX text** and add it to screens.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-10.png?w=1024)

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-11.png?w=1024)

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-12.png?w=1024)

### Add the **LaTeX** panel to the issue screen

On an issue view, click on the “three dots” icon and select **LaTeX**.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-13.png?w=1024)

## For Next-gen Jira projects

Click on **Project settings** on the left sidebar.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-1.png?w=1024)

On the **Project settings** page, click on **Apps** on the left sidebar.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-3.png?w=1024)

Click on **App fields** on the left sidebar and enable **LaTeX for Jira Cloud.**

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-14.png?w=1024)

Go back to the **Project settings** page, click on **Issue types** on the left sidebar.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-2.png?w=1024)

Drag the **LaTeX text** field from the right sidebar and drop it into the **Description fields** area.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-15.png?w=1024)

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-16.png?w=1024)

## Add LaTeX formulas to an issue

Click on the **Edit** button.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-17.png?w=1024)

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

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-18.png?w=1024)

After that, click **Save**.

![LaTeX for Jira](https://fulstech.files.wordpress.com/2020/09/image-19.png?w=1024)
