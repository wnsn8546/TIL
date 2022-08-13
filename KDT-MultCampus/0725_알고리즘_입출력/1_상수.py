# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
reverse_a = int(a[::-1])
reverse_b = int(b[::-1])

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)