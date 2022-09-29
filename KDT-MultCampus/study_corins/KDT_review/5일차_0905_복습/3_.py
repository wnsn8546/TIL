# 암호문 SWEA KDT 모의고사
# . I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
# 총 10개의 테스트 케이스가 주어진다.

import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T+1):
    original_length = int(input())
    original_text = list(input().split())
    order_num = int(input())
    order_text = list(input().split())
    result = original_text[:]
    x = 0
    y = 0

    for i in range(len(order_text)):
        if order_text[i] == 'I':
            x = int(order_text[i+1])
            y = int(order_text[i+2])

            for j in range(y):
                result.insert(x+j, order_text[i+3+j])
    result_len = len(result)

    print(f'#{test_case}', end=' ')
    if result_len >= 10:
        for i in range(10):
            print(result[i], end=' ')
    else:
        for i in range(len(result_len)):
            print(result[i], end=' ')