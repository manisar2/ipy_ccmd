# Example
# %%
from ipyccmd import display_ccmd, DisplayType
from ipyccmd import md_print
import numpy as np

r = 5
h = 20
volume = np.pi * r**2 * h
"---".md()
"## Using `display_ccmd()` or curse `.md()`".md(dtype=DisplayType.MARKDOWN)
"<hr>".md(dtype=DisplayType.HTML)
"""Thus we have calculated the **volume** of the *cylinder* by using the formula
$$ V = \pi r^2 h $$

Read on...""".md()
"Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()
A = np.pi * r**2 + 2 * np.pi * r * h
display_ccmd("<h2>Volume of a cone is given by:</h2>", dtype=DisplayType.HTML)
"V = {1 \over 3} \pi r^2 h".md(DisplayType.MATH)
f"New array = \n{np.array_str(np.array([[1, 2],[3, 4]]))}".md(DisplayType.PRETTY)
(2).md(DisplayType.MATH)

################################################################################
md_print("---", dtype=DisplayType.MARKDOWN) # we'll use md_print for print henceforth
print = md_print
print("<h2>Will now use overridden print()</h2>", is_md=True, dtype=DisplayType.HTML)
print("<hr>", dtype=DisplayType.HTML)

print("""Thus we have calculated the **volume** of the *cylinder* by using the formula
$$ V = \pi r^2 h $$

Read on...""")
"Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()
A = np.pi * r**2 + 2 * np.pi * r * h
print("<h2>Volume of a cone is given by:</h2>", dtype=DisplayType.HTML)
print("V = {1 \over 3} \pi r^2 h", dtype=DisplayType.MATH)
print(f"New array = \n{np.array_str(np.array([[1, 2],[3, 4]]))}", dtype=DisplayType.PRETTY)
print(2, is_md=True, dtype=DisplayType.MATH)

############# For output in IPython, see the notebook example.ipynb #############
################################ Python Output #################################
# Using display_ccmd() or curse .md()

# Thus we have calculated the volume of the cylinder by using the formula
# $$ V = \pi r^2 h $$
# Read on...
# Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.
# Volume of a cone is given by:
# V = {1 \over 3} \pi r^2 h
# New array =
# [[1 2]
#  [3 4]]
# 2

# Will now use overridden print()

# Thus we have calculated the volume of the cylinder by using the formula
# $$ V = \pi r^2 h $$
# Read on...
# Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.
# Volume of a cone is given by:
# V = {1 \over 3} \pi r^2 h
# New array =
# [[1 2]
#  [3 4]]
# 2
