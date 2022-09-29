# https://www.acmicpc.net/problem/4150
# 정수를 입력받아, 그에 해당하는 피보나치 수를 출력하는 프로그램을 작성하여라.

def fibonacci(N):
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

N = int(input())
print(fibonacci(N))