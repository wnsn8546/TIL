# 첫 줄에 테스트 케이스의 개수가 주어진다.
# O, X 가 나열된 문자열을 입력받는다.
# O가 연속으로 나오면 +1점씩 추가로 받는다.

T = int(input()) # 테스트케이스의 개수

for test_case in range(1, T+1): # 테스트케이스의 개수만큼 반복
    input_str = input() # 입력받는 문자열
    score = 0 # 점수를 계산해서 출력할 변수
    cnt = 0 # 'O'가 몇번 연속으로 나오는지를 매번 카운트할 변수

    for i in range(len(input_str)): # 입력받은 문자열을 순회한다.
        if input_str[i] == 'O': # 해당 인덱스의 문자가 'O'이면
            cnt += 1            # cnt를 +1 해주고
            score += cnt        # cnt 만큼의 점수를 score에 더해준다.
        else:                   # 그렇지 않을때에는, cnt를 0으로 초기화해준다.
            cnt = 0
    print(score) # 지금까지 더해준 점수를 출력한다.