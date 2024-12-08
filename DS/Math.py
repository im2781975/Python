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

import math
a, b = 1, 2
#return radian
res = math.sinh(a)
res = math.cosh(a)
#return arc tangent of pi
res = math.atan(math.pi)
# returns the Euclidean norm, same as math.sqrt(a*a + b*b)
res = math.hypot(a, b)
res = math.degrees(a)
res = math.radians(57.29577951308232)

print(3 * ('ab'), 3 * ('a', 'b'))

