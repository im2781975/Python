#list is changeable but tuple no
def Muteable(lst):
    lst.append(3)
x = [2, 5]
Muteable(x), print(x)

def Immuteable(lst):
    lst.append(3)
x = (2, 5)
Immuteable(x), print(x)
