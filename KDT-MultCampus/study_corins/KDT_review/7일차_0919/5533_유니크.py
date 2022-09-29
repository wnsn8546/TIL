# https://www.acmicpc.net/problem/5533
# 첫째 줄에 참가자의 수 N이 주어진다. (2 ≤ N ≤ 200)
# 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 
# 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 
# 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
# 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.
# 각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력한다.

N = int(input()) # N을 입력받는다.

player = [[], [], []] # 플레이어 숫자들을 담을 리스트
result = [0] * N # 점수들을 담을 리스트

for i in range(N): # N만큼 반복하면서
    a, b, c = map(int, input().split()) # 숫자를 입력받는다.
    player[0].append(a) # 하나씩 넣어준다.
    player[1].append(b)
    player[2].append(c)

for i in range(3): # 3번 반복
    for j in range(N): # N만큼 반복
        if player[i].count(player[i][j]) >= 2: # 같은 점수가 2개 이상이면,
            result[j] += 0 # 0점
        else:
            result[j] += player[i][j] # 아니면 점수획득
for i in result:
    print(i) # 출력