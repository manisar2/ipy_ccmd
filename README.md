## Show Markdown from within Code Cells in Jupyter and VS Code's Interactive Python

## Description
Display markdown from within code cells in IPython output, while ignoring it when run in normal Python (like usual comments).

More details and explanation on [randompearls.com](https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/).

## Installation
You can install it as a package by running pip install https://github.com/manisar2/ipy_ccmd.git.
<br>Or copy the code from src/ipy_ccmd/__init__.py into your project.

Note that **forbiddenfruit** is installed as a dependency, so that statements of the form `"anystring".md(type=DisplayType.Type)` can be used conveniently.<br>
You may instead choose to use the functionality like `display_string("anystring", type=DisplayType=Type)`.

## Usage
### For having curse work, there are three options:
1. `import ipy_ccmd`
2. `from ipy_ccmd import curse_str` and call it manually
3. `from ipy_ccmd import DisplayType`<br>
   This is **recommended** as you will probably use `DisplayType` anyway.

### See a [.py](example/example.py) or [.ipynb](example/ipy_md.ipynb) example.

### The display can be modified in these ways (using `type` argument):
* MARKDOWN
* LATEX
* MATH
* HTML
* PRETTY

