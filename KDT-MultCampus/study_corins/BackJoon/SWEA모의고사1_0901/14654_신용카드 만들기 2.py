# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 `자연수`와 `-`로 이루어진 길이가 1 이상인 문자열이 주어진다. 

T = int(input()) # 테스트케이스 개수를 입력받는다.

for test_case in range(1, T+1):
    nums = input().replace('-', '') # 카드번호를 입력받는다.
    
    if len(nums) != 16:
        print(f'#{test_case} 0') # 출력
        continue
    if nums[0] not in '34569':
        print(f'#{test_case} 0') # 출력
        continue
    print(f'#{test_case} 1') # 출력