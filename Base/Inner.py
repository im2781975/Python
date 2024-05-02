def double_dacker():
    print("Double Dacker")
    def inner():
        print("inner")
        return 3000
    return inner

print(double_dacker())
print(double_dacker()())

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
