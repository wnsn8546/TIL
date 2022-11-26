N = int(input())

ages = []

for i in range(N):
    age, name = input().split()
    ages.append((int(age), i, name))

result = sorted(ages)
for r in result:
    print(r[0], r[2])