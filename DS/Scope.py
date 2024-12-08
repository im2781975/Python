#scope
def counter():    
    num = 0    
    def incrementer():     
        nonlocal num
        num += 1        
        return num   
    return incrementer
c = counter()
for i in range(1, 12):
    print(c())
    
def readX():
    if True:
        x = 'Hi'
    print(x)
readX()

x = 'Hello'
def changeLocal():
    #global x
    x = 'Bye'
    print(x)
changeLocal()
print(x)

#del command
x = 5
print(x)
del x #delete x
print(x)

x = {'a': 1, 'b': 2} 
del x['a']
print(x) 

x = [0, 1, 2, 3, 4]
del x[1:3] 
print(x) 

a = 'global' 
class Fred:    
    a = 'class'  
    b = (a for i in range(10)) 
    c = [a for i in range(10)] 
    d = a  
    e = lambda: a     
    f = lambda a=a: a  
    @staticmethod 
    def g():  
        return a 
print(Fred.a)
print(next(Fred.b)) 
print(Fred.c[0]) 
print(Fred.d)
print(Fred.e()) 
print(Fred.f()) 
print(Fred.g())

#global scope
foo = 1
def fun():
    bar = 2
    print(foo, globals().keys())
    print(bar, locals().keys())
fun()

foo = 1 
def func():    
    foo = 2
    print(foo)
    print(globals()['foo'])
    print(locals()['foo'])
func()

foo = 1
def func():    
    global foo   
    foo = 2  
func()
print(foo)

foo = 1 
def func():
    foo = 7  
    print(foo)  
    print(globals()['foo']) 
    global foo  
    print(foo)
func()

foo = 1
def f1():    
    bar = 1    
    def f2():        
        baz = 2     
        print(locals().keys())
        print('bar' in locals())
        print('bar' in globals()) 
    def f3():        
        baz = 3        
        print(bar)     
        print(locals().keys())      
        print('bar' in locals()) 
        print('bar' in globals()) 
    def f4():        
        bar = 4   
        baz = 4        
        print(bar)       
        print(locals().keys())      
        print('bar' in locals()) 
        print('bar' in globals())
    return f2, f3, f4
f2, f3, f4 = f1()
f2()

foo = 0
def f1():    
    foo = 1
    def f2():       
        foo = 2       
        def f3():          
            foo = 3
            print(foo)          
            foo = 30          
        def f4():           
            global foo      
            print(foo) 
            foo = 100
            
def f1():       
    def f2():        
        foo = 2 
        def f3():            
            nonlocal foo
            print(foo)  
            foo = 20 
