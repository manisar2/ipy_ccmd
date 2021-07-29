## Show Markdown from within Code Cells in Jupyter and VS Code's Interactive Python

## Description
Display markdown from within code cells in IPython output, while ignoring it when run in normal Python (like usual comments).

More details and explanation on [randompearls.com](https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/).

## Installation
You can install it as a package by running `pip install git+https://github.com/manisar2/ipy_ccmd.git` .
<br>Or copy the code from src/ipy_ccmd/\_\_init\_\_.py into your project.

Note that `forbiddenfruit` is installed as a dependency, so that statements of the form `"anystring".md(type=DisplayType.Type)` can be used conveniently.<br>
You may instead choose to use the functionality like `display_string("anystring", type=DisplayType=Type)`.

## Usage
You can use it two ways.

### A. Using curse (forbiddenfruit):
`from ipy_ccmd import DisplayType`<br>
`"Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()`<br>
`"V = {1 \over 3} \pi r^2 h".md(DisplayType.MATH)`

### B. Without using curse (you can uninstall `forbiddenfruit`):
`from ipy_ccmd import display_string, DisplayType`<br>
`display_string("Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.")`<br>
`display_string("V = {1 \over 3} \pi r^2 h", DisplayType.MATH)`


### See a [.py](example/example.py) or [.ipynb](example/ipy_md.ipynb) example.

### The display can be modified in these ways (using `type` argument):
* MARKDOWN
* LATEX
* MATH
* HTML
* PRETTY

