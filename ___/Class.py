"""class Instructor:
    print("Empty class")
    def __init__(self):
        print("Constructor")
instruc = Instructor()
instruc.name = "Hasan"
print(type(instruc),"\n", instruc.name)
"""
class Instructor:
    follower = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        #self.follower = 0
    def display(self, subject):
        print(f"Hi, name {self.name}, i teach {subject}")
    def updateFollower(self, followerName):
        self.follower += 1
        print(f"{self.follower}, {followerName} ")
ins = Instructor("Ab", "Cd")
print(ins.name, ins.follower)
ins.display("python")
ins.updateFollower("pial")
print(ins.follower)

class CIRCLE:
    PI = 3.1416
    """
    def __init__(self, radius):
        self.radius = radius
    """
    #default value
    def __init__(self, radius = 6):
        self.radius = radius 
        self.area = CIRCLE.PI * radius * radius
    def circum(self):
        return 2 * self.PI * self.radius
cir = CIRCLE(5.43)
print(cir.circum(),"\n",cir.circum)
cir = CIRCLE()
print(cir.area)

class HUMAN:
    def __init__(self, Heart):
        self.eyes = 2
        self.noses = 1
        self.heart = Heart
    def eat(self):
        print("Can eat")
    def work(self):
        print("Can work")
class Male(HUMAN):
    #super can add class method
    def __init__(self, name, heart):
        self.name = name
        super().__init__(heart)
    def flirt(self):
        print("Can flirt")
    #super can add method, without super it will override
    def work(self):
        super().work()
        print("Can code")
    def display(self):
        print(f"Hi name is {self.name}, Heart\'s are {self.heart} ")
male = Male("Akash", 1)
male.work()
print("Noses are:" ,male.noses)
print(male.heart)
male.display()

"""       Multiple Inveritance       """
class HUMAN:
    def __init__(self, heart):
        print("Calling from HUMAN")
        self.noses = 1
        self.eyes = 2
        self.heart = heart
    def eat(self):
        print("Can eat")
    def work(self):
        print("Can work")
class Male:
    def __init__(self, name):
        print("Calling from Male")
        self.name = name
    def flirt(self):
        print("Can flirt")
    def work(self):
        print("Can Code")
class Boy(HUMAN, Male):
    def __init__(self, name, heart, language):
        self.language = language
        Male.__init__(self, name)
        HUMAN.__init__(self, heart)
    def sleep(self):
        print("Can sleep")
    def work(self):
        print("can test")
#boy = Boy()
boy = Boy("Hasan", 1, "python")
boy.flirt(); boy.work(); Male.work(boy)
print(Boy.mro())
print(boy.noses, boy.heart, boy.language)
"""        MultilevelHeritance        """
class HUMAN(object):
    Breath = True
    def __init__(self, heart):
        print("Calling")
        self.eyes = 2
        self.heart = heart
    def eat(self):
        print("Can Eat")
    def work(self):
        print("can work")
class Male(HUMAN):
    def __init__(self, name):
        print("Calling from")
        self.name = name
    def sleep(self):
        print("Can sleep")
class Boy(Male):
    def __init__(self, name, heart, dance):
        HUMAN.__init__(self, heart)
        Male.__init__(self, name)
        self.dance = dance
    def work(self):
        #HUMAN.work(self)
        super().work()
        print("Can Code")
class programmer(Boy):
    def work(self):
        print("Coded")
#boy = Boy(1)
boy = Boy("Roy", 1, True)
boy.eat(); boy.work()
print(boy.name, "\n", Boy.mro())
prg = programmer("Molla", 2, False)
prg.work() 
print(boy.name, boy.Breath, boy.heart, boy.dance)
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
"""        Hibrid Inheritance        """
class A:
    def disp(self):
        print("Class A")
class B(A):
    def disp(self):
        print("Class B")
class C:
    def show(self):
        print("Class C")
class D(B, C):
    def disp(self):
        print("Class D")
d = D()
d.disp(); print(D.mro())
"""		Diamond Inheritance		"""
class A:
    def disp(self):
        print("Class A")
class B(A):
    def disp(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
    def show(self):
        print("Disp C")
class D(B, C):
    pass
d = D()
d.disp()

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
"""            Encapsulation            """
class student:
    def __init__(self, name, roll, age):
        self.name = name
        self._roll = roll
        self.__age = age
    def getAge(self):
        return self.__age
    def setAge(self, age):
        if age > 35:
            print("should be less than 35")
        else:
            self.__age = age
    def __display(self):
        print(f"{self.name}\n{self._roll}\n{self.__age}")
    def dispData(self):
        self.__display()
class branch(student):
    def show(self):
        print(f"Roll is: {self._roll} ")
std = student("Molla", 34, 23)
print(std.dispData())
std._student__display()
print(dir(std))
print(std.getAge())
std.setAge(34)
print(std.getAge())
"""            DUCK TYPING            """
class Duck:
    def swim(self):
        print("Duck swim")
    def speak(self):
        print("Duck speak")
class Dog:
    def swim(self):
        print("Dog swim")
    def speak(self):
        print("Duck speak")
def display(obj):
        obj.swim()
        obj.speak()
class demo:
    def disp(self, obj):
        obj.swim()
        obj.speak()
d = Duck()
dog = Dog()
display(dog)
dm = demo()
dm.disp(d)
"""            OVERRIDING            """
class complexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __add__(self, other):
        return f"{self.real + other.real} + {self.img + other.img}i" 
a, b = complexNum(1, 2), complexNum(4, 5)
print(a + b)
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
x = person("Aa", 22)
y = person("Bb", 23)
if x > y:
    print(f"{x.name} pay the bill")
else:
    print(f"{y.name} pay the bill")
    
class father:
    def sleep(self):
        print("sleep")
    def eat(self):
        print("eat")
class son(father):
    def sleep(self):
        print("sleeping")
        super().sleep()
r = son()
r.sleep()
class author:
    def __init__(self, name, bookName, pages):
        self.name = name
        self.bookName = bookName
        self.pages = pages
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"{self.name} wrote {self.bookName} "
    def __call__(self, *args, **kwargs):
        print("Hi")
    def __del__(self):
        print("Has been deleted")
d = author("Aa", "Bb", 200)
print(len(d), d)
d()
del d
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
        return f"{self.holder} \n{self.balance} "
obj = Bank("Aa", 7000)
obj.deposite(500)
print(obj)
