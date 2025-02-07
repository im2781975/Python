class Instructor:
    print("Empty class")
    def __init__(self):
        print("Constructor")
instruc = Instructor()
instruc.name = "Hasan"
print(type(instruc),"\n", instruc.name)
"""                    """
class teacher:
    follower = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.follower = 0
    def show(self, sub):
        print(f"name: {self.name}, teach: {sub}, follower: {self.follower}, lived in: {self.address}");
    def update(self, namefollower):
        self.follower += 1
        print(f"name: {namefollower}\nfollower: {self.follower} ")
tr = teacher("Ab", "124 via villa")
tr.show("chem")
for i in range(5):
    tr.update("Hasan")
print(tr.follower)
"""                    """
class circle:
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def __init__(self, radius = 6):
        self.radius = radius
        self.area = circle.pi * radius * radius
    def circum(self):
        return 2 * circle.pi * self.radius
cir = circle(5.42)
print(cir.area, cir.circum())
"""        Multiple Inheritance        """
class human:
    def __init__(self, heart):
        self.eyes = 1; self.noses = 1;
        self.heart = heart
    def eat(self):
        print("eat")
    def work(self):
        print("work")
class male(human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name
    def flirt(self):
        print("flirt")
    def work(self):
        super().work()
    def show(self):
        print(f"name: {self.name}, have {self.heart}, do{self.work()} ")
        self.work()
class female:
    def __init__(self, name):
        self.name = name
    def flirt(self):
        print("flirt")
    def work():
        print("can code")
class boy(male, female):
    def __init__(self, name, heart, lang):
        male.__init__(self, name, heart)
        female.__init__(self, name)
        self.lang = lang
    def sleep(self):
        print("sleep")
    def work(self):
        print("cab test")
ml = male("Ab", 1); ml.show()
print(ml.noses, ml.eyes)
by = boy("Hasan", 1, "python")
by.flirt(); by.work();
print(boy.mro())
print(by.noses, by.heart, by.lang)
"""         MultiLevelHeritance        """
class human(object):
    breath = True
    def __init__(self, heart):
        self.heart = heart
        self.eyes = 2
    def eat(self):
        print("eat")
    def work(self):
        print("work")
class male(human):
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print("sleep")
class boy(male):
    def __init__(self, name, heart, dance):
        male.__init__(self, name)
        human.__init__(self, heart)
        self.dance = dance
    def work(self):
        #human.work(self)
        super().work()
        print("Can Code")
class programmer(boy):
    def work(self):
        print("Coded")
by = boy("Roy", 1, True)
by.eat(); by.work()
print(by.name, "\n", boy.mro())
prg = programmer("Molla", 2, False)
prg.work() 
"""        Heirical Inheritance        """
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self):
        print(f"name: {self.name}, age: {self.age} ")
    def eat(self):
        print("Can eat")
class Male(Human):
    def __init__(self, name, age, location):
        Human.__init__(self, name, age)
        self.location = location
    def sleep(self):
        print("Can sleep")
    def disp(self):
        print(f"name: {self.name}, age: {self.age}, location: {self.location} ")
class Female(Human):
    def __init__(self, name, age, dance):
        super().__init__(name, age)
        self.dance = dance
    def display(self):
        Human.disp(self)
        print(f"Dance: {self.dance} ")
    def work(self):
        print("Can code")
female = Female("Aslam", 24, True)
female.display(); female.eat()
male = Male("Molla", 25, "DCA")
male.disp()
"""            HibridHeritance        """
class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C:
    def show(self):
        print("C")
class D(B, C):
    def show(self):
        print("D")
x = D(); x.show();print(D.mro())
"""            DiamondHeritance        """
class A:
    def disp(self):
        print("A")
class B:
    def disp(self):
        print("B")
class C(A):
    def show(self):
        print("Class C")
    def show(self):
        print("Disp C")
class D(B, C):
    pass
d = D(); d.disp(); d.show()

