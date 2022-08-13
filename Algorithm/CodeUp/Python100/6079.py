i = 1
sum = 0
n = int(input())
while sum < n :
    sum += i
    if sum < n :
        i += 1
    else :
        print(i)