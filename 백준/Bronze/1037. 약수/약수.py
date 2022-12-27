N = int(input())
N_list = list(map(int, input().split()))

min_num = min(N_list)
max_num = max(N_list)
print(min_num * max_num)