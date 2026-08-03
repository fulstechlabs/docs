# Usage

## Excalidraw

### Insert Excalidraw drawings

Select the **Excalidraw** macro from the macro list.

![Excalidraw for Confluence](../../../assets/vCFqNcvoF1yY8IKfcvpx.png)

Click on the macro placeholder, and click **Edit**.

![Excalidraw for Confluence](../../../assets/u3NQLDpGZKTKOZDMud7i.png)

Draw anything you want. To draw perfect shapes like a circle, hold the **Shift** button while drawing.

![Excalidraw for Confluence](../../../assets/Jq9uxKXRlgyitIM17qGG.png)

Click **Save and Close**. If you don't want to save the changes, click the **X** button on the top right corner.

![Excalidraw for Confluence](../../../assets/sWdavP0gFrMrupEC7qnq.png)

### Adding new shapes from the Excalidraw Libraries website

The Excalidraw Libraries website (<https://libraries.excalidraw.com>) provides a lot of useful shapes. These shapes are contributed by the community.

To add new shapes, visit the website and click the **Download** button to save the collection you need to your computer. The downloaded library file's extension is `.excalidrawlib`.

> **Do not use the Add to Excalidraw button, as the library will not be added to the plugin-hosted Excalidraw Editor.**

![Excalidraw for Confluence](../../../assets/pH9arHH9Q1TmNWVFAUNk.png)

Open the Excalidraw Editor in Confluence, and upload the library file.

![Excalidraw for Confluence](../../../assets/iH0Cvqaj3k6X3XcJDulI.png)

You can then drag and drop shapes into the canvas.

![Excalidraw for Confluence](../../../assets/kVfQCbnwNcqGvhpApOF0.png)

### Adding shapes to library

To add a shape to library, select the shape, right-click on it, and click **Add to Library**.

![Excalidraw for Confluence](../../../assets/dL9IxsoT3eWtmkIdEGZP.png)

![Excalidraw for Confluence](../../../assets/QLEBPYAdGVKCe7IBnu4I.png)

To save your shapes library locally (e.g. for backup purposes), select the shape in the library panel, and click **Save to** in the menu.

![Excalidraw for Confluence](../../../assets/pd7bx8aqcGFaTLWvk7xm.png)

![Excalidraw for Confluence](../../../assets/3o6PFPf6A3eRnn335Hwd.png)

## Mermaid UML Diagrams Macro

The **Render Mermaid UML Diagrams** macro (<https://mermaid-js.github.io/mermaid/#/>) uses Mermaid to render UML diagrams. It allows you to define UML diagrams in plain-text format just like Markdown.

For a live editor to draft your diagrams, please try <https://mermaidjs.github.io/mermaid-live-editor>.

In the Confluence editor, insert the **Mermaid UML** macro.

![](../../../assets/pP85CKRT4Vn60w5f8Xje.png)

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

![Excalidraw for Confluence](../../../assets/XYTuNNRAEkmGDUxkBvjn.png)

![Mermaid UML Diagrams and Graphviz Diagrams for Confluence Cloud](../../../assets/-Ma8B0sd9DO6Y8VRI6th.png)

## PlantUML Diagrams Macro

The **PlantUML** macro (<https://plantuml.com/>) uses PlantUML to render UML diagrams. It allows you to define UML diagrams in plain-text format just like Markdown.

For a live editor to draft your diagrams, please try <http://www.plantuml.com/plantuml>.

In the Confluence editor, insert the **PlantUML** macro.

![Excalidraw for Confluence](../../../assets/Fxg2ryKaxuWgw7eh0ux3.png)

Type the content of the UML diagram into the macro editor.

> **info**
>
Some PlantUML diagrams requires **Graphviz** to be installed in the Confluence server <https://plantuml.com/graphviz-dot>. If you cannot install **Graphviz**, try adding `!pragma layout smetana` to the diagram content to enable the Smetana engine <https://plantuml.com/smetana02>.

Here is an example:

```plant-uml
@startuml C4_Elements
!pragma layout smetana
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

![Excalidraw for Confluence](../../../assets/1rN9xUC5kRsujQcP8hnq.png)

You can find more examples here <https://plantuml.com/>. The PDF guideline can be downloaded here <https://plantuml.com/guide>.

## Graphviz Diagrams Macro

The Graphviz layout programs (<https://www.graphviz.org/>) take descriptions of graphs in a simple text language, and make diagrams in useful formats, such as images and SVG for web pages; PDF or Postscript for inclusion in other documents; or display in an interactive graph browser. Graphviz has many useful features for concrete diagrams, such as options for colors, fonts, tabular node layouts, line styles, hyperlinks, and custom shapes.

You can find more Graphviz examples [here](https://graphs.grevian.org/example).

In the Confluence editor, insert the **Graphviz** macro.

![Excalidraw for Confluence](../../../assets/Bkf4G5Vvuu2RTZd62jDn.png)

Type the content of the Graphviz diagram into the macro editor. Here is an example:

```dot
graph {
  a -- b;
  b -- c;
  a -- c;
  d -- c;
  e -- c;
  e -- a;
}
```

![Excalidraw for Confluence](../../../assets/psnsAVrUtp4T5DtgQJYI.png)

## Examples

### Mermaid

#### Flowchart

Flowcharts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/flowchart>.

![Input](../../../assets/-MfRk3r-aZ5wr1KNon7F.png)

![Render](../../../assets/-MfRm7-zDyDMDPaGRBU4.png)

#### Sequence diagram

Sequence diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/sequenceDiagram>.

![Input](../../../assets/-MfRkuCcrDHX912SRYh-.png)

![Render](../../../assets/-MfRmf6Yp0CIrgp0v1iN.png)

#### Class diagram

Class diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/classDiagram>.

![Input](../../../assets/-MfRn3mlJrz1YqR05FCh.png)

![Render](../../../assets/-MfRnPR5JDnBDLWJvXg1.png)

#### State diagram

State diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/stateDiagram>.

![Input](../../../assets/-MfRp3169SHX4uJdp1Yc.png)

![Render](../../../assets/-MfRpBynG2viGNz43rej.png)

#### Entity Relationship diagram

Entity Relationship diagrams can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram>.

![Input](../../../assets/-MfRpqQjT8zOQQf8Q3nk.png)

![Render](../../../assets/-MfRpwIKfFDyRigQSJtG.png)

#### User Journey

User Journey can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/user-journey>.

![Render](../../../assets/-MfRqQFLOuW7X7WTD9sp.png)

![Input](../../../assets/-MfRqXGELy3h4DHIgEZr.png)

#### Gantt chart

Gantt charts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/gantt>.

![Input](../../../assets/-MfRrtD1vjpuuDNkExc4.png)

![Render](../../../assets/-MfRrxiC78rgOrLGKNrA.png)

#### Pie chart

Pie charts can be rendered with Mermaid. See more <https://mermaid-js.github.io/mermaid/#/pie>.

![Input](../../../assets/-MfRsoBc46muewkcNbc_.png)

![Render](../../../assets/-MfRsyf_O8ESY4dlkk2Z.png)

### Graphviz

This diagram is rendered with Graphviz.

![Input](../../../assets/-MfS1gUzu9gFC53VoOAz.png)

![Render](../../../assets/-MfS26jOEd1zEFuyuxWj.png)

### PlantUML

#### Sequence diagram

```plant-uml
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
@enduml
```

![](../../../assets/BzCpuj0JJXQCp9DyAzsB.png)

#### Use Case diagram

```plant-uml
@startuml
!pragma layout smetana
left to right direction
actor Guest as g
package Professional {
    actor Chef as c
    actor "Food Critic" as fc
}
package Restaurant {
    usecase "Eat Food" as UC1
    usecase "Pay for Food" as UC2
    usecase "Drink" as UC3
    usecase "Review" as UC4
}
fc --> UC4
g --> UC1
g --> UC2
g --> UC3
@enduml
```

![](../../../assets/4RkJiLZpmk4vG7JxPXCY.png)

#### Class diagram

```plant-uml
@startuml
!pragma layout smetana
Object <|-- ArrayList
Object : equals()
ArrayList : Object[] elementData
ArrayList : size()
@enduml
```

![](../../../assets/esFAsAhIsrF5ofw0pvlq.png)

#### Activity diagram

```plant-uml
@startuml
start
repeat
    :read data;
    :generate diagrams;
repeat while (more data?) is (yes)
->no;
stop
@enduml
```

![](../../../assets/LtYfO4TEXlZIdWAYP7Op.png)

#### Component diagram

```plant-uml
@startuml
!pragma layout smetana
package "Some Group" {
  HTTP - [First Component]
  [Another Component]
}
node "Other Groups" {
  FTP - [Second Component]
  [First Component] --> FTP
}
cloud {
  [Example 1]
}
database "MySql" {
  folder "This is my folder" {
    [Folder 3]
  }
  frame "Foo" {
    [Frame 4]
  }
}
[Another Component] --> [Example 1]
[Example 1] --> [Folder 3]
[Folder 3] --> [Frame 4]
@enduml
```

![](../../../assets/R0VFj9xIne5U5YkaJWu4.png)

#### Deployment diagram

```plant-uml
@startuml
!pragma layout smetana
node node1
node node2
node node3
node node4
node node5
node1 -- node2 : label1
node1 .. node3 : label2
node1 ~~ node4 : label3
node1 == node5
@enduml
```

![](../../../assets/EjHJxbc116V0wMZDr1GM.png)

#### State diagram

```plant-uml
@startuml
!pragma layout smetana
scale 350 width
[*] --> NotShooting
state NotShooting {
  [*] --> Idle
  Idle --> Configuring : EvConfig
  Configuring --> Idle : EvConfig
}
state Configuring {
  [*] --> NewValueSelection
  NewValueSelection --> NewValuePreview : EvNewValue
  NewValuePreview --> NewValueSelection : EvNewValueRejected
  NewValuePreview --> NewValueSelection : EvNewValueSaved
  state NewValuePreview {
    State1 -> State2
  }
}
@enduml
```

![](../../../assets/1f6yeFkSU4uVGyVH1O7W.png)

#### Timing diagram

```plant-uml
@startuml
robust "Web Browser" as WB
concise "Web User" as WU
@0
WU is Idle
WB is Idle
@100
WU is Waiting
WB is Processing
@300
WB is Waiting
@enduml
```

![](../../../assets/uYCBars88dYrPg58PtIl.png)

#### JSON

```plant-uml
@startjson
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}
@endjson
```

![](../../../assets/u2WBPufs4sSABRnZQVvw.png)

#### Mindmap

```plant-uml
@startmindmap
* Class Templates
**:Example 1
<code>
template <typename T>
class cname{
void f1()<U+003B>
...
}
</code>
;
**:Example 2
<code>
other template <typename T>
class cname{
...
</code>
;
@endmindmap
```

![](../../../assets/63NIaJdmiBvt7sQ6yNsX.png)

#### Work Breakdown Structure

```plant-uml
@startwbs
* Business Process Modelling WBS
** Launch the project
*** Complete Stakeholder Research
*** Initial Implementation Plan
** Design phase
*** Model of AsIs Processes Completed
**** Model of AsIs Processes Completed1
**** Model of AsIs Processes Completed2
*** Measure AsIs performance metrics
*** Identify Quick Wins
** Complete innovate phase
@endwbs
```

![](../../../assets/m7uYJ02VdLKmxx3ar7KZ.png)

#### Entity Relationship diagram

```plant-uml
@startuml
!pragma layout smetana
' hide the spot
hide circle
' avoid problems with angled crows feet
skinparam linetype ortho
entity "Entity01" as e01 {
  *e1_id : number <<generated>>
  --
  *name : text
  description : text
}
entity "Entity02" as e02 {
  *e2_id : number <<generated>>
  --
  *e1_id : number <<FK>>
  other_details : text
}
entity "Entity03" as e03 {
  *e3_id : number <<generated>>
  --
  e1_id : number <<FK>>
  other_details : text
}
e01 ||..o{ e02
e01 |o..o{ e03
@enduml
```

![](../../../assets/zSDrjcG3pIaIhX6BCryU.png)

#### C4 diagram

```plant-uml
@startuml
!pragma layout smetana
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
' uncomment the following line and comment the first to use locally
' !include C4_Container.puml

' LAYOUT_TOP_DOWN()
' LAYOUT_AS_SKETCH()
LAYOUT_WITH_LEGEND()

title Container diagram for Internet Banking System

Person(customer, Customer, "A customer of the bank, with personal bank accounts")

System_Boundary(c1, "Internet Banking") {
    Container(web_app, "Web Application", "Java, Spring MVC", "Delivers the static content and the Internet banking SPA")
    Container(spa, "Single-Page App", "JavaScript, Angular", "Provides all the Internet banking functionality to cutomers via their web browser")
    Container(mobile_app, "Mobile App", "C#, Xamarin", "Provides a limited subset of the Internet banking functionality to customers via their mobile device")
    ContainerDb(database, "Database", "SQL Database", "Stores user registration information, hashed auth credentials, access logs, etc.")
    Container(backend_api, "API Application", "Java, Docker Container", "Provides Internet banking functionality via API")
}

System_Ext(email_system, "E-Mail System", "The internal Microsoft Exchange system")
System_Ext(banking_system, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

Rel(customer, web_app, "Uses", "HTTPS")
Rel(customer, spa, "Uses", "HTTPS")
Rel(customer, mobile_app, "Uses")

Rel_Neighbor(web_app, spa, "Delivers")
Rel(spa, backend_api, "Uses", "async, JSON/HTTPS")
Rel(mobile_app, backend_api, "Uses", "async, JSON/HTTPS")
Rel_Back_Neighbor(database, backend_api, "Reads from and writes to", "sync, JDBC")

Rel_Back(customer, email_system, "Sends e-mails to")
Rel_Back(email_system, backend_api, "Sends e-mails using", "sync, SMTP")
Rel_Neighbor(backend_api, banking_system, "Uses", "sync/async, XML/HTTPS")
@endumlplan
```

![](../../../assets/LUsE7LSgZZSGRUdgWX6w.png)

#### AWS architecture diagram

```plant-uml
@startuml S3 Upload Workflow
!pragma layout smetana
'Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'SPDX-License-Identifier: MIT (For details, see https://github.com/awslabs/aws-icons-for-plantuml/blob/master/LICENSE)

!define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/v15.0/dist
!include AWSPuml/AWSCommon.puml
!include AWSPuml/AWSExperimental.puml
!include AWSPuml/Groups/all.puml
!include AWSPuml/Compute/LambdaLambdaFunction.puml
!include AWSPuml/General/Documents.puml
!include AWSPuml/General/Multimedia.puml
!include AWSPuml/General/Tapestorage.puml
!include AWSPuml/General/User.puml
!include AWSPuml/MediaServices/ElementalMediaConvert.puml
!include AWSPuml/MachineLearning/Transcribe.puml
!include AWSPuml/Storage/SimpleStorageService.puml

' define custom group for Amazon S3 bucket
AWSGroupColoring(S3BucketGroup, #FFFFFF, AWS_COLOR_GREEN, plain)
!define S3BucketGroup(g_alias, g_label="Amazon S3 bucket") AWSGroupEntity(g_alias, g_label, AWS_COLOR_GREEN, SimpleStorageService, S3BucketGroup)

' Groups are rectangles with a custom style using stereotype - need to hide
hide stereotype
skinparam linetype ortho
skinparam rectangle {
    BackgroundColor AWS_BG_COLOR
    BorderColor transparent
}

rectangle "$UserIMG()\nUser" as user
AWSCloudGroup(cloud){
  RegionGroup(region) {
    S3BucketGroup(s3) {
      rectangle "$MultimediaIMG()\n\tvideo\t" as video
      rectangle "$TapestorageIMG()\n\taudio\t" as audio
      rectangle "$DocumentsIMG()\n\ttranscript\t" as transcript

      user -r-> video: <$Callout_1>\lupload
      video -r-> audio
      audio -r-> transcript
    }

    rectangle "$LambdaLambdaFunctionIMG()\nObjectCreated\nevent handler" as e1
    rectangle "$ElementalMediaConvertIMG()\nAWS Elemental\nMediaConvert" as mediaconvert
    rectangle "$TranscribeIMG()\nAmazon Transcribe\n" as transcribe

    video -d-> e1: <$Callout_2>
    e1 -[hidden]r-> mediaconvert
    mediaconvert -[hidden]r-> transcribe
    mediaconvert -u-> audio: <$Callout_3>
    transcribe -u-> transcript: <$Callout_4>

    StepFunctionsWorkflowGroup(sfw) {
      rectangle "$LambdaLambdaFunctionIMG()\nextract audio" as sfw1
      rectangle "$LambdaLambdaFunctionIMG()\ntranscribe audio" as sfw2

      e1 -r-> sfw1: Start\nExecution
      sfw1 -r-> sfw2
      sfw1 -u-> mediaconvert
      sfw2 -u-> transcribe
    }
  }
}

@enduml
```

![](../../../assets/t0sW5tFqKW68QBFd99VG.png)
