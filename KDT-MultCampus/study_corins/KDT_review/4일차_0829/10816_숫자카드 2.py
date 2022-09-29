# 첫째 줄에 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어진다. 
# 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력

N = int(input()) # N을 입력받는다.
card_list = list(map(int, input().split())) # N개의 카드를 입력받는다.
M = int(input()) # M을 입력받는다.
number_list = list(map(int, input().split())) # M개의 숫자를 입력받는다.

card_dict = {} # 빈도수를 저장할 딕셔너리를 만든다.
for card in card_list: # card_list를 순회하면서
    if card not in card_dict: # 딕셔너리에 없었으면 값을 1로,
        card_dict[card] = 1
    else:
        card_dict[card] += 1 # 있었으면 값을 += 1 을 해준다

for num in number_list:
    if num not in card_dict:
        print(0, end=' ')
    else:
        print(card_dict[num], end=' ')