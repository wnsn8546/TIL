# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 공백으로 구분한 자연수 15개가 주어진다. 
# 각 테스트 케이스마다, 룬 공식 유효성 검사를 통과하기 위해 16번째 자리에 들어갸아하는 숫자를 찾아서 출력한다.
# 1) 매 홀수자리의 숫자마다 2를 곱해서 더합니다. 
# 2) 매 짝수자리의 숫자는 그대로 더합니다.
# 3) 1)과 2)를 더 한 숫자에 N을 더 한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효한 숫자입니다. 
# import sys
# sys.stdin = open('input.txt', 'r', encoding='utf-8')
# input = sys.stdin.readline

T = int(input()) # 테스트케이스 개수를 입력받는다.

for test_case in range(1, T+1):
    result = 0 # 결과를 저장해놓을 변수
    nums = list(map(int, input().split())) # # 카드번호를 입력받는다.
    sum_nums = 0

    for i in range(len(nums)):
        if i % 2 == 0: # 인덱스이기때문에 홀수번째
            sum_nums += nums[i] * 2 # 2를 곱해서 더한다.
        else: # 짝수 번째
            sum_nums += nums[i] # 그냥 더한다.
    # result = (sum_nums + N) % 10 == 0
    if sum_nums % 10 > 0: # 
        result = 10 - (sum_nums % 10)
    print(f'#{test_case} {result}') # 출력