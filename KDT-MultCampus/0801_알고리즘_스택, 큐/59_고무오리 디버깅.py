# https://www.acmicpc.net/problem/20001

word = ''
problems = []

while word != '고무오리 디버깅 끝':
    word = input()
    if word == '고무오리 디버깅 시작':
        while word != '고무오리 디버깅 끝':
            word = input()
            if word == '문제':
                problems.append('문제')
            elif word == '고무오리':
                if '문제'in problems:
                    problems.pop()
                else:
                    problems.append('문제')
                    problems.append('문제')
if len(problems) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')