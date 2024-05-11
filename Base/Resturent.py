from abc import ABC,abstractmethod
class user:
    def __init__(self, name):
        self.name = name
class customer(user):
    def __init__(self, name, money):
        self.wallet = money
        self.__order = None
        super().__init(name)
    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self, order):
        self.__order = order
