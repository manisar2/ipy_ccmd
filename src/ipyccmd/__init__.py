# # Show markdown in IPython output from within a code cell (selectively)
# For details see https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/
import sys, re
from enum import Enum
import builtins as __builtin__
from contextlib import suppress

PYTHON_PRINT = True # use with display_ccmd() or md()
IS_MD = True # use with print()
PRINT_OBJNAME = True
DEFAULT_DTYPE = None
# if DEFAULT_DTYPE is None and dtype is not provided, dtype will be determined dynamically as follows:
# .MARKDOWN if obj is string, else .PRETTY

class DisplayType(Enum):
    MARKDOWN = "Markdown"
    LATEX = "Latex"
    MATH = "Math"
    HTML = "HTML"
    PRETTY = "Pretty"
    PLAIN = ""

def print_object_name(obj):
    objname = None
    from inspect import currentframe
    frame = currentframe()
    lcls = None
    try: lcls =frame.f_back.f_back.f_locals
    finally: del frame
    if lcls:
        for obname, ob in lcls.items():
            if ob is obj:
                objname = obname
                break
    if objname:  __builtin__.print(f"{objname}: ", end='')

def md_to_text(md):
    from bs4 import BeautifulSoup as bs
    from markdown import markdown
    html = markdown(md)
    soup = bs(re.sub('<br\s*?>', '\n', html), features='html.parser')
    return soup.get_text()

def display_ccmd(obj, dtype=None, python_print=None, print_objname=None, **kwargs):
    """Display markdown or HTML text in IPython from code cell. Will additionally print markdown-html-stripped\
        text in Python (configurable).

    Parameters
    ----------
    obj : object
        Text (or any object that has __repr__ or __str__), with (or without markdown).

    dtype : ipyccmd.DisplayType (default: .MARKDOWN)
        How to format the markdown text, e.g. as MATH, LATEX, HTML etc.

        Pass .PRETTY to print as if builtin print would do. .PLAIN would display raw string representation of\
            the object.

    python_print: bool (default: True through global ipyccmd.PYTHON_PRINT)
        Whether or not to print obj in Python.
        :True => mardown symbols such as *, _ etc. to be removed as\
            much as possible (except MATH symbols).

    print_objname: bool (default: True through global ipyccmd.PYTHON_PRINT)
        Print object name if the name exists (only in IPython)
    """
    f = getattr(obj, "__str__", "__repr__")

    if 'ipykernel' in sys.modules:
        from IPython.display import display, Markdown, Latex, Math, HTML, Pretty
        print_objname = PRINT_OBJNAME if print_objname is None else print_objname
        if print_objname: print_object_name(obj)
        if dtype is DisplayType.PLAIN: display(f(), **kwargs)
        else:
            if dtype is None:
                if DEFAULT_DTYPE: dtype = DEFAULT_DTYPE
                else:
                    if type(obj) is str: dtype = DisplayType.MARKDOWN
                    else: dtype = DisplayType.PRETTY # let's be more verbose for objs other than strs.
            display(eval(dtype.value)(f(), **kwargs))
    else: # Python
        python_print = PYTHON_PRINT if python_print is None else python_print
        if python_print:
            if dtype in [DisplayType.MARKDOWN, DisplayType.HTML] :  __builtin__.print(md_to_text(f()))
            else:  __builtin__.print(obj) # no need to strip, print as such

with suppress(ModuleNotFoundError):
    from forbiddenfruit import curse
    def curse_obj(): curse(object, "md", display_ccmd)
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

    dtype : ipyccmd.DisplayType (default: .MARKDOWN)
        How to format the markdown text, e.g. as MATH, LATEX, HTML etc.        

        Pass .PRETTY to print as if builtin print would do. .PLAIN would display raw string representation of\
            the object.

    print_objname: bool (default: True through global ipyccmd.PYTHON_PRINT)
        Print object name if the name exists (only in IPython)
    """
    is_md           = kwargs.pop("is_md", IS_MD)
    dtype           = kwargs.pop("dtype", None)
    print_objname   = kwargs.pop("print_objname", PRINT_OBJNAME)
    if is_md: # markdown text was passed
        if 'ipykernel' in sys.modules:
            for arg in args:
                if print_objname: print_object_name(arg) # need to print objname here because of frame level
                if dtype is None:
                    if DEFAULT_DTYPE: dtype = DEFAULT_DTYPE
                    else:
                        if type(arg) is str: dtype = DisplayType.MARKDOWN
                        else: dtype = DisplayType.PRETTY # let's be more verbose for objs other than strs.
                # We already checked and it's IPython. No need to pass python_print as True.
                display_ccmd(arg, dtype=dtype, python_print=False, print_objname=False) # objname becomes arg
            return None
        else: # it's Python. We need to convert md to plain text (if possible - MARKDOWN and HTML).
            if dtype in [DisplayType.MARKDOWN, DisplayType.HTML]:
                args = list(args)
                for i in range(0, len(args)):
                    args[i] = md_to_text(args[i])
            return __builtin__.print(*args, **kwargs)
    else: return __builtin__.print(*args, **kwargs) # no md object, do normal print
