#decorator can modify a function in attribute
class user:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money
    def age(self):
        return self._age
    # getter without any setter is read only attribute
    @property
    def name(self):
        return self._name
    @property
    def salary(self):
        return self.__money
    #setter
    @salary.setter
    def salary(self, val):
        if val < 0:
            return f'Can\' negetive'
        self.__money += val
a = user('x', 12, 1223)
print(a._age)#used as attribute
print(a.age())#used as method
print(a.name)#used as attribute
print(a.salary)
a.salary = 200
print(a.salary)
