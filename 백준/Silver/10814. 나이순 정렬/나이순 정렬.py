from sys import stdin
N = int(stdin.readline())

ages = []

for i in range(N):
    age, name = stdin.readline().split()
    ages.append((int(age), i, name))

result = sorted(ages, key = lambda x : (x[0], x[1]))
for r in result:
    print(r[0], r[2])
