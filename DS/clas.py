def singleton(cls):        
    instance = [None]    
    def wrapper(*args, **kwargs):        
        if instance[0] is None:            
            instance[0] = cls(*args, **kwargs)        
            return instance[0]    
    return wrapper
@singleton 
class SomeSingletonClass:   
    x = 2    
    def __init__(self):        print("Created!") 
instance = SomeSingletonClass()  # prints: Created! 
instance = SomeSingletonClass()  # doesn't print anything 
print(instance.x)                # 2 
instance.x = 3 
print(SomeSingletonClass().x)

class Person(object): 
    """A simple class."""                                 
    species = "Homo Sapiens"                         
    def __init__(self, name):                        
        """This is the initializer. It's a special         method (see below).         """
        self.name = name                           
    def __str__(self):                              
        """This method is run when Python tries         to cast the object to a string. Return         this string when using print(), etc.         """
        return self.name # docstring # class attribute # special method # instance attribute # special method
    def rename(self, renamed):                       """Reassign and print the name attribute.""" 
        self.name = renamed 
        print("Now my name is {}".format(self.name))
kelly = Person("Kelly")
joseph = Person("Joseph") 
john_doe = Person("John Doe")
kelly.species
john_doe.species
john_doe.__str__()
print(john_doe)
john_doe.rename("John")

class A(object):    
    def f(self, x):      
        return 2 * x 
A.f
import inspect
inspect.isfunction(A.f)
inspect.ismethod(A.f)
A.f(1, 7)
a = A() 
A.f(a, 20)

class D(object):    
    multiplier = 2    
    @classmethod    
    def f(cls, x):       
        return cls.multiplier * x  
    @staticmethod    
    def g(name):       
        print("Hello, %s" % name)
D.f 
D.f(12) 
D.g 
D.g("world")

d = D() 
d.multiplier = 1337 (D.multiplier, d.multiplier)
d.f 
d.f(10)

class Rectangle():    
    def __init__(self, w, h):   self.w = w       
        self.h = h       
    def area(self):       
        return self.w * self.h           
    def perimeter(self):        return 2 * (self.w + self.h)
class Square(Rectangle):   
    def __init__(self, s):  
        super(Square, self).__init__(s, s)       
        self.s = s
r.area()
r.perimeter()
s.area()
s.perimeter()
issubclass(Square, Rectangle)
r = Rectangle(3, 4)
s = Square(2)
isinstance(r, Rectangle)  
isinstance(r, Square)
isinstance(s, Rectangle)
isinstance(s, Square)

class A(object):   
    def __init__(self, num):        
        self.num = num   
    def __add__(self, other):        
        return A(self.num + other.num)
def get_num(self):    
    return self.num
foo = A(42)
A.get_num = get_num
bar = A(6);
foo.get_num()
bar.get_num()
class Person(object):
    def __init__(self, first_name, last_name, age):        
        self.first_name = first_name        
        self.last_name = last_name        
        self.age = age        
        self.full_name =  first_name + " " + last_name      
    def greet(self):       
        print("Hello, my name is " + self.full_name + ".")
        
class Person(object):    
    def __init__(self, first_name, age, last_name=None):    if last_name is None:        
            self.first_name, 
            self.last_name = first_name.split(" ", 2)        
        else:            
            self.first_name = first_name            
            self.last_name = last_name              
            self.full_name = self.first_name + " " + self.last_name        
            self.age = age    
    def greet(self):       
        print("Hello, my name is " + self.full_name + ".")
        
class Person(object):    
    def __init__(self, first_name, last_name, age):        
        self.first_name = first_name       
        self.last_name = last_name        
        self.age = age        
        self.full_name = first_name + " " + last_name  
    @classmethod    
    def from_full_name(cls, name, age):        
        if " " not in name:            
            raise ValueError        
        first_name, last_name = name.split(" ", 2)        
        return cls(first_name, last_name, age)       
    def greet(self):        
        print("Hello, my name is " + self.full_name + ".")
bob = Person("Bob", "Bobberson", 42)
alice = Person.from_full_name("Alice Henderson", 31)
bob.greet()
class Foo(object):    
    def foo_method(self):        
        print "foo Method" 
class Bar(object):    
    def bar_method(self):        
        print "bar Method" 
class FooBar(Foo, Bar):    
    def foo_method(self):        
        super(FooBar, self).foo_method()

class Foo(object):        
    def __init__(self):            
        print "foo init"    
class Bar(object):        
    def __init__(self):            
        print "bar init"    
class FooBar(Foo, Bar):        
    def __init__(self):            
        print "foobar init"          
        super(FooBar, self).__init__()   
a = FooBar()
print isinstance(a,FooBar)
print isinstance(a,Foo)
print isinstance(a,Bar)

class MyClass(object):    
    def __init__(self):       
        self._my_string = ""     
    @property    
    def string(self):        
        """A profoundly important string."""        
        return self._my_string    
    @string.setter    
    def string(self, new_value):        
        assert isinstance(new_value, str), "Give me a string, not a %r!" % type(new_value)        
        self._my_string = new_value    
        @string.deleter    
        def x(self):        
            self._my_string = None
mc = MyClass() 
mc.string = "String!" 
print(mc.string) 
del mc.string
            
class Character(object):    
    def __init__(name, max_hp):        
        self._name = name        
        self._hp = max_hp        
        self._max_hp = max_hp
    @property    
    def hp(self):        
        return self._hp
    @property 
    def name(self):
        return self.name 
    def take_damage(self, damage): 
        self.hp -= damage 
        self.hp = 0 if self.hp <0 else self.hp 
    @property 
    def is_alive(self): 
        return self.hp != 0 
    @property 
    def is_wounded(self): 
        return self.hp < self.max_hp if self.hp > 0 else False 
    @property 
    def is_dead(self): 
        return not self.is_alive
bilbo = Character('Bilbo Baggins', 100) 
bilbo.hp 
bilbo.hp = 200      
bilbo.is_alive 
bilbo.is_wounded 
bilbo.is_dead 
bilbo.take_damage( 50 )
bilbo.hp 
bilbo.is_alive 
bilbo.is_wounded 
bilbo.is_dead 
bilbo.take_damage( 50 ) 
bilbo.hp 
bilbo.is_alive 
bilbo.is_wounded
bilbo.is_dead

class Rectangle(object):    
    def __init__(self, width, height, color='blue'):        
        self.width = width        
        self.height = height        
        self.color = color      
    def area(self):       
        return self.width  * self.height
default_rectangle = Rectangle(2, 3) 
print(default_rectangle.color) # 
blue red_rectangle = Rectangle(2, 3, 'red') 
print(red_rectangle.color)

class Rectangle2D(object):    
    def __init__(self, width, height, pos=[0,0], color='blue'):          
        self.width = width        
        self.height = height        
        self.pos = pos       
        self.color = color 
r1 = Rectangle2D(5,3)
r2 = Rectangle2D(7,8) 
r1.pos[0] = 4 
r1.pos 
r2.pos

class Rectangle2D(object):    
    def __init__(self, width, height, pos=None, color='blue'):          
        self.width = width        
        self.height = height        
        self.pos = pos or [0, 0]
        self.color = color
r1 = Rectangle2D(5,3)
r2 = Rectangle2D(7,8) 
r1.pos[0] = 4
r1.pos 
r2.pos


