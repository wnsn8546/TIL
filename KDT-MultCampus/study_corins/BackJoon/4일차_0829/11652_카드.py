# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.
# 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

N = int(input()) # N을 입력받는다.
card_dict = {} # 카드의 숫자와, 갯수를 저장할 딕셔너리를 만든다.

for _ in range(N): # N번 반복한다.
    card = int(input()) # 카드를 입력받는다.
    if card not in card_dict: # 카드가 기존에 없었으면
        card_dict[card] = 1 # 값을 1로 저장한다.
    else:
        card_dict[card] += 1 # 있었으면, +1을 해준다.
max_num = max(card_dict.values()) # 제일 많이 나온갯수를 찾는다.

max_list = [] # 제일 많이 나온갯수의 카드숫자를 저장할 리스트를 만든다.
for k, v in card_dict.items(): # 딕셔너리를 순회하면서
    if v == max_num:            # max_num과 같은 값의 카드를 찾으면,
        max_list.append(k)      # 리스트에 추가한다.
max_list = sorted(max_list)     # 정렬해준다.

print(max_list[0]) # 제일 작은 숫자를 출력한다.