# https://www.acmicpc.net/problem/17249

taebo = input() 
left_side = []
right_side = []
# 주어진 태보 그림을 입력받고, 얼굴의 시작지점을 찾은 뒤 왼쪽,오른쪽으로 나눈다.
for i in range(0, len(taebo)):
    if taebo[i] == '(':
        left_side = taebo[0:i]
        right_side = taebo[i+5:]
        break;
print(left_side.count('@'), right_side.count('@')) # 왼쪽 오른쪽에 주먹의 끝이 몇번나타났는지