n = int(input())     
a = input().split()  
min_num = 10000

for i in range(n) :
    a[i] = int(a[i])
    if a[i] < min_num:
        min_num = a[i]
print(min_num)