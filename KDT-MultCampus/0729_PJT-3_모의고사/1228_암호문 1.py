import sys
sys.stdin = open("input1.txt", "r")

#0~999999 
# |x,y,s x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
#출력 : #케이스번호 공백 수정된 암호문의 처음 10개항 출력
T = 10

for test_case in range(T):
    length_original = int(input()) # 원본 길이
    original_text = list(input().split()) # 원본
    length_order = int(input()) # 명령어 길이
    order_text = list(input().split()) # 명령어
    result = original_text # 결과
    x = ''
    y = ''
    for i in range(0, len(order_text)): # 명령문의 개수만큼 반복
        if order_text[i] == 'I': # I를 만났을때 x, y값 할당
            x= int(order_text[i+1])
            y = int(order_text[i+2])
                
            for k in range(0, y): # y개수 만큼 리스트에 추가
                if x > length_original:
                        break
                result.insert(x+k, order_text[i+3+k])
                
    print(f'#{test_case+1}',end=' ') # 출력
    for i in range(0, 10):
        print(result[i], end=' ')
    print()