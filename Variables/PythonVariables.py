x = 1  # Without type annotation
y = 'Some text'

a: int = 2  # With type annotation
b: str = 'Some text'

# Casting

q = str(123)  # Will be '123'
w = int(1234)  # Will be 123
e = float(12345)  # Will be 123.0

print(f'{q} is {type(q)},\n{w} is {type(w)},\n{e} is {type(e)}')
