# 첫째 줄에서 두개의 자연수를 입력받고,
# 첫번째 줄에 두 수의 최대공약수를,
# 두번째 줄에 두 수의 최소 공배수를 출력한다.

A, B = map(int, input().split()) # A, B를 입력받는다.
common_divisor = [] # 공약수들을 넣을 리스트를 만든다.

if A > B: # 크기를 비교하여 둘 중 작은 수를 찾는다.
    small_number = B
else:
    small_number = A

for num in range(1, small_number + 1): # num을 1부터 작은수까지 순회한다.
    if A % num == 0 and B % num == 0:  # A, B를 num으로 나누었을때 나머지가 0이되면 공약수이므로,
        common_divisor.append(num)     # 공약수 리스트에 추가한다.
greatest_common_divisor = max(common_divisor) # 그 중 제일 큰 숫자가 최대 공약수이다.

print(greatest_common_divisor) # 최대공약수를 출력한다.
print(A * B // greatest_common_divisor) # 두 수의 곱을 최대공약수로 나눈 최소공배수를 출력한다.