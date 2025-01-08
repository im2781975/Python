#immuteable
tup = (123, 'Hello')
put = ('world')
print(tup, tup[0])
"""            """
def multi():
    return 3, 4
print(multi())
"""              """
letter = 'A', 'B', 'C', 'D', 'E', 'F'
print(type(letter))
print(f"letter[0]: {letter[0]}\nletter[-1]: {letter[-1]}\nletter[5 : 2 : -1]: {letter[5 : 2 : -1]} ")
for item in letter:
    print(item)
print(len(letter))
"""             """
#tuple is immuteable but it can hold muteable object.like list
tup = ([1, 2, 3], [4, 5, 6])
tup[0][1] = 66
print(tup)

#tuple are zero idx
a = (1, 7, -4, "jenny", True, 9, -5)
b, c = (10, 12, 14, 16), (11,)
print(f"a[1]: {a[1]}\na[-2]: {a[-2]}\na[5]: {a[5]}\nlen(a): {len(a)} \n")
print(f"a[1 : 3]: {a[1 : 3]}\na[:5]: {a[:5]} ")
tup = (a , b, c)
print(f"len(tup): {len(tup)}\ntup[0]: {tup[0]}\ntup: {tup}")
tup = a + b + c
print(f"len(tup): {len(tup)}\ntup[0]: {tup[0]}\ntup: {tup}")
#should be same type not mixed
print(f"max(b): {max(b)}\nmin(b): {min(b)}")
print(f"b.count(12): {b.count(12)}\nb.index(12): {b.index(12)} ")
lst = [2, 3, 5, 8]
print(f"lst: {tuple(lst)}")
print((10, ) * 6, ("Molla") * 2)

lst = [1, 2, 3, 4, 5, 6]
print(f"tuple('Geeks'): {tuple('Geeks')}\ntuple(lst): {tuple(lst)} ")
"""					"""
tup = ()
tup = ('A', 'B')
lst = [2, 3, 1, 5, 4]
tup = tuple(lst)
tup = tuple("Hello")
tup = (5, "molla", 7, " vai")
ple = (9, 1)
print(tup[0]) #indexing
print(tup + ple)
print(("hello, ") * 3)
tup = ("molla", "vai", " ibra")
a, b, c = tup
print(a, b, c)
print(tup[:1], tup[::-1])
"""                """
tup = ("Molla")
n = 2
for i in range(int(n)):
    tup = (tup, )
    print(tup)
"""				"""
person = ("Molla", "Fra", (1, 9, 2000))
*_,(*_, Bdate) = person
print(Bdate, *_)
def add(*put):
    put += (3, )
    return put
print(add(1, 2, 4))
"""				"""
tup = ('a', 'b', 'c', 'd')
tup = ()
print(tuple('lupin'))
print(tuple(range(3)))
t = (1, 2)
q = t
t += q
print(q, t)
"""            """
a = 1, 2, 3, 4
_, x, y, _ = a
print(x, y)
first, *more, last = (1, 2, 3, 4, 5)
print(first, last, *more)
tup = (12, 45, 22222, 103, 6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tup)   
"""            """
tup1 = ('a', 'b', 'c', 'd', 'e')
tup2 = ('1', '2', '3')
tup3 = tup1
print(tup1 + tup2)
print(tup1 > tup2, tup2 > tup1, tup1 ==tup3)
print(len(tup1), max(tup1), min(tup1))
lst = [1, 2, 3, 4, 5]
print(tuple(lst))
"""            """
x = (1, 2, 3)
print(x[0], x[1], x[2], x[-1], x[-2], x[-3], x[:-1], x[-1:], x[1 : 3])
colors = "red", "green", "blue" 
print(colors[::-1])
print(tuple(reversed(colors)))
"""				"""
tup = ('bear', 'weasel', 'bear', 'frog')
print(tup.count('bear'), tup.count('fox'))
import heapq
heapq.nlargest(5, range(10))
heapq.nsmallest(5, range(10))
