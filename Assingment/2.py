class person:
    def __init__(self, name, age, height, weight) ->None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
class cricketer(person):
    def __init__(self, name, age, height, weight) ->None:
        super().__init__(name, age, height, weight)
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
sakib = cricketer('Sakib', 38, 68, 91)
mushi= cricketer('Mushfiq', 36, 55, 82)
riyad = cricketer('Riyad', 39, 72, 92)
youngest = min([sakib, mushi, riyad])
elder = max([sakib, mushi, riyad])
print(f"Younger player {youngest.name}\nElder player {elder.name} ")
"""					"""
class bank:
    def __init__(self, balance):
        self.balance = balance
        self.mini = 100
        self.maxi = 1000000
    def get(self):
        return self.balance
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"New balance is: {self.get()} ")
    def withdraw(self, amount):
        if amount > self.mini and amount < self.maxi and amount < self.balance:
            self.balance -= amount
            print(f"Withdrawal amount is {amount} & Remaining Balance is {self.balance} ")
        else:
            print("Enter amount correctly")
x = bank(15000)
x.withdraw(1200)
x.deposite(2700)

class bank:
    def __init__(self, name, initial):
        self.name = name
        self._branch = 'Banani'
        self.__balance = initial
    def deposite(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f"Insufficient Balance "
    def get(self):
        return self.__balance
xyz = bank('abc', 5000)
xyz.deposite(1000); xyz.withdraw(500)
print(xyz.get(), dir(xyz))
"""			"""
class shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []
    def add(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
        if total > amount:
            print(f"please provide {total - amount} ")
        else:
            print(f"Here is your remaining {amount - total} ")
x = shop('vai')
x.add('A', 12, 15)
x.add('B', 22, 5)
x.add('C', 9, 29)
x.checkout(400)
"""					"""
class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class store:
    def __init__(self):
        self.__itemprice = {}
        self.__itemquantity = {}
        self.__profit = 0
    def add(self, name, price, quantity):
        item = product(name, price, quantity)
        self.__itemprice[item.name] = item.price
        self.__itemquantity[item.name] = item.quantity
    def buy(self, name, quantity):
        if name in self.__itemprice:
            if self.__itemquantity[name] >= quantity:
                self.__profit += ((5 * self.__itemprice[name]) / 100)* quantity
                self.__itemquantity[name] -= quantity
            else:
                print("unavailable")
        else:
            print("Not Found")
    @property
    def show(self):
        print(self.__itemprice)
        print(self.__itemquantity)
    def show_profit(self):
        print(self.__profit)
class shop(store):
    def __init__(self, name):
        self.shop_name = name
        super().__init__()
x = shop("xyz")
x.add("abc", 400, 15); x.add("bcd", 200, 20)
x.show
x.buy("abc", 2)
x.show
x.show_profit()
"""        AbstractBaseClass        """
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def eat(self):
        print("Eating")
    @abstractmethod
    def move(self):
        print("Moving")
class monkey(animal):
    def __init__(self, name):
        self.category = "king"
        self.name = name
        super().__init__()
    def eat(self):
        print("eat")
    def move(self):
        print("Hang")
x = monkey("mn")
x.eat(); x.move()
"""                    """
class phone:
    menufactured = 'china'
    def __init__(self, owner, price, brand):
        self.owner = owner
        self.price = price
        self.brand = brand
    def send(self, phone, txt):
        print(f"send from {phone} encrypted {txt} ")
x = phone('A', 1200, 'B')
print(x.owner, x.brand, x.price)
x.send('xphone','Dj')
"""                    """
class shop:
    cart = []
    def __init__(self, user):
        self.user = user
        self.creditCard = []
    def add(self, item):
        self.cart.append(item)
        self.creditCard.append(item)
    def show(self):
        print(f"items included in shop cart is {self.cart}, User cart is {self.creditCard}")
x = shop('xyz')
x.add('C'); x.add('D'); x.show()
y = shop('abcd')
y.add('E'); y.add('F'); y.show()
print(y.cart, y.creditCard)
"""					"""
class Engine:
    def __init__(self, Type) -> None:
        self.Type = Type
    def start(self) -> None:
        return f"Engine started"
class Driver:
    def __init__(self, name, address):
        self.name = name
        self.address = address
class car:
    def __init__(self, Type, name, address) -> None:
        self.engine = Engine(Type)
        self.driver = Driver(name, address)
    def start(self):
        return f"{self.engine.start()}"
car = car("V8", "Mollavai", " 123 via street")
print(car.start())
"""                    """
class CPU:
    def __init__(self, core)->None:
        self.core = core
class Ram:
    def __init__(self, size)->None:
        self.size = size
class HardDrive:
    def __init__(self, cap)->None:
        self.cap = cap
class computer:
    def __init__(self, core, size, cap)->None:
        self.cpu = CPU(core)
        self.ram = Ram(size)
        self.drive = HardDrive(cap)
    def show(self):
        return f"core {self.cpu.core}\nram size: {self.ram.size}\ndrive capacity: {self.drive.cap} "
mac = computer(8, 16, 512)
print(mac.show())
"""            Decorator            """
class user:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money
    def getAge(self):
        return self._age
    #decorator can modify a function in attribute
    # getter without any setter is read only attribute
    @property
    def getName(self):
        return self._name
    @property
    def salary(self):
        return self.__money
    @salary.setter
    def salary(self, val):
        if val < 0:
            return f"can't negetive"
        self.__money += val
a = user('x', 12, 1223)
print(a._age, a.getAge())#used as attribute & method
print(a._name)#used as attribute
a.salary = 200; print(a.salary)
"""                """
class vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"vehicle brand: {self.name}\nprice: {self.price} "
class bus(vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)
class AcBus(bus):
    def __init__(self, name, price, seat, temp):
        self.temp = temp
        super().__init__(name, price, seat)
    def __repr__(self):
        print(f"Bus brand: {self.name}\nprice: {self.price}\nit has: {self.seat} seats & holds {self.temp}°c")
        return super().__repr__()
class Truck(vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)
class pickup(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
    def __repr__(self):
        return f"truck brand: {self.name}\ntruck price: {self.price}\ntruck weight: {self.weight} "
x = AcBus('abc', 500000, 22, 16)
y = pickup('xyz', 700000, 200)
print(x); print(y)
print(issubclass(vehicle, Truck))
print(isinstance(vehicle, Truck))
print(isinstance(vehicle, AcBus))
"""            Polymarphizm        """
class animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Aa")
class cat(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Bb")
class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Cc")
class goat(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Dd")
c = cat("c")
d = dog("d")
g = goat("g")
anim = [c, d, g]
for i in anim:
    i.sound()
"""                    """
from math import pi
class shape:
    def __init__(self, name):
        self.name = name
class rect(shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)
    def area(self):
        return self.length * self.width
    def __repr__(self):
        return f"area of {self.name} with length {self.length} & {self.width} is: {self.area()} "
class circle(shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius
    def __repr__(self):
        return f"area of {self.name} with radius {self.radius} is: {self.area()} "
x = circle('circle', 22)
y = rect('rectangle', 12, 23)
print(x, x.area())
print(y, y.area())
"""                    """
class student:
    def __init__(self, name, lev, id):
        self.name = name
        self.lev = lev; self.id = id
    def __repr__(self):
        return f"student name: {self.name}\nclass: {self.lev}\nid: {self.id}\n"
class teacher:
    def __init__(self, name, sub, id):
        self.name = name
        self.sub = sub; self.id = id
    def __repr__(self):
        return f"Teacher name: {self.name}\nsubject: {self.sub}\nid: {self.id}\n"
class school:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    def addTeacher(self, name, sub):
        id = len(self.teachers) + 101
        teach = teacher(name, sub, id)
        self.teachers.append(teach)
    def enroll(self, name, fee):
        if fee < 6500:
            return f"please provide more"
        else:
            id = len(self.students) + 1
            std = student(name, 'D', id)
            self.students.append(std)
            return f"enrolled name: {std.name}\nreturned money: {fee - 6500}\nid: {std.id} "
    def __repr__(self):
        output = f"School Name: {self.name}\n\nTeachers:\n"
        for teacher in self.teachers:
            output += f"{teacher}\n"
        output += "Students:\n"
        for student in self.students:
            output += f"{student}\n"
        return output
a = school('XYZ School')
print(a.enroll('Bob', 5200))  
print(a.enroll('Charlie', 6700))  
a.addTeacher('David', 'English')
a.addTeacher('Fiona', 'Mathematics')
print(a)
"""                    """
class instructor:
    def __init__(self):
        print("constructor")
a = instructor(); a.name = "molla"
b = instructor(); b.name = "vai"
print(a.name, b.name)
"""             OVERRIDE           """
class person:
    def __init__(self, name, age, height, weight):
        self.name = name; self.age = age
        self.height = height; self.weight = weight
    def eat(self):
        print("Eating")
    def exercise(self):
        raise NotImplementedError
class cricketer(person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    def eat(self):
        print("Eat rice")
    def exercise(self):
        print("Go To Gym")
    def __add__(self, other):
        return self.age + other.age
    def __mul__(self, other):
        return self.age * other.age
    def __len__(self):
        return self.height
    def __gt__(self, other):
        return self.height > other.height
sakib = cricketer('A', 35, 79,79,'BD')
sakib.eat(); sakib.exercise()
Mushi = cricketer('B', 35, 78,78,'BD')
print(sakib + Mushi, sakib * Mushi, len(sakib), sakib < Mushi)
"""                    """
class family:
    def __init__(self, address):
        self.address = address
class school:
    def __init__(self, id, level):
        self.id = id
        self.level = level
class sport:
    def __init__(self, game):
        self.game = game
class student(family, school, sport):
    def __init__(self, address, id, level, game):
        family.__init__(self, address)
        school.__init__(self, id, level)
        sport.__init__(self, game)
    def show(self):
        return (f"address :{self.address}\nid: {self.id}\nlevel: {self.level}\nGame liked: {self.game} ")
std = student("123 Main St", "A123", "High School", "Basketball")
print(std.show())
"""           Methode         """
class shop:
    cart = []
    origin = 'china'
    def __init__(self, name, location):
        self.name = 'E-BAZAR'
        self.location = 'BGD'
    def purches(self, item, price, amount):
        print(f"Buying: {item} which price: {price} remaining amount: {amount - price} ")
    #class method can access without useof instance
    #static mathod can't change or print class info
    @staticmethod
    def mult(a, b):
        print(a * b)
    @classmethod
    def show(self, item):
        print(item)
shop.purches('a', 4, 2, 2)
a = shop('DARAZ', 'Banani')
a.purches('xyz', 1200, 2000)
a.show('Lungi'); shop.show('Lungi')
shop.mult(8, 4); a.mult(8, 2)
"""                    """
class calculator:
    def add(self, a, b):
        return a + b
    def deduct(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a
    def mult(self, a, b):
        return a * b
    def subtract(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Can't Divide by zero")
x = calculator()
print(x.add(6, 9), x.subtract(6, 0))
"""                    """
class Device:
    def __init__(self, brand, price, color, origin):
        self.brand = brand; self.price = price
        self.color = color; self.origin = origin
    def run(self):
        return f"running: {self.brand}\nwhich color: {self.color}\norigin from: {self.origin}"
class phone(Device):
    def __init__(self, brand, price, color, origin, duality):
        self.duality = duality
        super().__init__(brand, price, color, origin)
    def call(self, num, sms):
        return f"sending from {num}\nEncrypted txt is {sms}"
    def __repr__(self) -> str:
        return f"Brand: {self.brand}\nColor: {self.color}\nOrigin: {self.origin}\nIsDuality: {self.duality}\n"
x = phone('iphone', 12000, 'silver', 'chine', True); print(x)
print(x.call("915653960", "Reached home")); print(x.run())

class phone:
    brand = 'Iphone'; price = 2200; color = 'silver'
    feature = ['Camera', 'Speaker', 'Duality']
    def call(self):
        print("Calling")
    def send(self, cellNo, txt):
        return f"sending from {cellNo}\nEncrypted txt is: {txt}"
x = phone(); x.call()
print(x.brand, x.price, x.color, x.feature)
print(x.send("915653960", "am I"))
"""            Represent            """
class Represent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):       
        return "Represent(x = {}, y = \" {} \")".format(self.x, self.y)
    def __str__(self):        
        return "Representing x as {} and y as {}".format(self.x, self.y)
r = Represent(1, "Goto")
print(r, r.__repr__, r.__repr__())
print(r.__repr__() == eval(r.__repr__()))
"""                    """
class car:
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']
    def __repr__(self):
        return f"speed is: {self.speed} color is: {self.color}\n"
audi = car(s = 200, c = "Grey")
bmw = car(s = 150, c = "Golden")
print(audi.color, bmw.speed)
print(audi, bmw)
"""                    """
class circle:
    def __init__(self, radius):
        self.radius = radius
    def calculateArea(self):
        return 3.1416 * self.radius * self.radius
x = circle(7); print(x.calculateArea())
"""                    """
class Test:
    def __init__(self):
        self.ing = "mollavai"
        self.x = 50
def fun():
    return Test()
t = fun()
print(t.ing, t.x)
"""            ENUM            """
from enum import Enum
class color(Enum):
    red = 1; green = 2; blue = 3
print(color.red, color(2), color['red'])
print([c for c in color])
