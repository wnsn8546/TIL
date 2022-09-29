#0~999999 
# |x,y,s 
# x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
# 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
# 두 번째 줄 : 원본 암호문
# 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
# 네 번째 줄 : 명령어
# 위와 같은 네 줄이 한 개의 테스트 케이스이며, 총 10개의 테스트 케이스가 주어진다.
#기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.
# import sys
# sys.stdin = open('input.txt', 'r', encoding='utf-8')
# input = sys.stdin.readline

T = 10 # 테스트케이스 개수

for test_case in range(1, T+1): # 테스트케이스 수만큼 반복
    original_length = int(input()) # 원본 길이
    original_text = list(input().split()) # 원본 내용
    order_num = int(input()) # 명령어 개수
    order_text = list(input().split()) # 명령어 내용
    result = original_text # 원본 복사
    x = 0 # x값을 저장할 변수
    y = 0 # y값을 저장할 변수

    for i in range(0, len(order_text)): # 명령문을 순회한다.
        if order_text[i] == 'I': # 명령문 시작
            x = int(order_text[i+1]) # 다음 인덱스가 x
            y = int(order_text[i+2]) # 그 다음 인덱스가 y

            for k in range(y): # y수 만큼 반복
                result.insert(x+k, order_text[i+3+k]) # insert로 넣어준다.
    result_len = len(result) # 수정된 암호문의 길이를 저장해놓고,

    print(f'#{test_case}',end=' ') # 출력형식
    if result_len >= 10: # 길이가 10이상이면
        for i in range(10): # 10까지 출력
            print(result[i], end=' ')
    else: # 10 미만이면
        for i in range(result_len+1): # 길이만큼만 출력
            print(result[i], end=' ')
    print() # 개행