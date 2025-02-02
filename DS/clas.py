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
        
class Vehicle(object):   
    """A generic vehicle class."""  
    def __init__(self, position):       
        self.position = position   
    def travel(self, destination):       
        route = calculate_route(from=self.position, to=destination)       
        self.move_along(route) 
class Car(Vehicle):   ...
class Boat(Vehicle):   ... 
class Plane(Vehicle):  ... 

class RadioUserMixin(object):   
    def __init__(self):     
        self.radio = Radio()
    def play_song_on_station(self, station):       
        self.radio.set_station(station)       self.radio.play_song()
class Car(Vehicle, RadioUserMixin):   ... 
class Clock(Vehicle, RadioUserMixin):   ...

class Mixin1(object):   
    def test(self):        
        print "Mixin1"
class Mixin2(object):    
    def test(self):        
        print "Mixin2" 
class BaseClass(object):    
    def test(self):       
        print "Base" 
class MyClass(BaseClass, Mixin1, Mixin2):    pass
x = MyClass() 
x.test()

class Book:    
    def __init__(self, title, author):        
        self.title = title        
        self.author = author
book1 = Book(title="Right Ho, Jeeves", author="P.G. Wodehouse")
book1.title

class P:    
    def __init__(self,title,author):        
        self.title = title       
        self.setAuthor(author)    
    def get_author(self):       
        return self.author   
    def set_author(self, author):       
        if not author:           
            self.author = "Unknown"        
        else:
            self.author = author
book = Book(title="Ancient Manuscript", author="Some Guy")
book.author = "" 

class Book:    
    def __init__(self, title, author):        
        self.title = title        
        self.author = author    
    @property    
    def author(self):        
        return self.__author    
    @author.setter    
    def author(self, author):       
        if not author:            
            self.author = "Unknown"        
        else:            
            self.author = author
book = Book(title="Ancient Manuscript", author="Some Guy") 
book.author = " "
book.author

class Fruit:      
    def check_ripeness(self):       
    raise NotImplementedError("check_ripeness method not implemented!") 
class Apple(Fruit):    
    pass
a = Apple() 
a.check_ripeness() 

class MontyPython:    
    def joke(self):        
        raise NotImplementedError()   
    def punchline(self):        
        raise NotImplementedError() 
class ArgumentClinic(MontyPython):    
    def joke(self):        
        return "Hahahahahah"
sketch = ArgumentClinic()
sketch.punchline() NotImplementedError

from abc import ABCMeta, abstractmethod 
class MontyPython(metaclass=ABCMeta):    
    @abstractmethod    
    def joke(self):       
        pass
    @abstractmethod
    def punchline(self):   
        pass
class ArgumentClinic(MontyPython):    
    def joke(self):        
        return "Hahahahahah"

class ArgumentClinic(MontyPython):    
    def joke(self):        
        return "Hahahahahah"    
    def punchline(self):        
        return "Send in the constable!"

class Mixin1(object):   
    def test(self):        
        print "Mixin1" 
class Mixin2(object):    
    def test(self):        
        print "Mixin2" 
class MyClass(Mixin1, Mixin2):    
    pass
class MyClass(Mixin2, Mixin1):    
    pass
obj = MyClass() 
obj.test()

class Base(object):    
    def test(self):        
        print("Base.")
class PluginA(object):    
    def test(self):        
        super().test()       
        print("Plugin A.")
class PluginB(object):    
    def test(self):        
        super().test()       
        print("Plugin B.")
plugins = PluginA, PluginB
class PluginSystemA(PluginA, Base): 
    pass
class PluginSystemB(PluginB, Base):  
    pass
PluginSystemA().test()
PluginSystemB().test()

class Base:    
    plugins = []   
    def __init_subclass__(cls, **kwargs):       
        super().__init_subclass__(**kwargs)        
        cls.plugins.append(cls)       
    def test(self):       
        print("Base.") 
class PluginA(Base):    
    def test(self):       
        super().test()       
        print("Plugin A.") 
class PluginB(Base):    
    def test(self):        
        super().test()        
        print("Plugin B.")
PluginA().test()
PluginB().test()

class MyClass:    
    def __bool__(self):        
        return False
my_instance = MyClass() 
print(bool(MyClass))      
print(bool(my_instance)) 

class A(object):    
    @property    
    def get(self):        
        raise IOError
    class B(object):   
    @property    
    def get(self):        
        return 'get in b' 
a = A() 
b = B()

print 'a hasattr get: ', hasattr(a, 'get')
print 'b hasattr get', hasattr(b, 'get')

try:   
    a.get 
except AttributeError:    
    print("no get property!")

p = getattr(a, "get", None) 
if p is not None:   
    print(p) 
else:    
    print("no get property!")

from itertools import chain 
class SolarSystem:   
    planets = [list (chain (planet, (index + 1,))) for index, planet in enumerate ((      
        ('Mercury', 'hot', 2240),        
        ('Venus', 'sulphurous', 6052),       
        ('Earth', 'fertile', 6378),        
        ('Mars', 'reddish', 3397),        
        ('Jupiter', 'stormy', 71492),        
        ('Saturn', 'ringed', 60268),        
        ('Uranus', 'cold', 25559),        
        ('Neptune', 'very cold', 24766)    ))]       
    lines = (        '{} is a {} planet',        'The radius of {} is {} km',        '{} is planet nr. {} counting from the sun'    )       
    def __init__ (self):        
        self.lineIndex = 0
    def greet (self):       
        self.planet = self.planets [int (Math.random () * len (self.planets))]       
        document.getElementById ('greet') .innerHTML = 'Hello {}'.format (self.planet [0])     
        self.explain()
    def explain (self):       
        document.getElementById ('explain').innerHTML = (            self.lines [self.lineIndex] .format (self.planet [0], self.planet [self.lineIndex + 1]) ) 
        self.lineIndex = (self.lineIndex + 1) % 3        
        solarSystem = SolarSystem ()

class A: 
    def __init__ (self, x):
        self.x = x 
    def show (self, label):
        print ('A.show', label, self.x)
class B: 
    def __init__ (self, y):        
        alert ('In B constructor') 
        self.y = y 
    def show (self, label): 
        print ('B.show', label, self.y) 
class C (A, B): 
    def __init__ (self, x, y):       
        alert ('In C constructor')      
        A.__init__ (self, x)       
        B.__init__ (self, y) 
        self.show ('constructor') 
    def show (self, label):        
        B.show (self, label) 
        print ('C.show', label, self.x, self.y)
a = A (1001) 
a.show ('america') 
b = B (2002) 
b.show ('russia') 
c = C (3003, 4004) 
c.show ('netherlands') 
show2 = c.show 
show2 ('copy')

class Singleton(object):    
    def __new__(cls):          
        if not hasattr(cls, 'instance'):           
            cls.instance = super(Singleton, cls).__new__(cls) 
        return cls.instance
s = Singleton() 
print ("Object created", s) 
s1 = Singleton() 
print ("Object2 created", s1)

from abc import ABCMeta, abstractmethod 
class Music():    
    __metaclass__ = ABCMeta    
    @abstractmethod    
    def do_play(self):        
        pass 
class Mp3(Music):    
    def do_play(self):        
        print ("Playing .mp3 music!")   
class Ogg(Music):   
    def do_play(self):        
        print ("Playing .ogg music!")   
class MusicFactory(object):    
    def play_sound(self, object_type):        
        return eval(object_type)().do_play()  
if __name__ == "__main__":    
    mf = MusicFactory()    
    music = input("Which music you want to play Mp3 or Ogg")   
    mf.play_sound(music)
    
from types import MethodType
class Animal(object):      
    def __init__(self, *args, **kwargs):        
        self.name = kwargs.pop('name', None) or 'Animal'       
        if kwargs.get('walk', None):            
            self.walk = MethodType(kwargs.pop('walk'), self)   
    def walk(self):        
        """        Cause animal instance to walk               Walking functionality is a strategy, and is intended to        be implemented separately by different types of animals.        """        
        message = '{} should implement a walk method'.format(           self.__class__.__name__)        
        raise NotImplementedError(message)
    def snake_walk(self):    
        print('I am slithering side to side because I am a {}.'.format(self.name)) 
    def four_legged_animal_walk(self):    
        print('I am using all four of my legs to walk because I am a(n) {}.'.format(        self.name)) 
    def two_legged_animal_walk(self):    
        print('I am standing up on my two legs to walk because I am a {}.'.format(        self.name))
generic_animal = Animal() 
king_cobra = Animal(name='King Cobra', walk=snake_walk) 
elephant = Animal(name='Elephant', walk=four_legged_animal_walk)
kangaroo = Animal(name='Kangaroo', walk=two_legged_animal_walk)
kangaroo.walk() 
elephant.walk() 
king_cobra.walk()
generic_animal.walk()

from datetime import date 
from operator import attrgetter
class Proxy: 
    def __init__(self, current_user, reservation_service): 
        self.current_user = current_user 
        self.reservation_service = reservation_service
    def highest_total_price_reservations(self, date_from, date_to, reservations_count): 
        if self.current_user.can_see_reservations: 
            return self.reservation_service.highest_total_price_reservations(                date_from,                date_to,                reservations_count ) 
        else: 
            return []
            
class Reservation: 
    def __init__(self, date, total_price): 
        self.date = date 
        self.total_price = total_price
class ReservationService: 
    def highest_total_price_reservations(self, date_from, date_to, reservations_count): 
        reservations = [            Reservation(date(2014, 5, 15), 100),            Reservation(date(2017, 5, 15), 10),            Reservation(date(2017, 1, 15), 50) ]
        filtered_reservations = [r for r in reservations if (date_from <= r.date <= date_to)]        
        sorted_reservations = sorted(filtered_reservations, key=attrgetter('total_price'), reverse=True) 
        return sorted_reservations[0:reservations_count]
class User:
    def __init__(self, can_see_reservations, name): 
        self.can_see_reservations = can_see_reservations 
        self.name = name
class StatsService: 
    def __init__(self, reservation_service): 
        self.reservation_service = reservation_service 
    def year_top_100_reservations_average_total_price(self, year):        
        reservations = self.reservation_service.highest_total_price_reservations(            date(year, 1, 1),            date(year, 12, 31), 1 ) 
        if len(reservations) > 0:            
            total = sum(r.total_price for r in reservations) 
            return total / len(reservations)
            else: 
                return 0
def test(user, year):    
    reservations_service = Proxy(user, ReservationService())    
    stats_service = StatsService(reservations_service)    
    average_price = stats_service.year_top_100_reservations_average_total_price(year) 
    print("{0} will see: {1}".format(user.name, average_price))
    test(User(True, "John the Admin"), 2017) 
    test(User(False, "Guest"),         2017)
"""				"""
import unittest
class SomeTest(unittest.TestCase): 
    def setUp(self): 
        super(SomeTest, self).setUp() 
        self.mock_data = [1,2,3,4,5]
    def test(self): 
        self.assertEqual(len(self.mock_data), 5) 
    def tearDown(self):
        super(SomeTest, self).tearDown() 
        self.mock_data = [] 
if __name__ == '__main__': unittest.main()

import unittest import some_module
class SomeOtherTest(unittest.TestCase):
    def setUp(self): 
        super(SomeOtherTest, self).setUp()
        my_patch = mock.patch.object(some_module, 'method')        
        my_patch.start()
    self.addCleanup(my_patch.stop)
def division_function(dividend, divisor):   
    return dividend / divisor
class MyTestCase(unittest.TestCase):  
    def test_using_context_manager(self):        
        with self.assertRaises(ZeroDivisionError):            
            x = division_function(1, 0)
class MyTestCase(unittest.TestCase):    
    def test_using_context_manager(self):        
        with self.assertRaises(ZeroDivisionError) as ex:           
            x = division_function(1, 0)        
        self.assertEqual(ex.message, 'integer division or modulo by zero')
        
class WrongInputException(Exception):    
    pass
def convert2number(random_input):    
    try:       
        my_input = int(random_input)    
    except ValueError:        
        raise WrongInputException("Expected an integer!")   
    return my_input

import unittest
class ExceptionTestCase(unittest.TestCase):    
    def test_wrong_input_string(self):        
        self.assertRaises(WrongInputException, convert2number, "not a number")    
    def test_correct_input(self):        
        try:            
            result = convert2number("56")            
            self.assertIsInstance(result, int)        
        except WrongInputException:            
            self.fail()
            
import unittest 
class SimplisticTest(unittest.TestCase):    
    def test_basic(self):        
        self.assertTrue(1 + 1 == 2)
        self.assertTrue(1 + 1 == 3)
        
class Deque:
    def __init__(self): 
        self.items = []
    def isEmpty(self):
        return self.items == [] 
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item): 
        self.items.insert(0,item) 
    def removeFront(self): 
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0) 
    def size(self): 
        return len(self.items)
class Father(object):   
    pass
class Child(Father):   
    pass

class Stack:   
    def __init__(self):       
        self.items = []
    def isEmpty(self): 
        return self.items == []
    def push(self, item):        
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self): 
        return self.items[-1]
    def size(self): 
        return len(self.items)
    def fullStack(self):
        return self.items
stack = Stack() 
print('Current stack:', stack.fullStack()). 
print('Stack empty?:', stack.isEmpty()) 
print('Pushing integer 1') stack.push(1) 
print('Pushing string "Told you, I am generic stack!"') 
stack.push('Told you, I am generic stack!') 
print('Pushing integer 3')
stack.push(3)
print('Current stack:', stack.fullStack()) 
print('Popped item:', stack.pop()) 
print('Current stack:', stack.fullStack()) 
print('Stack empty?:', stack.isEmpty())

def checkParenth(str):    
    stack = Stack()    
    pushChars, popChars = "<({[", ">)}]"   
    for c in str:        
        if c in pushChars:           
            stack.push(c)        
        elif c in popChars:           
            if stack.isEmpty():                
                return False         
            else:                
                stackTop = stack.pop()                # Checks to see whether the opening bracket matches the closing one               
                balancingBracket = pushChars[popChars.index(c)]               
                if stackTop != balancingBracket:                    
                    return False        
                    
        else:            
            return False    
    return not stack.isEmpty()
class Car(object):   
    def __init__(self):        
        self.color = "red"        
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
"""				"""
class IntegerContainer(object): 
    def __init__(self, value): 
        self.value = value __ne__ and __eq__:
    def __repr__(self): 
        return "{}({})".format(self.__class__.__name__, self.value)
    def __lt__(self, other): 
        print('{!r} - Test less than {!r}'.format(self, other)) 
        return self.value < other.value 
    def __le__(self, other): 
        print('{!r} - Test less than or equal to {!r}'.format(self, other))
        return self.value <= other.value
    def __gt__(self, other): 
        print('{!r} - Test greater than {!r}'.format(self, other)) 
        return self.value > other.value 
    def __ge__(self, other): 
        print('{!r} - Test greater than or equal to {!r}'.format(self, other)) 
        return self.value >= other.value 
    def __eq__(self, other):
        print('{!r} - Test equal to {!r}'.format(self, other)) 
        return self.value == other.value
    def __ne__(self, other):
        print('{!r} - Test not equal to {!r}'.format(self, other)) 
        return self.value != other.value
alist = [IntegerContainer(5), IntegerContainer(3),         IntegerContainer(10), IntegerContainer(7) ]
res = max(alist)
print(res)
res = min(alist)  
print(res)
res = sorted(alist)
print(res)
res = sorted(alist, reverse=True)
print(res)
del IntegerContainer.__lt__ 
res = min(alist)
print(res)

import functools 
@functools.total_ordering 
class IntegerContainer(object):    
    def __init__(self, value):        
        self.value = value           
    def __repr__(self):        
        return "{}({})".format(self.__class__.__name__, self.value)
    def __lt__(self, other):        
        print('{!r} - Test less than {!r}'.format(self, other))        
        return self.value < other.value       
    def __eq__(self, other):       print('{!r} - Test equal to {!r}'.format(self, other))        
        return self.value == other.value       
    def __ne__(self, other):        
        print('{!r} - Test not equal to {!r}'.format(self, other))        
        return self.value != other.value
IntegerContainer(5) > IntegerContainer(6)
IntegerContainer(6) > IntegerContainer(5)

class ListList:    
    def __init__(self, value):        
        self.value = value              
        self.setofvalues = set(item for sublist in self.value for item in sublist) 
    def __iter__(self):        print('Using __iter__.') 
        return (item for sublist in self.value for item in sublist)
    def __contains__(self, value):        
        print('Using __contains__.')        
        return value in self.setofvalues
a = ListList([[1,1,1],[0,1,1],[1,5,1]])
10 in a 
5 in a 
del ListList.__contains__ 
5 in a 
"""				"""
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

class SwitchBase:    
    def switch(self, case):       
        m = getattr(self, 'case_{}'.format(case), None)        
        if not m:            
            return self.default        
        return m
    __call__ = switch
    
class CustomSwitcher:    
    def case_1(self):        
        return 'one'    
    def case_2(self):        
        return 'two'    
    def case_42(self):        
        return 'the answer of life, the universe and everything!'    
    def default(self):       
        raise Exception('Not a case!')
switch = CustomSwitcher()
print(switch(1))
print(switch(2))

class Switch:   
    def __init__(self, value):       
        self._val = value    
    def __enter__(self):      
        return self    
    def __exit__(self, type, value, traceback):       
        return False # Allows traceback to occur    
    def __call__(self, cond, *mconds):       
        return self._val in (cond,)+mconds
def run_switch(value):   
    with Switch(value) as case:       
        if case(1):           
            return 'one'        
        if case(2):           
            return 'two'       
        if case(3):           
            return 'the answer to the question about life, the universe and everything'   
         raise Exception('Not a case!')
run_switch(1)
