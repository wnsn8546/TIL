# https://www.acmicpc.net/problem/23253
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
flag = 1

for i in range(M):
    num = int(input())
    nums = list(map(int, input().split()))
    print(nums)
    for j in range(num-1):
        if nums[j] < nums[j+1]:
            flag = 0
            break

if flag == 1:
    print('Yes')
else:
    print('No')