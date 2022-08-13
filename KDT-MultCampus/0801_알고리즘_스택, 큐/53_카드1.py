# https://www.acmicpc.net/problem/2161

from collections import deque

N = int(input())
dq = deque((range(1, N+1))) # 1부터 N까지 deque로 초기화

while len(dq) > 1: # 한장이 남을때 까지
    print(dq.popleft(), end=" ")# 버리고, 버린 카드 출력
    dq.append(dq.popleft()) # 맨 위 카드를 맨 아래로
print(dq[0]) # 마지막 남은 카드 출력