---
title: "Choose the right diagram macro"
description: "Choose between Excalidraw, Mermaid, Graphviz, PlantUML, Mind Map, BPMN, and DrawIO in Confluence Cloud."
---

Choose based on how people will create, review, and maintain the diagram. All
seven macros are included in the Confluence Cloud app.

## Start with the editing model

- Choose a **visual canvas** when people should work with shapes and direct
  manipulation.
- Choose a **text-defined diagram** when the source should be readable, copied,
  or reviewed alongside the result.

| Macro | Choose it when | Editing model |
| --- | --- | --- |
| **Excalidraw Diagram** | You want a quick sketch, informal architecture diagram, UI wireframe, or whiteboard. | Draw shapes and edit text on a canvas. |
| **Mermaid UML Diagram** | You want a flowchart, sequence, class, state, ER, Gantt, or other diagram maintained as readable text. | Edit Mermaid source and check a preview. |
| **Graphviz Diagram** | You want a dependency graph or relationship map whose layout is calculated from DOT source. | Edit DOT source and check a preview. |
| **PlantUML Diagram** | You want UML or another PlantUML-supported diagram maintained as text. | Edit PlantUML source and check a preview. |
| **Mind Map** | You want to brainstorm topics and arrange them into a hierarchy. | Rename topics and add child or sibling branches. |
| **BPMN Diagram** | You want to model a business process with BPMN elements. | Place and connect process elements on a canvas. |
| **DrawIO Diagram (Powered by draw.io)** | You need a structured diagram and draw.io shape libraries. | Use the embedded draw.io editor. |

## Practical defaults

- Start with **Excalidraw Diagram** when the discussion matters more than formal
  notation.
- Start with **Mermaid UML Diagram** when reviewers should be able to inspect and
  copy the source.
- Use **BPMN Diagram** only when BPMN notation is meaningful to the audience; a
  BPMN drawing does not execute a workflow in Confluence.
- Use **DrawIO Diagram** when a canvas with extensive shape libraries is more
  useful than a hand-drawn style.

## Continue with your diagram

- For Excalidraw, Mind Map, BPMN, or DrawIO, follow
  [Create and edit canvas diagrams](../canvas-diagrams/).
- For Mermaid, Graphviz, or PlantUML, follow
  [Create diagrams from text](../text-diagrams/).
- For advanced editor controls, open the
  [Cloud feature reference](../forge-preview/).
- If you are editing a diagram created before the Forge upgrade, follow
  [Existing Connect diagrams](../forge-preview/#existing-connect-diagrams)
  before the first save.

If your site still shows a separate **Open Editor** step, use the
[legacy Connect guide](../usage/). The macro names are similar, but the editors
and save flows differ.
