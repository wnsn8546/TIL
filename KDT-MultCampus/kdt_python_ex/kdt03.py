#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
#sum() 함수 사용 금지
#Input 10 Output 55

n = int(input())

#1) While
i = 1
sum1 = 0

while i <= n:
    sum1 += i
    i += 1
print(sum1)

#2) for
sum2 = 0

for j in range(1,n+1):
    sum2 += j
print(sum2)