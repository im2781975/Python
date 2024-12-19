import collections
counts = collections.Counter([1,2,3])
collections.Counter('Happy Birthday')
collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-Iam'.split())

c = collections.Counter({'a': 4, 'b': 2, 'c': -2, 'd': 0})
c['c'] = -3
sum(c.itervalues()) 
list(c.elements())
c.update({'a': 3, 'b':3})
c.update({'a': 2, 'c':2})
Counter({'a': 5, 'b': 3, 'c': 2})
c.subtract({'a': 3, 'b': 3, 'c': 3}) 

d = {'foo': 5, 'bar': 6}
print(d)
d['baz'] = 7
print(a)

from collections import OrderedDict
d = OrderedDict([('foo', 5), ('bar', 6)]) 
print(d)

OrderedDict([('foo', 5), ('bar', 6)])
d['baz'] = 7 
print(d)

OrderedDict([('foo', 5), ('bar', 6), ('baz', 7)]) 
d['foobar'] = 8
print(d)

OrderedDict([('foo', 5), ('bar', 6), ('baz', 7), ('foobar', 8)])
o = OrderedDict()
o['key1'] = "value1"
o['key2'] = "value2"
print(o)

