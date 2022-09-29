# https://www.acmicpc.net/problem/1547
# 첫째 줄에 컵의 위치를 바꾼 횟수 M이 주어지며, 
# M은 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 M개의 줄에는 컵의 위치를 바꾼 방법 X와 Y가 주어지며, 
# X번 컵과 Y번 컵의 위치를 서로 바꾸는 것을 의미한다. 
# X와 Y의 값은 3보다 작거나 같고, X와 Y가 같을 수도 있다.
# 첫째 줄에 공이 들어있는 컵의 번호를 출력한다. 
# 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.

M = int(input()) # M을 입력받는다.
cups = [1, 0, 0] # 컵
temp = 0 # 임시변수

for i in range(M): # M만큼 반복한다.
    x, y = map(int, input().split()) # x,y 값을 입력받는다.
    
    temp = cups[x-1]
    cups[x-1] = cups[y-1]
    cups[y-1] = temp

for i in range(len(cups)):
    if cups[i] == 1:
        print(i+1)
        break
else:
    print(-1)