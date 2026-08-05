---
title: "Usage"
---

After installing and starting the trial period, the app will add a custom field name **UML text** to the Jira instance.

The first step is to add the custom field **UML text** to issue types and projects.

## For classic Jira projects

### Associate the UML field to issue screens

Navigate to the **Custom fields** page.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-7e926d1490e4a36b.png)

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-bfd05a7f64382c75.png)

Search for the custom field **UML text** and add it to screens.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-b0a191fcf0984cab.png)

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-8d5bb2f308486cd8.png)

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-3534dd1ba03d23c8.png)

### Add the **UML** panel to the issue screen

On an issue view, click on the “three dots” icon and select **UML Diagrams**.

## **For Next-gen Jira project**

Click on **Project settings** on the left sidebar.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-99523016357c1eee.png)

On the **Project settings** page, click on **Apps** on the left sidebar.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-f475cc2761077474.png)

Click on **App fields** on the left sidebar and enable **Mermaid UML for Jira Cloud.**

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-fda5b389cff74146.png)

Go back to the **Project settings** page, click on **Issue types** on the left sidebar.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-a14893461410b900.png)

Drag the **UML text** field from the right sidebar and drop it into the **Description fields** area.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-04cc620f563068cf.png)

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-cbf1db6580561180.png)

## Add Mermaid UML graphs to an issue

Click on the **Edit** button.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-e613d4580ef97061.png)

**Please do not edit the custom field itself. Whenever you want to add or modify graphs, please use the app’s Edit button.**

The UML content is wrapped around by **{uml}…{uml}**. The diagram is defined using Mermaid. Mermaid (<https://mermaid-js.github.io/mermaid/#/>) allows you to define UML diagrams in plain-text format just like Markdown. For a live editor to draft your diagrams, please try <https://mermaidjs.github.io/mermaid-live-editor>.

Sample content:

```
{uml}
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
{uml}

{uml}
gantt
dateFormat  YYYY-MM-DD
excludes weekdays 2014-01-10

section A section
Completed task            :done,    des1, 2014-01-06,2014-01-08
Active task               :active,  des2, 2014-01-09, 3d
Future task               :         des3, after des2, 5d
Future task2               :         des4, after des3, 5d
{uml}
```

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-c5ca908d85136345.png)

After that, click **Save**.

![Mermaid UML Diagrams and Graphviz Diagrams for Jira](../../../assets/external-2a34e9ff33930f35.png)

## Examples

### Flowchart

Flowcharts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/flowchart>.

![Input](../../../assets/-MhIdeP_9qwFFjMXGLyu.png)

![Render](../../../assets/-MhIdjq-fl2RZxqDtmu7.png)

### Sequence diagram

Sequence diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/sequenceDiagram>.

![Input](../../../assets/-MhIe4Un8Eo3hWoWYYX4.png)

![Render](../../../assets/-MhIeD_QK-LvhMteP_Fj.png)

### Class diagram

Class diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/classDiagram>.

![Input](../../../assets/-MhIeWswsa5-7FqR3c0z.png)

![Render](../../../assets/-MhIeauFRKF8tHym5HLL.png)

### State diagram

State diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/stateDiagram>.

![Input](../../../assets/-MhIeq24gHrmQE9_v0ZY.png)

![Render](../../../assets/-MhIeua2A220VI3jfw7H.png)

### User Journey

User Journey can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/user-journey>.

![Input](../../../assets/-MhIhPIxr6ELAF866lj7.png)

![Render](../../../assets/-MhIhW7GCNPtPnK9GAv7.png)

### Gantt chart

Gantt charts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/gantt>.

![Input](../../../assets/-MhIgxkKyCrWsrPHevPU.png)

![Render](../../../assets/-MhIh1WjWk0ouUTnz2iD.png)

### Piechart

Pie charts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/pie>.

![Input](../../../assets/-MhIhhjFRsa0Yx2RByY5.png)

![Render](../../../assets/-MhIhmqtL_cy-dt981v5.png)
