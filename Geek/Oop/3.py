class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 22)
]
# Filter people older than 25
filtered_people = list(filter(lambda person: person.age > 25, people))
for person in filtered_people:
    print(person.name, person.age)
