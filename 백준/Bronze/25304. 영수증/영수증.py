X = int(input())
N = int(input())
temp_sum = 0
temp_quantity = 0
for _ in range(N):
    a, b = map(int, input().split())
    temp_sum += a * b

if temp_sum == X:
    print('Yes')
else:
    print('No')