# https://www.acmicpc.net/problem/4396
# 첫 번째 줄에는 10보다 작거나 같은 양의 정수 n이 입력된다. 
# 다음 n개의 줄은 지뢰의 위치를 나타낸다. 
# 각각의 줄은 n개의 문자를 사용하여 한 행을 나타낸다. 
# 온점(.)은 지뢰가 없는 지점이며 별표(*)는 지뢰가 있는 지점이다. 
# 다음 n개의 줄에는 길이가 n인 문자열이 입력된다. 
# 이미 열린 칸은 영소문자 x로, 열리지 않은 칸은 온점(.)으로 표시된다. 
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

mine_board = [ list(input()) for i in range(n)]
now_board = [ list(input()) for i in range(n)]
result_board = [['.'] * n for i in range(n)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
cnt = 0
is_mine = 0

for i in range(n):
    for j in range(n):
        if now_board[i][j] == 'x':
            if mine_board[i][j] == '*': is_mine = 1
            for d in range(8):
                if n > i+dx[d] and i+dx[d] >= 0 and n > j+dy[d] and j+dy[d] >= 0:
                    if mine_board[i+dx[d]][j+dy[d]] == '*':
                        cnt += 1
            result_board[i][j] = cnt
            cnt = 0
        else:
            continue
if is_mine == 0:
    for i in range(n):
        for j in range(n):
            print(result_board[i][j], end='')
        print()
else:
    for i in range(n):
        for j in range(n):
            if mine_board[i][j] == '*':
                print('*', end='')
            else:
                print(result_board[i][j], end='')
        print()