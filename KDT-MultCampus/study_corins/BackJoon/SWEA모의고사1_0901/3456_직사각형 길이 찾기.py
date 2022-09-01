# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 네 변 중에서 세 변의 길이가 주어진다.
# 홀 수개인 변의 길이가 답이다.

T = int(input()) # 테스트 개수

for test_case in range(T): # 테스트케이스 만큼 반복
    input_list = list(map(int, input().split())) # 세 변의 길이 입력
    my_dict = {} # 담아둘 딕셔너리 변수

    for i in input_list: # input_list를 순회하면서 딕셔너리를 채워준다.
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for k, v in my_dict.items(): # 딕셔너리를 순회하면서
        if v % 2 == 1: # v가 홀 수 인것이 답이다.
            print(f'#{test_case+1}', k) # 출력
            break