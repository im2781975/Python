https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s
def split_string(S):
    count = 0
    balance_strings = []
    count_X = 0
    count_Y = 0

    for char in S:

        if char == 'L':

            count_X += 1

        elif char == 'R':

            count_Y+= 1


        if count_X== count_Y:

            balance_strings.append(S[:count_X + count_Y])

            count += 1

            S = S[count_X + count_Y:]

            count_X = 0

            count_Y = 0


    return count, balance_strings

S = input().strip()

count, balance_strings = split_string(S)

print(count)

for string in balance_strings:

    print(string)
->https://atcoder.jp/contests/arc087/tasks/arc087_a
from collections import defaultdict


n = int(input())

a = list(map(int, input().split()))


mp = defaultdict(int)

for num in a:

    mp[num] += 1


ans = 0

for num, count in mp.items():

    if count < num:

        ans += count

    else:

        ans += count - num


print(ans)

->Write Python program to solve Minimize Number
def maximum(N, A):

    count = 0


    while all(numbers % 2 == 0 for numbers in A):

        A = [numbers // 2 for numbers in A]

        count =count+1


    return  count
N = int(input(""))

A_str = input("")

A = list(map(int, A_str.split()))


maximum_operation = maximum(N, A)

print("",maximum_operation)

->Take a number from the user and draw a pyramid using PyAutoGUI
import pyautogui

n = int(input())  

for i in range(1,n+1):  

    pyautogui.write("#"*i, interval=0.001)  

    pyautogui.press('enter')

