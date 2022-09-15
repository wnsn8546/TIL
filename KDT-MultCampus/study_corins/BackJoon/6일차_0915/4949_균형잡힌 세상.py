# https://www.acmicpc.net/problem/4949
# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류
# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 
# 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 
# 길이는 100글자보다 작거나 같다. 각 줄은 마침표(".")로 끝난다.
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

import sys
input = sys.stdin.readline

while True:
    input_str = input().rstrip() # readline 으로 입력받기때문에, rstrip()을 사용해준다.
    if input_str == '.': # 종료조건인 '.'가 입력되면 while문을 종료한다.
        break
    
    left_brackets = ['(', '['] # 여는 괄호들을 담은 리스트
    right_brackets = [')', ']'] # 닫는 괄호들을 담은 리스트
    stack_list = [] # stack_list를 만들어준다.
    for i in input_str: # 입력받은 문자열을 순회하다가,
        if i in left_brackets: # 여는 괄호들을 만나면,
            stack_list.append(i) # stack_list에 추가하고,
        elif i in right_brackets: # 닫는 괄호들을 만나면,
            if len(stack_list) != 0 and left_brackets.index(stack_list[-1]) == right_brackets.index(i): # stack_list가 비어있지 않고, 인덱스가 같은지 쌍이맞는지를 확인하고,
                stack_list.pop() # 맞다면 pop을 한다.
            else: # 쌍이 맞지 않으면,
                stack_list.append(i) # 스택 리스트에 추가하고,
                break # break로 멈춘다.
    
    if len(stack_list) == 0: # 스택 리스트의 길이가 0이면,
        print('yes') # yes 출력
    else : # 0이 아니면,
        print('no') # no 출력