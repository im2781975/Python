# simple match case statement
def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    
    # match case
    match num:
        # pattern 1
        case 1:
            print("One")
        # pattern 2
        case 2:
            print("Two")
        # pattern 3
        case 3:
            print("Three")
        # default pattern
        case _:
            print("Number not between 1 and 3")
            
runMatch()
////
# python match case with OR operator
def runMatch():
    num = int(input("Enter a number between 1 and 6: "))
    
    # match case
    match num:
        # pattern 1
        case 1 | 2:
            print("One or Two")
        # pattern 2
        case 3 | 4:
            print("Three or Four")
        # pattern 3
        case 5 | 6:
            print("Five or Six")
        # default pattern
        case _:
            print("Number not between 1 and 6")
            
runMatch()
////
# python match case with if condition
def runMatch():
    num = int(input("Enter a number: "))
    
    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")
            
runMatch()
////
# match case to check a character in a string
def runMatch():
    myStr = "Hello World"
     
    # match case
    match (myStr[6]):
        case "w":
            print("Case 1 matches")
        case "W":
            print("Case 2 matches")
        case _:
            print("Character not in the string")
            
runMatch()
////
# python match case with list
def runMatch(mystr):
    
    # match case
    match mystr:
        # pattern 1
        case ["a"]:
            print("a")
        # pattern 2
        case ["a", *b]:
            print(f"a and {b}")
        # pattern 3
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e")
        # default pattern
        case _:
            print("No data")
            
runMatch([])
runMatch(["a"])
runMatch(["a", "b"])
runMatch(["b", "c", "d", "e"])
////
# match case with python dictionaryu
def runMatch(dictionary):
    # match case
    match dictionary:
        # pattern 1
        case {"name": n, "age": a}:
            print(f"Name:{n}, Age:{a}")
        # pattern 2
        case {"name": n, "salary": s}:
            print(f"Name:{n}, Salary:{s}")
        # default pattern
        case _ :
            print("Data does not exist")

runMatch({"name": "Jay", "age": 24})
runMatch({"name": "Ed", "salary": 25000})
runMatch({"name": "Al", "age": 27})
runMatch({})
////
# match case with python classes
# import dataclass module
from dataclasses import dataclass

#Class 1
@dataclass
class Person:
    name: str
    age: int
    salary: int

# class 2
@dataclass
class Programmer:
    name: str
    language: str
    framework: str

def runMatch(instance):
    # match case
    match instance:
        # pattern 1
        case Programmer("Om", language="Python", framework="Django"):
            print(f"Name: Om, Language:Python, Framework:Django")
        # pattern 2
        case Programmer("Rishabh", "C++"):
            print("Name:Rishabh, Language:C++")
        # pattern 3
        case Person("Vishal", age=5, salary=100):
            print("Name:Vishal")
        # pattern 4
        case Programmer(name, language, framework):
            print(f"Name:{name}, Language:{language}, Framework:{framework}")
        # pattern 5
        case Person():
            print("He is just a person !")
        # default case
        case _:
            print("This person is nothiing!")

programmer1 = Programmer("Om", "Python", "Django")
programmer2 = Programmer("Rishabh", "C++", None)
programmer3 = Programmer("Sankalp", "Javascript", "React")
person1 = Person("Vishal", 5, 100)
runMatch(programmer1)
runMatch(programmer2)
runMatch(person1)
runMatch(programmer3)
////
def match_example(value):
    match value:
        case 1:
            return "The value is 1"
        case 2:
            return "The value is 2"
        case _:
            return "The value is something else"
print(match_example(1))  # Output: The value is 1
print(match_example(3))  # Output: The value is something else

