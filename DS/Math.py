a, b, c, d, e = 3, 2, 2.0, -3, 10
print(a / b, a / c, d / b, b / a, d / e)
print(a / (b * 1.0))   
print(1.0 * a / b)
print(a / b * 1.0)
print(float(a) / b)
print(a / float(b))

from operator import *
plus = add(a, b)
minus = sub(a, b)
div = truediv(a, b)
fd = floordiv(a, b)
print(plus, minus, div, fd)

#builtin type
int + int = int
int + float = float 
int + complex = complex
float + float = float
float + complex = complex
complex + complex =complex

