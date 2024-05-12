from abc import ABC,abstractmethod
class Resturent:
    def __init__(self, name):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = []
        self.expense = 0
        self.balance = 0
        self.revenue = 0
        self.profit = 0
    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'manager':
            self.manager = employee
        else employee_type == 'server':
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
class server(employe):
    def __init__(self, name, phone, email, address, salary, starting_date, depart, cooking_item):
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, depart)
        self.cooking_item = cooking_item
    def take_order(self, order):
        pass
    def transfer_order(self, order):
        pass
    def serve_food(self, order):
        pass
    def receive_tips(self, amount):
        tips_earning += amount
