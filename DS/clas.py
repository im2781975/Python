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

class C:    
    x = 2
    def __init__(self, y):        self.y = y 
C.x 
c1 = C(3) 
c1.x 
c1.y 
c2 = C(4) 
c2.x 
c2.y
c2.x = 4 
c2.x 
C.x

class D:   
    x = []    
    def __init__(self, item):        self.x.append(item)
d1 = D(1) 
d2 = D(2) 
d1.x 
d2.x 
D.x

class Country(object):   
    def __init__(self):        
        self.cities=[]           
    def addCity(self,city):        self.cities.append(city)

class City(object):   
    def __init__(self, numPeople):        
        self.people = []        
        self.numPeople = numPeople                  
    def addPerson(self, person):        
        self.people.append(person)       
    def join_country(self,country):        
        self.country = country        
        country.addCity(self)               
        for i in range(self.numPeople):                
            person(i).join_city(self) 
class Person(object):    
    def __init__(self, ID):        
        self.ID=ID    
    def join_city(self, city):        
        self.city = city        
        city.addPerson(self)           
    def people_in_my_country(self):        
        x= sum([len(c.people) for c in self.city.country.cities])        
        return x       
US=Country() 
NYC=City(10).join_country(US) 
SF=City(5).join_country(US) 
print(US.cities[0].people[0].people_in_my_country())

dir(list)
[m for m in dir(list) if not m.startswith('__')]
 
class Singleton:    
    def __new__(cls):        
    try:            
        it = cls.__it__        
    except AttributeError:            
        it = cls.__it__ = object.__new__(cls)        
    return it    
    def __repr__(self):        
        return '<{}>'.format(self.__class__.__name__.upper())    
    def __eq__(self, other):         return other is self

@Singleton 
class Single:   
    def __init__(self):        
        self.name=None        
        self.val=0    
    def getName(self):        
        print(self.name) 
x=Single.Instance() 
y=Single.Instance() 
x.name='I\'m single'
x.getName() 
y.getName()

class Parent(object):   
    def introduce(self):    
        print("Hello!")    
    def print_name(self):        
        print("Parent")
        
class Child(Parent):   
    def print_name(self):        
        print("Child")
p = Parent()
c = Child()
p.introduce() 
p.print_name() 
c.introduce() 
c.print_name()

class A(object):
    def func(self): 
        pass
@classmethod 
def classMethod(self): 
    pass
class B(object):
    unboundMeth = A.func
a = A()
b = B()
print A.func
print a.func
print B.unboundMeth
print b.unboundMeth
print A.classMethod
print a.classMethod

class Parent(object):
    def func(self):
        pass    
    func2 = func
class Child(Parent):   
    func = Parent.func
class AnotherClass(object):   
    func = Parent.func
print Parent.func is Parent.func                
print Parent.func2 is Parent.func2              
print Child.func is Child.func                  
print AnotherClass.func is AnotherClass.func 

import turtle, time, random
turtle.speed(0) 
turtle.colormode(255)
turtle.pensize(4)
def triangle(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(135) 
    turtle.forward(size * 1.5)
while(1): 
    turtle.setpos(random.randint(-200, 200), random.randint(-200, 200))
    turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    triangle(random.randint(5, 55))
    turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    
class Card:
    def __init__(self, suit, pips) : 
        self.suit = suit self.pips = pips
ace_of_spades = Card('Spades', 1) four_of_clubs = Card('Clubs',  4) six_of_hearts = Card('Hearts', 6)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]
print(my_hand)

string_of_card = str(ace_of_spades) 
print(string_of_card)

class Card: 
    def __init__(self, suit, pips): 
        self.suit = suit 
        self.pips = pips
    def __str__(self):       
        special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
        card_name = special_names.get(self.pips, str(self.pips)) 
        return "%s of %s" % (card_name, self.suit)
ace_of_spades = Card('Spades', 1)
print(ace_of_spades)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]
print(my_hand)

class Card:    
    special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}    
    def __init__(self, suit, pips):        
        self.suit = suit        
        self.pips = pips    
    def __str__(self):       
        card_name = Card.special_names.get(self.pips, str(self.pips))        
        return "%s of %s (S)" % (card_name, self.suit)    
   def __repr__(self):        
       card_name = Card.special_names.get(self.pips, str(self.pips))       
   return "%s of %s (R)" % (card_name, self.suit)
ace_of_spades = Card('Spades', 1) 
four_of_clubs = Card('Clubs',  4) 
six_of_hearts = Card('Hearts', 6)
my_hand = [ace_of_spades, four_of_clubs, six_of_hearts]
print(my_hand)     
print(ace_of_spades) 
str_card = str(four_of_clubs)
print(str_card)          
repr_card = repr(four_of_clubs)
print(repr_card) 
print(four_of_clubs.__str__())
print(four_of_clubs.__repr__())  

class Card:    
    special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}    
    def __init__(self, suit, pips):        
        self.suit = suit        
        self.pips = pips    
     def __repr__(self):       
        card_name = Card.special_names.get(self.pips, str(self.pips))        
        return "%s of %s" % (card_name, self.suit)
print(six_of_hearts)         
print(str(six_of_hearts))
print([six_of_hearts])
print(repr(six_of_hearts)) 

class Card:   
    special_names = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}   
    def __init__(self, suit, pips):       
        self.suit = suit      
        self.pips = pips
    def __str__(self):        
        card_name = Card.special_names.get(self.pips, str(self.pips))        
        return "%s of %s" % (card_name, self.suit)
    def __repr__(self):        
        return "Card(%s, %d)" % (self.suit, self.pips)
        
expression = '5 + 3 * a' 
a = 5 
result = eval(expression)
result

code = compile('a * b + c', '<string>', 'eval')
a, b, c = 1, 2, 3 
eval(code)
