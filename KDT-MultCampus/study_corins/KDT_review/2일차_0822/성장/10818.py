# 첫째 줄에 정수의 개수가 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 그중 최솟값과 최댓값을 공백으로 구분해 출력한다.

N = int(input()) # N을 입력받는다.
num_list = list(map(int, input().split())) # N개의 정수를 입력받고, list로 만들어준다.

print(min(num_list), max(num_list)) # min, max 함수를 이용해서 최솟값, 최댓값은 공백으로 구분해 출력한다.