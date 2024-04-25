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
