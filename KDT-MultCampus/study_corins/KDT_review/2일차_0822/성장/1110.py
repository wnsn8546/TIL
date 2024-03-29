# 첫째 줄에 0보다 크거나 같고, 99보다 작거나 같은 정수 N이 주어진다.
# 첫째 줄에 N의 사이클 길이를 출력한다.
# 1. 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리수로 만든다.
# 2. 각 자리의 숫자를 더한다.
# 3. 주어진 수의 가장 오른쪽 자리 수와, 앞에서 구한 합의 가장 오른쪽 
# 자리수를 이어 붙이면 새로운수를 만들 수 있다.

N = input() # 문자열로 처리하는게 쉬워 int로 형변환하지 않는다.
if int(N) < 10: # int로 한번 형변환하고 10보다 작은지 확인한다.
    N = '0' + N # N이 10보다 작으면 앞에 '0'을 붙여 두 자리수로 만든다.
number = N # 조작할 변수에 새로 넣어준다.

cnt = 0 # 사이클 길이를 카운트할 변수
while True: # 특정한 범위가 있지않아 while True를 사용한다.
    cnt += 1 # 반복할때 마다 cnt변수에 +1을 해준다.
    # 새로운 숫자를 만드는 방법을 그대로 적어준다.
    number = number[1] + str((int(number[0]) + int(number[1])) % 10)
    if number == N: # N과 같아졌으면,
        print(cnt) # 사이클의 길이를 출력하고,
        break # 반복문과 프로그램을 종료한다.