# 수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.
# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.
import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 테스트 케이스 T가 주어진다.
for test_case in range(1, T+1):
    N, K = map(int, input().split()) # 수강생수 N, 제출한 사람의 수 K
    K_list = list(map(int, input().split())) # 제출한 사람들의 번호

    print(f'#{test_case}', end=' ') # 출력형식
    for i in range(1, N+1): # 1부터 N+1까지 순회하면서
        if i not in K_list: # i가 K_list에 없는 숫자이면(제출하지 않은사람번호이면)
            print(i, end=' ') # 공백문자를 붙여서 출력해준다.
    print() # 마지막에 개행