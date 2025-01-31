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
"""								"""
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
"""								"""
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
