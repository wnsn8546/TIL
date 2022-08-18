# 첫째 줄에 교과서의 수 N, 교과서 더미의 수 M이 주어진다.
# 둘째 줄부터 2 * M줄에 걸쳐 각 더미의 정보가 주어진다.
# i번째 더미를 나타내는 첫 번째 줄에는 더미에 쌓인 교과서의 수 ki 가 주어지며, 두 번째 줄에는 ki 개의 정수가 공백으로 구분되어 주어진다.
# 올바른 순서대로 교과서를 꺼낼 수 있다면 Yes를, 불가능하다면 No를 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N, M을 입력 받는다.
book_list = [] # 책더미의 정보를 저장할 리스트

for _ in range(M): # M만큼 반복하면서
    ki = int(input()) # 책더미별 책 개수와
    book_list.append(list(map(int, input().split()))) # 책순서 정보를 받는다.

cnt = 0 # 순서가 맞지않는 경우를 카운트할 변수
for i in range(M): # 2중 반복문으로 전체를 순회하면서
    for j in range(len(book_list[i])-1):
        if book_list[i][j] < book_list[i][j+1]: # 밑에 있는 책의 숫자가 위에 있는 책보다 크면
            print('No') # 'No'를 출력하고 
            cnt += 1 # 카운트변수를 +1해주고
            break # break 해준다.
    if cnt != 0: # 한번이라도 발견했으면 i for문에서도 beak를 해준다.
        break
else: # 전체 책 순서가 잘 맞았으면,
    print('Yes') # 'Yes'를 출력. 