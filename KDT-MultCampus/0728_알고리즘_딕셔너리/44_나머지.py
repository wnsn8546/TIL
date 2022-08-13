# https://www.acmicpc.net/problem/3052

remainders = {}

for i in range(10):
    num = int(input())
    remainders[num % 42] = remainders.get(num % 42, 1)
print(len(remainders))

    