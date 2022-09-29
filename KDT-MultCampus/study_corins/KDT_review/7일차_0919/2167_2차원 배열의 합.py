# https://www.acmicpc.net/problem/2167
# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 
# 배열의 (i, j) 위치는 i행 j열을 나타낸다.
# 첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 
# 다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
# 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다.
# 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다.
# 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M).

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N,M을 입력받는다.
board = [list(map(int, input().split())) for _ in range(N)] # 
K = int(input()) # K를 입력받는다.

for q in range(K): # K만큼 반복한다.
    i, j, x, y = map(int, input().split()) # i,j,x,y를 입력받는다.
    result = 0 # 결과를 저장할 변수
    for w in range(N): #
        for e in range(M): #
            if i - 1 <= w and w <= x - 1 and j - 1 <= e and e <= y - 1: # 해당 범위에 맞으면
                result += board[w][e] # result에 더해준다.
    print(result) # 출력한다.