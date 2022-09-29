# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.
# 셀프넘버 : 생성자가 없는숫자.

gen_list = [] # 생성자가 있는 숫자들 넣을 리스트

for i in range(1, 10001): # 1 ~ 10000 순회
    for j in str(i): # 생성자가 있는 숫자를 만들어서
        i += int(j) 
    gen_list.append(i) # 리스트에 넣어준다.

gen_list = set(gen_list) # 중복된 숫자들을 제거해준다.
for i in range(1, 10001): # 1~10001을 순회하면서
    if i not in gen_list: # 생성자가 있는 숫자들이 아니면
        print(i) # 출력한다.