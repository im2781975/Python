def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
/////
def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

////
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
////
def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')
////
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
////
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
////
# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


# creating objects of car class
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)
///
# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


# creating objects of car class
audi = Car(s=200, c='red')
bmw = Car(s=250, c='black')
mb = Car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)
////
def example_function(*args, **kwargs):
    print(args)    # tuple of positional arguments
    print(kwargs)  # dictionary of keyword arguments

example_function(1, 2, 3, name='Alice', age=30)
Output:
(1, 2, 3)
{'name': 'Alice', 'age': 30}
///
def example_function(*args):
    print(type(args))  # <class 'tuple'>
example_function(1, 2, 3)
////
def sum_values(*args):
    total = sum(args)
    return total
result = sum_values(1, 2, 3, 4, 5)
print(result)  # Output: 15
////
def example_function(**kwargs):
    print(kwargs)
example_function(name='Alice', age=30)
Output:
{'name': 'Alice', 'age': 30}
/////

