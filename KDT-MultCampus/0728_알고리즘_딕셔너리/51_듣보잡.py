# https://www.acmicpc.net/problem/1764

N, M = map(int, input().split())
my_dict = {}
result = []

for i in range(N+M):
    name = input()
    if name not in my_dict:
        my_dict[name] = 1
    else:
        my_dict[name] += 1
for k,v in my_dict.items():
    if v == 2:
        result.append(k)
result = sorted(result)

print(len(result))
for i in result:
    print(i)