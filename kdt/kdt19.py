# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지
# Input 123
# Output 3

number = int(input())
cnt = 1

while True:
    if number // 10 > 0:
        number = number // 10
        cnt += 1
    else:
        break

print(cnt)