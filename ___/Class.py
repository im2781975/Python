"""class Instructor:
    print("Empty class")
    def __init__(self):
        print("Constructor")
instruc = Instructor()
instruc.name = "Hasan"
print(type(instruc),"\n", instruc.name)
"""
class Instructor:
    follower = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        #self.follower = 0
    def display(self, subject):
        print(f"Hi, name {self.name}, i teach {subject}")
    def updateFollower(self, followerName):
        self.follower += 1
        print(f"{self.follower}, {followerName} ")
ins = Instructor("Ab", "Cd")
print(ins.name, ins.follower)
ins.display("python")
ins.updateFollower("pial")
print(ins.follower)

class CIRCLE:
    PI = 3.1416
    """
    def __init__(self, radius):
        self.radius = radius
    """
    #default value
    def __init__(self, radius = 6):
        self.radius = radius 
        self.area = CIRCLE.PI * radius * radius
    def circum(self):
        return 2 * self.PI * self.radius
cir = CIRCLE(5.43)
print(cir.circum(),"\n",cir.circum)
cir = CIRCLE()
print(cir.area)

class HUMAN:
    def __init__(self, Heart):
        self.eyes = 2
        self.noses = 1
        self.heart = Heart
    def eat(self):
        print("Can eat")
    def work(self):
        print("Can work")
class Male(HUMAN):
    #super can add class method
    def __init__(self, name, heart):
        self.name = name
        super().__init__(heart)
    def flirt(self):
        print("Can flirt")
    #super can add method, without super it will override
    def work(self):
        super().work()
        print("Can code")
    def display(self):
        print(f"Hi name is {self.name}, Heart\'s are {self.heart} ")
male = Male("Akash", 1)
male.work()
print("Noses are:" ,male.noses)
print(male.heart)
male.display()

"""       Multiple Inveritance       """
class HUMAN:
    def __init__(self, heart):
        print("Calling from HUMAN")
        self.noses = 1
        self.eyes = 2
        self.heart = heart
    def eat(self):
        print("Can eat")
    def work(self):
        print("Can work")
class Male:
    def __init__(self, name):
        print("Calling from Male")
        self.name = name
    def flirt(self):
        print("Can flirt")
    def work(self):
        print("Can Code")
class Boy(HUMAN, Male):
    def __init__(self, name, heart, language):
        self.language = language
        Male.__init__(self, name)
        HUMAN.__init__(self, heart)
    def sleep(self):
        print("Can sleep")
    def work(self):
        print("can test")
#boy = Boy()
boy = Boy("Hasan", 1, "python")
boy.flirt(); boy.work(); Male.work(boy)
print(Boy.mro())
print(boy.noses, boy.heart, boy.language)
"""        MultilevelHeritance        """
class HUMAN(object):
    Breath = True
    def __init__(self, heart):
        print("Calling")
        self.eyes = 2
        self.heart = heart
    def eat(self):
        print("Can Eat")
    def work(self):
        print("can work")
class Male(HUMAN):
    def __init__(self, name):
        print("Calling from")
        self.name = name
    def sleep(self):
        print("Can sleep")
class Boy(Male):
    def __init__(self, name, heart, dance):
        HUMAN.__init__(self, heart)
        Male.__init__(self, name)
        self.dance = dance
    def work(self):
        #HUMAN.work(self)
        super().work()
        print("Can Code")
class programmer(Boy):
    def work(self):
        print("Coded")
#boy = Boy(1)
boy = Boy("Roy", 1, True)
boy.eat(); boy.work()
print(boy.name, "\n", Boy.mro())
prg = programmer("Molla", 2, False)
prg.work() 
print(boy.name, boy.Breath, boy.heart, boy.dance)
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
"""        Hibrid Inheritance        """
class A:
    def disp(self):
        print("Class A")
class B(A):
    def disp(self):
        print("Class B")
class C:
    def show(self):
        print("Class C")
class D(B, C):
    def disp(self):
        print("Class D")
d = D()
d.disp(); print(D.mro())
"""			Diamond Inheritance			"""
class A:
    def disp(self):
        print("Class A")
class B(A):
    def disp(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
    def show(self):
        print("Disp C")
class D(B, C):
    pass
d = D()
d.disp()
