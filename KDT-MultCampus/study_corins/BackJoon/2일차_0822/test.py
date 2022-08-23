N = int(input())

arr = list(map(int, input().split()))

min_ = 1000000
max_ = -1000000
for i in range(N):
    if arr[i] > max_:
        max_ = arr[i]
        if max_ < min_:
            min_ = max_
    else:
        min_ = arr[i]

print(min_, max_)