# Show markdown in IPython output from within a code cell (selectively)
# For details see https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/
import sys, re
from enum import Enum
import builtins as __builtin__
from contextlib import suppress

PYTHON_PRINT = True # use with display_string() or md()
IS_MD = True # use with print()

class DisplayType(Enum):
    MARKDOWN = "Markdown"
    LATEX = "Latex"
    MATH = "Math"
    HTML = "HTML"
    PRETTY = "Pretty"

def md_to_text(md):
    from bs4 import BeautifulSoup as bs
    from markdown import markdown
    html = markdown(md)
    soup = bs(re.sub('<br\s*?>', '\n', html), features='html.parser')
    return soup.get_text()

def display_string(self, type=DisplayType.MARKDOWN, python_print=None):
    if 'ipykernel' in sys.modules: 
        from IPython.display import display, Markdown, Latex, Math, HTML, Pretty
        display(eval(type.value)(self))
    else:
        if python_print is None: python_print = PYTHON_PRINT
        if python_print: print(md_to_text(self))

with suppress(ModuleNotFoundError):
    from forbiddenfruit import curse
    def curse_str():
        curse(str, "md", display_string)
    curse_str()

def md_print(*args, **kwargs):
    is_md = kwargs.pop("is_md", IS_MD)
    type = kwargs.pop("type", DisplayType.MARKDOWN)
    if is_md: # markdown text was passed
        if 'ipykernel' in sys.modules:
            for arg in args:
                display_string(arg, type=type, python_print=False)
            return None
        else: # we need to convert to plain text
            args = list(args)
            for i in range(0, len(args)):
                args[i] = md_to_text(args[i])
            return __builtin__.print(*args, **kwargs)
    else: return __builtin__.print(*args, **kwargs) # plain text

