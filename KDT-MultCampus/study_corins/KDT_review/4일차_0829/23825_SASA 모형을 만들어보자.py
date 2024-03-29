# 첫째 줄에 알파벳 S 모양의 블록의 개수 N과,
# 알파벳 A 모양의 블록의 개수 M이 공백으로 구분되어 주어진다.
# SASA 모형 1개를 만들기 위해서는
# S 모양의 블록 2개와, A 모양의 블록 2개가 필요하다.
# 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 출력한다.

N, M = map(int, input().split()) # S의 개수 N과, A의 개수 M을 입력받는다.

print(min(N, M) // 2) # 둘 중에 작은 숫자를 찾고, 2로 나눈 몫만큼이 최댓값이다.