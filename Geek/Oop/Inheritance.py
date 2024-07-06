# A Python program to demonstrate inheritance
class Person(object):
   
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()
////
class Emp(Person):
   
  def Print(self):
    print("Emp class called")
     
Emp_details = Emp("Mayank", 103)
 
# calling parent class function
Emp_details.Display()
 
# Calling child class function
Emp_details.Print()
////
# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
 
 
class Person(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is an employee
    def isEmployee(self):
        return False
 
 
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
 
    # Here we return true
    def isEmployee(self):
        return True
 
 
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
 
emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
////
# Python code to demonstrate how parent constructors
# are called.
 
# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
 
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()
//////
class A:
    def __init__(self, n='Rahul'):
        self.name = n
 
class B(A):
    def __init__(self, roll):
        self.roll = roll
 
object = B(23)
print(object.name)
////
# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
/////
# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age, dob):
    self.sName = name
    self.sAge = age
    self.dob = dob
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)
 
obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()
/////
# Python example to show the working of multiple
# inheritance
 
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
 
 
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
 
 
class Derived(Base1, Base2):
    def __init__(self):
 
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.str1, self.str2)
 
 
ob = Derived()
ob.printStrs()
////
# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
 
class Base(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
 
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
 
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
# Inherited or Sub class (Note Person in bracket)
 
 
class GrandChild(Child):
 
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
 
    # To get address
    def getAddress(self):
        return self.address
 
 
# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
/////
# Python program to demonstrate private members
# of the parent class
 
class C(object):
    def __init__(self):
        self.c = 21
 
        # d is private instance variable
        self.__d = 42
 
 
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
 
object1 = D()
 
# produces an error as d is private instance variable
print(object1.c)
print(object1.__d)
/////

