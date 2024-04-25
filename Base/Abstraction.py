from abc import ABC,abstractmethod
#abstractbaseclass
class animal(ABC):
    @abstractmethod
    #enforced all derived class to have a eat method
    def eat(self):
        print("Eating")
    @abstractmethod
    def move(self):
        print("Hanging")
class monkey(animal):
    def __init__(self, name):
        self.category = 'king'
        self.name = name
        super().__init__()
    def eat(self):
        print("Food")
    def move(self):
        print("Hanging")
x = monkey("xy")
x.eat()
x.move()
