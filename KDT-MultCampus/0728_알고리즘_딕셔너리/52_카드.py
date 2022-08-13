# https://www.acmicpc.net/problem/11652

N = int(input())
num_dict = {}
max_list = []

for i in range(N):
    num = int(input())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
max_num = max(num_dict.values())

for k,v in num_dict.items():
    if v == max_num:
        max_list.append(k)
print(sorted(max_list)[0])

