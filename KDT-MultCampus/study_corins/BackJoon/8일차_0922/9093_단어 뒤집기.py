# https://www.acmicpc.net/problem/9093
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
# 단, 단어의 순서는 바꿀 수 없다. 
# 단어는 영어 알파벳으로만 이루어져 있다.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다.
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

T = int(input()) # 테스트케이스의 개수

input_list = [] # 문장을 담을 리스트 변수
for i in range(T): #  테스트케이스 개수 만큼 반복
    input_list.append(input().split()) # 문장을 입력받고, 추가한다.

for i in range(T): # 테스트케이스 만큼 반복
    result = '' # 문자열을 합칠 변수, 케이스 마다 비워준다.
    for j in range(len(input_list[i])): # input_list를 순회하면서
        result += input_list[i][j][::-1] # result에 거꾸로 변환 후 합친다.
        result += ' ' # 띄어쓰기를 붙여준다.
    print(result) # 출력한다.