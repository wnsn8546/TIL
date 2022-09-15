# https://www.acmicpc.net/problem/2776
# 첫째 줄에 테스트케이스의 개수 T가 들어온다. 
# 다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다. 
# 그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다. 
# 그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고, 
# 다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다. 
# 모든 정수들의 범위는 int 로 한다.

T = int(input()) # 테스트케이스의 개수

for test_case in range(T): # 테스트케이스 개수만큼 반복한다.
    N = int(input()) # 수첩1에 적어놓은 정수의 개수 N을 입력받는다.
    N_list = set(map(int, input().split())) # N개의 정수를 입력받는다.
    # 수첩1에 중복이 존재할 수도 있으므로 set을 사용해보았다.
    M = int(input()) # 수첩2에 적어놓은 정수의 개수 M을 입력받는다.
    M_list = map(int, input().split()) # M개의 정수를 입력받는다.

    for i in M_list: # M_list를 순회하면서
        if i in N_list: # N_list에 i가 존재하면,
            print(1) # 1을 출력
        else: # 없으면,
            print(0) # 0을 출력