num = [10, 0, -1, 7, 8, -67]
name = ["Ab", "Cd"]
mix_list = [3, "Ef", True, 10.87]
print(num, name, mix_list)
print(num[2], num[-1])
print(num[0:4], num[0:], num[:4], num[0:4:2], num[4:0], num[4:0:-1])
print(f"lenth is: {len(num)}")
#print(num.sort()) #output None
num.sort();
print(num, max(num), min(num));
num.append(45)
num.extend([46, 47, 48, 49])#For append more value
num[1] = -95 
num[1:4]  =[97, 98, 99] #[pos:len] = values
x = input("Enter digit: ");
if x in num:
    num.remove(97)
else:
    print(f"doesn't exits")
#num.remove(97) #remove first occurance
print(num.pop()) #will remove last element
print(num.pop(1)) #num.pop(idx)
num.insert(2, 78)#(pos, value)
print(num.count(0)) #count elements
print(f"After append & insertion num is: {num} ")

#Nested list
num = [1, 10, 15, [20, -10, 15], 17, -20]
print(len(num))
print(num[3][1], num[len(num) -1])
#slice
print(num[3][0:3], num[3][-1:3], num[3][::-1])
#num[3][-1:3] num[pos][pos:length]
num = [1, 10, 15, ["Aa", "Bb", "Cc"], 17, -20]
print(num[3][0:3], num[3][-1:3], num[3][::-1], num[3][2])

#Dict
#num = { 'A': 123, 'B': 235,'C': 789,'A' : 666,}
#duplicate key will be override
#num = dict({ 'A': 123, 'B': 235,'C': 789,'A' : 666,})
num = dict([('A', 1234), ('B', 2345), ('C', 3456)])
num['D'] = {4567, 7777, 9999}
num['B'] ={'Home':9876, 'work':5432}
num['A'] = 2345
print(num)
print(num['A'])
print(num['B'], num['B']['work'])
print(num.get('B'))
for i in num:
    print(i)
    print(num[i])
#it will print dictionary or tuple pair
for i in num.items():
    print(i)
#copy
xyz = num.copy()
print("--")
print(xyz)
print(len(xyz))
print("--")
data = {
    1: 'abc', 2: 'bcd', 0: 'cde',
}
print(data[0])
print(data.keys())
print(data.values())
print(data.items())
#for delete key
del data[2]
#print(data.pop(0))
print(data.popitem())
data.clear()
print(data)
