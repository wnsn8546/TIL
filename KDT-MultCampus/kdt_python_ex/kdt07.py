#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
#min() 함수 사용 금지
# Input numbers = [0, 20, 100] Output 0
#추가 Input
# numbers = [0, 20, 100, 50, -60, 50, 100] # -60
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -100

numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # -60
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -100

min = numbers[0]

for i in range(1,len(numbers)):
    if min > numbers[i]:
        min = numbers[i]

print(min)