# 자연수 N이 주어졌을때, N부터 1까지 한 줄에 하나씩 출력한다.

N = int(input()) # N을 입력받는다.

for i in range(N, 0, -1): # i를 N 부터 1까지 -1씩 감소시킨다.
    print(i) # i를 한 줄에 하나씩 출력한다.