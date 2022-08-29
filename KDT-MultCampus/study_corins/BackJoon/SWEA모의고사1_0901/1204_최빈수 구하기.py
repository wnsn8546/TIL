# 최빈수를 출력하는 프로그램을 작성하여라.
# (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.
# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

T = int(input()) # 테스트케이스 개수

for test_case in range(T): # 테스트 개수만큼 반복한다.
    case_num = int(input()) # 테스트 케이스의 번호
    score = list(map(int, input().split())) # 점수들을 리스트로 받는다.

    score_dict = {} # 빈도수를 저장할 딕셔너리
    for i in score: # score를 순회하면서
        if i in score_dict: # 딕셔너리에 넣어준다.
            score_dict[i] += 1
        else:
            score_dict[i] = 1
    mode = max(score_dict.values()) # 딕셔너리에서 최빈도를 찾아준다.

    result = [] # 최빈값을 가진 점수들을 넣어줄 리스트변수
    for k, v in score_dict.items(): # 딕셔너리를 순회하면서
        if score_dict[k] == mode: # 최빈도와 같은 값이나오면 리스트에 추가한다.
            result.append(k)
    result = sorted(result, reverse=True) # 내림차순으로 정렬하고,
    print(f'#{case_num}', result[0]) # 첫번째 값을출력한다.