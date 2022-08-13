import sys
sys.stdin = open("input.txt", "r")

# 네 변 중에서 세 변의 길이가 주어짐
T = int(input())

for test_case in range(T):
    result = 0 # 결과를 저장할 변수
    input_list = list(map(int, input().split())) # 입력받은 변의 길이들
    my_dict = {}

    for i in input_list: # 딕셔너리에 같은 숫자들이 몇번나왔는지 카운트
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for k, v in my_dict.items(): # 홀수개인것이 나머지 한변의 길이이다
        if v % 2 == 1:
            result = k
            break
        
    print(f'#{test_case+1}', result)