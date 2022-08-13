# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

my_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,}
a = int(input())
b = int(input())
c = int(input())

for idx in str(a * b * c):
    if idx in my_dict:
        my_dict[idx] += 1
        
for idx in my_dict:
    print(my_dict[idx]) 