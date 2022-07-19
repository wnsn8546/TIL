# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
# Input 1234
# Output 4321

n = int(input())
my_list = []
result = []

while n:
    my_list.append(n%10)
    n //= 10

for i in my_list:
    print(i, end='')
