# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD&categoryId=AV14eWb6AAkCFAYD&categoryType=CODE&problemTitle=1218&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
#부호와 함께 테스트 케이스의 번호를 출력하고,
#  공백 문자 후 유효성 여부를 1 또는 0으로 표시한다 
# (1 - 유효함, 0 - 유효하지 않음).
import sys
sys.stdin = open("input.txt", "r")

T = 10

brakets_dict = {
    ')':'(',
    '}':'{',
    ']':'[',
    '>':'<',
}

for test_case in range(T):
    test_case_lentgh = int(input())
    test_input = input()
    result = 1
    
    stack_list = []
    for i in test_input:
        if i not in brakets_dict:
            stack_list.append(i)
        else:
            if stack_list[-1] != brakets_dict[i]:
                result = 0
                break
            else:
                stack_list.pop(-1)
    print(f'#{test_case+1} {result}')