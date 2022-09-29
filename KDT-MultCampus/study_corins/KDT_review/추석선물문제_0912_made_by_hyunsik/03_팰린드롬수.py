# https://www.acmicpc.net/problem/1259
# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

N = input()

if N == N[::-1]:
    print('yes')
else:
    print('no')