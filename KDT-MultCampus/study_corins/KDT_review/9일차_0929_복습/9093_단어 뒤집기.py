# https://www.acmicpc.net/problem/9093

T = int(input())

for i in range(T):
    result = ''
    sentence = input().split()
    for letter in sentence:
        result += letter[::-1] + ' '
    print(result)