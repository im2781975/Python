import collections
counts = collections.Counter([1, 2, 3])
counts = collections.Counter('Happy Birthday')
counts = collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-Iam'.split())
counts = collections.Counter({'a': 4, 'b': 2, 'c': -2, 'd': 0})
counts['c'] = -3
counts.update({'a': 3, 'b' : 3})
counts.update({'a': 2, 'c' : 2})
counts.subtract({'a': 3, 'b': 3, 'c': 3})
print(sum(counts.values()))
print(counts.elements())
"""                    """
from collections import deque
deq = deque('ghi')
deq.append('j')
deq.appendleft('bc')
deq.pop()
deq.popleft()
deq.extend('jkl')
deq.extendleft('mnk')
print(deque.reverse(deq))
deq.rotate(1)
deq.rotate(-1)
print(list(deq))
print(list(reversed(deq)))
print('h' in deq)
for val in deq:
    print(val.upper(), end = "")
deq.clear()
deq = deque([1, 2, 3])
deq.popleft()
deq.appendleft(5)
dl = deque()
#dl = deque(maxlen = 100)
dl.append(2)
dl.extend([6, 7])
dl.extendleft([-2, -1])
dl.pop_left()
dl.remove(1)
dl.reverse()
"""                """
def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                q.append(neighbor)
    return distance
graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
result = bfs(graph, 1)
print(result)
"""					"""
import operator
print(operator.pow(4, 2), operator.__pow__(4, 3))
x, y = 2, 6
print(x.__pow__(y), y.__rpow__(x))
import math
print(math.pow(2, 2), math.pow(2, -2), math.pow(-2, 5), math.e ** 2, math.exp(2), math.exp(10), math.exp(10).real)
print(math.e ** 1e-3 - 1, math.exp(1e-3) - 1, math.expm1(1e-3), math.e ** 1e-15 - 1, math.exp(1e-15) - 1, math.expm1(1e-15))
"""                    """
import math
from decimal import Decimal
import cmath
print(math.sqrt(9), math.sqrt(11.11), Decimal('6.25').sqrt())
print(cmath.sqrt(4), cmath.sqrt(-4))
"""                    """
def modularInverse(x, p):
    return pow(x, p - 2, p)
print([modularInverse(x, 13) for x in range(1,13)])
"""                    """
import heapq
num = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, num))
print(heapq.nsmallest(4, num))
heapq.heapify(num)
heapq.heappop(num)
print(num)
"""				"""
people = [{'firstname': 'John', 'lastname': 'Doe', 'age': 30},    
        {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},    
        {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},  
        {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},    
        {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},    
        {'firstname': 'John', 'lastname': 'Roe', 'age': 45}]
oldest = heapq.nlargest(2, people, key = lambda s : s['age'])
youngest = heapq.nsmallest(2, people, key = lambda s : s['age'])
print(oldest, youngest)
"""				"""
from operator import *
print(add(a, b), sub(a, b), truediv(a, b), floordiv(a, b))
"""            """
import math
a, b = 1, 2
print(math.sinh(a), math.cosh(a), math.atan(math.pi), math.hypot(a, b), math.degree(a), math.radians(57.29577951308232))
"""            """
import cmath
complex_num = cmath.sqrt(-1) 
while complex_num: 
    print(complex_num)  
"""				"""
import random
num = random.randint(0, 12)
print(str(num))
"""				"""
import random
laugh = ["Aa", "Bb", " Cc"]
random.shuffle(laugh)
print(laugh, random.choice(laugh))
print(random.sample(laugh, 1), random.sample(laugh, 2), random.sample(laugh, 3))
print(random.randint(1, 100), random.randrange(100), random.randrange(20, 50), random.randrange(10, 20, 3), random.random(), random.uniform(1, 8))
random.seed(5)
print(random.randrange(0, 10), random.randrange(0, 10))
random.seed(5)
print(random.randrange(0, 10))
"""            """
state = random.getstate()
random.setstate(state)
print(state)
random.seed(None)
random.seed()
"""            """
probability = 0.3
if random.random() < probability:    
    print("Decision with probability 0.3") 
else:    
    print("Decision with probability 0.7")
    
from Queue import Queue 
question_queue = Queue() 
for x in range(1,10):   
    temp_dict = ('key', x)    
    question_queue.put(temp_dict) 
while(not question_queue.empty()):    
    item = question_queue.get()    
    print(str(item))
