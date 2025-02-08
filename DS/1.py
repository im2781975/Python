class lst:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return repr(self.val)
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.val[item])        
        return [self.val[i] for i in item] 
    def __setitem__(self, item, value):  
        if isinstance(item, int):        
            self.val[item] = value
        elif isinstance(item, slice):    
            raise ValueError('Cannot interpret slice with multiindexing')        
        else:           
            for i in item:                
                if isinstance(i, slice):   
                    raise ValueError('Cannot interpret slice with multiindexing')
                self.val[i] = value   
    def __delitem__(self, item):        
        if isinstance(item, int):     
            del self.val[item]        
        elif isinstance(item, slice):     
            del self.val[item]        
        else:           
            if any(isinstance(elem, slice) for elem in item):        
                raise ValueError('Cannot interpret slice with multiindexing')       
            item = sorted(item, reverse = True)            
            for elem in item:           
                del self.val[elem]
l = lst([1, 2, 3, 4, 5, 6, 7, 8])
print(l[4], l[1], l[5:], l[::2])
l[4] = 1000; l[2, 6, 1] = 100
del(l[4, 2, 5])
print(l[::1])
"""				"""
import operator
class integral(object):   
    def __init__(self, val):        
        self.val = int(val)
    def __repr__(self):        
        return '{cls}( {val} )'.format(cls = self.__class__.__name__, val = self.val)
    def __pow__(self, other, module = None):        
        if module is None:           
            return self.__class__(self.val ** other)       
        else:  
            return self.__class__(pow(self.val, other, module)) 
    def __float__(self):      
        return float(self.val)       
    def __complex__(self):        
        return complex(self.val, 0)
x = integral(5)
print(x, x ** 5, x.__pow__(3, 7), float(x), complex(x))
print(integral(5) ** 8, pow(integral(2), 0.5))
print(operator.pow(integral(2), 3), operator.__pow__(integral(3), 3))
print(pow(integral(2), 3, 4), integral(2).__pow__(3, 4))

"""				"""
class Instructor:
    print("Empty class")
    def __init__(self):
        print("Constructor")
instruc = Instructor()
instruc.name = "Hasan"
print(type(instruc),"\n", instruc.name)
"""                    """
class teacher:
    follower = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.follower = 0
    def show(self, sub):
        print(f"name: {self.name}, teach: {sub}, follower: {self.follower}, lived in: {self.address}");
    def update(self, namefollower):
        self.follower += 1
        print(f"name: {namefollower}\nfollower: {self.follower} ")
tr = teacher("Ab", "124 via villa")
tr.show("chem")
for i in range(5):
    tr.update("Hasan")
print(tr.follower)
"""                    """
class circle:
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def __init__(self, radius = 6):
        self.radius = radius
        self.area = circle.pi * radius * radius
    def circum(self):
        return 2 * circle.pi * self.radius
cir = circle(5.42)
print(cir.area, cir.circum())
"""        Multiple Inheritance        """
class human:
    def __init__(self, heart):
        self.eyes = 1; self.noses = 1;
        self.heart = heart
    def eat(self):
        print("eat")
    def work(self):
        print("work")
class male(human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name
    def flirt(self):
        print("flirt")
    def work(self):
        super().work()
    def show(self):
        print(f"name: {self.name}, have {self.heart}, do{self.work()} ")
        self.work()
class female:
    def __init__(self, name):
        self.name = name
    def flirt(self):
        print("flirt")
    def work():
        print("can code")
class boy(male, female):
    def __init__(self, name, heart, lang):
        male.__init__(self, name, heart)
        female.__init__(self, name)
        self.lang = lang
    def sleep(self):
        print("sleep")
    def work(self):
        print("cab test")
ml = male("Ab", 1); ml.show()
print(ml.noses, ml.eyes)
by = boy("Hasan", 1, "python")
by.flirt(); by.work();
print(boy.mro())
print(by.noses, by.heart, by.lang)
"""         MultiLevelHeritance        """
class human(object):
    breath = True
    def __init__(self, heart):
        self.heart = heart
        self.eyes = 2
    def eat(self):
        print("eat")
    def work(self):
        print("work")
class male(human):
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print("sleep")
class boy(male):
    def __init__(self, name, heart, dance):
        male.__init__(self, name)
        human.__init__(self, heart)
        self.dance = dance
    def work(self):
        #human.work(self)
        super().work()
        print("Can Code")
class programmer(boy):
    def work(self):
        print("Coded")
by = boy("Roy", 1, True)
by.eat(); by.work()
print(by.name, "\n", boy.mro())
prg = programmer("Molla", 2, False)
prg.work() 
"""        Heirical Inheritance        """
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self):
        print(f"name: {self.name}, age: {self.age} ")
    def eat(self):
        print("Can eat")
class Male(Human):
    def __init__(self, name, age, location):
        Human.__init__(self, name, age)
        self.location = location
    def sleep(self):
        print("Can sleep")
    def disp(self):
        print(f"name: {self.name}, age: {self.age}, location: {self.location} ")
class Female(Human):
    def __init__(self, name, age, dance):
        super().__init__(name, age)
        self.dance = dance
    def display(self):
        Human.disp(self)
        print(f"Dance: {self.dance} ")
    def work(self):
        print("Can code")
female = Female("Aslam", 24, True)
female.display(); female.eat()
male = Male("Molla", 25, "DCA")
male.disp()
"""            HibridHeritance        """
class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C:
    def show(self):
        print("C")
class D(B, C):
    def show(self):
        print("D")
x = D(); x.show();print(D.mro())
"""            DiamondHeritance        """
class A:
    def disp(self):
        print("A")
class B:
    def disp(self):
        print("B")
class C(A):
    def show(self):
        print("Class C")
    def show(self):
        print("Disp C")
class D(B, C):
    pass
d = D(); d.disp(); d.show()
"""        ABSTRACTION            """
from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self, n):
        self.type = n
    @abstractmethod
    def start(self):
        pass
    def disp(self):
        print("calling from vehicle")
class bike(vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("Bike start")
    def disp(self):
        print("")
class scooty(vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("Scooty start")
class car(vehicle):
    def __init__(self, n, gear):
        super().__init__(n)
        self.gear = 6
    def start(self):
        print("Car start")
bk = bike(2, "black")
bk.start()
"""          Access Modifier          """
class student:
    def __init__(self, name, roll, age):
        self.name = name
        self._roll = roll
        self.__age = age
    def __display(self):
        print(f"{self.name}\n{self._roll}\n{self.__age}")
    def dispData(self):
        self.__display()
class branch(student):
    pass
def showData():
    std = branch("Hasan", 21, 22)
    print(std.name, std._roll)
showData()
std = student("Molla", 34, 23)
print(std.dispData())
std._student__display()
print(dir(std))
"""            ENCAPSULATION            """
class student:
    def __init__(self, name, roll, age):
        self.name = name
        self._roll = roll; self.__age = age
    def getage(self):
        return self._age
    def setage(self, age):
        if self.__age > 35:
            print("should be less than 35")
        else:
            self.__age = age
    def __disp(self):
        print(f"name: {self.name}, roll: {self._roll}, age: {self.__age} ")
    def show(self):
        self.__disp()
class branch(student):
    def showData(self):
        print(f"name: {self.name}, roll: {self._roll}, age: {self.__age} ")
std = student("Aa", 29, 35)
std.setage(49)
print(std.show()); std._student__disp()
print(dir(std))
"""            DUCK TYPING            """
class duck:
    def swim(self):
        print("duck swim")
    def speak(self):
        print("duck speak")
class dog:
    def swim(self):
        print("dog swim")
    def speak(self):
        print("dog speak")
def disp(obj):
    obj.swim(); obj.speak()
class demo:
    def disp(self, obj):
        obj.swim(); obj.speak()
d = duck(); disp(d)
dm = demo(); dm.disp(d)
"""            OVERRIDING            """
class complexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __add__(self, other):
        return f"{self.real + other.real} + {self.img + other.img}i" 
a, b = complexNum(1, 2), complexNum(4, 5)
print(a + b)
"""            """
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        self.age > other.age
x = person("Aa", 22)
y = person("Bb", 23)
if x > y:
    print(f"{x.name} pay the bill")
else:
    print(f"{y.name} pay the bill")
"""            """
class father:
    def sleep(self):
        print("sleep")
class son(father):
    def sleep(self):
        print("sleeping")
        super().sleep()
s = son(); s.sleep()
"""                """
class author:
    def __init__(self, name, bookname, pages):
        self.name = name
        self.bookname = bookname; self.pages = pages
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"{self.name} wrote {self.bookname} which has {self.pages}"
    def __call__(self, *args, **kwargs):
        print("Hi")
    def __del__(self):
        print("Has been deleted")
inf = author("Aa", "Bb", 124)
print(len(inf), str(inf), inf)
inf(7, 9); del inf
"""                """
class Bank:
    def __init__(self, name, balance = 9):
        self.holder = name
        self.balance = balance
    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited amount is {self.amount} ")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
    def __str__(self):
        return f"Holder name: {self.holder}\nBalanced: {self.balance}"
UCB = Bank("Aa", 9000)
print(UCB, str(UCB), Bank.mro())
