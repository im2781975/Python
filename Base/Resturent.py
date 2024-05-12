from abc import ABC,abstractmethod
class Resturent:
    def __init__(self, name, rent, menu = []):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = menu
        self.rent = rent
        self.expense = 0
        self.balance = 0
        self.revenue = 0
        self.profit = 0
    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'manager':
            self.manager = employee
        elif employee_type == 'server':
            self.server = employee
    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
    def pay_expences(self, amount, description):
        if amount < self.balance:
            self.balance -= amount
            self.expence += amount
        else:
            print(f'Not Enough money to pay {amount}')
    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.receive_salary()
    def show_employee(self):
        if self.chef is not None:
            print(f'{self.chef.name} with salary {self.chef.salary}')
        if self.manager is not None: 
            print(f'{self.manager.name} with salary {self.manager.salary}')
class user:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class customer(user):
    def __init__(self, name, phone, email, address, money):
        self.wallet = money
        self.__order = None
        super().__init(name, phone, email, address)
    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self, order):
        self.__order = order
    def place_order(self, order):
        self.order = order
        print(f'{self.name} {order.items}')
    def eat(self, order):
        print(f'{self.name} {order.items} ' )
    def pay_for_order(self, amount):
        # TODO : sibmit the money to manager
        pass
    def give_tips(self, tips_amount):
        pass
    def write_review(self, stars):
        pass
class employe(user):
    def __init__(self, name, phone, email, address, salary, starting_date, depart):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.depart = depart
        
    def receive_salary(self):
        self.due = 0
class chef(employe):
    def __init__(self, name, phone, email, address, salary, starting_date, depart, cooking_item):
        super().__init__(name, phone, email, address, salary, starting_date, depart)
        self.cooking_item = cooking_item
class Manager(employe):
    def __init__(self, name, phone, email, address, salary, starting_date, depart):
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, depart)
class server(employe):
    def __init__(self, name, phone, email, address, salary, starting_date, depart):
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, depart)
    def take_order(self, order):
        pass
    def transfer_order(self, order):
        pass
    def serve_food(self, order):
        pass
    def receive_tips(self, amount):
        tips_earning += amount
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cooking_time = 15
class Burger(Food):
    def __init__(self, name, price, meat, ingredients):
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients
class pizza(Food):
    def __init__(self, name, price, size, topping):
        super().__init__(name, price)
        self.size = size
        self.topping = topping
class drinks(Food):
    def __init__(self, name, price, iscold = True):
        super().__init__(name, price)
        self.iscold = iscold
class menu:
    def __init__(self):
        self.burgers = []
        self.pizzas = []
        self.drinks = []
    def add_menu_item(self, item_type, item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drink':
            self.drinks.append(item)
    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
    def show_menu(self):
        for pizza in self.pizzas:
            print(f'{pizza.name} {pizza.price} ')
        for burger in self.burgers:
            print(f'{burger.name} {burger.price} ')
        for drink in self.drinks:
            print(f'{drink.name} {drink.price} ')
x = pizza('A', 1200, 'L', ['B', 'C'])
Menu = menu()
Menu.add_menu_item('pizza', x)
y = Burger('B', 2300, 'M', ['C', 'D'])
Menu.add_menu_item('burger', y)
Menu.show_menu()
#def main():
rest = Resturent('A', 2000, menu)
manager = Manager('Z', 234, 'Y', 'X', 456, '2000', 'core')
rest.add_employee('manager', manager)
chef = chef('Z', 234, 'Y', 'X', 456, '2000', 'core', 'chinese')
rest.add_employee('chef', chef)
rest.show_employee()


