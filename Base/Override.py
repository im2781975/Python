class person:
    def __init__(self, name, age, height, weight)->None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print("Eat")
    def exercise(self):
        raise NotImplementedError 
class cricketer(person):
    def __init__(self, name, age, height, weight, team)->None:
        self.team = team
        super().__init__(name, age, height, weight)
    def eat(self):
        print("Eating")
    def exercise(self):
        print("Go To GYM")
    #'+' overload
    def __add__(self, other):
        return self.age + other.age
    #'*'overload
    def __mul__(self, other):
        return self.age * other.age
    #'len' overload
    def __len__(self):
        return self.height
    def __gt__(self, other):
        return self.height > other.height
sakib = cricketer('A', 35, 79,79,'BD')
sakib.eat()
sakib.exercise()
Mushi = cricketer('B', 35, 78,78,'BD')
print(sakib + Mushi)
print(sakib * Mushi)
print(len(sakib))
print(sakib < Mushi)
