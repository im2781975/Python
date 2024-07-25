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
        sum += i
    print(f"Sum is: {sum} ")
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
