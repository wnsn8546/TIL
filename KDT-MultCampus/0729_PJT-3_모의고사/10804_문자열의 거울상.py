import sys
sys.stdin = open("input.txt", "r")

# b,d,p,q 문자들의 거울상을 먼저 딕셔너리로 만들어주고 문자열을 조작한다.
T = int(input())
mirror_dimension = {'b': 'd', 'd': 'b', 'p': 'q','q': 'p' }

for test_case in range(T):
    strings = input()[::-1] # 입력받은 문자들의 순서를 먼저 거꾸로하는부분
    strings = list(map(str, strings)) # 리스트로 만들어 문자열 바꾸기
    result = ''

    for i in range(len(strings)): # 거울상 딕셔너리에서 찾아 바꿔준다.
        if strings[i] in mirror_dimension:
            strings[i] = mirror_dimension[strings[i]]
            result += strings[i]
    print(f'#{test_case+1}', result)