# https://www.acmicpc.net/problem/11286
# 1. 배열에 정수 x (x ≠ 0)를 넣는다.
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고,
# 그 값을 배열에서 제거한다.

import heapq # heapq를 사용하기 위해 import

N = int(input()) # N을 입력받는다.

num_list = [] # 입력받은 수들을 저장할 리스트
for i in range(N): # N번 입력을 받는다.
    x = int(input()) # x를 입력받는다.

    if x != 0: # x가 0이 아닐때
        heapq.heappush(num_list, (abs(x), x)) # heappush로 num_list에 절대값과, x를 같이 넣는다.
    else: # x가 0일때
        if len(num_list) == 0: # num_list의 길이가 0이면,
            print(0) # 0을 출력해주고
        else: # 길이가 0이 아닐때,
            print(heapq.heappop(num_list)[1]) # heappop으로 제일작은 값 set을 꺼내고, [1]인덱스를 출력해준다.