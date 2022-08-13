# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
nums = [0]
result = 0

for i in range(1,b+1):
    for j in range(i):
        nums.append(i)

for i in range(a, b+1):
    result += nums[i]

print(result)