N = int(input())
guests = list(map(int, input().split()))
check = {}
reject = 0

for i in guests:
    if i in check:
        check[i] += 1
        reject += 1
    else:
        check[i] = 1
print(reject)