# https://www.acmicpc.net/problem/1037

N = int(input())

yak_list = list(map(int, input().split()))
yak_list = sorted(yak_list)

idx = 0
for i in range(yak_list[-1], 1000000, yak_list[0]):
    if i > yak_list[-1]:
        for j in range(len(yak_list)):
            if i 
        