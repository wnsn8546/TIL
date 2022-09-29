# 시험 점수를 입력받아 90 ~ 100점은은 A, 80 ~ 89점은 B,
# ... 60 ~ 69점은 D, 나머지 점수를 F를 출력하는 프로그램을 작성하라.

score = int(input()) # 시험점수를 입력받는다.
# 구간별로, if, elif, else문을 작성하고 해당하는 등급을 출력한다.
if score >= 90: # 0 ~ 100까지의 점수만이 주어지므로, 90이상으로 해도 무방하다.
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')