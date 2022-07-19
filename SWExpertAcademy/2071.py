T = int(input())

for i in range(1,T+1):
    my_list = list(map(int, input().split()))
    
    print(f"#{i}", round(sum(my_list)/10))