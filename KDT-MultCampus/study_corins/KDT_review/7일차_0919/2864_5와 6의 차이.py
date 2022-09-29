# https://www.acmicpc.net/problem/2864
# 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
# 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 
# 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.
# 첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)
# 첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.

A, B = input().split() # 문자열로 입력받는다.
new_A = '' # 숫자를 바꾸고 저장해둘 변수
new_B = ''
min_sum = 0 # 합의 최솟값을 저장할 변수
max_sum = 0 # 합의 최댓값을 저장할 변수

for num in A: # 입력받은 A의 문자열을 순회하면서
    if num == '6': # 6일때
        new_A += '5' # 5로 바꿔서 새로운 변수에 합쳐준다.
    else:
        new_A += num # 아닐때는 그대로 합쳐준다.
for num in B:
    if num == '6':
        new_B += '5'
    else:
        new_B += num
min_sum = int(new_A) + int(new_B) # 합의 최솟값을 int형으로 저장한다.

new_A = '' # 빈 문자열로 바꿔준다.
new_B = ''
for num in A:
    if num == '5':
        new_A += '6'
    else:
        new_A += num
for num in B:
    if num == '5':
        new_B += '6'
    else:
        new_B += num
max_sum = int(new_A) + int(new_B) # 합의 최댓값을 int형으로 저장한다.

print(min_sum, max_sum) # 출력한다.