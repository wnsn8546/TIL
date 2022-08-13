# https://www.acmicpc.net/problem/1305

N = int(input())
dict_ = {}
bestsellers = []

for i in range(N):
    name = input()
    if name in dict_:
        dict_[name] += 1
    else:
        dict_[name] = 1
max_num = max(dict_.values())

for k,v in dict_.items():
    if v == max_num:
        bestsellers.append(k)
print(sorted(bestsellers)[0])
