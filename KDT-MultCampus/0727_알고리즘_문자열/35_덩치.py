# https://www.acmicpc.net/problem/7568

# x, y 를 각각 비교하여 둘 다 크면 그 쪽이 덩치가 크다라고한다.
# 나보다 덩치큰사람이 k명일때, 내 등수는 k+1로 정의된다. 
# 같은 등수를 가진 사람이 여러명일 수 있다.
# 이름별로 나보다 덩치가 큰사람이 몇명인지 찾고 +1을 해준다.

N = int(input())
people_list = [] # 덩치 정보를 담을 리스트
result = [] # 등수 결과를 담을 리스트
# N번만큼의 사람들의 덩치정보를 input으로 받는다.
for i in range(N):
    people_list.append(list(map(int, input().split())))
    result.append(1) # 정보를 받을때 마다 기본등수를 1로 저장해줬다.
# for문으로 덩치 크기를 비교하고 자신이 몇등인지를 저장한다.
# 나의 키, 몸무게가 다 작으면 내 등수를 +1
for i in range(0,N-1):
    for j in range(i+1,N):
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            result[i] += 1
        elif people_list[i][0] > people_list[j][0] and people_list[i][1] > people_list[j][1]:
            result[j] += 1
# 답 출력       
for i in result:
    print(i, end =' ')