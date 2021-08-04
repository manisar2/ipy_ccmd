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
    PLAIN = ""

def md_to_text(md):
    from bs4 import BeautifulSoup as bs
    from markdown import markdown
    html = markdown(md)
    soup = bs(re.sub('<br\s*?>', '\n', html), features='html.parser')
    return soup.get_text()

def display_string(obj, type=DisplayType.MARKDOWN, python_print=None, **kwargs):
    """Display markdown or HTML text in IPython from code cell. Will additionally print markdown-html-stripped\
        text in Python (configurable).

    Parameters
    ----------
    obj : object
        Text (or any object that has __repr__ or __str__), with (or without markdown).

    type : ipyccmd.DisplayType (default: .MARKDOWN)
        How to format the markdown text, e.g. as MATH, LATEX, HTML etc.

        Pass .PRETTY to print as if builtin print would do. .PLAIN would display raw string representation of\
            the object.

    python_print: bool (default: True through global ipyccmd.PYTHON_PRINT)
        Whether or not to print obj in Python. 
        :True => mardown symbols such as *, _ etc. to be removed as\
            much as possible (except MATH symbols).
    """
    f = getattr(obj, "__str__", "__repr__")
    if 'ipykernel' in sys.modules:
        from IPython.display import display, Markdown, Latex, Math, HTML, Pretty
        if type is DisplayType.PLAIN: display(f(), **kwargs)
        else: display(eval(type.value)(f(), **kwargs))
    else: # Python
        python_print = PYTHON_PRINT if python_print is None else python_print
        if python_print:
            if type in [DisplayType.MARKDOWN, DisplayType.HTML] : print(md_to_text(f()))
            else: print(obj) # no need to strip, print as such

with suppress(ModuleNotFoundError):
    from forbiddenfruit import curse
    def curse_obj(): curse(object, "md", display_string)
    curse_obj()

def md_print(*args, **kwargs):
    """Display formatted text in IPython and print markdown-html-stripped text in Python \
        (if is_md argument is True). If is_md argument is False, it simply runs __builtin__.print() \
        in both IPython and Python.

    Accepts any object builtin print would do.

    Parameters
    ----------
    is_md : bool (default: True through global ipyccmd.IS_MD)
        Stands for is_markdown. Set True for text containing markdown HTML, Latex, Math symbols.
        :True => formatted text in IPython, markdown-stripped text in Python
        :False => Plain print in both IPython and Python

    type : ipyccmd.DisplayType (default: .MARKDOWN)
        How to format the markdown text, e.g. as MATH, LATEX, HTML etc.        

        Pass .PRETTY to print as if builtin print would do. .PLAIN would display raw string representation of\
            the object.
    """
    is_md = kwargs.pop("is_md", IS_MD)
    type = kwargs.pop("type", DisplayType.MARKDOWN)
    if is_md: # markdown text was passed
        if 'ipykernel' in sys.modules:
            for arg in args:
                # We already checked and it's IPython. No need to pass python_print as True.
                display_string(arg, type=type, python_print=False)
            return None
        else: # it's Python. We need to convert md to plain text (if possible - MARKDOWN and HTML).
            if type in [DisplayType.MARKDOWN, DisplayType.HTML]:
                args = list(args)
                for i in range(0, len(args)):
                    args[i] = md_to_text(args[i])
            return __builtin__.print(*args, **kwargs)
    else: return __builtin__.print(*args, **kwargs) # no md object, do normal print

