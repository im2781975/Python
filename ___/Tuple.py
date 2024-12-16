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

tup = ([1, 2, 3], [4, 5, 6])
tup[0][1] = 66
print(tup)
