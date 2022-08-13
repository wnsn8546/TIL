# https://www.acmicpc.net/problem/2920

numbers = list(map(int, input().split()))
diffrence = 0 # 초기값 0, i번째 수와, i+1번째 수의 차이를 저장

for i in range(0, len(numbers)-1):
    if diffrence == 0: # 초기값일때는 차이를 그냥 저장
        diffrence = numbers[i+1] - numbers[i]
    elif diffrence == 1: # ascending중인지를 판별. 아닐때는 'mixed'출력하고 for문 break
        if numbers[i+1] - numbers[i] == 1:
            continue
        else:
            print('mixed')
            break
    elif diffrence == -1: # decending중인지를 판별. 아닐때는 'mixed'출력하고 for문 break
        if numbers[i+1] - numbers[i] -1:
            continue
        else:
            print('mixed')
            break
    else:# 아닐때는 'mixed'출력하고 for문 break
        print('mixed')
        break
else: # for문이 종료될때 break 한적이 없으면 diffrence가 진행중이던대로 출력
    if diffrence > 0:
        print('ascending')
    elif diffrence < 0:
        print('descending')