# https://www.acmicpc.net/problem/1652
# 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면
# 방의 크기 N과 방의 구조가 주어졌을 때, 
# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 
# 구하는 프로그램을 작성하시오.
# 첫째 줄에 방의 크기 N이 주어진다. 
# N은 1이상 100이하의 정수이다. 
# 그 다음 N줄에 걸쳐 N개의 문자가 들어오는데 
# '.'은 아무것도 없는 곳을 의미하고, 
# 'X'는 짐이 있는 곳을 의미한다.
# 첫째 줄에 가로로 누울 수 있는 자리와 
# 세로로 누울 수 있는 자리의 개수를 출력한다.

N = int(input()) # N을 입력받는다.
room = [list(map(str, input()))for _ in range(N)] # 방의 정보를 입력받는다.

row_cnt = 0 # 행에서 개수를 체크할 변수
for i in range(N): 
    cnt = 0 # 매번 cnt를 0으로 리셋해주고
    for j in range(N): 
        if room[i][j] == '.': # '.'일떄
            cnt += 1 # cnt를 +1 해준다
        else: # 그렇지 않을때, 'X'일때
            if cnt > 1: # cnt가 1보다 크면
                row_cnt += 1 # row_cnt를 +1 해준다.
            cnt = 0 # 0으로 리셋해준다.
    if cnt > 1: # 한 행이 끝났을때 한번 더 체크해준다.
        row_cnt += 1 
        cnt = 0

col_cnt = 0
for i in range(N): # 세로 체크. 위의 로직 반복
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        else:
            if cnt > 1:
                col_cnt += 1
            cnt = 0
    if cnt > 1:
        col_cnt += 1
        cnt = 0
print(row_cnt, col_cnt) # 출력한다.