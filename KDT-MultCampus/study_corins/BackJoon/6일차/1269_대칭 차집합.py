# 첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수가 빈 칸을 사이에 두고 주어진다.
# 둘째 줄에는 집합 A의 모든 원소가, 셋째 줄에는 집합 B의 모든 원소가 빈 칸을 사이에 두고 각각 주어진다.
# 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

N, M = map(int, input().split()) # N,M을 입력받는다.

A = set(map(int, input().split())) # set을 사용하면 차집합을 쉽게 구할 수 있기에,
B = set(map(int, input().split())) # set으로 입력받아준다.

print(len(A - B) + len(B - A)) # 차집합과 차집합의 합집합을 출력한다. 