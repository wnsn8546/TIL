# 첫째 줄에 테스트 케이스개수 T가 주어진다.
# 테스트 케이스 마다 한 줄에 A, B를 입력받고,
# "Case #x: A + B = C" 형식으로 출력한다.

T = int(input()) # 테스트개수 T를 입력받는다.

for test_case in range(1, T + 1): # T만큼 반복한다.
    A, B = map(int, input().split()) # A, B를 입력받는다.

    print(f'Case #{test_case}: {A} + {B} = {A + B}') # 요구사항대로 출력한다.