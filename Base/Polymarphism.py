from math import pi
class shape:
    def __init__(self, name):
        self.name = name
class rect(shape):
    def _init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)
    def area(self):
        return self.length * self.width
class circle(shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)
    def area(self):
        return self.radius * pi
x = circle('x', 5)
print(x.area())
"""
class animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Sound")
class cat(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("meow")
class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("gheo")
class goat(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("he he")
x = cat("x")
y = dog("y")
z = goat("z")
ani = [x, y, z]
for a in ani:
    a.sound()
"""
