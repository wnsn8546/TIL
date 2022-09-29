# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다. 
# 각 테스트 케이스마다 주어진 문자열을 거울에 비춘 문자열로 출력한다.

T = int(input()) # 테스트 케이스 개수를 입력받는다.
mirror_dimension = {'b': 'd', 'd': 'b', 'p': 'q','q': 'p' } # 미리 거울상을 딕셔너리로 만들어준다.

for test_case in range(T): # 테스트케이스만큼 반복
    strings = input()[::-1] # 문자열을 받고, 순서를 역순으로 저장해놓는다.
    
    print(f'#{test_case+1} ', end='') # 출력형식
    for i in range(len(strings)): # strings 를 순회하면서
        if strings[i] in mirror_dimension: # 딕셔너리에 해당하는 문자면 바꿔서 출력
            print(mirror_dimension[strings[i]], end='')
        else: # 아니면 그대로 출력한다.
            print(strings[i], end='')
    print() # 개행