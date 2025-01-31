class person:
    def __init__(self, name, age, height, weight) ->None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
class cricketer(person):
    def __init__(self, name, age, height, weight) ->None:
        super().__init__(name, age, height, weight)
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
sakib = cricketer('Sakib', 38, 68, 91)
mushi= cricketer('Mushfiq', 36, 55, 82)
riyad = cricketer('Riyad', 39, 72, 92)
youngest = min([sakib, mushi, riyad])
elder = max([sakib, mushi, riyad])
print(f"Younger player {youngest.name}\nElder player {elder.name} ")
