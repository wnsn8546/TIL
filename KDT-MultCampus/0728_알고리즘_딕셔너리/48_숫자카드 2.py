# https://www.acmicpc.net/problem/10816

from collections import Counter

N = int(input())
list_1 = list(map(int, input().split()))
M = int(input())
list_2 = list(map(int, input().split()))
result = []

cnt = Counter(list_1)
for i in list_2:
    if i in cnt:
        result.append(cnt[i])
    else:
        result.append(0)
for i in result:
    print(i, end =' ')