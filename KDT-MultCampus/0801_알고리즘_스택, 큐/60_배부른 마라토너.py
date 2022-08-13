# https://www.acmicpc.net/problem/10546

import sys
input = sys.stdin.readline

N = int(input())
players = {} # 마라톤 선수들을 담을 딕셔너리
# 처음 선수들을 입력받을때 +1, finish한 선수들은 -= 을 한뒤,
for i in range(N):
    player = input()
    if player in players :
        players[player] += 1
    else :
        players[player] = 1
for i in range(N-1):
    player = input()
    players[player] -= 1
#  value가 1인선수를 출력.
for p in players:
    if players[p]:
        print(p)
        break