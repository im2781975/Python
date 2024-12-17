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
