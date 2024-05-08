import time
def double_dacker():
    print("Double Dacker")
    def inner():
        print("inner")
        return 3000
    return inner

print(double_dacker())
print(double_dacker()())
double_dacker()()
def do_something(work):
    print("Starting")
    #print(work)
    #for passing function as a parameter have to use function
    work()
    print("Ended")
def coding():
    print("Coded")
#do_something(2)
do_something(coding)
def tim(func):
    def outer():
        print("Time Started")
        print(func)
        print("Time ended")
    return outer
def get():
    print("Factorial Starting")
tim(get)()
def timer(func):
    start = time.time()
    def outer(*args,**kargs):
        print("Started")
        func(*args,**kargs)
        print("ended")
        end = time.time()
        print({end - start})
    return outer
import math
@timer
def fact(n):
    print("Factorial")
    res = math.factorial(n)
    print(res)
#timer(fact(5))()
fact(n = 120)
"""@timer
def out():
    print("Going")
out() """
