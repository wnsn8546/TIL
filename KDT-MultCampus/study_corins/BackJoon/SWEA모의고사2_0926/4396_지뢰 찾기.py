# https://www.acmicpc.net/problem/4396
# 첫 번째 줄에는 10보다 작거나 같은 양의 정수 n이 입력된다. 
# 다음 n개의 줄은 지뢰의 위치를 나타낸다. 
# 각각의 줄은 n개의 문자를 사용하여 한 행을 나타낸다. 
# 온점(.)은 지뢰가 없는 지점이며 별표(*)는 지뢰가 있는 지점이다. 
# 다음 n개의 줄에는 길이가 n인 문자열이 입력된다. 
# 이미 열린 칸은 영소문자 x로, 열리지 않은 칸은 온점(.)으로 표시된다. 
import sys
sys.stdin = open("input.txt", "r")

n = int(input()) # n입력

mine_board = [ list(input()) for i in range(n)] # 지뢰정보를 담은 board 생성
now_board = [ list(input()) for i in range(n)] # 현재까지 열어본 정보를 담은 board 생성
result_board = [['.'] * n for i in range(n)] # 결과를 담을 board .으로 채워서 생성

dx = [0, 1, 1, 1, 0, -1, -1, -1] # 8방 변화값리스트
dy = [1, 1, 0, -1, -1, -1, 0, 1] # 8방 변화값리스트
cnt = 0 # 8방에 지뢰가 몇개인지를 카운트할 변수
is_mine = 0 # 지뢰를 선택했었는지를 검사하는 변수

for i in range(n): # 전체 순회를 하면서
    for j in range(n):
        if now_board[i][j] == 'x': # 열린곳의 인덱스일때
            if mine_board[i][j] == '*': is_mine = 1 # 해당 인덱스가 지뢰의 위치일때 is_mine의 값을 1로 바꿔주고
            for d in range(8): # 8방탐색을 한다.
                if n > i+dx[d] and i+dx[d] >= 0 and n > j+dy[d] and j+dy[d] >= 0: # 8방탐색할 위치의 인덱스가 n * n내의 범위이고
                    if mine_board[i+dx[d]][j+dy[d]] == '*': # 해당 인덱스에 지뢰가 있다면,
                        cnt += 1 # cnt를 +1 해준다.
            result_board[i][j] = cnt # 결과 board에 cnt값을 표시해준다.
            cnt = 0 # 인덱스마다 0으로 초기화 해준다.
        else:
            continue # 아직 열리지 않았던 곳은 continue로 넘어간다.
if is_mine == 0: # 지뢰가 선택된적이 없었으면,
    for i in range(n): # result_board를 그대로 출력해주고
        for j in range(n):
            print(result_board[i][j], end='')
        print()
else:
    for i in range(n): # 지뢰가 선택된적이 있었다면, 지뢰를 표시해주면서 출력한다.
        for j in range(n):
            if mine_board[i][j] == '*':
                print('*', end='')
            else:
                print(result_board[i][j], end='')
        print()