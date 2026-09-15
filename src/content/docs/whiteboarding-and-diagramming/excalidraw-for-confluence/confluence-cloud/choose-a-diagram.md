---
title: "Choose the right diagram macro"
description: "Choose between Excalidraw, Mermaid, Graphviz, PlantUML, Mind Map, BPMN, and DrawIO in Confluence Cloud."
---

Choose a macro based on how the diagram will be created and maintained. All
seven macros are included in the Confluence Cloud app.

| Macro | Choose it when | Editing model |
| --- | --- | --- |
| **Excalidraw Diagram** | You want a quick sketch, informal architecture diagram, UI wireframe, or whiteboard. | Draw shapes and edit text on a canvas. |
| **Mermaid UML Diagram** | You want a flowchart, sequence, class, state, ER, Gantt, or other diagram maintained as readable text. | Edit Mermaid source and check a preview. |
| **Graphviz Diagram** | You want a dependency graph or relationship map whose layout is calculated from DOT source. | Edit DOT source and check a preview. |
| **PlantUML Diagram** | You want UML or another PlantUML-supported diagram maintained as text. | Edit PlantUML source and check a preview. |
| **Mind Map** | You want to brainstorm topics and arrange them into a hierarchy. | Rename topics and add child or sibling branches. |
| **BPMN Diagram** | You want to model a business process with BPMN elements. | Place and connect process elements on a canvas. |
| **DrawIO Diagram (Powered by draw.io)** | You need a structured diagram and draw.io shape libraries. | Use the embedded draw.io editor. |

## A practical default

- Start with **Excalidraw Diagram** when the discussion matters more than formal
  notation.
- Start with **Mermaid UML Diagram** when reviewers should be able to inspect and
  copy the source.
- Use **BPMN Diagram** only when BPMN notation is meaningful to the audience; a
  BPMN drawing does not execute a workflow in Confluence.
- Use **DrawIO Diagram** when a canvas with extensive shape libraries is more
  useful than a hand-drawn style.

The macro names and basic purpose are shared by the current Connect app and the
Forge successor. Their editors and save flows differ. Use the
[Connect guide](../usage/) for the current Marketplace version or the
[Forge preview guide](../forge-preview/) only when your site has that preview.

## Data-handling choice

The diagram type can affect where content is processed. Review
[Connect permissions and data](../connect-permissions-and-data/) before putting
restricted information in a diagram. Forge preview participants should instead
read [Forge preview security and privacy](../security-and-privacy/).
