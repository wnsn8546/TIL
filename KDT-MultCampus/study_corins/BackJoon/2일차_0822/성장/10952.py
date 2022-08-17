# 입력의 마지막줄 에는 0 두개가 들어온다.
# 한 줄에 A, B를 입력받고 A + B 를 출력한다.

while True: # while True를 사용하여 계속 반복한다.
    A, B = map(int, input().split()) # A, B를 입력한다.

    if A == 0 and B == 0: # A, B가 둘 다 0이면 break로 while문을 빠져나가고
        break             # 프로그램을 종료한다.
    else:
        print(A + B) # 그렇지 않으면 A + B를 출력한다.