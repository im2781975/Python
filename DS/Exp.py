2 ** 3 
2 ** -3
(-2) ** (0.5)

import operator 
operator.pow(4, 2)      
operator.__pow__(4, 3) 

val1, val2 = 4, 2 
val1.__pow__(val2)      
val2.__rpow__(val1)

import math math.sqrt(9)            
math.sqrt(11.11)        
math.sqrt(Decimal('6.25'))

import cmath 
cmath.sqrt(4)  
cmath.sqrt(-4)

pow(3, 4, 17)
3 ** 4 % 17 

def modular_inverse(x, p):    
    """Find a such as  a·x ≡ 1 (mod p), assuming p is prime."""    
    return pow(x, p-2, p)
[modular_inverse(x, 13) for x in range(1,13)]

x = 2 ** 100 
cube = x ** 3
root = cube ** (1.0 / 3)


def nth_root(x, n):    # Start with some reasonable bounds around the nth root.    
    upper_bound = 1    
    while upper_bound ** n <= x:        
        upper_bound *= 2    
    lower_bound = upper_bound // 2    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:        
        mid = (lower_bound + upper_bound) // 2        
        mid_nth = mid ** n        
        if lower_bound < mid and mid_nth < x:            
            lower_bound = mid        
        elif upper_bound > mid and mid_nth > x:            upper_bound = mid        
        else:            # Found perfect nth root.            
            return mid    
    return mid + 1 x = 2 ** 100 
cube = x ** 3 
root = nth_root(cube, 3)
x == root

import math 
math.pow(2, 2)    
math.pow(-2., 2)

math.pow(2, 2+0j)
math.pow(-2, 0.5)

import math
math.e ** 2  
math.exp(2)

import cmath 
cmath.e ** 2 
cmath.exp(2) 

print(math.e ** 10)      
print(math.exp(10))       
print(cmath.exp(10).real)

import math
print(math.e ** 1e-3 - 1)  
print(math.exp(1e-3) - 1)  
print(math.expm1(1e-3)) 

print(math.e ** 1e-15 - 1) 
print(math.exp(1e-15) - 1)  
print(math.expm1(1e-15))

def planks_law(lambda_, T):    
    from scipy.constants import h, k, c 
    return 2 * h * c ** 2 / (lambda_ ** 5 * math.expm1(h * c / (lambda_ * k * T))) 
def planks_law_naive(lambda_, T):   
    from scipy.constants import h, k, c  
    return 2 * h * c ** 2 / (lambda_ ** 5 * (math.e ** (h * c / (lambda_ * k * T)) - 1)) 
planks_law(100, 5000)  
planks_law_naive(100, 5000) 
planks_law(1000, 5000)      
planks_law_naive(1000, 5000)

