# https://www.acmicpc.net/problem/25192
# ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다.
# 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.
# 새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다.
# 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.

N = int(input()) # N을 입력받는다.
my_dict = {} # 기록할 딕셔너리
cnt_gomgomticon = 0 # 곰곰티콘을 사용한 횟수를 카운트할 변수

for i in range(N): # N번 반복한다.
    input_str = input() # 문자열을 입력받는다.
    if input_str != 'ENTER': # ENTER가 아닐때
        if input_str not in my_dict: # 딕셔너리에 없었으면,
            my_dict[input_str] = 1 # 1로 추가해준다.
    else: # ENTER 일때
        cnt_gomgomticon += len(my_dict) # 딕셔너리의 길이만큼 카운트를 더해주고,
        my_dict = {} # 초기화한다.
cnt_gomgomticon += len(my_dict) # for문이 끝나고 한번 더, 딕셔너리의 길이만큼 카운트를 더해주고,
print(cnt_gomgomticon) # 출력한다.













# N = int(input()) # 채팅방 기록 수 N을 입력 받는다.

# my_dict = {} # 저장할 딕셔너리
# cnt_enter = 0 # ENTER 가 나온 횟수를 카운트할 변수
# cnt_gomgomticon = 0 # 곰곰티콘이 총 몇번 사용되었는지 카운트할 변수
# for i in range(N): # N번만큼 입력 받는다.
#     input_str = input() 

#     if input_str == 'ENTER': # 입력된 문자열이 ENTER이면,
#         cnt_enter += 1 # 카운트를 올려준다.
#     else: # ENTER가 아닐때,
#         if input_str not in my_dict: # 딕셔너리에 없었으면,
#             my_dict[input_str] = 1 # 값을 1로 추가해주고
#         else: # 있었으면,
#             if my_dict[input_str] < cnt_enter: # cnt_enter보다 작은 밸류값일때만,
#                 my_dict[input_str] += 1 # 카운트 해준다.

# cnt_gomgomticon = sum(my_dict.values()) # 총 곰곰티콘이 사용한 횟수를 구하고,
# print(cnt_gomgomticon) # 출력한다.
# print(my_dict)