# 첫 줄에는 전체 사람의 수 N이 주어진다.
# N개의 줄에는 몸무게와 키를 나타내는 x와 y가 공백을 두고 입력받는다.
# 키와 몸무게가 다 크면 덩치가 더 크다 라고한다.
# 자신보다 덩치가 큰 사람이 k명이면 등수는 k+1이다. 각 사람의 등수를 출력하라.

N = int(input()) # 전체 사람의 수를 입력받는다.
dungchi_list = [] # 덩치정보를 저장해놓을 리스트
result = [1] * N # 등수들을 리스트로 저장해놓을 변수 기본이 1등.

for _ in range(N): # N번 반복해서 덩치정보들을 입력받는다.
    dungchi_list.append(list(map(int, input().split())))

for i in range(len(dungchi_list)-1): # 다음 인덱스와의 비교를 고려해서 len-1까지 순회한다.
    for j in range(i+1, len(dungchi_list)):
        # i가 더 덩치가 작아서 등수가 밀리면,
        if dungchi_list[i][0] < dungchi_list[j][0] and dungchi_list[i][1] < dungchi_list[j][1]:
            result[i] += 1
        # j가 등수가 밀리면,
        elif dungchi_list[i][0] > dungchi_list[j][0] and dungchi_list[i][1] > dungchi_list[j][1]:
            result[j] += 1
# 출력한다.
print(*result)