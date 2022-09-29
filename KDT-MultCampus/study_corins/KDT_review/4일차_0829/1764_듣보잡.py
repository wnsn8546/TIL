# 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램.
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어진다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

N, M = map(int, input().split()) # N, M을 입력받는다.
name_dict = {} # 이름과 듣도 보도 못했을 경우를 저장할 딕셔너리를 만든다.

for _ in range(N): # N번 반복하면서 
    name = input()
    if name not in name_dict: # 기존에 없었으면 1로 만들어 추가해준다.
        name_dict[name] = 1

for _ in range(M):
    name = input()
    if name in name_dict: # 보도 못한사람이 듣도 못한사람이었으면,
        name_dict[name] += 1 # 1 더해준다.

result = [] # 결과를 저장할 변수
for k, v in name_dict.items(): # 딕셔너리를 순회하면서
    if v == 2: # 값이 2인 듣도 못한 사람이라면,
        result.append(k) # 리스트에 추가해준다.
result = sorted(result) # 사전순으로 정렬한다.

print(len(result)) # 몇개인지를 길이로 출력해주고,
for i in result: # 이름을 한 줄에 하나씩 출력해준다.
    print(i)