# https://www.acmicpc.net/problem/2609

a, b = map(int, input().split())
largest_common_multiple = 1
greatest_common_divisor = 0
common_divisor = []
common_multiple = []
numbers = []

if a > b:
    small_number = b
else:
    small_number = a

for number in range(1, small_number + 1):
    if a % number == 0 and b % number == 0:
        common_divisor.append(number)
greatest_common_divisor = max(common_divisor)
print(greatest_common_divisor)

largest_common_multiple = a * b // greatest_common_divisor
print(largest_common_multiple)

# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))

# print(math.lcm(a, b))