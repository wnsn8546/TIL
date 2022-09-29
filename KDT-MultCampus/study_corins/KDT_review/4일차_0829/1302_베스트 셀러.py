# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다.
# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다.
# 알파벳 소문자로만 이루어져 있다.
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다.
# 만약 가장 많이 팔린 책이 여러 개일 경우에는,
# 사전 순으로 가장 앞서는 제목을 출력한다.

N = int(input()) # 개수 N을 입력받는다.
sold_dict = {} # 책이름과, 팔린 부 수를 저장해 놓을 딕셔너리를 만든다.

for _ in range(N): # N개 만큼 반복
    book_name = input() # 책이름을 입력받고,

    if book_name not in sold_dict: # 기존에 없었으면 값을 1로,
        sold_dict[book_name] = 1 
    else:
        sold_dict[book_name] += 1 # 있었으면 값을 +1 해준다.
max_sold = max(sold_dict.values()) # 제일 큰 밸류를 찾아 저장해놓는다.

bestseller_list = [] # max_sold랑 같은 수로 팔린 책들을 저장해놓은 리스트.
for k, v in sold_dict.items(): # 딕셔너리를 순회하면서
    if v == max_sold:   # max_sold와 같은 밸류인 책을 찾으면,
        bestseller_list.append(k) # 리스트에 추가해준다.
bestseller_list = sorted(bestseller_list) # 사전순으로 정렬하고,

print(bestseller_list[0]) # 첫번째 책을 출력한다.