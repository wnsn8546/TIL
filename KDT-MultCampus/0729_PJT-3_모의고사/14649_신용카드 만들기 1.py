import sys
sys.stdin = open("input.txt", "r")

#1 매 홀수자리의 숫자마다 2를곱해서 더한다.
#2 매 짝수자리의 숫자는 그대로 더한다.
#3 1과2를 더한 숫자에 N을 더한 숫자가 10으로 나눴을때 나눠 떨어지면 유효수
T = int(input())

for test_case in range(T):
    nums = list(map(int, input().split()))
    odd = 0 # 홀수번째 수들을 더해 나아갈 변수 
    even = 0 # 짝수번째 수들을 더해 나아갈 변수
    result = 0 # 결과를 저장할 변수
    for i in range(0, len(nums)):
        if i % 2 == 0: # 인덱스는 0부터이므로, 이게 홀수번째 수
            odd += (nums[i] * 2)
        else:# 짝수번째 수
            even += nums[i]
    
    result = 10 - ((odd + even) % 10) # 10의 배수와 얼마나 차이나는지계산
    if result == 10: # 차이가 10이면 0으로 바꿔줄때 사용할 부분
        result = 0
    print(f'#{test_case+1}', result)