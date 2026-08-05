# Usage

## Mermaid UML Diagrams

> **Please make sure the Jira Server can connect to** [**https://app-nwtmwlxsha-uk.a.run.app**](https://app-nwtmwlxsha-uk.a.run.app/). **We use this Web Service to render the diagrams.**

This app renders Mermaid UML diagrams inside Jira Wiki Editor. The Mermaid UML content must be wrapped inside the **{uml}…{uml}** macro. **For Jira 7+, the macros have to be used in Text mode and not Visual mode**.

Mermaid (<https://mermaid-js.github.io/mermaid/#/>) allows you to define UML diagrams in plain-text format just like Markdown. For a live editor to draft your diagrams, please try <https://mermaidjs.github.io/mermaid-live-editor>.

As an example, after the app is installed, please paste the following text into Issue Description:

```
{uml}
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br />prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
{uml}
```

**For Jira 7+, the macros have to be used in Text mode and not Visual mode**.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-53b4a6a03e7d7940.png)

All Mermaid UML content will be rendered as below.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-9a44987ce0f8df77.png)

## Graphviz Diagrams

This app renders Graphviz diagrams inside Jira Wiki Editor. The Graphviz content must be wrapped inside the **{graphviz}…{graphviz}** macro. **For Jira 7+, the macros have to be used in Text mode and not Visual mode**.

As an example, after the app is installed, please paste the following text into Issue Description:

```
{graphviz}
graph {
  a -- b;
  b -- c;
  a -- c;
  d -- c;
  e -- c;
  e -- a;
}
{graphviz}
```

**For Jira 7+, the macros have to be used in Text mode and not Visual mode**.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-0d78c334a911ec10.png)

All Graphviz content will be rendered as below.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-027160122c7e45f5.png)

## Examples

### Flowchart

![Input](../../../assets/-MkUs_oJC5DKeT_xwaTh.png)

![Render](../../../assets/-MkUsTB67Zzejr2H4_ix.png)

### Sequence diagram

![Input](../../../assets/-MkUt7A6iSpie9PjLF-i.png)

![Render](../../../assets/-MkUtBY2X0MnGmhJKOLL.png)

### Class diagram

![Input](../../../assets/-MkUtPxZdjWnLtLgMDOa.png)

![Render](../../../assets/-MkUtUk8BHzvDUht9xnn.png)

### State diagram

![Input](../../../assets/-MkUufn7vwHI3fiuKHaA.png)

![Render](../../../assets/-MkUumhDeQZ2kQxTo1Fn.png)

### Entity Relationship diagram

![Input](../../../assets/-MkUvh77jxn3mARGgUs_.png)

![Render](../../../assets/-MkUvpdC914gXn4hqarl.png)

### User Journey

![Input](../../../assets/-MkUwDTjvsSHr9eax5Pj.png)

![Render](../../../assets/-MkUw2SBrfqtDtpA1qwA.png)

### Gantt chart

![Input](../../../assets/-MkUwPRZIOUt2hEouqs9.png)

![Render](../../../assets/-MkUxZGa1aXEX2ofWSzw.png)

### Pie chart

![Input](../../../assets/-MkUxi6MQEgwoEVhbI9_.png)

![Render](../../../assets/-MkUxneKvSlit2HRyFkX.png)

### Graphviz

![Input](../../../assets/-MkV-HNYNfQL2UGqPWwV.png)

![Render](../../../assets/-MkV-N7fwU-m-YhHdb6V.png)
