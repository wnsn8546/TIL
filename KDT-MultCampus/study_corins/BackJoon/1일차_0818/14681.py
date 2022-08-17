# 첫 줄에는 정수 x를, 다음 줄에는 정수 y를 입력받아,
# 그 점이 몇사분면에 위치해 있는지 출력한다. x, y는 0은 아니다.
# Quadrant 1(+, +), Quadrant 2(-, +), Quadrant 3(-, -), Quadrant 4(+, -)

x = int(input()) # 정수 x를 입력받는다.
y = int(input()) # 정수 y를 입력받는다.

if x > 0 and y > 0: # if, elif문으로 해당 점의 사분면을 출력한다.
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)