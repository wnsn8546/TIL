# 첫 줄에 테스트 케이스의 개수 T를 입력받고,
# ','로 구분된 A, B를 입력받아, A + B를 출력한다.

T = int(input()) # 테스트케이스 개수 T

for test_case in range(1, T + 1): # 테스트케이스 개수만큼 반복한다.
    A, B = map(int, input().split(',')) # ','로 구분하여 A, B를 각각 입력받아 저장한다.
    
    print(A + B) # A + B를 출력한다.