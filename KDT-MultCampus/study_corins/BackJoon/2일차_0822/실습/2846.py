# 첫째 줄에 측 정한 높이의 수열의 크기 N이 주어진다.
# 둘째 줄에는 N개의 양의 정수가 주어진다.
# 첫째 줄에 가장 큰 오르막길의 크기를 출력한다. 만약 없는경우 0을 출력한다.

N = int(input()) # N을 입력받는다.
height_list = list(map(int, input().split())) # 높이들을 리스트로 받는다.
uphill_load_list = [] # 오르막길 크기들을 넣을 리스트
temp = 0 #오르막길을 임시저장할 변수

for i in range(N-1): # 크기 비교를 위해, 범위를 N-1로 한다.
    if height_list[i] < height_list[i+1]: # i+1번째가 i번째보다 큰지 비교한다.
        temp += height_list[i+1] - height_list[i] # 오르막길 크기를 넣어준다.
    else:
        if temp > 0: # 오르막길이 있었으면,
            uphill_load_list.append(temp) # 리스트에 추가해주고
        temp = 0 # 카운트를 0으로 초기화해준다.
if temp > 0: # 마지막 높이에 대해서 한번 더 계산. 오르막길이 있었으면,
    uphill_load_list.append(temp) # 리스트에 추가해준다.
# 출력부분
if len(uphill_load_list): # 오르막길 리스트의 길이가 존재하면(값이 있으면)
    print(max(uphill_load_list)) # 제일 큰 오르막길을 출력해준다.
else:
    print(0) # 없으면 0을 출력한다.