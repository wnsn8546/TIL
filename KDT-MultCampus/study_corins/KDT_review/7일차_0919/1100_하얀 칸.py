# https://www.acmicpc.net/problem/1100
# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다.
# 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.
import sys
# sys.stdin=open("input.txt","r")
# input=sys.stdin.readline
sys.stdin = open('input.txt')

chess_board = [] # 흰,검을 표시해 놓은 체스판
input_board = [] # 입력받을 판을 저장할 변수

for i in range(8): # chess_board를 홀, 짝수 줄마다 색칠해준다.
    if i % 2 == 0 :
        chess_board.append('WBWBWBWB')
    else:
        chess_board.append('BWBWBWBW')

for i in range(8): # input_board를 입력받는다.
    input_board.append(input())

cnt = 0 # 하얀색이면서, 말이 놓여있는 칸을 카운트할 변수
for i in range(8): # 전체 보드의 인덱스를 순회하면서
    for j in range(8): # 하얀색이면서, 말이 놓여져있는 위치의 개수를 카운트해준다.
        if chess_board[i][j] == 'W' and input_board[i][j] == 'F':
            cnt += 1
print(cnt) # 출력한다.