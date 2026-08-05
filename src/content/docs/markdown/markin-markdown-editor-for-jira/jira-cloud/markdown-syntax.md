---
title: "Markdown Syntax"
---

## Overview

![Markdown for Jira](../../../assets/-Ma8B10HXqr1ay8bB3me.png)

## Autocompletion

You can get a list of all available syntax by pressing `Ctrl + Space` in the editor. A context menu with all available syntax will appear.

![Markdown for Jira](../../../assets/AHfBNWlfYGyglt1IyVUj.png)

To move between items, use `Up`, `Down`, `Left`, `Right` keys. To select an item, click on it or press `Enter`. An example will be inserted.

![Markdown for Jira](../../../assets/okEsf4E6DDnmViMTWYkY.png)

## LaTeX Math formulas

### Block formulas

```latex
\\[ax^2 + bx + c = 0\\]
```

![Render](../../../assets/-Mf7VKN4Z4OSw1QEtUuK.png)

### Inline formulas

```latex
\\(x = {-b \pm \sqrt{b^2-4ac} \over 2a}\\)
```

![Render](../../../assets/-Mf7VQcp4jawAlyeqmlK.png)

## Sequence diagrams

Learn more about the syntax here: <https://bramp.github.io/js-sequence-diagrams>.

````markdown
:::sequence
```
User->Phone: Says Hello
Note right of Phone: Phone thinks\nabout it
Phone->User: How are you?
User->>Phone: I am good thanks!
```
:::
````

![Render](../../../assets/-Mf7SoOdiDAPGOvqBmZG.png)

## Graphviz diagrams

Learn more about the syntax (Graphviz DOT) here: <http://www.graphviz.org/>.

````dot
:::graphviz
```
digraph site {
    home [label = "Home"];
    prod [label = "Products"];
    news [label = "News"];
    cont [label = "Contact"];

    home -> {prod news cont}
}
```
:::
````

![Render](../../../assets/-Mf7SVEtdfEEnODHuLba.png)

## Mermaid UML diagrams

Learn more about Mermaid UML diagrams here: <https://mermaid-js.github.io/mermaid/#/>.

Here we are just showing some examples.

### State diagrams

````mermaid
:::uml
```
stateDiagram
        [*] --> Still
        Still --> [*]
        Still --> Moving
        Moving --> Still
        Moving --> Crash
        Crash --> [*]
```
:::
````

![Render](../../../assets/-Mf7TWSY74w0jinQF_tH.png)

### Sequence diagrams

````mermaid
:::uml
```
sequenceDiagram
    autonumber
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```
:::
````

![Render](../../../assets/-Mf7Tcbae4QJzYGm7C1s.png)

### Class diagrams

````mermaid
:::uml
```
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
Class08 <--> C2: Cool label
```
:::
````

![Render](../../../assets/-Mf7TqC54hIhF7MCKKm-.png)

## Markdown syntax

### Heading

```markdown
# The largest heading
## The second largest heading
###### The smallest heading
```

![Result](../../../assets/-Mf2kpT6s1VweTu6rzC9.png)

### Styling text

```markdown
**bold**

*italic*

~~Strikethrough~~
```

![Render](../../../assets/-Mf2lMBRLjGiHJ1fnnBm.png)

### Lists

```markdown
* Item 1
* Item 2

1. Item 1
2. Item 2
```

![Render](../../../assets/-Mf2lff-KY3v7RGQs-V5.png)

### Task lists

```markdown
- [x] this is a complete item
- [ ] this is an incomplete item
```

![](../../../assets/-Mf2m6D0HC1hxW5l3ocI.png)

### Using emoji

```markdown
:) :D
```

![Render](../../../assets/-Mf2mO993Gva3CiaHgJu.png)

### Mentioning people <a href="#mentioning-people" id="mentioning-people"></a>

Type `@` and select the user to be mentioned.

![](../../../assets/remote-1c17d6c00f6cb6a0.png)Input

![](../../../assets/remote-78843caf54ebf61f.png)Render

### Inserting attachments as images <a href="#inserting-attachments-as-images" id="inserting-attachments-as-images"></a>

Type `@@` and select the attachment to be inserted.

![](../../../assets/remote-8bf5461accf4f29b.png)

### Images

```markdown
![Markdown Logo (Source: Wikipedia)](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
```

![Render](../../../assets/-Mf2nEOcCnu-YkdMfpg4.png)

### Links

```markdown
[Markin](https://marketplace.atlassian.com/plugins/com.fulstech.jira-gherkin-custom-field/server/overview)
```

![Render](../../../assets/-Mf2ok4GPY4HlRA71D1Y.png)

### Code snippets

````markdown
`inline code`

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:"#foo"})
  }
}
```
````

![Render](../../../assets/-Mf2p286-cffg5AXRmPo.png)

### Quote blocks

```markdown
As Eleanor Roosevelt said:
> You must do the thing you think you cannot do.
```

![Render](../../../assets/-Mf2pKDswmfduGi4Tj4Z.png)

### Tables

```markdown
| First Header | Second Header |
| - | - |
| Content from cell 1 | Content from cell 2 |
| Content in the first column | Content in the second column |
```

![Render](../../../assets/-Mf2pfbBE9tmVd8BTEz7.png)

## Gherkin syntax

> **Please enable Gherkin syntax first before using this feature.**

```gherkin
Scenario Outline: Password should be secure enough

Given a new password is being set
When I try to set the password to <new password>
Then the password should be considered <secure?>

Examples:
| new password | secure? | notes                  |
| -            | -       | -                      |
| p@swrd1;     | :(      | No uppercase character |
| Passwrd1     | :(      | No special character   |
| P@swrdl;     | :)      | -                      |
```

![Render](../../../assets/-Mf7Xn34A2zgO3-IFJiT.png)
