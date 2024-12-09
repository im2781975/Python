d = {"a": 1, "b": 2, "c": 3}
for key in d:    
    print(key)
for key in d.keys():    
    print(key)
for key in d.iterkeys():    
    print(key)
for value in d.values():    
    print(value)
for key, value in d.items():    
    print(key, "::", value)

#buidin
d = dict()                  
d = dict(key='value')         
d = dict([('key', 'value')])
d = dict(**otherdict)  

#modify
d['newkey'] = 42
d['new_list'] = [1, 2, 3] 
d['new_dict'] = {'nested_dict': 1}
del d['newkey']

mydict = {}
print(mydict) 
print(mydict.get("foo", "bar"))
print(mydict) 
print(mydict.setdefault("foo", "bar"))
print(mydict)
try:
    value = mydict[key] 
except KeyError:    
    value = default_value
if key in mydict:   
    value = mydict[key]
else:    
    value = default_value
    
d = {'a': 1, 'b': 2, 'c':3}
for key in d:    
    print(key, d[key])
for key, value in d.items():    print(key, value)
for key, value in d.values():    print(key, value)
print([key for key in d])

from collections import defaultdict 
d = defaultdict(int)
d['key']                        
d['key'] = 5
d['key']                         
d = defaultdict(lambda: 'empty') 
d['key']                         
d['key'] = 'full'
d['key']          
d = {}
d.setdefault('Another_key', []).append("This worked!")
