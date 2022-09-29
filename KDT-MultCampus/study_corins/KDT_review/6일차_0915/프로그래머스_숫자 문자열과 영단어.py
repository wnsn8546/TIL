# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = '' # 답을 저장할 변수
    temp = '' # 임시 변수
    my_dict = { # 문자, 숫자 까지 다 넣어놓고, 문자열로 변환받을 딕셔너리
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
    }
    
    for char in s: # s에서 한 글자씩 순회한다,
        temp += char # 임시변수에 하나씩 합치면서
        if temp in my_dict: # 딕셔너리에 있는 문자가 완성되면,
            answer += my_dict[temp] # answer 변수에 더해주고,
            temp = '' # 다시 비워준다.
            
    return int(answer) # int형으로 변환후 리턴한다.