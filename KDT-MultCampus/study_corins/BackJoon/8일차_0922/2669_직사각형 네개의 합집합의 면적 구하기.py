# https://www.acmicpc.net/problem/2669
# 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.
# 입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다.
# 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 
# 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.
# 첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.

coordinate = [[0] * 100 for _ in range(100)] # 전체 범위의 좌표를 리스트로 만든다.

for c in range(4): # 4줄의 입력을 받는다.
    x1, y1, x2, y2 = map(int, input().split()) # 변수 4개를 입력받는다.

    for i in range(x1, x2-1+1): # 주어진 좌표만큼 순회하면서
        for j in range(y1, y2-1+1): 
            coordinate[i][j] = '*' # '*'로 채워준다

result = 0
for x in range(100): # 전체를 순회하면서
    for y in range(100):
        if coordinate[x][y] == '*': # '*'의 개수를
            result += 1 # 카운트한다.
print(result) # 출력한다.
