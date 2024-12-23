class IntegerContainer(object): 
    def __init__(self, value): 
        self.value = value __ne__ and __eq__:
    def __repr__(self): 
        return "{}({})".format(self.__class__.__name__, self.value)
    def __lt__(self, other): 
        print('{!r} - Test less than {!r}'.format(self, other)) 
        return self.value < other.value 
    def __le__(self, other): 
        print('{!r} - Test less than or equal to {!r}'.format(self, other))
        return self.value <= other.value
    def __gt__(self, other): 
        print('{!r} - Test greater than {!r}'.format(self, other)) 
        return self.value > other.value 
    def __ge__(self, other): 
        print('{!r} - Test greater than or equal to {!r}'.format(self, other)) 
        return self.value >= other.value 
    def __eq__(self, other):
        print('{!r} - Test equal to {!r}'.format(self, other)) 
        return self.value == other.value
    def __ne__(self, other):
        print('{!r} - Test not equal to {!r}'.format(self, other)) 
        return self.value != other.value
alist = [IntegerContainer(5), IntegerContainer(3),         IntegerContainer(10), IntegerContainer(7) ]
res = max(alist)
print(res)
res = min(alist)  
print(res)
res = sorted(alist)
print(res)
res = sorted(alist, reverse=True)
print(res)
del IntegerContainer.__lt__ 
res = min(alist)
print(res)

import functools 
@functools.total_ordering 
class IntegerContainer(object):    
    def __init__(self, value):        
        self.value = value           
    def __repr__(self):        
        return "{}({})".format(self.__class__.__name__, self.value)
    def __lt__(self, other):        
        print('{!r} - Test less than {!r}'.format(self, other))        
        return self.value < other.value       
    def __eq__(self, other):       print('{!r} - Test equal to {!r}'.format(self, other))        
        return self.value == other.value       
    def __ne__(self, other):        
        print('{!r} - Test not equal to {!r}'.format(self, other))        
        return self.value != other.value
IntegerContainer(5) > IntegerContainer(6)
IntegerContainer(6) > IntegerContainer(5)


