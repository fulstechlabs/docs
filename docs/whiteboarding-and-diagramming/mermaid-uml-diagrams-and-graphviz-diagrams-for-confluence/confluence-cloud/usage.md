# Usage

## Mermaid UML Diagrams Macro

The **Render Mermaid UML Diagrams** macro (<https://mermaid-js.github.io/mermaid/#/>) uses Mermaid to render UML diagrams. It allows you to define UML diagrams in plain-text format just like Markdown.

For a live editor to draft your diagrams, please try <https://mermaidjs.github.io/mermaid-live-editor>.

In the Confluence editor, open the **Select macro** dialog. The macro name is **Render Mermaid UML Diagrams**.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-MkUpZEJm9Cn79WVgL7I.png)

Alternatively, type / (**slash**) and select the macro.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-MkUouybkR0GsW4lQCVv.png)

A dialog will appear. Type the content of the UML diagram into the macro editor. Here is an example:

```
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
```

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-MkUq01ClfLhF74YdYPm.png)

While editing, you can click **Show preview** to see the result. You can also click **Full Screen Editor** to open the Mermaid editor that will help you design new diagrams easily.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-MkUqJQW_e_LTREul1YO.png)

Save the page, and the UML diagram will be rendered.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-Ma8B0xrAAYS-9ey9JHP.png)

## PlantUML Diagrams Macro

The **Render PlantUML Diagrams** macro (<https://plantuml.com/>) uses PlantUML to render UML diagrams. It allows you to define UML diagrams in plain-text format just like Markdown.

For a live editor to draft your diagrams, please try <http://www.plantuml.com/plantuml>.

In the Confluence editor, open the **Select macro** dialog. The macro name is **Render PlantUML Diagrams**.

![UML for Confluence](../../../assets/Ti6pFcpdlc0kJHe7hKMt.png)

A dialog will appear. Type the content of the UML diagram into the macro editor. Here is an example:

```plant-uml
@startuml C4_Elements
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

You can find more examples here <https://plantuml.com/>. The PDF guideline can be downloaded here <https://plantuml.com/guide>.

Save the macro, and the UML diagram will be rendered.

![UML for Confluence](../../../assets/8NO49SJWVu2QoK49sZqx.png)

## Graphviz Diagrams Macro

The Graphviz layout programs (<https://www.graphviz.org/>) take descriptions of graphs in a simple text language, and make diagrams in useful formats, such as images and SVG for web pages; PDF or Postscript for inclusion in other documents; or display in an interactive graph browser. Graphviz has many useful features for concrete diagrams, such as options for colors, fonts, tabular node layouts, line styles, hyperlinks, and custom shapes.

You can find more Graphviz examples [here](https://graphs.grevian.org/example).

In the Confluence editor, open the **Select macro** dialog. The macro name is **Render Graphviz Diagrams**.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-Ma8B0xsFOBsCzEQcLL-.png)

Select the macro, then click **Insert**.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-Ma8B0xtOXazZvZkfdcb.png)

Type the content of the Graphviz diagram into the macro editor. Here is an example:

```
graph {
  a -- b;
  b -- c;
  a -- c;
  d -- c;
  e -- c;
  e -- a;
}
```

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-Ma8B0xu2ad5digcTY4F.png)

Save the page, and the Graphviz diagram will be rendered.

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-Ma8B0xvqyiNeJmFxLfq.png)

## Examples

### Flowchart

Flowcharts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/flowchart>.

![Input](../../../assets/-MfRk3r-aZ5wr1KNon7F.png)

![Render](../../../assets/-MfRm7-zDyDMDPaGRBU4.png)

### Sequence diagram

Sequence diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/sequenceDiagram>.

![Input](../../../assets/-MfRkuCcrDHX912SRYh-.png)

![Render](../../../assets/-MfRmf6Yp0CIrgp0v1iN.png)

### Class diagram

Class diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/classDiagram>.

![Input](../../../assets/-MfRn3mlJrz1YqR05FCh.png)

![Render](../../../assets/-MfRnPR5JDnBDLWJvXg1.png)

### State diagram

State diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/stateDiagram>.

![Input](../../../assets/-MfRp3169SHX4uJdp1Yc.png)

![Render](../../../assets/-MfRpBynG2viGNz43rej.png)

### Entity Relationship diagram

Entity Relationship diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram>.

![Input](../../../assets/-MfRpqQjT8zOQQf8Q3nk.png)

![Render](../../../assets/-MfRpwIKfFDyRigQSJtG.png)

### User Journey

User Journey can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/user-journey>.

![Render](../../../assets/-MfRqQFLOuW7X7WTD9sp.png)

![Input](../../../assets/-MfRqXGELy3h4DHIgEZr.png)

### Gantt chart

Gantt charts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/gantt>.

![Input](../../../assets/-MfRrtD1vjpuuDNkExc4.png)

![Render](../../../assets/-MfRrxiC78rgOrLGKNrA.png)

### Pie chart

Pie charts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/pie>.

![Input](../../../assets/-MfRsgjEHSnhzr0UTnqv.png)

![Render](../../../assets/-MfRsyf_O8ESY4dlkk2Z.png)

### Graphviz

This diagram is rendered with Graphviz.

![Input](../../../assets/-MfS1gUzu9gFC53VoOAz.png)

![Render](../../../assets/-MfS26jOEd1zEFuyuxWj.png)
