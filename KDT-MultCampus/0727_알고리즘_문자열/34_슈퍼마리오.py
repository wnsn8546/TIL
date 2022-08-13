# https://www.acmicpc.net/problem/2851

def abs_num(number): # 절대값함수 구현
    if number >= 0:
        return number
    else:
        return -number

sum_score = 0 # 점수들을 쭉 더해나갈 변수
score = 0 # 점수를 하나하나 input으로 받을 변수
flag = -1 # 점수의 합이 100이상일때와 아닐때를 구분하려고 만든 flag변수

for i in range(10):
    score = int(input()) # 점수를 하나씩 받는다 합이 100이상이어도 10개를 받기위해서 맨 위에 선언

    if flag == -1: # 100이하일때는 계속 점수를 더해준다.
        sum_score += score
        # 처음으로 점수의 합이 100이상일때 이전의 점수의 합과 이번의 점수의 합 중
        # 절대값이 작은쪽을 선택하기위한 조건문
        if sum_score >= 100: 
            if abs_num(sum_score - 100) > abs_num(sum_score - score -100):
                sum_score -= score
            flag = 1 # 점수의 합이 100 이상일때 flag를 초기값에서 변화를 준다.
print(sum_score) # 답 출력