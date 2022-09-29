# https://www.acmicpc.net/problem/2592
# 열 개의 자연수가 주어질 때 이들의 평균과 최빈값을 구하는 프로그램을 작성하시오.
# 첫째 줄부터 열 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 
# 주어지는 자연수는 1,000 보다 작은 10의 배수이다.
# 첫째 줄에는 평균을 출력하고, 둘째 줄에는 최빈값을 출력한다.
# 최빈값이 둘 이상일 경우 그 중 하나만 출력한다.
# 평균과 최빈값은 모두 자연수이다.

my_dict = {} # 빈도수를 저장할 딕셔너리
sum_num = 0 # 평균을 구하기 위해 입력된 N을 합할 변수
for i in range(10): # 10번 반복하면서
    N = int(input()) # 정수 N을 입력받고
    sum_num += N # 더해준다
    if N not in my_dict: # 딕셔너리에 없었으면
        my_dict[N] = 1 # 빈도 1 로 저장해주고
    else: # 있었으면
        my_dict[N] += 1 # 기존값에 1을 더해준다

mode = max(my_dict.values()) # 빈도수가 최대인 값을 mode변수에 저장해놓고
for k, v in my_dict.items(): # 딕셔너리를 순회하면서
    if v == mode: # 최대빈도수와 빈도수가 같은 수가 나오면
        mode_num = k # 저장해주고
        break # 하나만 찾아도 되므로 break

print(sum_num // 10) # 평균 몫만 출력 
print(k) # 최대빈도의 수 출력