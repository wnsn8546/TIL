# https://www.acmicpc.net/problem/23825

N, M = map(int, input().split())

N //= 2
M //= 2

print(min(N,M))