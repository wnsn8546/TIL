#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지
#Input numbers = [3, 10, 20] Output 11

numbers = [3, 10, 20]

l = 0
sum = 0

for i in numbers:
    l += 1
    sum += i

print(int(sum/l))