import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(T):
    incomes = list(map(int, input().split()))# 소득 리스트
    sum_income = 0 # 소득을 합산해서 평균을 구할떄 사용할 변수
    avg = 0 # 평균
    cnt = 0 # 평균 이하의 사람들을 카운트할때 사용할 변수
    case_case = int(input())
    

    for i in incomes: # 소득리스트를 순회하면서 더하고, 평균을구한다.
        sum_income += i
    avg = sum_income / len(incomes)

    for i in incomes: # 평균이하의 사람들의 수를 카운트한다.
        if i <= avg:
            cnt += 1
    print(f'#{test_case+1}', cnt) # 출력한다.