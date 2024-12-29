def print_kwargs(**kwargs):    
    print(kwargs)
print_kwargs(a="two", b=3)

def example(a, **kw):    
    print kw
example(a=2, b=3, c=4)

def print_kwargs(**kwargs):    
    for key in kwargs:        
        print("key = {0}, value = {1}".format(key, kwargs[key]))
print_kwargs(a = "two", b = 1)
key = a, value = "two"
key = b, value = 1

def print_args(farg, *args):  
    print("formal arg: %s" % farg)  
    for arg in args:      
        print("another positional arg: %s" % arg)
print_args(1, "two", 3)

def foobar(foo=None, bar=None):    
    return "{}{}".format(foo, bar) 
    values = {"foo": "foo", "bar": "bar"} 
foobar(**values) 

def print_args(arg1, *args, keyword_required, keyword_only=True):   
    print("first positional arg: {}".format(arg1))    
    for arg in args:       
        print("another positional arg: {}".format(arg))   
    print("keyword_required value: {}".format(keyword_required))    
    print("keyword_only value: {}".format(keyword_only))   
print(1, 2, 3, 4)
print(1, 2, 3, keyword_required=4)

def test_func(arg1, arg2, arg3):
    print("arg1: %s" % arg1)   
    print("arg2: %s" % arg2)  
    print("arg3: %s" % arg3)
kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)

def fun(**kwargs):    
    print kwargs.get('value', 0)
fun()
fun(value=1)

def print_args(arg1, arg2): 
    print(str(arg1) + str(arg2))
a = [1,2]
b = tuple([3,4])
print_args(*a, *b)

a = [1,3,5,7,9]
b = [2,4,6,8,10]
zipped = zip(a,b)
zip(*zipped)

def add_student():       
    students['count'] = students.get('count', 0) + 1
