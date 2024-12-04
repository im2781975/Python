print(round(2.555555,2))
print(round(2.55555))
print(round(2.5))
print(round(3.5))
print(round(674, -1))
print(round(675, -1))
print(round(674, -2))
print(round(675, -2))
print(round(675, -3))
print(round(-8/3, 2))
print(round(-1.5, 2))
print(round(675.678, -1))
print(type(round(6.7777, 2)))
print(type(round(6.77777)))

#range
"""for var_name in range(i, j, k)
i->start, j->stop, k->step
here i & k is optional"""
a = range(5)
print(a[1])
a = range(2, 10, 2)
#print(a[1])
for i in a:
    print(i, a)
a = range(10, 0, -1)
for i in a:
    print(i)
total = 0
for i in range(0, 100, 2):
    #exclude 100
    total += i
print(total)

#return
def FormateName(name, surname):
    name.title()
    surname.title()
    FormattedName = name.title()
    FormattedSurname = surname.title()
    print(f"{FormattedName} {FormattedSurname} ")
    print(f"{name} {surname} ")
    
FormateName("Molla", "vai")
import statistics
def MeanMedianMode(list1):
    return statistics.mean(list1), statistics.mode(list1), statistics.median(list1)
    #return [statistics.mean(list1), statistics.mode(list1), statistics.median(list1)]
print(MeanMedianMode([2, 4, 1, 7, 5, 9]))
a, b, c = MeanMedianMode([2, 4, 1, 7, 5, 9])
print(f"Mean is {a}\nMode is {b}\nMedian is {c}")


def add(a, b):
    if a == 0 & b == 0:
        return"entered zero for both"
    else:
        return a + b
x = int(input("First variable: "))
y= int(input("Second variable: "))
print(add(x, y))

def func(x):
    return x + 1
def func2(a, b):
    return a + b
x = func2(9, 11)
print(func(x))
