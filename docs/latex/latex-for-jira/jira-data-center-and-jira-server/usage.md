# Usage

This app renders LaTeX anywhere inside Jira– even in Issue Summary. The syntax is very simple.

![LaTeX for Jira](../../../assets/-MfGf9LV3wp36DJXfxDv.png)

## Activate the app

The app only works after the license has been activated. If a license has not been purchased, please activate the trial mode <https://confluence.atlassian.com/jirakb/how-to-generate-evaluation-licenses-for-jira-apps-1021233084.html>.

## Syntax in Atlassian Wiki fields

### Inline LaTeX content

To insert LaTeX content into Atlassian Wiki editors such as Description or Comment in inline mode:

* Select the **Text** mode (you must make sure ithe editor is not in **Visual** mode.
* Wrap the content inside the `{latex-inline}...{latex-inline}` macro.
* You can go back to **Visual** mode to type other content after that.

```
{latex-inline}e = mc^2{latex-inline}
```

![LaTeX for Jira](../../../assets/4E8qKb9A1m3VgUjQPach.png)

![LaTeX for Jira](../../../assets/LkBOGAypQEIFs16aGyad.png)

### Block LaTeX content

To insert LaTeX content into Atlassian Wiki editors such as Description or Comment in block mode:

* Select the **Text** mode (you must make sure ithe editor is not in **Visual** mode.
* Wrap the content inside the `{latex-block}...{latex-block}` macro.
* You can go back to **Visual** mode to type other content after that.

```
{latex-block}e = mc^2{latex-block}
```

![LaTeX for Jira](../../../assets/I9TgcSJhxWdrBN6kceqe.png)

![LaTeX for Jira](../../../assets/bVVI6wrzKSFv2Cp0hL63.png)

### Complex LaTeX content

Sometimes the symbols in complex LaTeX content can be misinterpreted by Atlassian Wiki as formatting syntax. To type such complex LaTeX content:

* You can go back to **Visual** mode to type other content after that.
* Wrap the content inside the `{noformat}//[...//]{noformat}` macro.
* Select the **Text** mode (you must make sure ithe editor is not in **Visual** mode.

```
{noformat}//[
\begin{align*}
a^2 + b^2 &= c^2, \\
e^{i\pi} + 1 &= 0, \\
\int_0^\infty e^{-x} \, dx &= 1.
\end{align*}
//]{noformat}
```

![LaTeX for Jira](../../../assets/7ZLVwBwVYeGuT0fWd3kL.png)

![LaTeX for Jira](../../../assets/2YE5oRDKWiE1anS4TIeN.png)

### Examples

#### Description

![Input](../../../assets/-MfGffJxCmPRQsu5ZQll.png)

![Render](../../../assets/-MfH8_MuYaekwoT9BOiR.png)

![Input](../../../assets/-MfHs-ULY-iCTrZ6sqo6.png)

![Render](../../../assets/-MfHs6mFKF__cG6pwJvE.png)

#### Comment

![Input](../../../assets/-MfHCDvCW3EOvmdLP6OG.png)

![Render](../../../assets/-MfHFrJoaatoAkkSLJyt.png)

![Input](../../../assets/-MfHsFgPpfLT-KyyNlPq.png)

![Render](../../../assets/-MfHsfuHl4PfgrbNAXyG.png)

## Syntax in plain-text fields

For plain-text fields like Summary, inline LaTeX must be wrapped inside `//(...//)` and LaTeX block must be wrapped inside `//[...//]`.

### Examples

#### Summary

![Input](../../../assets/-MfHGbtZz6DFreT_xSmM.png)

![Render](../../../assets/-MfHHAI48RM_sKpjOZce.png)

#### Text Field (multi-line)

![Input](../../../assets/-MfHICchU71eJwrxvmdA.png)

![Render](../../../assets/-MfHIKi9FDzAgN23i7Yd.png)

#### Text Field (single line)

![Input](../../../assets/-MfHIWyk5ex4bXQsLmyb.png)

![Render](../../../assets/-MfHIcLjlJ1JZWfz2SeK.png)
