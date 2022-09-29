def binary_search(N_list, target): # 이진탐색 함수구현
    left = 0
    right = len(N_list)-1

    while left <= right:
        mid = (left + right) // 2

        if target == N_list[mid]:
            return 1
        elif target < N_list[mid]:
            right = mid-1
        else:
            left = mid+1
    return 0

N = int(input()) # 정수 N을 입력받는다.
N_list = list(map(int, input().split())) # 해당 리스트정보를 입력받는다.
M = int(input()) # 정수 M을 입력받는다.
M_list = list(map(int, input().split())) # 해당 리스트정보를 입력받는다.

N_list = sorted(N_list) # 탐색될 리스트를 정렬하고
for i in M_list: # 탐색해야할 숫자들을 순회한다.
    print(binary_search(N_list, i)) # 이진탐색 함수를 호출, 리턴값을 출력한다.