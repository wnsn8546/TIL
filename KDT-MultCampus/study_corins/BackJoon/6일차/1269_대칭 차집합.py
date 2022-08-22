# 첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수가 빈 칸을 사이에 두고 주어진다.
# 둘째 줄에는 집합 A의 모든 원소가, 셋째 줄에는 집합 B의 모든 원소가 빈 칸을 사이에 두고 각각 주어진다.
# 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

N, M = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# print(len(set(A) - set(B)) + len(set(B) - set(A)))
print(len(A - B) + len(B - A))