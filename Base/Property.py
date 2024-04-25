class user:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money
    def age(self):
        return self._age
    @property
    def name(self):
        return self.name
a = user('x', 12, 1223)
print(a._age)#used as attribute
print(a.age())#used as method
print(a.name)#used as attribute
