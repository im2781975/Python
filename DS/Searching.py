alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
5 in alist  
10 in alist  

atuple = ('0', '1', '2', '3', '4')
4 in atuple    
'4' in atuple  

astring = 'i am a string' 
'a' in astring   
'am' in astring 
'I' in astring   

aset = {(10, 10), (20, 20), (30, 30)}
(10, 10) in aset  
10 in aset    

adict = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
1 in adict                
'a' in adict             
2 in adict.keys()          
'a' in adict.values()     
(0, 'a') in adict.items()

class ListList:    
    def __init__(self, value):        
        self.value = value              
        self.setofvalues = set(item for sublist in self.value for item in sublist) 
    def __iter__(self):        print('Using __iter__.') 
        return (item for sublist in self.value for item in sublist)
    def __contains__(self, value):        
        print('Using __contains__.')        
        return value in self.setofvalues
a = ListList([[1,1,1],[0,1,1],[1,5,1]])
10 in a 
5 in a 
del ListList.__contains__ 
5 in a 

astring = 'Hello on StackOverflow'
astring.index('o')  
astring.rindex('o')
astring.find('o')  
astring.rfind('o')
astring.find('q')
astring.index('o', 5)   
astring.index('o', 6)   
astring.index('o', 5, 7) 
astring.index('o', 5, 6)
astring.rindex('o', 20)
astring.rindex('o', 19) 

alist = [10, 16, 26, 5, 2, 19, 105, 26]
alist.index(16)
alist[1]  

atuple = (10, 16, 26, 5, 2, 19, 105, 26)
atuple.index(26)  
atuple[2]          
atuple[7]    

def getKeysForValue(dictionary, value):    
    foundkeys = []    
    for keys in dictionary:        
        if dictionary[key] == value:            
            foundkeys.append(key)    
    return foundkeys
def getKeysForValueComp(dictionary, value):    
    return [key for key in dictionary if dictionary[key] == value]
def getOneKeyForValue(dictionary, value):   
    return next(key for key in dictionary if dictionary[key] == value)
adict = {'a': 10, 'b': 20, 'c': 10} 
getKeysForValue(adict, 10)    
getKeysForValueComp(adict, 10) 
getKeysForValueComp(adict, 20) 
getKeysForValueComp(adict, 25) 
getOneKeyForValue(adict, 10) 
getOneKeyForValue(adict, 20) 
getOneKeyForValue(adict, 25)

import bisect 
def index_sorted(sorted_seq, value):   
    """Locate the leftmost value exactly equal to x or raise a ValueError"""
    i = bisect.bisect_left(sorted_seq, value)    
    if i != len(sorted_seq) and sorted_seq[i] == value:        
        return i    
    raise ValueError
alist = [i for i in range(1, 100000, 3)] 
index_sorted(alist, 97285)  
index_sorted(alist, 4)   

%timeit index_sorted(alist, 97285)
%timeit alist.index(97285)
%timeit index_sorted(alist, 4)
%timeit alist.index(4)

def outer_index(nested_sequence, value): 
    return next(index for index, inner in enumerate(nested_sequence) for item in inner if item == value)
alist_of_tuples = [(4, 5, 6), (3, 1, 'a'), (7, 0, 4.3)] 
outer_index(alist_of_tuples, 'a') 
outer_index(alist_of_tuples, 4.3) 

def outer_inner_index(nested_sequence, value): 
    return next((oindex, iindex) for oindex, inner in enumerate(nested_sequence) for iindex, item in enumerate(inner) if item == value)
outer_inner_index(alist_of_tuples, 'a') 
alist_of_tuples[1][2]
outer_inner_index(alist_of_tuples, 7)  
alist_of_tuples[2][0] 
