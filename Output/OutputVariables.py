# Python by default inserts spaces using print() and a comma

x: str = "Test"
z: str = "Text"
print(x, z)

# This isn't the case for string concatenation, the world would be jointed together

print(x + z)

"""
First is preferable and supports multiple data types. There is also fstring formatting
"""
# print(f'{q} is {type(q)},\n{w} is {type(w)},\n{e} is {type(e)}')
