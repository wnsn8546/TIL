# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
# 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다. 
# 첫째 줄에는 스위치 개수가 주어진다. 
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

N = int(input()) #스위치 개수
switches = list(map(int, input().split()))
s_num = int(input())
students = []
for _ in range(s_num):
    students.append(list(map(int, input().split())))
st1 = map(int,input().split()) # 성별 남1 여2, 받은숫자
st2 = map(int,input().split())

if st1[0] == 1:
