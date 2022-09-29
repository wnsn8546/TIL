# A, B, C를 한 줄씩 입력받고, A * B * C의 결과에 0부터 9가 몇번씩 쓰였는지?

A = int(input()) # A를 입력받는다.
B = int(input()) # B를 입력받는다.
C = int(input()) # C를 입력받는다.

nums = str(A * B * C) # A, B, C를 곱한 결과를 저장하고,
# str로 형변환해서 순회가 가능하게 해준다. 
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 ~ 9까지 몇번씩 쓰였는지를 저장할 리스트.

for i in nums: # nums 의 숫자들을 차례대로 순회하고 해당 숫자의 result 인덱스위치에 +1씩 해준다.
    result[int(i)] += 1
# 출력한다.
for i in result:
    print(i)