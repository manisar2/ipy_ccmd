# Example
# %% 
from ipy_code_cell_markdown import ipy_md
from ipy_code_cell_markdown.ipy_md import DisplayType

# if __name__ == "__main__": # so that this doesn't run when called from other modules
import numpy as np
r = 5
h = 20
volume = np.pi * r**2 * h
"""Thus we have calculated the **volume** of the *cylinder* by using the formula
$$ V = \pi r^2 h $$

Read on...""".md()
"Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()
A = np.pi * r**2 + 2 * np.pi * r * h
"<h2>Volume of a cone is given by:</h2>".md(DisplayType.HTML)
"V = {1 \over 3} \pi r^2 h".md(DisplayType.MATH)
f"New array = \n{np.array_str(np.array([[1, 2],[3, 4]]))}".md(DisplayType.PRETTY)
