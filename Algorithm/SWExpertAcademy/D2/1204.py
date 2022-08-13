import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    t_num = int(input())
    result = 0
    score_list = [0] * 101
    input_scores = list(map(int, input().split()))

    for i  in range(len(input_scores)):
        score_list[input_scores[i]] += 1
    max_score = max(score_list)

    for i in range(len(score_list)):
        if score_list[i] == max_score:
            result = i

    print(f'#{t_num} {result}')