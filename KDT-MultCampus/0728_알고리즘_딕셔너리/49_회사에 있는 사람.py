# https://www.acmicpc.net/problem/7785

n = int(input())
entered = {}

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        entered[name] = 1
    else:
        entered.pop(name)
entered = sorted(entered, reverse=True)

for i in entered:
    print(i)