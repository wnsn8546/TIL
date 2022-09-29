# https://www.acmicpc.net/problem/2930

R = int(input())
sang = input()
friend = int(input())
friend_list = []
for i in range(friend):
    friend_list.append(input())

score = 0
max_score = 0
for i in range(len(friend_list)):
    for j in range(R):
        if sang[j] > friend_list[i][j]:
            