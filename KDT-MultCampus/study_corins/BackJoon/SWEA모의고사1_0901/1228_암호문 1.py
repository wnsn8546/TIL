#0~999999 
# |x,y,s 
# x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
# 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
# 두 번째 줄 : 원본 암호문
# 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
# 네 번째 줄 : 명령어
# 위와 같은 네 줄이 한 개의 테스트 케이스이며, 총 10개의 테스트 케이스가 주어진다.
#기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.
import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline
T = 10 # 테스트케이스 개수

for test_case in range(T): # 테스트케이스 만큼 반복
    length_original = int(input()) # 원본 길이
    original_text = list(input().split()) # 원본
    length_order = int(input()) # 명령어 길이
    order_text = list(input().split()) # 명령어
    result = original_text # 결과
    x = '' # x를 담을 변수
    y = '' # y를 담을 변수

    for i in range(0, len(order_text)): # 명령문의 개수만큼 반복한다.
        if order_text[i] == 'I': # I를 만났을때 x, y값 할당한다.
            x = int(order_text[i+1])
            y = int(order_text[i+2])
                
            for k in range(0, y): # y개수 만큼 리스트에 추가
                if x > length_original:
                        break
                result.insert(x+k, order_text[i+3+k])
                
    print(f'#{test_case+1}',end=' ') # 출력
    for i in range(0, 10):
        print(result[i], end=' ')
    print()