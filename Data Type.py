#class
class Represent(object):    
    def __init__(self, x, y):       
        self.x, self.y = x, y    
    def __repr__(self):       
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)   
    def __str__(self):        
        return "Representing x as {} and y as {}".format(self.x, self.y)
r = Represent(1, "Hopper") 
print(r)
print(r.__repr__) 
rep = r.__repr__()  
print(rep)  
r2 = eval(rep) 
print(r2)  
print(r2 == r)
#Enum
from enum import Enum
class Color(Enum):    
    red = 1    
    green = 2    
    blue = 3 
print(Color.red)  
print(Color(1))  
print(Color['red']) 

class Colour(Enum):   
    red = 1   
    green = 2   
    blue = 3
[c for c in Colour]

class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


# creating objects of car class
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)
///
# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


# creating objects of car class
audi = Car(s=200, c='red')
bmw = Car(s=250, c='black')
mb = Car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)

class GeeksforGeeks:
    def __init__(self, topic):
        self.topic = topic
 
    def display_topic(self):
        print("Topic:", self.topic)
 
# Creating an instance of GeeksforGeeks
gfg_instance = GeeksforGeeks("Python")
 
# Calling the display_topic method
gfg_instance.display_topic()
/////
class Circle:
    def __init__(self, radius):
        self.radius = radius
 
    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return area
 
# Creating an instance of Circle
circle_instance = Circle(5)
 
# Calling the calculate_area method
print("Area of the circle:", circle_instance.calculate_area())
////
class Test: 
    def __init__(self): 
        self.str = "geeksforgeeks"
        self.x = 20   
  
# This function returns an object of Test 
def fun(): 
    return Test() 
      
# Driver code to test above method 
t = fun()  
print(t.str) 
print(t.x)
////
