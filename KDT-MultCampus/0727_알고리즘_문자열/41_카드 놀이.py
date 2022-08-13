# https://www.acmicpc.net/problem/2511

A = list(map(int, input().split())) # A와 B의 숫자카드를 리스트로 저장한다.
B = list(map(int, input().split()))

score_A = 0 # A, B의 총 점수를 저장할 변수를 선언, 초기화한다.
score_B = 0

for i in range(10): # for문을 통해 점수를 저장한다.
    if A[i] > B[i]:
        score_A += 3
    elif A[i] < B[i]:
        score_B += 3
    else:
        score_A += 1
        score_B += 1

print(score_A, score_B) # A, B의 총점을 출력한다.
# A, B의 총점의 크기가 다를땐 이긴쪽을 출력한다. 동점일 경우, for문을 사용하여
# 최근에 이긴 쪽을 판별해서 출력한다. 첫라운드까지 동점이었을경우 'D'를 출력한다.
if score_A > score_B:
    print('A')
elif score_A < score_B:
    print('B')
else:
    for i in range(0, 10):
        if A[9-i] > B[9-i]:
            print('A')
            break
        if A[9-i] < B[9-i]:
            print('B')
            break
    else:
        print('D')