# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
# Input 264, 14 Output 참 거짓
n = int(input())
if (n % 3 == 0) and (n % 2 == 0) :
    print('참')
else :
    print('거짓')