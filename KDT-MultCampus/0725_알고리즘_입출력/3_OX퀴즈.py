# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for test_case in range(1, T + 1):
    score = 0
    continuity = 0
    case = input()

    for char in case:
        if char == 'O':
            continuity += 1
        else:
            continuity = 0
        score += continuity
    print(score)