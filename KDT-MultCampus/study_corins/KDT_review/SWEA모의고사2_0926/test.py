# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 단, N은 홀수이다. 
# 그 다음 N개의 줄에는 정수들이 주어진다. 
# 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
number_dict = {}
for i in range(N):
    num = int(input())
    numbers.append(num)
    if num not in number_dict:
        number_dict[num] = 1
    else:
        number_dict[num] += 1

numbers = sorted(numbers)
avg = round(sum(numbers) / N)
mid_value = numbers[len(numbers) // 2]
r_num = numbers[-1] - numbers[0]
max_mod = max(number_dict.values())
mod_list = []
for k,v in number_dict.items():
    if v == max_mod:
        mod_list.append(k)
mod_list = sorted(mod_list)
print(avg)
print(mid_value)
if len(mod_list) > 1:
    print(mod_list[1])
else:
    print(mod_list[0])
print(r_num)