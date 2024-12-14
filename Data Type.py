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
