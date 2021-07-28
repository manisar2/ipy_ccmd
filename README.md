## Show Markdown from within Code Cells in Jupyter and VS Code's Interactive Python

Display markdown from within code cells in IPython output, while ignoring it when run in normal Python (like usual comments).

More details and explanation on [randompearls.com](https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/).

You can install it as a package by running pip install https://github.com/manisar2/ipy_ccmd.git.
Or copy the code in your project in src/ipy_ccmd/__init__.py.

Note that forbiddenfruit is installed as a dependency, so that statements of the form "anystring".md(type=DisplayType) can be used conveniently.
You may choose to instead use the functionality like display_string("anystring", type=DisplayType).

For curse to work, either import the package, or import curse_str and call it manually.
