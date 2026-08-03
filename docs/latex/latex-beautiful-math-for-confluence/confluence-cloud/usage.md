# Usage

Two types of LaTeX content

This app supports two types of LaTeX content. Simple content such as `e = mc^2` will be rendered by MathJax engine, and more complex content that uses packages such as `tikz` or `chemfig` will be rendered by TeX Live engine.

## Insert macros

In the article editor, click the **Insert** button, and select **View more** from the list.

![LaTeX for Confluence](../../../assets/Jk4dqJSIymSWhhN878Mk.png)

In the **Select macro** dialog, search for "**latex"**.

![LaTeX for Confluence](../../../assets/BDahKdOUXlcEY9ydSIE9.png)

Alternatively, type **/ (slash)** and select the LaTeX macros.

![LaTeX for Cònluence](../../../assets/kCQFkom6xbYXA3Io61cU.png)

## Insert simple LaTeX content (MathJax engine)

To insert simple LaTeX content please use the following macros:

* **Render LaTeX content inline**
* **Render LaTeX content as block**

These macros use MathJax engine to render content. The content is as simple as `e=mc2` and does not require LaTeX preambles.

The editor dialog allow users to type the LaTeX content and preview the result instantly. Errors will be highlighted in red color.

![LaTeX for Confluence](../../../assets/GZrvIfpG0DsC5BmG35ht.png)

You can open the **Math Keyboard** by clicking on the keyboard icon in the right-hand corner of the Math Editor preview area. For block content, you can also specify the alignment as left, right, center. To close the editor, click **Apply** or **Cancel** button in the top right corner.

![LaTeX for Confluence](../../../assets/AtViAiOIGoR0tsxcVDaZ.png)

Click **Save** to apply the macro. Then click **Publish** to save the article.

![LaTeX for Confluence](../../../assets/ursIu9AGrzGKfFTOgmWI.png)

The article with LaTeX content will then be rendered.

![LaTeX for Confluence](../../../assets/xlKJrtlP05WoSuAew7WK.png)

## Insert complex LaTeX content (TeX Live engine)

Sometimes you need to render complex LaTeX content such as the following one

```latex
\documentclass{article}
\pagestyle{empty}
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}
\addplot3[
    surf,
]
{exp(-x^2-y^2)*x};
\end{axis}
\end{tikzpicture}
\end{document}
```

which will be rendered as

![LaTeX for Confluence](../../../assets/0XAdvlGTAlDaSJG0GZ9q.png)

In this case, please make use of the following macros:

* **(Advanced) Render complex LaTeX content inline using TeX Live engine**
* **(Advanced) Render complex LaTeX content as block using TeX Live engine**

The editor dialog allow users to type the LaTeX content and preview the result instantly. Errors will be highlighted in red color. For block content, you can also specify the alignment as left, right, center.

![LaTeX for Confluence](../../../assets/khb1guiaNPYUy3RWA6Y6.png)

Please make sure that the following preample is used since it will exclude page headers, footers, and numbers from the output:

```latex
\documentclass{article}
\pagestyle{empty}
...
\begin{document}
...
\end{document}
```

The following sections will show you some examples.

![LaTeX for Confluence](../../../assets/9g68REdwu8P6XbUh5Bj4.png)

### 3d plots

```latex
\documentclass{article}
\pagestyle{empty}
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}
\begin{axis}
\addplot3[
    surf,
]
{exp(-x^2-y^2)*x};
\end{axis}
\end{tikzpicture}
\end{document}
```

### Chemistry formulae

```latex
\documentclass{article}
\pagestyle{empty}
\usepackage{chemfig}
\begin{document}
\chemfig{A*5(-B=C-D-E=)}
\end{document}
```

### Figures

```latex
\documentclass{article}
\pagestyle{empty}
\usepackage[pdftex]{pict2e}
\usepackage[dvipsnames]{xcolor}
\begin{document}
\setlength{\unitlength}{1cm}
\setlength{\fboxsep}{0pt}
\fbox{%
\begin{picture}(3,3)
\put(0,0){{\color{blue}\circle*{0.25}}\hbox{\kern3pt \texttt{(0,0)}}}
\put(3,3){{\color{red}\circle*{0.25}}\hbox{\kern3pt \texttt{(3,3)}}}
\end{picture}}
\end{document}
```

```latex
\documentclass{article}
\pagestyle{empty}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
\draw (-2,0) -- (2,0);
\filldraw [gray] (0,0) circle (2pt);
\draw (-2,-2) .. controls (0,0) .. (2,-2);
\draw (-2,2) .. controls (-1,0) and (1,0) .. (2,2);
\end{tikzpicture}
\end{document}
```

## Refer to a LaTeX content

You can refer to existing LaTeX content. Below are the instructions.

Provide a reference name for the LaTeX content.

![LaTeX for Confluence](../../../assets/DPvMPA2OVgzIgP5PWTMH.png)

In edit mode, the number will be shown as **(TBD)**.

![LaTeX for Confluence](../../../assets/6By2fisqRt54V7k2TO6H.png)

Insert the **Render LaTeX Reference** macro.

![LaTeX for Confluence](../../../assets/2DoI4jo3GDfd0V3WB0Ge.png)

![LaTeX for Confluence](../../../assets/vPWTxkThB1xc6gLySsii.png)

Publish the page.

![LaTeX for Confluence](../../../assets/EdukKm6mJcP33TpUWFFL.png)

## Mobile support

LaTeX content can also be viewed on mobile phones via Atlassian's Confluence Cloud apps.

![](../../../assets/-MfQJGN9n8OA6qo0cKB5.jpg)
