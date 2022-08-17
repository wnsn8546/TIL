# 주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다.
# 첫째 줄에 왼손의 잔상수와 오른손의 잔상수를 출력한다.

afterimage = input() # 잔상을 입력받는다.
left = 0 # 왼쪽 주먹을 뻗은 횟수
right = 0 # 오른쪽 주먹을 뻗은 횟수
location = 0 # 지금이 왼쪽인지 오른쪽인지를 판별할 변수 초기값0: 왼쪽

for i in afterimage: # 하나씩 순회한다.
    if i == ')': # 오른쪽 뺨을 만나면 location을 1로 바꿔준다.
        location = 1
    if i == '@': # '@' 주먹을 만났을때 location 변수를 확인하고 해당하는 쪽에 +1해준다.
        if location == 0:
            left += 1
        else:
            right += 1
print(left, right) # 출력한다.