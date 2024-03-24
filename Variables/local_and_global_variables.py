"""
Global variables. Usually variables inside functions are local, unless you use global keyword.
"""


def myfunc():
    global x
    x = "test"


myfunc()

print(x)

# One thing with global variables is that they cannot be annotated which is extremely r@tarded and unexpected.
# Instead, you have to annotate them in global space (outside of functions) and then remove annotations inside the
# function.

# These variables could be redeclared as well

x = "Fix annotations!"
print(x)
