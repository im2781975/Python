#arithmetic
print(5 + 2)
print(5 / 2)
print(5 // 2)
print(5 ** 2)
print(5 * 2)
print(5 % 2)
a, b, c = 4, 5, 7
d = a + b 
print(a, b, c)
a **= 2
a//= 2
d += a
print(a)
print(d)
# comparison
f = 6
print(f == 6, f!=6, f>= 6, f<=6, (f+1)!=6)
#logical
a, b = 7, 9
c = True
print((a > 4) and (b < 10) and c)
print((a > 4) or (b < 10))
a = False
print(not(a))
print(5 or 4)
#bitwise
a, b = 5, 4
print(a | b, a & b, a^b, ~a, a << 2)
#identity operator
print(a is b)
print(id(a))
print(a is not b)
c, d = 5, 5
e =5
#it will compare address
print(id(c) == id(d))
print(id(e) == id(a))
#Membership
str = "ibrahim"
print('m' in str)
print('i' not in str)
l = [1, 3 ,  5, 7]
print(5 in l)

