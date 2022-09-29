# 첫번째 줄에 n이 주어졌을때, 1부터 n까지의 합을 구하는 프로그램

n = int(input()) # n을 입력받는다.
sum_nums = 0 # 1부터 n까지 더해서 저장할 변수를 선언하고 0으로 초기화한다.

for i in range(1, n + 1): # i를 1부터 n까지 순회한다.
    sum_nums += i # sum_nums에 i를 더해준다.
print(sum_nums) # 출력한다.