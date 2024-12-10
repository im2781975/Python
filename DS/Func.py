def greet_two(greeting):
    print(greeting)
greet_two("Howdy")

def greet_two(greeting="Howdy"):    print(greeting)
greet_two()

def many_types(x):    
    if x < 0:        
        return "Hello!"    
    else:        
        return 0 
print(many_types(1)) 
print(many_types(-1))

def func(*args):
    for i in args:        
        print(i) 
func(1, 2, 3)  
list_of_arg_values = [1, 2, 3] 
func(*list_of_arg_values)

def func(**kwargs):   
    for name, value in kwargs.items():        
        print(name, value)
func(value1=1, value2=2, value3=3)

my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)       

def fn(**kwargs):   
    print(kwargs)   
    f1(**kwargs)
def f1(**kwargs):   
    print(len(kwargs))
fn(a=1, b=2)

def greeting():    
    return "Hello"
print(greeting())
greet_me = lambda: "Hello"
print(greet_me())

strip_and_upper_case = lambda s: s.strip().upper() 
strip_and_upper_case("  Hello   ")

greeting = lambda x, *args, **kwargs: 
    print(x, args, kwargs)
greeting('hello', 'world', world='world')

sorted( [" foo ", "    bAR", "BaZ    "], key=lambda s: s.strip().upper()) 
sorted( [" foo ", "    bAR", "BaZ    "], key=lambda s: s.strip())
sorted( map( lambda s: s.strip().upper(), [" foo ", "    bAR", "BaZ    "]))
sorted( map( lambda s: s.strip(), [" foo ", "    bAR", "BaZ    "]))

def foo(msg):    
    print(msg) 
greet = lambda x = "hello world": foo(x) 
greet()

def make(action='nothing'):
    return action
make("fun")
make(action="sleep")
make() 
