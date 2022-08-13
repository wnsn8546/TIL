# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# Input banana apple kiwi
# Output   1     0     -1

word = input()
cnt=0
idx = -1

for i in word:
    if i == 'a':
        idx = cnt
        break
    cnt += 1
print(idx)

# 추가문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
# Input HappyHacking  banana    kiwi
# Output    1 6        1 3 5     

word = input()
idx = -1

for i in word:
    idx += 1
    if i == 'a':
        print(idx, end=' ')
