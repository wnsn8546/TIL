# https://www.acmicpc.net/problem/9012

T = int(input())

for test_case in range(0, T):
    PS_list = list(input().rstrip()) # rstrip으로 개행문자를 먼저 지우고 리스트로변환한다.
    flag = 0 # 한번도 짝이 없을때를 위한 flag변수

    while True: 
        for i in range(0, len(PS_list)-1):# PS_list의 길이만큼 계속 반복한다.
            if PS_list[i] == '(' and PS_list[i+1] == ')':# i번째, i+1번째가 각각 '(', ')'이면,
                PS_list.pop(i) # i 번째를 짝으로해서 두 번 꺼낸다.
                PS_list.pop(i)
                break # 이번 for문을 break로 끝내고, 다시 반복한다.
        else: # i번째를 돌때, 한번도 짝이 없으면 -1로 저장한뒤, break
            flag = -1
            break

    if flag == -1 and len(PS_list): # 괄호가 짝이안된상태이고, 길이가 남아있을때 'NO'출력
        print('NO')
    else:
        print('YES')