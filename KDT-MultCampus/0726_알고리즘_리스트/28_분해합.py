# https://www.acmicpc.net/problem/2231

N = int(input())

for number in range(1, N+1):
    number_list = (map(int, str(number)))
    result = number + sum(number_list)

    if result == N:
        print(number)
        break
    if number == N:
        print(0)