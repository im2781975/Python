#class keyword
class Dog:

    attr1 = "mammal"

    attr2 = "dog"
 

    def fun(self):

        print("I'm a", self.attr1)

        print("I'm a", self.attr2)
 

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))
try:
    raise(MyError(3*2))
except MyError as error:
    print('A New Exception occurred: ', error.value)

class Error(Exception):
    pass
class zerodivision(Error):
    pass
try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision
except zerodivision:
    print("Input value is zero, try again!")
    print()
class Error(Exception):
    pass
class TransitionError(Error):
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex
        self.msg = msg
try:
    raise(TransitionError(2, 3*2, "Not Allowed"))
except TransitionError as error:
    print('Exception occurred: ', error.msg)
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise Networkerror("Error")
except Networkerror as e:
    print(e.args)
