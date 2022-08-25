# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지
# Input numbers = [0, 20, 100] Output 20
# 추가 Input
# numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30


numbers = [0, 20, 100] # 20
#numbers = [0, 20, 100, 50, -60, 50, 100] # 50
#numbers = [0, 1, 0] # 0
#numbers = [-10, -100, -30] # -30

if numbers[0] > numbers[1]:
    max_first = numbers[0]
    max_second = numbers[1]
else:
    max_first = numbers[1]
    max_second = numbers[0]

for i in range(2, len(numbers)):
    if max_first < numbers[i]:
        max_second = max_first
        max_first = numbers[i]
    else:
        if ((max_second < numbers[i]) and (max_first > numbers[i])):
            max_second = numbers[i]
    
print(max_second)