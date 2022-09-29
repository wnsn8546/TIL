# 첫째 줄에는 테스트 케이스 개수 T가 주어진다.
# 각 테스트 마다 한줄에 A, B가 주어진다.
# 각 테스트 케이스마다 "Case #x: "를 출력하고, A + B를 출력한다.

T = int(input()) # 테스트개수 T를 입력받는다.

for test_case in range(1, T + 1): # T만큼 반복한다.
    A, B = map(int, input().split()) # A, B를 입력받는다.

    print(f'Case #{test_case}: {A + B}') # 요구사항대로 출력한다.