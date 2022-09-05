# 회사에 있는사람 https://www.acmicpc.net/problem/7785
# 첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106)
# 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. 
# "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

n = int(input())

my_dict = {}
for i in range(n):
    name, status = input().split()

    my_dict[name] = status

in_office_list = []
for k, v in my_dict.items():
    if my_dict[k] == 'enter':
        in_office_list.append(k)
    
in_office_list = sorted(in_office_list,reverse=True)

for i in range(len(in_office_list)):
    print(in_office_list[i])