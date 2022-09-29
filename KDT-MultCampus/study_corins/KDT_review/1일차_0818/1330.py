# 두 정수 A, B를 입력받아, 대소비교를 통해서 '>', '<', '==' 를 출력한다.

A, B = map(int, input().split()) # 정수 A, B를 입력받는다.
# 크기비교를 하고, 출력한다.
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')