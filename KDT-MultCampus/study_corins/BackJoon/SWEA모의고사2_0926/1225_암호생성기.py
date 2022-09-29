import sys
sys.stdin = open("input.txt", "r")

T = 10 # 테스트케이스 10개

for test_case in range(1, T+1): # T만큼 반복.
    t_num = int(input()) # 테스트케이스의 번호를 입력받을 변수
    num_list = list(map(int, input().split())) # 숫자 정보들을 담을 변수

    cnt = 0 # 5까지 숫자를 늘려나갈 카운트변수
    while num_list[-1] != 0: # 마지막 숫자가 0이면 종료하는 while
        cnt += 1 # 반복할때마다 cnt를 +1 해준다.
        
        num_list[0] = num_list[0] - cnt # 첫번째 인덱스에서 cnt만큼 빼주고
        num_list.append(num_list.pop(0)) # 마지막 인덱스로 옮겨준다.

        if num_list[-1] < 0: # 마지막 인덱스의 숫자가 0 이하일때
            num_list[-1] = 0 # 0으로.
        
        if cnt > 4: # cnt가 5이상이면
            cnt = 0 # 0으로.

    print(f'#{t_num}',end=' ') # 출력
    for i in num_list:
        print(i, end=' ')
    print()