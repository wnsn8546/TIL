# https://www.acmicpc.net/problem/1236
# 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다.
# N과 M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다.
# 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.
# 첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.

N, M = map(int, input().split()) # N, M을 입력받는다.
castle = [list(map(str, input().rstrip())) for _ in range(N)] # N 만큼 입력받는다.
row_cnt = 0 # 행에 'X'가 없을때 카운트할 변수
col_cnt = 0 # 열에 'X'가 없을때 카운트할 변수 

for i in range(N): # 행 체크
    if 'X' not in castle[i]: # 'X'가 행에 없으면
        row_cnt += 1 # 카운트 +1

for j in range(M): # 열체크
    if 'X' not in [castle[i][j] for i in range(N)]: # 'X'가 열에 없으면,
        col_cnt += 1 # 카운트 +1
print(max(row_cnt, col_cnt)) # 둘 중에 큰 값을 출력