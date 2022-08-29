# 첫째 줄에는 참가자 수 N이 주어진다.
# N개의 줄에는 참가자의 이름이 주어진다.
# 추가적으로 주어지는 N-1개의 줄에는 완주한 참가자의 이름이 쓰여져 있다. 
# 알파벳 소문자로만 이루어져 있다.
# 참가자들 중엔 동명이인이 있을 수도 있다. 
# 마라톤을 완주하지 못한 참가자 한명의 이름을 출력한다.

import sys
input = sys.stdin.readline

N = int(input()) # N을 입력받는다.
player_dict = {} # 참가자들의 이름을 넣을 딕셔너리를 만든다.

for _ in range(N): # N만큼 반복하면서
    name = input() # 이름을 입력받고,
    if name not in player_dict: # 딕셔너리에 없었으면 1을,
        player_dict[name] = 1
    else:
        player_dict[name] += 1 # 있었으면 값을 +1 해준다.
for _ in range(N-1): # N-1만큼 반복하면서
    name = input()   # 이름을 입력받고,
    player_dict[name] -= 1 # 값을 -1 해준다.

for k, v in player_dict.items(): # 딕셔너리를 순회하면서
    if v != 0: # 값이 남아있는, 1인 참가자를 찾으면
        print(k) # 이름을 출력하고,
        break # 반복문을 종료한다.