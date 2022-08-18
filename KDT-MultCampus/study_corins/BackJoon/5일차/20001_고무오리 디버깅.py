# 첫 번째 줄에 "고무오리 디버깅 시작"이라고 주어진다
# 두 번째 줄부터 "고무오리" 또는 "문제"가 주어진다.
# 고무오리를 받으면 최근 풀던 문제를 해결한다
# 풀 문제가 없는데 사용한다면 고무오리는 벌칙으 로 두 문제를 추가한다
# "고무오리 디버깅 끝"이 주어질 때까지 반복한다.
# 모든 문제를 해결하였으면 "고무오리야 사랑해"을 출력하고
# 하나라도 문제가 남았다면 "힝구"를 출력하라.

input_str = '' # 문자열을 입력 받을 변수
problem_dict = {} # 문제 개수를 저장할 딕셔너리

while input_str != '고무오리 디버깅 끝': # while문 반복조건
    input_str = input() # 문자열을 입력받는다.

    if input_str == '문제': # '문제'를 입력받으면
        if '문제' not in problem_dict: # 이전에 없었으면 값을 1로
            problem_dict['문제'] = 1
        else:
            problem_dict['문제'] += 1 # 있었으면 값 +1을 해준다.
    elif input_str == '고무오리': # '고무오리'를 입력 받으면
        if '문제' not in problem_dict or problem_dict['문제'] == 0: # 이전에 '문제'가 0이거나 없었으면 값을 2로 해준다.
            problem_dict['문제'] = 2
        else:
            problem_dict['문제'] -= 1 # 있었으면 -1을 해준다.

if problem_dict['문제']: # 문제가 남아있으면 '힝구'를 출력
    print('힝구')
else:
    print('고무오리야 사랑해') # 없으면 '고무오리야 사랑해'출력