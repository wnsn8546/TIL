# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지
# Input apple   aeiou   zxcvb
# Output 2        5       0

word = input()
cnt = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)