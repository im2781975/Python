import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))
print(heapq.nsmallest(4, numbers)) 

people = [    {'firstname': 'John', 'lastname': 'Doe', 'age': 30},    {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},    {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},    {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},    {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},    {'firstname': 'John', 'lastname': 'Roe', 'age': 45} ]
oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest)
youngest = heapq.nsmallest(2, people, key=lambda s: s['age']) 
print(youngest)

numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8] 
heapq.heapify(numbers)
heapq.heappop(numbers)
print(numbers)
