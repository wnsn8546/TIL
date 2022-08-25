import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 테스트케이스 갯수, 학생은 1000명, 0<=점수<=100, #1 최빈점수

for test_case in range(T):
    score_dict = {}
    case_num = int(input())
    score = list(map(int, input().split())) # 점수들의 리스트

    for i in score:# 점수들의 빈도를 score 리스트를 돌면서 딕셔너리에 저장
        if i in score_dict:
            score_dict[i] += 1
        else:
            score_dict[i] = 1
    mode = max(score_dict.values()) # 최빈값을 max함수로 value값들중에서 구한다.
    
    result = []
    for k, v in score_dict.items(): # 최빈값을 가진 점수들을 저장
        if score_dict[k] == mode:
            result.append(k)
    result = sorted(result, reverse=True) # 큰 수순으로 정렬
    print(f'#{case_num}', result[0]) # 제일 큰 수 출력