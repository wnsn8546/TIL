#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
#Input 5 Output 120

n = int(input())

#1) While
i = 1
result1 = 1

while i <= n:
    result1 *= i
    i += 1
print(result1)

#2) for
result2 = 1

for j in range(1,n+1):
    result2 *= j
print(result2)