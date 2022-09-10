# https://www.acmicpc.net/problem/2738
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

N, M  = map(int, input().split()) # N, M을 입력받는다.

N_matrix = [] # N_matrix를 입력받기 위한 빈 리스트
for i in range(N): # N번 입력을 받는다.
    N_matrix.append(list(map(int, input().split())))
M_matrix = [] # M_matrix를 입력받기 위한 빈 리스트
for i in range(N): # M번 입력을 받는다.
    M_matrix.append(list(map(int, input().split())))

for i in range(N): # 출력한다.
    for j in range(M):
        print(N_matrix[i][j] + M_matrix[i][j], end=' ')
    print()