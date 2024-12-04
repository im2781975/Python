def func(name):
    print(f"Hi {name} ")
def add(a, b):
    c = a + b
    print(f"Sum is: {c} ")
def greet(name, age):
    print(f"name {name},age {age} ")
def DefaultArg(name, age, dept = "Cs"):
    print(f"name {name},age {age}, dept {dept}")
#Arbetry Positional Arg
def ArbetryArg(*num):
    sum = 0
    for i in num:
        print(f"Elements are {i} ")
        sum += i
    print(f"Sum is: {sum} ")
def ArbetryPosArg(*num, name):
    sum = 0
    print(name)
    for i in num:
        print(f"Elements are {i} ")
        sum += i
    print(f"Sum is: {sum} ")
def ArbetryfPosArg(name, *num):
    sum = 0
    print(name)
    for i in num:
        print(f"Elements are {i} ")
        sum += i
    print(f"Sum is: {sum} ")
#Arbetry key args
#its a key_value pair like dictionary
def Info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
#args must be before kargs
def info(*args, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(args)
add(7, 11)
func("molla")
func("Aslam")
#keyword argument
greet(age = 28, name = "Ibrahim")
#positional arguments
greet("ibrahim", 28)
#keyword arg should be after positional arg
greet("ibrahim", age = 28)
#default arg should be provided after non def arg
DefaultArg("Mollavai", 26)
DefaultArg("Mollavai", 26, "ME")
ArbetryArg(9, 8, 7, 6, 5, 4)
ArbetryPosArg(1, 3, 5, name = "Mollavai")
#it will count 1 as a name
ArbetryfPosArg(1, 3, 5)
Info(name = "Ab", age = 34, dept = "Cs")
Info(name = "Cd", age = 43)
info(2, 4, 6, name = "Ab", age = 34, dept = "Cs")
