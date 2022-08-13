# https://www.acmicpc.net/problem/5622

dial = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8,'TUV':9, 'WXYZ':10}
word = input()
result = 0

for char in word:
    for key in dial.keys():
        if char in key:
            result += dial[key]
print(result)