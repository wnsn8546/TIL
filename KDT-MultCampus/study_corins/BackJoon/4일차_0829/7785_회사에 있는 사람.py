# 첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. 
# 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다.
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

n = int(input()) # n을 입력받는다.
office_dict = {} # 이름과, 상태를 저장할 딕셔너리를 만든다.

for _ in range(n): # n번 반복해서 
    name, status = input().split() # 이름, 상태를 입력받는다
    office_dict[name] = status

result = [] # 결과를 저장할 변수
for k, v in office_dict.items(): # 딕셔너리를 순회하면서
    if office_dict[k] == 'enter': # 상태가 'enter'이면,
        result.append(k)            # result 리스트에 이름을 추가한다.
result = sorted(result, reverse = True) # sorted의 reverse 로 사전 역순으로 정렬한다.

for i in result: # 한 줄당 하나씩 출력한다.
    print(i)