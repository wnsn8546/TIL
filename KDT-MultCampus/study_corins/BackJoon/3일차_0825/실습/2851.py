# 10개 줄에 각각 버섯의 점수가 주어진다.
# 중간에 중단할 수 있다.
# 버섯 점수의 합이 최대한 100에 가깝게하여 점수를 출력하라.

mushroom_list = [] # 버섯 점수들을 담아놓은 리스트를 만든다.

for _ in range(10): # 총 10개 밖에 안되니 일단 다 받는다.
    mushroom_list.append(int(input()))

sum_score = 0 # 점수들을 더해갈 변수를 만든다.
for i in range(len(mushroom_list)): # 버섯의 개수만큼 반복한다.
    sum_score += mushroom_list[i] # 점수들을 더해주고
    if sum_score >= 100: # 총점이 100점이상일떄
        # 이전 값과 누가 더 100과의 차이가 적은지 비교한다.
        if sum_score - 100 > 100 - (sum_score - mushroom_list[i]): # 지금 값이 차이가 훨씬 크면 이전값을 답으로 출력하고 반복문을 종료한다.
            print(sum_score - mushroom_list[i])
            break
        else: # 그렇지 않으면 현재값을 출력하고 반복문을 종료한다.
            print(sum_score)
            break
else: # 10번을 다 돌았을때 break를 한적이 없다면 현재까지의 총점을 출력한다.
    print(sum_score)