chess = [1, 1, 2, 2, 2 ,8]
dongheok = list(map(int, input().split()))
result = []

for i in range(len(chess)):
    result.append(chess[i] - dongheok[i])

for i in result:
    print(i, end = ' ')