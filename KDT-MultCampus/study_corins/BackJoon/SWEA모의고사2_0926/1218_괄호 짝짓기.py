import sys
sys.stdin = open("input.txt", "r")

T = 10 # 테스트 케이스 10.
bracket_dict = { # 괄호들을 딕셔너리 형태로 저장해 둔다.
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

for test_case in range(1, T+1): # T만큼 반복.
    test_length = int(input()) # test케이스마다의 길이
    test_list = list(input()) # test케이스의 리스트 정보
    result = 1 # 유효성 여부 기본 1로.
    
    stack_list = [] # stack에 사용할 list
    for i in range(test_length): # test_case 리스트를 순회하면서
        if test_list[i] not in bracket_dict: # 여는 괄호일때는 stack에 추가해준다.
            stack_list.append(test_list[i])
        else: # 닫는 괄호일때는
            if stack_list[-1] == bracket_dict[test_list[i]]: # stack_list의 마지막 괄호와 짝이 맞다면
                stack_list.pop(-1) # 해당 여는 괄호를 제거해준다.
            else: # 짝이 맞지않다면,
                result = 0 # 유효성 여부를 0으로 하고
                break # 반복문을 종료한다.
    print(f'#{test_case} {result}') # 유효성여부를 출력한다.