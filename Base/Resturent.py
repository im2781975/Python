from abc import ABC,abstractmethod
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
        self.starting_date = starting_date
        self.depart = depart

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
    
