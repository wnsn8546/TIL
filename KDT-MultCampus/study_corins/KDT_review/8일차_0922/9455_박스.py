# https://www.acmicpc.net/problem/9455
# 박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다. (1 ≤ m, n ≤ 100) 
# 다음 m개 줄에는 그리드의 각 행의 정보를 나타내는 n개의 정수가 주어진다. 그리드 첫 행부터 마지막 행까지 순서대로 주어진다. 
# 박스가 들어있는 칸은 1로, 다른 칸은 0으로 주어진다. 각 정수 사이에는 공백이 하나 주어진다.
# 각 테스트 케이스마다 입력으로 주어진 그리드에서 모든 박스가 이동한 거리를 출력한다.

T = int(input()) # 테스트케이스의 개수를 입력받는다.

for test_case in range(T): # 테스트케이스 만큼 반복
    m, n = map(int, input().split()) # m, n을 입력받는다.
    grid = [list(map(int, input().split())) for _ in range(m)] # grid 정보를 입력받는다.
    cnt = 0 # 이동거리를 카운트할 변수

    for j in range(n): # 그리드를 순회하면서
        for i in range(m):
            if grid[i][j] == 1: # 처음 발견한 상자 위치
                for k in range(i+1, m): # 의 다음부터 바닥 까지 순회를 하면서
                    if grid[k][j] == 0: # 빈 공간의 개수를
                        cnt += 1 # 카운트해준다.
    print(cnt) # 출력한다.