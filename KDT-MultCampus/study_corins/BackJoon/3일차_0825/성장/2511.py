# A와 B에게는 각각 0에서 9까지의 숫자가 하나씩 표시된 10장의 카드뭉치가 주어진다.
# 각 라운드에서는 공개된 숫자가 더 큰 사람이 승자가 된다.
# 승자에게는 승점 3점이 주어지고 비기게 되면, A, B 모두에게 승점 1점이 주어진다.
# 첫 번째 줄에는 게임이 끝난 후, A와 B가 받은 총 승점을 순서대로 빈칸을 사이에 두고 출력한다.
# 두 번째 줄에는 이긴 사람이 A인지 B인지 결정해서, 이긴 사람을 문자 A 또는 B로 출력한다.
# 만약 비기는 경우에는 문자 D를 출력한다. 

A_list = list(map(int, input().split())) # A의 카드를 입력받는다.
B_list = list(map(int, input().split())) # B의 카드를 입력받는다.
A_score = 0 # A의 점수를 저장할 변수.
B_score = 0 # B의 점수를 저장할 변수.

for i in range(10): # 카드 수 만큼 순회한다.
    if A_list[i] > B_list[i]: # 카드의 ㅜ숫자를 비교해서 점수를 추가한다.
        A_score += 3
    elif A_list[i] < B_list[i]:
        B_score += 3
    else:
        A_score += 1
        B_score += 1

print(A_score, B_score) # A, B의 score를 출력하고,
if A_score > B_score: # 이긴사람을 출력한다.
    print('A')
elif A_score < B_score:
    print('B')
else: # 무승부일때 거꾸로 돌아가며 가장 마지막에 이긴 사람을 출력한다.
    for i in range(10):
        if A_list[9-i] > B_list[9-i]:
            print('A')
            break
        elif A_list[9-i] < B_list[9-i]:
            print('B')
            break
    else: # 첫라운드까지도 무승부였으면 'D'를 출력한다.
        print('D')