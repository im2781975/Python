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
