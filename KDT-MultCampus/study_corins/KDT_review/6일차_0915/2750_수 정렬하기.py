# https://www.acmicpc.net/problem/2750
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수 주어진다.

# N = int(input())

# num_list = []
# for i in range(N):
#     num_list.append(int(input()))

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
# answer = quick_sort(num_list)
# for i in range(len(answer)):
#     print(answer[i])

N = int(input()) # N을 입력받는다.
numbers = [] # 숫자들을 저장할 리스트
result = [] # 결과를 저장할 리스트

for i in range(N): # N만큼 돌면서 숫자를 입력받는다.
    numbers.append(int(input()))

result = sorted(numbers) # 정렬하여 result변수에 넣는다.
for i in result: # 출력한다.
    print(i)