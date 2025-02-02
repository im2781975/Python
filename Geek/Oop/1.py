class Dog:
    x = "molla"; y = "vai"
    def func(self):
        print("i am ", self.x)
        print("i am ", self.y)
    
dog = Dog()
print(dog.x, dog.y); dog.func()
"""                    """
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"MyError has occurred with value: {repr(self.value)}"
try:
    raise MyError(3 * 2)
except MyError as error:
    print('A New Exception occurred:', error.value)
    print('Error details:', str(error))
finally:
    print('Exception handling completed.')
"""                    """
class Error(Exception):
    pass
class zerodivision(Error):
    pass
while True:
    try:
        num = int(input("Enter a number (or type 'exit' to quit): "))
        if num == 0:
            raise zerodivision
        print(f"You entered: {num}")
        break 
    except zerodivision:
        print("Input value is zero, try again!\n")
    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        break
"""                    """
class Error(Exception):
    """Base class for other exceptions."""
    pass
class TransitionError(Error):
    """Raised when an operation is not allowed due to an invalid state transition."""
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.nex = nex
        self.msg = msg
    def __str__(self):
        return f"Transition from {self.prev} to {self.nex} is not allowed: {self.msg}"
try:
    raise TransitionError(2, 3 * 2, "Not Allowed")
except TransitionError as error:
    print('Exception occurred:', error.msg)
    print('Full Error Details:', error)
"""                        """
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise Networkerror("Error")
except Networkerror as e:
    print(e.args)
"""						"""
class student:
    depart = 'CSE'
    def __init__(self, roll):
        self.roll = roll
a = student(103)
b = student(104)
print(a.depart, b.depart, a.roll, b.roll, student.depart)
"""                    """
class operation:
    def __init__(self, value):
        self.value = value
    def __and__(self, other):
        print("And operator ")
        if isinstance(other, operation):
            return self.value & other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __or__(self, other):
        print("OR operator ")
        if isinstance(other, operation):
            return self.value | other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __xor__(self, other):
        print("XOR operator ")
        if isinstance(other, operation):
            return self.value ^ other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __lshift__(self, other):
        print("left shift operator ")
        if isinstance(other, operation):
            return self.value << other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __rshift__(self, other):
        print("right shift operator ")
        if isinstance(other, operation):
            return self.value >> other.value
        else:
            raise ValueError("Must be a object of class operation")
    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value
if __name__ == "__main__":
    a, b = operation(10), operation(20)
    print(a & b, a | b, a ^ b, a << b, a >> b, ~a)
"""                    """
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [ 
    person('Alice', 25), person('Bob', 30), person('Charlie', 22) ]
filtered = list(filter(lambda person: person.age > 25, people))
for person in filtered:
    print(person.name, person.age)
    
