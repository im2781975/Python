string = "GFG"
ch_iterator = iter(string)
 
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
////
# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value
 
# An iterable user defined type
class Test:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1;
        return x
 
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)
 
# Prints nothing
for i in Test(5):
    print(i)
 /////
# Sample built-in iterators
 
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")    
s = "Geeks"
for i in s :
    print(i)
     
# Iterating over dictionary
print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
/////
tup = ('a', 'b', 'c', 'd', 'e')
 
for item in tup:
    print(item)
/////
tup = ('a', 'b', 'c', 'd', 'e')
 
# creating an iterator from the tuple
tup_iter = iter(tup)
 
print("Inside loop:")
# iterating on each item of the iterator object
for index, item in enumerate(tup_iter):
    print(item)
 
    # break outside loop after iterating on 3 elements
    if index == 2:
        break
 
# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))
/////
iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)
 
print("Iterable loop 1:")
# iterating on iterable
for item in iterable:
    print(item, end=",")
 
print("\nIterable Loop 2:")
for item in iterable:
    print(item, end=",")
 
print("\nIterating on an iterator:")
# iterating on an iterator object multiple times
for item in iterator_obj:
    print(item, end=",")
 
print("\nIterator: Outside loop")
# this line will raise StopIteration Exception
# since all items are iterated in the previous for-loop
print(next(iterator_obj))
//////

