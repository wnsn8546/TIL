# https://www.acmicpc.net/problem/5063
# 첫째 줄에 테스트 케이스의 개수 N이 주어진다.
# 다음 N개의 줄에는 3개의 정수 r, e, c가 주어진다.
# r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용이다.
# 각 테스트 케이스에 대해서, 광고를 해야 하면 "advertise", 하지 않아야 하면 "do not advertise", 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

N = int(input()) # N을 입력받는다.

for test_case in range(1, N + 1): # 테스트 케이스만큼 반복한다.
    r, e, c = map(int, input().split()) # r, e, c를 입력 받는다.
    
    if r > e - c: # 광고를 하지않았을때가 더 수익이 클때,
        print('do not advertise')
    elif r < e - c: # 광고를 했을때가 더 수익이 클때,
        print('advertise')
    else: # 했을때와 하지않았을때가 같을때,
        print('does not matter')