# 첫째 줄에 8개 숫자가 주어진다. 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

ascending_list = [1, 2, 3, 4, 5, 6, 7, 8] # 어센딩 리스트를 만들어 놓는다.
descending_list = [8, 7, 6, 5, 4, 3, 2, 1] # 디센딩 리스트를 만들어 놓는다.

input_list = list(map(int, input().split())) # 음 리스트를 입력받는다.

if input_list == ascending_list: # 어센딩리스트와 같다면,
    print('ascending')
elif input_list == descending_list: # 디센딩리스트와 같다면,
    print('descending')
else: # 둘 다 아니라면,
    print('mixed')