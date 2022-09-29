# 첫 줄에 테스트케이스 개수 T를 입력 받고, 한 줄씩 A, B를 한 번에 입력받아
# A + B를 출력한다.

T = int(input()) # 테스트케이스 개수 T

for test_case in range(1, T + 1): # 테스트 케이스 개수만큼 반복한다.
    A, B = map(int, input().split()) # A, B를 한 줄에 입력받는다.

    print(A + B) # A + B를 출력한다.