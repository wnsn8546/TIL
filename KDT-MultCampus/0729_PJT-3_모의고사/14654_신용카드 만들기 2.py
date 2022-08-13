import sys
sys.stdin = open("input1.txt", "r")
# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

T = int(input())

for test_case in range(T):
    nums = input().replace('-', '')# 사용하기 좋게 '-'를 먼저 제거
    if len(nums) != 16: # 길이가 16이 안될때 0을 출력하고, continue
        print(f'#{test_case+1}', '0')
        continue
    # 첫번째 숫자가 3,4,5,6,9 가 아닐때 0을 출력하고, continue
    if nums[0] != '3' and nums[0] != '4' and nums[0] != '5' and nums[0] != '6' and nums[0] != '9':
        print(f'#{test_case+1}', '0')
        continue
    print(f'#{test_case+1}', '1') # 사용가능한 번호면 1출력