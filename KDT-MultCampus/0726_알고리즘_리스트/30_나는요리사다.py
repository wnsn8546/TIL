# https://www.acmicpc.net/problem/2953

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))

score_board = []

score_board.append(sum(a))
score_board.append(sum(b))
score_board.append(sum(c))
score_board.append(sum(d))
score_board.append(sum(e))

max_score = max(score_board)

print(score_board.index(max_score) + 1, max_score)