# Show markdown in IPython output from within a code cell (selectively)
# For details see https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/
import sys
from enum import Enum
from forbiddenfruit import curse
from IPython.display import display, Markdown, Latex, Math, HTML, Pretty
class DisplayType(Enum):
    MARKDOWN = Markdown
    LATEX = Latex
    MATH = Math
    HTML = HTML
    PRETTY = Pretty

def display_string(self, type=DisplayType.MARKDOWN):
    if 'ipykernel' in sys.modules: display(type.value(self))
def curse_str():
    curse(str, "md", display_string)
curse_str()
