# https://www.acmicpc.net/problem/10816

N = int(input())
list_1 = list(map(int, input().split()))
M = int(input())
list_2 = list(map(int, input().split()))

my_dict = {list_2[i] : 0 for i in range(len(list_2))}

for i in list_1:
    if i in my_dict:
        my_dict[i] += 1

for i in my_dict:
    print(my_dict[i], end = ' ')