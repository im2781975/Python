dict = {
  1: 'Python', 
  2: 'dictionary', 
  3: 'example'
}
///
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)
///
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

////
Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
////
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)
////
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
////
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using key:")
print(Dict[1])
////
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Accessing a element using get:")
print(Dict.get(3))
////
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
////
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dictionary =")
print(Dict)
del(Dict[1]) 
print("Data after deletion Dictionary=")
print(Dict)
////
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())
////
# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}
# Accessing values by keys
print(my_dict['key1'])  # Output: value1
# Modifying values
my_dict['key2'] = 'new_value'
# Adding new key-value pairs
my_dict['key3'] = 'value3'
# Removing a key-value pair
del my_dict['key1']
////
# Empty dictionary
empty_dict = {}
# Dictionary with initial values
my_dict = {'key1': 'value1', 'key2': 'value2'}
////
my_dict = {'name': 'Alice', 'age': 30}
# Accessing keys and values
print(my_dict.keys())    # Output: dict_keys(['name', 'age'])
print(my_dict.values())  # Output: dict_values(['Alice', 30])
///
my_dict = {'A': 10, 'B': 20, 'C': 0}
print(all(my_dict.values()))   # False (0 evaluates to False)
print(any(my_dict.values()))   # True (at least one value is True)
print(sorted(my_dict))         # ['A', 'B', 'C'] (sorted keys)
////

