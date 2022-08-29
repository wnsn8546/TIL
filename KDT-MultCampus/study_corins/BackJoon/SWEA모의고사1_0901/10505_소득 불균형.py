# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.
# 첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다.
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

T = int(input()) # 테스트케이스 개수

for test_case in range(T): # 테스트케이스 개수만큼 순회
    case_N = int(input()) # 케이스 정수의 개수
    incomes = list(map(int, input().split())) # 정수들을 리스트로 저장
    avg = sum(incomes) / case_N # 평균 계산

    cnt = 0 # 평균이하의 사람이 몇명인지 카운트할 변수
    for i in incomes: # incomes를 순회하면서
        if i <= avg: # i가 avg이하일떄
            cnt += 1 # cnt += 1
    print(f'#{test_case+1}', cnt) # 출력