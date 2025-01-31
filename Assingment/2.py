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
