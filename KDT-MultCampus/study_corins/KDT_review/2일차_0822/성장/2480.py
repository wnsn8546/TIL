# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 1. 같은 눈이 3개 일때 10000원 + 같은 눈 * 1000원
# 2. 같은 눈이 2개 일때 1000원 + 같은 눈 * 100원
# 3. 모두 다른 눈이 나오는 경우, 가장 큰 눈 * 100원
# 3개 주사위의 나온 눈만큼의 상금을 출력하라. 

dices = list(map(int, input().split())) # 주사위 A, B, C를 입력받는다.
# count() 함수를 사용해 보기위해 list로 만든다.
if dices.count(dices[0]) == 3: # 3개의 눈이 같을때.
    print(10000 + (dices[0] * 1000))
elif dices.count(dices[0]) == 2: # dices[0]과 같은 수가 2개일때 
    print(1000 + (dices[0] * 100))
elif dices.count(dices[1]) == 2: # 아니면 dices[1]과 같은 수가 2개일때 
    print(1000 + (dices[1] * 100))
else: # 3개가 다 다를때
    print(max(dices) * 100) # 제일 큰 수를 max함수로 찾고 상금을 계산한다.