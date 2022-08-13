# https://www.acmicpc.net/problem/1357

X, Y = input().split()
print(int(str(int(X[::-1]) + int(Y[::-1]))[::-1]))
