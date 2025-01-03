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
